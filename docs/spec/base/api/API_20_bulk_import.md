# 一括インポートAPI

## 目的・用途

クライアントからメタデータ（TSV/CSV）を含むZIPファイルを受け取り、非同期で一括インポートタスク（インポート可否の事前チェック、およびアイテムの登録・更新）を実行する。  
実際の処理状況やインポート結果は、タスク登録時に発行されるタスクIDを用いてステータス確認APIから取得する。

画面インポート（[ADMIN_2_4：インポート](../admin/ADMIN_2_4.md)）と同等の check→import パイプライン（`weko_search_ui.tasks.check_import_items_task` / `import_item`）を、OAuth2で保護したエンドポイントとして公開する独自REST APIである。SWORD API（[API-6](./API_06_sword_api.md)）とは別系統である。

## 利用方法

APIの認証にはOAuth2を利用する。  
アクセストークンの発行は[API-1:OAuth2](./API_01_Oauth2.md#oauth2)を参照。

### Scope：

一括インポートタスクの登録、およびステータス確認を行うためには以下のスコープが必要となる。

- item:bulkprocess（`weko_items_ui.scopes.item_bulk_process_scope`、group `item`）

### エンドポイント：

| 項番 | HTTP request | 内容 |
| :--: | ------------ | ---- |
| 1 | POST /api/items/import-task | メタデータ（TSV/CSV）を含むZIPファイルをアップロードし、一括インポートタスクを登録する（`mode=check` の場合は検証のみ）。 |
| 2 | GET /api/items/import-task/get_bulk_import_task_status/\<task_id> | task_id を指定して、インポートタスクの処理状況や実行結果を取得する。 |

- いずれのエンドポイントも `weko_items_ui/views.py` の `blueprint_api`（`setup.py` の `invenio_base.api_blueprints` で登録、ベースパス `/api`、`url_prefix="/items"`）に定義される。
- 共通のデコレータ構成は `@oauth2.require_oauth()` → `@limiter.limit("")`（`weko_accounts.utils.limiter`）→ `@require_oauth_scopes(item_bulk_process_scope.id)`。POST 側はさらに `@roles_required(WEKO_PERMISSION_SUPER_ROLE_USER)`（`weko_accounts.utils.roles_required`）を伴う。

### CURLでのリクエスト実行例：

#### POST /api/items/import-task

```shell
curl -X POST "https://{hostname}/api/items/import-task?mode=<mode>&is_change_identifier=<is_change_identifier>" \
  -F "file=@<filename>;type=application/zip" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Disposition: attachment; filename=<filename>"
```

- ZIPファイルは [ADMIN_2_4：インポート](../admin/ADMIN_2_4.md) で使用するファイルと同様のもの（TSV/CSV形式のメタデータを含むZIP）を使用する。
- TSVファイルの「.bulk_doi」に指定したDOI値で、[DOIを使用したメタデータ補完機能](../user/USER_4_6.md#3-web-apiによるdoiを使用したメタデータ補完機能)を行うことができる。

#### GET /api/items/import-task/get_bulk_import_task_status/\<task_id>

```shell
curl -X GET "https://{hostname}/api/items/import-task/get_bulk_import_task_status/<task_id>" \
  -H "Authorization: Bearer <token>"
```

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | -------------- | ---------------- | ------------------ | ------------ | ------------ | ------------------ |
| 利用可否 | 〇 | 〇 | × | × | × | × |

※ 〇：利用可能、×：利用不可

- タスク登録（POST）のロール判定は `weko_records_ui.config.WEKO_PERMISSION_SUPER_ROLE_USER`（`["System Administrator", "Repository Administrator"]`）をモジュール読み込み時に import した値で行う。このため instance.cfg 等で同 config を上書きしても POST のロール判定には反映されない。
- ステータス確認（GET）にはロール判定は無く、スコープ `item:bulkprocess` を持つトークンのユーザーが、自身が登録したタスク（Redis に保存した `user_id` が一致するもの）のみ参照できる。他ユーザーのタスクは 403 となる。

## 機能内容

- ZIP（一括登録フォーマット）をアップロードし、画面インポートと同等の check→import 処理を行う。
- `mode=check` では検証のみを行い、`mode=import`（既定）では検証後に登録処理を非同期実行する。
- 検証・登録タスクの情報はRedisに保存され、ステータス確認エンドポイントで結果を参照できる。
- OAuthアクセストークンによるユーザー認証を必須とする。
- インポートチェック処理のタイムアウト時間は既定で60秒（`WEKO_ITEMS_UI_BULK_IMPORT_TIMEOUT`）。目安として、60秒で処理できるインポートアイテム数は約250件（実行環境による）。
- タスク結果は expire（有効期限）まで確認でき、既定はタスク登録から24時間後（`WEKO_ITEMS_UI_EXPIRE_TIME`）。

## API仕様

### 一括インポート登録／検証機能：POST /api/items/import-task

#### エンドポイント
POST /api/items/import-task

#### クエリパラメータ

| パラメータ | 必須 | 値 | 説明 |
| ---------- | ---- | -- | ---- |
| mode | - | import（既定） / check | `check` は検証のみ、`import` は検証後に登録処理を実行する。それ以外の値は `import` として扱う。 |
| is_change_identifier | - | true / false（既定） | 識別子変更モードでインポートするか否か。 |

#### リクエストヘッダー

| ヘッダー | 必須 | 説明 | 例 |
| -------- | ---- | ---- | -- |
| Authorization | ○ | OAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。 | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4" |
| Content-Disposition | ○ | `attachment; filename=...` 形式で、リクエストボディに付加したZIPファイルのファイル名を指定する。<br/>`attachment` でない、またはファイル名を取得できない場合は400を返す。 | "attachment; filename=example.zip" |
| Content-Type | ○ | リクエストボディにファイルを付加するため "multipart/form-data" を指定する。 | multipart/form-data; boundary=xxxxxxxx |

#### ボディ

| フィールド | 必須 | 説明 | 例 |
| ---------- | ---- | ---- | -- |
| file | ○ | form-data 形式でボディにZIPファイルを付加する。`request.files["file"]` が無い場合、ZIPとして不正な場合はいずれも400を返す。 | "file=@example.zip;type=application/zip" |

#### レスポンスコード

| コード | 説明 |
| ------ | ---- |
| 200 | 検証成功（`can_import:true`）または登録受付成功。 |
| 400 | Content-Disposition が不正／ファイル名を取得できない（`Cannot get filename by Content-Disposition.`）。 |
| 400 | リクエストボディにファイルが存在しない（`Not found <filename> in request body.`）。 |
| 400 | アップロードされたファイルがZIP形式でない（`Uploaded file is not a valid ZIP file.`）。 |
| 400 | チェック処理でファイル全体のエラーが返った場合（`{"result":"NG","error":[...]}`）。 |
| 400 | チェック結果にエラーのあるアイテムが含まれる場合（`can_import:false`、`check_status:"ERROR"`、`error_details`）。 |
| 400 | Celeryのチェックタスクが失敗・強制終了した場合（`check_status:"ERROR"`、`Check task failed.`）、またはタイムアウトした場合（`check_status:"TIMEOUT"`、`Check task timeout.`）。 |
| 401 | アクセストークンが無い・無効、または未認証（`{"result":"NG","error":["Authentication is required."]}`）。 |
| 403 | ロールがシステム管理者・リポジトリ管理者でない、またはトークンのスコープ不足（`{"result":"NG","error":["Permission required."]}`）。 |
| 429 | レート制限超過（`@limiter.limit("")`、`weko_accounts.utils.limiter` の既定制限）。 |
| 500 | その他の例外発生時（`{"result":"NG","error":["Internal Server Error"]}`）。 |

#### レスポンス

- 成功レスポンス（インポートモード）

  ```json
  {
    "can_import": true,
    "check_status": "SUCCESS",
    "expire": "YYYY-MM-DD HH:mm:ss",
    "summary": {
      "total": <総件数>,
      "new_item": <新規登録数>,
      "update_item": <更新数>,
      "check_error": <エラー数>,
      "warning": <警告数>
    },
    "tasks": [
      {
        "item_task_id": <インポートタスクID>,
        "task_status": "PENDING",
        "task_result": {}
      }
    ],
    "task_id": <タスクID>
  }
  ```

- 成功レスポンス（チェックモード）：`tasks` は空配列となる。

  ```json
  {
    "can_import": true,
    "check_status": "SUCCESS",
    "expire": "YYYY-MM-DD HH:mm:ss",
    "summary": {
      "total": <総件数>,
      "new_item": <新規登録数>,
      "update_item": <更新数>,
      "check_error": <エラー数>,
      "warning": <警告数>
    },
    "tasks": [],
    "task_id": <タスクID>
  }
  ```

  - `check_status` は、エラーのあるアイテムがあれば `ERROR`、警告のみであれば `WARNING`、いずれも無ければ `SUCCESS`。警告がある場合は `warning_details`（警告メッセージ配列）を、エラーがある場合は `error_details` を併せて返す。
  - `update_item` は、チェック結果の `status` が `keep` または `upgrade` のアイテム数。

- エラーレスポンス（入力不正・認証／認可エラー等）

  ```json
  {
    "result": "NG",
    "error": [<エラーメッセージ>]
  }
  ```

- エラーレスポンス（チェックエラー）

  ```json
  {
    "can_import": false,
    "check_status": "ERROR",
    "expire": "YYYY-MM-DD HH:mm:ss",
    "error_details": [<エラーメッセージ>],
    "summary": { ... },
    "tasks": [],
    "task_id": <タスクID>
  }
  ```

  チェックタスクの失敗・タイムアウト時は `summary` が空、`task_id` が空文字で、`expire` を含まない。

### 一括インポート進捗取得機能：GET /api/items/import-task/get_bulk_import_task_status/\<task_id>

#### エンドポイント
GET /api/items/import-task/get_bulk_import_task_status/\<task_id>

#### パスパラメータ

| キー | 必須 | 説明 |
| ---- | ---- | ---- |
| task_id | ○ | POST時に払い出されたタスクID。 |

#### リクエストヘッダー

| ヘッダー | 必須 | 説明 |
| -------- | ---- | ---- |
| Authorization | ○ | "Bearer" + " (半角スペース)" + "アクセストークン"の形式。 |

#### レスポンスコード

| コード | 説明 |
| ------ | ---- |
| 200 | タスク情報の `status` が `ERROR` 以外の場合（`can_import:true`）。インポートタスクが実行中（`PENDING` 等）の場合も200となる。 |
| 400 | タスク情報の `status` が `ERROR` の場合（`can_import:false`、`error_details`）。 |
| 400 | タスク情報のデコードに失敗した場合（`Task data decode error.`）、その他の例外（`Task check failed.: ...`）。 |
| 401 | アクセストークンが無い・無効、または未認証。 |
| 403 | タスクの登録ユーザーと現在ユーザーが一致しない場合（`Permission denied.`）、またはトークンのスコープ不足。 |
| 404 | 指定した `task_id` がRedisに存在しない（有効期限切れを含む）場合（`Task not found.`）。 |
| 429 | レート制限超過。 |

#### レスポンス

- 成功レスポンス

  ```json
  {
    "can_import": true,
    "check_status": <状態>,
    "expire": "YYYY-MM-DD HH:mm:ss",
    "tasks": [
      {
        "item_task_id": <インポートタスクID>,
        "task_status": <状態>,
        "task_result": {
          "recid": <レコードID>,
          "start_date": <インポート開始時間>,
          "success": true
        }
      }
    ],
    "task_id": <タスクID>
  }
  ```

  - `task_status` は Celery の `import_item.AsyncResult(item_task_id).status`（`PENDING` / `STARTED` / `SUCCESS` / `FAILURE` 等）。`check_status` は最後に参照したインポートタスクの状態で更新される。
  - 注：`check_status` が `ERROR` でなければ200（`can_import:true`）を返すため、個々のインポートタスクが `FAILURE` の場合でも200となりうる。各アイテムの成否は `tasks[].task_status` / `task_result` で確認する。

- エラーレスポンス

  ```json
  {
    "can_import": false,
    "check_status": "ERROR",
    "expire": "YYYY-MM-DD HH:mm:ss",
    "error_details": <エラー内容>,
    "tasks": [],
    "task_id": <タスクID>
  }
  ```

  ```json
  {
    "result": "NG",
    "error": [<エラーメッセージ>]
  }
  ```

- 401/403 の本文 `{"result":"NG","error":[...]}` は、当該2エンドポイントに限り `blueprint_api.errorhandler(401/403)` により整形される。

## 関連モジュール

- weko-items-ui（API本体。`views.py` の `register_bulk_import_task` / `get_bulk_import_task_status` / `handle_unauthorized_error` / `handle_forbidden_error`、`scopes.py` の `item_bulk_process_scope`、`config.py` の各設定）
- weko-search-ui（`tasks.check_import_items_task`（内部で `utils.check_tsv_import_items`）/ `tasks.import_item`、`utils.handle_metadata_by_doi`、`create_flow_define` / `handle_workflow`）
- weko-records-ui（`config.WEKO_PERMISSION_SUPER_ROLE_USER`）
- weko-accounts（`utils.limiter` / `utils.roles_required`）
- weko-logging（`UserActivityLogger`）
- invenio-oauth2server（`provider.oauth2.require_oauth`、`decorators.require_oauth_scopes`）
- Redis（タスクデータ保持）／Celery（非同期タスク実行）

## 関連設定値

| 設定キー | 既定値 | 説明 |
| -------- | ------ | ---- |
| WEKO_ITEMS_UI_BULK_IMPORT_TIMEOUT | 60 | checkタスク待機のタイムアウト（秒）。 |
| WEKO_ITEMS_UI_EXPIRE_TIME | 24 | タスクデータのRedis保持時間（時間）。 |
| WEKO_PERMISSION_SUPER_ROLE_USER（weko-records-ui） | ["System Administrator", "Repository Administrator"] | POST の利用可能ロール（モジュール読み込み時の値で固定）。 |

## 処理概要

### POST /api/items/import-task（register_bulk_import_task）

1. `Content-Disposition: attachment; filename=...` からファイル名を取得する（`attachment` でない、またはファイル名が無ければ400）。`request.files["file"]` が無ければ400とする。
2. クエリ `mode`（`import`（既定）/ `check`）、`is_change_identifier`（true/false、既定false）を取得する。ZIPを一時ディレクトリ（`tempfile.mkdtemp()`）へ保存し `zipfile.is_zipfile` で検証する（不正なら400）。
3. Celery `weko_search_ui.tasks.check_import_items_task` を `apply_async` し、`WEKO_ITEMS_UI_BULK_IMPORT_TIMEOUT` 秒までポーリングする。結果に `error` があれば400（`result:"NG"`）とする。結果 `list_record` を集計し `summary`（total / new_item / update_item / check_error / warning）と `error_details` / `warning_details` を構築する。タスクが `FAILURE`/`REVOKED` の場合、またはタイムアウトの場合は400とする。
4. タスク情報（user_id / created / expire / status / result / tasks / import_started / is_check_only）を `RedisConnection().connection(db=CACHE_REDIS_DB, kv=True)` に `task.id` キーで保存する（`WEKO_ITEMS_UI_EXPIRE_TIME` 時間有効）。
5. checkモードでは `task_id` を返し、`can_import` により 200／400 を返す。
6. importモードでは、`can_import`（エラーのあるアイテムが無い）のとき、各レコードに対し `create_flow_define`→`handle_workflow` を行い、DOI（`bulk_doi`）があれば `handle_metadata_by_doi` で補完したうえで `weko_search_ui.tasks.import_item` を `apply_async` する。`tasks[]`（item_task_id / task_status / task_result）をRedisへ更新する（TTL は維持）。`request_info` の action は `IMPORT`（`UserActivityLogger` の要約情報を付加）。

### GET /api/items/import-task/get_bulk_import_task_status/\<task_id>（get_bulk_import_task_status）

1. Redisから `task_id` を取得する（無ければ404、デコード失敗は400）。
2. `task_data.user_id` と現在ユーザーが不一致なら403とする。
3. `import_item.AsyncResult` で各タスクのステータス・結果を更新し、Redisへ保存する（TTL は維持）。
4. `task_data.status` が `ERROR` 以外なら200（`can_import:true`）、`ERROR` なら400（`can_import:false`, `error_details`）を返す。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2026/07/17 |  | v2.1.0差分反映：一括インポートAPI（`/api/items/import-task`、`item:bulkprocess`スコープ）の初版作成 |
| 2026/07/31 |  | 別ファイル `API_20_bulk_import_api.md`（一括インポートタスク登録・ステータスチェックAPI）として新規作成（curl例・レスポンス例・ロール表） |
| 2026/10/05 | 508030789 | release_v2.1.0突合：`API_20_bulk_import_api.md` を本ファイルに統合（curl例・レスポンス例を取り込み）。POSTのロール判定を実装準拠（`WEKO_PERMISSION_SUPER_ROLE_USER`、存在しない `WEKO_ITEMS_UI_BULK_IMPORT_ENABLE_ROLE` を削除）に修正、ファイル未指定時を404→400に修正、レスポンスコード（チェックエラー・タイムアウト・429）、GETの判定条件（`status`≠ERROR で200）とロール判定なしを追記 |
