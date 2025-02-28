### OpenSearch

#### 目的・用途

アイテムの検索に利用できる。

#### エンドポイントURL

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
<td>description.xmlを表示する</td>
</tr>
<tr class="even">
<td>weko_search_ui.<br />
query.opensearch_factory※</td>
<td><strong>GET /api/opensearch/search</strong></td>
<td>アイテムを検索する</td>
</tr>
</tbody>
</table>

※ modules/weko-search-ui/weko_search_ui/config.py のRECORDS_REST_ENDPOINTS["opensearch"]にて設定

#### 利用可能なロール

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

#### 関連モジュール
  - invenio_records_rest：検索を行いその結果を返すモジュール
  - weko_records：返却値を作成するモジュール
  - weko_search_ui：OpenSearch Descriptionファイルを定義するモジュール

#### /api/opensearch/description.xml

- 機能内容
  - OpenSearch API記述(opensearch/description.xml)を返却する

  **Opensearch API記述（opensearch/description.xml)　2022/10/28 opensearch api の description.xml は修正の必要性がある。**

- レスポンス例

  ```xml
  <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>WEKO</ShortName>
  <Description>WEKO - NII Scholarly and Academic Information Navigator</Description>
  <Image height="16" type="image/x-icon" width="16">https://localhost:8443/static/favicon.ico</Image>
  <Url template="https://localhost:8443/api/opensearch/search?q={searchTerms}" type="application/atom+xml"/>
  <Url template="https://localhost:8443/api/opensearch/search?q={searchTerms}\&amp;format=atom" type="application/atom+xml"/>
  </OpenSearchDescription>
  ```

- 処理概要
  - weko_search_ui.views.opensearch_description関数でOpenSearch Descriptionファイルを作成している

- 設定
  - modules/weko-search-ui/weko_search_ui/config.py で表示内容を設定している

  ```python
  # Opensearch description
  WEKO_OPENSEARCH_SYSTEM_SHORTNAME = 'WEKO'
  WEKO_OPENSEARCH_SYSTEM_DESCRIPTION = 'WEKO - NII Scholarly and Academic Information Navigator'
  WEKO_OPENSEARCH_IMAGE_URL = 'static/favicon.ico'
  ```

#### /api/opensearch/search

- 機能内容
  
  - 以下の形のURLを使用してアイテムの検索ができる  
    https://\[host\]/api/opensearch/search?クエリパラメータ=値&クエリパラメータ=値&...

- 処理概要

  - パラメータの追加
    - modules/invenio-records-rest/invenio_records_rest/views.py

  - format変換
    - modules/invenio-records-rest/invenio_records_rest/serializers/json.py
    - weko_search_ui/views.py
      - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/views.py#L310>
    
  - invenio_records_rest.views.RecordsListResource.getメソッドで検索を行う
    - 検索自体は、ユーザ画面の詳細検索と同様にElasticSearchで行う
    - RecordsListResourceクラスはWEKOのソースにforkされていないinvenio_rest.views. ContentNegotiatedMethodViewクラスのサブクラスであり、スーパークラスのmake_responseメソッドを使用してgetメソッドの返却値を作成する
    - make_responseメソッドの中でシリアライザを呼び出す。これによってweko_records.serializers.opensearchresponse.opensearch_responsify関数が呼び出される
    - その中で呼び出すOpenSearchSerializer.serialize_searchメソッドの中でformatを確認して、内容によって異なるレスポンス作成処理を呼び出す
      - formatの指定が「rss」「atom」「jpcoar」「それ以外」で分岐する
      - 「rss」「atom」の場合は、weko_records.serializers.utils. OpenSearchDetailDataクラスのインスタンスをoutput_type=（指定したformatを表す値）として作成して、output_open_search_detail_dataメソッドによってレスポンスを作成する
      - 「jpcoar」の場合は、jpcoar形式のレスポンスを作成する
      - 「それ以外」の場合は、json形式のレスポンスを作成する

