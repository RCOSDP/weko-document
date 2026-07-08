# JDCat マスタデータ移行プログラム 利用者マニュアル

対象システム: Weko3（JDCatインスタンス）
対象作業: develop_v1.0.8系（＋JDCat固有対応 `feature/jdcat_202601`）→ develop_v2.0.0 へのバージョンアップに伴うマスタデータ移行

| 項目 | 内容 |
|---|---|
| 要求仕様 | 要求仕様：J2026-01_v4.docx |
| 設計書 | [JDCat マスタデータ移行プログラム 設計書](JDCat_Master_Data_Migration_Design_Spec.md) |
| 関連資料（別紙） | [別紙_v3.xlsx](attachments/別紙_v3.xlsx)（NII様提供資料。別紙1〜3を各シートに収録） |
| English version | [User Manual (English)](JDCat_Master_Data_Migration_Tool_Manual_en.md) |

本書は、移行プログラム一式（`scripts/demo/jdcat_migration/`）の**利用者向け操作手順**をまとめたものである。プログラムの設計思想・処理内容の詳細は[設計書](JDCat_Master_Data_Migration_Design_Spec.md)を参照すること。本書は設計書 **5章「プログラム構成」** を中心に、各ツールの実行方法を具体的に記載する。

---

# 1. このプログラムでできること

JDCat（Weko3）を `develop_v1.0.8` 系から `develop_v2.0.0` へバージョンアップする際に必要となる、**マスタデータ（`item_type` / `item_type_property` / `item_type_mapping`）の移行**を行う。

- 対象 item_type は **12（Multiple）/ 20（Harvesting DDI）** のみ。
- 変換ルールは外部設定ファイル `mapping_config.json` に集約された**設定駆動**方式。
- `item_type_property` を TRUNCATE しない**非破壊**・再実行可能な**冪等**方式。
- **登録済みメタデータ（`item_metadata` / `records_metadata`）は変換しない**。移行後、OAI-PMH / ResourceSync による**再ハーベスト**で v2.0.0 構造のメタデータが再生成される（設計書 2.4）。

> ⚠️ **注意**: 本プログラムはマスタデータのみを扱う。メタデータの再取得（再ハーベスト）は本プログラムの対象外であり、移行完了後に別途実施する。

---

# 2. 前提・実行環境

## 2.1 実行場所

移行本体（`migrate.py`）と開発補助ツール（`gen_properties.py`）は **Weko の web コンテナ内**で `invenio shell` を通じて実行する。設定ファイル生成ツール（`convert_xlsx.py`）は **DB非依存・stdlib のみ**のため、コンテナ外の素の `python3` でも実行できる。

| ツール | 実行場所 | DB接続 |
|---|---|---|
| `convert_xlsx.py` | 任意（素の `python3` で可） | 不要 |
| `gen_properties.py` | web コンテナ内（`invenio shell`） | 必要（開発時のみ） |
| `migrate.py` | web コンテナ内（`invenio shell`） | 必要 |

## 2.2 プログラムの配置

移行プログラム一式を、Weko 本体の `scripts/demo/jdcat_migration/` 配下に配置する（web コンテナからは `/code/scripts/demo/jdcat_migration/` として見える）。

```
scripts/demo/jdcat_migration/
  __init__.py
  config.py          # mapping_config.json の読込・スキーマ検証・整合チェック
  convert_xlsx.py    # xlsx回答 → mapping_config.json
  gen_properties.py  # DB → properties/*.py ドラフト生成（開発時）
  engine.py          # 変換エンジン本体（フェーズ1〜3）
  migrate.py         # CLIエントリ（invenio shell から実行）
  report.py          # dry-run / 進捗 / 事後検証レポート
```

## 2.3 【重要】invenio shell と引数の渡し方

`invenio shell` の実体は **IPython** であり、`--config` などの `--` フラグを **IPython 自身が横取りしてしまう**（スクリプトへ届かない）。このため、`invenio shell` 経由で実行する `migrate.py` / `gen_properties.py` では、**引数を環境変数（`JDCAT_*`）で渡す**（IPython は環境変数を触らない）。

