### アイテム検索用API

  - 目的・用途

アイテム検索機能を提供する。

  - 利用方法

| **Method** | **HTTP request**     | **Description** |
| ---------- | -------------------- | --------------- |
|            | **GET /api/records** | アイテムを検索する       |

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
<td>search_type</td>
<td></td>
<td><ul>
<li><p>0:フルテキスト</p></li>
<li><p>1:キーワード</p></li>
</ul></td>
<td><p>フルテキストを指定した場合は本文ファイルから抽出されたテキストも検索対象とする。</p>
<p>キーワードを指定した場合はメタデータ項目のみを検索対象とする。</p></td>
</tr>
<tr class="odd">
<td>q</td>
<td></td>
<td>string</td>
<td>検索キーワードを指定する。</td>
</tr>
<tr class="even">
<td>size</td>
<td></td>
<td>int</td>
<td>検索結果の件数を指定する</td>
</tr>
<tr class="odd">
<td>page</td>
<td></td>
<td>Int</td>
<td>検索結果で表示するページ番号を指定する。</td>
</tr>
<tr class="even">
<td>Sort</td>
<td></td>
<td><ul>
<li><p>+controlnumber</p></li>
<li><p>-controlnumber</p></li>
<li><p>+wtl</p></li>
<li><p>+wtl</p></li>
<li><p>+itemType</p></li>
<li><p>-itemType</p></li>
</ul>
<p>他</p></td>
<td>ソートキーを指定する。接頭辞「+」は昇順、「-」は降順となる。</td>
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
<tr class="odd">
<td><p>date_range1_from</p>
<p>date_range1_to</p></td>
<td></td>
<td>yyymmdd</td>
<td>dte_range1 に対して期間の範囲を指定して検索</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

レスポンス例：

