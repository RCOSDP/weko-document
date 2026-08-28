# feature/jgss-pre から v2.0.3 へのアップデート方法（docker-compose 版）

JGSS（大阪商業大学 JGSS 研究センター）向けカスタマイズを施した `feature/jgss-pre` で稼働している環境を
`v2.0.3` へアップデートし、データをマイグレーションする手順である。

> **重要 — 本移行は「v1.0.x → v2.0.3」ではない。実体は `v0.9.21 → v2.0.3` である。**
> コミット日付（2024-04）ではなく、リポジトリの資産集合と祖先タグから起点を同定した（1 章）。
> 途中の v0.9.22 / v0.9.26 / v0.9.27 / v1.0.6 / v1.0.7a2 の各移行手順が**すべて必要**になる。

> **本手順書の位置づけ**
> 既存の公式手順書を、本移行のパスに沿って接続したものである。各段階の詳細は原典を参照すること。
>
> | 段階 | 原典 |
> | --- | --- |
> | v0.9.2x | [`v0.9.17_to_v0.9.26.md`](./v0.9.17_to_v0.9.26.md) |
> | v0.9.26 → v1.0.6 | [`v0.9.26_to_v1.0.6.md`](./v0.9.26_to_v1.0.6.md) |
> | v1.0.7 → v1.0.7b | [`v1.0.7_to_v1.0.7b.md`](./v1.0.7_to_v1.0.7b.md) / [`v1.0.7_to_v1.0.7a2.md`](./v1.0.7_to_v1.0.7a2.md) |
> | v1.0.8b → v2.0.0 | [`v1.0.8b_v2.0.0.md`](./v1.0.8b_v2.0.0.md) |
> | v2.0.0 → v2.0.3 ＋ 制限公開 | [`restricted_v1.0.7_to_v2.0.3.md`](./restricted_v1.0.7_to_v2.0.3.md) |
>
> 本番適用前に必ず「12. NII に確認すべき事項」を確認し、クローン環境でリハーサル（5 章）を行うこと。

---

## 1. 起点の同定

`feature/jgss-pre` はどのリリースタグの子孫でもなく、**v0.9.21 相当のベースに W2023-21/22/23（制限公開・
メールテンプレート・利用申請）と JGSS 独自カスタマイズを載せたブランチ**である。
以下の 3 つの独立した根拠が一致する。

**根拠 1 — 祖先になっている最新のリリースタグは `v0.9.20a`（2022-11-13）**

```sh
for t in $(git tag); do git merge-base --is-ancestor "$t" feature/jgss-pre 2>/dev/null && echo "$t"; done
# => v0.9.20a が最新。v0.9.21 以降・v1.0 系はいずれも祖先ではない
git describe --tags ed1968f52    # => v0.9.20a-489-ged1968f52
```

**根拠 2 — `postgresql/` の資産集合が `v0.9.21` と完全一致**

```sh
comm -13 <(git ls-tree -r --name-only feature/jgss-pre postgresql/|sort) \
         <(git ls-tree -r --name-only v0.9.21          postgresql/|sort) | wc -l   # => 0
```

| 比較対象 | タグ側にあって jgss-pre に無いファイル |
| --- | --- |
| v0.9.20a / **v0.9.21** | **0 件** |
| v0.9.22a 〜 v0.9.26a | 2 件（`pr873.sql` / `pr1025.sql`） |
| v0.9.27 〜 v1.0.7 | 6 件（＋`v0.9.27.sql` / `2023_Q4.sql` / `pr1274.sql` / `fix_issue_37699.sql`） |

jgss-pre 側にのみ有るのは W2023-21/22/23 系の 5 ファイル。
なお `sp65`〜`sp72` と `v0.9.15_search_management.sql`（`v0.9.17_to_v0.9.26.md`「DB の更新」で使うもの）は
**jgss-pre のツリーに存在する**ため、その範囲は適用済みの可能性が高い（要検証。4-2）。

**根拠 3 — `modules/` の内容差分が最小になるのが `v0.9.21`**

```sh
for t in v0.9.20a v0.9.21 v0.9.22 v0.9.26 v0.9.27 v1.0.6 v1.0.7 v2.0.3; do
  echo "$t $(git diff --name-only feature/jgss-pre $t -- modules | wc -l)"
done
# v0.9.20a 538 / v0.9.21 432 / v0.9.22 557 / v0.9.26 949 / v0.9.27 1090 / v1.0.6 1112 / v1.0.7 1152 / v2.0.3 2001
```

### 1-1. バージョンパス

```
feature/jgss-pre（≒ v0.9.21 + W2023-21/22/23 + JGSS カスタマイズ）
  ↓ v0.9.22 相当   pr873.sql / pr1025.sql
  ↓ v0.9.26 相当   sp65〜sp72 / v0.9.15_search_management（ツリーに有り。要検証）
  ↓ v0.9.27 相当   v0.9.27.sql → SELECT update_v0927()
  ↓ v1.0.6 相当    JPCOAR 2.0 プロパティ移行 / 2023_Q4.sql
  ↓ v1.0.7a2 相当  v1_0_7a2.sql
  ↓ v2.0.0 相当    fix_issue45092.sql（判定）→ W2025-29.sql → update_W2025-29.py
  ↓ v2.0.3 相当    61660.sql（S3 利用時）
v2.0.3
```

### 1-2. 移行元 / 移行先

| 項目 | 内容 |
| --- | --- |
| 移行元 | `feature/jgss-pre`（HEAD: `c179cee` 2025-08-25、分岐元 `ed1968f5` 2024-04-15） |
| 移行先 | `v2.0.3`（`d2fdc0e` 2026-07-28） |
| 独自コミット | 2 本のみ（`3682782f5` instance.cfg / `c179ceed1` npm ビルド修正） |
| `modules/` 変更ファイル数 | 約 2,001 |

---

## 2. 移行で「不要」と判明したもの

長いバージョンパスの割に、以下は**不要**であることを確認した。

| 対象 | 判定 | 根拠 |
| --- | --- | --- |
| 基盤（Python / ES / PostgreSQL）の入れ替え | **不要** | Python 3.6（`python:3.6-slim-buster`）、ES 6.8.23、PostgreSQL 12 はいずれも据え置き。`elasticsearch/Dockerfile` の内容は完全一致 |
| alembic の段階的 upgrade | **不要** | alembic リビジョン数は v0.9.21 / v0.9.26 / v1.0.6 / v1.0.7 / jgss-pre のいずれも **37 本で不変**（この時代は生 SQL 運用）。v2.0.3 の 70 本との差分は `W2025-29.sql` が内包する |
| 統計インデックス／テンプレートの移行 | **不要** | `modules/invenio-stats/invenio_stats/contrib/` の **JSON テンプレートに差分なし**（変更は `.py` 2 本のみ）。`v0.9.17_to_v0.9.26.md` の「Elasticsearch テンプレートの登録」「Elasticsearch インデックスの移行」は本移行では不要 |
| アイテムインデックスの再作成 | **不要** | `weko_schema_ui/mappings/v6/weko/item-v1.0.0.json` の差分は `refresh_interval` 追加と `request_mail_list` 削除のみ（14 行）。既存インデックスのまま**再インデックスで足りる** |
| 著者インデックスの再作成 | **不要** | `weko_authors/mappings/v6/authors/author-v1.0.0.json` の差分は `communityIds`（keyword）の**追加のみ**。ES 6.8 のフィールド追加で対応可（9-3） |
| 独自コミット `c179ceed1` の cherry-pick | **不要** | v2.0.3 に完全に取り込み済み（3-1） |

