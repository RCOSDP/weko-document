# OAuth2

- 目的・用途

他のウェブアプリがweko3のリソースにアクセスできるようAPI利用を承認することを目的としている。

- 利用方法

API-8-5の機能を用いて、OAuthアプリケーション、またはトークンを登録する。その後、設定された値を利用してAPI接続の設定を行う。

- 機能内容

**OAuthアプリの登録**

  - 【アカウント(Account)>Applications】画面にてOAuthアプリケーション、OAuthトークンを登録することができる。

  - 詳細は[USER-8-5 API設定](../user/USER_8_5.md)を参照すること

**Authorize URL (GET) /oauth/authorize**

Query parameters ( example request ):

  - response_type (required, use code or token)

  - client_id (required)

  - scope (required, space separate list of scopes)

  - redirect_uri (required, URL encoded)

  - state (recommended, for CSRF protection)

URLの例：

Query parametersの値を以下とする。

  - response_type : code

  - client_id : CLIENTID

  - scope : deposit:write deposit:actions

  - redirect_uri : http://localhost:5000/callback

  - state : CHANGEME

> そうしたときURLは以下のものとなる。
>
> `https://「weko3の接続先」/oauth/authorize?response_type=code&client_id=CLIENTID&scope=deposit%3Awrite+deposit%3Aactions&state=CHANGEME&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback`
>
> /oauth/authorize…に接続した際、許可される内容について表示される。
>
> 「Authorize application」ボタンを押下すると、codeとstateの値がサーバー側からクライアント側に渡される。

レスポンスコード

  | コード | 説明                                                          |
  | ------ | ------------------------------------------------------------- |
  | 200    | ・正常終了<br>・ユーザが OAuth 認証画面で Reject を押下した時 |
  | 400    | リクエストに不備がある時                                     |

**Access token URL (POST) /oauth/token**

Request body parameters:

  - client_id (required).

  - client_secret (required).

  - grant_type (required, use authorization_code, refresh_token, client_credentials).

  - code (required for grant_type authorization code).

  - state(recommended, for CSRF protection)

  - redirect_uri(required for grant_type authorization code)

  - scope (required for grant_type client_credentials).

  - refresh_token (required for grant_type refresh_token).

Request（BaseHTTPRequestHandler）の例：

Authorize URL (GET)からcodeとstateを取得しているものとする。

Request body parametersを以下のものだとする。

  - client_id : CLIENTID

  - client_secret : SECRET

  - grant_type : authorization_code

  - code : CODECODE

  - state : CHANGEME

  - redirect_uri: http://localhost:5000/callback

> この場合、以下のコードでアクセストークンを取得できる。

```python
params = {
    'client_id': 'CLIENTID',
    'client_secret': 'SECRET',
    'grant_type': 'authorization_code',
    'code': 'CODECODE',
    'state': CHANGEME,
    'redirect_uri': 'http://localhost:5000/callback'
}

accessurl = 'https://「weko3の接続先」/oauth/token'

request = requests.post(url=accessurl, data=params)
```

レスポンスコード

  | コード | 説明                                                          |
  | ------ | ------------------------------------------------------------- |
  | 200    | 正常終了|
  | 400    | リクエストに不備がある時                                     |

**アクセストークンの発行**

Personal access tokens の新規発行(/account/settings/applications/tokens/new/)からアクセストークンを発行することができる。

curlコマンドによるアクセストークン利用例

```bash
curl -H 'Content-type: application/json' -XPOST -H 'Authorization: Bearer unGyWc31FNoAUOLm2AtMqJaDiqdJev6V6trTKEmRPBNAuMZ2lAKy4hcj7aLu' -k https://weko3.example.org:8443/api/indextree/create -d '{"parent_id":"0","index_info":{"index_name":"index index","index_name_english":"index index english","public_state":true}}'
```

**新しい Scope を追加する手順**

  - modules/weko-index-tree下にScopeを追加する手順を例とする。  
    （v0.9.22現在 以下のScopeは実装済みである。）

  - ソースコードを編集する操作なため、機能設計書の範疇ではないが、参考手順として残す。

  - モジュールにある scopes.py （ない場合は自分で作成する）に以下のように新規の scopes を追加する。

```python
class IndexScope(Scope):
    """Basic index scope."""

    def __init__(self, id_, *args, **kwargs):
        """Define the scope."""
        super(IndexScope, self).__init__(
            id_='index:{0}'.format(id_),
            group='index', *args, **kwargs
        )

create_index_scope = IndexScope('create',
    help_text=_('Allow create.'))
    """Allow create."""
```

  - モジュールの setup.py に以下のようにエントリポイントを追加する

```python
entry_points={
    ...
    'invenio_oauth2server.scopes': [
        'weko_index_tree_create = weko_index_tree.scopes:create_index_scope',
    ],
},
```

  - コードでは以下のように使う

```python
@blueprint_api.route('/indextree/create', methods=['POST'])
@require_api_auth()
@require_oauth_scopes(create_index_scope.id)
def create_index():
    ...
```



```
csrf_token=`curl -X GET -k -L -s -c cookie.txt "https://dev.ir.rcos.nii.ac.jp/login"|xmllint -html --xpath "//input[@name='csrf_token']/@value" -|sed 's/"//g'|awk -F'=' '{print $2}'`
```

```
curl -X POST -k -s -c cookie.txt -b cookie.txt -F "csrf_token=${csrf_token}" -F "email=wekosoftware@nii.ac.jp" -F "password=uspass123" -F "next=/" "https://dev.ir.rcos.nii.ac.jp/login/" > /dev/null
```

