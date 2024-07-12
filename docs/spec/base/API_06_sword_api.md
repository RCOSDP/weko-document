### SWORD API

#### 目的・用途

クライアントからSWORDv3プロトコルに従いリポジトリ上のアイテム操作を実現する。

#### 利用方法

APIの認証にはOAuth2を利用する。

アクセストークンの発行はAPI-1:OAuth2を参照。

**Scope：**

deposit: write

**エンドポイント：**

<table>
<thead>
<tr class="header">
<th>
<p>項番</p>
</th>
<th>
<p>HTTP request</p>
</th>
<th>
<p>内容</p>
</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>
<p>1</p>
</td>
<td>
<p>GET /sword/service-document</p>
</td>
<td>
<p>リポジトリのサービスドキュメントを取得する。</p>
</td>
</tr>
<tr class="even">
<td>
<p>2</p></td>
<td><p>POST /sword/service-document</p>
</td>
<td>
<p>WEKO3の一括登録フォーマットを用いて、アイテムを登録する。</p>
</td>
</tr>
<tr class="odd">
<td>
<p>3</p>
</td>
<td>
<p>GET /sword/deposit/&lt;recid&gt;</p>
</td>
<td>
<p>recidを指定してリポジトリ上に存在するアイテムのステータスドキュメントを取得する。</p>
</td>
</tr>
<tr class="even">
<td>
<p>4</p>
</td>
<td>
<p>DELETE /sword/deposit/&lt;recid&gt;</p>
</td>
<td>
<p>recidを指定してアイテムを削除する。</p>
</td>
</tr>
</tbody>
</table>

##### CURLでのリクエスト実行例：

各APIのリクエスト仕様の詳細は後述。

###### GET /sword/service-document

```
curl https://192.168.56.103/sword/service-document -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo" |
```


  - > \-H オプション
    
      - > Authorization は "Bearer" + " (半角スペース)" + "認証キー"の形式で指定する

###### POST /sword/service-document**


```
curl -s -k https://weko3.ir.rcos.nii.ac.jp/sword/service-document -F
 "file=@import.zip;type=application/zip" -H "Authorization:Bearer 50is1B9XcyHcyRckWx9z0V
2XZnpHq7" -H "Content-Disposition:attachment; filename=import.zip" -H "Packaging:http://
purl.org/net/sword/3.0/package/SimpleZip"| jq .
{
  "@context": "https://swordapp.github.io/swordv3/swordv3.jsonld",
  "@id": "https://weko3.ir.rcos.nii.ac.jp/sword/deposit/96568",
  "@type": "Status",
  "actions": {
    "appendFiles": false,
    "appendMetadata": false,
    "deleteFiles": false,
    "deleteMetadata": false,
    "deleteObject": true,
    "getFiles": false,
    "getMetadata": false,
    "replaceFiles": false,
    "replaceMetadata": false
  },
  "eTag": "5",
  "fileSet": {},
  "links": [
    {
      "@id": "https://weko3.ir.rcos.nii.ac.jp/records/96568",
      "contentType": "text/html",
      "rel": [
        "alternate"
      ]
    },
    {
      "@id": "http://hdl.handle.net/20.500.12465/0000096568",
      "contentType": "text/html",
      "rel": [
        "alternate"
      ]
    }
  ],
  "metadata": {},
  "service": "/sword/service-document",
  "state": [
    {
      "@id": "http://purl.org/net/sword/3.0/state/ingested",
      "description": ""
    }
  ]
}                                                                                       ```
                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| curl https://192.168.56.103/sword/service-document -F "file=@export-all3.zip;type=application/zip" -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo" -H "Content-Disposition:attachment; filename=export-all3.zip" -H "Packaging:http://purl.org/net/sword/3.0/package/SimpleZip" |

  - > \-F オプション
    
      - multipart/form-data 形式で POSTするファイルを指定する
    
      - boundaryやContent-Lengthは自動で付加されるため自前で指定しなくてもよい
    
      - ファイル名の先頭には@を付加すること
    
      - ファイルのContent-Typeを"application/zip"とするため、ここでtypeを指定する（指定しないと application/octet-stream となってしまう）

  - > \-H オプション
    
      - Authorization は "Bearer" + " (半角スペース)" + "認証キー"の形式で指定する
    
      - Content-Disposition の filename は -Fオプションで指定したファイルのファイル名と一致させる
    
      - Packaging は "http://purl.org/net/sword/3.0/package/SimpleZip" を指定
    
      - 必須の Content-Length および Content-Type については前述の通り、-Fオプションにて自動付加されるため-Hオプションでの指定は不要