> **統計インデックス（`*-stats-*` / `*-events-stats-*`）は再構築できない。**
> `invenio index destroy` は本移行のどの段階でも実行しないこと。

---

## 3. jgss-pre 固有の差分

### 3-1. 独自コミット 2 本の扱い

| コミット | 内容 | v2.0.3 での扱い |
| --- | --- | --- |
| `c179ceed1`「ビルドエラー（npm関連）の改修」 | nodesource 20.x 化、`archive.debian.org` への切替、`node-sass@9.0.0`、`tv4` / `objectpath` のパス修正、RCOSDP 版 `angular-schema-form-ckeditor`、`invenio-search-js` の差し替え | **再適用不要。v2.0.3 に完全に取り込み済み**（`scripts/provision-web.sh` 52/55/75/127/163 行、`scripts/create-instance2.sh` 138/139/145/146 行、両 `bundles.py` を照合して一致を確認） |
| `3682782f5`「instance.cfgを大商大オリジナルに修正」 | JGSS 向けアイテムタイプ名・ロール定義 | **大半が v2.0.3 の instance.cfg に「For JGSS」節として上流化済み。4 点のみ追随が必要**（3-2） |

コードの独自パッチは残っていない。**`v2.0.3` をそのままチェックアウトしてよい。**

### 3-2. instance.cfg で追随が必要な 4 点

v2.0.3 の `scripts/instance.cfg` 749 行以降に「For JGSS」節があり、
アイテムタイプ名（`JGSSデータ登録` / `ライフ利用申請` / `利用申請（授業利用可）` ほか）、
`WEKO_ITEMS_UI_*_ROLES`、`WEKO_ITEMS_UI_AUTO_FILL_TITLE*` は**そのまま入っている**。

| # | 設定キー | jgss-pre | v2.0.3 の既定 | 対応 |
| --- | --- | --- | --- | --- |
| 1 | `WEKO_USERPROFILES_FORM_COLUMN` | 有効（`university` / `department` / `position` / `instituteName1〜5` ほか 22 項目） | **`#--` でコメントアウト** | コメント解除。あわせて `WEKO_USERPROFILES_CUSTOMIZE_ENABLED = True` が必要（3-3） |
| 2 | `WEKO_USERPROFILES_ROLE_MAPPING_ENABLED` / `WEKO_USERPROFILES_ROLE_MAPPING` | 有効 | **`#--` でコメントアウト** | コメント解除。無いと職位→ロールの自動割当が止まり、`WEKO_ITEMS_UI_*_ROLES` による申請フォームの出し分けが機能しない |
| 3 | `WEKO_ITEMS_UI_USAGE_REPORT` | `"利用報告"` | `"利用報告-Data Usage Report"` | **DB のアイテムタイプ名に合わせる**（4-5） |
| 4 | `WEKO_ITEMS_UI_HIDE_PUBLICATION_DATE` | 先頭に `"デフォルトアイテムタイプ（フル）"` を含む | 含まない | JGSS の運用に合わせるなら先頭に追加 |

> **`WEKO_WORKFLOW_COLUMNS`**：jgss-pre は `'ItemName'` を含むが、この文字列は
> `weko-workflow` のどこからも参照されていない（jgss-pre / v2.0.3 とも 0 件）。
> **v2.0.3 既定の `'title'` を採用すること。**
>
> **`WEKO_SITEMAP__ROBOT_TXT`**：jgss-pre にあり v2.0.3 に無い。継続したい場合は移植する。

### 3-3. 制限公開（利用申請）フラグ

jgss-pre では制限公開まわりの機能に**フラグが存在せず、常時有効**である
（8 個のキーいずれも jgss-pre の `modules/*/config.py` に定義が無い）。
v2.0.3 ではフラグ化され、**`WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS` 以外は既定 False**。

| 設定キー | jgss-pre | v2.0.3 既定 | 移行後 |
| --- | --- | --- | --- |
| `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` | 定義なし（常時有効） | `False` | **True** |
| `WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS` | 定義なし（常時有効） | `True` | True |
| `WEKO_RECORDS_UI_RESTRICTED_API` | 定義なし（常時有効） | `False` | **True** |
| `WEKO_ITEMS_UI_PROXY_POSTING` | 定義なし（常時有効） | `False` | **True** |
| `WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED` | 定義なし（常時有効） | `False` | **True** |
| `WEKO_INDEX_TREE_SHOW_MODAL` | 定義なし（常時有効） | `False` | **True** |
| `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` | 定義なし（常時有効） | `False` | **True** |
| `INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED` | 定義なし（常時有効） | `False` | **True** |

**設定しないと、移行後に利用申請機能が画面から消える。**

### 3-4. S3 を利用している場合

jgss-pre:

```python
S3_SECRECT_ACCESS_KEY = None                        # ← キー名にタイプミス
FILES_REST_LOCATION_TYPE_LIST = [('s3', 'Amazon S3')]
```

v2.0.3（**環境変数名は据え置いてよい**）:

```python
S3_SECRET_ACCESS_KEY = '{{ environ("S3_SECRECT_ACCESS_KEY") }}'
S3_READONLY_ACCESS_KEY_ID = ...          # weko#61752（v2.0.3 で追加）
S3_READONLY_SECRET_ACCESS_KEY = ...
FILES_REST_LOCATION_TYPE_LIST = [('s3', 'S3 Path'), ('s3_vh', 'S3 Virtural Host')]
```

### 3-5. 新規に必要になるもの

| 項目 | 内容 |
| --- | --- |
| `inbox` サービス | COAR Notify LDN Inbox（`inbox/Dockerfile`、`RCOSDP/coar-notify-inbox` の `nii_main` を clone、Python 3.12 / uvicorn 8080） |
| `mongo` サービス | `mongo:7.0.14`（inbox のバックエンド） |
| Tika | `tika/tika-app-2.6.0.jar`（同梱）。`TIKA_JAR_FILE_PATH` を web / worker に設定 |
| イメージ更新 | `pgpool/pgpool:4.2.2`、`redis:7.4.1`、`rabbitmq:4.0.2` |
| 新規モジュール | `invenio-indexer` / `weko-workspace` / `weko-signposting` / `weko-notifications` |
| 環境変数 | `CACHE_REDIS_DB` / `ACCOUNTS_SESSION_REDIS_DB_NO` / `CELERY_RESULT_BACKEND_DB_NO` / `WEKO_AGGREGATE_EVENT_HOUR` / `WEKO_AGGREGATE_EVENT_MINUTE` / `WEKO_RECORDS_UI_SECRET_KEY` / `SECRET_KEY` / `WTF_CSRF_SECRET_KEY` / `WEKO_HANDLE_ALLOW_REGISTER_CRNI` / `TIKA_JAR_FILE_PATH`（v2.0.3 の instance.cfg が `environ()` 経由で参照する。jgss-pre は直値だったため未定義だと空になる） |

