# OpenSearch

- 目的・用途

アイテムの検索に利用できる。

- 利用方法

以下の形のURLを使用して検索ができる

https://[host]/api/opensearch/search?クエリパラメータ=値&クエリパラメータ値&...

| **Method** | **HTTP request** | **Description** |
| ---- | ---- | ---- |
| weko_search_ui.views.opensearch_description | GET /api/opensearch/description.xml | |
| weko_search_ui.query.opensearch_factory※ | GET /api/opensearch/search | |

※ modules/weko-search-ui/weko_search_ui/config.py のRECORDS_REST_ENDPOINTS["opensearch"]にて設定

クエリパラメータ

**GET /api/opensearch/search**

| パラメータ | 必須 | 値 | 説明 |
| ---- | ---- | ---- | ---- |
| q | | string | 主検索語（searchTerms）。値が指定された場合はインデックスIDとして扱い `item_path_search_factory` に委譲する（description.xml のUrlテンプレートも `q={searchTerms}`） |
| format | | atom / rss / jpcoar | レスポンス結果のフォーマット。デフォルトはjson形式。 |
| size | | int | レスポンスに含めるフィード件数（別名 `list_view_num`、既定10） |
| page | | Int | 表示するページ番号（別名 `page_no`、既定1） |
| 以下は設定ファイルやアイテムタイプマッピングにより定義が変化する（`WEKO_SEARCH_KEYWORDS_DICT`） | | | |
| title | | string | dc:titleにマッピングされた項目の検索 |
| des | | string | datacite:descriptionにマッピングされた項目の検索 |
| type | | string | dc:typeにマッピングされた項目の検索 |
| wid | | Int | 作成者（著者）識別子（`creator.nameIdentifier`）で検索。※「アイテムIDを指定」ではない |
| iid | | Int | インデックスID（`path.tree`）で検索 |
| accessrights | | string（カンマ区切り） | アクセス権（`open access` / `embargoed access` / `restricted access` / `metadata only access`＝`WEKO_ACCESS_RIGHTS_CHOICES`）で絞り込む。`WEKO_SEARCH_FIX_ACCESSRIGHTS`=True の環境ではエンバーゴ状態（ファイルの `accessrole`・公開日・現在日）を考慮して出し分ける（[API-07](./API_07_item_search.md) と共通）。既定（`WEKO_SEARCH_FIX_ACCESSRIGHTS`=False）は素の term/terms 一致による従来動作。 |

レスポンス例：

**レスポンス例：format: atom**

/api/opensearch/search?title=nooai&format=atom&size=1

```xml
<feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
<id>https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;format=atom&amp;size=1</id>
<title>WEKO OpenSearch: </title>
<updated>2023-11-14T23:47:46.452823+00:00</updated>
<link href="https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;format=atom&amp;size=1"/>
<generator uri="http://lkiesow.github.io/python-feedgen" version="0.7.0">python-feedgen</generator>
<opensearch:totalResults>9</opensearch:totalResults>
<opensearch:startIndex>1</opensearch:startIndex>
<opensearch:itemsPerPage>1</opensearch:itemsPerPage>
<entry>
<id>https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;metadataPrefix=jpcoar&amp;identifier=oai:weko3.example.org:00000035</id>
<title>public-item-2-public-nooai-guest-35-ja</title>
<updated>2023-11-06T05:45:01.746520+00:00</updated>
<content xml:lang="ja">概要
概要
概要
概要</content>
<link href="https://dev.ir.rcos.nii.ac.jp/records/35"/>
<link href="https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;metadataPrefix=jpcoar&amp;identifier=oai:weko3.example.org:00000035"/>
<dc:publisher xml:lang="en">Publisher</dc:publisher>
<dc:subject>2-public-nooai-guest-35-ja</dc:subject>
<dc:type>デフォルトアイテムタイプ（フル）</dc:type>
<dc:format>text/plain</dc:format>
<dc:identifier>35</dc:identifier>
<dc:identifier>https://weko3.example.org/record/35/files/1KB.pdf</dc:identifier>
<prism:aggregationType>conference paper</prism:aggregationType>
<prism:issn>xxxx-xxxx-xxxx</prism:issn>
<prism:creationDate>2023-11-06T05:44:59.220388+00:00</prism:creationDate>
<prism:modificationDate>2023-11-06T05:45:01.746520+00:00</prism:modificationDate>
</entry>
</feed>
```

