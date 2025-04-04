### OpenSearch

  - 目的・用途

アイテムの検索に利用できる。

  - 利用方法

以下の形のURLを使用して検索ができる

https://\[host\]/api/opensearch/search?クエリパラメータ=値&クエリパラメータ値&...

<table>
<thead>
<tr class="header">
<th><strong>Method</strong></th>
<th><strong>HTTP request</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>weko_search_ui.<br />
views.opensearch_description</td>
<td><strong>GET /api/opensearch/description.xml</strong></td>
<td></td>
</tr>
<tr class="even">
<td>weko_search_ui.<br />
query.opensearch_factory※</td>
<td><strong>GET /api/opensearch/search</strong></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

※ modules/weko-search-ui/weko\_search\_ui/config.py のRECORDS\_REST\_ENDPOINTS\["opensearch"\]にて設定

クエリパラメータ

<table>
<thead>
<tr class="header">
<th><strong>GET /api/opensearch/search</strong></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>パラメータ</td>
<td>必須</td>
<td>値</td>
<td>説明</td>
</tr>
<tr class="even">
<td>format</td>
<td></td>
<td><ul>
<li><p>atom</p></li>
<li><p>rss</p></li>
<li><p>jpcoar</p></li>
</ul></td>
<td><p>レスポンス結果のフォーマット</p>
<p>デフォルトはjson形式。</p></td>
</tr>
<tr class="odd">
<td>size</td>
<td></td>
<td>int</td>
<td>レスポンスに含めるフィード件数</td>
</tr>
<tr class="even">
<td>page</td>
<td></td>
<td>Int</td>
<td>表示するページ番号</td>
</tr>
<tr class="odd">
<td>以下は設定ファイルやアイテムタイプマッピングにより定義が変化する</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>title</td>
<td></td>
<td>string</td>
<td>dc:titleにマッピングされた項目の検索</td>
</tr>
<tr class="odd">
<td>des</td>
<td></td>
<td>strin</td>
<td>datacite:descriptionにマッピングされた項目の検索</td>
</tr>
<tr class="even">
<td>type</td>
<td></td>
<td>string</td>
<td>dc:typeにマッピングされた項目の検索</td>
</tr>
<tr class="odd">
<td>wid</td>
<td></td>
<td>Int</td>
<td>アイテムIDを指定して検索</td>
</tr>
<tr class="even">
<td>Iid</td>
<td></td>
<td>Int</td>
<td>インデックスIDを指定して検索</td>
</tr>
</tbody>
</table>

レスポンス例：

