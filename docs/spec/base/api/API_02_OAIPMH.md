# OAI-PMH 2.0

## 目的・用途

OAI-PMH(Open Archives Initiative Protocol for Metadata Harvesting)2.0とは、メタデータ交換のための通信プロトコルである。

プロトコルの仕様（日本語訳）：
[https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/](https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/)


WEKO3はメタデータをリポジトリから取り込むハーベスタ機能とリポジトリからハーベスタに対してメタデータを提供するプロバイダ機能の両方に対応する。

WEKO3のOAIPMHプロバイダのベースURLは以下となる。

https://[host]/oai


OAIPMHプロバイダ機能を有効にするには[Identify設定](../admin/ADMIN_9_2.md)が必要である。

メタデータを出力するにはインデックスの [ハーベスト公開](../admin/ADMIN_3_1.md)が有効になっている必要がある。

## 機能内容

* Verbに指定できる値は、以下の6種類となる。    

### GetRecord  
        
この verb は、あるリポジトリから個別のメタデータレコードを検索するために使用される。

メタデータはアイテムタイプマッピングを利用してrecords_metadataのレコードを元に作成される。

datestampにはrecords_metadataテーブルのupdatedカラム値が利用される。
        
#### 引数  
        
- identifier：レコードの抽出元となるリポジトリのアイテムの固有識別子を指定する引数。必須項目。  
- metadataPrefix：返却レコードのメタデータ部に含まれるフォーマットを指定する引数。必須項目。

#### エラー

- badArgument - 要求に不正な引数があるか、必要な引数がありません。
- cannotDisseminateFormat - metadataPrefix 引数の値が、identifier 引数の値によって指定されたアイテムでサポートされていません。
- idDoesNotExist - このリポジトリでは、 identifier 引数の値が不明または不正です。
        
#### 例

https://[host]/oai?verb=GetRecord&metadataPrefix=jpcoar_2.0&identifier=https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&metadataPrefix=jpcoar_2.0&identifier=oai:weko3.example.org:00000001

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">

<responseDate>yyyy-mm-ddThh:mm:ssZ</responseDate>
<request metadataPrefix="jpcoar_2.0" verb="GetRecord" identifier="oai:weko3.example.org:00000001">https://[host]/oai</request>
<GetRecord>
<record>
<header>
<identifier>oai:weko3.example.org:00000001</identifier>
<datestamp>yyyy-mm-ddThh:mm:ssZ</datestamp>
<setSpec>○○○○</setSpec>
</header>
<metadata>
指定したアイテムのメタデータがここに記載される
</metadata>
</record>
</GetRecord>
</OAI-PMH>
```

idDoesNotExist　の例。

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>2024-09-10T15:31:52Z</responseDate>
<request>https://dev.ir.rcos.nii.ac.jp/oai</request>
<error code="idDoesNotExist">No matching identifier</error>
</OAI-PMH>
```

cannotDisseminateFormat　の例。


```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>2024-09-10T15:31:20Z</responseDate>
<request>https://dev.ir.rcos.nii.ac.jp/oai</request>
<error code="cannotDisseminateFormat">The metadataPrefix "oai_marc" is not supported by this repository.</error>
</OAI-PMH>
```

badArgument　の例。

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>yyyy-mm-ddThh:mm:ssZ</responseDate>
<request>https://[host]/oai</request>
<error code="badArgument">Missing data for required field "metadataPrefix".</error>
<error code="badArgument">Missing data for required field "identifier".</error>
</OAI-PMH>
```

### Identify  
    
リポジトリについての情報を検索する際に使用するverb。  
    
#### 引数

なし
    
#### 例

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>yyyy-mm-ddThh:mm:ssZ</responseDate>
<request verb="Identify">https://[host] /oai</request>
<Identify>
<repositoryName>○○○○</repositoryName>
<adminEmail>○○○○</adminEmail>
<baseURL>https://[host]/oai</baseURL>
<protocolVersion>2.0</protocolVersion>
<earliestDatestamp> yyyy-mm-ddThh:mm:ssZ </earliestDatestamp>
<deletedRecord>transient</deletedRecord>
<granularity>YYYY-MM-DDThh:mm:ssZ</granularity>
</Identify>
</OAI-PMH>
```

