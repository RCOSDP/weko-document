# 承認API

-   目的・用途

本機能はアクティビティを承認するAPIである。

-   利用方法

APIを実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:-------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○           | ×           | ×                |

-   機能内容

-   指定したアクティビティをログイン中のユーザーで承認する。

-   関連モジュール

-   weko_workflow.rest.py

-   weko_workflow.views.py

-   weko_workflow.utils.py

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。

-   アクティビティ情報を取得する(get_activity_display_info)。

    -   取得できない場合は404エラー。

    -   アクティビティのステータスが承認でない場合は400エラー。

-   承認可能かどうかをチェックする(check_authority_action)。

    -   不可の場合はユーザー権限なしとして403エラー。

-   承認を行う(next_action)。

-   レスポンスに必要な情報を取得する。

    -   承認した情報を取得する(workflow_action_historyから最新の情報を取得)。

    -   フローから次のアクションを取得する。

> 実装補足（v2.0.2）：エンドポイントは `POST /api/<version>/workflow/activities/<activity_id>/approve`、ハンドラは `weko_workflow.rest.ApproveActivity`（`post_v1`）。認可は `@require_api_auth()` ＋ `@require_oauth_scopes(activity_scope.id)`（`user:activity`）＋ `@limiter.limit`。ステータスが承認(`action_endpoint=='approval'`)でない場合は `StatusNotApproveError`(400)、承認権限が無い場合は `check_authority_action` により `PermissionError`(403)。応答は `next_action{id,endpoint}` ＋ `action_info{action_id,action_date,action_user,action_status,action_comment}`（履歴は `action_id==4`＝approval でフィルタし最新を取得）。※アクティビティ取得不可時の明示的な404処理は実装に無い。

-   リクエスト

    -   API仕様書を参照

-   レスポンス

    -   API仕様書を参照

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/7/4  |初版作成   |
|2026/07/14|実装(v2.0.2)と突き合わせ。エンドポイント/ハンドラ(ApproveActivity/ThrowOutActivity)・スコープ・エラークラス・応答フィールド・却下は前アクション差戻しである点を追記|

# 却下API

-   目的・用途

本機能はアクティビティを却下するAPIである。

-   利用方法

APIを実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○           | ○           | ×                |

-   機能内容

-   指定したアクティビティをログイン中のユーザーで却下する。

-   関連モジュール

-   weko_workflow.rest.py

-   weko_workflow.views.py

-   weko_workflow.utils.py

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。

-   アクティビティ情報を取得する(get_activity_display_info)。

    -   取得できない場合は404エラー。

    -   アクティビティのステータスが承認でない場合は400エラー。

-   却下可能かどうかをチェックする(check_authority_action)。

    -   不可の場合はユーザー権限なしとして403エラー。

-   却下を行う(previous_action)。

-   レスポンスに必要な情報を取得する。

    -   却下した情報を取得する(workflow_action_historyから最新の情報を取得)。

    -   フローから次のアクションを取得する。

> 実装補足（v2.0.2）：エンドポイントは `POST /api/<version>/workflow/activities/<activity_id>/throw-out`、ハンドラは `weko_workflow.rest.ThrowOutActivity`（`post_v1`）。却下は `previous_action`（前アクションへ差戻し）で実行する。認可・エラー（`StatusNotApproveError`(400) / `PermissionError`(403)）は承認APIと同じく `check_authority_action` に一本化されており、「利用可能なロール」表の承認/却下の差はコードには存在しない。応答は `ApproveActivity.create_approve_response` を流用し、承認(approval, `action_id==4`)履歴を返す。

-   リクエスト

    -   API仕様書を参照

-   レスポンス

    -   API仕様書を参照

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/7/4  |初版作成   |
|2026/07/14|実装(v2.0.2)と突き合わせ。エンドポイント/ハンドラ(ApproveActivity/ThrowOutActivity)・スコープ・エラークラス・応答フィールド・却下は前アクション差戻しである点を追記|