<table>
<thead>
<tr class="header">
<th><strong>レスポンス例：format: atom</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/api/opensearch/search?title=nooai&amp;format=atom&amp;size=1</strong></td>
</tr>
<tr class="even">
<td><p>&lt;feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns="http://www.w3.org/2005/Atom" xml:lang="en"&gt;</p>
<p>&lt;id&gt;https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=atom&amp;amp;size=1&lt;/id&gt;</p>
<p>&lt;title&gt;WEKO OpenSearch: &lt;/title&gt;</p>
<p>&lt;updated&gt;2023-11-14T23:47:46.452823+00:00&lt;/updated&gt;</p>
<p>&lt;link href="https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=atom&amp;amp;size=1"/&gt;</p>
<p>&lt;generator uri="http://lkiesow.github.io/python-feedgen" version="0.7.0"&gt;python-feedgen&lt;/generator&gt;</p>
<p>&lt;opensearch:totalResults&gt;9&lt;/opensearch:totalResults&gt;</p>
<p>&lt;opensearch:startIndex&gt;1&lt;/opensearch:startIndex&gt;</p>
<p>&lt;opensearch:itemsPerPage&gt;1&lt;/opensearch:itemsPerPage&gt;</p>
<p>&lt;entry&gt;</p>
<p>&lt;id&gt;https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;amp;metadataPrefix=jpcoar&amp;amp;identifier=oai:weko3.example.org:00000035&lt;/id&gt;</p>
<p>&lt;title&gt;public-item-2-public-nooai-guest-35-ja&lt;/title&gt;</p>
<p>&lt;updated&gt;2023-11-06T05:45:01.746520+00:00&lt;/updated&gt;</p>
<p>&lt;content xml:lang="ja"&gt;概要</p>
<p>概要</p>
<p>概要</p>
<p>概要&lt;/content&gt;</p>
<p>&lt;link href="https://dev.ir.rcos.nii.ac.jp/records/35"/&gt;</p>
<p>&lt;link href="https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;amp;metadataPrefix=jpcoar&amp;amp;identifier=oai:weko3.example.org:00000035"/&gt;</p>
<p>&lt;dc:publisher xml:lang="en"&gt;Publisher&lt;/dc:publisher&gt;</p>
<p>&lt;dc:subject&gt;2-public-nooai-guest-35-ja&lt;/dc:subject&gt;</p>
<p>&lt;dc:type&gt;デフォルトアイテムタイプ（フル）&lt;/dc:type&gt;</p>
<p>&lt;dc:format&gt;text/plain&lt;/dc:format&gt;</p>
<p>&lt;dc:identifier&gt;35&lt;/dc:identifier&gt;</p>
<p>&lt;dc:identifier&gt;https://weko3.example.org/record/35/files/1KB.pdf&lt;/dc:identifier&gt;</p>
<p>&lt;prism:aggregationType&gt;conference paper&lt;/prism:aggregationType&gt;</p>
<p>&lt;prism:issn&gt;xxxx-xxxx-xxxx&lt;/prism:issn&gt;</p>
<p>&lt;prism:creationDate&gt;2023-11-06T05:44:59.220388+00:00&lt;/prism:creationDate&gt;</p>
<p>&lt;prism:modificationDate&gt;2023-11-06T05:45:01.746520+00:00&lt;/prism:modificationDate&gt;</p>
<p>&lt;/entry&gt;</p>
<p>&lt;/feed&gt;</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>レスポンス例：format: rss</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/api/opensearch/search?title=nooai&amp;format=rss&amp;size=1</strong></td>
</tr>
<tr class="even">
<td><p>&lt;?xml version='1.0' encoding='UTF-8'?&gt;</p>
<p>&lt;rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns="http://purl.org/rss/1.0/" xml:lang="en"&gt;</p>
<p>&lt;channel rdf:about="https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=rss&amp;amp;size=1"&gt;</p>
<p>&lt;title&gt;WEKO OpenSearch: &lt;/title&gt;</p>
<p>&lt;link&gt;https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=rss&amp;amp;size=1&lt;/link&gt;</p>
<p>&lt;docs&gt;http://www.rssboard.org/rss-specification&lt;/docs&gt;</p>
<p>&lt;generator&gt;python-feedgen&lt;/generator&gt;</p>
<p>&lt;language&gt;en&lt;/language&gt;</p>
<p>&lt;items&gt;</p>
<p>&lt;rdf:Seq&gt;</p>
<p>&lt;rdf:li rdf:resource="https://dev.ir.rcos.nii.ac.jp/records/35"/&gt;</p>
<p>&lt;/rdf:Seq&gt;</p>
<p>&lt;/items&gt;</p>
<p>&lt;lastBuildDate&gt;Tue, 14 Nov 2023 23:48:47 +0000&lt;/lastBuildDate&gt;</p>
<p>&lt;dc:date&gt;2023-11-14 23:48:47.221230+00:00&lt;/dc:date&gt;</p>
<p>&lt;opensearch:totalResults&gt;9&lt;/opensearch:totalResults&gt;</p>
<p>&lt;opensearch:startIndex&gt;1&lt;/opensearch:startIndex&gt;</p>
<p>&lt;opensearch:itemsPerPage&gt;1&lt;/opensearch:itemsPerPage&gt;</p>
<p>&lt;/channel&gt;</p>
<p>&lt;item rdf:about="https://dev.ir.rcos.nii.ac.jp/records/35"&gt;</p>
<p>&lt;title&gt;public-item-2-public-nooai-guest-35-ja&lt;/title&gt;</p>
<p>&lt;link&gt;https://dev.ir.rcos.nii.ac.jp/records/35&lt;/link&gt;</p>
<p>&lt;rdfs:seeAlso rdf:resource="https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;amp;metadataPrefix=jpcoar&amp;amp;identifier=oai:weko3.example.org:00000035"/&gt;</p>
<p>&lt;description&gt;概要</p>
<p>概要</p>
<p>概要</p>
<p>概要&lt;/description&gt;</p>
<p>&lt;dc:date&gt;2023-11-14 23:48:47.276148+00:00&lt;/dc:date&gt;</p>
<p>&lt;dc:publisher xml:lang="en"&gt;Publisher&lt;/dc:publisher&gt;</p>
<p>&lt;dc:subject&gt;2-public-nooai-guest-35-ja&lt;/dc:subject&gt;</p>
<p>&lt;dc:type&gt;デフォルトアイテムタイプ（フル）&lt;/dc:type&gt;</p>
<p>&lt;dc:format&gt;text/plain&lt;/dc:format&gt;</p>
<p>&lt;dc:identifier&gt;35&lt;/dc:identifier&gt;</p>
<p>&lt;dc:identifier&gt;https://weko3.example.org/record/35/files/1KB.pdf&lt;/dc:identifier&gt;</p>
<p>&lt;prism:aggregationType&gt;conference paper&lt;/prism:aggregationType&gt;</p>
<p>&lt;prism:creationDate&gt;2023-11-06T05:44:59.220388+00:00&lt;/prism:creationDate&gt;</p>
<p>&lt;prism:modificationDate&gt;2023-11-06T05:45:01.746520+00:00&lt;/prism:modificationDate&gt;</p>
<p>&lt;prism:url&gt;https://dev.ir.rcos.nii.ac.jp/records/35&lt;/prism:url&gt;</p>
<p>&lt;/item&gt;</p>
<p>&lt;/rdf:RDF&gt;</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th>レスポンス例：format: jpcoar</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/api/opensearch/search?title=nooai&amp;format=jpcoar&amp;size=1</strong></td>
</tr>
<tr class="even">
<td><p>This XML file does not appear to have any style information associated with it. The document tree is shown below.</p>
<p>&lt;rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;</p>
<p>&lt;header&gt;</p>
<p>&lt;opensearch:totalResults&gt;9&lt;/opensearch:totalResults&gt;</p>
<p>&lt;opensearch:startIndex&gt;1&lt;/opensearch:startIndex&gt;</p>
<p>&lt;opensearch:itemsPerPage&gt;1&lt;/opensearch:itemsPerPage&gt;</p>
<p>&lt;/header&gt;</p>
<p>&lt;items&gt;</p>
<p>&lt;rdf:Description rdf:about="https://dev.ir.rcos.nii.ac.jp/records/35"&gt;</p>
<p>&lt;jpcoar:jpcoar xmlns:datacite="https://schema.datacite.org/meta/kernel-4/" xmlns:dcndl="http://ndl.go.jp/dcndl/terms/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:jpcoar="https://github.com/JPCOAR/schema/blob/master/2.0/" xmlns:oaire="http://namespace.openaire.eu/schema/oaire/" xmlns:rioxxterms="http://www.rioxx.net/schema/v2.0/rioxxterms/" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="https://github.com/JPCOAR/schema/blob/master/2.0/" xsi:schemaLocation="https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd"&gt;</p>
<p>&lt;dc:title xml:lang="ja"&gt;public-item-2-public-nooai-guest-35-ja&lt;/dc:title&gt;</p>
<p>&lt;dc:title xml:lang="en"&gt;public-item-2-public-nooai-guest-35-en&lt;/dc:title&gt;</p>
<p>&lt;dcterms:alternative xml:lang="en"&gt;Alternative Title&lt;/dcterms:alternative&gt;</p>
<p>&lt;dcterms:alternative xml:lang="ja"&gt;Alternative Title&lt;/dcterms:alternative&gt;</p>
<p>&lt;jpcoar:creator&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID"&gt;xxxxxxx&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="ja"&gt;情報, 太郎&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="ja-Kana"&gt;ジョウホウ タロウ&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="en"&gt;Joho Taro&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja"&gt;情報&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja-Kana"&gt;ジョウホウ&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="en"&gt;Joho&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja"&gt;太郎&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja-Kana"&gt;タロウ&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="en"&gt;Taro&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:affiliation&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierURI="http://isni.org/isni/0000000121691048" nameIdentifierScheme="ISNI"&gt;0000000121691048&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:affiliationName xml:lang="en"&gt;University&lt;/jpcoar:affiliationName&gt;</p>
<p>&lt;/jpcoar:affiliation&gt;</p>
<p>&lt;/jpcoar:creator&gt;</p>
<p>&lt;jpcoar:creator&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID"&gt;xxxxxxx&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="ja"&gt;情報, 太郎&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="ja-Kana"&gt;ジョウホウ タロウ&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="en"&gt;Joho Taro&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja"&gt;情報&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja-Kana"&gt;ジョウホウ&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="en"&gt;Joho&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja"&gt;太郎&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja-Kana"&gt;タロウ&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="en"&gt;Taro&lt;/jpcoar:givenName&gt;</p>
<p>&lt;/jpcoar:creator&gt;</p>
<p>&lt;jpcoar:creator&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID"&gt;xxxxxxx&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="ja"&gt;情報, 太郎&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="ja-Kana"&gt;ジョウホウ タロウ&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:creatorName xml:lang="en"&gt;Joho Taro&lt;/jpcoar:creatorName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja"&gt;情報&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja-Kana"&gt;ジョウホウ&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="en"&gt;Joho&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja"&gt;太郎&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja-Kana"&gt;タロウ&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="en"&gt;Taro&lt;/jpcoar:givenName&gt;</p>
<p>&lt;/jpcoar:creator&gt;</p>
<p>&lt;jpcoar:contributor contributorType="ContactPerson"&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID"&gt;xxxxxxx&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:contributorName xml:lang="ja"&gt;情報, 太郎&lt;/jpcoar:contributorName&gt;</p>
<p>&lt;jpcoar:contributorName xml:lang="ja-Kana"&gt;ジョウホウ タロウ&lt;/jpcoar:contributorName&gt;</p>
<p>&lt;jpcoar:contributorName xml:lang="en"&gt;Joho Taro&lt;/jpcoar:contributorName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja"&gt;情報&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="ja-Kana"&gt;ジョウホウ&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:familyName xml:lang="en"&gt;Joho&lt;/jpcoar:familyName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja"&gt;太郎&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="ja-Kana"&gt;タロウ&lt;/jpcoar:givenName&gt;</p>
<p>&lt;jpcoar:givenName xml:lang="en"&gt;Taro&lt;/jpcoar:givenName&gt;</p>
<p>&lt;/jpcoar:contributor&gt;</p>
<p>&lt;dcterms:accessRights rdf:resource="http://purl.org/coar/access_right/c_abf2"&gt;open access&lt;/dcterms:accessRights&gt;</p>
<p>&lt;dc:rights xml:lang="ja" rdf:resource="http://localhost"&gt;Rights Information&lt;/dc:rights&gt;</p>
<p>&lt;jpcoar:rightsHolder&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierURI="https://orcid.org/" nameIdentifierScheme="ORCID"&gt;xxxxxx&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:rightsHolderName xml:lang="ja"&gt;Right Holder Name&lt;/jpcoar:rightsHolderName&gt;</p>
<p>&lt;/jpcoar:rightsHolder&gt;</p>
<p>&lt;jpcoar:subject xml:lang="ja" subjectURI="http://localhost/" subjectScheme="Other"&gt;Sibject1&lt;/jpcoar:subject&gt;</p>
<p>&lt;datacite:description xml:lang="en" descriptionType="Abstract"&gt;Description Description Description&lt;/datacite:description&gt;</p>
<p>&lt;datacite:description xml:lang="ja" descriptionType="Abstract"&gt;概要 概要 概要 概要&lt;/datacite:description&gt;</p>
<p>&lt;dc:publisher xml:lang="en"&gt;Publisher&lt;/dc:publisher&gt;</p>
<p>&lt;datacite:date dateType="Available"&gt;2021-06-30&lt;/datacite:date&gt;</p>
<p>&lt;dc:language&gt;jpn&lt;/dc:language&gt;</p>
<p>&lt;dc:type rdf:resource="http://purl.org/coar/resource_type/c_5794"&gt;conference paper&lt;/dc:type&gt;</p>
<p>&lt;datacite:version&gt;Version&lt;/datacite:version&gt;</p>
<p>&lt;oaire:version rdf:resource="http://purl.org/coar/version/c_b1a7d7d4d402bcce"&gt;AO&lt;/oaire:version&gt;</p>
<p>&lt;jpcoar:identifier identifierType="URI"&gt;http://localhost&lt;/jpcoar:identifier&gt;</p>
<p>&lt;jpcoar:relation relationType="isVersionOf"&gt;</p>
<p>&lt;jpcoar:relatedIdentifier identifierType="arXiv"&gt;xxxxx&lt;/jpcoar:relatedIdentifier&gt;</p>
<p>&lt;jpcoar:relatedTitle xml:lang="en"&gt;Related Title&lt;/jpcoar:relatedTitle&gt;</p>
<p>&lt;/jpcoar:relation&gt;</p>
<p>&lt;dcterms:temporal xml:lang="en"&gt;Temporal&lt;/dcterms:temporal&gt;</p>
<p>&lt;datacite:geoLocation&gt;</p>
<p>&lt;datacite:geoLocationPlace&gt;Japan&lt;/datacite:geoLocationPlace&gt;</p>
<p>&lt;/datacite:geoLocation&gt;</p>
<p>&lt;jpcoar:fundingReference&gt;</p>
<p>&lt;jpcoar:funderIdentifier funderIdentifierType="ISNI"&gt;http://xxx&lt;/jpcoar:funderIdentifier&gt;</p>
<p>&lt;jpcoar:funderName xml:lang="en"&gt;Funder Name&lt;/jpcoar:funderName&gt;</p>
<p>&lt;jpcoar:awardNumber awardURI="Award URI"&gt;Award Number&lt;/jpcoar:awardNumber&gt;</p>
<p>&lt;jpcoar:awardTitle xml:lang="en"&gt;Award Title&lt;/jpcoar:awardTitle&gt;</p>
<p>&lt;/jpcoar:fundingReference&gt;</p>
<p>&lt;jpcoar:sourceIdentifier identifierType="ISSN"&gt;xxxx-xxxx-xxxx&lt;/jpcoar:sourceIdentifier&gt;</p>
<p>&lt;jpcoar:sourceTitle xml:lang="en"&gt;Source Title&lt;/jpcoar:sourceTitle&gt;</p>
<p>&lt;jpcoar:volume&gt;1&lt;/jpcoar:volume&gt;</p>
<p>&lt;jpcoar:issue&gt;111&lt;/jpcoar:issue&gt;</p>
<p>&lt;jpcoar:numPages&gt;12&lt;/jpcoar:numPages&gt;</p>
<p>&lt;jpcoar:pageStart&gt;1&lt;/jpcoar:pageStart&gt;</p>
<p>&lt;jpcoar:pageEnd&gt;3&lt;/jpcoar:pageEnd&gt;</p>
<p>&lt;dcndl:degreeName xml:lang="en"&gt;Degree Name&lt;/dcndl:degreeName&gt;</p>
<p>&lt;dcndl:dateGranted&gt;2021-06-30&lt;/dcndl:dateGranted&gt;</p>
<p>&lt;jpcoar:degreeGrantor&gt;</p>
<p>&lt;jpcoar:nameIdentifier nameIdentifierScheme="kakenhi"&gt;xxxxxx&lt;/jpcoar:nameIdentifier&gt;</p>
<p>&lt;jpcoar:degreeGrantorName xml:lang="en"&gt;Degree Grantor Name&lt;/jpcoar:degreeGrantorName&gt;</p>
<p>&lt;/jpcoar:degreeGrantor&gt;</p>
<p>&lt;jpcoar:conference&gt;</p>
<p>&lt;jpcoar:conferenceName xml:lang="ja"&gt;Conference Name&lt;/jpcoar:conferenceName&gt;</p>
<p>&lt;jpcoar:conferenceSequence&gt;1&lt;/jpcoar:conferenceSequence&gt;</p>
<p>&lt;jpcoar:conferenceSponsor xml:lang="ja"&gt;Sponsor&lt;/jpcoar:conferenceSponsor&gt;</p>
<p>&lt;jpcoar:conferenceDate endDay="1" endYear="2020" endMonth="12" startDay="1" xml:lang="ja" startYear="2000" startMonth="12"&gt;2020/12/11&lt;/jpcoar:conferenceDate&gt;</p>
<p>&lt;jpcoar:conferenceVenue xml:lang="ja"&gt;Conference Venue&lt;/jpcoar:conferenceVenue&gt;</p>
<p>&lt;jpcoar:conferenceCountry&gt;JPN&lt;/jpcoar:conferenceCountry&gt;</p>
<p>&lt;/jpcoar:conference&gt;</p>
<p>&lt;jpcoar:file&gt;</p>
<p>&lt;jpcoar:URI&gt;https://weko3.example.org/record/35/files/1KB.pdf&lt;/jpcoar:URI&gt;</p>
<p>&lt;jpcoar:mimeType&gt;text/plain&lt;/jpcoar:mimeType&gt;</p>
<p>&lt;jpcoar:extent&gt;1 KB&lt;/jpcoar:extent&gt;</p>
<p>&lt;/jpcoar:file&gt;</p>
<p>&lt;system_file/&gt;</p>
<p>&lt;/jpcoar:jpcoar&gt;</p>
<p>&lt;/rdf:Description&gt;</p>
<p>&lt;/items&gt;</p>
<p>&lt;/rdf:RDF&gt;</p></td>
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
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
</tr>
</tbody>
</table>

  - 機能内容

