# ログイン

ログインに関するAPIのアクセスコントロールについて記述します。

## 目次

- [POST /api/\<version>/login](#post-apiversionlogin)
- [POST /api/\<version>/logout](#post-apiversionlogout)

## POST `/api/<version>/login`

表内のいずれかの○に合致すれば、ログインAPIへのアクセスおよびログインが出来ます。

| ログイン後のロール                                  | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| メールアドレス、パスワードが正しい | ○                  | ○                    | ○                      | ○            | ○            | ×                       |
| メールアドレス、パスワードが誤り                                 | ×                  | ×                    | ×                      | ×            | ×            | ×                        |

> 【v2.1.0】実装補足（v2.1.0）：ログインAPI（`weko_accounts.rest.WekoLogin.post_v1`）の判定と応答は以下のとおり。
>
> | 条件 | 応答 |
> | ---- | ---- |
> | リクエストボディが JSON オブジェクトでない、または `email` / `password` が文字列でない・空 | 400 `InvalidLoginRequestError`（"Invalid request."） |
> | 既にログイン済み | 400 `UserAllreadyLoggedInError` |
> | メールアドレスに該当するユーザーが存在しない、パスワード未設定のユーザー、またはパスワード不一致 | 403 `InvalidCredentialsError`（"Invalid email or password."）。アカウントの存否で応答が変わらないよう、ユーザーが存在しない場合もパスワードのハッシュ計算を行ってから同じ応答を返す（v2.0.2 までの `UserNotFoundError` / `InvalidPasswordError` による応答の区別は廃止） |
> | アカウントが無効（`active` が False） | 403 `DisabledUserError`（"Account is disabled."） |
> | 成功 | 200、`{"id": <ユーザーID>, "email": <メールアドレス>}`。`UserActivityLogger` に LOGIN を記録 |
>
> レート制限：ログインAPIのみ、API アプリ専用の `weko_accounts.utils.login_limiter`（Flask-Limiter、既定の制限なし）で回数制限をかける。上限値は `WEKO_API_LIMIT_RATE_DEFAULT`（既定 `['100 per minute']`）で、キーは「エンドポイント名＋接続元 IP アドレス（`get_remote_addr`）」。上限超過時は Flask-Limiter により 429 が返る。API アプリの他のエンドポイントには共有の `limiter` の既定制限は適用されない。

## POST `/api/<version>/logout`

表内のいずれかの○に合致すれば、ログアウトAPIへアクセスすることが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                 | ○                   | ○                      | ○            | ○            | ○                        |

表内のいずれかの○に合致すれば、ログアウトすることが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                 | ○                   | ○                      | ○            | ○            | ×                        |

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本APIの認可は OAuth2 を基本とし、`require_api_auth(allow_anonymous=…)`（未認証許可可否）、`require_oauth_scopes(<scope>)`（トークン使用時のみスコープ検証）、`roles_required([...])`（未認証かつ guest_token 無しは 401）の組み合わせで判定される。ゲスト（未ログイン）可否は主に `allow_anonymous` と `roles_required` の有無で決まり、公開範囲は検索系では `weko_search_ui.query.get_permission_filter` で絞り込まれる。各エンドポイントの実ハンドラ・スコープは [API仕様（api カテゴリ）](../api/README.md) を参照。

### 実装補足（v2.1.0）

- API アプリ（`/api/` 配下）では、`login_required` 等で未認証と判定された場合、ログイン画面へのリダイレクト（v2.0.x では API アプリに `security` Blueprint が無いため 500 になっていた）ではなく、401 と JSON `{"status": 401, "message": "Authentication required."}` を返す（`weko_accounts.unauthorized.install(app, api_only=True)`、`WekoAccountsREST.init_unauthorized_handler`）。UI アプリでも、AJAX/fetch 等の機械的な呼び出し（パスが `/api/` で始まる、`X-Requested-With: XMLHttpRequest`、JSON ボディ、`Sec-Fetch-Dest` が document/iframe/frame/embed/object 以外、または Accept で JSON を優先）には同じ 401 JSON を返し、通常の画面遷移や iframe 内のページはログイン画面へリダイレクトする。`WEKO_ACCOUNTS_UNAUTHORIZED_JSON`（既定 True）を False にすると従来動作に戻る。
- ログアウトAPI（`WekoLogout.post_v1`）は未ログインでも 200（空ボディ）を返し、ログイン中の場合のみログアウトして `UserActivityLogger` に LOGOUT を記録する。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3      | 初版作成                                                 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：ログインAPIの失敗応答の統一（403 InvalidCredentialsError / 400 InvalidLoginRequestError）、レート制限、API アプリの未認証 401 応答を追記 |
