# 未病データベース Shibboleth対応

## 用語説明

- 本書では以下の用語で統一する

  | 用語 | 説明 |
  | ---- | ---- |
  | フロント | 未病データベースのフロントエンド |
  | WEKO | 未病データベース用のWEKO3リポジトリ（バックエンド） |
  | Shibbolethログイン | 学認IdPやOrthrosアカウントによるログイン |

## 1. Shibbolethログイン時のロール付与

- WEKOの処理に変更を加えず使用する

- WEKOのShibboleth対応については[SHIBBOLETH_01](../other/SHIBBOLETH_01.md)を参照

- IdPから取得した属性情報はWEKOに渡され、所属グループの判定を行う

  - 所属グループが「目標2Grp」である場合、対応するロールを付与することにより、目標2ユーザとしてアクセス権限を付与する

    - 属性情報（`isMemberOf`）からmAPグループIDに所属しているか判定する。判定パターンは WEKO 実装上 config 駆動で `<prefix>_<fqdn>_<role_keyword>_<suffix>` 形式（`WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT`、既定 `prefix=jc` / `role_keyword=ro`）。AMS では `role_keyword` に `groups` を設定するため `jc_<fqdn>_groups_<groupname>` となる（`<groupname>` に目標2Grpの値が入る）。マッチしたグループ名に対応する WEKO ロールを付与する。

  - 所属グループが「目標2Grp」ではない場合、通常通りログインする

  - WEKO実装（関連モジュール：weko-accounts）：ロール同期は `WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS` が有効なとき `sync_shib_gakunin_map_groups` → `ShibUser.check_in` → `_get_roles_to_add` → `_assign_roles_to_user` の順で処理される。属性のパースは `weko_accounts.utils.parse_attributes`、fqdn は `create_fqdn_from_entity_id`（`WEKO_ACCOUNTS_IDP_ENTITY_ID` の netloc から生成）で得る。


## 2. Shibbolethログインの実装

- nginx/ams/weko-frontend/pages/login.vueのonMounted関数でEmbedded DSを導入する

  - Embedded DSの導入にはiframeを活用する

  - Embedded DSを導入する際に必要な変数をnginx/ams/weko-frontend/app.config.tsで定義する

    ```js
    const weko = 'xxx'; //ホスト名を設定

    shibLogin: {
      dsURL: 'https://ds.gakunin.nii.ac.jp/WAYF',
      orthrosURL: 'https://core.orthros.gakunin.nii.ac.jp/idp',
      entityID: 'https://' + weko + '/shibboleth',
      handlerURL: 'https://' + weko + '/Shibboleth.sso',
      returnURL: 'https://' + weko + '/secure/login.py?next=ams'
    }
    ```

  - /secure/login.pyからweko_accounts.views.shib_sp_login関数を実行する
    - WEKO実装：`/secure/login.py` は nginx が配信するCGI（`nginx/login.py`）であり、Shibboleth属性を WEKO バックエンドの実エンドポイント **`POST /weko/shib/login`**（`weko_accounts.views.shib_sp_login`。Blueprint の `url_prefix='/weko'`）へ中継する。IdP からの returnURL は config `WEKO_ACCOUNTS_SHIB_IDP_LOGIN_URL`（`'{}secure/login.py'`）に対応する。

- weko_accounts.views.shib_sp_login関数によって、IdPからのリクエストを処理する

  - 参考： [SHIBBOLETH_01: 5.実装](../other/SHIBBOLETH_01.md)

  - ログイン処理後のリダイレクト先はフロントのTOPページを指定する

- ログイン処理後、nginx/ams/weko-frontend/pages/index.vueからOAuth2 APIを実行する

  - 参考： [OAuth2 API](../api/API_01_Oauth2.md)

  - ユーザがトークン発行を許可することで認可コードを受け取ることが出来る

## 3. Shibbolethログイン、OAuth認証時のエラー

