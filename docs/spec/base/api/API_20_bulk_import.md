# 一括インポートAPI

## 目的・用途

SWORD APIや管理画面を介さず、ZIP（TSV/CSV・XML・JSON-LD等のメタデータを含む一括登録フォーマット）をOAuth2認証で一括登録／検証するためのAMS向け独自REST APIを提供する。  
画面インポートと同等の check→import パイプライン（`weko_search_ui.tasks.check_import_items_task` / `import_item`）を、OAuth2で保護したエンドポイントとして公開する。SWORD API（[API-6](./API_06_sword_api.md)）とは別系統の独自APIである。

## 利用方法

APIの認証にはOAuth2を利用する。  
アクセストークンの発行は[API-1:OAuth2](./API_01_Oauth2.md#oauth2)を参照。

### Scope：

一括インポート処理を行うためには以下のスコープが必要となる。

- item:bulkprocess（`weko_items_ui.scopes.item_bulk_process_scope`、group `item`）

### エンドポイント：

| 項番 | HTTP request | 内容 |
| :--: | ------------ | ---- |
| 1 | POST /api/items/import-task | ZIPファイルをアップロードし、アイテムの検証（check）または登録（import）を行う。 |
| 2 | GET /api/items/import-task/get_bulk_import_task_status/\<task_id> | 登録タスクの進捗・結果を取得する。 |

- いずれのエンドポイントも `weko_items_ui/views.py` の `blueprint_api`（`setup.py` の `invenio_base.api_blueprints` で登録、ベースパス `/api`、`url_prefix="/items"`）に定義される。
- 共通のデコレータ構成は `@oauth2.require_oauth()` → `@limiter.limit("")`（`weko_accounts.utils.limiter`）→ `@require_oauth_scopes(item_bulk_process_scope.id)`。POST側はさらに `@roles_required(WEKO_ITEMS_UI_BULK_IMPORT_ENABLE_ROLE)`（`weko_accounts.utils.roles_required`）を伴う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | -------------- | ---------------- | ------------------ | ------------ | ------------ | ------------------ |
| 利用可否 | 〇 | 〇 | × | × | × | × |

※ 〇：利用可能、×：利用不可

- 利用可能なロールは `WEKO_ITEMS_UI_BULK_IMPORT_ENABLE_ROLE`（既定 `["System Administrator", "Repository Administrator"]`）で制御する。

## 機能内容

- ZIP（一括登録フォーマット）をアップロードし、画面インポートと同等の check→import 処理を行う。
- `mode=check` では検証のみを行い、`mode=import`（既定）では検証後に登録処理を非同期実行する。
- 検証・登録タスクの情報はRedisに保存され、進捗取得エンドポイントで結果を参照できる。
- OAuthアクセストークンによるユーザー認証を必須とする。

## API仕様

### 一括インポート登録／検証機能：POST /api/items/import-task

#### エンドポイント
POST /api/items/import-task

#### クエリパラメータ

| パラメータ | 必須 | 値 | 説明 |
| ---------- | ---- | -- | ---- |
| mode | - | import（既定） / check | `check` は検証のみ、`import` は検証後に登録処理を実行する。 |
| is_change_identifier | - | true / false | 識別子を変更してインポートするか否か。 |

#### リクエストヘッダー

| ヘッダー | 必須 | 説明 | 例 |
| -------- | ---- | ---- | -- |
| Authorization | ○ | OAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。 | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4" |
| Content-Disposition | ○ | リクエストボディに付加したZIPファイルのファイル名を指定する。<br/>値が不正な場合は400を返す。 | "attachment; filename=example.zip" |
| Content-Type | ○ | リクエストボディにファイルを付加するため "multipart/form-data" を指定する。 | multipart/form-data; boundary=xxxxxxxx |

#### ボディ

| フィールド | 必須 | 説明 | 例 |
| ---------- | ---- | ---- | -- |
| file | ○ | form-data 形式でボディにZIPファイルを付加する。`request.files["file"]` が無い場合は404、ZIPとして不正な場合は400を返す。 | "file=@example.zip;type=application/zip" |

#### レスポンスコード

| コード | 説明 |
| ------ | ---- |
| 200 | 検証成功（`can_import:true`）または登録受付成功。 |
| 400 | 入力不正・無効ZIP・checkエラー・インポート不可・タイムアウト等（`can_import:false`）。 |
| 401 | 未認証。本文 `{"result":"NG","error":["Authentication is required."]}`。 |
| 403 | 権限不足、または他ユーザーのタスク参照。 |
| 404 | アップロードファイルが存在しない場合。 |
| 500 | サーバー内部エラー。 |

### 一括インポート進捗取得機能：GET /api/items/import-task/get_bulk_import_task_status/\<task_id>

#### エンドポイント
GET /api/items/import-task/get_bulk_import_task_status/\<task_id>

#### パスパラメータ

| キー | 必須 | 説明 |
| ---- | ---- | ---- |
| task_id | ○ | POST時に払い出されたタスクID。 |

#### レスポンスコード

| コード | 説明 |
| ------ | ---- |
| 200 | 全タスクが成功しエラーが無い場合（`can_import:true`）。 |
| 400 | タスクにエラーがある場合（`can_import:false`, `error_details`）、またはタスクデータのデコードに失敗した場合。 |
| 403 | タスクの登録ユーザーと現在ユーザーが一致しない場合。 |
| 404 | 指定した `task_id` がRedisに存在しない場合。 |

## レスポンス

成功時／失敗時とも独自形式のJSONを返す。主なフィールドは以下のとおり。

| フィールド | 説明 |
| ---------- | ---- |
| result | 成功時は登録・検証結果、失敗時は `"NG"`。 |
| error | 失敗時のエラーメッセージ配列。 |
| can_import | インポート可能か否か。 |
| check_status | チェック結果の状態。 |
| expire | タスクデータの有効期限。 |
| summary | 集計（total / new_item / update_item / check_error / warning）。 |
| error_details | エラー詳細。 |
| warning_details | 警告詳細。 |
| tasks | 非同期登録タスクの配列（item_task_id / task_status / task_result）。 |
| task_id | 払い出されたタスクID。 |

エラーレスポンスの本文形式は `{"result":"NG","error":[...]}`。401/403は当該エンドポイント時のみ `blueprint_api.errorhandler` によりJSON整形される。

## 関連モジュール

- weko-items-ui（API本体。`views.py` の `register_bulk_import_task` / `get_bulk_import_task_status`、`scopes.py` の `item_bulk_process_scope`、`config.py` の各設定）
- weko-search-ui（`tasks.check_import_items_task` / `tasks.import_item`、`utils.handle_metadata_by_doi`、`create_flow_define` / `handle_workflow`）
- weko-accounts（`utils.limiter` / `utils.roles_required`）
- invenio-oauth2server（スコープによる認証、`decorators.require_oauth_scopes`）
- Redis（タスクデータ保持）／Celery（非同期タスク実行）

## 関連設定値

| 設定キー | 既定値 | 説明 |
| -------- | ------ | ---- |
| WEKO_ITEMS_UI_BULK_IMPORT_TIMEOUT | 60 | checkタスク待機のタイムアウト（秒）。 |
| WEKO_ITEMS_UI_EXPIRE_TIME | 24 | タスクデータのRedis保持時間（時間）。 |
| WEKO_ITEMS_UI_BULK_IMPORT_ENABLE_ROLE | ["System Administrator", "Repository Administrator"] | 利用可能ロール。 |

## 処理概要

### POST /api/items/import-task（register_bulk_import_task）

1. `Content-Disposition: attachment; filename=...` からファイル名を取得する（不正なら400）。`request.files["file"]` が無ければ404とする。
2. クエリ `mode`（`import`（既定）/ `check`）、`is_change_identifier`（true/false）を取得する。ZIPを一時ディレクトリ（`tempfile.mkdtemp()`）へ保存し `zipfile.is_zipfile` で検証する（不正なら400）。
3. Celery `weko_search_ui.tasks.check_import_items_task` を `apply_async` し、`WEKO_ITEMS_UI_BULK_IMPORT_TIMEOUT` 秒までポーリングする。結果 `list_record` を集計し `summary`（total / new_item / update_item / check_error / warning）と `error_details` / `warning_details` を構築する。
4. タスク情報（user_id / created / expire / status / result / tasks / import_started / is_check_only）を `RedisConnection().connection(db=CACHE_REDIS_DB, kv=True)` に `task.id` キーで保存する（`WEKO_ITEMS_UI_EXPIRE_TIME` 時間有効）。
5. checkモードでは `task_id` を返し、`can_import` により 200／400 を返す。
6. importモードでは、`can_import` かつエラー無しのとき、各レコードに対し `create_flow_define`→`handle_workflow` を行い、DOI（`bulk_doi`）があれば `handle_metadata_by_doi` で補完したうえで `weko_search_ui.tasks.import_item` を `apply_async` する。`tasks[]`（item_task_id / task_status / task_result）をRedisへ更新する。監査ログは `UserActivityLogger`（action=IMPORT）に記録する。

### GET /api/items/import-task/get_bulk_import_task_status/\<task_id>（get_bulk_import_task_status）

1. Redisから `task_id` を取得する（無ければ404、デコード失敗は400）。
2. `task_data.user_id` と現在ユーザーが不一致なら403とする。
3. `import_item.AsyncResult` で各タスクのステータスを更新しRedisへ保存する。
4. 全タスク成功かつエラー無しで200（`can_import:true`）、それ以外は400（`can_import:false`, `error_details`）を返す。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2026/07/17 |  | v2.1.0差分反映：一括インポートAPI（`/api/items/import-task`、`item:bulkprocess`スコープ）の初版作成 |