**Opensearch API記述（opensearch/description.xml)　2022/10/28 opensearch api の description.xml は修正の必要性がある。**

  - /api/opensearch/description.xml

> 例：
> 
> **\<OpenSearchDescription** xmlns="http://a9.com/-/spec/opensearch/1.1/"**\>**
> 
> **\<ShortName\>**WEKO**\</ShortName\>**
> 
> **\<Description\>**WEKO - NII Scholarly and Academic Information Navigator**\</Description\>**
> 
> **\<Image** height="16" type="image/x-icon" width="16"**\>**https://localhost:8443/static/favicon.ico**\</Image\>**
> 
> **\<Url** template="https://localhost:8443/api/opensearch/search?q={searchTerms}" type="application/atom+xml"**/\>**
> 
> **\<Url** template="https://localhost:8443/api/opensearch/search?q={searchTerms}**\&amp;**format=atom" type="application/atom+xml"**/\>**
> 
> **\</OpenSearchDescription\>**

**/api/opensearch/search**

クエリパラメータ

  - 利用できるクエリパラメータは以下を参照
    
      - パス：https://github.com/RCOSDP/weko/blob/adbdfd55ce1d9a289e1dd0af8e4383663f6eddaf/modules/weko-search-ui/weko\_search\_ui/config.py\#L245
    
      - 設定キー：WEKO\_SEARCH\_KEYWORDS\_DICT

