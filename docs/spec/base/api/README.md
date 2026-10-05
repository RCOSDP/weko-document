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

## 認証・認可の共通事項（release_v2.1.0）

- **未認証時の応答**：APIアプリ（`/api/` 配下）では、`login_required` 等で未認証と判定された場合、401 と JSON `{"status": 401, "message": "Authentication required."}` を返す（`weko_accounts.unauthorized.install(app, api_only=True)`）。v2.0.x では API アプリにログイン画面が無いため 500 になっていた。UI アプリでも AJAX/fetch 等の機械的な呼び出しには同じ 401 JSON を返し、通常の画面遷移はログイン画面へリダイレクトする。`WEKO_ACCOUNTS_UNAUTHORIZED_JSON`（既定 True）で制御する。詳細は [アクセスコントロール：ログイン](../access_control/API_LOGIN_01.md) を参照。
  - OAuth2 のトークンが無い・無効な場合（`@oauth2.require_oauth()`）は従来どおり 401、スコープ不足（`@require_oauth_scopes`）は 403。SWORD API（`/sword/...`）・一括インポートAPIなど、Blueprint 単位のエラーハンドラを持つ API は各仕様書記載の本文形式で返す。
- **ログインAPI**（`POST /api/<version>/login`）：失敗応答は存否を区別しない 403 `InvalidCredentialsError`／400 `InvalidLoginRequestError` に統一され、ログインAPIのみ `WEKO_API_LIMIT_RATE_DEFAULT`（既定 `['100 per minute']`）でレート制限（超過時 429）される。詳細は [アクセスコントロール：ログイン](../access_control/API_LOGIN_01.md)。
- **ファイル権限の管理者判定**：`check_file_download_permission` 等で無条件に許可される管理者は、システム管理者・リポジトリ管理者と、当該アイテムが所属するコミュニティを担当するコミュニティ管理者に限られる（`weko_records_ui.permissions.is_superuser_or_record_comadmin`）。

## 個別のAPI仕様書が無いAPIの一覧（release_v2.1.0）

外部から呼び出し可能なAPI（機械向けエンドポイント）のうち、本カテゴリに個別の仕様書が無いものと、その認可を示す。認可欄の「v2.1.0」は b19e39d8a 以降（issue62569 / issue62807 / PR #1924〜#1931）で追加・変更されたもの。

