# 一括インポートタスク登録・ステータスチェックAPI

## 目的・用途

クライアントからメタデータ(tsv/csv)を含むzipファイルを受け取り、非同期で一括インポートタスク(インポート可否の事前チェック、およびアイテムの登録・更新)を実行する。<br>
実際の処理状況やインポート結果はタスク登録時に発行されるタスクIDを用いてステータス確認APIから取得する。

## 利用方法

APIの認証にはOAuth2を利用する。<br>
アクセストークンの発行は[API-1:OAuth2](./API_01_Oauth2.md#oauth2)を参照。

### Scope：
一括インポートタスクの登録、およびステータス確認を行うためには以下のスコープが必要となる。

- item:bulkprocess

#### 利用可能なロール

| ロール          | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録<br>ユーザー | 一般<br>ユーザー | ゲスト<br>(未ログイン) |
|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| 利用可否 | 〇 | 〇 | × | × | × | × |

### エンドポイント：

| 項番 | HTTP request                                      | 内容                                                                 |
|------|--------------------------------------------------|----------------------------------------------------------------------|
| 1    | POST /api/items/import-task | メタデータ(tsv/csv)を含むzipファイルをアップロードし、一括インポートタスクを登録する。                                   |
| 2    | GET /api/items/import-task/get_bulk_import_task_status/<task_id> | task_idを指定して、インポートタスクの処理状況や実行結果を取得する。      |

### POST /api/items/import-task

#### リクエスト

```shell
curl -X POST {hostname}/api/items/import-task?mode=<mode>&is_change_identifier=<is_change_identifier> \
  -F "file=@<filename>;type=application/zip" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Disposition:attachment; filename=<filename>"
```

- **クエリパラメータ**
  - `mode`：モード指定("import" または "check") 指定しなかった場合は"import"として扱われる。
  - `is_change_identifier`：識別子変更モード可否（true/false）指定しなかった場合はfalseとして扱われる。

- **フォームデータ**
  - `file`：アップロードするZIPファイル（MIMEタイプ: application/zip）<br>
  ※ ZIPファイルは[ADMIN_2_4.md](../admin/ADMIN_2_4.md)で使用するファイルと同様のものを使用する。<br>
  ※ TSVファイルの「.bulk_doi」に指定したDOI値
  で[DOIを使用したメタデータ補完機能](../user/USER_4_6.md#3-web-apiによるdoiを使用したメタデータ補完機能)を行うことが出来る。

- **HTTPヘッダー**
  - `Authorization`: Bearer <アクセストークン>
  - `Content-Disposition`: attachment; filename=〇〇.zip（添付ファイル名指定）

#### レスポンス

- インポートチェック処理のタイムアウト時間はデフォルトで60秒が設定されている。<br>
  この値は設定ファイルのWEKO_ITEMS_UI_BULK_IMPORT_TIMEOUTから変更可能。<br>
  ※ タイムアウト時間60秒で処理できるインポートファイル数は約250件。(実行環境による)
- タスク結果はexpire(有効期限)まで確認することが出来、デフォルトはタスク登録から24時間後に設定されている。<br>
  有効期限は設定ファイルのWEKO_ITEMS_UI_EXPIRE_TIMEから変更可能。

- **成功レスポンス インポートモード**
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
        },
        ...
    ],
    "task_id": <タスクID>,
  }
  ```

- **成功レスポンス チェックモード**
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
    "task_id": <タスクID>,
  }
  ```

- **エラーレスポンス**
  ```json
  {
    "result": "NG",
    "error": [<エラーメッセージ>]
  }
  ```

  ```json
  {
    "can_import": false,
    "check_status": "ERROR",
    "expire": "YYYY-MM-DD HH:mm:ss",
    "error_details": [ 
        <エラーメッセージ>
      ],
    "summary": {},
    "tasks": [],
    "task_id": <タスクID>
  }
  ```

#### レスポンスコード

| コード  |   内容  |
|--------------|--------------|
| 200 | 正常レスポンス |
| 400 | Content-Dispositionヘッダが不正、またはファイル名が取得できない場合 |
| 400 | リクエストボディに指定されたファイル名のファイルが存在しない場合 |
| 400 | アップロードされたファイルがZIP形式でない場合 |
| 400 | Celeryによるチェックタスクが失敗または強制終了した場合 |
| 400 | チェックタスクがタイムアウトした場合 | 
| 401 | アクセストークンが無効 |
| 403 | ロールがシステム管理者、もしくはリポジトリ管理者ではない場合 |
| 500 | その他例外発生時 |

---

### GET /api/items/import-task/get_bulk_import_task_status/<task_id>

#### リクエスト

```shell
curl -X GET {hostname}/api/items/import-task/get_bulk_import_task_status/<task_id> \
  -H "Authorization: Bearer <token>"
```

- **パスパラメータ**
  - `task_id`：タスクID

- **HTTPヘッダー**
  - `Authorization`: Bearer <アクセストークン>

#### レスポンス

- **成功レスポンス**
  ```json
  {
      "can_import": true,
      "check_status": "SUCCESS",
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
          },
          ...
      ],
      "task_id": <タスクID>
  }
  ```

- **エラーレスポンス**
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

#### レスポンスコード

|   レスポンス    |   内容  |
|--------------|--------------|
|  200 | 正常レスポンス |
|  400 | タスク情報のデコード失敗  |
|  400 | 上記以外のエラー発生時  |
|  401 | アクセストークンが無効 |
|  403 | ユーザーID不一致（登録ユーザー以外によるアクセス） |
|  404 | タスク情報が存在しない  |


### 関連モジュール

> weko\_items\_ui 

### 更新履歴

|   日付   |  GitHubコミットID  | 更新内容   |
|--------------|--------------|--------------|
| 3/31 |      | 新規作成  |