- `invenio shell` 経由（本番の実行方法） → **環境変数で渡す**（`docker compose exec -e ...`）。
- 素の `python` 実行（開発時、app context が別途必要） → `--` フラグが使える。

以降のコマンド例はこの前提に従う。

---

# 3. 全体の流れ

```
[1] convert_xlsx.py … 記入済みxlsx → mapping_config.json を生成
        │
       （必要な場合のみ）
[2] gen_properties.py … 新設プロパティの properties/*.py ドラフトを生成（開発時）
        │
[3] 事前準備 … DBバックアップ取得（pg_dump 等・手動）
        │
[4] migrate.py --dry-run … DB無更新で想定変更を事前確認
        │
[5] migrate.py（本実行） … Phase1〜3 を適用
        │
[6] レポート確認 … 総合判定・旧キー残0件・未知プロパティ参照0件 を確認
```

- **[2] は通常スキップ可**。新設プロパティのドラフト `.py` を作りたい開発時のみ使用する（設計書 4.2）。
- **[3][4] は本実行前に必ず実施**する（設計書 5.3）。

---

# 4. 実行方法

## 4.1 convert_xlsx.py（記入済みxlsx → 設定JSON生成）

NII様に記入いただいた `マッピング必要データ_XXXXXXXX.xlsx` を、移行プログラムの実入力である `mapping_config.json` に変換する。

### 入力・出力

- **入力**: 記入済み `マッピング必要データ_XXXXXXXX.xlsx`（`item` / `property` シート）
- **出力**: `mapping_config.json`（設計書 3.2 のスキーマ）

### 実行コマンド

DB非依存・stdlib のみのため、素の `python3` で単体実行できる。

```bash
python3 convert_xlsx.py マッピング必要データ_20260423.xlsx mapping_config.json \
    --item-types 12,20
```

| 引数 | 説明 |
|---|---|
| 第1引数（`input`） | 記入済み `マッピング必要データ_*.xlsx`（必須） |
| 第2引数（`output`） | 出力する `mapping_config.json` のパス（必須） |
| `--item-types` | 対象item_type（カンマ区切り。既定 `12,20`） |

### 出力・警告の確認

- 標準エラーへ処理結果と警告を出力する。正常時は末尾に `OK: ... を出力（property_id_map N件 / item_key_map {...}）` が表示される。
- 未記入（`#N/A`）・不整合（旧id/新idが整数でない、prop_name が識別子形式でない、キー重複 等）は `[WARN]` として、シート欠落・ヘッダ不足などの致命的問題は `[ERROR]` として出力される。**`[ERROR]` がある場合は変換に失敗し、終了コード 1** を返す。警告は内容を確認のうえ、必要ならxlsxを修正して再実行する。

> 生成された `mapping_config.json` は運用成果物であり、Weko リポジトリの管理対象外。移行本体（`migrate.py`）はこの JSON のみを参照して動作する。

<br/>

## 4.2 gen_properties.py（プロパティ定義 .py のドラフト生成・開発時）

現状DBの `item_type_property` を雛形に、既存 `properties/*.py` と同契約のドラフト `.py` を生成する**開発時の補助ツール**。生成時に subitemキーを変換マップで置換する。**移行本体（Phase1〜3）では使用しない。**

> ℹ️ **通常運用ではこのツールを使う必要はない**。既存標準にプロパティが揃っている場合は既存 `properties/*.py` を用いる。本ツールの主用途は「新設」プロパティのドラフト生成であり、生成物はあくまで**たたき台**（別紙2・別紙3 を見て手修正・検証する前提）である（設計書 4.2）。

### 入力・出力

- **入力**: DB接続、対象 property_id、subitemキー変換マップ（任意）、出力先ディレクトリ
- **出力**: `properties/*.py` と同体裁のドラフト `.py`（UTF-8）。`mapping` は DB に無いため `DEFAULT_MAPPING` を仮置き。

### 実行コマンド（invenio shell 経由・環境変数入力）