**レスポンス例：format: rss**

/api/opensearch/search?title=nooai&format=rss&size=1

```xml
<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns="http://purl.org/rss/1.0/" xml:lang="en">
<channel rdf:about="https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;format=rss&amp;size=1">
<title>WEKO OpenSearch: </title>
<link>https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;format=rss&amp;size=1</link>
<docs>http://www.rssboard.org/rss-specification</docs>
<generator>python-feedgen</generator>
<language>en</language>
<items>
<rdf:Seq>
<rdf:li rdf:resource="https://dev.ir.rcos.nii.ac.jp/records/35"/>
</rdf:Seq>
</items>
<lastBuildDate>Tue, 14 Nov 2023 23:48:47 +0000</lastBuildDate>
<dc:date>2023-11-14 23:48:47.221230+00:00</dc:date>
<opensearch:totalResults>9</opensearch:totalResults>
<opensearch:startIndex>1</opensearch:startIndex>
<opensearch:itemsPerPage>1</opensearch:itemsPerPage>
</channel>
<item rdf:about="https://dev.ir.rcos.nii.ac.jp/records/35">
<title>public-item-2-public-nooai-guest-35-ja</title>
<link>https://dev.ir.rcos.nii.ac.jp/records/35</link>
<rdfs:seeAlso rdf:resource="https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;metadataPrefix=jpcoar&amp;identifier=oai:weko3.example.org:00000035"/>
<description>概要
概要
概要
概要</description>
<dc:date>2023-11-14 23:48:47.276148+00:00</dc:date>
<dc:publisher xml:lang="en">Publisher</dc:publisher>
<dc:subject>2-public-nooai-guest-35-ja</dc:subject>
<dc:type>デフォルトアイテムタイプ（フル）</dc:type>
<dc:format>text/plain</dc:format>
<dc:identifier>35</dc:identifier>
<dc:identifier>https://weko3.example.org/record/35/files/1KB.pdf</dc:identifier>
<prism:aggregationType>conference paper</prism:aggregationType>
<prism:creationDate>2023-11-06T05:44:59.220388+00:00</prism:creationDate>
<prism:modificationDate>2023-11-06T05:45:01.746520+00:00</prism:modificationDate>
<prism:url>https://dev.ir.rcos.nii.ac.jp/records/35</prism:url>
</item>
</rdf:RDF>
```

**レスポンス例：format: jpcoar**

/api/opensearch/search?title=nooai&format=jpcoar&size=1

