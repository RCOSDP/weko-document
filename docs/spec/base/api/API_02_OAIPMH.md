# OAI-PMH 2.0

## 目的・用途

OAI-PMH(Open Archives Initiative Protocol for Metadata Harvesting)2.0とは、メタデータ交換のための通信プロトコルである。

プロトコルの仕様（日本語訳）：
[https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/](https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/)


WEKO3はメタデータをリポジトリから取り込むハーベスタ機能とリポジトリからハーベスタに対してメタデータを提供するプロバイダ機能の両方に対応する。

WEKO3のOAIPMHプロバイダのベースURLは以下となる。

https://[host]/oai


OAIPMHプロバイダ機能を有効にするには[Identify設定](#Identify設定)が必要。

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
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"\>

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
</OAI-PMH\>
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

\<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"\>

\<responseDate\>yyyy-mm-ddThh:mm:ssZ\</responseDate\>

\<request verb="Identify"\>https://\[host\] /oai\</request\>

\<Identify\>

\<repositoryName\>○○○○\</repositoryName\>

\<adminEmail\>○○○○\</adminEmail\>

\<baseURL\>https://\[host\] /oai\</baseURL\>

\<protocolVersion\>2.0\</protocolVersion\>

\<earliestDatestamp\> yyyy-mm-ddThh:mm:ssZ \</earliestDatestamp\>

\<deletedRecord\>transient\</deletedRecord\>

\<granularity\>YYYY-MM-DDThh:mm:ssZ\</granularity\>

\</Identify\>

\</OAI-PMH\>

  - ListIdentifiers  
    任意の引数を指定し、ヘッダの検索する際に使用するverb。  
    追加で指定可能な引数は次の5つとなる。  
    １．from：UTCdatetimeの任意の引数。日付による選択的ハーベスティングの下限を設定する。  
    ２．until：UTCdatetimeの任意の引数。日付による選択的ハーベスティングの上限を設定する。  
    ３．metadataPrefix：返却レコードのメタデータ部に含まれるフォーマットを指定する引数。必須項目。  
    ４．set：Spec値を持つ任意の引数。選択的ハーベスティングを行う際のセットの基準を指定する。  
    ５. resumptionToken：リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。
    
      - 以下に応答例を示す。

\<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"\>

\<responseDate\>YYYY-MM-DDThh:mm:ssZ\</responseDate\>

\<request verb="ListIdentifiers" metadataPrefix="○○○○"\>https://\[host\]/oai\</request\>

\<ListIdentifiers\>

\<header\>

\<指定したヘッダの情報\>

\</header\>

\</ListIdentifiers\>

\</OAI-PMH\>

  - ListMetadataFormats  
    リポジトリから入手可能なメタデータフォーマットを検索する際に使用するverb。  
    指定可能な引数を以下に示す。  
    identifier：アイテムに利用可能なメタデータフォーマットが要求されている場合に、そのアイテムの固有識別子を指定する任意の引数。
    
      - 以下に応答例を示す。

\<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"\>

\<responseDate\>YYYY-MM-DDThh:mm:ssZ\</responseDate\>

\<ListMetadataFormats\>

\<metadataFormat\>

\<metadataPrefix\>jpcoar\</metadataPrefix\>

\<schema\>https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar\_scm.xsd\</schema\>

\<metadataNamespace\>https://github.com/JPCOAR/schema/blob/master/2.0/\</metadataNamespace\>

\</metadataFormat\>

\<metadataFormat\>

\<metadataPrefix\>jpcoar\_1.0\</metadataPrefix\>

\<schema\>https://irdb.nii.ac.jp/schema/jpcoar/1.0/jpcoar\_scm.xsd\</schema\>

\<metadataNamespace\>https://irdb.nii.ac.jp/schema/jpcoar/1.0/\</metadataNamespace\>

\</metadataFormat\>

\<metadataFormat\>

\<metadataPrefix\>jpcoar\_2.0\</metadataPrefix\>

\<schema\>https://irdb.nii.ac.jp/schema/jpcoar/2.0/jpcoar\_scm.xsd\</schema\>

\<metadataNamespace\>https://irdb.nii.ac.jp/schema/jpcoar/2.0/\</metadataNamespace\>

\</metadataFormat\>

\<metadataFormat\>

\<metadataPrefix\>oai\_dc\</metadataPrefix\>

\<schema\>http://www.openarchives.org/OAI/2.0/oai\_dc/ http://www.openarchives.org/OAI/2.0/oai\_dc.xsd\</schema\>

\<metadataNamespace\>http://www.w3.org/2001/XMLSchema\</metadataNamespace\>

\</metadataFormat\>

\<metadataFormat\>

\<metadataPrefix\>ddi\</metadataPrefix\>

\<schema\>https://ddialliance.org/Specification/DDI-Codebook/2.5/XMLSchema/codebook.xsd\</schema\>

\<metadataNamespace\>ddi:codebook:2\_5\</metadataNamespace\>

\</metadataFormat\>

\<metadataFormat\>

\<metadataPrefix\>jpcoar\_v1\</metadataPrefix\>

\<schema\>https://github.com/JPCOAR/schema/blob/master/1.0/jpcoar\_scm.xsd\</schema\>

\<metadataNamespace\>https://github.com//schema/blob/master/1.0/\</metadataNamespace\>

\</metadataFormat\>

\<metadataFormat\>

\<metadataPrefix\>lom\</metadataPrefix\>

\<schema\>http://www.lido-schema.org http://www.lido-schema.org/schema/v1.0/lido-v1.0.xsd\</schema\>

\<metadataNamespace\>http://ltsc.ieee.org/xsd/LOM\</metadataNamespace\>

\</metadataFormat\>

\</ListMetadataFormats\>

\</OAI-PMH\>

  - ListRecord  
    リポジトリからレコードを収集する際に使用するverb。  
    追加で指定可能な引数は次の5つとなる。  
    １．from：UTCdatetimeの任意の引数。日付による選択的ハーベスティングの下限を設定する。  
    ２．until：UTCdatetimeの任意の引数。日付による選択的ハーベスティングの上限を設定する。  
    ３．metadataPrefix：返却レコードのメタデータ部に含まれるフォーマットを指定する引数。必須項目。  
    ４．set：Spec値を持つ任意の引数。選択的ハーベスティングを行う際のセットの基準を指定する。  
    ５. resumptionToken：リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。
    
      - 以下に応答例を示す。

> \<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"\>
> 
> \<responseDate\>YYYY-MM-DDThh:mm:ssZ\</responseDate\>
> 
> \<request verb="ListRecords" metadataPrefix="○○○○"\>https://\[host\]/oai\</request\>
> 
> \<ListRecords\>
> 
> \<record\>
> 
> \<header\>
> 
> \<指定したレコードの情報\>
> 
> \</header\>
> 
> \</record\>
> 
> \</ListRecords\>
> 
> \</OAI-PMH\>

  - ListSets  
    リポジトリのセット構成を検索する際に使用するverb。  
    使用可能となる引数は次のものである。  
    resumptionToken：リポジトリが応答する際に不完全リストとセットになっている要素。この要素を指定して検索を行うことで完全リストの検索を可能とする任意の引数。
    
      - 以下に応答例を示す。

> \<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"\>
> 
> \<responseDate\>YYYY-MM-DDThh:mm:ssZ\</responseDate\>
> 
> \<request verb="ListSets"\>https://\[host\]/oai\</request\>
> 
> \<ListSets\>
> 
> \<set\>
> 
> \<セット構成の情報\>
> 
> \</ListSets\>
> 
> \</OAI-PMH\>
> 
> \</OAI-PMH\>\</OAI-PMH\>

  - > リクエストに不備がある場合は以下のエラーのいずれかがOAI-PMH出力の本文内に記載される。
    
      - > badArgument：不正な引数があるか、必須となる引数がない場合。
    
      - > cannotDisseminateFormat：metadataPrefixの値がidentifierにより指定されたアイテムでサポートされていない場合。
    
      - > idDoesNotExist：リポジトリでidentiferの値が不明であるか、不正なものである場合。
    
      - > badResumptionToken：resumptionTokenの値が無効であるか期限切れである場合。
    
      - > noRecordsMatch：from、until、setの値を組み合わせると空のリストになる場合。
    
      - > noSetHierarchy：リポジトリがセットをサポートしていない場合。
    
      - > noMetadataFormats：指定したアイテムで利用可能なメタデータフォーマットではない場合。

<!-- end list -->

## 関連モジュール

* Invenio_oaiserver

##  更新履歴

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
</tbody>
</table>