レスポンス

**format:rss**

> \<?xml version='1.0' encoding='UTF-8'?\>
> 
> \<rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns\#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema\#" xmlns="http://purl.org/rss/1.0/" xml:lang="en"\>
> 
> \<channel rdf:about="https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=rss\&amp;title=アブ\&amp;list\_view\_num=1"\>
> 
> \<title\>WEKO OpenSearch: \</title\>
> 
> \<link\>https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=rss\&amp;title=アブ\&amp;list\_view\_num=1\</link\>
> 
> \<docs\>http://www.rssboard.org/rss-specification\</docs\>
> 
> \<generator\>python-feedgen\</generator\>
> 
> \<language\>en\</language\>
> 
> \<items\>
> 
> \<rdf:Seq\>
> 
> \<rdf:li rdf:resource="https://weko3.ir.rcos.nii.ac.jp/records/88854"/\>
> 
> \</rdf:Seq\>
> 
> \</items\>
> 
> \<lastBuildDate\>Fri, 28 Oct 2022 05:22:20 +0000\</lastBuildDate\>
> 
> \<dc:date\>2022-10-28 05:22:20.844292+00:00\</dc:date\>
> 
> \<opensearch:totalResults\>8\</opensearch:totalResults\>
> 
> \<opensearch:startIndex\>1\</opensearch:startIndex\>
> 
> \<opensearch:itemsPerPage\>1\</opensearch:itemsPerPage\>
> 
> \</channel\>
> 
> \<item rdf:about="https://weko3.ir.rcos.nii.ac.jp/records/88854"\>
> 
> \<title\>宮古島のピンザアブ洞の後期更新世堆積物より発見されたヘビ類化石の分類学的帰属とその歴史生物地理学的意義\</title\>
> 
> \<link\>https://weko3.ir.rcos.nii.ac.jp/records/88854\</link\>
> 
> \<rdfs:seeAlso rdf:resource="https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord\&amp;metadataPrefix=jpcoar\&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854"/\>
> 
> \<dc:date\>2022-10-28 05:22:20.856008+00:00\</dc:date\>
> 
> \<dc:publisher xml:lang="ja"\>琉球大学21世紀プログラム\</dc:publisher\>
> 
> \<dc:subject\>ja\_Index B-5-1\</dc:subject\>
> 
> \<dc:type\>Multiple\</dc:type\>
> 
> \<dc:identifier\>88854\</dc:identifier\>
> 
> \<dc:identifier\>https://u-ryukyu.repo.nii.ac.jp/record/2001096/files/2006PS-22.pdf\</dc:identifier\>
> 
> \<prism:aggregationType\>research report\</prism:aggregationType\>
> 
> \<prism:publicationName\>琉球大学21世紀プログラム「サンゴ礁島嶼系の生物多様性の総合解析」平成18年度成果発表会\</prism:publicationName\>
> 
> \<prism:creationDate\>2022-03-22T05:56:28.569325+00:00\</prism:creationDate\>
> 
> \<prism:modificationDate\>2022-03-22T05:56:29.259651+00:00\</prism:modificationDate\>
> 
> \<prism:url\>https://weko3.ir.rcos.nii.ac.jp/records/88854\</prism:url\>
> 
> \</item\>
> 
> \</rdf:RDF\>

