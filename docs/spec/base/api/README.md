# WEB API

WEKO3 が提供する各種 WEB API の仕様をまとめる。REST API はAPIアプリ（ベースパス `/api`）に登録され、バージョン付きのものはフルパス `/api/<version>/...`（現行 `v1`）となる。認証は主に OAuth2（Bearer トークン）＋スコープで行う。

## 本カテゴリの構成

| ドキュメント | 主なエンドポイント / モジュール |
| --- | --- |
| [API-1: OAuth2](./API_01_Oauth2.md) | `/oauth/authorize`, `/oauth/token`（invenio-oauth2server） |
| [API-2: OAI-PMH](./API_02_OAIPMH.md) | `/oai`（invenio-oaiserver / weko-schema-ui） |
| [API-3: OpenSearch](./API_03_OpenSearch.md) | `/api/opensearch/search`（weko-search-ui） |
| [API-4: Workflow API](./API_04_workflow.md) | `/api/depositactivity`（weko-workflow） |
| [API-5: Index操作API](./API_05_index_op.md) | `/api/<v>/tree...`（weko-index-tree） |
| [API-6: SWORD API](./API_06_sword_api.md) | `/sword/...`（weko-swordserver） |
| [API-7: アイテム検索用API](./API_07_item_search.md) | `/api/records/`（invenio-records-rest / weko-search-ui） |
| [API-8: インデックス検索用API](./API_08_index_search.md) | `/api/index/`（weko-search-ui） |
| [API-9: Render](./API_09_render.md) | `/admin/itemtypes/<id>/render`（weko-itemtypes-ui） |
| [API-10: JSON Schema](./API_10_JSON_Schema.md) | `/items/jsonschema/<id>`（weko-items-ui） |
| [API-11: JSON Form](./API_11_JSON_Form.md) | `/items/schemaform/<id>`（weko-items-ui） |
| [API-12: アイテム検索用API（RO-Crate）](./API_12_item_search_RO-Crate.md) | `/api/v1/records`, `/api/v1/records/<id>`, `/api/v1/records/list`（weko-search-ui / weko-records-ui） |
| [API-13: 著者DB機能API](./API_13_author.md) | `/api/<v>/authors`（weko-authors） |
| [API-14: 利用規約取得API](./API_14_acquiring_application.md) | `/api/<v>/records/<pid>/files/<file>/terms` 他（weko-records-ui） |
| [API-15: 利用申請要否判定API](./API_15_application_decision.md) | `/api/<v>/records/<pid>/need-restricted-access`（weko-records-ui） |
| [API-16: アクティビティ一覧取得API](./API_16_activity_list.md) | `/api/<v>/workflow/activities`（weko-workflow） |
| [API-17: 承認API](./API_17_approval_activity.md) | `/api/<v>/workflow/activities/<id>/approve`,`/throw-out`（weko-workflow） |
| [API-18: CAPTCHA](./API_18_CAPTCHA.md) | `/api/v1/captcha/image`,`/validate`（weko-records-ui） |
| [API-19: リクエストメール送信API](./API_19_reqest_mail.md) | `/api/v1/records/<pid>/request-mail`（weko-records-ui） |
| [API-20: 一括インポートAPI](./API_20_bulk_import.md) | `/api/items/import-task`, `/api/items/import-task/get_bulk_import_task_status/<task_id>`（weko-items-ui） |
| [API Endpoint](./API_ENDPOINT_01.md) | エンドポイント一覧の入口 |
