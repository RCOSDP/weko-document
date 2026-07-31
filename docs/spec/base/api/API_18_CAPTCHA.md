# CAPTCHA

- 目的・用途

本機能はリクエスト機能を用いてメールを送信時などに用いられるCAPTCHA（画像認証）機能を提供するAPIである。

- 利用方法

  - サンプルコード

    - CAPTCHA画像取得API

      ```bash
      curl <WEKO3のURL>/api/v1/captcha/image
      ```

    - CAPTCHA結果検証API

      ```bash
      curl -X POST -H "Content-Type: application/json" <WEKO3のURL>/api/v1/captcha/validate -d '{ "key": "aaa", "calculation_result": 20 }'
      ```

- 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

- 機能内容

  1. CAPTCHA画像取得API

     - CAPTCHA画像を取得する。

  2. CAPTCHA認証API

     - CAPTCHAの計算結果を検証、計算結果が正しい場合に認証トークンを生成する。

- 関連モジュール

  - weko-records-ui（ハンドラ `rest.CreateCaptchaImage` / `rest.CaptchaAnswerValidation`、生成・検証 `api.create_captcha_image` / `api.validate_captcha_answer`、画像生成 `captcha.py`）
  - weko-redis（`redis.RedisConnection`。Redis DBは `CACHE_REDIS_DB`）

> 実装補足（v2.0.2）：エンドポイントは `GET /api/v1/captcha/image`（`CreateCaptchaImage`）、`POST /api/v1/captcha/validate`（`CaptchaAnswerValidation`）。キーは `sha1(画像生成日時+ソルト)`、認証トークンは `sha256`（64桁）。Redis有効期限は `WEKO_RECORDS_UI_CAPTCHA_EXPIRATION_SECONDS`（900）、レスポンスTTLは `min(有効期限, WEKO_RECORDS_UI_CAPTCHA_TTL_SECONDS(600))`。

- 処理概要

    1. CAPTCHA画像取得API
       - サーバー負荷軽減のためリクエストのアクセス制限機能をかける。

       - リクエスト
         - API仕様書を参照
       - レスポンス
         - API仕様書を参照

       - APIの処理の流れ
         - CAPTCHA画像の生成を行う。
         - CAPTCHA画像の計算結果をRedisに保存する。
           - キー値は、画像生成日時とランダムなソルト値を組み合わせハッシュ化した値
         - 認証トークンを発行し、Redisに保存する。
           - 認証トークンは64文字のハッシュ値
         - 設定値により、Redisの有効期限を設定する。
         - レスポンスに設定するTTL値はRedisの有効期限より小さい値を設定する

    2. CAPTCHA認証API
       - サーバー負荷軽減のためリクエストのアクセス制限機能をかける。

       - リクエスト
         - API仕様書を参照
       - レスポンス
         - API仕様書を参照

       - APIの処理の流れ
         - CAPTCHAの計算結果を照合する。
           - 計算結果が異なる場合は400エラー。
         - 計算結果が正しい場合、Redisに格納されている認証トークンを返す。
           - 計算結果が間違っている場合、該当キーに登録されたRedisの情報を削除する。
         - 設定値により、Redisの有効期限を再設定する。
           - 設定値は、「CAPTCHA画像取得API」 で利用している設定値と同じ値を利用する。


- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2025/10/10 |  | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。ハンドラクラス(rest.py)・エンドポイント・キー/トークン生成方式・configキー(有効期限/TTL)・Redis接続を追記 |
