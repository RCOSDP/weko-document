# 未病データベースとWEKOの構成

未病データベースとWEKOの構成を記述する。

> 注：本書で「フロント」と呼ぶ Nuxt アプリケーション（`weko-frontend` / `nginx/ams/weko-frontend/`）は WEKO バックエンドとは**別リポジトリ**で管理されており、本仕様書リポジトリおよび WEKO バックエンドリポジトリ（`/home/mhaya/weko`）には含まれない。以下のフロントのパス・ページ・サーバーサイドAPIの定義はそのフロントリポジトリ側にある。

## 用語説明

本書では以下の用語で統一する。

| 用語 | 説明 |
| ---- | ---- |
| フロント | 未病データベースのフロントエンド                    |
| WEKO     | 未病データベース用のWEKO3リポジトリ（バックエンド） |

## フロントのパス一覧

以下はNuxtアプリケーションで動作する画面のパスであり、 各ページの動作は `weko-frontend/pages` ディレクトリ内のファイルで定義されている。

| パス                                             | 説明                                                        |
|--------------------------------------------------|-------------------------------------------------------------|
| /                                                | トップ画面                                                  |
| /ams/search                                      | 検索画面                                                    |
| /ams/contact                                     | お問い合わせ画面                                            |
| /ams/detail                                      | アイテム詳細画面                                            |
| /ams/files                                       | ファイル一覧画面                                            |
| /ams/login                                       | ログイン画面                                                |
| /ams/logout                                      | ログアウト画面                                              |

以下はNuxtアプリケーションのサーバーサイドで動作するAPIのパスであり、 各APIの動作は `weko-frontend/server` ディレクトリ内のファイルで定義されている。

| APIパス                                         | メソッド | 説明                                                      |
|-------------------------------------------------|:--------:|-----------------------------------------------------------|
| /api/ams/captcha/<アイテムのID>/request-mail    |   POST   | WEKOのリクエストメール送信APIにリクエストを送信するAPI    |
| /api/ams/captcha/image                          |    GET   | WEKOのCAPTCHA画像取得APIにリクエストを送信するAPI         |
| /api/ams/captcha/validate                       |   POST   | WEKOのCAPTCHA結果検証APIにリクエストを送信するAPI         |
| /api/ams/mail/send                              |   POST   | メール送信API                                             |
| /api/ams/token/create                           |    GET   | WEKOからアクセストークンを初回取得するためのAPI           |
| /api/ams/token/refresh                          |    GET   | WEKOからアクセストークンを再度取得するためのAPI           |

上記フロントのサーバーサイドAPIが最終的に呼び出す WEKO バックエンド側の実APIは以下（いずれも `/home/mhaya/weko` 内で実装を確認）。

| フロントAPI | 呼び出す WEKO バックエンドAPI | 実装（モジュール / シンボル） |
|---|---|---|
| /api/ams/captcha/&lt;ID&gt;/request-mail | `POST /api/v1/records/<id>/request-mail` | weko-records-ui `RequestMail`（`send_request_mail`、`rest.py` / `api.py`） |
| /api/ams/captcha/image | `GET /api/v1/captcha/image` | weko-records-ui `CreateCaptchaImage`（`create_captcha_image`、`captcha.py`） |
| /api/ams/captcha/validate | `POST /api/v1/captcha/validate` | weko-records-ui `CaptchaAnswerValidation`（`validate_captcha_answer`） |
| /api/ams/token/create, /token/refresh | `POST /oauth/token` ほか | invenio-oauth2server（OAuth2） |

- リクエストメール／CAPTCHA の WEKO 直APIは `WEKO_RECORDS_UI_REST_ENDPOINTS`（weko-records-ui `config.py`）で定義される。関連config：`WEKO_RECORDS_UI_CAPTCHA_EXPIRATION_SECONDS`（既定900）、`WEKO_RECORDS_UI_CAPTCHA_TTL_SECONDS`（既定600）。


## フロントとWEKOの共存

フロントとWEKOを同一オリジンで動作させる。
フロントとWEKOの画面の両方を表示、またはフロントの画面のみを表示可能とする。

### フロントとWEKOの両方の画面を表示

nginxの設定により、リクエストされたパスに応じてアクセス先のアプリケーションを振り分ける。
これにより、フロントとWEKOの両方の画面を表示できる。
WEKO単体で動作している場合と比較し、アクセスできない画面はWEKOのトップ画面のみとなる。
nginxコンテナの`/etc/nginx/conf.d/weko.conf`に`weko/nginx/weko-ams.conf`の内容を設定した場合、この動作となる。

| パス         | アクセス先アプリケーション| 説明                     |
|--------------|:---------- |-----------------------------------------|
|  /           |  フロント  |  フロントのトップ画面                   |
|  /ams/*      |  フロント  |  フロントの各画面 <br> `/ams`および`/ams/`にアクセスした場合は`/`にリダイレクトする |
|  /api/ams/*  |  フロント  |  フロントのサーバーサイドで動作するAPI  |
|  /img/ams/*  |  フロント  |  フロントで使用する画像                 |
| 上記以外     |   WEKO     |  WEKOの画面、APIなど                    |

> 実装補足（`nginx/weko-ams.conf`、v2.0.2）：上表は振り分け結果を示すが、実装上は `/ams/*` `/api/ams/*` `/img/ams/*` それぞれに専用の `location` があるわけではなく、`location / → proxy_pass http://nuxt`（フロント）をキャッチオールとし、WEKO へ回すパスのみを明示 `location` で指定する方式である。WEKO へ振り分ける主な `location`：`/api/v1`、`~ /(admin|oauth|tree)`、`/oai`、`/api/records`、`/api/files`、`~ /record/[0-9]*/(files|file_preview|preview)/`、`/api/iiif/v2/`、`/ping`、`/static`、`/data`、`/weko/shib` および Shibboleth 系。
>
> また `~ /api/v1/(captcha|records/[0-9]*/request-mail)` には **IPアドレス制限（`allow` 内部ネットワーク / `deny all`）** が設定されており、リクエストメール・CAPTCHA の WEKO 直APIは内部ネットワーク（＝フロントのサーバーサイド経由）からのみ許可される。

### フロントの画面のみを表示

nginxの設定を変更することで、WEKOへのアクセスを制限する。
フロントの動作に必要なものを除き、WEKOの画面やAPIへのアクセスを制限し、フロントの画面のみにアクセスできるようにする。
nginxコンテナの`/etc/nginx/conf.d/weko.conf`に`weko/nginx/weko-ams-restricted.conf`の内容を設定した場合、この動作となる。

> 実装補足（v2.0.2）：`weko-ams-restricted.conf` はバックエンドリポジトリ（`/home/mhaya/weko/nginx/`）には**未収録**である（`weko-ams.conf` のみ存在）。本モード（フロントの画面のみを表示）を利用する場合は当該 conf を別途用意する必要がある。

## 更新履歴

| 日付         | GitHubコミットID | 更新内容   |
|--------------|------------------|------------|
| 2025/08/29   |   6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3  | 初版作成   |
| 2026/07/14   |  | 実装(v2.0.2)と突き合わせ。フロントが呼ぶWEKOバックエンド実API・nginx振り分けの実装方式・CAPTCHA/リクエストメールのIP制限・`weko-ams-restricted.conf`未収録・フロントが別リポジトリである旨を追記 |