**format:atom**

> \<?xml version='1.0' encoding='UTF-8'?\>
> 
> \<feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns="http://www.w3.org/2005/Atom" xml:lang="en"\>
> 
> \<id\>https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=atom\&amp;title=アブ\&amp;list\_view\_num=1\</id\>
> 
> \<title\>WEKO OpenSearch: \</title\>
> 
> \<updated\>2022-10-28T05:15:02.121033+00:00\</updated\>
> 
> \<link href="https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=atom\&amp;title=アブ\&amp;list\_view\_num=1"/\>
> 
> \<generator uri="http://lkiesow.github.io/python-feedgen" version="0.7.0"\>python-feedgen\</generator\>
> 
> \<opensearch:totalResults\>8\</opensearch:totalResults\>
> 
> \<opensearch:startIndex\>1\</opensearch:startIndex\>
> 
> \<opensearch:itemsPerPage\>1\</opensearch:itemsPerPage\>
> 
> \<entry\>
> 
> \<id\>https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord\&amp;metadataPrefix=jpcoar\&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854\</id\>
> 
> \<title\>宮古島のピンザアブ洞の後期更新世堆積物より発見されたヘビ類化石の分類学的帰属とその歴史生物地理学的意義\</title\>
> 
> \<updated\>2022-03-22T05:56:29.259651+00:00\</updated\>
> 
> \<link href="https://weko3.ir.rcos.nii.ac.jp/records/88854"/\>
> 
> \<link href="https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord\&amp;metadataPrefix=jpcoar\&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854"/\>
> 
> \<dc:publisher xml:lang="ja"\>琉球大学21世紀プログラム\</dc:publisher\>
> 
> \<dc:subject\>ja\_Index B-5-1\</dc:subject\>
> 
> \<dc:type\>Multiple\</dc:type\>
> 
> \<dc:identifier\>88854\</dc:identifier\>
> 
> \<dc:identifier\>https://u-ryukyu.repo.nii.ac.jp/record/2001096/files/2006PS-22.pdf\</dc:identifier\>
> 
> \<prism:aggregationType\>research report\</prism:aggregationType\>
> 
> \<prism:publicationName\>琉球大学21世紀プログラム「サンゴ礁島嶼系の生物多様性の総合解析」平成18年度成果発表会\</prism:publicationName\>
> 
> \<prism:creationDate\>2022-03-22T05:56:28.569325+00:00\</prism:creationDate\>
> 
> \<prism:modificationDate\>2022-03-22T05:56:29.259651+00:00\</prism:modificationDate\>
> 
> \</entry\>
> 
> \</feed\>

  - 