- Shibbolethログイン、およびトークン取得時のエラー内容は以下の通り  
  検知したエラーはログイン画面、OAuth認証画面でそれぞれ表示する

  - ログイン画面

    「レスポンス（バックエンド実挙動）」列は WEKO バックエンド（`weko_accounts.views`）の実際の応答、「エラーメッセージ（日/英）」列はフロントのログイン画面での表示文言である。

    | エラー原因 | ステータスコード | レスポンス（バックエンド実挙動） | エラーメッセージ（日/英） |
    | --------- | --------------- | --------- | ----------------------- |
    | WEKOでログインブロックされている | リダイレクト | `flash("Failed to login.")`＋ログイン画面へリダイレクト（ブロック判定は AdminSettings `blocked_user_settings.blocked_ePPNs`、ワイルドカード対応） | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator. |
    | 登録ユーザー情報がない | - | フロント側で判定・表示（バックエンドに該当文字列なし） | ユーザー情報がありません。<br>/There is no user information. |
    | Redisにcache_keyがない | 400（`abort(400)` 時。通常は `flash()`＋リダイレクト） | Missing SHIB_CACHE_PREFIX! | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.  |
    | Shibboleth-Session-IDが取得出来ない | 400（`abort(400)` 時。通常は `flash()`＋リダイレクト） | Missing Shib-Session-ID! | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.  |
    | shib_eppnが取得出来ない | 400（`abort(400)` 時。通常は `flash()`＋リダイレクト） | Missing SHIB_ATTRs!（`shib_login` 側は単数形 Missing SHIB_ATTR!） | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.  |

  - OAuth認証画面

    OAuth認証はバックエンドでは invenio-oauth2server（`invenio_oauth2server.views.server.authorize` ＋ oauthlib）が処理し、「レスポンス（バックエンド実挙動）」列は oauthlib 標準のエラーコードである。「エラーメッセージ（日/英）」列はフロント（`weko-frontend`）側でエラーコードから生成・表示する文言である。

    | エラー原因 | ステータスコード | レスポンス（バックエンド実挙動） | エラーメッセージ（日/英） |
    | --------- | --------------- | --------- | ----------------------- |
    | レスポンスタイプ誤り | 400 | `unsupported_response_type` | このレスポンスタイプはサポートされていません。<br>/This response type is not supported. |
    | クライアントID誤り | 400（クライアントID不在時は 404） | `invalid_client` | クライアントIDに誤りがあります。<br>/The client ID is incorrect. |
    | スコープ誤り | 400 | `invalid_scope` | スコープに誤りがあります。<br>/The scope is incorrect. |
    | ユーザーが【Reject】を選択 | 200 | `access_denied` | アクセスが拒否されました。<br>/Access has been denied. |

## 4. 目標2ユーザ以外が閲覧権限が必要なアイテム詳細画面にアクセスした場合

- 未ログインユーザが閲覧権限が必要なアイテム詳細画面にアクセスした場合

  - アイテム閲覧にはログインが必要であるというメッセージを表示し、xx秒後に自動でフロントのログイン画面に遷移する

  - xx(秒数)はnginx/ams/weko-frontend/app.config.tsで指定する

    - defineAppConfig関数に`transitionTimeMs:xx` (ミリ秒)を追加する

    - デフォルト値は10000(=10秒)

  - アイテム詳細画面からログイン画面にリダイレクトする際に、nginx/ams/weko-frontend/pages/detail.vueで以下処理を実行する

    - アイテム詳細画面のURLを`sessionStorage`に保存する

    - navigateTo関数のパスに`/login`と、クエリに`source=detail`を指定する

  - ログイン画面へ遷移時、クエリに`source=detail`がない場合はnginx/ams/weko-frontend/pages/login.vueの`onBeforeMount`で`sessionStorage`のアイテム詳細画面URLを削除する

  - nginx/ams/weko-frontend/pages/index.vueでOAuth2 APIを実行する際にリダイレクト先をアイテム詳細画面のURLに指定する

    - API実行前にそれぞれの変数を指定する
      ```js
      const baseURI = useRuntimeConfig().public.redirectURI;
      const itemURL = sessionStorage.getItem('item-url');
      const redirectURL = itemURL ? itemURL : baseURI;
      ```

    - `itemURL`に値を設定した後、`sessionStorage`のアイテム詳細画面URLを削除する

    - `finally`の`useRouter().replace()`のパスに`redirectURL`を指定する

- 目標2ユーザ以外のログインユーザが閲覧権限のないアイテム詳細画面にアクセスした場合
  - アイテムの閲覧権限がないというエラーメッセージを表示する

## 更新履歴

| 日付         | GitHubコミットID | 更新内容   |
|--------------|------------------|------------|
| 2025/08/29   |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3    | 初版作成   |
| 2026/07/14   |  | 実装(v2.0.2)と突き合わせ。実エンドポイント`POST /weko/shib/login`・ロール同期の実関数・mAPグループ形式のconfig駆動・エラー文言のバックエンド実挙動（flash+redirect、OAuthはoauthlib標準）を追記 |
