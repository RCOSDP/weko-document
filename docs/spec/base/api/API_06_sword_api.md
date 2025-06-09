# SWORD API

## 目的・用途

クライアントからSWORD v3プロトコルに従いリポジトリ上のアイテム操作を実現する。  
アイテム登録には、TSV/CSV、XML、あるいはJSON-LD形式のメタデータを含むZIPファイルを用いる。

## 利用方法

APIの認証にはOAuth2を利用する。  
アクセストークンの発行は[API-1:OAuth2](./API_01_Oauth2.md#oauth2)を参照。

### Scope：
アイテムをアップロードし、直接登録するためには以下のスコープが必要となる。
- deposit:write
- deposit:actions
- item:create

既存のアイテムを更新するためには以下のスコープが必要となる。
- deposit:write
- deposit:actions
- item:update

アイテムを削除するためには以下のスコープが必要となる。
- deposit:write
- deposit:actions
- item:delete

アイテムをワークフローを経由して登録・更新・削除するためには、さらに以下のスコープが必要となる。
- user:activity

### エンドポイント：

| 項番 | HTTP request                   | 内容                                                                                     |
| :--: | ------------------------------ | ---------------------------------------------------------------------------------------- |
|  1   | GET /sword/service-document    | リポジトリのサービスドキュメントを取得する。                                             |
|  2   | POST /sword/service-document   | WEKO3の一括登録フォーマットを用いて、アイテムを登録する。                                |
|  3   | GET /sword/deposit/\<recid>    | recidを指定してリポジトリ上に存在するアイテムのステータスドキュメントを取得する。        |
|  4   | PUT /sword/deposit/\<recid>    | recidを指定してリポジトリ上に存在するアイテムに対して、メタデータやファイルを置換する。  |
|  5   | DELETE /sword/deposit/\<recid> | recidを指定してアイテムを削除する。                                                      |


### CURLでのリクエスト実行例：

各APIのリクエスト仕様の詳細は後述。

#### GET /sword/service-document
##### リクエスト

```shell
$ curl -X GET https://192.168.56.101/sword/service-document \
    -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo"
```

  - -H オプション

    - リクエストにカスタムヘッダーを追加する
    - Authorization は "Bearer" + " (半角スペース)" + "アクセストークン"の形式で指定する

##### レスポンス

```json
{
  "@context": "https://swordapp.github.io/swordv3/swordv3.jsonld",
  "@id": "https://192.168.56.101/sword/service-document",
  "@type": "ServiceDocument",
  "accept": [
    "*/*"
  ],
  "acceptArchiveFormat": [
    "application/zip"
  ],
  "acceptDeposits": true,
  "acceptMetadata": [
    "https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd",
    "https://w3id.org/ro/crate/1.1/"
  ],
  "acceptPackaging": [
    "*"
  ],
  "authentication": [
    "OAuth"
  ],
  "byReferenceDeposit": false,
  "collectionPolicy": {},
  "dc:title": "WEKO3",
  "dcterms:abstract": "",
  "digest": [
    "SHA-256",
    "SHA",
    "MD5"
  ],
  "maxAssembledSize": 30000000000000,
  "maxByReferenceSize": 30000000000000000,
  "maxSegments": 1000,
  "maxUploadSize": 16777216000,
  "onBehalfOf": true,
  "root": "https://192.168.56.101/sword/service-document",
  "staging": "",
  "stagingMaxIdle": 3600,
  "treatment": {},
  "version": "http://purl.org/net/sword/3.0"
}
```

#### POST /sword/service-document
##### リクエスト

```shell
$ curl -X POST -s -k https://192.168.56.101/sword/service-document -F "file=@import.zip;type=application/zip" \
    -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo" \
    -H "Content-Disposition:attachment; filename=import.zip" -H "Packaging:http://purl.org/net/sword/3.0/package/SimpleZip"
```

##### レスポンス

```json
{
  "@context": "https://swordapp.github.io/swordv3/swordv3.jsonld",
  "@id": "https://192.168.56.101/sword/deposit/96568",
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
}
```

  - -F オプション
      - POSTするファイルを指定する。自動的にContent-Typeは"multipart/form-data"となる
      - boundaryやContent-Lengthは自動で付加されるため自前で指定しなくてもよい
      - ファイル名の先頭には@を付加すること
      - ファイルのContent-Typeを"application/zip"とするため、ここでtypeを指定する（指定しないと application/octet-stream となってしまう）

  - -H オプション
      - Authorization は "Bearer" + " (半角スペース)" + "アクセストークン"の形式で指定する
      - Content-Disposition の filename は -Fオプションで指定したファイルのファイル名と一致させる
      - Packaging は "http://purl.org/net/sword/3.0/package/SimpleZip" を指定
      - 必須の Content-Length および Content-Type については前述の通り、-Fオプションにて自動付加されるため-Hオプションでの指定は不要


#### GET /sword/deposit/\<recid\>

```shell
curl -X GET https://192.168.56.101/sword/deposit/1 -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo"
```

  - recid
      - アイテムIDを指定する

  - -H オプション
      - Authorization は "Bearer" + " (半角スペース)" + "アクセストークン"の形式で指定する

#### PUT /sword/deposit/\<recid\>

```shell
curl -X PUT https://192.168.56.101/sword/deposit/1   -F "file=@import.zip;type=application/zip" \
    -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo" \
    -H "Content-Disposition:attachment; filename=import.zip" -H "Packaging:http://purl.org/net/sword/3.0/package/SimpleZip"
```

  - recid
      - アイテムIDを指定する

  - -F オプション
      - POSTするファイルを指定する。自動的にContent-Typeは"multipart/form-data"となる
      - boundaryやContent-Lengthは自動で付加されるため自前で指定しなくてもよい
      - ファイル名の先頭には@を付加すること
      - ファイルのContent-Typeを"application/zip"とするため、ここでtypeを指定する（指定しないと application/octet-stream となってしまう）

  - -H オプション
      - Authorization は "Bearer" + " (半角スペース)" + "アクセストークン"の形式で指定する

#### DELETE /sword/deposit/\<recid\>

```shell
curl -X DELETE https://192.168.56.101/sword/deposit/1 -H "Authorization:Bearer Dp85qdLJefoKZ9AuUeIVCqL0Zj9lHxulU1ZSqWGZKI0xJUfxA4wKFnWgztEo"
```

  - recid
      - アイテムIDを指定する

  - -H オプション
      - Authorization は "Bearer" + " (半角スペース)" + "アクセストークン"の形式で指定する


## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | -------------- | ---------------- | ------------------ | ------------ | ------------ | ------------------ |
| 利用可否 |       〇       |        〇        |         〇         |      △      |      △      |        ×          |

※ 〇：利用可能、△：一部機能のみ利用可能、×：利用不可

- アイテムを操作可能なAPIは、システム管理者、リポジトリ管理者が利用可能。

## 機能内容

- 各APIへのリクエストに応じて処理を実行しレスポンスを返す
    - OAuthアクセストークンによるユーザー認証を必須とする

- アイテム登録機能で登録に使用するZIPファイルは、メタデータのファイルがTSV/CSV形式、XML形式、あるいはJSON-LD形式である必要がある。
    - TSV/CSV形式のメタデータを含むZIPファイルの詳細は [ADMIN_2_4：インポート](../admin/ADMIN_2_4.md#インポートファイルtsvファイルについて) を参照
    - XML形式のメタデータを含むZIPファイルは、JPCOARスキーマに準拠したXMLファイルを含むZIPファイルである必要がある。
    - JSON-LD形式のメタデータを含むZIPファイルは、[RO-Crate+BagIt](../admin/ADMIN_2_5.md#ro-cratebagitファイルの構成)
      またはSWORDBagItに準拠したZIPファイルである必要がある。

- メタデータ形式がXMLおよびJSON-LDの場合は、マッピング機能をもちいてWEKO3のアイテムタイプへ変換されメタデータの登録および更新に使用される。

- メタデータ形式がJSON-LDの場合、メタデータ内の特定のフラグが有効の場合、展開せずZIPファイルそのものをアイテムのファイルとして保存する。  
  フラグについては [ADMIN_2_5：RO-Crate インポート](../admin/ADMIN_2_5.md#カスタム語彙) を参照。

- SWORD APIの管理者による設定は、[ADMIN_1_5：JSON-LD マッピング](../admin/ADMIN_1_5.md#json-ld-マッピング) 、
  [ADMIN_16_1：SWORD API](../admin/ADMIN_16_1.md) を参照。

## API仕様

### サービスドキュメント取得機能：GET /sword/service-document
リポジトリのサービスドキュメントを取得する。

#### エンドポイント
GET /sword/service-document

#### リクエストヘッダー

| ヘッダー      | 必須 | 説明                                                                                                                  | 例                                      |
| ------------- | ---- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Authorization |  ○  | 操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。 | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4" |
| On-Behalf-Of  |  -   | 代理投稿ユーザーのメールアドレス、パーソナルアクセストークンまたはePPNが入る。                                        |                                         |

#### レスポンスコード

| コード | ドキュメント         | 説明                                                                                                                  |
| ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 200    | サービスドキュメント | サーバーのサービスドキュメントを返す。                                                                                |
| 400    | エラードキュメント   | リクエスト内容に何らかの不備がある場合。                                                                              |
| 401    | エラードキュメント   | リクエストでAuthorization ヘッダーが提供されない場合。                                                                |
| 403    | エラードキュメント   | 認証に失敗した場合。                                                                                                  |
| 412    | エラードキュメント   | サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、<br/>リクエストでOn-Behalf-Of ヘッダーが提供された場合。 |
| 500    | エラードキュメント   | サーバー内部エラーが発生した場合。                                                                                    |


#### レスポンス
成功時 : [サービスドキュメント](#サービスドキュメント)を返す。
失敗時 : [エラードキュメント](#エラードキュメント)を返す。


### アイテム登録機能：POST /sword/service-document
一括登録用のZIPファイルを用いてアイテムを新規登録する。

#### エンドポイント
POST /sword/service-document

#### リクエストヘッダー

| フィールド          | 必須   | 説明                                                                                                                                                                                                                                                                                   | 例                                                                                                         |
| ------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Authorization       | ○     | 操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。                                                                                                                                                                  | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4"                                                                    |
| On-Behalf-Of        | -      | 代理投稿ユーザーのメールアドレス、パーソナルアクセストークンまたはePPNが入る。                                                                                                                                                                                                         | パーソナルアクセストークン: <br>　　"e0Pke8qpzEkkGjPE1RoSqNw7qu3tH4..."<br>ePPN: "sample@sampleuniv.ac.jp" |
| Content-Disposition | ○     | リクエストボディに付加したファイルのファイル名を指定する。                                                                                                                                                                                                                             | "attachment; filename=example.zip"                                                                         |
| Content-Length      | -      | リクエストの大きさを指定する。付与されていない場合、リクエストのファイルサイズを代わりに参照する。                                                                                                                                                                                     | 1024000                                                                                                    |
| Content-Type        | ○     | リクエストボディにファイルを付加するため "multipart/form-data" を指定する。                                                                                                                                                                                                            | multipart/form-data; boundary=xxxxxxxx                                                                     |
| Packaging           | ○     | パッケージフォーマットと指定する。<br/>SWORDでは以下の3つのパッケージフォーマットが定義されている。<br/>http://purl.org/net/sword/3.0/package/Binary<br/>http://purl.org/net/sword/3.0/package/SimpleZip<br/>http://purl.org/net/sword/3.0/package/SWORDBagIt<br/>※現在Binaryは未対応 | "http://purl.org/net/sword/3.0/package/SimpleZip"                                                          |
| Digest              | ※     | ボディに付加したファイルのハッシュ値を指定する。<br/>※ダイジェスト検証設定（[設定値:21](#conf21)）が有効の場合、必須。                                                                                                                                                                | "SHA-256=e0Pke8qpzEkkGjPE1RoSqNw7qu3tH4..."                                                                |


#### ボディ

| フィールド | 必須 | 説明                                                                                                               | 例                                                          |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| file       | ○   | form-data 形式でボディにZIPファイルを付加する。<br/>ファイルのContent-Type には"application/zip"を指定すること。   | "file=@project/post_files/example.zip;type=application/zip" |

#### レスポンスコード

| コード | ドキュメント           | 説明                                                                                                                              |
| ------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 201    | ステータスドキュメント | 登録されたアイテムのステータスドキュメントを返す。                                                                                |
| 202    | ステータスドキュメント | 登録するアイテムのステータスドキュメントを返す。<br> 登録のリクエストを受け付け、アクティビティが承認待ちとなっていることを示す。 |
| 400    | エラードキュメント     | リクエスト内容に何らかの不備がある場合。                                                                                          |
| 401    | エラードキュメント     | リクエストでAuthorization ヘッダーが提供されない場合。                                                                            |
| 403    | エラードキュメント     | 認証に失敗した場合。<br/>認証したOAuthトークンに必要なスコープが与えられていない場合。                                            |
| 404    | エラードキュメント     | 登録されたアイテムが見つからない場合。                                                                                            |
| 412    | エラードキュメント     | サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、<br/>リクエストでOn-Behalf-Of ヘッダーーが提供された場合。           |
| 413    | エラードキュメント     | 送信されたファイルのサイズがサーバーに設定されたmaxUploadSizeを超えている場合。                                                   |
| 415    | エラードキュメント     | ヘッダーまたはボディに付加されたファイルのContent-Typeがサーバー側で<br/>サポートされていない場合。                               |
| 500    | エラードキュメント     | サーバー内部エラーが発生した場合。                                                                                                |


#### レスポンス
成功時 : [ステータスドキュメント](#ステータスドキュメント)を返す。
失敗時 : [エラードキュメント](#エラードキュメント)を返す。


### アイテム状態取得機能：GET /sword/deposit/\<recid\>

#### エンドポイント
GET /sword/deposit/\<recid\>

#### リクエストヘッダー

| フィールド         | 必須 | 説明                                                                                                                  | 例                                      |
| ------------------ | ---- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Authorization      | ○   | 操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。 | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4" |
| On-Behalf-Of       | -    | 代理投稿ユーザーのメールアドレス、パーソナルアクセストークンまたはePPNが入る。                                        | "user@example.com"                      |


#### パスパラメータ

| キー        | 必須 | 説明                    | 例                   |
| ----------- | ---- | ----------------------- | -------------------- |
| recid       | ○   | レコードID              | 2000021              |


#### レスポンスコード

| コード | ドキュメント           | 説明                                                                                                                       |
| ------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 200    | ステータスドキュメント | 指定されたアイテムのステータスドキュメントを返す。                                                                         |
| 400    | エラードキュメント     | リクエスト内容に何らかの不備がある場合。                                                                                   |
| 401    | エラードキュメント     | リクエストでAuthorization ヘッダーが提供されない場合。                                                                     |
| 403    | エラードキュメント     | 認証に失敗した場合。                                                                                                       |
| 404    | エラードキュメント     | 指定したrecidに該当するアイテムが存在しない（削除されている）場合。                                                        |
| 412    | エラードキュメント     | サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、<br/>リクエストでOn-Behalf-Of ヘッダーが提供された場合。      |
| 500    | エラードキュメント     | サーバー内部エラーが発生した場合。                                                                                         |


#### レスポンス
成功時 : [ステータスドキュメント](#ステータスドキュメント)を返す。
失敗時 : [エラードキュメント](#エラードキュメント)を返す。


### アイテム更新機能：PUT /sword/deposit/\<recid\>

#### エンドポイント
PUT /sword/deposit/\<recid\>

#### リクエストヘッダー

| フィールド          | 必須   | 説明                                                                                                                                                                                                                                                                                   | 例                                                                                                         |
| ------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Authorization       | ○     | 操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。                                                                                                                                                                  | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4"                                                                    |
| On-Behalf-Of        | -      | 代理投稿ユーザーのメールアドレス、パーソナルアクセストークンまたはePPNが入る。                                                                                                                                                                                                         | パーソナルアクセストークン: <br>　　"e0Pke8qpzEkkGjPE1RoSqNw7qu3tH4..."<br>ePPN: "sample@sampleuniv.ac.jp" |
| Content-Disposition | ○     | リクエストボディに付加したファイルのファイル名を指定する。                                                                                                                                                                                                                             | "attachment; filename=example.zip"                                                                         |
| Content-Length      | -      | リクエストの大きさを指定する。付与されていない場合、リクエストのファイルサイズを代わりに参照する。                                                                                                                                                                                     | 1024000                                                                                                    |
| Content-Type        | ○     | リクエストボディにファイルを付加するため "multipart/form-data" を指定する。                                                                                                                                                                                                            | multipart/form-data; boundary=xxxxxxxx                                                                     |
| Packaging           | ○     | パッケージフォーマットと指定する。<br/>SWORDでは以下の3つのパッケージフォーマットが定義されている。<br/>http://purl.org/net/sword/3.0/package/Binary<br/>http://purl.org/net/sword/3.0/package/SimpleZip<br/>http://purl.org/net/sword/3.0/package/SWORDBagIt<br/>※現在Binaryは未対応 | "http://purl.org/net/sword/3.0/package/SimpleZip"                                                          |
| Digest              | ※     | ボディに付加したファイルのハッシュ値を指定する。<br/>※ダイジェスト検証設定（[設定値:21](#conf21)）が有効の場合、必須。                                                                                                                                                                | "SHA-256=e0Pke8qpzEkkGjPE1RoSqNw7qu3tH4..."                                                                |

#### パスパラメータ

| キー        | 必須 | 説明                    | 例                   |
| ----------- | ---- | ----------------------- | -------------------- |
| recid       | ○   | レコードID              | 2000021              |

#### ボディ

| フィールド | 必須 | 説明                                                                                                               | 例                                                          |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| file       | ○   | form-data 形式でボディにZIPファイルを付加する。<br/>ファイルのContent-Type には"application/zip"を指定すること。   | "file=@project/post_files/example.zip;type=application/zip" |

#### レスポンスコード

| コード | ドキュメント           | 説明                                                                                                                              |
| ------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 200    | ステータスドキュメント | 更新されたアイテムのステータスドキュメントを返す。                                                                                |
| 202    | ステータスドキュメント | 更新するアイテムのステータスドキュメントを返す。<br> 更新のリクエストを受け付け、アクティビティが承認待ちとなっていることを示す。 |
| 400    | エラードキュメント     | リクエスト内容に何らかの不備がある場合。                                                                                          |
| 401    | エラードキュメント     | リクエストでAuthorization ヘッダーが提供されない場合。                                                                            |
| 403    | エラードキュメント     | 認証に失敗した場合。<br/>認証したOAuthトークンに必要なスコープが与えられていない場合。                                            |
| 404    | エラードキュメント     | 登録されたアイテムが見つからない場合。                                                                                            |
| 412    | エラードキュメント     | サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、<br/>リクエストでOn-Behalf-Of ヘッダーーが提供された場合。           |
| 413    | エラードキュメント     | 送信されたファイルのサイズがサーバーに設定されたmaxUploadSizeを超えている場合。                                                   |
| 415    | エラードキュメント     | ヘッダーまたはボディに付加されたファイルのContent-Typeがサーバー側で<br/>サポートされていない場合。                               |
| 500    | エラードキュメント     | サーバー内部エラーが発生した場合。                                                                                                |


### アイテム削除機能：DELETE /sword/deposit/\<recid\>

#### エンドポイント
DELETE /sword/deposit/\<recid\>

#### リクエストヘッダー

| フィールド         | 必須 | 説明                                                                                                                  | 例                                      |
| ------------------ | ---- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Authorization      | ○   | 操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。<br/>"Bearer" + " (半角スペース)" + "トークン"の形式。 | "Bearer fVzaeTNY5PCHsNS3rZOARrYR7kPBl4" |
| On-Behalf-Of       | -    | 代理投稿ユーザーのメールアドレス、パーソナルアクセストークンまたはePPNが入る。                                        | "user@example.com"                      |


#### パスパラメータ

| キー        | 必須 | 説明                    | 例                   |
| ----------- | ---- | ----------------------- | -------------------- |
| recid       | ○   | レコードID              | 2000021              |


#### レスポンスコード

| コード | ドキュメント           | 説明                                                                                                                       |
| ------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 202    | -                      | アイテム削除のリクエストを受け付け、削除アクティビティが承認待ちとなっていることを示す。                                   |
| 204    | -                      | 空のレスポンスを返す。削除に成功したことを示す。                                                                           |
| 400    | エラードキュメント     | リクエスト内容に何らかの不備がある場合。                                                                                   |
| 401    | エラードキュメント     | リクエストでAuthorization ヘッダーが提供されない場合。                                                                     |
| 403    | エラードキュメント     | 認証に失敗した場合。                                                                                                       |
| 404    | エラードキュメント     | 指定したrecidに該当するアイテムが存在しない（削除されている）場合。                                                        |
| 412    | エラードキュメント     | サーバー側がOn-Behalf-Of をサポートしていないにもかかわらず、<br/>リクエストでOn-Behalf-Of ヘッダーが提供された場合。      |
| 500    | エラードキュメント     | サーバー内部エラーが発生した場合。                                                                                         |


#### レスポンス
成功時 : 空のレスポンスを返す。 アクティビティを使用している場合、アクティビティ詳細画面のURLをLinkヘッダーに含める。
失敗時 : [エラードキュメント](#エラードキュメント)を返す。


## ドキュメント仕様

### サービスドキュメント
サーバー全体の機能と操作パラメータを定義したドキュメント

| 項目                         | 型      | 説明                                                                                                                                                       |
| ---------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| @context                     | string  | "https://swordapp.github.io/swordv3/swordv3.jsonld" を固定で出力。                                                                                         |
| @id                          | string  | "[WEKO3のURL]/sword/service-document"を出力。                                                                                                              |
| @type                        | string  | "ServiceDocument"を固定で出力。                                                                                                                            |
| accept                       | array   | サーバーに受け入れられるコンテンツタイプのリスト。"\*/\*"を出力する。[設定値:3](#conf03)                                                                   |
| acceptArchiveFormat          | array   | サーバーが解凍できるアーカイブ形式のリスト。現状"application/zip"のみ対応。[設定値:4](#conf04)                                                             |
| acceptDeposits               | boolean | サーバーがデポジットを受け入れるか否か。[設定値:5](#conf05)                                                                                                |
| acceptMetadata               | array   | サーバーで受け入れ可能なメタデータ形式のリスト。[設定値:6](#conf06)                                                                                        |
| acceptPackaging              | array   | サーバーで受け入れ可能なパッケージ形式のリスト。<br/>現状すべての形式を受け入れるが、アイテム登録はSimpleZip/SWORDBagIt形式でのみ可能。[設定値:9](#conf07) |
| authentication               | Array   | サーバーでサポートされている認証スキームのリスト。現状”OAuth”のみ対応。[設定値:15](#conf15)                                                              |
| byReferenceDeposit           | boolean | サーバーがbyReferenceDepositをサポートしているか否か。現状未対応のためFalseを出力。[設定値:12](#conf12)                                                    |
| collectionPolicy             | object  | コレクションポリシーを示すオブジェクト。[設定値:8](#conf08)                                                                                               |
| collectionPolicy.@id         | string  | コレクションポリシーのURL。                                                                                                                                |
| collectionPolicy.description | string  | コレクションポリシーの説明。                                                                                                                               |
| dc:title                     | string  | リポジトリの名称を出力。"WEKO3"を固定で出力。                                                                                                              |
| dcterms:abstract             | string  | リポジトリの説明。未設定。[設定値:2](#conf02)                                                                                                              |
| digest                       | array   | サーバーが受け入れるdigest形式のリスト。現状はSHA-256の検証が可能。[設定値:14](#conf14)                                                                    |
| maxAssembledSize             | integer | Segmented File Upload時のファイル合計最大サイズ（単位：byte）。[設定値:19](#conf19)                                                                        |
| maxByReferenceSize           | integer | By-Reference Deposit時のファイル最大サイズ（単位：byte）。[設定値:18](#conf18)                                                                             |
| maxSegmentSize               | integer | Segmented File Upload時の１ファイルの最大サイズ（単位：byte）。<br/>現時点では出力していない。                                                             |
| maxSegments                  | integer | Segmented File Upload時のセグメントの最大数。[設定値:20](#conf20)                                                                                          |
| maxUploadSize                | integer | アップロードされるファイルの最大サイズ（単位：byte）。[設定値:17](#conf17)                                                                                 |
| minSegmentSize               | integer | Segmented File Upload時の１ファイルの最小サイズ（単位：byte）。                                                                                            |
| onBehalfOf                   | boolean | 代理投稿をサポートしているか否か。[設定値:13](#conf13)                                                                                                     |
| root                         | string  | サービスドキュメントのルートURL。                                                                                                                          |
| services                     | array   | 親サービスに含まれるサービスのリスト。現状未対応。[設定値:16](#conf16)                                                                                     |
| staging                      | string  | Segmented File Upload時にコンテンツをステージング先URL。現状未対応のため空文字を出力。[設定値:10](#conf10)                                                 |
| stagingMaxIdle               | integer | ステージングされたファイルの最小保持時間。[設定値:11](#conf11)                                                                                             |
| treatment                    | object  | デポジット時に期待される処理のURLと説明を示すオブジェクト。[設定値:9](#conf09)                                                                            |
| treatment.@id                | string  | 処理のURL。                                                                                                                                                |
| treatment.description        | string  | 処理の説明。                                                                                                                                               |
| version                      | string  | サポートしているSWORDバージョン。"http://purl.org/net/sword/3.0"を出力。[設定値:1](#conf01)                                                                |


### ステータスドキュメント
アイテムの内容と現在の状態に関する詳細情報を示すドキュメント

| 項目                         | 型      | 説明                                                                                                                                   |
| ---------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| @context                     | string  | "https://swordapp.github.io/swordv3/swordv3.jsonld" を固定で出力。                                                                     |
| @id                          | string  | "[WEKO3のURL]/sword/deposit/[アイテムのrecid]"を出力。                                                                                 |
| @type                        | string  | "ServiceDocument"を固定で出力。                                                                                                        |
| actions                      | object  | アイテムに対してSWORDで使用可能なアクション。  現時点では deleteObject のみTrueを返し、それ以外はFalseを返すようになっている。         |
| actions. appendFiles         | boolean | ファイル追加要求が発行可能か否か。                                                                                                     |
| actions.appendMetadata       | boolean | メタデータ追加要求が発行可能か否か。                                                                                                   |
| actions. deleteFiles         | boolean | ファイル削除要求が発行可能か否か。                                                                                                     |
| actions. deleteMetadata      | boolean | メタデータ削除要求が発行可能か否か。                                                                                                   |
| actions. deleteObject        | boolean | アイテム削除要求が発行可能か否か。                                                                                                     |
| actions. getFiles            | boolean | ファイル取得要求が発行可能か否か。                                                                                                     |
| actions. getMetadata         | boolean | メタデータ取得要求が発行可能か否か。                                                                                                   |
| actions. replaceFiles        | boolean | ファイル置き換え要求が発行可能か否か。                                                                                                 |
| actions. replaceMetadata     | boolean | メタデータ置き換え要求が発行可能か否か。                                                                                               |
| eTag                         | string  | アイテムのeTag。  WEKOではアイテムのリビジョン番号を返す。                                                                             |
| fileSet                      | object  | ファイルセットを示すオブジェクト。  現時点では空オブジェクトを返す。                                                                   |
| fileSet.@id                  | string  | ファイルセットのURL。                                                                                                                  |
| fileSet.eTag                 | string  | ファイルセットのeTag。                                                                                                                 |
| links                        | array   | アイテムのリンクを示すオブジェクト。  現時点ではアイテム詳細ページのURLを出力する。またDOIやCNRIハンドルを持つ場合も同様に出力する。   |
| links[].@id                  | string  | リソースのURL。                                                                                                                        |
| links[].byReference          | string  | byReference deposit の際の参照元URL。                                                                                                  |
| links[].contentType          | string  | リソースのコンテンツタイプ。                                                                                                           |
| links[].dcterms:isReplacedBy | string  | 同じオブジェクト内のファイルの新しいバージョンへのURL。                                                                                |
| links[].dcterms:relation     | string  | 非SWORDアクセスポイントへのURL。                                                                                                       |
| links[].dcterms:replaces     | string  | 同じオブジェクト内の古いバージョンのファイルへのURL。                                                                                  |
| links[].depositedBy          | string  | アイテム登録を行ったユーザーの識別子。                                                                                                 |
| links[].depositedOn          | string  | アイテム登録日時のタイムスタンプ。                                                                                                     |
| links[].depositedOnBehalfOf  | string  | 代理投稿により登録を行ったユーザーの識別子。                                                                                           |
| links[].derivedFrom          | string  | 現在のリソースが派生したリソースのURLへの参照。                                                                                        |
| links[].eTag                 | string  | リソースのeTag。                                                                                                                       |
| links[].log                  | string  | クライアントが知っておくべきデポジットに関連する情報。                                                                                 |
| links[].packaging            | string  | リソースがパッケージである場合、パッケージ形式の識別子を示す。                                                                         |
| links[].rel                  | string  | リソースとオブジェクトの関係。  以下の何れかの文字列を持つ。<ul><li>alternate</li><li>packaging</li><li>depositedOn</li><li>depositedOnBehalfOf</li><li>status</li><li>log</li><li>dcterms:relation</li><li>dcterms:replaces</li><li>dcterms:isReplacedBy</li><li>versionReplaced</li><li>eTag</li><li>byReference</li><li>derivedFrom</li><li>metadataFormat</li></ul> |
| links[].status               | string  | 取り込みに関するリソースのステータス。                                                                                                 |
| links[].versionReplacedOn    | string  | 現在のリソースが新しいリソースに置き換えられた日付。                                                                                   |
| metadata                     | object  | メタデータを示すオブジェクト。  現時点では空オブジェクトを返す。                                                                       |
| metadata.@id                 | string  | メタデータのURL。                                                                                                                      |
| metadata.eTag                | string  | メタデータのeTag。                                                                                                                     |
| service                      | string  | サービスドキュメントのURL。                                                                                                            |
| state                        | array   | アイテムがサーバー上にある状態のリスト。                                                                                               |
| state[].@id                  | string  | 状態の識別子。現状では"http://purl.org/net/sword/3.0/state/ingested"を固定で出力。                                                     |
| state[].description          | string  | 状態の説明                                                                                                                             |

### エラードキュメント
エラー内容を表すドキュメント

| 項目      | 型     | 説明                                                                |
| --------- | ------ | ------------------------------------------------------------------- |
| @context  | string | "https://swordapp.github.io/swordv3/swordv3.jsonld"を固定で出力。   |
| @type     | string | エラータイプを示す文字列。[エラータイプ](#エラータイプ) を参照。    |
| error     | string | エラー内容の説明。                                                  |
| log       | string | より詳細なエラー内容。現在は出力していない。                        |
| timestamp | string | エラー発生時のタイムスタンプ。                                      |

## エラータイプ

| エラータイプ文字列           | エラーコード | エラー原因等                                                                           |
| ---------------------------- | ------ | -------------------------------------------------------------------------------------------- |
| **SWORD v3 ErrorType**       |        |                                                                                              |
| AuthenticationFailed         | 403    | 認証に失敗。                                                                                 |
| AuthenticationRequired       | 401    | 認証情報が不足。                                                                             |
| BadRequest                   | 400    | リクエストに何らかの不備がある。                                                             |
| ByReferenceFileSizeExceeded  | 400    | サーバーの制限を超えるファイルをデポジットしようとした。                                     |
| ByReferenceNotAllowed        | 412    | サーバーが By-Reference deposit をサポートしていない。                                       |
| ContentMalformed             | 400    | リクエスト本文の内容に不正がある。                                                           |
| ContentTypeNotAcceptable     | 415    | サーバーで許可されていないコンテンツタイプをリクエストした。                                 |
| DigestMismatch               | 412    | リクエストヘッダーによって提供されたdigestがサーバーで受け取ったコンテンツと一致していない。 |
| ETagNotMatched               | 412    | リクエストヘッダーによって提供されたIf-Matchの値が更新対象コンテンツのeTagと一致していない。 |
| ETagRequired                 | 412    | リクエストヘッダーにIf-Matchの値が指定されていない。                                         |
| Forbidden                    | 403    | サーバーによって許可されていない操作をリクエストした。                                       |
| FormatHeaderMismatch         | 415    | サーバーがサポートしていない形式のコンテンツがリクエストされた。                             |
| InvalidSegmentSize           | 400    | Segmented File Upload時のファイルサイズが範囲外。                                            |
| MaxAssembledSizeExceeded     | 400    | Segmented File Upload時の合計ファイルサイズが最大値を超えている。                            |
| MaxUploadSizeExceeded        | 413    | アップロードされたコンテンツサイズが最大値を超えている。                                     |
| MetadataFormatNotAcceptable  | 415    | サーバーがサポートしていない形式のMetadata-Formatがリクエストされた。                        |
| MethodNotAllowed             | 405    | メソッドへのアクセスが許可されていない。                                                     |
| OnBehalfOfNotAllowed         | 412    | サーバーが On-Behalf-Of をサポートしていない。                                               |
| PackagingFormatNotAcceptable | 415    | サーバーがサポートしていない形式のPackagingフォーマットがリクエストされた。                  |
| SegmentedUploadTimedOut      | 410    | Segmented File Upload先のURLにアクセスできない。                                             |
| SegmentLimitExceeded         | 400    | セグメント数が最大値を超えている。                                                           |
| UnexpectedSegment            | 400    | サーバーが予期していないセグメントを受信した。                                               |
| **Additional ErrorType**     |        |                                                                                              |
| NotFound                     | 404    | リクエストされたリソースが存在しない。                                                       |
| ServerError                  | 500    | サーバー内部エラーが発生した。                                                               |
| TooManyRequests              | 429    | 分間のリクエスト数が制限を超えている。                                                       |

## 関連モジュール


  - invenio_oauth2server：OAuthトークンによるユーザー認証を行う

  - invenio_deposit：OAuthトークンが参照するデポジット操作スコープを定義している

  - weko_swordserver：リクエストの処理を行う

  - weko_records_ui：レコード情報の取得、アイテムの削除を実行する

  - weko_search_ui：インポート処理およびメタデータのマッピング処理を実行する

  - weko_workflow：ワークフロー経由でインポート処理を実行する

## 関連テーブル

  - item_type_mapping：アイテムタイプとjpcoar語彙のマッピング情報を保持する

    - id：ID
    - item_type_id：アイテムタイプID
    - mapping：マッピング定義(JSON)

  - sword_clients：SWORD連携設定情報を保持する

    - id：ID
    - client_id：クライアントID
    - active：有効フラグ
    - registration_type_id：登録方式区分。1:直接登録、2:ワークフロー登録
    - mapping_id：マッピング定義ID
    - workflow_id：ワークフローID
    - duplicate_check：アイテム重複チェックフラグ
    - meta_data_api：メタデータ補完APIの優先順序

  - jsonld_mappings：アイテムタイプとJSON-LD語彙のマッピング定義設定を保持する

    - id：マッピング定義ID
    - name：マッピング定義名
    - mapping：マッピング定義(JSON)
    - item_type_id：アイテムタイプID
    - version_id：バージョンID
    - is_delete：論理削除フラグ

  - oauth2server_token：クライアントが使用できるトークンを保持する

    - id：オブジェクトID
    - client_id：クライアントID
    - user_id：ユーザーID
    - token_type：トークンタイプ
    - access_token：アクセストークン
    - refresh_token：リフレッシュトークン
    - expires：有効期限
    - _scopes：スコープ
    - is_personal：個人用トークンフラグ
    - is_internal：内部用トークンフラグ


## 処理概要
使用する設定値は[サーバー設定値](#サーバー設定値)、エラーメッセージは[エラーメッセージ](#エラーメッセージ)を参照。

### サービスドキュメント取得機能：GET /sword/service-document

- リクエストをチェックする
    - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
    - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
- サーバー設定値を参照し、サービスドキュメントを生成する
- サービスドキュメントを返却する

### アイテム登録機能：POST /sword/service-document
#### GRDM側(想定)
1. GRDMでインポート画面を表示する際、WEKOのAPIを使用しユーザーの選択可能な登録先を取得する
2. GRDMでインポートするデータを指定し、パッケージ化する
3. WEKOのエンドポイントPOST /sword/service-documentにパッケージを送信する  
  この時、リクエストヘッダーにアクセストークンを付加する

#### WEKO3側
1. リクエストをチェックする
    - **`Authorization`** ヘッダーに記載されたアクセストークンを使用しユーザーを認証する。  
      アクセストークンのScopeを確認し、`deposit:write`、`deposit:actions`、`item:create`が与えられていなければエラーとする。
    - **`On-Behalf-Of`** ヘッダーが存在する場合、`On-Behalf-Of`許容設定（[設定値:13](#conf13)）が無効であればエラー（[メッセージ:2](#err02)）とする。
    - **`Content-Length`** ヘッダーおよびファイルサイズを検証する。  
      `Content-Length`ヘッダーの値あるいはファイルサイズがアップロードのサイズ上限（[設定値:17](#conf17)）を上回っていればエラー（[メッセージ:5](#err05)）とする。
    - **`Content-Disposition`** ヘッダーを解析する。  
      値が`attachment`かつオプションにファイル名が指定されているかを確認し、満たさない場合はエラー（[メッセージ:8](#err08)）とする。
      リクエストのファイルの有無や実際のファイルと上記のファイル名の合致を確認し、不一致であればエラー（[メッセージ:9](#err09）)とする。
    - **`Content-Type`** ヘッダーをもとに送付されたファイルを検証する。  
      ヘッダーの値が`application/zip`でなければ、エラー（[メッセージ:6](#err06)）とする。
    - **`Packaging`** ヘッダーを検証する。  
      値の末尾が`SWORDBagIt`のとき、`/metadata`フォルダ直下に`sword.json`ファイルが存在すればSWORDBagIt形式と判定し、なければエラー（[メッセージ:16](#err16)）とする。  
      値の末尾が`SimpleZip`のとき、`/data`フォルダ直下に`ro-crate-metadata.json`ファイルが存在すればRO-Crate+BagIt形式と判定し、`.tsv/.csv`ファイルがあればTSV/CSV形式、`.xml`ファイルがあればXML形式と判定する。  
      値がその他の場合はエラー（[メッセージ:07](#err7)）とする。
    - **`Digest`** ヘッダーを検証する。  
      メタデータ形式がJSON-LD、かつダイジェスト検証設定（[設定値:21](#conf21)）が有効であるとき、DigestとリクエストボディのZipファイルのハッシュ値が一致しなければエラー（[メッセージ:10](#err10)）とする。

    ※ SWORD APIでは使用可能なエラータイプが定められているため、適切なエラータイプが存在しない場合はBad Request（エラーコード400）とし、エラードキュメントにエラー原因を記述し返却する。

2. ファイル内容に不備が無いかのチェックを行う

    Zipファイルを展開し、必要なファイルが含まれているか確認する。メタデータファイル形式によって必須事項が異なる。

    **TSV/CSV形式**
    - メタデータを記述したTSV/CSVファイルが含まれていなければエラーとする。

    **XML形式**
    - メタデータを記述したXMLファイルが含まれていなければエラーとする。

    **JSON-LD形式**
    - 登録対象のファイルそれぞれのハッシュ値が`manifest-sha256.txt` に記載されている値と一致しなければエラー（[メッセージ:24](#err24)）とする。

3. 登録の前処理を行う

   メタデータファイル形式がXMLおよびJSON-LDであれば、メタデータをアイテムタイプへマッピングする。  
   また、アイテムを登録するとき、一括登録機能をもちいて直接登録をするか、個別登録機能をもちいてワークフローを経由して登録するかを、
   [ADMIN_16_1：SWORD API TSV/XML](../admin/ADMIN_16_1.md)および[ADMIN_16_2：SWORD API JSON-LD](../admin/ADMIN_16_2.md)の設定から取得する。  
   このとき、設定されたワークフローが削除されていた場合や、Item Registration アクションが含まれていなければエラー（[メッセージ:22](#err22)）とする。

    **TSV/CSV形式**
    - メタデータのマッピングを行わず、直接アイテムタイプとして読み込む。
    - アイテムタイプをもとに、使用できるワークフローを取得する。

    **XML形式**
    - メタデータをアイテムタイプにマッピングする。
    - アイテムタイプとjpcoar語彙のマッピング定義からのキーが一致するXMLのメタデータの属性値を探す。
    - 新しいJSONを作成し対応する「item_xxxx」をキー、対応するXMLのメタデータ部分を値とする。

    **JSON-LD形式**
    - アクセストークンから、マッピング定義、マッピング先アイテムタイプを取得する。  
        クライアントに対する設定がない場合はエラー（[メッセージ:21](#err21)）とする。
    - JSONファイルからメタデータを取得し、マッピング定義に基づいてメタデータをアイテムタイプへマッピングする。  
        マッピング処理の詳細については、[メタデータマッピング機能](../admin/ADMIN_2_5.md#マッピング機能)を参照。  
        SWORD APIとしては原則1リクエストにつき1つのアイテムが登録されるべきだが、例外としてアイテム分割フラグ（[wk:isSplited](../admin/ADMIN_2_5.md#wkissplitedアイテム分割フラグ)）が有効であれば、メタデータを論文アイテムと論拠データアイテムに分割する。
        [アイテム分割機能](#アイテム分割機能)を参照。  
    - 登録用ファイル保存フラグ（[wk:saveAsIs](../admin/ADMIN_2_5.md#wksaveasis登録用ファイル保存フラグ)）が有効であれば、メタデータを含むZIPファイルそのものをアイテムのファイルとして
      登録するようにメタデータを作成する。
    - マッピング先が無いメタデータはテキストエリアに保存する。
    - メタデータ自動補完フラグ（[wk:metadataAutoFill](../admin/ADMIN_2_5.md#wkmetadataautofillメタデータ自動補完フラグ)）が有効で、補完にもちいるDOIが指定されていれば、メタデータ補完APIを呼び出し、メタデータを補完する。
    - ファイルが階層化されている場合、weko3のストレージでは階層を維持できないため、あらかじめ相対パスをURLエンコードしてファイル名を改め、`/data/`フォルダ直下に配置する。  
      例：`/data/20230101/sample.pdf` → `/data/20230101%2Fsample.pdf`

    **共通処理**
    - `On-Behalf-Of`ヘッダーが存在する場合、その値を取得しアイテムの代理投稿者情報とする。
    - 読み込まれたメタデータのバリデーションチェックや必須項目のチェックを行い、問題があればエラー（[メッセージ:11](#err11)）とする。
    - 登録先インデックスの状態やアイテムの公開ステータスのチェックを行い、問題があればエラーとする。
    - 設定されたアイテム重複チェック（[設定値:27](#conf27)）が有効であれば、アイテムの重複チェックを行う。  
      重複している場合はエラー（）とする。

4. 登録処理を行う
   アイテムの登録方法に応じて別々の登録処理を行う。

    **直接登録の場合**
    - 一括インポート機能を使用してインポート処理を行う。

    **ワークフロー経由で登録する場合**

    - 設定されたワークフローで新しいアクティビティを作成する。
    - 読み込まれたメタデータをもとにアクティビティにメタデータや登録先インデックスを保存する。
    - 承認不要のワークフローの場合はワークフローを最後まで実行し登録を完了させる。
    - 承認が必要なワークフローの場合はアクティビティを承認アクションまで進める。
    - アクティビティの進行に必要なのメタデータが存在しない場合はアクティビティを停止し、どのメタデータが必須かエラーメッセージをJSON-LD形式で返却する。
    - アイテムのPIDと、登録が完了した場合はレコードのURL、アクティビティ詳細画面のURLを返却する。

    ※ メタデータ形式がXML形式の場合、現時点ではインデックスを指定することができないため、直接登録は行えない。  
      また、ワークフロー経由で登録する場合、ワークフローに登録先インデックスが指定されていなければ、アクティビティにメタデータとファイルを登録して停止する。

    アイテムの登録処理に失敗した場合は、エラー（[メッセージ:14](#err14)）とする。

5. レスポンスを返却する
   - アイテムの登録が完了した場合は、登録されたアイテムのURLをステータスドキュメントに含めて返却する。
   - アイテムの登録が完了していない場合は、アクティビティのURLをステータスドキュメントに含めて返却する。
   - 一連の登録処理に問題がありエラーが発生した場合は、エラードキュメントを返却する。

### アイテム状態取得機能：GET /sword/deposit/\<recid\>

- リクエストをチェックする
    - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
    - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
- 指定されたrecidからアイテム情報を取得する
- 取得したアイテム情報からステータスドキュメントを生成する
- ステータスドキュメントを返却する

### アイテム更新機能：PUT /sword/deposit/\<recid\>

ほとんどの処理はアイテム状態取得機能と同様であるが、以下の点が異なる。

- アイテムの分割は許可されない
- SWORD v3プロトコルでは、PUTメソッドはアイテムのメタデータとファイルすべての置き換えを意味するが、
  例外として[メタデータのみ置換フラグ](../admin/ADMIN_2_5.md#wkmetadatareplaceメタデータのみ置換フラグ)が有効な場合は、
  メタデータのみを置き換え、ファイルを維持する。  
  本来、このような扱いはメタデータのURIに対するPOSTメソッドで行うべき処理であるが、暫定的にアイテム更新のPUTメソッドで対応する。
- 画面やAPI同士との競合を避けるため、排他制御を行う。排他制御によって更新が拒否された場合は、エラー（[ーメッセージ:25](#err25)）とする。  
  一括インポート機能によって更新中である場合、すでにアイテムに対するアクティビティが存在する場合も同様にエラー（[ーメッセージ:26](#err26)、[メッセージ:27](#err27)）とする。


### アイテム削除機能：DELETE /sword/deposit/\<recid\>

- リクエストをチェックする
    - Authorizationヘッダーに記載されたOAuth認証情報を使用しWEKOにログインする
    - On-Behalf-Ofヘッダーが存在する場合、サーバー設定を確認する
- [ADMIN_16_1：SWORD API TSV/XML](../admin/ADMIN_16_1.md)および[ADMIN_16_2：SWORD API JSON-LD](../admin/ADMIN_16_2.md)の設定、
  ワークフローに削除用フローが設定されているかを確認し、直接削除を行うか、ワークフローを経由して削除するかを決定する。
- 画面やAPI同士との競合を避けるため、排他制御を行う。排他制御によって更新が拒否された場合は、エラー（[メッセージ:25](#err25)）とする。  
  一括インポート機能によって更新中である場合、すでにアイテムに対するアクティビティが存在する場合も同様にエラー（[メッセージ:26](#err26)、[メッセージ:27](#err27)）とする。
- 直接削除の場合、アイテムの削除を行う
- ワークフロー経由で削除する場合、削除用のアクティビティを作成し、承認アクションがなければアイテムの削除を行う。ある場合はアクティビティを承認アクションまで進めて停止する。
- 空のレスポンスを返却する


### アイテム分割機能

- SWORD v3プロトコルでは、1リクエストにつき1つのアイテムが登録されるべきであるが、WEKO3ではアイテム分割機能を提供している。
- これは、1つのアイテムを論文アイテムと論拠データアイテムに分割して登録する機能であり、複数アイテムを1リクエストで登録するために提供される機能ではない。
- この機能を使用するには、JSON-LD形式のメタデータ内で、`wk:isSplited`プロパティに`true`を設定する必要がある。
- 記述方法については、[ADMIN_2_5：RO-Crate インポート](../admin/ADMIN_2_5.md#wkissplitedアイテム分割フラグ)を参照。
- 分割されるアイテムは、論文アイテムと論拠データアイテムの2種に分類され、相互にアイテムリンクされる。
- 論文アイテムから論拠データアイテムへのアイテムリンクのリレーションタイプは`isSupplementedBy`、論拠データアイテムから論文アイテムへのアイテムリンクのリレーションタイプは`isSupplementTo`である。
- アイテムリンクにはアイテムIDが必要なため、先に論拠データを登録しそのアイテムIDを取得し、論文アイテムを登録する際に相互にアイテムリンクを設定する。 
- このとき、`isSupplementTo`のアイテムリンク先をもつ論拠データアイテムを先に登録するように、アイテムの登録順を制御する。

### 処理に関するエトセトラ

- ZIPの展開に使用しているライブラリ：zipfile
- ハッシュ値の計算に使用しているライブラリ：hashlib
- Bagの整合性検証に使用しているライブラリ：[bagit v1.7.0](https://github.com/LibraryOfCongress/bagit-python/tree/v1.7.0)
- アイテムをインポートする際に作成する一時ディレクトリは以下のようにミリ秒までの日時を含めて生成する。

    /tmp/weko_import_YYYYMMDDhhmmssfff


## エラーメッセージ
1. OAuthトークンがリクエストに含まれていない場合<span id="err01">
  ```python
  "OAuth token is missing in the request."
  ```

2. ```On-Behalf-Of``` ヘッダーがサポートされていない場合<span id="err02">
  ```python
  "Not support On-Behalf-Of but request has it."
  ```

3. リクエストにファイルが含まれていない場合<span id="err03">
  ```python
  "No file part."
  ```

4. ファイルが選択されていない場合<span id="err05">
  ```python
  "No selected file."
  ```

5. ```Content-Length``` が最大アップロードサイズを超える場合<span id="err05">
  ```python
  "Content size is too large. (request:[Content-Lengthの値], maxUploadSize:[最大アップロードサイズ])"
  ```

6. サポートされていない ```Content-Type``` がリクエストに含まれている場合<span id="err06">
  ```python
  "Not accept Content-Type: [サポートされていないContent-Type]"
  ```

7. サポートされていないパッケージング形式がリクエストに含まれている場合<span id="err07">
  ```python
  "Not accept packaging: [サポートされていないパッケージング形式]"
  ```

8. ```Content-Disposition``` ヘッダーからファイル名を取得できない場合<span id="err08">
  ```python
  "Cannot get filename by Content-Disposition."
  ```

9. リクエストボディにファイルが見つからない場合<span id="err09">
  ```python
  "Not found [ファイル名] in request body."
  ```

10. リクエストボディとダイジェストの検証に失敗した場合<span id="err10">
  ```python
  "Failed to verify request body and digest."
  ```

11. インポートアイテムのチェック中にエラーが発生した場合<span id="err11">
  ```python
  "Item check error: [エラーメッセージ]"
  ```

12. アイテムが既に登録されている場合<span id="err12">
  ```python
  "This item is already registered: [アイテムのタイトル]"
  ```

13. アイテムの重複を検知した場合<span id="err13">
  ```python
  "New item appears to be a duplicate: [重複が疑われるアイテムIDのリスト]"
  ```

14. アイテムのシステムへのインポート中にエラーが発生した場合<span id="err14">
  ```python
  "Failed to import item; [エラーメッセージ]"
  ```

15. 管理者による設定で特定のメタデータ形式によるアイテム登録が無効な場合<span id="err15">
  ```python
  "[メタデータ形式] metadata import is not enabled."
  ```

16. SWORDBagIt形式で ```metadata/sword.json``` が存在しない場合<span id="err16">
  ```python
  "SWORDBagIt requires metadate/sword.json."
  ```

17.  RO-Crate+BagIt形式で ```ro-crate-metadata.json``` の位置が誤っている場合<span id="err17">
  ```python
  "ro-crate-metadata.json is required in data/ directory."
  ```

18.   SimpleZip形式で ```metadata/sword.json``` が存在する場合<span id="err18">
  ```python
  "packaging format is SimpleZip, but sword.json is found."
  ```

19.  ```On-Behalf-Of``` ヘッダーでユーザーが見つからない場合<span id="err19">
  ```python
  "No user found by On-Behalf-Of."
  ```

20.  ```On-Behalf-Of``` ヘッダーでユーザー検索中にエラーが発生した場合<span id="err20">
  ```python
  "Failed to get shared ID from On-Behalf-Of."
  ```

21.   クライアントに対する設定がされていない場合<span id="err21">
  ```python
  "No SWORD API setting found for client ID that you are using."
  ```

22.   ワークフローが見つからない、または削除されている場合<span id="err22">
  ```python
  "Workflow is not for item registration."
  ```

23.   マッピング定義設定のアイテムタイプIDとワークフローのアイテムタイプIDが一致しない場合<span id="err23">
  ```python
  "Item type and workflow do not match. ItemType ID must be [マッピング定義設定のアイテムタイプID], but the workflow's ItemType ID was [ワークフローのアイテムタイプID]."
  ```

24.  Bagの検証に失敗した場合<span id="err24">
  ```python
  "Failed to validate import bagit file."
  ```

25. アイテムの更新や削除処理が排他制御によって拒否された場合<span id="err25">
  ```python
  "Item [アイテムID] will be edited by another process."
  ```

26. 更新、削除対象のアイテムが一括インポートによる更新中である場合<span id="err26">
    ```python
    "Item [アイテムID] is in import progress."
    ```

27. アイテムに更新や削除のためのアクティビティが存在する場合<span id="err27">
  ```python
  "Item [アイテムID] is being edited."
  ```

## サーバー設定値

1. サーバーがサポートするSWORDプロトコルのバージョン<span id="conf01">

    ```python
    WEKO_SWORDSERVER_SWORD_VERSION = "http://purl.org/net/sword/3.0"
    ```

2. サービスの説明<span id="conf02">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ABSTRACT = ""
    ```

3. サーバーが受け入れられるコンテンツタイプのリスト<span id="conf03">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ACCEPT = ["*/*"]
    ```

4. サーバーが展開できるアーカイブ形式のリスト<span id="conf04">

    サーバーが異なるフォーマットでパッケージを送信した場合、サーバーはそれをバイナリファイルとして扱うことができる。  
    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ACCEPT_ARCHIVE_FORMAT = ["application/zip"]
    ```

5. ファイルの登録を受け付けるかどうか<span id="conf05">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ACCEPT_DEPOSITS = True
    ```

6. サーバーが受け入れられるメタデータ形式のリスト<span id="conf06">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ACCEPT_METADATA = [
        "https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd",
        "https://w3id.org/ro/crate/1.1/",
    ]
    ```

7. サーバーで受け入れられるパッケージ形式のリスト<span id="conf07">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ACCEPT_PACKAGING = ["*"]
    """
    ["*"] or List of Packaging Formats URI
    - http://purl.org/net/sword/3.0/package/Binary
    - http://purl.org/net/sword/3.0/package/SimpleZip
    - http://purl.org/net/sword/3.0/package/SWORDBagIt
    """
    ```

8. サーバーの収集ポリシーのURLと説明<span id="conf08">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_COLLECTION_POLICY = {}
    """
    example:
    {
        "@id" : "http://www.myorg.ac.uk/collectionpolicy",
        "description" : "...."
    }
    """
    ```

9. デポジット時に期待される処理のURLと説明を示すオブジェクト<span id="conf09">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_TREATMENT = {}
    ```

10. セSegmented File Upload時のステージング先URL<span id="conf10">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_STAGING = ""
    ```

11. Segmented File Upload時のステージングしたファイルを保持する最小時間<span id="conf11">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_STAGING_MAX_IDLE = 3600
    ```

12. 参照によるデポジットをサポートするか<span id="conf12">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_BY_REFERENCE_DEPOSIT = False
    ```

13. 他のユーザーに代わっての代理投稿をサポートするか<span id="conf13">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_ON_BEHALF_OF = True
    ```

14. サーバーが受け入れるダイジェスト形式のリスト<span id="conf14">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_DIGEST = ["SHA-256"]
    ```

15. サポートする認証方式のリスト<span id="conf15">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_AUTHENTICATION = ["OAuth"]
    ```

16. 親サービスに含まれるサービスのリスト<span id="conf16">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_SERVICES = []
    ```

17. アップロードされるファイルの最大サイズ (整数) (バイト単位)<span id="conf17">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_MAX_UPLOAD_SIZE = 16777216000
    ```

18. 参照によってアップロードされたファイルの最大サイズ (バイト単位)<span id="conf18">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_MAX_BY_REFERENCE_SIZE = 30000000000000000
    ```

19. Segmented File Uploadの合計サイズの最大サイズ (整数) (バイト単位)<span id="conf19">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_MAX_ASSEMBLED_SIZE = 30000000000000
    ```

20. Segmented File Uploadがサポートされている場合、サーバーがひとつのアップロードで受け入れるセグメントの最大数<span id="conf20">

    ```python
    WEKO_SWORDSERVER_SERVICEDOCUMENT_MAX_SEGMENTS = 1000
    ```

21. クライアントにダイジェストを送信することを要求するか<span id="conf21">

    ```python
    WEKO_SWORDSERVER_DIGEST_VERIFICATION = True
    ```

22. SWORD APIを使用することができるロール<span id="conf22">

    ```python
    WEKO_SWORDSERVER_DEPOSIT_ROLE_ENABLE = [
        "System Administrator",
        "Repository Administrator"
    ]
    ```

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2022/06/13 | e6db31c99d459605f5bc09f15c4abd07ea573428   | 初版作成                                                 |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562   | ADMIN-2-4へのリンクを追加                                |
| 2025/02/12 | 91e291b7bdb24c0f6cbc65d603f2f9427cd0f031   | JSON-LD形式のメタデータ登録機能を追加                    |
| 2025/03/07 | 6918f05b5dccb52126c36afb5f9b180e847c958f   | アイテムの分割機能について追記                           |
| 2025/06/03 | c145ed4a8052597a2e552a628c92f3fa60b878d4   | 更新・削除機能およびメタデータのみ置換フラグについて記載 |