```xml
<rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<header>
<opensearch:totalResults>9</opensearch:totalResults>
<opensearch:startIndex>1</opensearch:startIndex>
<opensearch:itemsPerPage>1</opensearch:itemsPerPage>
</header>
<items>
<rdf:Description rdf:about="https://dev.ir.rcos.nii.ac.jp/records/35">
<jpcoar:jpcoar xmlns:datacite="https://schema.datacite.org/meta/kernel-4/" xmlns:dcndl="http://ndl.go.jp/dcndl/terms/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:jpcoar="https://github.com/JPCOAR/schema/blob/master/2.0/" xmlns:oaire="http://namespace.openaire.eu/schema/oaire/" xmlns:rioxxterms="http://www.rioxx.net/schema/v2.0/rioxxterms/" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="https://github.com/JPCOAR/schema/blob/master/2.0/" xsi:schemaLocation="https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd">
<dc:title xml:lang="ja">public-item-2-public-nooai-guest-35-ja</dc:title>
<dc:title xml:lang="en">public-item-2-public-nooai-guest-35-en</dc:title>
<dcterms:alternative xml:lang="en">Alternative Title</dcterms:alternative>
<dcterms:alternative xml:lang="ja">Alternative Title</dcterms:alternative>
<jpcoar:creator>
<jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID">xxxxxxx</jpcoar:nameIdentifier>
<jpcoar:creatorName xml:lang="ja">情報, 太郎</jpcoar:creatorName>
<jpcoar:creatorName xml:lang="ja-Kana">ジョウホウ タロウ</jpcoar:creatorName>
<jpcoar:creatorName xml:lang="en">Joho Taro</jpcoar:creatorName>
<jpcoar:familyName xml:lang="ja">情報</jpcoar:familyName>
<jpcoar:familyName xml:lang="ja-Kana">ジョウホウ</jpcoar:familyName>
<jpcoar:familyName xml:lang="en">Joho</jpcoar:familyName>
<jpcoar:givenName xml:lang="ja">太郎</jpcoar:givenName>
<jpcoar:givenName xml:lang="ja-Kana">タロウ</jpcoar:givenName>
<jpcoar:givenName xml:lang="en">Taro</jpcoar:givenName>
<jpcoar:affiliation>
<jpcoar:nameIdentifier nameIdentifierURI="http://isni.org/isni/0000000121691048" nameIdentifierScheme="ISNI">0000000121691048</jpcoar:nameIdentifier>
<jpcoar:affiliationName xml:lang="en">University</jpcoar:affiliationName>
</jpcoar:affiliation>
</jpcoar:creator>
<jpcoar:creator>
<jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID">xxxxxxx</jpcoar:nameIdentifier>
<jpcoar:creatorName xml:lang="ja">情報, 太郎</jpcoar:creatorName>
<jpcoar:creatorName xml:lang="ja-Kana">ジョウホウ タロウ</jpcoar:creatorName>
<jpcoar:creatorName xml:lang="en">Joho Taro</jpcoar:creatorName>
<jpcoar:familyName xml:lang="ja">情報</jpcoar:familyName>
<jpcoar:familyName xml:lang="ja-Kana">ジョウホウ</jpcoar:familyName>
<jpcoar:familyName xml:lang="en">Joho</jpcoar:familyName>
<jpcoar:givenName xml:lang="ja">太郎</jpcoar:givenName>
<jpcoar:givenName xml:lang="ja-Kana">タロウ</jpcoar:givenName>
<jpcoar:givenName xml:lang="en">Taro</jpcoar:givenName>
</jpcoar:creator>
<jpcoar:creator>
<jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID">xxxxxxx</jpcoar:nameIdentifier>
<jpcoar:creatorName xml:lang="ja">情報, 太郎</jpcoar:creatorName>
<jpcoar:creatorName xml:lang="ja-Kana">ジョウホウ タロウ</jpcoar:creatorName>
<jpcoar:creatorName xml:lang="en">Joho Taro</jpcoar:creatorName>
<jpcoar:familyName xml:lang="ja">情報</jpcoar:familyName>
<jpcoar:familyName xml:lang="ja-Kana">ジョウホウ</jpcoar:familyName>
<jpcoar:familyName xml:lang="en">Joho</jpcoar:familyName>
<jpcoar:givenName xml:lang="ja">太郎</jpcoar:givenName>
<jpcoar:givenName xml:lang="ja-Kana">タロウ</jpcoar:givenName>
<jpcoar:givenName xml:lang="en">Taro</jpcoar:givenName>
</jpcoar:creator>
<jpcoar:contributor contributorType="ContactPerson">
<jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID">xxxxxxx</jpcoar:nameIdentifier>
<jpcoar:contributorName xml:lang="ja">情報, 太郎</jpcoar:contributorName>
<jpcoar:contributorName xml:lang="ja-Kana">ジョウホウ タロウ</jpcoar:contributorName>
<jpcoar:contributorName xml:lang="en">Joho Taro</jpcoar:contributorName>
<jpcoar:familyName xml:lang="ja">情報</jpcoar:familyName>
<jpcoar:familyName xml:lang="ja-Kana">ジョウホウ</jpcoar:familyName>
<jpcoar:familyName xml:lang="en">Joho</jpcoar:familyName>
<jpcoar:givenName xml:lang="ja">太郎</jpcoar:givenName>
<jpcoar:givenName xml:lang="ja-Kana">タロウ</jpcoar:givenName>
<jpcoar:givenName xml:lang="en">Taro</jpcoar:givenName>
</jpcoar:contributor>
<dcterms:accessRights rdf:resource="http://purl.org/coar/access_right/c_abf2">open access</dcterms:accessRights>
<dc:rights xml:lang="ja" rdf:resource="http://localhost">Rights Information</dc:rights>
<jpcoar:rightsHolder>
<jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID">xxxxxx</jpcoar:nameIdentifier>
<jpcoar:rightsHolderName xml:lang="ja">Right Holder Name</jpcoar:rightsHolderName>
</jpcoar:rightsHolder>
<jpcoar:subject xml:lang="ja" subjectURI="http://localhost/" subjectScheme="Other">Sibject1</jpcoar:subject>
<datacite:description xml:lang="en" descriptionType="Abstract">Description Description Description</datacite:description>
<datacite:description xml:lang="ja" descriptionType="Abstract">概要 概要 概要 概要</datacite:description>
<dc:publisher xml:lang="en">Publisher</dc:publisher>
<datacite:date dateType="Available">2021-06-30</datacite:date>
<dc:language>jpn</dc:language>
<dc:type rdf:resource="http://purl.org/coar/resource_type/c_5794">conference paper</dc:type>
<datacite:version>Version</datacite:version>
<oaire:version rdf:resource="http://purl.org/coar/version/c_b1a7d7d4d402bcce">AO</oaire:version>
<jpcoar:identifier identifierType="URI">http://localhost</jpcoar:identifier>
<jpcoar:relation relationType="isVersionOf">
<jpcoar:relatedIdentifier identifierType="arXiv">xxxxx</jpcoar:relatedIdentifier>
<jpcoar:relatedTitle xml:lang="en">Related Title</jpcoar:relatedTitle>
</jpcoar:relation>
<dcterms:temporal xml:lang="en">Temporal</dcterms:temporal>
<datacite:geoLocation>
<datacite:geoLocationPlace>Japan</datacite:geoLocationPlace>
</datacite:geoLocation>
<jpcoar:fundingReference>
<jpcoar:funderIdentifier funderIdentifierType="ISNI">http://xxx</jpcoar:funderIdentifier>
<jpcoar:funderName xml:lang="en">Funder Name</jpcoar:funderName>
<jpcoar:awardNumber awardURI="Award URI">Award Number</jpcoar:awardNumber>
<jpcoar:awardTitle xml:lang="en">Award Title</jpcoar:awardTitle>
</jpcoar:fundingReference>
<jpcoar:sourceIdentifier identifierType="ISSN">xxxx-xxxx-xxxx</jpcoar:sourceIdentifier>
<jpcoar:sourceTitle xml:lang="en">Source Title</jpcoar:sourceTitle>
<jpcoar:volume>1</jpcoar:volume>
<jpcoar:issue>111</jpcoar:issue>
<jpcoar:numPages>12</jpcoar:numPages>
<jpcoar:pageStart>1</jpcoar:pageStart>
<jpcoar:pageEnd>3</jpcoar:pageEnd>
<dcndl:degreeName xml:lang="en">Degree Name</dcndl:degreeName>
<dcndl:dateGranted>2021-06-30</dcndl:dateGranted>
<jpcoar:degreeGrantor>
<jpcoar:nameIdentifier nameIdentifierScheme="kakenhi">xxxxxx</jpcoar:nameIdentifier>
<jpcoar:degreeGrantorName xml:lang="en">Degree Grantor Name</jpcoar:degreeGrantorName>
</jpcoar:degreeGrantor>
<jpcoar:conference>
<jpcoar:conferenceName xml:lang="ja">Conference Name</jpcoar:conferenceName>
<jpcoar:conferenceSequence>1</jpcoar:conferenceSequence>
<jpcoar:conferenceSponsor xml:lang="ja">Sponsor</jpcoar:conferenceSponsor>
<jpcoar:conferenceDate endDay="1" endYear="2020" endMonth="12" startDay="1" xml:lang="ja" startYear="2000" startMonth="12">2020/12/11</jpcoar:conferenceDate>
<jpcoar:conferenceVenue xml:lang="ja">Conference Venue</jpcoar:conferenceVenue>
<jpcoar:conferenceCountry>JPN</jpcoar:conferenceCountry>
</jpcoar:conference>
<jpcoar:file>
<jpcoar:URI>https://weko3.example.org/record/35/files/1KB.pdf</jpcoar:URI>
<jpcoar:mimeType>text/plain</jpcoar:mimeType>
<jpcoar:extent>1 KB</jpcoar:extent>
</jpcoar:file>
<system_file/>
</jpcoar:jpcoar>
</rdf:Description>
</items>
</rdf:RDF>
```

