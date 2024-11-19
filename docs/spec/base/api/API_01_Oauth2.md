### OAuth2

  - > 目的・用途

他のウェブアプリがweko3のリソースにアクセスできるようAPI利用を承認することを目的としている。

  - > 利用方法

API-8-5の機能を用いて、OAuthアプリケーション、またはトークンを登録する。その後、設定された値を利用してAPI接続の設定を行う。

  - > 機能内容

**OAuthアプリの登録**

  - 【アカウント(Account)\>Applications】画面にてOAuthアプリケーション、OAuthトークンを登録することができる。

  - 詳細は[USER-8-5 API設定](https://ivis.sharepoint.com/sites/NIIDMR646/Shared%20Documents/%5bWEKO3%5d10_開発/01.開発/2023/JAIRO%20Cloud（WEKO3）のドキュメント整備/機能設計書/マージ前/機能設計書_WebAPI_API-1-6.docx#_API設定)を参照すること

**Authorize URL (GET) /oauth/authorize**

Query parameters ( example request ):

  - response\_type (required, use code or token)

  - client\_id (required)

  - scope (required, space separate list of scopes)

  - redirect\_uri (required, URL encoded)

  - state (recommended, for CSRF protection)

URLの例：

Query parametersの値を以下とする。

  - response\_type : code

  - client\_id : CLIENTID

  - scope : deposit:write deposit:actions

  - redirect\_uri : http://localhost:5000/callback

  - state : CHANGEME

> そうしたときURLは以下のものとなる。
> 
> <https://「weko3>の接続先」/oauth/authorize? response\_type=code&
> 
> client\_id= CLIENTID\&scope=deposit%3Awrite+deposit%3Aactions&
> 
> state=CHANGEME\&redirect\_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback
> 
> /oauth/authorize…に接続した際、許可される内容について表示される。
> 
> 「Authorize application」ボタンを押下すると、codeとstateの値がサーバー側からクライアント側に渡される。

**Access token URL (POST) /oauth/token**

Request body parameters:

  - client\_id (required).

  - client\_secret (required).

  - grant\_type (required, use authorization\_code, refresh\_token, client\_credentials).

  - code (required for grant\_type authorization code).

  - state(recommended, for CSRF protection)

  - redirect\_uri(required for grant\_type authorization code)

  - scope (required for grant\_type client\_credentials).

  - refresh\_token (required for grant\_type refresh\_token).

Request（BaseHTTPRequestHandler）の例：

Authorize URL (GET)からcodeとstateを取得しているものとする。

Request body parametersを以下のものだとする。

  - client\_id : CLIENTID

  - client\_secret : SECRET

  - grant\_type : authorization\_code

  - code : CODECODE

  - state : CHANGEME

  - redirect\_uri: http://localhost:5000/callback

> この場合、以下のコードでアクセストークンを取得できる。
> 
> params = {'client\_id': 'CLIENTID', 'client\_secret': 'SECRET',
> 
> 'grant\_type': 'authorization\_code',
> 
> 'code': 'CODECODE', 'state':CHANGEME,
> 
> 'redirect\_uri':'http://localhost:5000/callback'}
> 
> accessurl = 'https://「weko3の接続先」/oauth/token'
> 
> request = requests.post(url=accessurl, data=params)

**アクセストークンの発行**

Personal access tokens の新規発行(/account/settings/applications/tokens/new/)からアクセストークンを発行することができる。

curlコマンドによるアクセストークン利用例

> curl -H 'Content-type: application/json' -XPOST -H 'Authorization: Bearer unGyWc31FNoAUOLm2AtMqJaDiqdJev6V6trTKEmRPBNAuMZ2lAKy4hcj7aLu' -k https://weko3.example.org:8443/api/indextree/create -d '{"parent\_id":"0","index\_info":{"index\_name":"index index","index\_name\_english":"index index english","public\_state":true}}'

**新しい Scope を追加する手順**

  - modules/weko-index-tree下にScopeを追加する手順を例とする。  
    （v0.9.22現在 以下のScopeは実装済みである。）

  - ソースコードを編集する操作なため、機能設計書の範疇ではないが、参考手順として残す。

  - モジュールにある scopes.py （ない場合は自分で作成する）に以下のように新規の scopes を追加する。

> **class** **IndexScope**(Scope):
> 
> """Basic index scope."""
> 
> **def** **\_\_init\_\_**(self, id\_, \*args, \*\*kwargs):
> 
> """Define the scope."""
> 
> **super**(IndexScope, self).\_\_init\_\_(
> 
> id\_='index:{0}'.format(id\_),
> 
> group='index', \*args, \*\*kwargs
> 
> )
> 
> create\_index\_scope = IndexScope('create',
> 
> help\_text=\_('Allow create.'))
> 
> """Allow create."""

  - モジュールの setup.py に以下のようにエントリポイントを追加する

> entry\_points={
> 
> ...
> 
> 'invenio\_oauth2server.scopes': \[
> 
> 'weko\_index\_tree\_create = weko\_index\_tree.scopes:create\_index\_scope',
> 
> \],
> 
> },

  - コードでは以下のように使う

> @blueprint\_api.route('/indextree/create', methods=\['POST'\])
> 
> @require\_api\_auth()
> 
> @require\_oauth\_scopes(create\_index\_scope.id)
> 
> **def** **create\_index**():
> 
> ...



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

curl -k -s -X POST -d "grant_type=authorization_code" -d "client_id=QE77MZSrnljwDqp4lRxgfHal4M5II6K1JgtmIblA" -d "client_secret=TIHRA8RaBgxiBZ1s9gxj40watdjEcJDQFiINMIAQ15UqaoQGEMm0r1Cc0sMq" -b cookie.txt -c cookie.txt -d 'state=teststate' -d "code=6LGWFTvaj1DJ4W5xjRHiRViiS2Qn4h" "https://dev.ir.rcos.nii.ac.jp/oauth/token"|jq .


authorization_response = 'https://localhost/callback?state=xxxxxxxx&code=xxxxxxxx'
url, headers, body = oauth.prepare_token_request('https://dev.ir.rcos.nii.ac.jp/oauth/token', authorization_response=authorization_response, client_secret=TIHRA8RaBgxiBZ1s9gxj40watdjEcJDQFiINMIAQ15UqaoQGEMm0r1Cc0sMq)

  - > 関連モジュール

> invenio\_oauth2server

  - > 更新履歴

<table>
<thead>
<tr class="header">
<th>日付</th>
<th>GitHubコミットID</th>
<th>更新内容</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>