**　3. GET /sword/deposit/\<recid\>**

|                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| curl https://192.168.56.103/sword/deposit/1 -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo" |

  - > \-H オプション
    
      - Authorization は "Bearer" + " (半角スペース)" + "認証キー"の形式で指定する

**　4. DELETE /sword/deposit/\<recid\>**

|                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------- |
| curl -X DELETE https://192.168.56.103/sword/deposit/1 -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo" |

  - > \-H オプション
    
      - Authorization は "Bearer" + " (半角スペース)" + "認証キー"の形式で指定する

<!-- end list -->

  - 利用可能なロール

<table>
<thead>
<tr class="header">
<th>ロール</th>
<th>システム<br />
管理者</th>
<th>リポジトリ<br />
管理者</th>
<th>コミュニティ<br />
管理者</th>
<th>登録ユーザー</th>
<th>一般ユーザー</th>
<th>ゲスト<br />
(未ログイン)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>利用可否</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>×</td>
</tr>
</tbody>
</table>

  - 機能内容

<!-- end list -->

  - 各APIへのリクエストに応じて処理を実行しレスポンスを返す
    
      - OAuthアクセストークンによるユーザー認証を必須とする

  - アイテム登録機能で登録に使用するZIPファイルはインポートで使用するものと同様の形式のみ使用できる。
    
      - ZIPファイル形式の詳細は [ADMIN-2-4:インポート](./functional_design.md#インポート) を参照

> API仕様

  - > サービスドキュメント取得機能：GET /sword/service-document

<table>
<thead>
<tr class="header">
<th>エンドポイント</th>
<th>GET /sword/service-document</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>概要</td>
<td>リポジトリのサービスドキュメントを取得する。</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>リクエスト</td>
<td>ヘッダー</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ヘッダー</td>
<td>必須</td>
<td>説明</td>
<td>例</td>
</tr>
<tr class="even">
<td></td>
<td>Authorization</td>
<td>○</td>
<td>操作するWEKOユーザーのOAuth認証情報。<br />
“Bearer”+” (半角スペース)”+“認証キー”の形式で指定する。</td>
<td>“Bearer xxxxxxx”</td>
</tr>
<tr class="odd">
<td></td>
<td>On-Behalf-Of</td>
<td>-</td>
<td>代理投稿ユーザーのメールアドレスを指定する。</td>
<td>user@example.com</td>
</tr>
<tr class="even">
<td>レスポンス</td>
<td>コード</td>
<td>ドキュメント</td>
<td>説明</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>200</td>
<td>サービスドキュメント</td>
<td>サーバーのサービスドキュメントを返す。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>400</td>
<td>エラードキュメント</td>
<td>リクエスト内容に何らかの不備がある場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>401</td>
<td></td>
<td>リクエストでAuthorization ヘッダーが提供されない場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>403</td>
<td></td>
<td>認証に失敗した場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>412</td>
<td></td>
<td>サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、リクエストでOn-Behalf-Of ヘッダーが提供された場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>500</td>
<td></td>
<td>サーバー内部エラーが発生した場合。</td>
<td></td>
</tr>
</tbody>
</table>

  - > アイテム登録機能：POST /sword/service-document

<table>
<thead>
<tr class="header">
<th>エンドポイント</th>
<th>POST /sword/service-document</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>概要</td>
<td>一括登録用のZIPファイルを用いてアイテムを新規登録する。</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>リクエスト</td>
<td>ヘッダー</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ヘッダー</td>
<td>必須</td>
<td>説明</td>
<td>例</td>
</tr>
<tr class="even">
<td></td>
<td>Authorization</td>
<td>○</td>
<td>操作するWEKOユーザーのOAuth認証情報。<br />
“Bearer”+” (半角スペース)”+“認証キー”の形式で指定する。</td>
<td>“Bearer xxxxxxx”</td>
</tr>
<tr class="odd">
<td></td>
<td>On-Behalf-Of</td>
<td>-</td>
<td>代理投稿ユーザーのメールアドレスを指定する。</td>
<td>“user@example.com”</td>
</tr>
<tr class="even">
<td></td>
<td>Content-Disposition</td>
<td>○</td>
<td>リクエストボディに付加したファイルのファイル名を指定する。</td>
<td>“attachment; filename=example.zip”</td>
</tr>
<tr class="odd">
<td></td>
<td>Content-Length</td>
<td>○</td>
<td>リクエストボディに付加したファイルサイズを指定する。</td>
<td>1024000</td>
</tr>
<tr class="even">
<td></td>
<td>Content-Type</td>
<td>○</td>
<td>リクエストボディにファイルを付加するため multipart/form-data を指定する。</td>
<td>multipart/form-data; boundary=xxxxxxxx</td>
</tr>
<tr class="odd">
<td></td>
<td>Packaging</td>
<td>○</td>
<td>パッケージフォーマットと指定する。<br />
SWORDでは以下の3つのパッケージフォーマットが定義されている。<br />
http://purl.org/net/sword/3.0/package/Binary<br />
http://purl.org/net/sword/3.0/package/SimpleZip<br />
http://purl.org/net/sword/3.0/package/SWORDBagIt<br />
※現在はSimpleZip形式のみ対応</td>
<td>“http://purl.org/net/sword<br />
/3.0/package/SimpleZip”</td>
</tr>
<tr class="even">
<td></td>
<td>ボディ</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Key</td>
<td>必須</td>
<td>説明</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>file</td>
<td>○</td>
<td>form-data 形式でボディにZIPファイルを付加する。<br />
ファイルのContent-Type には“application/zip”を指定すること。</td>
<td></td>
</tr>
<tr class="odd">
<td>レスポンス</td>
<td>コード</td>
<td>ドキュメント</td>
<td>説明</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>200</td>
<td>ステータスドキュメント</td>
<td>登録されたアイテムのステータスドキュメントを返す。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>400</td>
<td>エラードキュメント</td>
<td>リクエスト内容に何らかの不備がある場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>401</td>
<td></td>
<td>リクエストでAuthorization ヘッダーが提供されない場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>403</td>
<td></td>
<td>認証に失敗した場合。<br />
認証したOAuthトークンが「deposit:write」スコープを持っていない場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>412</td>
<td></td>
<td>サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、リクエストでOn-Behalf-Of ヘッダーが提供された場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>413</td>
<td></td>
<td>送信されたファイルのサイズがサーバーに設定されたmaxUploadSizeを超えている場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>415</td>
<td></td>
<td>ヘッダーまたはボディに付加されたファイルのContent-Typeがサーバー側でサポートされていない場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>500</td>
<td></td>
<td>サーバー内部エラーが発生した場合。</td>
<td></td>
</tr>
</tbody>
</table>

  - > アイテム状態取得機能：GET /sword/deposit/\<recid\>

<table>
<thead>
<tr class="header">
<th>エンドポイント</th>
<th>GET /sword/deposit/&lt;recid&gt;</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>概要</td>
<td>指定したアイテムのステータスドキュメントを取得する。</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>リクエスト</td>
<td>ヘッダー</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ヘッダー</td>
<td>必須</td>
<td>説明</td>
<td>例</td>
</tr>
<tr class="even">
<td></td>
<td>Authorization</td>
<td>○</td>
<td>操作するWEKOユーザーのOAuth認証情報。<br />
“Bearer”+” (半角スペース)”+“認証キー”の形式で指定する。</td>
<td>“Bearer xxxxxxx”</td>
</tr>
<tr class="odd">
<td></td>
<td>On-Behalf-Of</td>
<td>-</td>
<td>代理投稿ユーザーのメールアドレスを指定する。</td>
<td>“user@example.com”</td>
</tr>
<tr class="even">
<td></td>
<td>パスパラメータ</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Key</td>
<td>必須</td>
<td>説明</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>&lt;recid&gt;</td>
<td>○</td>
<td>レコードID</td>
<td></td>
</tr>
<tr class="odd">
<td>レスポンス</td>
<td>コード</td>
<td>ドキュメント</td>
<td>説明</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>200</td>
<td>ステータスドキュメント</td>
<td>指定されたアイテムのステータスドキュメントを返す。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>400</td>
<td>エラードキュメント</td>
<td>リクエスト内容に何らかの不備がある場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>401</td>
<td></td>
<td>リクエストでAuthorization ヘッダーが提供されない場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>403</td>
<td></td>
<td>認証に失敗した場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>404</td>
<td></td>
<td>指定したrecidに該当するアイテムが存在しない（削除されている）場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>412</td>
<td></td>
<td>サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、リクエストでOn-Behalf-Of ヘッダーが提供された場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>500</td>
<td></td>
<td>サーバー内部エラーが発生した場合。</td>
<td></td>
</tr>
</tbody>
</table>

  - > アイテム削除機能：DELETE /sword/deposit/\<recid\>

<table>
<thead>
<tr class="header">
<th>エンドポイント</th>
<th>DELETE /sword/deposit/&lt;recid&gt;</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>概要</td>
<td>指定したアイテムを削除する。</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>リクエスト</td>
<td>ヘッダー</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ヘッダー</td>
<td>必須</td>
<td>説明</td>
<td>例</td>
</tr>
<tr class="even">
<td></td>
<td>Authorization</td>
<td>○</td>
<td>操作するWEKOユーザーのOAuth認証情報。<br />
“Bearer”+” (半角スペース)”+“認証キー”の形式で指定する。</td>
<td>“Bearer xxxxxxx”</td>
</tr>
<tr class="odd">
<td></td>
<td>On-Behalf-Of</td>
<td>-</td>
<td>代理投稿ユーザーのメールアドレスを指定する。</td>
<td>“user@example.com”</td>
</tr>
<tr class="even">
<td></td>
<td>パスパラメータ</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Key</td>
<td>必須</td>
<td>説明</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>&lt;recid&gt;</td>
<td>○</td>
<td>レコードID</td>
<td></td>
</tr>
<tr class="odd">
<td>レスポンス</td>
<td>コード</td>
<td>ドキュメント</td>
<td>説明</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>204</td>
<td>なし</td>
<td>空のレスポンスを返す。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>400</td>
<td>エラードキュメント</td>
<td>リクエスト内容に何らかの不備がある場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>401</td>
<td></td>
<td>リクエストでAuthorization ヘッダーが提供されない場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>403</td>
<td></td>
<td>認証に失敗した場合。</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>412</td>
<td></td>
<td>サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、リクエストでOn-Behalf-Of ヘッダーが提供された場合。</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>500</td>
<td></td>
<td>サーバー内部エラーが発生した場合。</td>
<td></td>
</tr>
</tbody>
</table>

> ドキュメント仕様

  - > サービスドキュメント  
    > サーバー全体の機能と操作パラメータを定義したドキュメント

<table>
<thead>
<tr class="header">
<th>項目</th>
<th>型</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>@context</td>
<td>string</td>
<td>“https://swordapp.github.io/swordv3/swordv3.jsonld”を固定で出力。</td>
</tr>
<tr class="even">
<td>@id</td>
<td>string</td>
<td>"[WEKO3のURL]/sword/service-document"を出力。</td>
</tr>
<tr class="odd">
<td>@type</td>
<td>string</td>
<td>"ServiceDocument"を固定で出力。</td>
</tr>
<tr class="even">
<td>accept</td>
<td>array</td>
<td>サーバーに受け入れられるコンテンツタイプのリスト。<br />
”*/*”を出力する。</td>
</tr>
<tr class="odd">
<td>acceptArchiveFormat</td>
<td>array</td>
<td>サーバーが解凍できるアーカイブ形式のリスト。<br />
現状"application/zip"のみ対応。</td>
</tr>
<tr class="even">
<td>acceptDeposits</td>
<td>boolean</td>
<td>サーバーがデポジットを受け入れるか否か。</td>
</tr>
<tr class="odd">
<td>acceptMetadata</td>
<td>array</td>
<td>サーバーで受け入れ可能なメタデータ形式のリスト。<br />
現状では出力内容にかかわらず、Metadataの受け入れには対応していない。</td>
</tr>
<tr class="even">
<td>acceptPackaging</td>
<td>array</td>
<td>サーバーで受け入れ可能なパッケージ形式のリスト。<br />
現状すべての形式を受け入れるが、アイテム登録はWEKOの一括登録用ZIP形式でのみ可能。</td>
</tr>
<tr class="odd">
<td>authentication</td>
<td>Array</td>
<td>サーバーでサポートされている認証スキームのリスト。<br />
現状”OAuth”のみ対応。</td>
</tr>
<tr class="even">
<td>byReferenceDeposit</td>
<td>boolean</td>
<td>サーバーがbyReferenceDepositをサポートしているか否か。現状未対応のためFalseを出力。</td>
</tr>
<tr class="odd">
<td>collectionPolicy</td>
<td>object</td>
<td>コレクションポリシーを示すオブジェクト。</td>
</tr>
<tr class="even">
<td>collectionPolicy.@id</td>
<td>string</td>
<td>コレクションポリシーのURL。</td>
</tr>
<tr class="odd">
<td>collectionPolicy.description</td>
<td>string</td>
<td>コレクションポリシーの説明。</td>
</tr>
<tr class="even">
<td>dc:title</td>
<td>string</td>
<td>リポジトリの名称を出力。</td>
</tr>
<tr class="odd">
<td>dcterms:abstract</td>
<td>string</td>
<td>リポジトリの説明。</td>
</tr>
<tr class="even">
<td>digest</td>
<td>array</td>
<td>サーバーが受け入れるdigest形式のリスト。<br />
現状digestの検証は未対応。</td>
</tr>
<tr class="odd">
<td>maxAssembledSize</td>
<td>integer</td>
<td>Segmented File Upload時のファイル合計最大サイズ（単位：byte）。</td>
</tr>
<tr class="even">
<td>maxByReferenceSize</td>
<td>integer</td>
<td>By-Reference Deposit時のファイル最大サイズ（単位：byte）。</td>
</tr>
<tr class="odd">
<td>maxSegmentSize</td>
<td>integer</td>
<td>Segmented File Upload時の１ファイルの最大サイズ（単位：byte）。</td>
</tr>
<tr class="even">
<td>maxSegments</td>
<td>integer</td>
<td>Segmented File Upload時のセグメントの最大数。</td>
</tr>
<tr class="odd">
<td>maxUploadSize</td>
<td>integer</td>
<td>アップロードされるファイルの最大サイズ（単位：byte）。</td>
</tr>
<tr class="even">
<td>minSegmentSize</td>
<td>integer</td>
<td>Segmented File Upload時の１ファイルの最小サイズ（単位：byte）。</td>
</tr>
<tr class="odd">
<td>onBehalfOf</td>
<td>boolean</td>
<td>代理投稿をサポートしているか否か。<br />
現状未対応のためfalseを出力。</td>
</tr>
<tr class="even">
<td>root</td>
<td>string</td>
<td>サービスドキュメントのルートURL。</td>
</tr>
<tr class="odd">
<td>services</td>
<td>array</td>
<td>親サービスに含まれるサービスのリスト。<br />
現状未対応。</td>
</tr>
<tr class="even">
<td>staging</td>
<td>string</td>
<td>Segmented File Upload時にコンテンツをステージング先URL。現状未対応のため空文字を出力。</td>
</tr>
<tr class="odd">
<td>stagingMaxIdle</td>
<td>integer</td>
<td>ステージングされたファイルの最小保持時間。</td>
</tr>
<tr class="even">
<td>treatment</td>
<td>object</td>
<td>デポジット時に期待される処理のURLと説明を示すオブジェクト。</td>
</tr>
<tr class="odd">
<td>treatment.@id</td>
<td>string</td>
<td>処理のURL。</td>
</tr>
<tr class="even">
<td>treatment.description</td>
<td>string</td>
<td>処理の説明。</td>
</tr>
<tr class="odd">
<td>version</td>
<td>string</td>
<td>サポートしているSWORDバージョン。<br />
"http://purl.org/net/sword/3.0"を出力。</td>
</tr>
</tbody>
</table>

  - > ステータスドキュメント  
    > アイテムの内容と現在の状態に関する詳細情報を示すドキュメント

<table>
<thead>
<tr class="header">
<th>項目</th>
<th>型</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>@context</td>
<td>string</td>
<td>“https://swordapp.github.io/swordv3/swordv3.jsonld”を固定で出力。</td>
</tr>
<tr class="even">
<td>@id</td>
<td>string</td>
<td>"[WEKO3のURL]/sword/deposit/[アイテムのrecid]"を出力。</td>
</tr>
<tr class="odd">
<td>@type</td>
<td>string</td>
<td>"ServiceDocument"を固定で出力。</td>
</tr>
<tr class="even">
<td>actions</td>
<td>object</td>
<td>アイテムに対してSWORDで使用可能なアクション。<br />
現時点では deleteObject のみTrueを返し、それ以外はFalseを返すようになっている。</td>
</tr>
<tr class="odd">
<td>actions. appendFiles</td>
<td>boolean</td>
<td>ファイル追加要求が発行可能か否か。</td>
</tr>
<tr class="even">
<td>actions.appendMetadata</td>
<td>boolean</td>
<td>メタデータ追加要求が発行可能か否か。</td>
</tr>
<tr class="odd">
<td>actions. deleteFiles</td>
<td>boolean</td>
<td>ファイル削除要求が発行可能か否か。</td>
</tr>
<tr class="even">
<td>actions. deleteMetadata</td>
<td>boolean</td>
<td>メタデータ削除要求が発行可能か否か。</td>
</tr>
<tr class="odd">
<td>actions. deleteObject</td>
<td>boolean</td>
<td>アイテム削除要求が発行可能か否か。</td>
</tr>
<tr class="even">
<td>actions. getFiles</td>
<td>boolean</td>
<td>ファイル取得要求が発行可能か否か。</td>
</tr>
<tr class="odd">
<td>actions. getMetadata</td>
<td>boolean</td>
<td>メタデータ取得要求が発行可能か否か。</td>
</tr>
<tr class="even">
<td>actions. replaceFiles</td>
<td>boolean</td>
<td>ファイル置き換え要求が発行可能か否か。</td>
</tr>
<tr class="odd">
<td>actions. replaceMetadata</td>
<td>boolean</td>
<td>メタデータ置き換え要求が発行可能か否か。</td>
</tr>
<tr class="even">
<td>eTag</td>
<td>string</td>
<td>アイテムのeTag。<br />
WEKOではアイテムのリビジョン番号を返す。</td>
</tr>
<tr class="odd">
<td>fileSet</td>
<td>object</td>
<td>ファイルセットを示すオブジェクト。<br />
現時点では空オブジェクトを返す。</td>
</tr>
<tr class="even">
<td>fileSet.@id</td>
<td>string</td>
<td>ファイルセットのURL。</td>
</tr>
<tr class="odd">
<td>fileSet.eTag</td>
<td>string</td>
<td>ファイルセットのeTag。</td>
</tr>
<tr class="even">
<td>links</td>
<td>array</td>
<td>アイテムのリンクを示すオブジェクト。<br />
現時点ではアイテム詳細ページのURLを出力する。またDOIやCNRIハンドルを持つ場合も同様に出力する。</td>
</tr>
<tr class="odd">
<td>links[].@id</td>
<td>string</td>
<td>リソースのURL。</td>
</tr>
<tr class="even">
<td>links[].byReference</td>
<td>string</td>
<td>byReference deposit の際の参照元URL。</td>
</tr>
<tr class="odd">
<td>links[].contentType</td>
<td>string</td>
<td>リソースのコンテンツタイプ。</td>
</tr>
<tr class="even">
<td>links[].dcterms:isReplacedBy</td>
<td>string</td>
<td>同じオブジェクト内のファイルの新しいバージョンへのURL。</td>
</tr>
<tr class="odd">
<td>links[].dcterms:relation</td>
<td>string</td>
<td>非SWORDアクセスポイントへのURL。</td>
</tr>
<tr class="even">
<td>links[].dcterms:replaces</td>
<td>string</td>
<td>同じオブジェクト内の古いバージョンのファイルへのURL。</td>
</tr>
<tr class="odd">
<td>links[].depositedBy</td>
<td>string</td>
<td>アイテム登録を行ったユーザーの識別子。</td>
</tr>
<tr class="even">
<td>links[].depositedOn</td>
<td>string</td>
<td>アイテム登録日時のタイムスタンプ。</td>
</tr>
<tr class="odd">
<td>links[].depositedOnBehalfOf</td>
<td>string</td>
<td>代理投稿により登録を行ったユーザーの識別子。</td>
</tr>
<tr class="even">
<td>links[].derivedFrom</td>
<td>string</td>
<td>現在のリソースが派生したリソースのURLへの参照。</td>
</tr>
<tr class="odd">
<td>links[].eTag</td>
<td>string</td>
<td>リソースのeTag。</td>
</tr>
<tr class="even">
<td>links[].log</td>
<td>string</td>
<td>クライアントが知っておくべきデポジットに関連する情報。</td>
</tr>
<tr class="odd">
<td>links[].packaging</td>
<td>string</td>
<td>リソースがパッケージである場合、パッケージ形式の識別子を示す。</td>
</tr>
<tr class="even">
<td>links[].rel</td>
<td>string</td>
<td><p>リソースとオブジェクトの関係。<br />
以下の何れかの文字列を持つ。</p>
<ul>
<li>
<p>alternate</p>
</li>
<li>
<p>packaging</p>
</li>
<li>
<p>depositedOn</p>
</li>
<li><p>depositedOnBehalfOf</p></li>
<li><p>status</p></li>
<li><p>log</p></li>
<li><p>dcterms:relation</p></li>
<li><p>dcterms:replaces</p></li>
<li><p>dcterms:isReplacedBy</p></li>
<li><p>versionReplaced</p></li>
<li><p>eTag</p></li>
<li><p>byReference</p></li>
<li><p>derivedFrom</p></li>
<li><p>metadataFormat</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>links[].status</td>
<td>string</td>
<td>取り込みに関するリソースのステータス。</td>
</tr>
<tr class="even">
<td>links[].versionReplacedOn</td>
<td>string</td>
<td>現在のリソースが新しいリソースに置き換えられた日付。</td>
</tr>
<tr class="odd">
<td>metadata</td>
<td>object</td>
<td>メタデータを示すオブジェクト。<br />
現時点では空オブジェクトを返す。</td>
</tr>
<tr class="even">
<td>metadata.@id</td>
<td>string</td>
<td>メタデータのURL。</td>
</tr>
<tr class="odd">
<td>metadata.eTag</td>
<td>string</td>
<td>メタデータのeTag。</td>
</tr>
<tr class="even">
<td>service</td>
<td>string</td>
<td>サービスドキュメントのURL。</td>
</tr>
<tr class="odd">
<td>state</td>
<td>array</td>
<td>アイテムがサーバー上にある状態のリスト。</td>
</tr>
<tr class="even">
<td>state[].@id</td>
<td>string</td>
<td>状態の識別子。<br />
現状では"http://purl.org/net/sword/3.0/state/ingested"を固定で出力。</td>
</tr>
<tr class="odd">
<td>state[].description</td>
<td>string</td>
<td>状態の説明</td>
</tr>
</tbody>
</table>

  - > エラードキュメント  
    > エラー内容を表すドキュメント

<table>
<thead>
<tr class="header">
<th>項目</th>
<th>型</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>@context</td>
<td>string</td>
<td>“https://swordapp.github.io/swordv3/swordv3.jsonld”を固定で出力。</td>
</tr>
<tr class="even">
<td>@type</td>
<td>string</td>
<td>エラータイプを示す文字列。<br />
4.3.3エラータイプ を参照。</td>
</tr>
<tr class="odd">
<td>error</td>
<td>string</td>
<td>エラー内容の説明。</td>
</tr>
<tr class="even">
<td>log</td>
<td>string</td>
<td>より詳細なエラー内容。<br />
現在は出力していない。</td>
</tr>
<tr class="odd">
<td>timestamp</td>
<td>string</td>
<td>エラー発生時のタイムスタンプ。</td>
</tr>
</tbody>
</table>

> エラータイプ

| エラータイプ文字列                    | エラーコード | エラー原因等                                               |
| ---------------------------- | ------ | ---------------------------------------------------- |
| AuthenticationFailed         | 403    | 認証に失敗。                                               |
| AuthenticationRequired       | 401    | 認証情報が不足。                                             |
| BadRequest                   | 400    | リクエストに何らかの不備がある。                                     |
| ByReferenceFileSizeExceeded  | 400    | サーバーの制限を超えるファイルをデポジットしようとした。                         |
| ByReferenceNotAllowed        | 412    | サーバーが By-Reference deposit をサポートしていない。               |
| ContentMalformed             | 400    | リクエスト本文の内容に不正がある。                                    |
| ContentTypeNotAcceptable     | 415    | サーバーで許可されていないコンテンツタイプをリクエストした。                       |
| DigestMismatch               | 412    | リクエストヘッダーによって提供されたdigestがサーバーで受け取ったコンテンツと一致していない。    |
| ETagNotMatched               | 412    | リクエストヘッダーによって提供されたIf-Matchの値が更新対象コンテンツのeTagと一致していない。 |
| ETagRequired                 | 412    | リクエストヘッダーにIf-Matchの値が指定されていない。                       |
| Forbidden                    | 403    | サーバーによって許可されていない操作をリクエストした。                          |
| FormatHeaderMismatch         | 415    | サーバーがサポートしていない形式のコンテンツがリクエストされた。                     |
| InvalidSegmentSize           | 400    | セグメントアップロード時のファイルサイズが範囲外。                            |
| MaxAssembledSizeExceeded     | 400    | セグメントアップロード時の合計ファイルサイズが最大値を超えている。                    |
| MaxUploadSizeExceeded        | 413    | アップロードされたコンテンツサイズが最大値を超えている                          |
| MetadataFormatNotAcceptable  | 415    | サーバーがサポートしていない形式のMetadata-Formatがリクエストされた。           |
| MethodNotAllowed             | 405    | メソッドへのアクセスが許可されていない。                                 |
| OnBehalfOfNotAllowed         | 412    | サーバーが On-Behalf-Of をサポートしていない。                       |
| PackagingFormatNotAcceptable | 415    | サーバーがサポートしていない形式のPackagingフォーマットがリクエストされた。           |
| SegmentedUploadTimedOut      | 410    | セグメントアップロード先のURLにアクセスできない。                           |
| SegmentLimitExceeded         | 400    | セグメント数が最大値を超えている。                                    |
| UnexpectedSegment            | 400    | サーバーが予期していないセグメントを受信した。                              |

  - 関連モジュール

<!-- end list -->

  - > invenio\_oauth2server：OAuthトークンによるユーザー認証を行う

  - > invenio\_deposit：OAuthトークンが参照するデポジット操作スコープを定義している

  - > weko\_records\_ui：レコード情報の取得、アイテムの削除を実行する

  - > weko\_search\_ui：インポート処理を実行する

<!-- end list -->

  - 処理概要

<!-- end list -->

  - > サービスドキュメント取得機能：GET /sword/service-document
    
      - リクエストをチェックする
        
          - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
        
          - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
    
      - サーバー設定値を参照し、サービスドキュメントを生成する
    
      - サービスドキュメントを返却する

  - > アイテム登録機能：POST /sword/service-document
    
      - リクエストをチェックする
        
          - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
        
          - 認証に使用されたOAuthトークンのScopeを確認する
        
          - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
        
          - 送付されたファイルの有無を確認する
        
          - ファイルサイズを確認する
        
          - Content-Typeを確認する
        
          - Packagingを確認する
    
      - ファイル内容に不備が無いかのチェックを行う
    
      - ファイル内のアイテムが新規登録か否かを確認する
    
      - インポート処理を行う
    
      - 登録したアイテムのステータスドキュメントを生成する
        
          - インポート処理から返されたrecidからアイテム情報を取得する
        
          - 取得したアイテム情報からステータスドキュメントを生成する
    
      - ステータスドキュメントを返却する

  - > アイテム状態取得機能：GET /sword/deposit/\<recid\>
    
      - リクエストをチェックする
        
          - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
        
          - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
    
      - 指定されたrecidからアイテム情報を取得する
    
      - 取得したアイテム情報からステータスドキュメントを生成する
    
      - ステータスドキュメントを返却する

  - > アイテム削除機能：DELETE /sword/deposit/\<recid\>
    
      - リクエストをチェックする
        
          - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
        
          - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
    
      - 指定されたrecidを引数にsoft\_delete処理を実行する
    
      - 空のレスポンスを返却する

<!-- end list -->

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
<td>
<p>2022/06/13</p>
</td>
<td>e6db31c99d459605f5bc09f15c4abd07ea573428</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td>
<p>2023/08/31</p>
</td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>ADMIN-2-4へのリンクを追加</td>
</tr>
</tbody>
</table>
