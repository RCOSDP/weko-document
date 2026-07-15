# 利用申請が必要か判定するAPI

-   目的・用途

本機能はアイテムのコンテンツをダウンロードする際に、利用申請が必要かどうかを判定するAPIである。

-   利用方法

APIを実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○           | ○           | ○                |

-   機能内容

-   指定したアイテム内のコンテンツをログインユーザーがダウンロードする際に利用申請が必要かどうかを判定する。

-   関連モジュール

-   weko-records-ui（ハンドラ `rest.NeedRestrictedAccess`（`get_v1`）、権限判定 `permissions.check_file_download_permission` / `permissions.check_content_clickable`、ファイル一覧 `utils.get_file_info_list`）

> 実装補足（v2.0.2）：エンドポイントは `GET /api/<version>/records/<pid_value>/need-restricted-access`（`WEKO_RECORDS_UI_REST_ENDPOINTS['need_restricted_access']`）。認可は `@require_api_auth(True)`（allow_anonymous）＋ `@require_oauth_scopes(item_read_scope.id)`（`item:read`、weko-items-ui）。レスポンスは各ファイルの `{need_restricted_access, filename}` の配列。

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。

-   リクエスト

    -   API仕様書を参照

-   レスポンス

    -   API仕様書を参照

-   APIの処理の流れ

    -   レコードIDからレコードメタデータを取得する。

        -   ワークフローが完了していない場合は404エラー。

    -   レコードメタデータからファイル一覧を取得する(get_file_info_list)。

    -   ファイルでループ

        -   ファイルのアクセス権限を確認する(check_file_download_permission)。

        -   利用申請が必要なファイルか確認する(check_content_clickable)。

        -   アクセス権限なし、かつ、利用申請が必要なファイルの場合は、利用申請が必要と判定する。

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/7/14 |初版作成   |
|2026/07/14 |実装(v2.0.2)と突き合わせ。ハンドラ`NeedRestrictedAccess`・エンドポイント・スコープ(item:read)・レスポンス形式を追記|