- 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

- 機能内容

**Opensearch API記述（opensearch/description.xml)　2022/10/28 opensearch api の description.xml は修正の必要性がある。**

- /api/opensearch/description.xml

例：

```xml
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
<ShortName>WEKO</ShortName>
<Description>WEKO - NII Scholarly and Academic Information Navigator</Description>
<Image height="16" type="image/x-icon" width="16">https://localhost:8443/static/favicon.ico</Image>
<Url template="https://localhost:8443/api/opensearch/search?q={searchTerms}" type="application/atom+xml"/>
<Url template="https://localhost:8443/api/opensearch/search?q={searchTerms}&amp;format=atom" type="application/atom+xml"/>
</OpenSearchDescription>
```

**/api/opensearch/search**

クエリパラメータ

- 利用できるクエリパラメータは以下を参照
  - パス：https://github.com/RCOSDP/weko/blob/adbdfd55ce1d9a289e1dd0af8e4383663f6eddaf/modules/weko-search-ui/weko_search_ui/config.py#L245
  - 設定キー：WEKO_SEARCH_KEYWORDS_DICT

レスポンス

**format:rss**

```xml
<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns="http://purl.org/rss/1.0/" xml:lang="en">
<channel rdf:about="https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=rss&amp;title=アブ&amp;list_view_num=1">
<title>WEKO OpenSearch: </title>
<link>https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=rss&amp;title=アブ&amp;list_view_num=1</link>
<docs>http://www.rssboard.org/rss-specification</docs>
<generator>python-feedgen</generator>
<language>en</language>
<items>
<rdf:Seq>
<rdf:li rdf:resource="https://weko3.ir.rcos.nii.ac.jp/records/88854"/>
</rdf:Seq>
</items>
<lastBuildDate>Fri, 28 Oct 2022 05:22:20 +0000</lastBuildDate>
<dc:date>2022-10-28 05:22:20.844292+00:00</dc:date>
<opensearch:totalResults>8</opensearch:totalResults>
<opensearch:startIndex>1</opensearch:startIndex>
<opensearch:itemsPerPage>1</opensearch:itemsPerPage>
</channel>
<item rdf:about="https://weko3.ir.rcos.nii.ac.jp/records/88854">
<title>宮古島のピンザアブ洞の後期更新世堆積物より発見されたヘビ類化石の分類学的帰属とその歴史生物地理学的意義</title>
<link>https://weko3.ir.rcos.nii.ac.jp/records/88854</link>
<rdfs:seeAlso rdf:resource="https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;metadataPrefix=jpcoar&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854"/>
<dc:date>2022-10-28 05:22:20.856008+00:00</dc:date>
<dc:publisher xml:lang="ja">琉球大学21世紀プログラム</dc:publisher>
<dc:subject>ja_Index B-5-1</dc:subject>
<dc:type>Multiple</dc:type>
<dc:identifier>88854</dc:identifier>
<dc:identifier>https://u-ryukyu.repo.nii.ac.jp/record/2001096/files/2006PS-22.pdf</dc:identifier>
<prism:aggregationType>research report</prism:aggregationType>
<prism:publicationName>琉球大学21世紀プログラム「サンゴ礁島嶼系の生物多様性の総合解析」平成18年度成果発表会</prism:publicationName>
<prism:creationDate>2022-03-22T05:56:28.569325+00:00</prism:creationDate>
<prism:modificationDate>2022-03-22T05:56:29.259651+00:00</prism:modificationDate>
<prism:url>https://weko3.ir.rcos.nii.ac.jp/records/88854</prism:url>
</item>
</rdf:RDF>
```