設定

> \# Opensearch description
> 
> WEKO\_OPENSEARCH\_SYSTEM\_SHORTNAME = 'WEKO'
> 
> WEKO\_OPENSEARCH\_SYSTEM\_DESCRIPTION = 'WEKO - NII Scholarly and Academic Information Navigator'
> 
> WEKO\_OPENSEARCH\_IMAGE\_URL = 'static/favicon.ico'

  - > 関連モジュール

<!-- end list -->

  - invenio\_records\_rest：検索を行いその結果を返すモジュール

  - weko\_records：返却値を作成するモジュール

  - weko\_search\_ui：OpenSearch Descriptionファイルを定義するモジュール

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - パラメータの追加
    
      - modules/invenio-records-rest/invenio\_records\_rest/views.py

  - format変換：
    
      - modules/invenio-records-rest/invenio\_records\_rest/serializers/json.py
    
      - weko\_search\_ui/views.py
        
          - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/views.py#L310>

<!-- end list -->

  - weko\_search\_ui.views. opensearch\_description関数でOpenSearch Descriptionファイルを作成している
    
      - > invenio\_records\_rest.views.RecordsListResource.getメソッドで検索を行う
    
    <!-- end list -->
    
      - 検索自体は、ユーザ画面の詳細検索と同様にElasticSearchで行う
    
      - RecordsListResourceクラスはWEKOのソースにforkされていないinvenio\_rest.views. ContentNegotiatedMethodViewクラスのサブクラスであり、スーパークラスのmake\_responseメソッドを使用してgetメソッドの返却値を作成する
    
      - make\_responseメソッドの中でシリアライザを呼び出す。これによってweko\_records.serializers.opensearchresponse.opensearch\_responsify関数が呼び出される
    
      - その中で呼び出すOpenSearchSerializer.serialize\_searchメソッドの中でformatを確認して、内容によって異なるレスポンス作成処理を呼び出す
        
          - formatの指定が「rss」「atom」「jpcoar」「それ以外」で分岐する
        
          - 「rss」「atom」の場合は、weko\_records.serializers.utils. OpenSearchDetailDataクラスのインスタンスをoutput\_type=（指定したformatを表す値）として作成して、output\_open\_search\_detail\_dataメソッドによってレスポンスを作成する
        
          - 「それ以外」の場合は、json形式のレスポンスを作成する

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
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2023/11/14</p>
</blockquote></td>
<td>V0.9.27</td>
<td></td>
</tr>
</tbody>
</table>
