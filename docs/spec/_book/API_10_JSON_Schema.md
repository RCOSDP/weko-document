
### JSON Schema

  - 目的・用途

インデックスIDを指定しての検索機能を提供する。

  - 利用方法

| **Method** | **HTTP request**                         | **Description** |
| ---------- | ---------------------------------------- | --------------- |
|            | **GET /items/jsonschema/**{ITEMTYPE\_ID} | アイテムを検索する       |

パスパラメータ

| **GET /items/jsonschema/**{ITEMTYPE\_ID} |     |             |
| ---------------------------------------- | --- | ----------- |
| パラメータ                                    | 値   | 説明          |
| ITEMTYPE\_ID                             | int | インデックスIDを指定 |

レスポンス例：

<table>
<thead>
<tr class="header">
<th><strong>レスポンス例</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/api/index/?q=9</strong></td>
</tr>
<tr class="even">
<td><p>{</p>
<p>"$schema":"http://json-schema.org/draft-04/schema#",</p>
<p>"description":"",</p>
<p>"properties":{</p>
<p>"item_1617186331708":{</p>
<p>"items":{</p>
<p>"properties":{</p>
<p>"subitem_1551255647225":{</p>
<p>"format":"text",</p>
<p>"title":"Title",</p>
<p>"title_i18n":{</p>
<p>"en":"Title",</p>
<p>"ja":"タイトル"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_1551255648112":{</p>
<p>"currentEnum":[</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"Language",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>}</p>
<p>},</p>
<p>"required":[</p>
<p>"subitem_1551255647225",</p>
<p>"subitem_1551255648112"</p>
<p>],</p>
<p>"type":"object"</p>
<p>},</p>
<p>"maxItems":9999,</p>
<p>"minItems":1,</p>
<p>"title":"Title",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"item_1617186419668":{</p>
<p>"items":{</p>
<p>"properties":{</p>
<p>"creatorAffiliations":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"affiliationNameIdentifiers":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"affiliationNameIdentifier":{</p>
<p>"format":"text",</p>
<p>"title":"所属機関識別子",</p>
<p>"title_i18n":{</p>
<p>"en":"Affiliation Name Identifier",</p>
<p>"ja":"所属機関識別子"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"affiliationNameIdentifierScheme":{</p>
<p>"currentEnum":[</p>
<p>"kakenhi",</p>
<p>"ISNI",</p>
<p>"Ringgold",</p>
<p>"GRID"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"kakenhi",</p>
<p>"ISNI",</p>
<p>"Ringgold",</p>
<p>"GRID"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"所属機関識別子スキーマ",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"affiliationNameIdentifierURI":{</p>
<p>"format":"text",</p>
<p>"title":"所属機関識別子URI",</p>
<p>"title_i18n":{</p>
<p>"en":"Affiliation Name Identifier URI",</p>
<p>"ja":"所属機関識別子URI"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"所属機関識別子",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"affiliationNames":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"affiliationName":{</p>
<p>"format":"text",</p>
<p>"title":"所属機関名",</p>
<p>"title_i18n":{</p>
<p>"en":"Affiliation Name",</p>
<p>"ja":"所属機関名"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"affiliationNameLang":{</p>
<p>"currentEnum":[</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"言語",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"所属機関名",</p>
<p>"type":"array"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者所属",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"creatorAlternatives":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"creatorAlternative":{</p>
<p>"format":"text",</p>
<p>"title":"別名",</p>
<p>"title_i18n":{</p>
<p>"en":"Alternative Name",</p>
<p>"ja":"別名"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"creatorAlternativeLang":{</p>
<p>"currentEnum":[</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"言語",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者別名",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"creatorMails":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"creatorMail":{</p>
<p>"format":"text",</p>
<p>"title":"メールアドレス",</p>
<p>"title_i18n":{</p>
<p>"en":"Email Address",</p>
<p>"ja":"メールアドレス"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者メールアドレス",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"creatorNames":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"creatorName":{</p>
<p>"format":"text",</p>
<p>"title":"姓名",</p>
<p>"title_i18n":{</p>
<p>"en":"Name",</p>
<p>"ja":"姓名"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"creatorNameLang":{</p>
<p>"currentEnum":[</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"言語",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者姓名",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"familyNames":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"familyName":{</p>
<p>"format":"text",</p>
<p>"title":"姓",</p>
<p>"title_i18n":{</p>
<p>"en":"Family Name",</p>
<p>"ja":"姓"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"familyNameLang":{</p>
<p>"currentEnum":[</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"言語",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者姓",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"givenNames":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"givenName":{</p>
<p>"format":"text",</p>
<p>"title":"名",</p>
<p>"title_i18n":{</p>
<p>"en":"Given Name",</p>
<p>"ja":"名"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"givenNameLang":{</p>
<p>"currentEnum":[</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"ja",</p>
<p>"ja-Kana",</p>
<p>"ja-Latn",</p>
<p>"en",</p>
<p>"fr",</p>
<p>"it",</p>
<p>"de",</p>
<p>"es",</p>
<p>"zh-cn",</p>
<p>"zh-tw",</p>
<p>"ru",</p>
<p>"la",</p>
<p>"ms",</p>
<p>"eo",</p>
<p>"ar",</p>
<p>"el",</p>
<p>"ko"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"言語",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者名",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"iscreator":{</p>
<p>"format":"text",</p>
<p>"title":"iscreator",</p>
<p>"title_i18n":{</p>
<p>"en":"",</p>
<p>"ja":""</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"nameIdentifiers":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"nameIdentifier":{</p>
<p>"format":"text",</p>
<p>"title":"作成者識別子",</p>
<p>"title_i18n":{</p>
<p>"en":"Creator Identifier",</p>
<p>"ja":"作成者識別子"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"nameIdentifierScheme":{</p>
<p>"currentEnum":[</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"作成者識別子Scheme",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"nameIdentifierURI":{</p>
<p>"format":"text",</p>
<p>"title":"作成者識別子URI",</p>
<p>"title_i18n":{</p>
<p>"en":"Creator Identifier URI",</p>
<p>"ja":"作成者識別子URI"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"作成者識別子",</p>
<p>"type":"array"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"maxItems":9999,</p>
<p>"minItems":1,</p>
<p>"title":"Creator",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"item_1617258105262":{</p>
<p>"properties":{</p>
<p>"resourcetype":{</p>
<p>"currentEnum":[</p>
<p>"conference paper",</p>
<p>"data paper",</p>
<p>"departmental bulletin paper",</p>
<p>"editorial",</p>
<p>"journal article",</p>
<p>"newspaper",</p>
<p>"periodical",</p>
<p>"review article",</p>
<p>"software paper",</p>
<p>"article",</p>
<p>"book",</p>
<p>"book part",</p>
<p>"cartographic material",</p>
<p>"map",</p>
<p>"conference object",</p>
<p>"conference proceedings",</p>
<p>"conference poster",</p>
<p>"aggregated data",</p>
<p>"clinical trial data",</p>
<p>"compiled data",</p>
<p>"encoded data",</p>
<p>"experimental data",</p>
<p>"genomic data",</p>
<p>"geospatial data",</p>
<p>"laboratory notebook",</p>
<p>"measurement and test data",</p>
<p>"observational data",</p>
<p>"recorded data",</p>
<p>"simulation data",</p>
<p>"survey data",</p>
<p>"dataset",</p>
<p>"interview",</p>
<p>"image",</p>
<p>"still image",</p>
<p>"moving image",</p>
<p>"video",</p>
<p>"lecture",</p>
<p>"patent",</p>
<p>"internal report",</p>
<p>"report",</p>
<p>"research report",</p>
<p>"technical report",</p>
<p>"policy report",</p>
<p>"report part",</p>
<p>"working paper",</p>
<p>"data management plan",</p>
<p>"sound",</p>
<p>"thesis",</p>
<p>"bachelor thesis",</p>
<p>"master thesis",</p>
<p>"doctoral thesis",</p>
<p>"interactive resource",</p>
<p>"learning object",</p>
<p>"manuscript",</p>
<p>"musical notation",</p>
<p>"research proposal",</p>
<p>"software",</p>
<p>"technical documentation",</p>
<p>"workflow",</p>
<p>"other"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"conference paper",</p>
<p>"data paper",</p>
<p>"departmental bulletin paper",</p>
<p>"editorial",</p>
<p>"journal article",</p>
<p>"newspaper",</p>
<p>"periodical",</p>
<p>"review article",</p>
<p>"software paper",</p>
<p>"article",</p>
<p>"book",</p>
<p>"book part",</p>
<p>"cartographic material",</p>
<p>"map",</p>
<p>"conference object",</p>
<p>"conference proceedings",</p>
<p>"conference poster",</p>
<p>"aggregated data",</p>
<p>"clinical trial data",</p>
<p>"compiled data",</p>
<p>"encoded data",</p>
<p>"experimental data",</p>
<p>"genomic data",</p>
<p>"geospatial data",</p>
<p>"laboratory notebook",</p>
<p>"measurement and test data",</p>
<p>"observational data",</p>
<p>"recorded data",</p>
<p>"simulation data",</p>
<p>"survey data",</p>
<p>"dataset",</p>
<p>"interview",</p>
<p>"image",</p>
<p>"still image",</p>
<p>"moving image",</p>
<p>"video",</p>
<p>"lecture",</p>
<p>"patent",</p>
<p>"internal report",</p>
<p>"report",</p>
<p>"research report",</p>
<p>"technical report",</p>
<p>"policy report",</p>
<p>"report part",</p>
<p>"working paper",</p>
<p>"data management plan",</p>
<p>"sound",</p>
<p>"thesis",</p>
<p>"bachelor thesis",</p>
<p>"master thesis",</p>
<p>"doctoral thesis",</p>
<p>"interactive resource",</p>
<p>"learning object",</p>
<p>"manuscript",</p>
<p>"musical notation",</p>
<p>"research proposal",</p>
<p>"software",</p>
<p>"technical documentation",</p>
<p>"workflow",</p>
<p>"other"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"資源タイプ",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"resourceuri":{</p>
<p>"format":"text",</p>
<p>"title":"資源タイプ識別子",</p>
<p>"title_i18n":{</p>
<p>"en":"Resource Type Identifier",</p>
<p>"ja":"資源タイプ識別子"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"required":[</p>
<p>"resourcetype",</p>
<p>"resourceuri"</p>
<p>],</p>
<p>"title":"Resource Type",</p>
<p>"type":"object"</p>
<p>},</p>
<p>"item_1617605131499":{</p>
<p>"items":{</p>
<p>"properties":{</p>
<p>"accessrole":{</p>
<p>"enum":[</p>
<p>"open_access",</p>
<p>"open_date",</p>
<p>"open_login",</p>
<p>"open_no"</p>
<p>],</p>
<p>"format":"radios",</p>
<p>"title":"アクセス",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"date":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"dateType":{</p>
<p>"currentEnum":[</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"日付タイプ",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"dateValue":{</p>
<p>"format":"datetime",</p>
<p>"title":"日付",</p>
<p>"title_i18n":{</p>
<p>"en":"",</p>
<p>"ja":""</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"オープンアクセスの日付",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"displaytype":{</p>
<p>"currentEnum":[</p>
<p>"detail",</p>
<p>"simple",</p>
<p>"preview"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"detail",</p>
<p>"simple",</p>
<p>"preview"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"表示形式",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"fileDate":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"fileDateType":{</p>
<p>"currentEnum":[</p>
<p>"Accepted",</p>
<p>"Collected",</p>
<p>"Copyrighted",</p>
<p>"Created",</p>
<p>"Issued",</p>
<p>"Submitted",</p>
<p>"Updated",</p>
<p>"Valid"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"Accepted",</p>
<p>"Collected",</p>
<p>"Copyrighted",</p>
<p>"Created",</p>
<p>"Issued",</p>
<p>"Submitted",</p>
<p>"Updated",</p>
<p>"Valid"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"日付タイプ",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"fileDateValue":{</p>
<p>"format":"datetime",</p>
<p>"title":"日付",</p>
<p>"title_i18n":{</p>
<p>"en":"Date",</p>
<p>"ja":"日付"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"日付",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"filename":{</p>
<p>"format":"text",</p>
<p>"title":"表示名",</p>
<p>"title_i18n":{</p>
<p>"en":"FileName",</p>
<p>"ja":"表示名"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"filesize":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"value":{</p>
<p>"format":"text",</p>
<p>"title":"サイズ",</p>
<p>"title_i18n":{</p>
<p>"en":"Size",</p>
<p>"ja":"サイズ"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"サイズ",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"format":{</p>
<p>"format":"text",</p>
<p>"title":"フォーマット",</p>
<p>"title_i18n":{</p>
<p>"en":"Format",</p>
<p>"ja":"フォーマット"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"groups":{</p>
<p>"currentEnum":[</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"グループ",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"licensefree":{</p>
<p>"format":"textarea",</p>
<p>"title":"自由ライセンス",</p>
<p>"title_i18n":{</p>
<p>"en":"自由ライセンス",</p>
<p>"ja":"自由ライセンス"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"licensetype":{</p>
<p>"currentEnum":[</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"ライセンス",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"url":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"label":{</p>
<p>"format":"text",</p>
<p>"title":"ラベル",</p>
<p>"title_i18n":{</p>
<p>"en":"Label",</p>
<p>"ja":"ラベル"</p>
<p>},</p>
<p>"type":"string"</p>
<p>},</p>
<p>"objectType":{</p>
<p>"currentEnum":[</p>
<p>"abstract",</p>
<p>"summary",</p>
<p>"fulltext",</p>
<p>"thumbnail",</p>
<p>"other"</p>
<p>],</p>
<p>"enum":[</p>
<p>null,</p>
<p>"abstract",</p>
<p>"summary",</p>
<p>"fulltext",</p>
<p>"thumbnail",</p>
<p>"other"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"オブジェクトタイプ",</p>
<p>"type":[</p>
<p>"null",</p>
<p>"string"</p>
<p>]</p>
<p>},</p>
<p>"url":{</p>
<p>"format":"text",</p>
<p>"title":"本文URL",</p>
<p>"title_i18n":{</p>
<p>"en":"Text URL",</p>
<p>"ja":"本文URL"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"title":"本文URL",</p>
<p>"type":"object"</p>
<p>},</p>
<p>"version":{</p>
<p>"format":"text",</p>
<p>"title":"バージョン情報",</p>
<p>"title_i18n":{</p>
<p>"en":"Version Information",</p>
<p>"ja":"バージョン情報"</p>
<p>},</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"maxItems":9999,</p>
<p>"minItems":1,</p>
<p>"title":"File",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"pubdate":{</p>
<p>"format":"datetime",</p>
<p>"title":"PubDate",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"system_file":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"subitem_systemfile_datetime":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"subitem_systemfile_datetime_date":{</p>
<p>"format":"datetime",</p>
<p>"title":"SYSTEMFILE DateTime Date",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemfile_datetime_type":{</p>
<p>"enum":[</p>
<p>"Accepted",</p>
<p>"Available",</p>
<p>"Collected",</p>
<p>"Copyrighted",</p>
<p>"Created",</p>
<p>"Issued",</p>
<p>"Submitted",</p>
<p>"Updated",</p>
<p>"Valid"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"SYSTEMFILE DateTime Type",</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"SYSTEMFILE DateTime",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"subitem_systemfile_filename":{</p>
<p>"format":"array",</p>
<p>"items":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"subitem_systemfile_filename_label":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMFILE Filename Label",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemfile_filename_type":{</p>
<p>"enum":[</p>
<p>"Abstract",</p>
<p>"Fulltext",</p>
<p>"Summary",</p>
<p>"Thumbnail",</p>
<p>"Other"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"SYSTEMFILE Filename Type",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemfile_filename_uri":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMFILE Filename URI",</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"type":"object"</p>
<p>},</p>
<p>"title":"SYSTEMFILE Filename",</p>
<p>"type":"array"</p>
<p>},</p>
<p>"subitem_systemfile_mimetype":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMFILE MimeType",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemfile_size":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMFILE Size",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemfile_version":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMFILE Version",</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"system_prop":true,</p>
<p>"title":"File Information",</p>
<p>"type":"object"</p>
<p>},</p>
<p>"system_identifier_doi":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"subitem_systemidt_identifier":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMIDT Identifier",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemidt_identifier_type":{</p>
<p>"enum":[</p>
<p>"DOI",</p>
<p>"HDL",</p>
<p>"URI"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"SYSTEMIDT Identifier Type",</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"system_prop":true,</p>
<p>"title":"Persistent Identifier(DOI)",</p>
<p>"type":"object"</p>
<p>},</p>
<p>"system_identifier_hdl":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"subitem_systemidt_identifier":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMIDT Identifier",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemidt_identifier_type":{</p>
<p>"enum":[</p>
<p>"DOI",</p>
<p>"HDL",</p>
<p>"URI"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"SYSTEMIDT Identifier Type",</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"system_prop":true,</p>
<p>"title":"Persistent Identifier(HDL)",</p>
<p>"type":"object"</p>
<p>},</p>
<p>"system_identifier_uri":{</p>
<p>"format":"object",</p>
<p>"properties":{</p>
<p>"subitem_systemidt_identifier":{</p>
<p>"format":"text",</p>
<p>"title":"SYSTEMIDT Identifier",</p>
<p>"type":"string"</p>
<p>},</p>
<p>"subitem_systemidt_identifier_type":{</p>
<p>"enum":[</p>
<p>"DOI",</p>
<p>"HDL",</p>
<p>"URI"</p>
<p>],</p>
<p>"format":"select",</p>
<p>"title":"SYSTEMIDT Identifier Type",</p>
<p>"type":"string"</p>
<p>}</p>
<p>},</p>
<p>"system_prop":true,</p>
<p>"title":"Persistent Identifier(URI)",</p>
<p>"type":"object"</p>
<p>}</p>
<p>},</p>
<p>"required":[</p>
<p>"pubdate",</p>
<p>"item_1617186331708",</p>
<p>"item_1617258105262"</p>
<p>],</p>
<p>"type":"object"</p>
<p>}</p></td>
</tr>
</tbody>
</table>

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - 機能内容

  - 関連モジュール

  - 処理概要

  - 更新履歴

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
<p>2023/11/14</p>
</blockquote></td>
<td>V0.9.27</td>
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