```bash
docker compose exec \
    -e JDCAT_GEN_IDS=1042,305 \
    -e JDCAT_GEN_OUT=scripts/demo/jdcat_migration/_gen \
    -e JDCAT_GEN_SUBITEM=scripts/demo/jdcat_migration/subitem_map.json \
    web invenio shell scripts/demo/jdcat_migration/gen_properties.py
```

| 環境変数 | 説明 |
|---|---|
| `JDCAT_GEN_IDS` | 生成対象 property_id（カンマ区切り。**必須**） |
| `JDCAT_GEN_OUT` | 出力ディレクトリ（**必須**。無ければ作成） |
| `JDCAT_GEN_SUBITEM` | subitemキー変換マップ（`.json`＝`{旧:新}` または `.xlsx`）。任意 |
| `JDCAT_GEN_SUBITEM_SHEET` | xlsx時のシート名（既定 `subitem`） |

### 生成後の作業

1. 生成された `.py` の先頭には `★GENERATED DRAFT（要手修正）★` が付く。
2. `mapping`・`name_en`・`multiple_flag` はDBから確定できないため、別紙2・別紙3 を見て**手修正・検証**する。
3. 確定した `.py` を `properties/` 配下へ置き、`properties/__init__.py` に取り込むと、`migrate.py` の **Phase1 で自動的に登録**される。
4. 補助として、生成物と既存標準 `properties/*.py` を diff すれば「現状DB構造 vs v2.0.0標準」のズレを確認できる。

<br/>

## 4.3 migrate.py（移行本体）

`mapping_config.json` を入力に、対象 item_type（12/20）のマスタデータを v2.0.0 形へ移行する。

### 4.3.1 実行前の準備（設計書 5.3）

本実行の前に、運用手順として次を必ず実施する。

1. **DBバックアップ取得**（手動・本プログラム対象外）: 対象テーブル（`item_type` / `item_type_mapping` / `item_type_property`）を `pg_dump` 等で取得する。異常時はここからリストアする。
2. **dry-run で事前確認**（次項）: DB無更新で設定JSONの検証・想定変更内容を確認する。

### 4.3.2 dry-run（DB無更新の事前確認）

まず必ず dry-run で想定変更を確認する。

```bash
docker compose exec \
    -e JDCAT_CONFIG=scripts/demo/jdcat_migration/mapping_config.json \
    -e JDCAT_ITEM_TYPES=12,20 \
    -e JDCAT_PHASE=all \
    -e JDCAT_DRY_RUN=1 \
    web invenio shell scripts/demo/jdcat_migration/migrate.py
```

### 4.3.3 本実行

dry-run の内容に問題が無ければ、`JDCAT_DRY_RUN` を外して（または `0` にして）本実行する。

```bash
docker compose exec \
    -e JDCAT_CONFIG=scripts/demo/jdcat_migration/mapping_config.json \
    -e JDCAT_ITEM_TYPES=12,20 \
    -e JDCAT_PHASE=all \
    web invenio shell scripts/demo/jdcat_migration/migrate.py
```

### 4.3.4 環境変数一覧

| 環境変数 | 説明 |
|---|---|
| `JDCAT_CONFIG` | 設定JSON（`mapping_config.json`）のパス（**必須**） |
| `JDCAT_ITEM_TYPES` | 対象item_type（カンマ区切り。既定は設定の `target_item_types`） |
| `JDCAT_PHASE` | 実行フェーズ `all` / `1` / `2` / `3` / `pre`（既定 `all`） |
| `JDCAT_DRY_RUN` | `1`/`true`/`yes` で dry-run（DB無更新） |
| `JDCAT_CLEANUP` | `1`/`true`/`yes` で Phase3 の論理削除（opt-in） |
| `JDCAT_REPORT_OUT` | レポート出力先ファイル（未指定は標準出力／ログ） |

- `JDCAT_PHASE` の `pre` は実行前検証（設定JSON × DB）のみを行う。`1`/`2`/`3` は各フェーズ単独実行。
- `JDCAT_CLEANUP` は、どの item_type からも参照されなくなった JDCat 独自プロパティを論理削除（`delflg=true`）する。既定では実行しない（opt-in）。