### ListIdentifiers

任意の引数を指定し、ヘッダの検索する際に使用するverb。  
    
    
#### 引数

- from：UTCdatetimeの任意の引数。日付による選択的ハーベスティングの下限を設定する。  
- until：UTCdatetimeの任意の引数。日付による選択的ハーベスティングの上限を設定する。  
- metadataPrefix：返却レコードのメタデータ部に含まれるフォーマットを指定する引数。必須項目。  
- set：Spec値を持つ任意の引数。選択的ハーベスティングを行う際のセットの基準を指定する。  
- resumptionToken：リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。
    
#### 例

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>YYYY-MM-DDThh:mm:ssZ</responseDate>
<request verb="ListIdentifiers" metadataPrefix="○○○○">https://[host]/oai</request>
<ListIdentifiers>
<header>
<指定したヘッダの情報>
</header>
</ListIdentifiers>
</OAI-PMH>
```

### ListMetadataFormats  
    
リポジトリから入手可能なメタデータフォーマットを検索する際に使用するverb。  
    
#### 引数
    
identifier：アイテムに利用可能なメタデータフォーマットが要求されている場合に、そのアイテムの固有識別子を指定する任意の引数。

#### 例    

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>YYYY-MM-DDThh:mm:ssZ</responseDate>
<ListMetadataFormats>
<metadataFormat>
<metadataPrefix>jpcoar</metadataPrefix>
<schema>https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd</schema>
<metadataNamespace>https://github.com/JPCOAR/schema/blob/master/2.0/</metadataNamespace>
</metadataFormat>
<metadataFormat>
<metadataPrefix>jpcoar_1.0</metadataPrefix>
<schema>https://irdb.nii.ac.jp/schema/jpcoar/1.0/jpcoar_scm.xsd</schema>
<metadataNamespace>https://irdb.nii.ac.jp/schema/jpcoar/1.0/</metadataNamespace>
</metadataFormat>
<metadataFormat>
<metadataPrefix>jpcoar_2.0</metadataPrefix>
<schema>https://irdb.nii.ac.jp/schema/jpcoar/2.0/jpcoar_scm.xsd</schema>
<metadataNamespace>https://irdb.nii.ac.jp/schema/jpcoar/2.0/</metadataNamespace>
</metadataFormat>
<metadataFormat>
<metadataPrefix>oai_dc</metadataPrefix>
<schema>http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd</schema>
<metadataNamespace>http://www.w3.org/2001/XMLSchema</metadataNamespace>
</metadataFormat>
<metadataFormat>
<metadataPrefix>ddi</metadataPrefix>
<schema>https://ddialliance.org/Specification/DDI-Codebook/2.5/XMLSchema/codebook.xsd</schema>
<metadataNamespace>ddi:codebook:2_5</metadataNamespace>
</metadataFormat>
<metadataFormat>
<metadataPrefix>jpcoar_v1</metadataPrefix>
<schema>https://github.com/JPCOAR/schema/blob/master/1.0/jpcoar_scm.xsd</schema>
<metadataNamespace>https://github.com//schema/blob/master/1.0/</metadataNamespace>
</metadataFormat>
<metadataFormat>
<metadataPrefix>lom</metadataPrefix>
<schema>http://www.lido-schema.org http://www.lido-schema.org/schema/v1.0/lido-v1.0.xsd</schema>
<metadataNamespace>http://ltsc.ieee.org/xsd/LOM</metadataNamespace>
</metadataFormat>
</ListMetadataFormats>
</OAI-PMH><?xml version='1.0' encoding='UTF-8'?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2024-09-10T16:03:44Z</responseDate>
  <request verb="ListMetadataFormats">https://dev.ir.rcos.nii.ac.jp/oai</request>
  <ListMetadataFormats>
    <metadataFormat>
      <metadataPrefix>jpcoar_1.0</metadataPrefix>
      <schema>https://irdb.nii.ac.jp/schema/jpcoar/1.0/jpcoar_scm.xsd</schema>
      <metadataNamespace>https://irdb.nii.ac.jp/schema/jpcoar/1.0/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>jpcoar</metadataPrefix>
      <schema>https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd</schema>
      <metadataNamespace>https://github.com/JPCOAR/schema/blob/master/2.0/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>jpcoar_2.0</metadataPrefix>
      <schema>https://irdb.nii.ac.jp/schema/jpcoar/2.0/jpcoar_scm.xsd</schema>
      <metadataNamespace>https://irdb.nii.ac.jp/schema/jpcoar/2.0/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>oai_dc</metadataPrefix>
      <schema>http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd</schema>
      <metadataNamespace>http://www.w3.org/2001/XMLSchema</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>ddi</metadataPrefix>
      <schema>https://ddialliance.org/Specification/DDI-Codebook/2.5/XMLSchema/codebook.xsd</schema>
      <metadataNamespace>ddi:codebook:2_5</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>jpcoar_v1</metadataPrefix>
      <schema>https://github.com/JPCOAR/schema/blob/master/1.0/jpcoar_scm.xsd</schema>
      <metadataNamespace>https://github.com/JPCOAR/schema/blob/master/1.0/</metadataNamespace>
    </metadataFormat>
    <metadataFormat>
      <metadataPrefix>lom</metadataPrefix>
      <schema>http://www.lido-schema.org http://www.lido-schema.org/schema/v1.0/lido-v1.0.xsd</schema>
      <metadataNamespace>http://ltsc.ieee.org/xsd/LOM</metadataNamespace>
    </metadataFormat>
  </ListMetadataFormats>
</OAI-PMH>
```