| エンドポイント | モジュール | 認可・応答（release_v2.1.0） | 参照 |
| --- | --- | --- | --- |
| `POST /api/<v>/login`、`POST /api/<v>/logout` | weko-accounts（`rest.WekoLogin` / `WekoLogout`） | 上記「ログインAPI」参照（v2.1.0） | [ログイン](../access_control/API_LOGIN_01.md) |
| `GET /api/<v>/records/<pid>/files/<filename>`、`.../files/all`、`POST .../files/selected`、`GET /api/<v>/records/<pid>/stats`、`.../files/<filename>/stats` | weko-records-ui（`rest.WekoFilesGet` 他） | レコード stats は `item:read`、ファイル系は `file:read` スコープ＋詳細画面と同じ閲覧権限（`page_permission_factory`）。ファイル取得はダウンロード権限も判定 | [ファイル](../access_control/API_FILE_01.md) |
| `GET /api/<v>/ranking/<ranking_type>`、`/api/<v>/ranking/<pid>/files` | weko-items-ui（`rest`） | `ranking:read` スコープ | [ファイル](../access_control/API_FILE_01.md) |
| `POST /api/<v>/oa_status/callback` | weko-records | OA Assist 連携 | [OAステータス](../access_control/API_OA_STATUS_01.md) |
| `GET /api/record/cites/<pid>` | weko-records-ui（`rest.WekoRecordsCitesResource`） | v2.1.0：`@require_api_auth(allow_anonymous=True)`＋`item:read` スコープを付与し、詳細画面と同じ閲覧権限（`page_permission_factory`）が無い場合は 404（"Not found"）。`style`（既定 `aapg-bulletin`）/`locale`（既定 `en-US`）で引用文字列（citeproc）を返す | － |
| `GET /api/stats/<record_id>`、`POST /api/stats/<record_id>`（閲覧数）、`GET/POST /api/stats/<bucket_id>/<file_key>`（ファイル統計） | invenio-stats（`views.QueryRecordViewCount` / `QueryFileStatsCount`） | v2.1.0：レコードの閲覧権限（`page_permission_factory`）が必要。ID不正 400、レコード不存在 404、閲覧不可 403（`permissions.record_view_permission_required` / `bucket_view_permission_required`）。POST の `date` は `total` または `YYYY-MM`（不正は 400） | － |
| `GET /api/stats/<target_report>/...`、`/api/stats/report/...`、`/api/stats/tasks/<task_name>` 等（レポート系） | invenio-stats | `STATS_PERMISSION_FACTORY`（`weko_permission_factory`）による `stats_api_access_required`。v2.1.0 で `QueryCommonReports`（`/api/stats/<event>/<year>/<month>`）にも適用 | － |
| `GET /api/iiif/v2/<uuid>/...`（画像配信、info.json） | invenio-iiif（`handlers.protect_api`） | v2.1.0：レコードの閲覧権限かつファイルのダウンロード権限（`permissions.iiif_object_permission_factory`）が無い場合は 404。レコードに属さないオブジェクトは invenio-files-rest の `object-read` 権限 | － |
| `GET /api/iiif/v2/records/<pid_value>/manifest.json` | invenio-iiif（`views.manifest_view`） | v2.1.0：`IIIF_MANIFEST_ENDPOINTS['recid']['permission_factory_imp']`＝`page_permission_factory`。閲覧不可は未ログイン 401／ログイン済み 403。マニフェストにはダウンロード可能なファイルのみ列挙 | － |
| `POST /api/schemas/`、`POST /api/schemas/<pid_value>`、`PUT /api/schemas/put/<pid_value>/<path:key>` | weko-schema-ui（`rest.SchemaFilesResource`） | v2.1.0：`@login_required`（未認証 401）＋`schema_permission`（`schema-access` アクション、不足は 403）。OAIスキーマ管理画面から利用（`require_api_auth` から変更） | [OAIスキーマ](../admin/ADMIN_1_3.md) |
| `PUT/POST /api/deposits/redirect/<pid_value>`、`PUT /api/deposits/publish/<pid_value>` | weko-deposit（`rest.ItemResource` / `publish`） | v2.1.0：未認証 401、対象アイテムの編集権限（`weko_items_ui.permissions.edit_permission_factory`）が無い場合 403、アイテム不存在 404（`require_item_edit_permission`、publish は `@login_required`＋同判定）。バージョン付き pid は親 recid で判定 | － |
| `GET/PUT/DELETE /api/deposits/items/<pid_value>` 等（invenio-deposit 系 depid ルート） | weko-deposit（`DEPOSIT_REST_ENDPOINTS['depid']`） | v2.1.0：更新系の権限判定 `update_permission_factory_imp` に `weko_items_ui.permissions:edit_permission_factory` を設定（従来は未設定） | － |
| `/api/files/<bucket_id>/<key>` 等（ファイル操作） | invenio-files-rest | v2.1.0：ゲスト（未ログイン、ゲストトークンでのアクティビティ）による操作は、当該トークンのアクティビティのアイテム（およびその親バージョン）のバケットに限定（`permissions.get_guest_activity_bucket_ids`） | － |
| `GET /get_path_name_dict/<path_str>`（インデックス名取得） | weko-search-ui（UI アプリ） | v2.1.0：`path_str` の各要素が数値（1〜18桁）でない場合 400。閲覧権限（`check_index_permissions`）の無いインデックスは結果に含めない | － |
| `HEAD /records/<pid_value>`（Signposting） | weko-signposting（`RECORDS_UI_ENDPOINTS['recid_signposting']`） | v2.1.0：アイテム詳細画面と同じ閲覧権限（`permission_factory_imp`＝`page_permission_factory`）を適用 | [Signposting](../other/SIGNPOSTING_01.md) |
| `/resync/...`、`/.well-known/resourcesync`（ResourceSync） | invenio-resourcesyncserver | v2.1.0：レコード単位のルート（`file_content.zip`、`resourcedump_manifest.xml`、`changedump_manifest.xml`、`change_dump_content.zip`）は公開アイテム（公開状態・公開日到来・公開インデックス）以外 404（`permissions.public_record_required`）。変更リストの検索対象は公開・削除状態のアイテムに限定。manifest に列挙するファイルはダウンロード可能なもの（`can_download_file`）に限定 | [ResourceSync](../access_control/ADMIN_RESOURCE_SYNC_01.md) |
| `POST /handle/retrieve`、`/handle/register`、`/handle/delete` | weko-handle（UI アプリ） | v2.1.0：`@login_required`＋システム管理者・リポジトリ管理者のみ（`roles_required`） | － |
| `POST /items/validate_bibtext_export`（BibTeX 出力検証、ルート名は実装のまま） | weko-items-ui | v2.1.0：`record_ids` がリストでない等は 400。閲覧権限（`page_permission_factory`）の無いレコードは存在しないレコードと同様に「出力不可」として返す | [エクスポート](../user/USER_2_4.md) |

- 上記のほか、`/api/admin/...`（weko-admin・weko-gridlayout）、`/api/items/...`（weko-items-ui）、`/api/authors/...`、`/api/itemtypes/...`、`/api/autofill/...`、`/api/workspaceAPI/...` 等は各画面から呼ばれる内部API（各画面の仕様書を参照）。v2.1.0 では、API認証情報の参照（`/api/admin/get_api_cert_type`、`/api/admin/get_curr_api_cert/<api_code>`：システム管理者のみ）、検索設定用インデックス取得（`/api/admin/search/init_display_index/<selected_index>`：システム／リポジトリ管理者のみ）、サイトライセンスメール送信設定の取得（システム／リポジトリ管理者のみ）、送信履歴の取得・手動送信（対象リポジトリが担当範囲内かを検証）、ウィジェット設定の保存・削除（`repository_scope_required` によるリポジトリスコープ検証）などに認可が追加されている。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2026/10/05 | 508030789 | release_v2.1.0突合：認証・認可の共通事項（未認証401統一・ログインAPI・ファイル権限の管理者判定）と、個別仕様書の無いAPIの一覧（cites・統計・IIIF・/api/schemas・deposits・Signposting・ResourceSync・weko-handle・BibTeX 等の認可）を追記。API-20 を `API_20_bulk_import.md` に一本化 |
