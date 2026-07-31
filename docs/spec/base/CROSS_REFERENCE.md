# 横断索引

機能をまたぐ関心事（設定値・DB・API エンドポイント・非同期タスク・権限・ログ・ID 体系など）への
ハブ。既存の横断ドキュメントへの入口と、「実装のどこに定義があるか」を併記する。
全体像は [アーキテクチャ](ARCHITECTURE.md)、モジュール逆引きは [モジュール索引](MODULE_INDEX.md)、
作業起点は [開発者ガイド](DEV_GUIDE.md) を参照。

## 設定値（config）

- ドキュメント: [その他 › コンフィグ](other/CONFIG_01.md)
- 優先順位: `instance.cfg`（＝ `invenio.cfg`, サーバ個別上書き） > 各モジュールの `config.py`（デフォルト）
- 実装での探し方: `modules/<モジュール>/<パッケージ>/config.py`。キー名は接頭辞がモジュールに対応する
  （例: `WEKO_ADMIN_*`, `WEKO_WORKFLOW_*`, `WEKO_RECORDS_UI_*`, `WEKO_SEARCH_*`）。
- 注意: 旧バージョン参照は陳腐化。綴り・実在は実 `config.py` で最終確認する（[開発者ガイド › 落とし穴](DEV_GUIDE.md) 参照）。

## DB（テーブル・モデル）

- ドキュメント: [その他 › DB](other/DB_01.md)
- 実装での探し方: 各モジュールの `models.py`（`invenio_db.models` entry_points で登録）。
  スキーマ変更は同モジュールの `alembic/`（`invenio_db.alembic`）でマイグレーションを追加。
- レコード（メタデータ）本体は `invenio-records` / `weko-records`、ファイルは `invenio-files-rest` のモデルが中心。

## API エンドポイント

- ドキュメント: [API Endpoint](api/API_ENDPOINT_01.md)、WebAPI 一覧は [WebAPI](api/README.md)
- 構成: UI アプリと API アプリの 2 つがある。API アプリはベースパス `/api` にマウントされ、
  バージョン付き REST のフルパスは `/api/<version>/...`（現行 `v1`）。
- 実装での探し方: 各モジュールの `*_REST_ENDPOINTS`（例 `WEKO_RECORDS_UI_REST_ENDPOINTS`,
  `WEKO_AUTHORS_REST_ENDPOINTS`, `WEKO_INDEX_TREE_REST_ENDPOINTS`, `WEKO_SEARCH_REST_ENDPOINTS`,
  `WEKO_WORKFLOW_REST_ENDPOINTS`）で定義し、`create_blueprint`（`rest.py`／`ext.py`）で API アプリへ登録。
- OAuth2 スコープは各モジュールの `scopes.py`（`invenio_oauth2server.scopes`）。

## 非同期タスク（Celery）

- ドキュメント: [その他 › celery タスク](other/CELERY_01.md)
- 定期実行: `instance.cfg`（`invenio.cfg`）の `CELERY_BEAT_SCHEDULE` で定義。
- 実装での探し方: 各モジュールの `tasks.py`（`invenio_celery.tasks` entry_points で登録）。
- 代表例: 統計処理 `invenio_stats.tasks.process_events` / `aggregate_events`、インデックス更新、メール送信、インポート。

## 権限・ロール（アクセスコントロール）

- ドキュメント: [アクセスコントロール](access_control/README.md)（画面・API ごとのロール別可否表）
- ロール: システム管理者／リポジトリ管理者／コミュニティ管理者／登録ユーザー／一般ユーザー／ゲスト（未ログイン）
- 実装での探し方: 各モジュールの `permissions.py`、または `views.py`／`admin.py` 内のデコレータ・factory。
  認証基盤は `invenio-accounts` ＋ `weko-accounts`（Shibboleth）、WebAPI は `invenio-oauth2server`。
- 注意: 一部のロール可否表は Flask-Admin の factory 依存でコード上の明示が弱く、仕様書内に要検証注記がある。

## 認証・セッション

- セッション: [その他 › セッション管理](other/SESSION_01.md)（`invenio-accounts` ベース。一括登録は `WEKO_ADMIN_IMPORT_PAGE_LIFETIME`）
- 学認（Shibboleth）: [その他 › Shibboleth対応](other/SHIBBOLETH_01.md)、[ADMIN-14-19](admin/ADMIN_14_19.md)、`weko-accounts`

## ログ

- 運用ログ: [その他 › ログ](other/LOG.md)（ログレベル定義）、実装は `weko-logging`
- 利用統計ログ: [その他 › 利用統計ログ](other/USAGE_LOG.md)（`invenio-stats`）
- 基本監査ログ: [その他 › 基本監査ログ](other/USER_ACTIVITY_LOG.md)（`weko-logging`）、[ADMIN-17-1](admin/ADMIN_17_1.md)

## ID 体系

- ドキュメント: [その他 › ID体系](other/ID_01.md)（アイテムタイプ ID の割り当て等）
- 制限公開に使うアイテムタイプ ID（31001〜）は SQL 直挿入で定義（[制限公開](restricted_access/README.md)、`scripts/demo/*.sql`）。

## データ構造（スキーマ／フォーム／レンダリング）

- [SCHEMA-1-1: Render](other/SCHEMA_1_1.md) / [SCHEMA-1-2: Schema](other/SCHEMA_1_2.md) / [SCHEMA-1-3: Form](other/SCHEMA_1_3.md)
- メタデータ出力スキーマとマッピングは `weko-schema-ui`、アイテムタイプ／プロパティは `weko-itemtypes-ui`。

## 外部連携

- OAI-PMH: [ADMIN-9-*](admin/ADMIN_9_1.md), [API-2](api/API_02_OAIPMH.md) / `invenio-oaiserver`, `invenio-oaiharvester`
- ResourceSync: [ADMIN-10-*](admin/ADMIN_10_1.md) / `invenio-resourcesyncserver`, `invenio-resourcesyncclient`
- SWORD: [ADMIN-16-*](admin/ADMIN_16_1.md), [API-6](api/API_06_sword_api.md) / `weko-swordserver`
- Signposting: `weko-signposting`
- COAR Notify（プッシュ通知）: [プッシュ通知機能](other/INBOX_01.md) / `weko-notifications`
- GakuNinRDM 連携: [その他 › GakuNinRDM連携](other/WORKFLOW_01.md)
- 解析基盤連携: [その他 › 解析基盤連携](other/KAISEKI_01.md)
- OA アシスト連携: [OAアシスト機能ステータス連携](other/OA-ASSIST_STATUS_LINKING.md)
- researchmap 連携: [researchmap連携機能](user/USER_11_1.md)

## 更新履歴

| 日付 | 更新内容 |
| --- | --- |
| 2026/07/15 | 新規作成。config／DB／API エンドポイント／Celery／権限／ログ／ID 等の横断索引ハブとして整備 |