---

## 4. 事前調査（サービス稼働中に実施可）

### 4-1. 変数の定義

```sh
WEKO_DIR=/path/to/weko
COMPOSE="docker compose -f docker-compose2.yml"
WORK_DIR=${WEKO_DIR}/upgrade_work
mkdir -p ${WORK_DIR}
cd ${WEKO_DIR}
git rev-parse --abbrev-ref HEAD ; git rev-parse HEAD | tee ${WORK_DIR}/current_revision.txt
PSQL="${COMPOSE} exec -T postgresql psql -U invenio -d invenio -qtAX -c"
```

### 4-2. 段階ごとの未適用判定

**この判定が本手順書の中核である。** 起点が v0.9.21 相当のため、v0.9.22 以降のすべての段階について
適用済みかを DB で確認する。

```sh
# ---- 段階 1: v0.9.22 相当（pr873.sql / pr1025.sql）----
${PSQL} "SELECT column_name FROM information_schema.columns
         WHERE table_name='facet_search_setting'
           AND column_name IN ('is_open','ui_type','display_number') ORDER BY 1;"   # 3 件そろうべき
${PSQL} "SELECT column_name FROM information_schema.columns
         WHERE table_name='files_location'
           AND column_name IN ('s3_endpoint_url','s3_send_file_directly') ORDER BY 1;"  # 2 件
${PSQL} "SELECT to_regclass('public.workflow_activity_count');"                      # 非 NULL
${PSQL} "SELECT count(*) FROM admin_settings WHERE name='elastic_reindex_settings';" # 1

# ---- 段階 2: v0.9.26 相当（sp65〜sp72 / v0.9.15_search_management）----
#   ※ これらの SQL は jgss-pre のツリーに存在するため適用済みの可能性が高いが、必ず確認する
${PSQL} "SELECT to_regclass('public.authors_affiliation_settings');"   -- sp72
${PSQL} "SELECT to_regclass('public.index_style');"
${PSQL} "SELECT count(*) FROM information_schema.columns
         WHERE table_name='resync_indexes';"                            -- sp70-resync
${PSQL} "SELECT count(*) FROM information_schema.columns
         WHERE table_name='workflow_activity' AND column_name='location_id';"  -- sp70-workflow_location
${PSQL} "SELECT count(*) FROM information_schema.columns
         WHERE table_name='oaiserver_set' AND column_name='id';"        -- sp71-oaiset
#   不足があれば postgresql/ddl/sp*.sql を個別に適用する（原典: v0.9.17_to_v0.9.26.md「DBの更新」）

# ---- 段階 3: v0.9.27 相当（v0.9.27.sql）----
${PSQL} "SELECT count(*) FROM item_type WHERE schema::text LIKE '%subitem_1587693279322%';"
${PSQL} "SELECT count(*) FROM item_type_property WHERE id IN (121,122,124,132);"
#   -> 前者が 0 以外、または後者が 0 以外なら v0.9.27.sql が未適用

# ---- 段階 4: v1.0.6 相当（JPCOAR 2.0 / 2023_Q4.sql）----
${PSQL} "SELECT count(*) FROM item_type_property
         WHERE name IN ('カタログ','データセットシリーズ','保持者','フォーマット','大きさ',
                        '原文の言語','巻号年月次','版','日付（リテラル）','出版者情報');"
#   -> 0 なら JPCOAR 2.0 プロパティが未登録
${PSQL} "SELECT count(*) FROM oaiserver_schema WHERE schema_name='jpcoar_v2_mapping';"
#   -> 0 なら JPCOAR 2.0 の OAI スキーマが未登録
${PSQL} "SELECT count(*) FROM information_schema.columns
         WHERE table_name='mail_config' AND column_name='mail_local_hostname';"       -- 2023_Q4
${PSQL} "SELECT COALESCE(character_maximum_length,0) FROM information_schema.columns
         WHERE table_name='shibboleth_user' AND column_name='shib_eppn';"             -- 2310 であるべき
${PSQL} "SELECT count(*) FROM authors WHERE jsonb_typeof(json)='string';"             -- 0 であるべき

# ---- 段階 5: v1.0.7a2 相当（v1_0_7a2.sql）----
${PSQL} "SELECT scheme FROM authors_prefix_settings ORDER BY id;"
${PSQL} "SELECT scheme FROM authors_affiliation_settings ORDER BY id;"
#   判定: prefix に 'e-Rad_Researcher' または 'AID' が無い、
#         あるいは affiliation に 'ROR' が無い -> v1_0_7a2.sql を適用
#   ※ 'ROR' は prefix 側の初期データに最初から含まれる。prefix の ROR で判定してはいけない

# ---- 段階 6: v2.0.0 相当（fix_issue45092.sql）----
${PSQL} "SELECT count(*) FROM item_type WHERE schema::text LIKE '%subitem_record_name%';"
#   -> 0 以外なら fix_issue45092.sql を適用

# ---- 段階 7: v2.0.3 相当（61660.sql。S3 利用時のみ）----
${PSQL} "SELECT column_name FROM information_schema.columns
         WHERE table_name='files_location' AND column_name LIKE 'readonly%';"
${PSQL} "SELECT count(*) FROM files_location WHERE type LIKE 's3%';"
#   -> 前者 0 行かつ後者 0 以外なら 61660.sql を適用
```

### 4-3. スキーマ全体の突き合わせ（推奨）

段階判定は既知の SQL に対するものであり、v0.9.21 起点では**取りこぼしが起きうる**。
クリーンな v2.0.3 環境を 1 つ立て、スキーマを機械的に比較しておくことを強く推奨する。

```sh
# 現行環境のスキーマ
${COMPOSE} exec -T postgresql pg_dump -U invenio -d invenio -s > ${WORK_DIR}/schema.jgss-pre.sql

# 別ディレクトリに v2.0.3 をクリーン構築し、同様に取得（install.sh / v1.0.7.md「初期インストール手順」）
#   => ${WORK_DIR}/schema.v2.0.3.sql

# テーブル・カラムの集合比較
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -qtAX -c \
"SELECT table_name||'.'||column_name FROM information_schema.columns
  WHERE table_schema='public' ORDER BY 1;" | sort > ${WORK_DIR}/cols.jgss-pre.txt
# v2.0.3 側でも同じクエリを流し cols.v2.0.3.txt を作り
comm -13 ${WORK_DIR}/cols.jgss-pre.txt ${WORK_DIR}/cols.v2.0.3.txt > ${WORK_DIR}/cols.missing.txt
```

