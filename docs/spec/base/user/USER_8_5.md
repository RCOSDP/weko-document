# API設定

## 目的・用途

本機能は、API使用のためのOAuthの設定を閲覧・作成・編集できる機能である。

## 利用方法

画面ヘッダの右側の［▼］ボタンをクリックし、プルダウンから「Applications」を選択する。  
【Applications】画面に遷移する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ |  |

## 機能内容

「Developer Applications」エリア

- エリア右上の「New Applications」ボタンを押下するとOAuthアプリケーション(以下クライアントと表記)作成画面に遷移し、新しいクライアントを作成することができる。

  - 入力事項

    - 名前(Name)：必須入力

    - 記述(Description)：自由記述

    - WebSite URL：必須入力

    - Redirect URIs:必須入力

    - Client type :プルダウンより「Confidential」、「Public」から選択する。

- エリアを表示した際、ログインしているアカウントに登録されているクライアントの名前と説明を表示する。

- 表示されているクライアントの名前を押下するとその詳細情報が表示される。

  - 「Application/[名前]」エリア

    - 表示情報

      - Client ID

      - Client Secret

      - 名前(Name)

      - 記述(Description)

      - Website URL

      - Redirect URIs

      - Client type

        - 「Client ID」,「Client Secret」以外の項目は編集可能である。

    - 「Reset client secret」ボタンを押下すると「Client Secret」項目を再生成することができる。

    - 「削除」ボタンを押下すると即時表示されているクライアント情報を削除する。

    - 「保存」ボタンを押下すると編集した内容を保存する。

  - 「OAuth 2.0 Endpoints」エリア

    - 「Authorize URL(GET)」に必要なパラメータが記載されている。  
      Query parameters:

      - response_type (required, use code or token)

      - client_id (required)

      - scope (required, space separate list of scopes)

      - redirect_uri (required, URL encoded)

      - state (recommended, for CSRF protection)

「example request」を押下するとAuthorize requestの例として生成されるURLに遷移する。

- 「Access token URL(POST)」に必要なパラメータが記載されている。

  - client_id (required).

  - client_secret (required).

  - grant_type (required, use client_credentials, authorization_code, refresh_token).

  - code (required for grant_type authorization code).

  - scope (required for grant_type client_credentials).

  - refresh_token (required for grant_type refresh_token).

「Personal access tokens」エリア

- エリア右上の「New token」ボタンを押下するとOAuthトークン(以下トークン)作成画面に遷移し、新しいトークンを作成することができる。

  - 入力項目

    - Name:必須

    - Scopes：以下チェックで入力

      - deposit:actions　アップロードの公開の許可

      - deposit:write　アップロードの許可（公開の権限なし）

      - index:create　インデックス作成の許可

      - user:email　登録されているメールアドレスへの接続許可(読み込みのみ)

      - user:activity　ワークフロー作成の許可

    - 上記は主なスコープであり、実際の作成画面には登録済みの全スコープが列挙される（deposit / index / item / author / file / oa_status / ranking / user:email / user:activity 系など）。

- エリアを表示した際、ログインしているアカウントに登録されているまだ承認されていないトークンの名前と説明を表示する。

- 表示されているクライアントの名前を押下するとその詳細情報が表示される。

  - 「Personal access token/[名前]」エリア

    - 表示情報

      - Access token

      - Name

      - Scopes:以下チェックで入力

        - deposit:actions

        - deposit:write

        - index:create

        - user:email

        - user:activity

          - Access token以外の項目は編集可能である。

    - 「削除」ボタンを押下すると表示されているトークン情報を即削除する。

    - 「保存」ボタンを押下すると編集した内容を保存する。

「Authorized applications」エリア

- 承認されたトークンを表示する。

- 表示されているトークンを押下するとその詳細情報が表示される画面に遷移する。

  - 「Authorized application:[名前]」エリア

    - 表示情報

      - Description

      - トークンが持つ権限（スコープ）

      - トークンの所属しているOAuthアプリケーション情報

        - アプリケーションの名前

        - アプリケーションのWebsiteリンク

          - リンクを押下すると遷移する。

- アプリケーション名右にある「撤回」ボタンを押下するとそのアプリケーションに属するトークン情報を削除する。

## 関連モジュール

- Invenio-oauth2server

## 処理概要

【ホーム>アカウント>Applications】画面を表示する。この操作によって、invenio_oauth2server.views.settings.indexメソッドが呼び出され、oauth2server_clientテーブルからクライアント情報を、oauth2server_tokenテーブルからトークン情報をそれぞれ取得し表示する。なお、取得するのはログインしているユーザーが作成したもののみである。