<table>
<thead>
<tr class="header">
<th><strong>レスポンス例</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/api/records/?page=1&amp;size=1&amp;sort=controlnumber&amp;search_type=0&amp;q=%E6%A6%82%E8%A6%81</strong></td>
</tr>
<tr class="even">
<td><p>{</p>
<p>"aggregations": {</p>
<p>"Access": {</p>
<p>"buckets": [</p>
<p>{</p>
<p>"doc_count": 1761,</p>
<p>"key": "open access"</p>
<p>}</p>
<p>],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"Data Language": {</p>
<p>"buckets": [</p>
<p>{</p>
<p>"doc_count": 1761,</p>
<p>"key": "jpn"</p>
<p>}</p>
<p>],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"Data Type": {</p>
<p>"Data Type": {</p>
<p>"buckets": [],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"doc_count": 0</p>
<p>},</p>
<p>"Distributor": {</p>
<p>"Distributor": {</p>
<p>"buckets": [],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"doc_count": 0</p>
<p>},</p>
<p>"Location": {</p>
<p>"buckets": [</p>
<p>{</p>
<p>"doc_count": 1761,</p>
<p>"key": "Japan"</p>
<p>}</p>
<p>],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"Temporal": {</p>
<p>"buckets": [</p>
<p>{</p>
<p>"doc_count": 1761,</p>
<p>"key": "Temporal"</p>
<p>}</p>
<p>],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"Topic": {</p>
<p>"buckets": [</p>
<p>{</p>
<p>"doc_count": 1761,</p>
<p>"key": "Sibject1"</p>
<p>}</p>
<p>],</p>
<p>"doc_count_error_upper_bound": 0,</p>
<p>"sum_other_doc_count": 0</p>
<p>},</p>
<p>"path": {</p>
<p>"buckets": [],</p>
<p>"doc_count_error_upper_bound": "0",</p>
<p>"sum_order_doc_count": "0"</p>
<p>}</p>
<p>},</p>
<p>"hits": {</p>
<p>"hits": [</p>
<p>{</p>
<p>"created": "2023-11-06T05:43:58.044449+00:00",</p>
<p>"id": 1,</p>
<p>"links": {</p>
<p>"self": "https://dev.ir.rcos.nii.ac.jp/api/records/1"</p>
<p>},</p>
<p>"metadata": {</p>
<p>"_comment": [</p>
<p>"public-item-0-public-oai-guest-1-en",</p>
<p>"Source Title,1,111,12,1,3,en,2021-06-30",</p>
<p>"Conference Name",</p>
<p>"1",</p>
<p>"JPN",</p>
<p>"Sponsor",</p>
<p>"Conference Venue",</p>
<p>"Conference Place"</p>
<p>],</p>
<p>"_creator_info": [</p>
<p>{</p>
<p>"creatorAffiliations": [</p>
<p>{</p>
<p>"affiliationNameIdentifiers": [</p>
<p>{</p>
<p>"affiliationNameIdentifier": "0000000121691048",</p>
<p>"affiliationNameIdentifierScheme": "ISNI",</p>
<p>"affiliationNameIdentifierURI": "http://isni.org/isni/0000000121691048"</p>
<p>}</p>
<p>],</p>
<p>"affiliationNames": [</p>
<p>{</p>
<p>"affiliationName": "University",</p>
<p>"affiliationNameLang": "en"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>],</p>
<p>"creatorMails": [</p>
<p>{</p>
<p>"creatorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"creatorNames": {</p>
<p>"creatorName": "Joho\t Taro",</p>
<p>"creatorNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"familyNames": {</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"givenNames": {</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "4",</p>
<p>"nameIdentifierScheme": "WEKO"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "zzzzzzz",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>{</p>
<p>"creatorMails": [</p>
<p>{</p>
<p>"creatorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"creatorNames": {</p>
<p>"creatorName": "Joho\t Taro",</p>
<p>"creatorNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"familyNames": {</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"givenNames": {</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "zzzzzzz",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>{</p>
<p>"creatorMails": [</p>
<p>{</p>
<p>"creatorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"creatorNames": {</p>
<p>"creatorName": "Joho\t Taro",</p>
<p>"creatorNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"familyNames": {</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"givenNames": {</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "zzzzzzz",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>],</p>
<p>"_files_info": [</p>
<p>{</p>
<p>"extention": "pdf",</p>
<p>"label": "1KB.pdf",</p>
<p>"url": "https://weko3.example.org/record/1/files/1KB.pdf"</p>
<p>}</p>
<p>],</p>
<p>"_item_metadata": {</p>
<p>"author_link": [</p>
<p>"4"</p>
<p>],</p>
<p>"control_number": "1",</p>
<p>"item_1617186331708": {</p>
<p>"attribute_name": "Title",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_title": "public-item-0-public-oai-guest-1-ja",</p>
<p>"subitem_title_language": "ja"</p>
<p>},</p>
<p>{</p>
<p>"subitem_title": "public-item-0-public-oai-guest-1-en",</p>
<p>"subitem_title_language": "en"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186385884": {</p>
<p>"attribute_name": "Alternative Title",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_alternative_title": "Alternative Title",</p>
<p>"subitem_alternative_title_language": "en"</p>
<p>},</p>
<p>{</p>
<p>"subitem_alternative_title": "Alternative Title",</p>
<p>"subitem_alternative_title_language": "ja"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186419668": {</p>
<p>"attribute_name": "Creator",</p>
<p>"attribute_type": "creator",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"creatorAffiliations": [</p>
<p>{</p>
<p>"affiliationNameIdentifiers": [</p>
<p>{</p>
<p>"affiliationNameIdentifier": "0000000121691048",</p>
<p>"affiliationNameIdentifierScheme": "ISNI",</p>
<p>"affiliationNameIdentifierURI": "http://isni.org/isni/0000000121691048"</p>
<p>}</p>
<p>],</p>
<p>"affiliationNames": [</p>
<p>{</p>
<p>"affiliationName": "University",</p>
<p>"affiliationNameLang": "en"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>],</p>
<p>"creatorMails": [</p>
<p>{</p>
<p>"creatorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"creatorNames": {</p>
<p>"creatorName": "Joho\t Taro",</p>
<p>"creatorNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"familyNames": {</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"givenNames": {</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "4",</p>
<p>"nameIdentifierScheme": "WEKO"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "zzzzzzz",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>{</p>
<p>"creatorMails": [</p>
<p>{</p>
<p>"creatorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"creatorNames": {</p>
<p>"creatorName": "Joho\t Taro",</p>
<p>"creatorNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"familyNames": {</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"givenNames": {</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "zzzzzzz",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>{</p>
<p>"creatorMails": [</p>
<p>{</p>
<p>"creatorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"creatorNames": {</p>
<p>"creatorName": "Joho\t Taro",</p>
<p>"creatorNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"familyNames": {</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"givenNames": {</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en",</p>
<p>"idx": 2</p>
<p>},</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "zzzzzzz",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186476635": {</p>
<p>"attribute_name": "Access Rights",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_access_right": "open access",</p>
<p>"subitem_access_right_uri": "http://purl.org/coar/access_right/c_abf2"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186499011": {</p>
<p>"attribute_name": "Rights",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_rights": "Rights Information",</p>
<p>"subitem_rights_language": "ja",</p>
<p>"subitem_rights_resource": "http://localhost"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186609386": {</p>
<p>"attribute_name": "Subject",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_subject": "Sibject1",</p>
<p>"subitem_subject_language": "ja",</p>
<p>"subitem_subject_scheme": "Other",</p>
<p>"subitem_subject_uri": "http://localhost/"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186626617": {</p>
<p>"attribute_name": "Description",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_description": "Description\nDescription\nDescription",</p>
<p>"subitem_description_language": "en",</p>
<p>"subitem_description_type": "Abstract"</p>
<p>},</p>
<p>{</p>
<p>"subitem_description": "概要\n概要\n概要\n概要",</p>
<p>"subitem_description_language": "ja",</p>
<p>"subitem_description_type": "Abstract"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186643794": {</p>
<p>"attribute_name": "Publisher",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_publisher": "en",</p>
<p>"subitem_publisher_languag": "Publisher"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186660861": {</p>
<p>"attribute_name": "Date",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_date_issued_datetime": "2021-06-30",</p>
<p>"subitem_date_issued_type": "Available"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186702042": {</p>
<p>"attribute_name": "Language",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_language": "jpn"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186783814": {</p>
<p>"attribute_name": "Identifier",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_identifier_type": "URI",</p>
<p>"subitem_identifier_uri": "http://localhost"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186859717": {</p>
<p>"attribute_name": "Temporal",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_temporal_languag": "en",</p>
<p>"subitem_temporal_text": "Temporal"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186882738": {</p>
<p>"attribute_name": "Geo Location",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_geolocation_place": [</p>
<p>{</p>
<p>"subitem_geolocation_place_text": "Japan"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186901218": {</p>
<p>"attribute_name": "Funding Reference",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_award_numbers": {</p>
<p>"subitem_award_number": "Award Number",</p>
<p>"subitem_award_uri": "Award URI"</p>
<p>},</p>
<p>"subitem_award_titles": [</p>
<p>{</p>
<p>"subitem_award_title": "Award Title",</p>
<p>"subitem_award_title_language": "en"</p>
<p>}</p>
<p>],</p>
<p>"subitem_funder_identifiers": {</p>
<p>"subitem_funder_identifier": "http://xxx",</p>
<p>"subitem_funder_identifier_type": "ISNI"</p>
<p>},</p>
<p>"subitem_funder_names": [</p>
<p>{</p>
<p>"subitem_funder_name": "Funder Name",</p>
<p>"subitem_funder_name_language": "en"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186920753": {</p>
<p>"attribute_name": "Source Identifier",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_source_identifier": "xxxx-xxxx-xxxx",</p>
<p>"subitem_source_identifier_type": "ISSN"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186941041": {</p>
<p>"attribute_name": "Source Title",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_record_name": "Source Title",</p>
<p>"subitem_record_name_languag": "en"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186959569": {</p>
<p>"attribute_name": "Volume Number",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_volume": "1"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186981471": {</p>
<p>"attribute_name": "Issue Number",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_issue": "111"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617186994930": {</p>
<p>"attribute_name": "Number of Pages",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_number_of_pages": "12"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617187024783": {</p>
<p>"attribute_name": "Page Start",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_start_page": "1"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617187045071": {</p>
<p>"attribute_name": "Page End",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_end_page": "3"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617187112279": {</p>
<p>"attribute_name": "Degree Name",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_degreename": "en",</p>
<p>"subitem_issue": "Degree Name"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617187136212": {</p>
<p>"attribute_name": "Date Granted",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_dategranted": "2021-06-30"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617187187528": {</p>
<p>"attribute_name": "Conference",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_conference_country": "JPN",</p>
<p>"subitem_conference_date": {</p>
<p>"subitem_conference_date_language": "ja",</p>
<p>"subitem_conference_end_day": "1",</p>
<p>"subitem_conference_end_month": "12",</p>
<p>"subitem_conference_end_year": "2020",</p>
<p>"subitem_conference_period": "2020/12/11",</p>
<p>"subitem_conference_start_day": "1",</p>
<p>"subitem_conference_start_month": "12",</p>
<p>"subitem_conference_start_year": "2000"</p>
<p>},</p>
<p>"subitem_conference_names": [</p>
<p>{</p>
<p>"subitem_conference_name": "Conference Name",</p>
<p>"subitem_conference_name_language": "ja"</p>
<p>}</p>
<p>],</p>
<p>"subitem_conference_places": [</p>
<p>{</p>
<p>"subitem_conference_place": "Conference Place",</p>
<p>"subitem_conference_place_language": "ja"</p>
<p>}</p>
<p>],</p>
<p>"subitem_conference_sequence": "1",</p>
<p>"subitem_conference_sponsors": [</p>
<p>{</p>
<p>"subitem_conference_sponsor": "Sponsor",</p>
<p>"subitem_conference_sponsor_language": "ja"</p>
<p>}</p>
<p>],</p>
<p>"subitem_conference_venues": [</p>
<p>{</p>
<p>"subitem_conference_venue": "Conference Venue",</p>
<p>"subitem_conference_venue_language": "ja"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617258105262": {</p>
<p>"attribute_name": "Resource Type",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"resourcetype": "conference paper",</p>
<p>"resourceuri": "http://purl.org/coar/resource_type/c_5794"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617265215918": {</p>
<p>"attribute_name": "Version Type",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_version_resource": "http://purl.org/coar/version/c_b1a7d7d4d402bcce",</p>
<p>"subitem_version_type": "AO"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617349709064": {</p>
<p>"attribute_name": "Contributor",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"contributorMails": [</p>
<p>{</p>
<p>"contributorMail": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"contributorNames": [</p>
<p>{</p>
<p>"contributorName": "情報, 太郎",</p>
<p>"lang": "ja"</p>
<p>},</p>
<p>{</p>
<p>"contributorName": "ジョウホウ\t タロウ",</p>
<p>"lang": "ja-Kana"</p>
<p>},</p>
<p>{</p>
<p>"contributorName": "Joho\t Taro",</p>
<p>"lang": "en"</p>
<p>}</p>
<p>],</p>
<p>"contributorType": "ContactPerson",</p>
<p>"familyNames": [</p>
<p>{</p>
<p>"familyName": "情報",</p>
<p>"familyNameLang": "ja"</p>
<p>},</p>
<p>{</p>
<p>"familyName": "ジョウホウ",</p>
<p>"familyNameLang": "ja-Kana"</p>
<p>},</p>
<p>{</p>
<p>"familyName": "Joho",</p>
<p>"familyNameLang": "en"</p>
<p>}</p>
<p>],</p>
<p>"givenNames": [</p>
<p>{</p>
<p>"givenName": "太郎",</p>
<p>"givenNameLang": "ja"</p>
<p>},</p>
<p>{</p>
<p>"givenName": "タロウ",</p>
<p>"givenNameLang": "ja-Kana"</p>
<p>},</p>
<p>{</p>
<p>"givenName": "Taro",</p>
<p>"givenNameLang": "en"</p>
<p>}</p>
<p>],</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "CiNii",</p>
<p>"nameIdentifierURI": "https://ci.nii.ac.jp/"</p>
<p>},</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxxx",</p>
<p>"nameIdentifierScheme": "KAKEN2",</p>
<p>"nameIdentifierURI": "https://kaken.nii.ac.jp/"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617349808926": {</p>
<p>"attribute_name": "Version",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_version": "Version"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617351524846": {</p>
<p>"attribute_name": "APC",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_apc": "Unknown"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617353299429": {</p>
<p>"attribute_name": "Relation",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_relation_name": [</p>
<p>{</p>
<p>"subitem_relation_name_language": "en",</p>
<p>"subitem_relation_name_text": "Related Title"</p>
<p>}</p>
<p>],</p>
<p>"subitem_relation_type": "isVersionOf",</p>
<p>"subitem_relation_type_id": {</p>
<p>"subitem_relation_type_id_text": "xxxxx",</p>
<p>"subitem_relation_type_select": "arXiv"</p>
<p>}</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617605131499": {</p>
<p>"attribute_name": "File",</p>
<p>"attribute_type": "file",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"accessrole": "open_access",</p>
<p>"date": [</p>
<p>{</p>
<p>"dateType": "Available",</p>
<p>"dateValue": "2021-07-12"</p>
<p>}</p>
<p>],</p>
<p>"displaytype": "simple",</p>
<p>"filename": "1KB.pdf",</p>
<p>"filesize": [</p>
<p>{</p>
<p>"value": "1 KB"</p>
<p>}</p>
<p>],</p>
<p>"format": "text/plain",</p>
<p>"mimetype": "application/pdf",</p>
<p>"url": {</p>
<p>"url": "https://dev.ir.rcos.nii.ac.jp/record/1/files/1KB.pdf"</p>
<p>},</p>
<p>"version_id": "b1a73fe7-5325-4819-953b-722518118e3d"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617610673286": {</p>
<p>"attribute_name": "Rights Holder",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"nameIdentifiers": [</p>
<p>{</p>
<p>"nameIdentifier": "xxxxxx",</p>
<p>"nameIdentifierScheme": "ORCID",</p>
<p>"nameIdentifierURI": "https://orcid.org/"</p>
<p>}</p>
<p>],</p>
<p>"rightHolderNames": [</p>
<p>{</p>
<p>"rightHolderLanguage": "ja",</p>
<p>"rightHolderName": "Right Holder Name"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617620223087": {</p>
<p>"attribute_name": "Heading",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_heading_banner_headline": "Banner Headline",</p>
<p>"subitem_heading_headline": "Subheading",</p>
<p>"subitem_heading_language": "ja"</p>
<p>},</p>
<p>{</p>
<p>"subitem_heading_banner_headline": "Banner Headline",</p>
<p>"subitem_heading_headline": "Subheding",</p>
<p>"subitem_heading_language": "en"</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_1617944105607": {</p>
<p>"attribute_name": "Degree Grantor",</p>
<p>"attribute_value_mlt": [</p>
<p>{</p>
<p>"subitem_degreegrantor": [</p>
<p>{</p>
<p>"subitem_degreegrantor_language": "en",</p>
<p>"subitem_degreegrantor_name": "Degree Grantor Name"</p>
<p>}</p>
<p>],</p>
<p>"subitem_degreegrantor_identifie": [</p>
<p>{</p>
<p>"subitem_degreegrantor_identifier_name": "xxxxxx",</p>
<p>"subitem_degreegrantor_identifier_scheme": "kakenhi"</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>},</p>
<p>"item_title": "public-item-0-public-oai-guest-1-ja",</p>
<p>"item_type_id": "15",</p>
<p>"owner": "1",</p>
<p>"path": [</p>
<p>"1"</p>
<p>],</p>
<p>"pubdate": {</p>
<p>"attribute_name": "PubDate",</p>
<p>"attribute_value": "2021-11-20"</p>
<p>},</p>
<p>"publish_date": "2021-11-20",</p>
<p>"publish_status": "0",</p>
<p>"relation_version_is_last": true,</p>
<p>"title": [</p>
<p>"public-item-0-public-oai-guest-1-ja"</p>
<p>],</p>
<p>"weko_shared_id": -1</p>
<p>},</p>
<p>"_oai": {</p>
<p>"id": "oai:weko3.example.org:00000001",</p>
<p>"sets": [</p>
<p>"1"</p>
<p>]</p>
<p>},</p>
<p>"accessRights": [</p>
<p>"open access"</p>
<p>],</p>
<p>"alternative": [</p>
<p>"Alternative Title",</p>
<p>"Alternative Title"</p>
<p>],</p>
<p>"apc": [</p>
<p>"Unknown"</p>
<p>],</p>
<p>"author_link": [</p>
<p>"4"</p>
<p>],</p>
<p>"conference": {</p>
<p>"conferenceCountry": [</p>
<p>"JPN"</p>
<p>],</p>
<p>"conferenceDate": [</p>
<p>"2020/12/11"</p>
<p>],</p>
<p>"conferenceName": [</p>
<p>"Conference Name"</p>
<p>],</p>
<p>"conferenceSequence": [</p>
<p>"1"</p>
<p>],</p>
<p>"conferenceSponsor": [</p>
<p>"Sponsor"</p>
<p>],</p>
<p>"conferenceVenue": [</p>
<p>"Conference Venue"</p>
<p>]</p>
<p>},</p>
<p>"contributor": {</p>
<p>"@attributes": {</p>
<p>"contributorType": [</p>
<p>[</p>
<p>"ContactPerson"</p>
<p>]</p>
<p>]</p>
<p>},</p>
<p>"affiliation": {</p>
<p>"affiliationName": [],</p>
<p>"nameIdentifier": []</p>
<p>},</p>
<p>"contributorAlternative": [],</p>
<p>"contributorName": [</p>
<p>"情報, 太郎",</p>
<p>"ジョウホウ\t タロウ",</p>
<p>"Joho\t Taro"</p>
<p>],</p>
<p>"familyName": [</p>
<p>"情報",</p>
<p>"ジョウホウ",</p>
<p>"Joho"</p>
<p>],</p>
<p>"givenName": [</p>
<p>"太郎",</p>
<p>"タロウ",</p>
<p>"Taro"</p>
<p>],</p>
<p>"nameIdentifier": [</p>
<p>"xxxxxxx",</p>
<p>"xxxxxxx",</p>
<p>"xxxxxxx"</p>
<p>]</p>
<p>},</p>
<p>"control_number": "1",</p>
<p>"creator": {</p>
<p>"affiliation": {</p>
<p>"affiliationName": [</p>
<p>"University"</p>
<p>],</p>
<p>"nameIdentifier": [</p>
<p>"0000000121691048"</p>
<p>]</p>
<p>},</p>
<p>"creatorAlternative": [],</p>
<p>"creatorName": [</p>
<p>"情報, 太郎",</p>
<p>"ジョウホウ\t タロウ",</p>
<p>"Joho\t Taro",</p>
<p>"情報, 太郎",</p>
<p>"ジョウホウ\t タロウ",</p>
<p>"Joho\t Taro",</p>
<p>"情報, 太郎",</p>
<p>"ジョウホウ\t タロウ",</p>
<p>"Joho\t Taro"</p>
<p>],</p>
<p>"familyName": [</p>
<p>"情報",</p>
<p>"ジョウホウ",</p>
<p>"Joho",</p>
<p>"情報",</p>
<p>"ジョウホウ",</p>
<p>"Joho",</p>
<p>"情報",</p>
<p>"ジョウホウ",</p>
<p>"Joho"</p>
<p>],</p>
<p>"givenName": [</p>
<p>"太郎",</p>
<p>"タロウ",</p>
<p>"Taro",</p>
<p>"太郎",</p>
<p>"タロウ",</p>
<p>"Taro",</p>
<p>"太郎",</p>
<p>"タロウ",</p>
<p>"Taro"</p>
<p>],</p>
<p>"nameIdentifier": [</p>
<p>"4",</p>
<p>"xxxxxxx",</p>
<p>"xxxxxxx",</p>
<p>"zzzzzzz",</p>
<p>"xxxxxxx",</p>
<p>"xxxxxxx",</p>
<p>"zzzzzzz",</p>
<p>"xxxxxxx",</p>
<p>"xxxxxxx",</p>
<p>"zzzzzzz"</p>
<p>]</p>
<p>},</p>
<p>"date": [</p>
<p>{</p>
<p>"dateType": "Available",</p>
<p>"value": "2021-06-30"</p>
<p>}</p>
<p>],</p>
<p>"dateGranted": [</p>
<p>"2021-06-30"</p>
<p>],</p>
<p>"degreeGrantor": {</p>
<p>"degreeGrantorName": [</p>
<p>"Degree Grantor Name"</p>
<p>],</p>
<p>"nameIdentifier": [</p>
<p>"xxxxxx"</p>
<p>]</p>
<p>},</p>
<p>"degreeName": [</p>
<p>"en"</p>
<p>],</p>
<p>"description": [</p>
<p>{</p>
<p>"descriptionType": "Abstract",</p>
<p>"value": "Description\nDescription\nDescription"</p>
<p>},</p>
<p>{</p>
<p>"descriptionType": "Abstract",</p>
<p>"value": "概要\n概要\n概要\n概要"</p>
<p>}</p>
<p>],</p>
<p>"feedback_mail_list": [</p>
<p>{</p>
<p>"author_id": "",</p>
<p>"email": "wekosoftware@nii.ac.jp"</p>
<p>}</p>
<p>],</p>
<p>"fundingReference": {</p>
<p>"awardNumber": [</p>
<p>"Award Number"</p>
<p>],</p>
<p>"awardTitle": [</p>
<p>"Award Title"</p>
<p>],</p>
<p>"funderIdentifier": [</p>
<p>"http://xxx"</p>
<p>],</p>
<p>"funderName": [</p>
<p>"Funder Name"</p>
<p>]</p>
<p>},</p>
<p>"geoLocation": {</p>
<p>"geoLocationPlace": [</p>
<p>"Japan"</p>
<p>]</p>
<p>},</p>
<p>"identifier": [</p>
<p>{</p>
<p>"identifierType": "URI",</p>
<p>"value": "http://localhost"</p>
<p>}</p>
<p>],</p>
<p>"issue": [</p>
<p>"111"</p>
<p>],</p>
<p>"itemtype": "デフォルトアイテムタイプ（フル）",</p>
<p>"language": [</p>
<p>"jpn"</p>
<p>],</p>
<p>"numPages": [</p>
<p>"12"</p>
<p>],</p>
<p>"pageEnd": [</p>
<p>"3"</p>
<p>],</p>
<p>"pageStart": [</p>
<p>"1"</p>
<p>],</p>
<p>"path": [</p>
<p>"1"</p>
<p>],</p>
<p>"publish_date": "2021-11-20",</p>
<p>"publish_status": "0",</p>
<p>"publisher": [</p>
<p>"Publisher"</p>
<p>],</p>
<p>"relation": {</p>
<p>"@attributes": {</p>
<p>"relationType": [</p>
<p>[</p>
<p>"isVersionOf"</p>
<p>]</p>
<p>]</p>
<p>},</p>
<p>"relatedIdentifier": [</p>
<p>{</p>
<p>"identifierType": "arXiv",</p>
<p>"value": "xxxxx"</p>
<p>}</p>
<p>],</p>
<p>"relatedTitle": [</p>
<p>"Related Title"</p>
<p>]</p>
<p>},</p>
<p>"relation_version_is_last": true,</p>
<p>"rights": [</p>
<p>"Rights Information"</p>
<p>],</p>
<p>"rightsHolder": {</p>
<p>"nameIdentifier": [</p>
<p>"xxxxxx"</p>
<p>],</p>
<p>"rightsHolderName": [</p>
<p>"Right Holder Name"</p>
<p>]</p>
<p>},</p>
<p>"sourceIdentifier": [</p>
<p>{</p>
<p>"identifierType": "ISSN",</p>
<p>"value": "xxxx-xxxx-xxxx"</p>
<p>}</p>
<p>],</p>
<p>"sourceTitle": [</p>
<p>"Source Title"</p>
<p>],</p>
<p>"subject": [</p>
<p>{</p>
<p>"subjectScheme": "Other",</p>
<p>"value": "Sibject1"</p>
<p>}</p>
<p>],</p>
<p>"temporal": [</p>
<p>"Temporal"</p>
<p>],</p>
<p>"title": [</p>
<p>"public-item-0-public-oai-guest-1-en",</p>
<p>"public-item-0-public-oai-guest-1-ja"</p>
<p>],</p>
<p>"type": [</p>
<p>"conference paper"</p>
<p>],</p>
<p>"version": [</p>
<p>"Version"</p>
<p>],</p>
<p>"versiontype": [</p>
<p>"AO"</p>
<p>],</p>
<p>"volume": [</p>
<p>"1"</p>
<p>],</p>
<p>"weko_creator_id": "1",</p>
<p>"weko_shared_id": -1</p>
<p>},</p>
<p>"updated": "2023-11-15T02:46:32.217662+00:00"</p>
<p>}</p>
<p>],</p>
<p>"total": 1761</p>
<p>},</p>
<p>"links": {</p>
<p>"next": "https://dev.ir.rcos.nii.ac.jp/api/records/?page=2&amp;q=%E6%A6%82%E8%A6%81&amp;size=1",</p>
<p>"self": "https://dev.ir.rcos.nii.ac.jp/api/records/?page=1&amp;q=%E6%A6%82%E8%A6%81&amp;size=1"</p>
<p>}</p>
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
<td>〇</td>
<td>〇</td>
<td>〇</td>
<td>〇</td>
<td>〇</td>
<td>〇</td>
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
</tbody>
</table>