`cols.missing.txt` に残るもののうち `W2025-29.sql` が作るもの（10 章の確認クエリの対象）を除いた分が、
段階 1〜5 で埋めるべき差分である。**リハーサル前に必ずこの照合を行うこと。**

### 4-4. 制限公開プロパティ ID の特定

`update_W2025-29.py` の第 1 引数は**アイテムタイプ ID ではなく `item_type_property.id`**である
（`tools/updateRestrictedRecords.py` の `update_item_type_property()` が `ItemTypeProperty.id` で検索）。
既定値は 30015。

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT id, name FROM item_type_property WHERE schema::text LIKE '%termsDescription%' ORDER BY id;"
```

複数出た場合は NII に確認すること。

### 4-5. JGSS アイテムタイプ名の確認

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT itn.id, itn.name, count(it.id) AS versions
   FROM item_type_name itn LEFT JOIN item_type it ON it.name_id = itn.id
  GROUP BY itn.id, itn.name ORDER BY itn.id;"
```

instance.cfg の以下のキーが、この一覧と**一字一句一致**していること。
不一致だと利用申請フォームの出し分け・自動タイトル・自動入力抑止が無効になる。

```
WEKO_ITEMS_UI_USAGE_APPLICATION                                利用申請
WEKO_ITEMS_UI_USAGE_APPLICATION_EDUCATIONAL_PURPOSE            利用申請（授業利用可）
WEKO_ITEMS_UI_USAGE_APPLICATION_TWO_STAGES                     二段階利用申請
WEKO_ITEMS_UI_USAGE_APPLICATION_TWO_STAGES_EDUCATIONAL_PURPOSE 二段階利用申請（授業利用可）
WEKO_ITEMS_UI_USAGE_APPLICATION_TWO_STAGES_GUARANTOR           二段階利用申請（保証人）
WEKO_ITEMS_UI_USAGE_APPLICATION_TWO_STAGES_ADVISOR             二段階利用申請（指導教員）
WEKO_ITEMS_UI_USAGE_APPLICATION_THREE_STAGES                   三段階利用申請
WEKO_ITEMS_UI_APPLICATION_FOR_LIFE                             ライフ利用申請
WEKO_ITEMS_UI_APPLICATION_FOR_ACCUMULATION                     累積利用申請
WEKO_ITEMS_UI_APPLICATION_FOR_COMBINATIONAL_ANALYSIS           組合せ分析利用申請
WEKO_ITEMS_UI_APPLICATION_FOR_PERFECTURES                      都道府県利用申請
WEKO_ITEMS_UI_APPLICATION_FOR_LOCATION_INFORMATION             地点情報利用申請
WEKO_ITEMS_UI_DATA_REGISTRATION                                JGSSデータ登録
WEKO_ITEMS_UI_OUTPUT_REPORT                                    成果物登録
WEKO_ITEMS_UI_USAGE_REPORT                                     利用報告 ← v2.0.3 既定は "利用報告-Data Usage Report"
```

### 4-6. instance.cfg のカスタマイズ差分抽出

```sh
cp scripts/instance.cfg ${WORK_DIR}/instance.cfg.jgss-pre
${COMPOSE} exec -T web cat /home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg \
  > ${WORK_DIR}/invenio.cfg.current
git show v2.0.3:scripts/instance.cfg > ${WORK_DIR}/instance.cfg.v2.0.3
diff -u ${WORK_DIR}/instance.cfg.jgss-pre ${WORK_DIR}/instance.cfg.v2.0.3 > ${WORK_DIR}/instance.cfg.diff ; :
```

リポジトリの `scripts/instance.cfg` と稼働中の `invenio.cfg` が食い違っていないかも必ず確認する。

### 4-7. 所要時間の見積り

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT (SELECT count(*) FROM records_metadata) AS records,
        (SELECT count(*) FROM item_metadata)   AS items,
        (SELECT count(*) FROM item_type)       AS item_types,
        (SELECT count(*) FROM authors)         AS authors;"
```

`v0.9.27.sql`（2,001 行）と `update_W2025-29.py` はいずれも全アイテムのメタデータを走査する。
**v0.9.21 起点のため、v1.0.7 起点の機関より所要時間は長くなる。**

---

## 5. リハーサル（必須）

**本移行はバージョン飛び越し幅が大きく、公式手順書がそのまま当てはまらない。リハーサルは省略できない。**
本番と同じデータを持つクローン環境で 6〜10 章を通しで実施し、以下を記録する。

- 4-2 の段階判定の結果（どの段階が「要」だったか）
- 4-3 のスキーマ照合で残った差分
- `v0.9.27.sql` / `update_jpcoar_2_0.py` / `W2025-29.sql` / `update_W2025-29.py` の各所要時間とエラー有無
- 再インデックスの所要時間
- 動作確認チェックリスト（11 章）、特に **JGSS の 12 種類の利用申請アイテムタイプでフォームが出るか**

---

## 6. バックアップ

```sh
cd ${WEKO_DIR}
${COMPOSE} exec -T postgresql pg_dump -U invenio -d invenio -Fc > ${WORK_DIR}/invenio_$(date +%Y%m%d%H%M).dump
cp scripts/instance.cfg ${WORK_DIR}/
${COMPOSE} exec -T web cat /home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg > ${WORK_DIR}/invenio.cfg.bak
docker volume ls
```

段階ごとに DB ダンプを取ること（7-x の各段階の前後）。
Elasticsearch は DB から再構築できるためバックアップ必須ではないが、
**統計インデックスは再構築できないので削除しないこと**。

---

## 7. サービス停止とコードの更新

### 7-1. サービス停止

```sh
cd ${WEKO_DIR}
${COMPOSE} down
```

（公開環境ではメンテナンス画面へ切り替えてから停止すること）

### 7-2. コード取得

```sh
git fetch origin --tags
git stash
git checkout v2.0.3 -B v2.0.3
git log -1 --format='%H %ci %s'      # d2fdc0e... 2026-07-28
```

独自コミット 2 本の cherry-pick は**不要**（3-1）。

### 7-3. instance.cfg のマージ

**(1) 制限公開フラグ（3-3）**

```
WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG  = True
WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS     = True
WEKO_RECORDS_UI_RESTRICTED_API             = True
WEKO_ITEMS_UI_PROXY_POSTING                = True
WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED    = True
WEKO_INDEX_TREE_SHOW_MODAL                 = True
WEKO_USERPROFILES_CUSTOMIZE_ENABLED        = True
INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED = True
```

**(2) 「For JGSS」節のコメント解除（3-2 #1, #2）** — 先頭の `#--` を外す。

```
WEKO_USERPROFILES_FORM_COLUMN = [...]
WEKO_USERPROFILES_ROLE_MAPPING_ENABLED = True
WEKO_USERPROFILES_ROLE_MAPPING = {...}
```