**format:atom**

```xml
<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
<id>https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=atom&amp;title=アブ&amp;list_view_num=1</id>
<title>WEKO OpenSearch: </title>
<updated>2022-10-28T05:15:02.121033+00:00</updated>
<link href="https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=atom&amp;title=アブ&amp;list_view_num=1"/>
<generator uri="http://lkiesow.github.io/python-feedgen" version="0.7.0">python-feedgen</generator>
<opensearch:totalResults>8</opensearch:totalResults>
<opensearch:startIndex>1</opensearch:startIndex>
<opensearch:itemsPerPage>1</opensearch:itemsPerPage>
<entry>
<id>https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;metadataPrefix=jpcoar&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854</id>
<title>宮古島のピンザアブ洞の後期更新世堆積物より発見されたヘビ類化石の分類学的帰属とその歴史生物地理学的意義</title>
<updated>2022-03-22T05:56:29.259651+00:00</updated>
<link href="https://weko3.ir.rcos.nii.ac.jp/records/88854"/>
<link href="https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;metadataPrefix=jpcoar&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854"/>
<dc:publisher xml:lang="ja">琉球大学21世紀プログラム</dc:publisher>
<dc:subject>ja_Index B-5-1</dc:subject>
<dc:type>Multiple</dc:type>
<dc:identifier>88854</dc:identifier>
<dc:identifier>https://u-ryukyu.repo.nii.ac.jp/record/2001096/files/2006PS-22.pdf</dc:identifier>
<prism:aggregationType>research report</prism:aggregationType>
<prism:publicationName>琉球大学21世紀プログラム「サンゴ礁島嶼系の生物多様性の総合解析」平成18年度成果発表会</prism:publicationName>
<prism:creationDate>2022-03-22T05:56:28.569325+00:00</prism:creationDate>
<prism:modificationDate>2022-03-22T05:56:29.259651+00:00</prism:modificationDate>
</entry>
</feed>
```

