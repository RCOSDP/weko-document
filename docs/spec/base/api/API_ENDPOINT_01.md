# API Endpoint

invenio では、UI とAPI　のアプリケーションが２つあり（※）、統合して実行している。  
各アプリケーションに含まれるエンドポイントは以下を参照のこと。  
（invenioコマンドで取得できるエンドポイント一覧はUI部分のみ。APIはinvenio-baseをデバックして確認）

1.  UI [https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/ESFoWv7Q-LlLu2KJbQQyXBQBA2wOZ-3aFba9XQQRRsxMaA?e=FhDHyj](https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/ESFoWv7Q-LlLu2KJbQQyXBQBA2wOZ-3aFba9XQQRRsxMaA?e=FhDHyj)

2.  API [https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/EcR8uA8LSs5HtNFUrGgSmaIBULWfZ6yznzAMd6hIhqZlaw?e=l7Jvgg](https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/EcR8uA8LSs5HtNFUrGgSmaIBULWfZ6yznzAMd6hIhqZlaw?e=l7Jvgg)

補足（実装 v2.0.2）：APIアプリはベースパス `/api` にマウントされ、バージョン付きREST APIのフルパスは `/api/<version>/...`（現行 `v1`）となる。各機能のRESTエンドポイントは、モジュールごとの `*_REST_ENDPOINTS`（例：`WEKO_RECORDS_UI_REST_ENDPOINTS`、`WEKO_AUTHORS_REST_ENDPOINTS`、`WEKO_INDEX_TREE_REST_ENDPOINTS`、`WEKO_SEARCH_REST_ENDPOINTS`、`WEKO_WORKFLOW_REST_ENDPOINTS`）で定義され、各モジュールの `create_blueprint` によりAPIアプリへ登録される。

補足（release_v2.1.0）：

- RESTエンドポイントの定義 config（`*_REST_ENDPOINTS`）は、上記のほか `WEKO_ACCOUNTS_REST_ENDPOINTS`（ログイン／ログアウト）、`WEKO_ITEMS_UI_REST_ENDPOINTS`（ランキング）、`WEKO_RECORDS_UI_CITES_REST_ENDPOINTS`（引用・レコード／ファイル取得・統計）、`WEKO_RECORDS_REST_ENDPOINTS`（OAステータスコールバック）、`WEKO_SCHEMA_REST_ENDPOINTS`（`/api/schemas`）、`WEKO_DEPOSIT_REST_ENDPOINTS`（`/api/deposits/...`）、`WEKO_INDEXTREE_JOURNAL_REST_ENDPOINTS`、`RECORDS_REST_ENDPOINTS`（weko-search-ui で上書き。`/api/opensearch/search`、`/api/workspace/search` 等）、`IIIF_MANIFEST_ENDPOINTS`（`/api/iiif/v2/records/<pid_value>/manifest.json`）がある。
- 上記以外に、各モジュールの `setup.py` の `invenio_base.api_blueprints` で APIアプリに登録される Blueprint（weko-admin・weko-gridlayout の `/api/admin`、weko-items-ui の `/api/items`、weko-authors の `/api/authors`、weko-itemtypes-ui の `/api/itemtypes`、weko-items-autofill の `/api/autofill`、weko-workspace の `/api/workspaceAPI`、weko-index-tree、weko-notifications、weko-user-profiles、invenio-communities、invenio-files-rest、invenio-stats の `/api/stats`、invenio-iiif 等）があり、主に各画面から呼び出される。
- 外部から呼び出し可能なAPIの一覧と release_v2.1.0 での認可は [WEB API（README）](./README.md#個別のapi仕様書が無いapiの一覧release_v210) を参照。APIアプリでの未認証時は 401 JSON（`{"status": 401, "message": "Authentication required."}`）を返す（[README：認証・認可の共通事項](./README.md#認証認可の共通事項release_v210)）。
- 実装リポジトリには API台帳の差分検知ツール（`tools/api-inventory/`）が置かれているが、台帳データ本体は非公開リポジトリで管理されている。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。APIベースパス`/api/<version>`とモジュール別`*_REST_ENDPOINTS`定義を追記 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：REST エンドポイント定義 config・APIアプリ登録 Blueprint の一覧、未認証 401 応答、README の API 一覧への参照を追記 |