**(3) アイテムタイプ名の合わせ込み（3-2 #3, #4／4-5 の結果に従う）**

**(4) S3 利用時（3-4）**

**(5) 環境変数の追加（3-5）** — `docker-compose2.yml` の `web` / `worker` に定義する。

**(6) Redis Sentinel を使っている場合**
jgss-pre は `[("sentinel-1","26379"),("sentinel-2","26379"),("sentinel-3","26379")]`、
v2.0.3 は `[("weko-sentinel-service.weko3re","26379")]`（Kubernetes 向け）。
**docker-compose 環境では jgss-pre 側の値を維持すること。** `CELERY_RESULT_BACKEND` も同様。

**(7) 移植を検討するもの** — `WEKO_SITEMAP__ROBOT_TXT`。

### 7-4. weko.conf（Shibboleth 利用時のみ）

```diff
-shib_request_set $shib_shib_session_id $upstream_http_variable_shib_session_id;
-fastcgi_param Shib-Session-ID $shib_shib_session_id;
+shib_request_set $shib_session_id $upstream_http_variable_shib_session_id;
+fastcgi_param Shib-Session-ID $shib_session_id;
```

jgss-pre は `WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = True`。学認を使っていない場合は `False` にして本節を飛ばす。

### 7-5. uwsgi.ini

```ini
# harakiri = 300
```

### 7-6. イメージのビルド

```sh
DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 ${COMPOSE} build --no-cache --force-rm
```

`inbox` は GitHub から `RCOSDP/coar-notify-inbox` を clone する。到達性を事前に確認すること。

### 7-7. postgresql のみ起動

```sh
${COMPOSE} up -d postgresql
${COMPOSE} exec postgresql pg_isready -U invenio
```

---

## 8. DB マイグレーション（段階順）

**必ずこの順序で実施する。** 各段階の前に DB ダンプを取ること。

### 8-1. 段階 1 — v0.9.22 相当（pr873 / pr1025）

`postgresql/ddl/pr873.sql` / `pr1025.sql` は `IF NOT EXISTS` の無い素の DDL であり、
一部適用済みだと異常終了する。**以下の冪等版を使う。**
`pr1274.sql` / `fix_issue_37699.sql`（＝`2023_Q4.sql` の一部）もここでまとめて当てる。

```sh
cat > ${WORK_DIR}/stage1_catchup.sql <<'EOF'
BEGIN;
DO $$
DECLARE
    eppn_len int;
BEGIN
RAISE NOTICE 'Start: stage1 (pr873 / pr1025 / pr1274 / fix_issue_37699)';

-- pr873.sql : facet_search_setting
ALTER TABLE facet_search_setting ADD COLUMN IF NOT EXISTS is_open boolean DEFAULT true NOT NULL;
ALTER TABLE facet_search_setting ADD COLUMN IF NOT EXISTS ui_type character varying(20) DEFAULT 'Editbox' NOT NULL;
ALTER TABLE facet_search_setting ADD COLUMN IF NOT EXISTS display_number integer;
UPDATE facet_search_setting SET ui_type = 'Range' WHERE mapping = 'temporal' AND ui_type <> 'Range';

-- pr1025.sql : files_location
ALTER TABLE files_location ADD COLUMN IF NOT EXISTS s3_endpoint_url varchar(128);
ALTER TABLE files_location ADD COLUMN IF NOT EXISTS s3_send_file_directly boolean NOT NULL DEFAULT true;

-- pr1025.sql : workflow_activity_count
CREATE TABLE IF NOT EXISTS workflow_activity_count (
    status VARCHAR(1) NOT NULL,
    created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    updated TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    date DATE NOT NULL,
    activity_count INTEGER NOT NULL,
    CONSTRAINT pk_workflow_activity_count PRIMARY KEY (date)
);
INSERT INTO workflow_activity_count (status, created, updated, date, activity_count)
SELECT 'N', now(), now(), CURRENT_DATE,
       (SELECT count(*) FROM workflow_activity a
         WHERE a.created >= CURRENT_DATE AND a.created < CURRENT_DATE + 1)
 WHERE NOT EXISTS (SELECT 1 FROM workflow_activity_count WHERE date = CURRENT_DATE);

-- pr1025.sql : admin_settings
INSERT INTO admin_settings (id, name, settings)
SELECT (SELECT COALESCE(MAX(id), 0) + 1 FROM admin_settings),
       'elastic_reindex_settings', '{"has_errored": false}'
 WHERE NOT EXISTS (SELECT 1 FROM admin_settings WHERE name = 'elastic_reindex_settings');
PERFORM setval('admin_settings_id_seq', (SELECT COALESCE(MAX(id), 1) FROM admin_settings));

-- pr1274.sql / 2023_Q4.sql : mail_config
ALTER TABLE mail_config ADD COLUMN IF NOT EXISTS mail_local_hostname character varying(255) DEFAULT '';

-- fix_issue_37699.sql / 2023_Q4.sql : shibboleth_user.shib_eppn
SELECT character_maximum_length INTO eppn_len FROM information_schema.columns
 WHERE table_name = 'shibboleth_user' AND column_name = 'shib_eppn';
IF eppn_len IS NOT NULL AND eppn_len < 2310 THEN
    ALTER TABLE shibboleth_user ALTER COLUMN shib_eppn TYPE CHARACTER VARYING(2310);
    RAISE NOTICE 'shibboleth_user.shib_eppn: % -> 2310', eppn_len;
ELSE
    RAISE NOTICE 'shibboleth_user.shib_eppn: already %, skipping', eppn_len;
END IF;

RAISE NOTICE 'End: stage1';
END $$;
COMMIT;
EOF

docker cp ${WORK_DIR}/stage1_catchup.sql $(${COMPOSE} ps -q postgresql):/tmp/stage1_catchup.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 \
  -f /tmp/stage1_catchup.sql 2>&1 | tee ${WORK_DIR}/stage1.log
```

`authors.json` の二重エンコードが残っていた場合（4-2 段階 4 の判定）:

```sh
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 \
  -c "UPDATE authors SET json = (json #>> '{}')::jsonb WHERE jsonb_typeof(json)='string';"
```

### 8-2. 段階 2 — v0.9.26 相当（不足があった場合のみ）

原典: [`v0.9.17_to_v0.9.26.md`](./v0.9.17_to_v0.9.26.md)「DB の更新」。
4-2 段階 2 で不足が出た SQL のみを適用する。

```sh
for f in sp65-ExportAuthors sp66-ImportAuthors sp70-enhancedSiteInformationScreen \
         sp70-FixOaireVersionInOaiserverSchema sp70-gakuninrdm sp70-resync \
         sp70-workflow_location sp71-oaiset sp71-UpdateAuthorPermission \
         sp71-UpdateSearchLicence sp72-CreateAuthersAffiliation sp72-createindex ; do
  echo "=== $f"   # 4-2 の判定で「要」となったものだけ実行すること
  # docker cp postgresql/ddl/${f}.sql $(${COMPOSE} ps -q postgresql):/tmp/
  # ${COMPOSE} exec -T postgresql psql -U invenio -d invenio -f /tmp/${f}.sql
done
# docker cp postgresql/update/v0.9.15_search_management.sql $(${COMPOSE} ps -q postgresql):/tmp/
```

