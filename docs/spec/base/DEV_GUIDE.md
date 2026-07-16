# 開発者ガイド（道しるべ）

WEKO3 に変更を加える人（および AI）が、「やりたいこと」から該当機能仕様・実装モジュール・入口ファイルへ
最短で到達するためのガイド。全体像は [アーキテクチャ全体像](ARCHITECTURE.md)、
モジュール単位の逆引きは [モジュール索引](MODULE_INDEX.md)、
config／DB／エンドポイント等の横断は [横断索引](CROSS_REFERENCE.md) を参照。

## この索引の辿り方（推奨フロー）

1. **機能から入る**: [目次](SUMMARY.md) かサイト内検索で対象機能の仕様書を開く。
2. **仕様書内で当たりを付ける**: 各仕様書の「関連モジュール」「処理概要」節に、
   実際の **モジュール名・ファイル名・クラス／メソッド名・config キー・テーブル名** が書かれている。
   （方針として本文に `:行番号` は載せていない。行番号は実ソースを開いて確認する。）
3. **実装を開く**: `modules/<モジュール名>/<パッケージ>/` を開き、入口ファイル（下表）から読む。
4. **影響範囲を確認する**: [モジュール索引](MODULE_INDEX.md) で、そのモジュールを参照する他機能を逆引きする。
5. **横断情報を確認する**: config キー・DB テーブル・API エンドポイント・Celery タスク・権限は [横断索引](CROSS_REFERENCE.md) から辿る。

> AI で利用する場合も同じ順序が有効。まず機能仕様（自然言語＋記号名）で当たりを付け、
> 記号名で実ソースを grep し、モジュール索引で影響範囲を広げる、という流れが誤爆が少ない。

## やりたいこと → どこを見るか（タスク逆引き）

