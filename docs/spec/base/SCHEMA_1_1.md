### Render

<!-- end list -->

#### 目的・用途

他のウェブアプリがweko3のリソースにアクセスできるようAPI利用を承認することを目的としている。

#### 利用方法

API-8-5の機能を用いて、OAuthアプリケーション、またはトークンを登録する。その後、設定された値を利用してAPI接続の設定を行う。


#### 構造

```
- meta_fix : アイテムタイプの定義上必須となっている固定プロパティの辞書
    - pubdate
        - title: "PubDate"
        - option: 
            - crtf: false,
            - hidden: false,
            - multiple: false,
            - required: true,
            - showlist: false
        - input_type: "datetime",
        - title_i18n: 
            - en: "PubDate",
            - ja: "公開日"
        - input_value: ""
- meta_list：アイテムタイプに含まれる固定プロパティ以外のプロパティの辞書
    - "item_1617186331708": {"title": "Title", "option": {"crtf": true, "hidden": false, "multiple": true, "required": true, "showlist": true}, "input_type": "cus_1001", "title_i18n": {"en": "Title", "ja": "タイトル"}, "input_value": "", "input_maxItems": "9999", "input_minItems": "1"}
- table_row：アイテムタイプの順序順プロパティ名のリスト
    -  ["item_1617186331708", "item_1617186385884",...]
- edit_notes
- meta_system
    - system_file": {
        - "title": "File Information",
        - "option": {
            - "crtf": false,
            - "hidden": true,
            - "oneline": false,
            - "multiple": false,
            - "required": false,
            - "showlist": false
        - "input_type": "cus_125",
        - "title_i18n": {
            - "en": "File Information",
            - "ja": "ファイル情報"
        - "input_value": ""
    - "system_identifier_doi": 
        - "title": "Persistent Identifier(DOI)",
        - "option": {
            - "crtf": false,
            - "hidden": true,
            - "oneline": false,
            - "multiple": false,
            - "required": false,
            - "showlist": false
        - "input_type": "cus_123",
        - "title_i18n": {
            - "en": "Persistent Identifier(DOI)",
            - "ja": "永続識別子（DOI）"
        - "input_value": ""
    - "system_identifier_hdl": {
        - "title": "Persistent Identifier(HDL)",
        - "option": {
            - "crtf": false,
            - "hidden": true,
            - "oneline": false,
            - "multiple": false,
            - "required": false,
            - "showlist": false
        - "input_type": "cus_123",
        - "title_i18n": {
            - "en": "Persistent Identifier(HDL)",
            - "ja": "永続識別子（HDL）"
        - "input_value": ""
    - "system_identifier_uri": {
        - "title": "Persistent Identifier(URI)",
        - "option": {
            - "crtf": false,
            - "hidden": true,
            - "oneline": false,
            - "multiple": false,
            - "required": false,
            - "showlist": false
        - "input_type": "cus_123",
        - "title_i18n": {
            - "en": "Persistent Identifier(URI)",
            - "ja": "永続識別子（URI）"
        - "input_value": ""
- upload_file：true or false.  使っていない？
- schemaeditor
    - schema
- table_row_map
    - form：アイテムタイプのJSON Form
    - name： アイテムタイプの名前
    - action： "upt"
    - schema：アイテムタイプのJSON Schema
        - type
        - "type": "object",
        - "$schema": "http://json-schema.org/draft-04/schema#",
        - "required": []
        - properties: {}
        - description: ""
    - mapping：プロパティのマッピング
        - system_identifier_doi": {
            - "ddi_mapping": {
                - "stdyDscr": {
                    - "citation": {
                        - "holdings": {
                            - "@attributes": {
                                - "URI": "subitem_systemidt_identifier"
            - "lom_mapping": "",
            - "lido_mapping": "",
            - "spase_mapping": "",
            - "jpcoar_mapping": {
                - "identifier": {
                    - "@value": "subitem_systemidt_identifier",
                    - "@attributes": {
                        - "identifierType": "subitem_systemidt_identifier_type"
            - "junii2_mapping": "",
            - "oai_dc_mapping": {
                - "identifier": {
                    - "@value": "subitem_systemidt_identifier"      
            - "display_lang_type": "",
            - "jpcoar_v1_mapping": {
                - "identifier": {
                    - "@value": "subitem_systemidt_identifier",
                        - "@attributes": {
                            - "identifierType": "subitem_systemidt_identifier_type"
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