> これらは jgss-pre のツリーに存在するため**適用済みの可能性が高い**。
> 二重適用は `ADD COLUMN` の重複エラーになるので、必ず 4-2 の判定に従うこと。

### 8-3. 段階 3 — v0.9.27 相当

原典: [`v0.9.26_to_v1.0.6.md`](./v0.9.26_to_v1.0.6.md)。
`v0.9.27.sql` は関数を定義するだけで、実行は別途 `SELECT update_v0927();` が必要。
関数は `item_type_property` が 53 件を超える場合のみ本体を実行する（新規構築機関を除外するガード）。

```sh
docker cp postgresql/ddl/v0.9.27.sql $(${COMPOSE} ps -q postgresql):/tmp/v0.9.27.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/v0.9.27.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -c "SELECT update_v0927();" \
  2>&1 | tee ${WORK_DIR}/v0.9.27.log
```

> **アイテムタイプのプロパティ（121 / 122 / 124 / 132）を DELETE し、
> `records_metadata` の subitem キーを一括置換する。**必ずリハーサルで影響を確認すること。

### 8-4. 段階 4 — v1.0.6 相当（JPCOAR 2.0）

原典: [`v0.9.26_to_v1.0.6.md`](./v0.9.26_to_v1.0.6.md)「JPCOAR 2.0プロパティの追加・更新」。
v2.0.3 のツリーには必要な `scripts/demo/properties/*.py` と `update_jpcoar_2_0.py` が
**すべて同梱されている**ため、原典のような GitHub からの `curl` は不要。

```sh
${COMPOSE} up -d
${COMPOSE} exec -T web invenio shell scripts/demo/update_jpcoar_2_0.py only_specified \
  2>&1 | tee ${WORK_DIR}/update_jpcoar_2_0.log
```

> **`W2025-29.sql` / `update_W2025-29.py` はこの処理を内包していない。**
> `update_W2025-29.py` が呼ぶのは `register_properties_only_specified()`（`SPECIFIED_LIST` 限定）と
> `renew_all_item_types()` のみで、`update_jpcoar_2_0.py` が行う
> `register_properties`（全件）/ `update_itemtype_full` / `update_item_type` /
> `addjpcoar_v2_mapping` は含まれない。**この段階を飛ばしてはいけない。**

OAI-PMH スキーマも更新する（原典 v0.9.26_to_v1.0.6.md）。

```sh
${COMPOSE} exec -T web invenio shell scripts/demo/register_oai_schema.py overwrite_all
```

### 8-5. 段階 5 — v1.0.7a2 相当

```sh
# 4-2 段階 5 で「要」なら
docker cp postgresql/update/v1_0_7a2.sql $(${COMPOSE} ps -q postgresql):/tmp/v1_0_7a2.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/v1_0_7a2.sql
```

> `postgresql/update/v1.0.7b.sql` は**適用しないこと**。
> `SET name='e-Rad_Researcher' scheme='e-Rad_Researcher'` とカンマが欠落した SQL 構文エラーであり、
> かつ jgss-pre 系の初期データに `e-Rad` は存在しないため対象 0 件である。
> `postgresql/ddl/fix_itemtype_issue_45614.sql` も新規構築機関向けで、移行機関は対象外。

### 8-6. 段階 6 — v2.0.0 相当（W2025-29.sql）

原典: [`v1.0.8b_v2.0.0.md`](./v1.0.8b_v2.0.0.md)。

```sh
# 4-2 段階 6 で「要」なら先に
docker cp postgresql/update/fix_issue45092.sql $(${COMPOSE} ps -q postgresql):/tmp/fix_issue45092.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/fix_issue45092.sql

# W2025-29.sql 本体（単一トランザクション。失敗すれば全体がロールバックされる）
docker cp postgresql/ddl/W2025-29.sql $(${COMPOSE} ps -q postgresql):/tmp/W2025-29.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 \
  -f /tmp/W2025-29.sql 2>&1 | tee ${WORK_DIR}/W2025-29.log

grep -iE 'error|fatal|rollback' ${WORK_DIR}/W2025-29.log
tail -3 ${WORK_DIR}/W2025-29.log   # 'End execution: Migration W2025-29.sql' と COMMIT を確認
```

`W2025-29.sql`（1,866 行）が内包しているもの: alembic リビジョン 36 本、
`W2023-23-item-application.sql` / `mail_template.sql` / `W2023-23-request_mail.sql` /
`W2023-21 workflow_flow_action_role.sql` / `W2023-21 update_resticted_items.sql` /
`WOA-06-jsonld_mapping.sql` / `fix_issue_37736.sql` / `fix_issue_39700.sql` /
`202409_BioResource_ddl.sql` / `v1.0.8.sql` / `W-OA-user_activity_log.sql` /
`W2024-58-ams.sql` 相当 / `fix_lang_code_column.sql` / `restricted_mail_template.sql` 相当。

### 8-7. 段階 7 — v2.0.3 相当（S3 利用時のみ）

```sh
docker cp postgresql/ddl/61660.sql $(${COMPOSE} ps -q postgresql):/tmp/61660.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/61660.sql
```

### 8-8. 適用結果の確認

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c "
SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename IN
 ('mail_templates','mail_template_genres','mail_template_users','jsonld_mappings',
  'oa_status','user_activity_logs','notifications_user_settings','sword_clients',
  'workspace_default_conditions','workspace_status_management',
  'author_community_relations','file_onetime_download','file_secret_download',
  'workflow_activity_count','authors_affiliation_settings')
ORDER BY tablename;"