- クエリパラメータ

  - 利用できるクエリパラメータは以下を参照している
    - パス：https://github.com/RCOSDP/weko/blob/adbdfd55ce1d9a289e1dd0af8e4383663f6eddaf/modules/weko-search-ui/weko_search_ui/config.py#L245
    - 設定キー：WEKO_SEARCH_KEYWORDS_DICT

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
  <td>型</td>
  <td>説明</td>
  </tr>
  <tr class="even">
  <td>format</td>
  <td></td>
  <td>string</td>
  <td>
  レスポンス結果のフォーマット<br>
  以下から選択する<br>
  <ul>
    <li>atom</li>
    <li>rss</li>
    <li>jpcoar</li>
    <li>json</li>
  </ul>
  デフォルトはjson形式
  </td>
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
  <td>int</td>
  <td>表示するページ番号</td>
  </tr>
  <tr class="odd">
  <td>以下は設定ファイルやアイテムタイプマッピングにより定義が変化する</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>keyword</td>
  <td></td>
  <td>string</td>
  <td>検索キーワードを指定して検索</td>
  </tr>
  <tr class="even">
  <td>title</td>
  <td></td>
  <td>string</td>
  <td>タイトルを指定して検索</td>
  </tr>
  <tr class="odd">
  <td>des</td>
  <td></td>
  <td>string</td>
  <td>内容記述を指定して検索</td>
  </tr>
  <tr class="even">
  <td>type</td>
  <td></td>
  <td>int (候補から選択)</td>
  <td>資源タイプを指定して検索</td>
  </tr>
  <tr class="odd">
  <td>wid</td>
  <td></td>
  <td>int</td>
  <td>作成者識別子を指定して検索</td>
  </tr>
  <tr class="even">
  <td>iid</td>
  <td></td>
  <td>int</td>
  <td>インデックスIDを指定して検索</td>
  </tr>
  <tr>
  <td>exact_title_match</td>
  <td></td>
  <td>bool</td>
  <td>タイトル完全一致検索を指定する (デフォルト:false)</td>
  </tr>
  <tr>
  <td>creator</td>
  <td></td>
  <td>string</td>
  <td>著者名を指定して検索</td>
  </tr>
  <tr>
  <td>subject</td>
  <td></td>
  <td>string</td>
  <td>件名を指定して検索</td>
  </tr>
  <tr>
  <td>sbjscheme</td>
  <td></td>
  <td>int (候補から選択)</td>
  <td>件名種別を指定して検索</td>
  </tr>
  <tr>
  <td>spatial</td>
  <td></td>
  <td>string</td>
  <td>地域を指定して検索</td>
  </tr>
  <tr>
  <td>publisher</td>
  <td></td>
  <td>string</td>
  <td>出版者を指定して検索</td>
  </tr>
  <tr>
  <td>cname</td>
  <td></td>
  <td>string</td>
  <td>寄与者を指定して検索</td>
  </tr>
  <tr>
  <td>fd_attr</td>
  <td></td>
  <td>string (候補から選択)</td>
  <td>日付種別を指定して検索</td>
  </tr>
  <tr>
  <td>filedate_from</td>
  <td></td>
  <td>date (YYYYMMDD形式)</td>
  <td>日付下限を指定して検索</td>
  </tr>
  <tr>
  <td>filedate_to</td>
  <td></td>
  <td>date (YYYYMMDD形式)</td>
  <td>日付上限を指定して検索</td>
  </tr>
  <tr>
  <td>mimetype</td>
  <td></td>
  <td>string</td>
  <td>フォーマットを指定して検索</td>
  </tr>
  <tr>
  <td>id</td>
  <td></td>
  <td>string</td>
  <td>識別子を指定して検索</td>
  </tr>
  <tr>
  <td>id_attr</td>
  <td></td>
  <td>string (候補から選択)</td>
  <td>識別子種別を指定して検索</td>
  </tr>
  <tr>
  <td>srctitle</td>
  <td></td>
  <td>string</td>
  <td>雑誌名を指定して検索</td>
  </tr>
  <tr>
  <td>itemtype</td>
  <td></td>
  <td>string</td>
  <td>アイテムタイプを指定して検索</td>
  </tr>
  <tr>
  <td>lang</td>
  <td></td>
  <td>string (候補から選択)</td>
  <td>言語を指定して検索</td>
  </tr>
  <tr>
  <td>temporal</td>
  <td></td>
  <td>string</td>
  <td>期間を指定して検索</td>
  </tr>
  <tr>
  <td>dategranted_from</td>
  <td></td>
  <td>date (YYYYMMDD形式)</td>
  <td>学位取得日下限を指定して検索</td>
  </tr>
  <tr>
  <td>dategranted_to</td>
  <td></td>
  <td>date (YYYYMMDD形式)</td>
  <td>学位取得日上限を指定して検索</td>
  </tr>
  <tr>
  <td>version</td>
  <td></td>
  <td>string (候補から選択)</td>
  <td>著者版フラグを指定して検索</td>
  </tr>
  <tr>
  <td>dissno</td>
  <td></td>
  <td>string</td>
  <td>学位番号を指定して検索</td>
  </tr>
  <tr>
  <td>degreename</td>
  <td></td>
  <td>string</td>
  <td>学位名を指定して検索</td>
  </tr>
  <tr>
  <td>dgname</td>
  <td></td>
  <td>string</td>
  <td>学位授与機関を指定して検索</td>
  </tr>
  <tr>
  <td>license</td>
  <td></td>
  <td>string (候補から選択)</td>
  <td>ライセンスを指定して検索</td>
  </tr>
  </tbody>
  </table>

- パラメータ sbjscheme, fd_attr, id_attr, type, lang, version, license について
  - 使用可能な値が事前に定義されている  
  - 使用可能な値と、値を指定した際に検索に用いられる値はDBのsearch_managementテーブルのsearch_conditions列(DBにデータがない場合はmodules/weko-admin/weko_admin/config.pyのdetail_condition) を参照する
  - 使用できない値を指定したパラメータは無視される
  - 複数の値を指定する場合は「,」(カンマ)で区切って指定する

- (subject, sbjscheme), (fd_attr, filedate_from, filedate_to), (id, id_attr), (dategranted_from, dategranted_to) は括弧内のパラメータを全て指定した場合のみ検索条件として使用される

