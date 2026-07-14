## API Endpoint

invenio では、UI とAPI　のアプリケーションが２つあり（※）、統合して実行している。  
各アプリケーションに含まれるエンドポイントは以下を参照のこと。  
（invenioコマンドで取得できるエンドポイント一覧はUI部分のみ。APIはinvenio-baseをデバックして確認）

1.  UI [https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/ESFoWv7Q-LlLu2KJbQQyXBQBA2wOZ-3aFba9XQQRRsxMaA?e=FhDHyj](https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/ESFoWv7Q-LlLu2KJbQQyXBQBA2wOZ-3aFba9XQQRRsxMaA?e=FhDHyj)

2.  API [https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/EcR8uA8LSs5HtNFUrGgSmaIBULWfZ6yznzAMd6hIhqZlaw?e=l7Jvgg](https://rcosms-my.sharepoint.com/:x:/g/personal/hayashi_rcosms_onmicrosoft_com/EcR8uA8LSs5HtNFUrGgSmaIBULWfZ6yznzAMd6hIhqZlaw?e=l7Jvgg)

補足（実装 v2.0.2）：APIアプリはベースパス `/api` にマウントされ、バージョン付きREST APIのフルパスは `/api/<version>/...`（現行 `v1`）となる。各機能のRESTエンドポイントは、モジュールごとの `*_REST_ENDPOINTS`（例：`WEKO_RECORDS_UI_REST_ENDPOINTS`、`WEKO_AUTHORS_REST_ENDPOINTS`、`WEKO_INDEX_TREE_REST_ENDPOINTS`、`WEKO_SEARCH_REST_ENDPOINTS`、`WEKO_WORKFLOW_REST_ENDPOINTS`）で定義され、各モジュールの `create_blueprint` によりAPIアプリへ登録される。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。APIベースパス`/api/<version>`とモジュール別`*_REST_ENDPOINTS`定義を追記 |
