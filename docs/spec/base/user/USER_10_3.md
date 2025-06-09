# ワークスペース：メタデータ自動補完機能

## 目的・用途

指定されたDOIをキーに外部サービスからメタデータを取得し、メタデータ入力の自動補完を行う。

## 利用方法

* ワークスペース（WorkSpace）の簡易登録画面にてDOIを入力し「取得」ボタンを押下する。
* [SWORD API JSON-LD](../admin/ADMIN_16_2.md)
* [RO-Crate インポート](../admin/ADMIN_2_5.md#メタデータ補完機能)

## 利用可能なロール

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
<td></td>
</tr>
</tbody>
</table>

## 機能内容

### CrossRef APIからのメタデータ取得

  - CrossRef APIからのメタデータ取得する際は事前に「CrossRefクエリサービスアカウント」の設定が必要。
    - 参照： [WebAPIアカウント](../admin/ADMIN_14_17.md) 

  - 機能については [Item Registration：メタデータ入力](./USER_4_6.md) の [2. アイテムのメタデータを自動入力できる > CrossRef API経由でアイテムメタデータを入力する] の項目参照

---

### CiNii Research APIからのメタデータ取得

  - WEB API リクエスト  
    ※ API仕様： https://support.nii.ac.jp/ja/cir/r_opensearch
    - リクエストURL  
      https://cir.nii.ac.jp/opensearch/all?doi={doi}&format=json
    - method  
      GET
    - パラメータ  
      | パラメーター名 | 説明 | 値 |
      | ----- | ----- | ----- |
      | doi | 検索するDOI | {doi}: 入力されたDOI
      | format | レスポンス形式 | 「json」固定とする

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される  
    
      取得データの入力先メタデータ項目
      | **データ** | **パス** | **対応するJPCOARマッピング** |
      | --------- | -------- | --------------------------- |
      | タイトル      | dc:title                                        | dc:title                              |
      | 別タイトル     | dcterms:alternative                             | dc:title                              |
      | 成果物識別子    | productIdentifier.identifier(type=xx)           | jpcoar:relation                       |
      | 著者名       | creator.foaf:name                               | jpcoar:creatorName                            |
      | 著者識別子     | creator.personIdentifier                        |                                       |
      | 著者所属名     | creator.jpcoar:affiliationName                  |                                       |
      | 寄与者名      | contributor.foaf:name                           | jpcoar:contributorName |
      | 寄与者所属名    | contributor.jpcoar:affiliationName              |                                       |
      | 寄与者識別子    | contributor.personIdentifier                    |                                       |
      | 収録物識別子    | publication.publicationidentifier               |                                       |
      | 収録物名      | publication.prism:publicationName               | jpcoar:sourceTitle                 |
      | 収録物発行日    | publication.prism:publicationDate               |                                       |
      | 巻         | publication.prism:volume                        | jpcoar:volume                          |
      | 号         | publication.prism:number                        | jpcoar:issue                          |
      | 開始ページ     | publication.prism:startingPage                  | jpcoar:pageStart                    |
      | 終了ページ     | publication.prism:endingPage                    | jpcoar:pageEnd                      |
      | 総ページ数     | publication.jpcoar:numPages                     | jpcoar:numPages                       |
      | 発行者       | publication.dc:publisher                        | dc:publisher                          |
      | 日付        | publication.prism:publicationDate               | datacite:date               |
      | 収録誌のNCID  | publication.publicationIdentifier(@type=NCID)   |jpcoar:sourceIdentifier                            |
      | 収録誌のISSN  | publication.publicationIdentifier(@type=ISSN)   | jpcoar:sourceIdentifier                            |
      | 学位授与番号    | ndl:dissertationNumber                          |                                       |
      | 学位名       | ndl:degreeName                                  |                                       |
      | 学位授与年月日   | ndl:dateGranted                                 |                                       |
      | 学位授与機関識別子 | degreeAwardInstitution.institutionIdentifier    |                                       |
      | 学位授与機関名   | degreeAwardInstitution.jpcoar:degreeGrantorName |                                       |
      | 学会、会議名    | jpcoar:conferenceName                           |                                       |
      | 開催地       | jpcoar:conferencePlace                          |                                       |
      | 開催期間(開始日) | jpcoar:conferenceDate.jpcoar:startDay           |                                       |
      | 開催期間(開始月) | jpcoar:conferenceDate.jpcoar:startMonth         |                                       |
      | 開催期間(開始年) | jpcoar:conferenceDate.jpcoar:startYear          |                                       |
      | 開催期間(終了日) | jpcoar:conferenceDate.jpcoar:endDay             |                                       |
      | 開催期間(終了月) | jpcoar:conferenceDate.jpcoar:endDay             |                                       |
      | 開催期間(終了年) | jpcoar:conferenceDate.jpcoar:endDay             |                                       |
      | 助成機関名     | fundingProgram.notation                         |                                       |
      | 関連物関連タイプ  | relatedProduct.relationType                     |                                       |
      | 関連物識別子    | relatedProduct.productIdentifier                |                                       |
      | 関連物タイトル   | relatedProduct.jpcoar:relatedTitle              |                                       |
      | 抄録タイプ     | description.type                                | typeはAbstraction固定                    |
      | 抄録本文      | description.notation                            | dc:description                        |
      | 主題URL     | foaf:topic.@id                                  | jpcoar:subject                        |
      | 主題タイトル    | foaf:topic.dc:title                             | jpcoar:subject                        |
      | バージョン     | datacite:version                                |                                       |
      | 言語        | dc:language                                     |                                       |

---

### Jalc APIからのメタデータ取得

  - WEB API リクエスト  
    ※ API仕様： https://japanlinkcenter.org/top/doc/REST_API_Functional_Description.pdf
    - リクエストURL  
      https://api.japanlinkcenter.org/dois/{doi}
    - method  
      GET
    - パラメータ  
      | パラメーター名 | 説明 | 値 |
      | ----- | ----- | ----- |
      | doi | 検索するDOI | {doi}: 入力されたDOIをURLエンコードした文字列

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される

      取得データの入力先メタデータ項目
      | **データ** | **パス** | **対応するJPCOARマッピング** |
      | --------- | -------- | --------------------------- |
      | タイトル      | title                                        | dc:title                              |
      | 著者名       | creator                                           | jpcoar:creatorName                    |
      | 著者所属名     | affiliation                                     | jpcoar:affiliationName                |
      | 寄与者名      | creator                                          | jpcoar:contributorName                |
      | 寄与者所属名    | affiliationName                                |jpcoar:affiliationName                 |
      | 収録物名      | journal_title_name                               | jpcoar:sourceTitle                 |
      | 収録物発行日    | date                                           | date(dateType="Issued")             |
      | 巻         | volume                                             | jpcoar:volume                          |
      | 号         | issue                                              | jpcoar:issue                          |
      | 開始ページ     | first_page                                      | jpcoar:pageStart                    |
      | 終了ページ     | last_page                                       | jpcoar:pageEnd                      |
      | 日付        | date                                               | datacite:date                      |
      | 収録誌のISSN  | journal_id_type                                  | jpcoar:sourceIdentifier             |

---

### DataCite APIからのメタデータ取得

  - WEB API リクエスト  
    ※ API仕様： https://support.datacite.org/docs/api
    - リクエストURL  
      https://api.datacite.org/dois/{id}
    - method  
      GET
    - パラメータ  
      | パラメーター名 | 説明 | 値 |
      | ----- | ----- | ----- |
      | doi | 検索するDOI | {doi}: 入力されたDOI

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される

      取得データの入力先メタデータ項目
      | **データ** | **パス** | **対応するJPCOARマッピング** |
      | --------- | -------- | --------------------------- |
      | タイトル      | title                                        | dc:title                              |
      | 著者名       | creator                                           | jpcoar:creatorName                    |
      | 著者所属名     | affiliation                                     | jpcoar:affiliationName                |
      | 寄与者名      | creator                                          | jpcoar:contributorName                |
      | 寄与者所属名    | affiliationName                                |jpcoar:affiliationName                 |
      | 識別子      | doi                               　　　　　　　　　| jpcoar:identifier                 　　|
      | 日付        | date                                               | datacite:date                      |
      | 会議名      | fundingReferences                                  | jpcoar:fundingReference             |
      | 関連識別子   | relationships_type                              | jpcoar:relatedIdentifier(identifierType="DOI")    |
      | 権利　      | rights                                              | jpcoar:rights                      |
      | バージョン   | version                                             | jpcoar:edition                    |

### 医中誌Web APIからのメタデータ取得

  - SRUによるメタデータ取得を行う
  - 医中誌WebAPI利用には事前申請が必要。ログイン時にID/PWもしくはIPアドレスによる認証が行われるが、本機能はIPアドレスによる認証を前提とする。（現時点でID/PW認証には未対応）
  - WEB API リクエスト  
    ※ API仕様： https://www.jamas.or.jp/service/service_o/api.html

    - ログイン
      - リクエストURL  
      https://search.jamas.or.jp/api/login
      - method  
        POST
      - パラメータ  
        なし
      
      認証に成功すると cookie が生成されるので保持する。  
      (cookie の名称は"JamasSecInfo"、値は22byteの数字)

    - メタデータ取得  
      ※ログイン時に取得した cookie をhttp ヘッダにセットしてリクエストする。
      - リクエストURL  
      https://search.jamas.or.jp/api/sru?operation=searchRetrieve&version=1.2&startRecord=1&recordPacking=xml&recordSchema=pam&query={query}
      - method  
        GET
      - パラメータ  
        | パラメーター名 | 説明 | 値 |
        | ----- | ----- | ----- |
        | operation | 操作種別 | SRUの場合は「searchRetrieve」固定
        | version | バージョン | 「1.2」固定とする
        | startRecord | 開始位置 | 「1」固定とする
        | recordPacking | レスポンス形式 | 「xml」固定とする
        | recordSchema | 取得データスキーマ | 「pam」固定とする
        | query | 検索式 | {query}: 「prism.doi={doi}」をURLエンコードした文字列<br>  * {doi}: 入力されたDOI
    
    - ログアウト  
      ※ログイン時に取得した cookie をhttp ヘッダにセットしてリクエストする。
      - リクエストURL  
      https://search.jamas.or.jp/api/logout
      - method  
        POST
      - パラメータ  
        なし

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される

      取得データの入力先メタデータ項目
      | **データ** | **パス** | **対応するJPCOARマッピング** |
      | --------- | -------- | --------------------------- |
      | タイトル      | dc:title                                     | jpcoar:titleName                             |
      | 著者名       | dc:creator                                        | jpcoar:creatorName　　　                   |
      | 寄与者名      | dc:creator                                           | jpcoar:contributorName                |
      | 収録物名      | prism:publicationName                               | jpcoar:sourceTitle                 |
      | 収録物発行日    | prism:publicationDate                              | date(dateType="Issued")             |
      | 巻         | prism:volume                                             | jpcoar:volume                          |
      | 号         | prism:number                                            | jpcoar:issue                          |
      | 開始ページ     | prism:startingPage                                      | jpcoar:pageStart                    |
      | 総ページ数     | prism:pageRange                                     | jpcoar:numPages                       |
      | 日付        | prism:publicationDatee                                 | datacite:date                      |
      | 収録誌のISSN  | prism:issn                                          | jpcoar:sourceIdentifier             |
      | 関連識別子  | prism:doi                                             | jpcoar:relatedIdentifier(identifierType="DOI")             |


## 関連モジュール

  - weko-workspace
  - weko-items-ui
  - weko-items-autofill


## 処理概要

### CrossRef APIからのメタデータ取得

  * 「CrossRefクエリサービスアカウント」を api_certificateテーブルから取得する
    * 取得できない場合は CrossRef API へのリクエストは行わない。
  * CrossRef API からDOIに紐づくメタデータを取得する
    * `weko_items_autofill.api.CrossRefOpenURL.get_data()` を呼び出し、CrossRef API からデータを取得する
      * CrossRef API からはXML形式でレスポンスが返却される
    * 取得したAPIレスポンスを解析し、辞書型に整形する
    * アイテムタイプのJPCOARマッピングに応じた項目にメタデータを設定する

---

### CiNii Research APIからのメタデータ取得

  * CiNii Research API からDOIに紐づくメタデータを取得する
    * `weko_workspace.api.CiNiiURL.get_data()` を呼び出し、CiNii Research API からデータを取得する
      * CiNii Research API からはJSON形式でレスポンスが返却される
    * 取得したAPIレスポンスを解析し、辞書型に整形する
    * アイテムタイプのJPCOARマッピングに応じた項目にメタデータを設定する

---

### Jalc APIからのメタデータ取得

  * Jalc API からDOIに紐づくメタデータを取得する
    * `weko_workspace.api.JALCURL.get_data()` を呼び出し、Jalc API からデータを取得する
      * Jalc API からはJSON形式でレスポンスが返却される
    * 取得したAPIレスポンスを解析し、辞書型に整形する
    * アイテムタイプのJPCOARマッピングに応じた項目にメタデータを設定する

---

### DataCite APIからのメタデータ取得

  * DataCite API からDOIに紐づくメタデータを取得する
    * `weko_workspace.api.DATACITEURL.get_data()` を呼び出し、DataCite API からデータを取得する
      * DataCite API からはJSON形式でレスポンスが返却される
    * 取得したAPIレスポンスを解析し、辞書型に整形する
    * アイテムタイプのJPCOARマッピングに応じた項目にメタデータを設定する

### 医中誌Web APIからのメタデータ取得

  * 医中誌Web API からDOIに紐づくメタデータを取得する
    * `weko_workspace.api.JamasURL.get_data()` を呼び出し、医中誌Web API からデータを取得する
      * データ取得前に医中誌WebのログインAPIを呼び出し、cookie を受け取る
      * 医中誌Web API にメタデータ取得リクエストを送信する
        * XML形式でレスポンスが返却される
      * レスポンス取得後はログアウトAPIを呼びだす
    * 取得したAPIレスポンスを解析し、辞書型に整形する
    * アイテムタイプのJPCOARマッピングに応じた項目にメタデータを設定する


## 更新履歴

|日付|GitHubコミットID|更新内容|
|---|---|---|
|2025/03/27|057e4d8985a4b5526c0db7f07f717a4bb45bc984|初版作成|

