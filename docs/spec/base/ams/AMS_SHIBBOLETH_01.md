# 未病データベース Shibboleth対応

## 用語説明

- 本書では以下の用語で統一する

  <table>
  <thead>
  <tr>
  <th>用語</th>
  <th>説明</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>フロント</td>
  <td>未病データベースのフロントエンド</td>
  </tr>
  <tr>
  <td>WEKO</td>
  <td>未病データベース用のWEKO3リポジトリ（バックエンド）</td>
  </tr>
  <tr>
  <td>Shibbolethログイン</td>
  <td>学認IdPやOrthrosアカウントによるログイン</td>
  </tr>
  </tbody>
  </table>

## 1. Shibbolethログイン時のロール付与

- WEKOの処理に変更を加えず使用する

- WEKOのShibboleth対応については[SHIBBOLETH_01](../other/SHIBBOLETH_01.md)を参照

- IdPから取得した属性情報はWEKOに渡され、所属グループの判定を行う

  - 所属グループが「目標2Grp」である場合、対応するロールを付与することにより、目標2ユーザとしてアクセス権限を付与する

    - 属性情報（`isMemberOf`）からmAPグループIDに所属しているか判定する。判定パターンは WEKO 実装上 config 駆動で `<prefix>_<fqdn>_<role_keyword>_<suffix>` 形式（`WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT`、既定 `prefix=jc` / `role_keyword=ro`）。AMS では `role_keyword` に `groups` を設定するため `jc_<fqdn>_groups_<groupname>` となる（`<groupname>` に目標2Grpの値が入る）。マッチしたグループ名に対応する WEKO ロールを付与する。
      - 【v2.1.0】実装補足（v2.1.0）：`ShibUser._assign_roles_to_user` は、`<prefix>_<fqdn>_<role_keyword>_<suffix>` に一致するグループには `role_mapping` の WEKO ロールを、`sysadm_group` には System Administrator を付与し、さらにグループ名と同名のロールが存在すればそのロールも付与する。一方、インデックスの閲覧・投稿権限判定や管理画面の選択肢では、#1891（map conditions）以降、`<prefix>_<fqdn>_<role_keyword>_` で始まるロールは「学認mAPロール」として非表示・判定対象外となり、グループとして扱われるのは `<prefix>_<fqdn>_<group_keyword>_`（`group_keyword` 既定 `gr`）で始まるロールである。このため、上記のように `role_keyword` を `groups` に変更する運用では目標2Grp のロールがインデックス権限判定から除外される点に注意が必要である（AMS 環境で `WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT` を変更している設定ファイルは release_v2.1.0 のソースツリー内には見当たらず、実環境の設定値は未確認）。

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

  - 【v2.1.0】WEKO実装（AMSログイン経路）：フロント login.vue は returnURL に `?next=ams` を付与する。`shib_sp_login`（`POST /weko/shib/login`）は `next=ams`（`ams_login`）を判定して後続処理（`shib_auto_login` / `confirm_user_without_page` / `confirm_user` / `shib_login`）へ `next=ams` を伝播する。AMS経路では失敗時に WEKO ログイン画面へ flash せず、`generate_ams_login_url` ／ `_redirect_method(..., ams_error=...)` により外部 AMS ログイン画面（config `WEKO_ACCOUNTS_SHIB_AMS_LOGIN_URL`、既定 `'{}ams/login'`）へ `?error=<訳文をquote_plus>` 付きでリダイレクトする。成功時は `/?next=ams` へ遷移し、index.vue から OAuth2 API を実行する。

- ログイン処理後、nginx/ams/weko-frontend/pages/index.vueからOAuth2 APIを実行する

  - 参考： [OAuth2 API](../api/API_01_Oauth2.md)

  - ユーザがトークン発行を許可することで認可コードを受け取ることが出来る

## 3. Shibbolethログイン、OAuth認証時のエラー