| やりたいこと | 主な機能仕様 | 主なモジュール | 入口の目安 |
| --- | --- | --- | --- |
| アイテムタイプ／メタデータ／マッピングを変える | [ADMIN-1-*](admin/ADMIN_1_1.md) | `weko-itemtypes-ui`, `weko-records` | `views.py`, `models.py`, `scripts/demo/*.sql` |
| 検索の挙動・ファセットを変える | [USER-1-*](user/USER_1_1.md), [ADMIN-14-11/12](admin/ADMIN_14_11.md) | `weko-search-ui`, `invenio-records-rest` | `rest.py`, `config.py` |
| アイテム詳細表示・ファイル配信・アクセス制御 | [USER-3-*](user/USER_3_1.md), [制限公開](restricted_access/README.md) | `weko-records-ui` | `views.py`, `permissions.py`, `utils.py` |
| 登録処理・Elasticsearch 投入 | [USER-4-*](user/USER_4_4.md) | `weko-deposit`, `invenio-indexer` | `api.py`, `tasks.py`, `receivers.py` |
| ワークフロー・承認・利用申請 | [USER-4-*](user/USER_4_3.md), [ADMIN-7-*](admin/ADMIN_7_1.md), [制限公開](restricted_access/README.md) | `weko-workflow` | `views.py`, `models.py`, `config.py` |
| インデックスツリー（分類階層） | [USER-1-3](user/USER_1_3.md), [ADMIN-3-*](admin/ADMIN_3_1.md) | `weko-index-tree`, `weko-indextree-journal` | `api.py`, `rest.py`, `models.py` |
| ウェブデザイン（ウィジェット／レイアウト） | [ADMIN-4-*](admin/ADMIN_4_1.md) | `weko-gridlayout` | `views.py`, `models.py`, `admin.py` |
| 著者DB（編集／一括登録・出力／名寄せ） | [ADMIN-5-*](admin/ADMIN_5_1.md) | `weko-authors` | `views.py`, `rest.py`, `tasks.py` |
| 統計・運用レポート | [ADMIN-6-*](admin/ADMIN_6_1.md), [USER-3-5](user/USER_3_5.md) | `weko-admin`, `invenio-stats` | `tasks.py`, `models.py` |
| OAI-PMH（提供／ハーベスト） | [ADMIN-9-*](admin/ADMIN_9_1.md), [API-2](api/API_02_OAIPMH.md) | `invenio-oaiserver`, `invenio-oaiharvester` | `api.py`, `tasks.py` |
| ResourceSync | [ADMIN-10-*](admin/ADMIN_10_1.md) | `invenio-resourcesyncserver`, `invenio-resourcesyncclient` | `views.py`, `api.py` |
| SWORD 受入 | [ADMIN-16-*](admin/ADMIN_16_1.md), [API-6](api/API_06_sword_api.md) | `weko-swordserver` | `views.py`, `api.py` |
| ユーザ・ロール・OAuth／WebAPI アカウント | [ADMIN-13-*](admin/ADMIN_13_1.md) | `invenio-accounts`, `weko-accounts`, `invenio-oauth2server` | `models.py`, `config.py` |
| 管理設定（サイト情報／メール／ログ解析等） | [ADMIN-14-*](admin/ADMIN_14_1.md) | `weko-admin` | `views.py`, `models.py`, `config.py` |
| メール送信・テンプレート | [ADMIN-14-16](admin/ADMIN_14_16.md), [ADMIN-14-22](admin/ADMIN_14_22.md) | `invenio-mail`, `weko-admin` | `models.py`, `templates/` |
| コミュニティ（サブリポジトリ） | [USER-5-*](user/USER_5_1.md), [ADMIN-8-*](admin/ADMIN_8_1.md) | `invenio-communities` | `models.py`, `views.py` |
| テーマ・トップページ・共通レイアウト | — | `weko-theme` | `views.py`, `templates/`, `static/` |
| 永続識別子（Handle／DOI 等） | [ADMIN-11-1](admin/ADMIN_11_1.md), [USER-4-10](user/USER_4_10.md) | `weko-handle`, `weko-workflow` | `api.py`, `config.py` |
| ファイル実体の格納・配信 | [ADMIN-12-*](admin/ADMIN_12_1.md), [API-6/File](api/README.md) | `invenio-files-rest`, `invenio-s3` | `views.py`, `models.py` |
| プッシュ通知（COAR Notify） | [プッシュ通知機能](other/INBOX_01.md) | `weko-notifications` | `views.py`, `models.py` |

## 変更対象別・入口ファイルの型

Invenio 拡張は entry_points 経由でアプリに組み込まれる（詳細は [アーキテクチャ](ARCHITECTURE.md)）。
何を変えたいかで、開くファイルはおおむね決まっている。

| 変えたいもの | 開くファイル | 対応 entry_points |
| --- | --- | --- |
| 画面（UI）の挙動・ルート | `<pkg>/views.py`, `templates/`, `static/js/` | `invenio_base.apps`, `invenio_assets.bundles` |
| WebAPI（REST）の挙動・ルート | `<pkg>/rest.py`, `<pkg>/ext.py` | `invenio_base.api_apps` |
| 管理画面（Flask-Admin）のビュー | `<pkg>/admin.py` | `invenio_admin.views` |
| データモデル・テーブル | `<pkg>/models.py`（＋ `alembic/` でマイグレーション） | `invenio_db.models`, `invenio_db.alembic` |
| 非同期処理 | `<pkg>/tasks.py` | `invenio_celery.tasks` |
| 設定値（デフォルト） | `<pkg>/config.py`（サーバ上書きは `scripts/instance.cfg`） | — |
| 権限判定 | `<pkg>/permissions.py`（無い場合は `views.py`／`admin.py` 内） | — |
| WebAPI のスコープ | `<pkg>/scopes.py` | `invenio_oauth2server.scopes` |
| CLI コマンド | `<pkg>/cli.py` | `flask.commands` |
| ビジネスロジック | `<pkg>/api.py`, `<pkg>/utils.py` | — |

## 開発環境・テスト

出典: リポジトリ直下 `AGENTS.md`。