- 取得したトークン情報を承認されているかで「Personal access tokens」と「Authorized applications」で振り分ける。振り分け条件としては前者にはクライアント情報のis_internal列がTrueかつトークン情報のis_personal列がTrueであるものを、後者にはクライアント情報のis_internal列がfalseかつトークン情報のis_personal列がfalseであるものを振り分ける。

「Developer Applications」エリア

- 「New application」ボタンを押下する。この操作によって、invenio_oauth2server.views.settings. client_newメソッドがGETで呼び出され、新しいクライアントを登録する画面が表示される。

  - 必須入力事項を入力し、「登録」ボタンを押下する。  
    この操作によって、invenio_oauth2server.views.settings. client_newメソッドがPOSTで呼び出され、oauth2server_clientテーブルに入力した情報を登録する。

- エリアにて表示されているクライアントの名前を押下する。  
  この操作によって、invenio_oauth2server.views.settings. client_viewメソッドがGETで呼び出され、oauth2server_clientテーブルからそのクライアント情報を取得し、画面に表示する。

  - 「Application/[名前]」エリア

    - 「Reset client secret」ボタンを押下する。  
      この操作によって、invenio_oauth2server.views.settings.client_resetメソッドがPOSTで呼び出され、Client Secretを再生成し、oauth2server_clientテーブルのclient_secret列に保存する。

    - 「削除」ボタンを押下する。  
      この操作によって、invenio_oauth2server.views.settings.client_viewメソッドがPOST（form field `delete` 付き）で呼び出され、表示されていたクライアント情報をoauth2server_clientテーブルから削除する。

  - 「OAuth 2.0 Endpoints」エリア

    - 「example request」を押下するとinvenio_oauth2server.templates.invenio_oauth2server.settings.client_viewの61行目から記載されているURLのページに遷移する。

- 表示されているクライアント情報を編集後、「保存」ボタンを押下する。  
  この操作によって、invenio_oauth2server.views.settings.client_viewメソッドがPOSTで呼び出され、編集した情報をoauth2server_clientテーブルに保存する。

「Personal access tokens」エリア

- 「New token」ボタンを押下する。  
  この操作によって、invenio_oauth2server.views.settings.token_newメソッドがGETで呼び出され、新しいトークンを作成する画面が表示される。

  - 必須入力事項を入力し、「作成」ボタンを押下する。  
    この操作によって、invenio_oauth2server.views.settings.token_newメソッドがPOSTで呼び出され、oauth2server_tokenテーブルに入力した情報を登録する。

- エリアにて表示されているトークンの名前を押下する。  
  この操作によって、invenio_oauth2server.views.settings. token_viewメソッドがGETで呼び出され、oauth2server_tokenテーブルからそのトークン情報を取得し、画面に表示する。

  - 「Personal access token/[名前]」エリア

    - 「削除」ボタンを押下する。  
      この操作によって、invenio_oauth2server.views.settings.token_viewメソッドがPOST（form field `delete` 付き）で呼び出され、表示されていたトークン情報をoauth2server_tokenテーブルから削除する。

    - 表示されているトークン情報を編集後、「保存」ボタンを押下する。  
      この操作によって、invenio_oauth2server.views.settings.token_viewメソッドがPOSTで呼び出され、編集した情報をoauth2server_tokenテーブルに保存する。

「Authorized applications」エリア

- エリアにて表示されているトークンの名前を押下する。この操作によって、invenio_oauth2server.views.settings. token_permission_viewメソッドがGETで呼び出される。これによってoauth2server_clientテーブルからクライアント情報をoauth2server_tokenテーブルからそのトークンのスコープを取得し、画面に表示する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：blueprint `invenio_oauth2server_settings`（prefix `/account/settings/applications`）。`index` / `client_new` / `client_view` / `client_reset` / `token_new` / `token_view` / `token_permission_view`（＋ `token_revoke`）。table `oauth2server_client` / `oauth2server_token`。
- 実装補足：カラムは `client_secret`、ラベルは「Confidential」。personal/authorized の振り分けには `Token.is_internal==False` 条件もある。削除は POST＋form field `delete`（HTTP DELETE ではない）。トークン作成画面のスコープは全登録スコープを列挙する（deposit/index/item/author/file/oa_status/ranking/user:email/user:activity 等）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
