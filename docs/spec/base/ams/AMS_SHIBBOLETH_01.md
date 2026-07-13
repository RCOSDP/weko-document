## 未病データベース Shibboleth対応

### 用語説明

- 本書では以下の用語で統一する

  | 用語 | 説明 |
  | ---- | ---- |
  | フロント | 未病データベースのフロントエンド |
  | WEKO | 未病データベース用のWEKO3リポジトリ（バックエンド） |
  | Shibbolethログイン | 学認IdPやOrthrosアカウントによるログイン |

### 1. Shibbolethログイン時のロール付与

- WEKOの処理に変更を加えず使用する

- WEKOのShibboleth対応については[SHIBBOLETH_01](../other/SHIBBOLETH_01.md)を参照

- IdPから取得した属性情報はWEKOに渡され、所属グループの判定を行う

  - 所属グループが「目標2Grp」である場合、対応するロールを付与することにより、目標2ユーザとしてアクセス権限を付与する

    - 属性情報からmAPグループID: `jc_<fqdn>_groups_<groupname>` に所属しているか判定する (`<groupname>` に目標2Grpの値が入る)

  - 所属グループが「目標2Grp」ではない場合、通常通りログインする


### 2. Shibbolethログインの実装

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

- weko_accounts.views.shib_sp_login関数によって、IdPからのリクエストを処理する

  - 参考： [SHIBBOLETH_01: 5.実装](../other/SHIBBOLETH_01.md)

  - ログイン処理後のリダイレクト先はフロントのTOPページを指定する

- ログイン処理後、nginx/ams/weko-frontend/pages/index.vueからOAuth2 APIを実行する

  - 参考： [OAuth2 API](../api/API_01_Oauth2.md)

  - ユーザがトークン発行を許可することで認可コードを受け取ることが出来る

### 3. Shibbolethログイン、OAuth認証時のエラー

- Shibbolethログイン、およびトークン取得時のエラー内容は以下の通り  
  検知したエラーはログイン画面、OAuth認証画面でそれぞれ表示する

  - ログイン画面

    | エラー原因 | ステータスコード | レスポンス | エラーメッセージ（日/英） |
    | --------- | --------------- | --------- | ----------------------- |
    | WEKOでログインブロックされている | 403 | Login is blocked. | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator. |
    | 登録ユーザー情報がない | 403 | There is no user information. | ユーザー情報がありません。<br>/There is no user information. |
    | Redisにcache_keyがない | 400 | Missing SHIB_CACHE_PREFIX! | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.  |
    | Shibboleth-Session-IDが取得出来ない | 400 | Missing Shib-Session-ID! | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.  |
    | shib_eppnが取得出来ない | 400 | Missing SHIB_ATTRs! | ログインに失敗しました。管理者に連絡してください。<br>/Failed to Login. Please contact server administrator.  |

  - OAuth認証画面

    | エラー原因 | ステータスコード | レスポンス | エラーメッセージ（日/英） |
    | --------- | --------------- | --------- | ----------------------- |
    | レスポンスタイプ誤り | 400 | This response type is not supported. | このレスポンスタイプはサポートされていません。<br>/This response type is not supported. |
    | クライアントID誤り | 400 | The client ID is incorrect. | クライアントIDに誤りがあります。<br>/The client ID is incorrect. |
    | スコープ誤り | 400 | The scope is incorrect. | スコープに誤りがあります。<br>/The scope is incorrect. |
    | ユーザーが【Reject】を選択 | 200 | Access has been denied. | アクセスが拒否されました。<br>/Access has been denied. |

### 4. 目標2ユーザ以外が閲覧権限が必要なアイテム詳細画面にアクセスした場合

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
