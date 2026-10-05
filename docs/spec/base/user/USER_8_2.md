# ログイン

## 目的・用途

本機能は、サインアップ済みのユーザーがログインするための機能である。

## 利用方法

ユーザー画面のヘッダから［ログイン（Log in）］ボタンを押す。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

## 機能内容

- ユーザー画面のヘッダから［ログイン（Log in）］ボタンを押すと、ログイン画面に移動する

  - コンフィグの以下設定値の組み合わせに応じて、該当ログイン画面に移動する  
    （シボレスログイン処理について、[ADMIN-14-19: Shibboleth](../admin/ADMIN_14_19.md) を参照）

    1. WEKO login only:

       - WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = False

    2. WEKO login + Shibbolth(Idp):

       - WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = True

       - WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED = True

    3. WEKO login + Shibbolth(DS):

       - WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = True

       - WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED = False

    4. Shibbolth(Idp):

       - WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = True

       - WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED = True

       - WEKO_ACCOUNTS_SHIB_INST_LOGIN_DIRECTLY_ENABLED = True

    5. Shibbolth(DS)

       - WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = True

       - WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED = False

       - WEKO_ACCOUNTS_SHIB_DP_LOGIN_DIRECTLY_ENABLED = True

- WEKOのログイン画面からログインする

  - 表示言語はヘッダにて選択しているシステム言語とする

  - メールアドレスとパスワードのテキストボックスを設ける

  - ［ログイン（Log In）］ボタン、「サインアップ」（Sign Up）リンク、「パスワードをお忘れの方はこちら」（Forgot password?）リンクを設ける

    - ［ログイン（Log In）］ボタンを押すと、入力した情報で、ログインリクエストを送信する

      - 問題なければ、もともとのユーザー画面に移動する

      - エラーがあった場合、エラー内容を メールアドレスとパスワードのテキストボックスの上部に表示させる

        - メールアドレス、またはパスワードを入力しない場合  
          エラーメッセージ：「{} not provided」

        - メールアドレス、またはパスワードを正しく入力しない場合  
          エラーメッセージ：「Specified user does not exist」

    - 「サインアップ」（Sign Up）リンクを押すと、アカウント登録画面に移動する

    - 「パスワードをお忘れの方はこちら」（Forgot password?）リンクを押すと、リセットパスワード画面に移動する

## 関連モジュール

- Flask-Security（ログイン画面・文言を提供）
- invenio_accounts（セッション記録・ユーザーデータストアを提供）
- weko-accounts（Shibboleth関連ビューを提供）

## 関連テーブル

- accounts_user_session_activity
- accounts_user

## 処理概要

ログイン画面の種類を決定するコンフィグは、instance.cfgまたはweko-accountsのconfig.pyで設定する。両方で設定されている場合、instance.cfgの設定が優先される。

- パス（instance.cfg）：  
  https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg

- パス（config.py）：  
  <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py>

- 対象となるコンフィグは以下の通り。

  - WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED

  - WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED

  - WEKO_ACCOUNTS_SHIB_INST_LOGIN_DIRECTLY_ENABLED

ログイン画面・文言は依存ライブラリ Flask-Security（`flask_security.views.login`、route `/login/`）に由来する。

ログインボタンを押すと、invenio-accountsのsessions.pyにあるlogin_listenerからadd_sessionが呼び出される。

- ログイン時には、accounts_user_session_activityテーブルとredisにセッション情報を記録して、accounts_userテーブルの最終ログイン情報を更新する。

- 登録するセッション情報を以下に示す。

| セッション情報 | 登録内容 |
|------------|-------------------------------------------|
| sid_s | セッションID |
| user_id | ユーザID |
| ip | IPアドレス |
| country | 国名 |
| browser | ブラウザ |
| browser_version | バージョン |
| os | os |
| device | デバイス |
| orgniazation_name（綴りママ・invenio-accounts側の列） | shibboleth認証を行った機関の名称<br> 本項目には、Shibboleth認証時にレスポンスのボディで返却されるJaOrganizationName(jao)の値を設定する。 <br> ローカル認証およびJaOrganizationNameが返却されなかった場合はNullとする。 |

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足：ログイン画面・文言は **Flask-Security**（`flask_security.views.login`、route `/login/`）由来。セッション記録は `invenio_accounts.sessions`（`login_listener`→`add_session`、table `accounts_user_session_activity`）。所属機関名は invenio-accounts 側の列 `orgniazation_name`（綴りママ。ローカル認証時は Null）。Shibboleth 関連の実ビューは weko-accounts（`shib_login` / `shib_sp_login` 等）。config `WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED`（既定 False）/ `_SHIB_IDP_LOGIN_ENABLED` / `_SHIB_INST_LOGIN_DIRECTLY_ENABLED` / `_SHIB_DP_LOGIN_DIRECTLY_ENABLED`。

- 実装補足（v2.1.0、未ログイン時の応答）：`login_required` で未ログインと判定された場合の応答は `weko_accounts.unauthorized`（`WekoAccounts.init_unauthorized_handler` が login_manager の unauthorized handler として登録。`WEKO_ACCOUNTS_UNAUTHORIZED_JSON`、既定 True）が決める。UI アプリでは、画面遷移（`Sec-Fetch-Dest` が `document`／`iframe`／`frame`／`embed`／`object`、または判定材料が無い通常のリクエスト・HTML フォーム POST）は従来どおりログイン画面へリダイレクトし、プログラムからの呼び出し（パスが `/api/` で始まる、`X-Requested-With: XMLHttpRequest`、JSON 本文、`Sec-Fetch-Dest` がナビゲーション以外（`empty` 等）、Accept で JSON を HTML より優先）には 401 と JSON `{"status": 401, "message": "Authentication required."}` を返す。iframe 等の埋め込み（制限付きファイルのプレビュー等）もログイン画面へ戻すため、枠内に JSON が表示されることはない。API アプリ（`/api`）はログイン画面を持たないため常に 401 JSON を返す。
- 【v2.1.0】実装補足（v2.1.0、ログイン API）：REST のログイン API `POST /api/<version>/login`（`weko_accounts.rest.WekoLogin`、`v1` のみ）は、本文が JSON オブジェクトでない・`email`／`password` が文字列でないか空の場合は 400「Invalid request.」、ログイン済みは 400「User allready logged in.」、ユーザー不存在・パスワード不一致はいずれも 403「Invalid email or password.」（存在しない場合もハッシュ計算を行い応答時間を揃える）、無効化ユーザーは 403「Account is disabled.」、成功時は 200 で `{"id", "email"}` を返す。レート制限は既定制限を持たないログイン専用の `weko_accounts.utils.login_limiter` を API アプリにのみ初期化し、本 API にだけ `WEKO_API_LIMIT_RATE_DEFAULT`（既定 `['100 per minute']`）を適用する（キーはエンドポイント名＋接続元アドレス）。他の `/api` 配下の経路にはこの制限はかからない。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2024/03/14 | xxxxx | W-OA-14_WEKO3サブリポジトリ管理・表示機能の開発対応 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：未ログイン時の応答（画面遷移はログイン画面、AJAX・API は 401 JSON、iframe 内もログイン画面へ）とログイン API の応答・レート制限を追記 |