### ListRecord  

リポジトリからレコードを収集する際に使用するverb。  

各レコードのメタデータはアイテムタイプマッピングを利用してrecords_metadataのレコードを元に作成される。
各レコードのdatestampにはrecords_metadataテーブルのupdatedカラム値が利用される。

#### 引数

| 引数 | 概要 |
| ---- | ---- |
| from|UTCdatetimeの任意の引数。日付による選択的ハーベスティングの下限を設定する。|
| until| UTCdatetimeの任意の引数。日付による選択的ハーベスティングの上限を設定する。  |
| metadataPrefix | 返却レコードのメタデータ部に含まれるフォーマットを指定する引数。必須項目。|  
| set | Spec値を持つ任意の引数。選択的ハーベスティングを行う際のセットの基準を指定する。  |
| resumptionToken | リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。|

以下に応答例を示す。

```
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>YYYY-MM-DDThh:mm:ssZ</responseDate> 
<request verb="ListRecords" metadataPrefix="○○○○">https://[host]/oai</request>
<ListRecords>
<record>
<header>
指定したレコードの情報
</header>
</record> 
</ListRecords>
</OAI-PMH>
```

#### 処理概要

1. パラメータを基にElasticsearchで絞り込みを実施
2. 絞り込み結果をもとにPostgreSQLから応答XMLを作成


### ListSets

リポジトリのセット構成を検索する際に使用するverb。

使用可能となる引数は次のものである。

resumptionToken：リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。

#### 例

```
<?xml version='1.0' encoding='UTF-8'?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2024-09-10T16:05:37Z</responseDate>
  <request verb="ListRecords" metadataPrefix="jpcoar_2.0">https://dev.ir.rcos.nii.ac.jp/oai</request>
  <ListRecords>
    <record>
      <header>
        <identifier>oai:weko3.example.org:00000001</identifier>
        <datestamp>2024-09-01T12:52:55Z</datestamp>
        <setSpec>○○○○</setSpec>
      </header>
      <metadata>
      <メタデータ>
      </metadata>
    </record>
    <record>
      <header>
        <identifier>oai:weko3.example.org:02000001</identifier>
        <datestamp>2024-09-01T12:52:55Z</datestamp>
        <setSpec>1623632832836</setSpec>
      </header>
      <metadata>
      <メタデータ>
      </metadata>
    </record>
    ....
  </ListRecords>
</OAI-PMH>

```

### ListSets  

リポジトリのセット構成を検索する際に使用するverb。  

#### 引数
    
- resumptionToken：リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。
    
#### 例

```
<?xml version='1.0' encoding='UTF-8'?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2024-09-10T16:09:43Z</responseDate>
  <request verb="ListSets">https://[host]/oai</request>
  <ListSets>
    <set>
     <セット内容>
    </set>
  </ListSets>
</OAI-PMH>
```