### 4.3.5 処理フェーズの概要（設計書 6章）

| フェーズ | 内容 |
|---|---|
| Phase 1 | properties（非破壊UPSERT）。`properties/` の定義から v2.0.0 標準プロパティを UPDATE で更新。独自プロパティは残置。 |
| Phase 2 | itemtype。`render` の `cus_<旧id>` → `cus_<新id>` 置換（③）、旧itemキー → 新itemキー置換（①）、`ItemTypes.reload()` でプロパティ定義を反映。 |
| Phase 3 | verify & cleanup。旧キー残存0件・未知プロパティ参照0件 を検証。（opt-in で独自プロパティを論理削除） |

- `migrate.py` は実行全体を try/finally で囲み、`weko_records` の `Timestamp.before_update` リスナーを一時解除→復元する（マスタテーブルの `updated` 列を汚さないため）。

### 4.3.6 素の python 実行（開発時のみ）

app context が別途用意できる開発環境では `--` フラグが使える。

```bash
python migrate.py --config mapping_config.json --item-types 12,20 \
    --phase all --dry-run
```

| 引数 | 対応する環境変数 |
|---|---|
| `--config` | `JDCAT_CONFIG` |
| `--item-types` | `JDCAT_ITEM_TYPES` |
| `--phase` | `JDCAT_PHASE` |
| `--dry-run` | `JDCAT_DRY_RUN` |
| `--cleanup` | `JDCAT_CLEANUP` |
| `--report-out` | `JDCAT_REPORT_OUT` |

---

# 5. レポートの見方

`migrate.py` は実行後にテキストレポートを出力する（`JDCAT_REPORT_OUT` 指定時はファイルへ、未指定時は標準出力／ログへ）。主な確認ポイントは次のとおり。

- **モード**: `dry-run（DB無更新）` か `本実行` か。
- **実行前検証（設定JSON × DB）**: `[ERROR]` があると移行は中断される。`[WARN]` は内容を確認する。
- **Phase1**: UPSERT対象の件数（追加／更新）。対象が無い場合は「対象なし」と明記される。
- **Phase2**: item_type ごとに ③（プロパティID変換）件数・①（itemキー変換）件数、`reload` の結果コード。「変換済み/冪等スキップ」表示は既に移行済みの意味。
- **Phase3**: item_type ごとに `OK`/`NG`、**旧キー残存件数**・**未知プロパティ参照件数**。両方 0 かつ `OK` が正常。
- **総合判定**: 末尾に `dry-run 完了` / `本実行 完了` と「問題は検出されませんでした」もしくは要確認事項が表示される。

> ✅ 移行成功の目安: 総合判定が「問題は検出されませんでした」、Phase3 が全 item_type で `OK`（旧キー残0件・未知プロパティ参照0件）。

---

# 6. 再実行・トラブル時の対応（設計書 7章）

- **冪等**: Phase1 は UPDATE、Phase2 はキー形式で「変換済み」を判定してスキップするため、**何度実行しても安全**。dry-run → 本実行の順で進める。
- **エラー時のロールバック**: 処理中にエラーが発生した場合、当該トランザクションはロールバックされ、DBは変更前の状態に保たれる。通常のエラーはこれで回復し、冪等な再実行で続行できる（リストア不要）。
- **バックアップからのリストア**: トランザクションのロールバックや再実行で回復できない**想定外の事態**（部分コミット後の不整合・データ破損等）に備えた**最終手段**。事前取得したバックアップ（4.3.1）からリストアする。

---

# 7. 移行後の作業

- マスタデータ移行の完了後、**メタデータは OAI-PMH / ResourceSync による再ハーベスト**で v2.0.0 構造として再取得される（本プログラム対象外。設計書 2.4）。
- 移行本体はマスタデータ（`item_type` 定義・mapping・プロパティ）を整えることに専念しており、メタデータ個別変換は行わない点に留意する。