${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT count(*) FROM records_metadata WHERE json ? 'weko_shared_id';"   -- 0 件であること
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT count(*) FROM records_metadata WHERE json ? 'owners';"           -- 全件

${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT tablename FROM pg_tables WHERE tablename LIKE 'user_activity_logs_%' ORDER BY 1;"
```

4-3 のスキーマ照合をここで再実行し、`cols.missing.txt` が空になることを確認する。

> **alembic について**
> `W2025-29.sql` は alembic リビジョンを SQL 化したもので `alembic_version` を更新しない。
> WEKO の運用は `invenio db create` / 生 SQL ベースで `invenio alembic upgrade` を使わないため
> 実害はないが、次回以降 alembic を使う予定がある場合は NII に確認すること。

---

## 9. データマイグレーションと再インデックス

### 9-1. 全サービス起動

```sh
${COMPOSE} up -d
${COMPOSE} ps
${COMPOSE} logs --tail=100 web
```

新規サービス（`inbox` / `mongo`）が Up になっていることを確認する。

### 9-2. update_W2025-29.py の実行

```sh
RESTRICTED_ACCESS_PROPERTY=30015    # 4-4 で特定した値
BATCH_SIZE=500

${COMPOSE} exec -T web invenio shell scripts/demo/update_W2025-29.py \
  ${RESTRICTED_ACCESS_PROPERTY} ${BATCH_SIZE} 2>&1 | tee ${WORK_DIR}/update_W2025-29.log

grep 'All updates completed successfully' ${WORK_DIR}/update_W2025-29.log
grep -iE 'error|traceback|rollback|not found' ${WORK_DIR}/update_W2025-29.log
```

> **`main()` は例外を握りつぶして `db.session.rollback()` するだけで異常終了しない。**
> 終了コードではなく必ずログで判定すること。
> `All updates completed successfully.` が出ていなければ失敗である。

> **JGSS 環境での注意**
> JGSS は利用申請系アイテムタイプが 12 種類ある（4-5）。
> `updateRestrictedRecords` は `item_type_property.id` を起点に、そのプロパティを使う
> アイテムタイプをすべて v2.0 形式（`roles`）へ変換する。
> ログに 12 種類すべてが現れることをリハーサルで確認しておくこと。

### 9-3. Elasticsearch マッピングの更新

| インデックス | 変更 | 対応 |
| --- | --- | --- |
| `<prefix>-weko-item-v1.0.0` | `request_mail_list` の削除、`refresh_interval` 追加 | 既存マッピングに残っていても無害。**再作成不要** |
| `<prefix>-authors-author-v1.0.0` | `communityIds`（keyword）の追加 | フィールド追加 → 著者を再インデックス |

```sh
${COMPOSE} exec -T elasticsearch curl -s "localhost:9200/_cat/indices?v"

AUTHORS_INDEX=$(${COMPOSE} exec -T elasticsearch \
  curl -s "localhost:9200/_cat/indices/*authors*?h=index" | tr -d '\r' | grep -v '^$' | head -1)
echo "${AUTHORS_INDEX}"    # <prefix>-authors-author-v1.0.0 の形式

${COMPOSE} exec -T elasticsearch curl -XPUT \
  "localhost:9200/${AUTHORS_INDEX}/_mapping/author-v1.0.0?pretty" \
  -H "Content-Type: application/json" \
  -d '{"properties":{"communityIds":{"type":"keyword"}}}'

${COMPOSE} exec -T elasticsearch curl -s \
  "localhost:9200/${AUTHORS_INDEX}/_mapping?pretty" | grep -A2 communityIds
```

> `WEKO_AUTHORS_ES_INDEX_NAME = "{SEARCH_INDEX_PREFIX}-authors"` は**エイリアス名**であり、
> 実インデックスは `<prefix>-authors-author-v1.0.0` である。

### 9-4. dynamic mapping timeout の変更

```sh
${COMPOSE} exec -T elasticsearch curl -XPUT localhost:9200/_cluster/settings \
  -H "Content-Type: application/json" \
  -d '{"persistent": {"indices.mapping.dynamic_timeout": "600s"}}'
```

### 9-5. 再インデックス

```sh
${COMPOSE} exec -T web invenio index reindex --pid-type recid --yes-i-know 2>&1 | tee ${WORK_DIR}/reindex.log
${COMPOSE} exec -T web invenio index run --raise-on-error False --chunk-size 50 2>&1 | tee -a ${WORK_DIR}/reindex.log
${COMPOSE} exec -T web invenio authors reindex --yes-i-know 2>&1 | tee ${WORK_DIR}/reindex_authors.log
```

`--raise-on-error False` で個別アイテムのエラーがあっても継続し、`--chunk-size 50`（既定 500）で
ES / RabbitMQ の負荷を抑える。**`invenio index destroy` は実行しないこと。**

件数照合:

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -qtAX -c \
 "SELECT count(*) FROM pidstore_pid WHERE pid_type='recid' AND status='R';"
${COMPOSE} exec -T elasticsearch curl -s "localhost:9200/_cat/indices?v"
```

### 9-6. 静的リソースの再生成

```sh
${COMPOSE} exec -T web invenio assets build
${COMPOSE} exec -T web invenio collect -v
${COMPOSE} exec -T web bash -c \
  "jinja2 /code/scripts/instance.cfg > /home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg"
${COMPOSE} restart web worker
```

---

## 10. 動作確認チェックリスト

**共通**

- [ ] トップページが表示され、HTTP 500 / 502 が発生しない
- [ ] 管理者でログインできる／一般ユーザーでログインできる
- [ ] 検索が表示される（検索結果件数に不自然な差異がない）
- [ ] ファセット検索が表示される（8-1 の `ui_type` / `display_number` 追加後）
- [ ] アイテム詳細画面が表示され、ファイルがダウンロードできる
- [ ] **JPCOAR 2.0 のプロパティがアイテムタイプ編集画面に出る**（8-4）
- [ ] **OAI-PMH で `jpcoar_2.0` が返る**（8-4）
- [ ] アイテム登録・編集・承認が通る
- [ ] 著者DB の検索・編集
- [ ] メール送信（`mail_templates` / `mail_template_users` の To/CC/BCC）
- [ ] 統計（`*-stats-*` が残っていること）
- [ ] `${COMPOSE} logs web worker` にエラーが出ていない

**制限公開（3-3 のフラグ設定確認）**

- [ ] Administration > 制限公開（利用申請）設定が表示される
- [ ] 制限公開アイテムの利用申請フォームが表示され、申請できる
- [ ] ワークフローに制限公開の承認アクションが表示される
- [ ] シークレットURL の発行・ダウンロード

**JGSS 固有**

- [ ] ユーザープロファイル画面に `university` / `department` / `position` / `instituteName1〜5` が表示される
- [ ] 職位に応じたロールが自動付与される（`WEKO_USERPROFILES_ROLE_MAPPING`）
- [ ] **ライフ / 累積 / 組合せ分析 / 都道府県 / 地点情報**の各利用申請で、
      ロール（一般／既卒生／学生）ごとに保証人欄・指導教員欄の出し分けが正しい
- [ ] 二段階利用申請（保証人）／（指導教員）の承認メールが正しい宛先へ飛ぶ
- [ ] 利用報告・成果物登録でタイトルが自動設定される
- [ ] JGSSデータ登録・各利用申請で公開日欄が非表示
- [ ] ワークフロー活動一覧の列が想定どおり（3-2 の `WEKO_WORKFLOW_COLUMNS` 注記）

---

## 11. 切り戻し

```sh
cd ${WEKO_DIR}
${COMPOSE} down
git checkout feature/jgss-pre
cp ${WORK_DIR}/instance.cfg scripts/instance.cfg
DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 ${COMPOSE} build --no-cache --force-rm
${COMPOSE} up -d postgresql
docker cp ${WORK_DIR}/invenio_YYYYMMDDHHMM.dump $(${COMPOSE} ps -q postgresql):/tmp/restore.dump
${COMPOSE} exec -T postgresql pg_restore -U invenio -d invenio --clean --if-exists /tmp/restore.dump
${COMPOSE} up -d
${COMPOSE} exec -T web invenio index reindex -t recid --yes-i-know
${COMPOSE} exec -T web invenio index run
```

段階 1（8-1）までなら列追加のみで jgss-pre のコードからは参照されないため無害。
**段階 3（`update_v0927()`）以降はメタデータが書き換わるため、必ず DB リストアが必要。**
段階ごとにダンプを取っておくこと。

---

## 12. NII に確認すべき事項

1. **【最重要】起点が v0.9.21 相当であることの確認と、正規の移行パス**
   `feature/jgss-pre` の `postgresql/` 資産集合は `v0.9.21` と完全一致し、祖先タグの最新は `v0.9.20a`。
   一方で W2023-21/22/23 の機能は入っている（1 章）。
   このハイブリッド構成に対する NII 側の想定移行パスを確認する。
   本手順書は v0.9.22 → v0.9.26 → v0.9.27 → v1.0.6 → v1.0.7a2 → v2.0.0 → v2.0.3 と積み上げる前提で書いた。

2. **段階 2（sp65〜sp72 / v0.9.15_search_management）の要否**
   これらの SQL は jgss-pre のツリーに存在するが、実際に DB へ適用済みかは環境側の履歴による。
   4-2 の判定方法で足りるか、他に確認すべき項目がないかを確認する。

3. **段階 3（`v0.9.27.sql` / `update_v0927()`）を移行機関に適用してよいか**
   `item_type_property` の 121 / 122 / 124 / 132 を DELETE し、`records_metadata` の
   subitem キーを一括置換する。JGSS の独自アイテムタイプへの影響を確認する。

4. **段階 4（JPCOAR 2.0）の実行方法**
   `update_jpcoar_2_0.py only_specified` を v2.0.3 のツリーで実行してよいか
   （原典は develop ブランチから個別ファイルを `curl` する手順）。
   また `W2025-29.sql` / `update_W2025-29.py` との実行順（JPCOAR 2.0 が先）で正しいか。

5. **`WEKO_ITEMS_UI_USAGE_REPORT` の正しい値**
   jgss-pre は `"利用報告"`、v2.0.3 の instance.cfg 既定は `"利用報告-Data Usage Report"`。
   アイテムタイプ名をリネームする想定なのか、設定側を戻すのかを確認する。

6. **v2.0.3 instance.cfg の「For JGSS」節がコメントアウトされている意図**
   `WEKO_USERPROFILES_FORM_COLUMN` / `WEKO_USERPROFILES_ROLE_MAPPING*` が `#--`。
   JGSS 機関ではコメント解除が前提でよいか。

7. **`postgresql/update/v1.0.7b.sql` の SQL 構文エラー**（カンマ欠落）。修正版が必要か。

8. **制限公開機能を有効のまま移行する場合の追加手順・検証ツールの有無**
   （`tools/verify_restricted_records.py` 等は v2.0.3 に未収録で、
   `fix/restricted_update_202606` 等のブランチにのみ存在する）。

9. `inbox` / `mongo` を本番構成に含めるか。

10. `alembic_version` を stamp する運用があるか。

---

## アップデート処理の流れ

```text
起点の同定(1章) ─ v0.9.21 相当 + W2023-2x + JGSS カスタマイズ
    ↓
事前調査(4章) ─ 段階1〜7の未適用判定 / スキーマ全体照合 / アイテムタイプ名 / 制限公開プロパティID
    ↓
リハーサル(5章) ★省略不可
    ↓
バックアップ(6章)
    ↓
WEKO 停止 → v2.0.3 チェックアウト(7-1,7-2)   ← 独自コミットの cherry-pick は不要
    ↓
instance.cfg 更新(7-3)  ← 制限公開8フラグ True / JGSS節のコメント解除 / アイテムタイプ名
    ↓
イメージビルド(7-6) → postgresql のみ起動(7-7)
    ↓
段階1 v0.9.22相当  pr873 / pr1025 / pr1274 / fix_issue_37699（冪等版）        (8-1)
    ↓
段階2 v0.9.26相当  sp65〜sp72 / v0.9.15_search_management（不足分のみ）        (8-2)
    ↓
段階3 v0.9.27相当  v0.9.27.sql → SELECT update_v0927()                        (8-3)
    ↓
段階4 v1.0.6相当   update_jpcoar_2_0.py only_specified / register_oai_schema  (8-4)
    ↓
段階5 v1.0.7a2相当 v1_0_7a2.sql                                               (8-5)
    ↓
段階6 v2.0.0相当   fix_issue45092.sql → W2025-29.sql                          (8-6)
    ↓
段階7 v2.0.3相当   61660.sql（S3利用時）                                       (8-7)
    ↓
確認(8-8) → WEKO 起動(9-1) → update_W2025-29.py 30015 500 (9-2)
    ↓
ES mapping communityIds 追加(9-3) → dynamic mapping timeout 600s(9-4)
    ↓
reindex(9-5) → assets build / collect(9-6)
    ↓
動作確認(10章)
```

---

## 付録: 実行スクリプト

`weko` リポジトリ直下に配置して使う。

```
tools/upgrade_jgss-pre_to_v2.0.3.sh
```

```sh
./tools/upgrade_jgss-pre_to_v2.0.3.sh check     # 4章    段階1〜7の未適用判定（DB を更新しない）
./tools/upgrade_jgss-pre_to_v2.0.3.sh backup    # 6章    DB/設定のバックアップ
./tools/upgrade_jgss-pre_to_v2.0.3.sh config    # 7-3    制限公開フラグ + JGSS節のコメント解除
./tools/upgrade_jgss-pre_to_v2.0.3.sh build     # 7-6,7-7 ビルド + postgresql 起動
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage1    # 8-1    v0.9.22相当（冪等版）
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage2    # 8-2    v0.9.26相当（不足分の一覧を出力）
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage3    # 8-3    v0.9.27相当
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage4    # 8-4    JPCOAR 2.0
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage5    # 8-5    v1.0.7a2相当
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage6    # 8-6    W2025-29.sql
./tools/upgrade_jgss-pre_to_v2.0.3.sh stage7    # 8-7    61660.sql（S3利用時）
./tools/upgrade_jgss-pre_to_v2.0.3.sh data      # 9-1,9-2 起動 + update_W2025-29.py
./tools/upgrade_jgss-pre_to_v2.0.3.sh reindex   # 9-3〜9-5 mapping + timeout + reindex
./tools/upgrade_jgss-pre_to_v2.0.3.sh assets    # 9-6    assets build / collect
./tools/upgrade_jgss-pre_to_v2.0.3.sh verify    # 8-8 / 10章 の機械的確認
```

ログ・バックアップはすべて `${WORK_DIR}`（既定 `./upgrade_work`）に集約される。
各 `stage*` は `check` が生成した `${WORK_DIR}/decisions.env` の判定に従い、
不要と判定された段階は自動的にスキップする。