- リクエストに不備がある場合は以下のエラーのいずれかがOAI-PMH出力の本文内に記載される。
  - badArgument：不正な引数があるか、必須となる引数がない場合。
  - cannotDisseminateFormat：metadataPrefixの値がidentifierにより指定されたアイテムでサポートされていない場合。
  - idDoesNotExist：リポジトリでidentifierの値が不明であるか、不正なものである場合。
  - badResumptionToken：resumptionTokenの値が無効であるか期限切れである場合。
  - noRecordsMatch：from、until、setの値を組み合わせると空のリストになる場合。
  - noSetHierarchy：リポジトリがセットをサポートしていない場合。
  - noMetadataFormats：指定したアイテムで利用可能なメタデータフォーマットではない場合。

## 関連モジュール

* invenio-oaiserver（エンドポイント `/oai`（GET/POST）、`views.server.response` によるverbディスパッチ、`response.py` の各verb処理、`verbs.py` の引数検証、`query.py` のES検索、`resumption_token.py`）
* weko-schema-ui（metadataPrefix一覧と各フォーマットのシリアライザ `schema.get_oai_metadata_formats` / `dumps_etree`）
* weko-index-tree（set＝インデックスの公開・ハーベスト公開判定 `Indexes`）
* weko-deposit / weko-records（レコード本体取得とアイテムタイプマッピング `WekoRecord.get_record_by_uuid`）

> 実装補足（v2.0.2）：
> - metadataPrefixの一覧は固定ではなく、管理画面で登録されたスキーマ（`WekoSchema` / `OAIServerSchema`）から `get_oai_metadata_formats` が動的生成する。コード上の既定値は `oai_dc` / `marc21` のみで、`jpcoar` / `jpcoar_2.0` / `ddi` / `lom` 等はスキーマ登録に依存する。
> - ListRecords / ListIdentifiers が実際に検索するESインデックスは `INDEXER_DEFAULT_INDEX` である（`OAISERVER_RECORD_INDEX` はこの経路では未使用）。
> - resumptionToken は ES scroll ベースで、ページサイズは `OAISERVER_PAGE_SIZE`（100）。
> - エラーは marshmallow の `ValidationError` 等を HTTP 422 でXML返却する。`noSetHierarchy` はインデックスを常にsetとして扱うため実装上発行されない。
> - 主なconfig：`OAISERVER_PAGE_SIZE` / `OAISERVER_GRANULARITY` / `OAISERVER_PROTOCOL_VERSION` / `OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME` / `OAISERVER_METADATA_FORMATS` / `OAISERVER_CODE_NO_RECORDS_MATCH` / `OAISERVER_MESSAGE_NO_RECORDS_MATCH`、`INDEXER_DEFAULT_INDEX`。

> 実装補足（v2.1.0：エンバーゴ考慮）：
> - `weko_search_ui/config.py` の `WEKO_SEARCH_FIX_ACCESSRIGHTS`（既定 `False`）が `True` の環境では、ListRecords/ListIdentifiers の from/until 絞り込みが `invenio_oaiserver/query.py` の `range_query`（`get_records` から呼び出し）に切り替わり、エンバーゴ解除（公開日到来）アイテムを収集対象に含める。`range_query` はエンバーゴアイテム（accessRights=embargoed access）について `content.accessrole.raw`=open_date とその公開日（`content.date.dateValue.raw`）および `_updated` の双方で期間内外を判定する。
> - 併せて `invenio_records/api.py` の `Record.updated` プロパティが、エンバーゴ解除（open access 化）と判定されたアイテムの更新日時（datestamp）を `max(元のupdated, 最新の公開日)` に繰り上げる。
> - `WEKO_SEARCH_FIX_ACCESSRIGHTS`=False（既定）の場合は素の `_updated` レンジ・素の更新日時による従来動作。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。関連モジュール・エンドポイント・metadataFormatの動的生成・ESインデックス・resumptionToken・configキー・noSetHierarchy未発行を追記 |
| 2026/07/17 |  | v2.1.0差分反映：from/until のエンバーゴ考慮（`range_query`）・datestamp繰り上げ（`Record.updated`）を追記（`WEKO_SEARCH_FIX_ACCESSRIGHTS`、既定False） |
