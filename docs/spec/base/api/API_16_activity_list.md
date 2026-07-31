# アクティビティ一覧取得API

-   目的・用途

本機能は、システムに登録されているアクティビティを取得する際に用いるAPIである。アクティビティの状態を指定することにより、取得するアクティビティを選別することが可能となる。

-   利用方法

リクエスト時に要求されているパラメータ(※処理概要参照)を指定しAPIを実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:-------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○            | ×           | ×                |

-   機能内容

-   システム管理者、リポジトリ管理者は全ユーザーのアクティビティ一覧を取得する。

-   コミュニティ管理者、登録ユーザーは自身が担当するアクティビティ一覧を取得する。

-   関連モジュール

-   weko-workflow.rest.py: GetActivities

-   weko-workflow.api.py: WorkActivity

-   weko-workflow.utils.py

-   weko-workflow.config.py

-   weko-workflow.errors.py

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。

-   ETagを用いて既に取得したことがあるデータか判定を行う。

-   アクティビティ一覧取得を行う場合、以下のように動作する。

    -   認証しているユーザーを確認する。

    -   リクエストパラメータからアクティビティ状態、取得するデータ件数、ページ数を取得する。

    -   関連モジュールを用いて該当するアクティビティ一覧を取得する。

    -   取得したアクティビティ一覧をjsonに格納して返却する。

-   URLはapi/:version/workflow/activities

  | パラメータ | 値           |
  |------------|--------------|
  | :version   | APIのバージョン |

-   リクエスト

    -   ヘッダ

  | キー名            | 値                                                    |
  |-------------------|-------------------------------------------------------|
  | Accept-Language   | 表示する言語の指定                                    |
  | Authorization     | Bearer アクセストークン                               |
  | If-None-Match     | 初回リクエスト時のレスポンスヘッダーに設定されているETagの値 |

-   ボディ

> 無し

-   パラメータ

| キー名   | 値 |
|--------|--------------------------------------------------|
| status | アクティビティの状態（※1）<br>・all : 登録・編集中、承認待、却下、終了<br>・wait : 承認待<br>・todo : 登録・編集中、却下 |
| limit  | 取得するデータ件数（※2） |
| page   | 取得可能なデータ総数をlimitの数値で分割した際の取得するページ（※3） |
| pretty | レスポンスの整形フラグ（※4）<br>・true, t, yes, 1：有効<br>・上記以外：無効 |

（※1）指定がない場合「todo」がデフォルトで設定される

（※2）指定がない場合「20」がデフォルトで設定される

（※3）指定がない場合「1」がデフォルトで設定される

（※4）指定がない場合「false(無効)」がデフォルトで設定される

-   レスポンス

    -   ヘッダ

  | キー名 | 値             |
  |--------|----------------|
  | ETag   | コンテンツのハッシュ値 |

-   ボディ

> アクティビティ一覧をJSON形式で返す（※詳細はAPI仕様書を参照）

-   異常系

    -   リクエストで与えたパラメータに不正があった場合、エラーコード400を返す（`InvalidParameterValueError`）

    -   Bearer認証に失敗した場合、エラーコード401を返す

    -   APIを利用できないロールだった場合、エラーコード403を返す（`PermissionError`）

    -   バージョンが未知の場合、エラーコード400を返す（`VersionNotFoundRESTError`）。サーバー内部エラー時は500（`InternalServerError`）

> 実装補足（v2.0.2）：
> - 実ハンドラは `weko_workflow.rest.GetActivities.get_v1`。認可は `@require_api_auth()` ＋ `@require_oauth_scopes(activity_scope.id)`（`user:activity`）＋ `@limiter.limit`。
> - ロール判定 `utils.check_role`（`WEKO_PERMISSION_ROLE_USER` に属するロールが対象。一般ユーザー・ゲスト不可）。全ユーザー分／自身担当分の切替は `api.WorkActivity.get_activity_list` 内の管理者判定による。
> - `Accept-Language` は `WEKO_WORKFLOW_API_ACCEPT_LANGUAGES`（`en` / `ja`）に含まれる場合のみ適用。`If-None-Match` 一致時は 304 を返す。
> - レスポンスボディの主フィールド：`total` / `condition{status,limit,page}` / `activities[{created,updated,activity_id,item_name,workflow_type,action,status,user}]`。
> - `status` 有効値：`todo` / `wait` / `all`（`WEKO_WORKFLOW_TODO_TAB` / `WAIT_TAB` / `ALL_TAB`）。
> - 関連config：`WEKO_WORKFLOW_REST_ENDPOINTS`、`WEKO_WORKFLOW_API_ACCEPT_LANGUAGES`、`WEKO_WORKFLOW_API_LIMIT_RATE_DEFAULT`、`WEKO_PERMISSION_ROLE_USER`。

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/06/15|初版作成   |
|2026/07/14|実装(v2.0.2)と突き合わせ。スコープ(user:activity)・ハンドラ`GetActivities.get_v1`・応答フィールド・追加エラー・configキーを追記|