設定

```python
# Opensearch description
WEKO_OPENSEARCH_SYSTEM_SHORTNAME = 'WEKO'
WEKO_OPENSEARCH_SYSTEM_DESCRIPTION = 'WEKO - NII Scholarly and Academic Information Navigator'
WEKO_OPENSEARCH_IMAGE_URL = 'static/favicon.ico'
```

- 関連モジュール

- invenio_records_rest：検索を行いその結果を返すモジュール
- weko_records：返却値を作成するモジュール
- weko_search_ui：OpenSearch Descriptionファイルを定義するモジュール

- 処理概要

- パラメータの追加
  - modules/invenio-records-rest/invenio_records_rest/views.py

- format変換：
  - modules/invenio-records-rest/invenio_records_rest/serializers/json.py
  - weko_search_ui/views.py
    - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/views.py#L310>

- weko_search_ui.views.opensearch_description関数でOpenSearch Descriptionファイルを作成している
  - invenio_records_rest.views.RecordsListResource.getメソッドで検索を行う
  - 検索自体は、ユーザ画面の詳細検索と同様にElasticSearchで行う
  - RecordsListResourceクラスはWEKOのソースにforkされていないinvenio_rest.views.ContentNegotiatedMethodViewクラスのサブクラスであり、スーパークラスのmake_responseメソッドを使用してgetメソッドの返却値を作成する
  - make_responseメソッドの中でシリアライザを呼び出す。これによってweko_records.serializers.opensearchresponse.oepnsearch_responsify関数が呼び出される
  - その中で呼び出すOpenSearchSerializer.serialize_searchメソッドの中でformatを確認して、内容によって異なるレスポンス作成処理を呼び出す
    - formatの指定が「rss」「atom」「jpcoar」「それ以外」で分岐する
    - 「rss」「atom」の場合は、weko_records.serializers.utils.OpenSearchDetailDataクラスのインスタンスをoutput_type=（指定したformatを表す値）として作成して、output_open_search_detail_dataメソッドによってレスポンスを作成する
    - 「それ以外」の場合は、json形式のレスポンスを作成する