- レスポンス例：

  **format: atom**  
  **/api/opensearch/search?title=nooai&amp;format=atom&amp;size=1**

  ```xml
  <feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
  <id>https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=atom&amp;amp;size=1</id>
  <title>WEKO OpenSearch: </title>
  <updated>2023-11-14T23:47:46.452823+00:00</updated>
  <link href="https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=atom&amp;amp;size=1"/>
  <generator uri="http://lkiesow.github.io/python-feedgen" version="0.7.0">python-feedgen</generator>
  <opensearch:totalResults>9</opensearch:totalResults>
  <opensearch:startIndex>1</opensearch:startIndex>
  <opensearch:itemsPerPage>1</opensearch:itemsPerPage>
  <entry>
  <id>https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;amp;metadataPrefix=jpcoar&amp;amp;identifier=oai:weko3.example.org:00000035</id>
  <title>public-item-2-public-nooai-guest-35-ja</title>
  <updated>2023-11-06T05:45:01.746520+00:00</updated>
  <content xml:lang="ja">概要
  概要
  概要
  概要</content>
  <link href="https://dev.ir.rcos.nii.ac.jp/records/35"/>
  <link href="https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;amp;metadataPrefix=jpcoar&amp;amp;identifier=oai:weko3.example.org:00000035"/>
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

  **format: rss**  
  **/api/opensearch/search?title=nooai&amp;format=rss&amp;size=1**

  ```xml
  <?xml version='1.0' encoding='UTF-8'?>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns="http://purl.org/rss/1.0/" xml:lang="en">
  <channel rdf:about="https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=rss&amp;amp;size=1">
  <title>WEKO OpenSearch: </title>
  <link>https://dev.ir.rcos.nii.ac.jp/api/opensearch/search?title=nooai&amp;amp;format=rss&amp;amp;size=1</link>
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
  <rdfs:seeAlso rdf:resource="https://dev.ir.rcos.nii.ac.jp/oai?verb=GetRecord&amp;amp;metadataPrefix=jpcoar&amp;amp;identifier=oai:weko3.example.org:00000035"/>
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

  **format: jpcoar**  
  **/api/opensearch/search?title=nooai&amp;format=jpcoar&amp;size=1**

  ```xml
  This XML file does not appear to have any style information associated with it. The document tree is shown below.
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

  **format: rss**

    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns\#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema\#" xmlns="http://purl.org/rss/1.0/" xml:lang="en">
    <channel rdf:about="https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=rss\&amp;title=アブ\&amp;list\_view\_num=1">
    <title>WEKO OpenSearch: </title>
    <link>https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=rss\&amp;title=アブ\&amp;list\_view\_num=1</link>
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
    <rdfs:seeAlso rdf:resource="https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord\&amp;metadataPrefix=jpcoar\&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854"/>
    <dc:date>2022-10-28 05:22:20.856008+00:00</dc:date>
    <dc:publisher xml:lang="ja">琉球大学21世紀プログラム</dc:publisher>
    <dc:subject>ja\_Index B-5-1</dc:subject>
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

  **format: atom**

    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
    <id>https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=atom\&amp;title=アブ\&amp;list\_view\_num=1</id>
    <title>WEKO OpenSearch: </title>
    <updated>2022-10-28T05:15:02.121033+00:00</updated>
    <link href="https://weko3.ir.rcos.nii.ac.jp/api/opensearch/search?format=atom\&amp;title=アブ\&amp;list\_view\_num=1"/>
    <generator uri="http://lkiesow.github.io/python-feedgen" version="0.7.0">python-feedgen</generator>
    <opensearch:totalResults>8</opensearch:totalResults>
    <opensearch:startIndex>1</opensearch:startIndex>
    <opensearch:itemsPerPage>1</opensearch:itemsPerPage>
    <entry>
    <id>https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord\&amp;metadataPrefix=jpcoar\&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854</id>
    <title>宮古島のピンザアブ洞の後期更新世堆積物より発見されたヘビ類化石の分類学的帰属とその歴史生物地理学的意義</title>
    <updated>2022-03-22T05:56:29.259651+00:00</updated>
    <link href="https://weko3.ir.rcos.nii.ac.jp/records/88854"/>
    <link href="https://weko3.ir.rcos.nii.ac.jp/oai?verb=GetRecord\&amp;metadataPrefix=jpcoar\&amp;identifier=oai:weko3.ir.rcos.nii.ac.jp:00088854"/>
    <dc:publisher xml:lang="ja">琉球大学21世紀プログラム</dc:publisher>
    <dc:subject>ja\_Index B-5-1</dc:subject>
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

#### 更新履歴

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
  2023/08/31
  </td>
  <td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
  <td>初版作成</td>
  </tr>
  <tr class="even">
  <td>
  2023/11/14
  </td>
  <td>V0.9.27</td>
  <td></td>
  </tr>
    <tr class="even">
  <td>
  2025/2/14
  </td>
  <td></td>
  <td>タイトル完全一致検索、識別子による検索を追記</td>
  </tr>
  </tbody>
  </table>
