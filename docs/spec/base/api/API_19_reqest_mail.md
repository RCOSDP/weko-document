### リクエストメール送信API

- 目的・用途

本機能はアイテムに紐づくリクエスト送信先に、リクエストメールを送信するAPIである。

- 利用方法

  - サンプルコード

    ```bash
    curl -X POST -H "Content-Type: application/json" <WEKO3のURL>/api/v1/records/1/request-mail \
    -d '{ "from": "contributor@example.org",
    "subject": "About request mail",
    "message": "this is message of request mail.",
    "key": "aaa",
    "authorization_token": "68680b0b249e005b2d422393a17a9a3373ab6320d0d1af4d443336c0854602d8" }'
    ```

- 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

- 機能内容

  - 指定したアイテムに紐づくリクエスト送信先に、リクエストメールを送信する。

- 関連モジュール

  - weko-records-ui（ハンドラ `rest.RequestMail`（`post_v1`）、送信処理 `api.send_request_mail`）
  - weko-records（送信先取得 `api.RequestMailList.get_mail_list_by_item_id`）

- 処理概要

  - サーバー負荷軽減のためリクエストのアクセス制限機能をかける（`@limiter.limit`。OAuthデコレータは無く、未ログインでも実行可能）。

  - リクエスト
    - エンドポイント `POST /api/v1/records/<pid_value>/request-mail`（`WEKO_RECORDS_UI_REST_ENDPOINTS['send_request_mail']`）
    - 必須ボディ：`from`（送信元）/`subject`/`message`/`key`/`authorization_token`。`key` と `authorization_token` はCAPTCHA検証API（[API-18](./API_18_CAPTCHA.md)）が発行した値。不足時は400（`RequiredItemNotExistError`）

  - レスポンス
    - API仕様書を参照

  - APIの処理の流れ（実装 v2.0.2 の順序）

    - 認証トークン（`key` + `authorization_token`）をRedisと照合する。

      - 認証トークンの値が異なる場合は401エラー。

    - レコードIDからリクエスト送信先を取得する（`RequestMailList.get_mail_list_by_item_id`）。

      - リクエスト送信先が1件もない場合は404エラー。

    - 送信元メールアドレスの必須チェックおよびバリデーション（不正時は400）。

    - 入力情報を元にリクエスト送信先にメールを送信する。

      - 送信元宛には「Cc」ではなく、別途通知メール（recipients＝送信元）を送信する。本文には `WEKO_RECORDS_UI_REQUEST_MESSAGE` / `WEKO_RECORDS_UI_NOTIFICATION_MESSAGE` を連結する。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2025/10/10 |  | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。処理順序（トークン照合が先）に修正、送信元は「Cc」でなく別途通知メールである旨に修正、ハンドラ・エンドポイント・必須ボディ・configキーを追記 |