```
$ curl -k -s -b cookie.txt -c cookie.txt -d -X POST -d "response_type=code" -d "client_id=QE77MZSrnljwDqp4lRxgfHal4M5II6K1JgtmIblA" -d "scope=deposit:write" -d "redirect_uri=http://127.0.0.1:8080/"  -d "confirm=yes" -d "state=teststate" "https://dev.ir.rcos.nii.ac.jp/oauth/authorize" -i | grep "Location:"
Location: http://127.0.0.1:8080/?code=B3SD4JqPNE6yjFnHWHe92NPW8VkPWD&state=teststate
```

```
$ curl -k -s -X POST -d "response_type=token" -d "client_id=QE77MZSrnljwDqp4lRxgfHal4M5II6K1JgtmIblA" -d "scope=deposit:write" -d "redirect_uri=http://127.0.0.1:8080/" "https://dev.ir.rcos.nii.ac.jp/oauth/authorize" -b cookie.txt -c cookie.txt -d "code=6LGWFTvaj1DJ4W5xjRHiRViiS2Qn4h" -d 'state=teststate' -i -d "confirm=yes" | grep "Location:"
Location: http://127.0.0.1:8080/#access_token=prhKYk6SEcRDiBfdRxp3G9Ocbk9UUM&expires_in=3600&token_type=Bearer&scope=deposit%3Awrite&state=teststate&user=%7B%27id%27%3A+%271%27%7D
```



```
$ curl -X GET -H "Authorization: Bearer prhKYk6SEcRDiBfdRxp3G9Ocbk9UUM" -k "https://dev.ir.rcos.nii.ac.jp/oauth/ping"
{
  "ping": "pong"
}
```


```
$ curl -k -s -X POST -d "grant_type=client_credentials" -d "client_id=QE77MZSrnljwDqp4lRxgfHal4M5II6K1JgtmIblA" -d "client_secret=TIHRA8RaBgxiBZ1s9gxj40watdjEcJDQFiINMIAQ15UqaoQGEMm0r1Cc0sMq" -d "scope=deposit:write" "https://dev.ir.rcos.nii.ac.jp/oauth/token" -b cookie.txt -c cookie.txt -d 'state=teststate' |jq .
{
  "access_token": "N1NHiEEDhC93Ysx7vuNJdmBdV34Wnm",
  "expires_in": 3600,
  "token_type": "Bearer",
  "scope": "deposit:write",
  "state": "teststate",
  "user": {
    "id": "1"
  }
}
```

```bash
curl -k -s -X POST -d "grant_type=authorization_code" -d "client_id=QE77MZSrnljwDqp4lRxgfHal4M5II6K1JgtmIblA" -d "client_secret=TIHRA8RaBgxiBZ1s9gxj40watdjEcJDQFiINMIAQ15UqaoQGEMm0r1Cc0sMq" -b cookie.txt -c cookie.txt -d 'state=teststate' -d "code=6LGWFTvaj1DJ4W5xjRHiRViiS2Qn4h" "https://dev.ir.rcos.nii.ac.jp/oauth/token"|jq .
```

```python
authorization_response = 'https://localhost/callback?state=xxxxxxxx&code=xxxxxxxx'
url, headers, body = oauth.prepare_token_request('https://dev.ir.rcos.nii.ac.jp/oauth/token', authorization_response=authorization_response, client_secret=TIHRA8RaBgxiBZ1s9gxj40watdjEcJDQFiINMIAQ15UqaoQGEMm0r1Cc0sMq)
```

- 関連モジュール

- invenio-oauth2server（OAuth2プロバイダ本体。エンドポイント `views.server.authorize`（`/oauth/authorize`、GET/POST両対応）・`views.server.access_token`（`/oauth/token`、POST）、トークン発行UI `views.settings.token_new`（`/account/settings/applications/tokens/new/`）、`provider.save_token`、`decorators.require_oauth_scopes`）
- スコープ提供モジュール（各 `scopes.py` を `invenio_oauth2server.scopes` エントリポイントで登録）：invenio-oauth2server（`user:email`）、invenio-deposit（`deposit:write` / `deposit:actions`）、weko-index-tree（`index:create/read/update/delete`）、weko-items-ui（`item:read/create/update/delete` / `ranking:read`）、weko-authors（`author:search/create/update/delete`）、weko-records（`oa_status:update`）、weko-workflow（`user:activity`）、weko-records-ui（`file:read`）

> 実装補足（v2.0.2）：
> - `/oauth/authorize` は `methods=['GET','POST']`（GET/POST両対応）。
> - `grant_type` は `authorization_code` / `client_credentials` / `refresh_token`（`OAUTH2SERVER_ALLOWED_GRANT_TYPES`）、`response_type` は `code` / `token`（`OAUTH2SERVER_ALLOWED_RESPONSE_TYPES`）。
> - トークン有効期限は `OAUTH2_PROVIDER_TOKEN_EXPIRES_IN`（3600秒）。
> - エラー時挙動：クライアントID不在は 404、未ログイン時は `@login_required` により 302 リダイレクト、`client_credentials` を非機密クライアントで用いると `InvalidClientError`。
> - `weko-accounts` にはOAuth関連の実装は無い（認証基盤としての間接関与のみ）。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2024/07/1 | 7733de131da9ad59ab591b2df1c70ddefcfcad98 | v1.0.7対応 |
| 2025/06/11 |  | レスポンスコードを追記 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。authorizeのGET/POST両対応、grant_type/response_type、scope提供モジュール一覧・現行scope、configキー、エラーコードを追記 |