- Shibbolethログイン、およびトークン取得時のエラー内容は以下の通り  
  検知したエラーはログイン画面、OAuth認証画面でそれぞれ表示する

  - ログイン画面

    「レスポンス（バックエンド実挙動）」列は WEKO バックエンド（`weko_accounts.views`）の実際の応答、「エラーメッセージ（日/英）」列はフロントのログイン画面での表示文言である。

    【v2.1.0】AMSログイン経路（`next=ams`）では、下表の各エラーで WEKO ログイン画面へ flash せず、外部 AMS ログイン画面 `{url_root}ams/login?error=<訳文>`（config `WEKO_ACCOUNTS_SHIB_AMS_LOGIN_URL`、既定 `'{}ams/login'`）へエラー文言付きでリダイレクトする（`generate_ams_login_url` ／ `_redirect_method(..., ams_error=...)`）。AMS経路のエラー文言は、ログインブロック時は "Login is blocked."、登録ユーザー情報がない場合は "There is no user information."（いずれも `_()` で翻訳可能）。

    <table>
    <thead>
    <tr>
    <th>エラー原因</th>
    <th>ステータスコード</th>
    <th>レスポンス（バックエンド実挙動）</th>
    <th>エラーメッセージ（日/英）</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>WEKOでログインブロックされている</td>
    <td>リダイレクト</td>
    <td><code>flash("Failed to login.")</code>＋ログイン画面へリダイレクト（ブロック判定は AdminSettings <code>blocked_user_settings.blocked_ePPNs</code>、ワイルドカード対応）</td>
    <td>ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.</td>
    </tr>
    <tr>
    <td>【v2.1.0】登録ユーザー情報がない</td>
    <td>リダイレクト</td>
    <td>AMS経路では <code>ShibUser.check_weko_user</code> が偽の場合に <code>{url_root}ams/login?error=There is no user information.</code> へリダイレクト（<code>_()</code> で翻訳される）し、フロント（<code>pages/ams/login.vue</code>）が <code>error</code> クエリの英語文字列と照合して訳文を表示する。通常経路は <code>flash('check_weko_user')</code>＋ログイン画面へリダイレクト</td>
    <td>ユーザー情報がありません。<br>/There is no user information.</td>
    </tr>
    <tr>
    <td>Redisにcache_keyがない</td>
    <td>400（<code>abort(400)</code> 時。通常は <code>flash()</code>＋リダイレクト）</td>
    <td>Missing SHIB_CACHE_PREFIX!</td>
    <td>ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.</td>
    </tr>
    <tr>
    <td>Shibboleth-Session-IDが取得出来ない</td>
    <td>400（<code>abort(400)</code> 時。通常は <code>flash()</code>＋リダイレクト）</td>
    <td>Missing Shib-Session-ID!</td>
    <td>ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.</td>
    </tr>
    <tr>
    <td>shib_eppnが取得出来ない</td>
    <td>400（<code>abort(400)</code> 時。通常は <code>flash()</code>＋リダイレクト）</td>
    <td>Missing SHIB_ATTRs!（<code>shib_login</code> 側は単数形 Missing SHIB_ATTR!）</td>
    <td>ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.</td>
    </tr>
    </tbody>
    </table>

  - OAuth認証画面

    OAuth認証はバックエンドでは invenio-oauth2server（`invenio_oauth2server.views.server.authorize` ＋ oauthlib）が処理し、「レスポンス（バックエンド実挙動）」列は oauthlib 標準のエラーコードである。「エラーメッセージ（日/英）」列はフロント（`weko-frontend`）側でエラーコードから生成・表示する文言である。

    <table>
    <thead>
    <tr>
    <th>エラー原因</th>
    <th>ステータスコード</th>
    <th>レスポンス（バックエンド実挙動）</th>
    <th>エラーメッセージ（日/英）</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>レスポンスタイプ誤り</td>
    <td>400</td>
    <td><code>unsupported_response_type</code></td>
    <td>このレスポンスタイプはサポートされていません。<br>/This response type is not supported.</td>
    </tr>
    <tr>
    <td>クライアントID誤り</td>
    <td>400（クライアントID不在時は 404）</td>
    <td><code>invalid_client</code></td>
    <td>クライアントIDに誤りがあります。<br>/The client ID is incorrect.</td>
    </tr>
    <tr>
    <td>スコープ誤り</td>
    <td>400</td>
    <td><code>invalid_scope</code></td>
    <td>スコープに誤りがあります。<br>/The scope is incorrect.</td>
    </tr>
    <tr>
    <td>ユーザーが【Reject】を選択</td>
    <td>200</td>
    <td><code>access_denied</code></td>
    <td>アクセスが拒否されました。<br>/Access has been denied.</td>
    </tr>
    </tbody>
    </table>

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
| 2026/07/17   |  | v2.1.0差分反映：AMSログイン経路（`next=ams`）のフローと、エラー時の外部AMSログイン画面リダイレクト（`WEKO_ACCOUNTS_SHIB_AMS_LOGIN_URL`、"Login is blocked." / "There is no user information."）を追記 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：「登録ユーザー情報がない」エラーのバックエンド実挙動（AMSログイン画面へ error 付きリダイレクト、フロント login.vue で訳文表示）に修正、mAPグループ判定（map conditions #1891、group_keyword）との関係を追記 |