- Docker を利用。クローン後 `install.sh` を実行すると環境構築が始まる。構築後 `https://127.0.0.1/` にアクセスできる。
- テスト: `python manage.py test`（または `pytest`）。新機能には対応テストを追加し、全パスを確認してから確定する。
- コードスタイル: PEP8。フォーマッタ Black、リンタ Flake8、インポート整列 isort。コミット前に指摘ゼロにする。
- 機密情報はコードに直書きせず、環境変数（`docker-compose2.yml`）・`scripts/instance.cfg` から読む。

## 索引の保守（陳腐化を防ぐ）

- [モジュール索引](MODULE_INDEX.md) の逆引き（モジュール→機能）は、各機能仕様の「関連モジュール」節を
  機械集計して生成する。**関連モジュール節を編集したら再生成すること**:

  ```
  python3 spec/tools/generate_module_index.py
  ```

  モジュールの1行説明はスクリプト内の `DESC` を人手で維持する（新規モジュール追加時は `DESC` にも追記）。
- リンク切れ・SUMMARY 掲載漏れは、コミット前に確認するとナビの信頼性を保てる（CI 化推奨）。
- [アーキテクチャ](ARCHITECTURE.md) / [横断索引](CROSS_REFERENCE.md) は手動保守。

## 既知の落とし穴（AI・新規開発者向け注意）

`findings.md`（実装 v2.0.2 との突き合わせ記録）から、間違えやすい点を抜粋。

- **フロントエンドは別リポジトリのものがある**。AMS の Nuxt フロント `weko-frontend`（`nginx/ams/weko-frontend/`）等は
  この環境（`/home/mhaya/weko`）に無く検証不可。OAuth 認証画面や AMS 画面の**エラー文言はフロント生成**で、
  backend の実文字列とは異なることがある。UI 文言を直す際は「どちら側の実装か」を先に確認する。
- **アイテムタイプは SQL 直挿入で管理**されている（`scripts/demo/*.sql`）。Python のアイテムタイプ定義ではない。
  制限公開系のアイテムタイプ（31001〜31008 等）は `scripts/demo/resticted_access.sql` ほかを参照。
- **UI アプリと REST API アプリは別インスタンス**。同名の機能でも登録先の Blueprint／entry_points が違う
  （`invenio_base.apps` と `invenio_base.api_apps`）。「画面から動くのか API からか」を最初に切り分ける。
- **API の実装位置を取り違えやすい**例: リクエストメール送信 API（`/api/v1/records/<id>/request-mail`）は
  `weko-deposit` ではなく **`weko-records-ui`**（`RequestMail` / `send_request_mail`）にある。
- **未対応のまま残っている定義**がある。例: ワークフローの OA Policy Confirmation（action_id 6, `oa_policy`）は
  config 定義のみで `WEKO_WORKFLOW_ACTIONS` に含まれず、`views.py` に処理分岐が無い（非対応）。
- **旧バージョン参照は陳腐化**している。各仕様の更新履歴や `other/MODULE_01.md`・`other/CONFIG_01.md` にある
  GitHub リンク（v0.9.22 など）は古い。実体は tag `v2.0.2` の実装を正とする。
- **config キーの綴り・実在に注意**。過去に `S3_SECRECT_ACCESS_KEY`（誤）→ `S3_SECRET_ACCESS_KEY`（正）等の混入があった。
  存在しないキーもある。config は [横断索引](CROSS_REFERENCE.md) 経由で `other/CONFIG_01.md` と実 `config.py` の両方で確認する。
- **アクセスコントロール表の一部はコード裏付けが弱い**。管理画面のロール可否表には Flask-Admin の factory 依存で
  コード上の明示的な `can_*` が無いものがあり、仕様書内で要検証と注記されている箇所がある。

## 更新履歴

| 日付 | 更新内容 |
| --- | --- |
| 2026/07/15 | 新規作成。タスク逆引き表・入口ファイルの型・開発環境／テスト・既知の落とし穴（`findings.md` 由来）を整備 |