- 関連モジュール

  - invenio-records-rest（実ハンドラ `views.RecordsListResource.get`、レスポンス生成 `oepnsearch_responsify`）
  - weko-search-ui（検索ファクトリ `query.opensearch_factory`、権限フィルタ `query.get_permission_filter`、description.xml `views.opensearch_description`、REST定義 `config.RECORDS_REST_ENDPOINTS["opensearch"]`）
  - weko-records（シリアライザ `serializers.OpenSearchSerializer` / `AtomSerializer` / `RssSerializer` / `JpcoarSerializer`、`serializers.utils.OpenSearchDetailData`）

- 主要設定値

  - `WEKO_SEARCH_KEYWORDS_DICT`（検索キーの内部フィールド対応）
  - `WEKO_OPENSEARCH_SYSTEM_SHORTNAME` / `WEKO_OPENSEARCH_SYSTEM_DESCRIPTION` / `WEKO_OPENSEARCH_SYSTEM_IMAGE_URL`（description.xml）

> 実装補足（v2.0.2）：エンドポイントは `GET /api/opensearch/search`（description は `GET /api/opensearch/description.xml`）。ログイン状態・ロールに応じ `get_permission_filter` で公開範囲を自動的に絞り込む（非管理者は公開かつ公開日到来分のみ）。

> 実装補足（v2.1.0）：OpenSearch の絞り込みは `weko_search_ui/query.py` の `opensearch_factory` が `q`（インデックスID）未指定時に `default_search_factory` を呼ぶため、`accessrights` パラメータによるアクセス権フィルタ（`__get_accessrights_query`）が OpenSearch にも適用される。`WEKO_SEARCH_FIX_ACCESSRIGHTS`（`weko_search_ui/config.py`、既定 `False`）が `True` の場合、`embargoed access` のアイテムをファイルの `content.accessrole.raw`・公開日（`content.date.dateValue.raw`）・現在日で open/restricted/embargoed に振り分けて絞り込む（[API-07](./API_07_item_search.md) と共通）。`False`（既定）では素の term/terms 一致による従来動作。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2023/11/14 | V0.9.27 | |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。`q`パラメータ追加、`wid`（作成者識別子）・`iid`の説明修正、size/pageの別名・既定値、関連モジュール・設定値・権限フィルタを追記 |
| 2026/07/17 |  | v2.1.0差分反映：`accessrights` パラメータ（`opensearch_factory`→`default_search_factory` 経由）とエンバーゴ考慮（`WEKO_SEARCH_FIX_ACCESSRIGHTS`、既定False）を追記 |
