# ワークスペース：メタデータ自動補完機能

## 目的・用途

指定されたDOIをキーに外部サービスからメタデータを取得し、メタデータ入力の自動補完を行う。

## 利用方法

* ワークスペース（WorkSpace）の簡易登録画面にてDOIを入力し「取得」ボタンを押下する。
* [SWORD API JSON-LD](../admin/ADMIN_16_2.md)
* [RO-Crate インポート](../admin/ADMIN_2_5.md#wkmetadataautofillメタデータ自動補完フラグ)

## 利用可能なロール

| ロール   | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:--------:|:--------------:|:----------------:|:------------------:|:------------:|:------------:|:-------------------:|
| 利用可否 | ○              | ○                | ○                  | ○            | ○            |                      |

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

      <table>
      <thead>
      <tr>
      <th>パラメーター名</th>
      <th>説明</th>
      <th>値</th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>doi</td>
      <td>検索するDOI</td>
      <td>{doi}: 入力されたDOI</td>
      </tr>
      <tr>
      <td>format</td>
      <td>レスポンス形式</td>
      <td>「json」固定とする</td>
      </tr>
      </tbody>
      </table>

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される  
    
      取得データの入力先メタデータ項目

      <table>
      <thead>
      <tr>
      <th><strong>データ</strong></th>
      <th><strong>パス</strong></th>
      <th><strong>対応するJPCOARマッピング</strong></th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>タイトル</td>
      <td>dc:title</td>
      <td>dc:title</td>
      </tr>
      <tr>
      <td>別タイトル</td>
      <td>dcterms:alternative</td>
      <td>dc:title</td>
      </tr>
      <tr>
      <td>成果物識別子</td>
      <td>productIdentifier.identifier(type=xx)</td>
      <td>jpcoar:relation</td>
      </tr>
      <tr>
      <td>著者名</td>
      <td>creator.foaf:name</td>
      <td>jpcoar:creatorName</td>
      </tr>
      <tr>
      <td>著者識別子</td>
      <td>creator.personIdentifier</td>
      <td></td>
      </tr>
      <tr>
      <td>著者所属名</td>
      <td>creator.jpcoar:affiliationName</td>
      <td></td>
      </tr>
      <tr>
      <td>寄与者名</td>
      <td>contributor.foaf:name</td>
      <td>jpcoar:contributorName</td>
      </tr>
      <tr>
      <td>寄与者所属名</td>
      <td>contributor.jpcoar:affiliationName</td>
      <td></td>
      </tr>
      <tr>
      <td>寄与者識別子</td>
      <td>contributor.personIdentifier</td>
      <td></td>
      </tr>
      <tr>
      <td>収録物識別子</td>
      <td>publication.publicationidentifier</td>
      <td></td>
      </tr>
      <tr>
      <td>収録物名</td>
      <td>publication.prism:publicationName</td>
      <td>jpcoar:sourceTitle</td>
      </tr>
      <tr>
      <td>収録物発行日</td>
      <td>publication.prism:publicationDate</td>
      <td></td>
      </tr>
      <tr>
      <td>巻</td>
      <td>publication.prism:volume</td>
      <td>jpcoar:volume</td>
      </tr>
      <tr>
      <td>号</td>
      <td>publication.prism:number</td>
      <td>jpcoar:issue</td>
      </tr>
      <tr>
      <td>開始ページ</td>
      <td>publication.prism:startingPage</td>
      <td>jpcoar:pageStart</td>
      </tr>
      <tr>
      <td>終了ページ</td>
      <td>publication.prism:endingPage</td>
      <td>jpcoar:pageEnd</td>
      </tr>
      <tr>
      <td>総ページ数</td>
      <td>publication.jpcoar:numPages</td>
      <td>jpcoar:numPages</td>
      </tr>
      <tr>
      <td>発行者</td>
      <td>publication.dc:publisher</td>
      <td>dc:publisher</td>
      </tr>
      <tr>
      <td>日付</td>
      <td>publication.prism:publicationDate</td>
      <td>datacite:date</td>
      </tr>
      <tr>
      <td>収録誌のNCID</td>
      <td>publication.publicationIdentifier(@type=NCID)</td>
      <td>jpcoar:sourceIdentifier</td>
      </tr>
      <tr>
      <td>収録誌のISSN</td>
      <td>publication.publicationIdentifier(@type=ISSN)</td>
      <td>jpcoar:sourceIdentifier</td>
      </tr>
      <tr>
      <td>学位授与番号</td>
      <td>ndl:dissertationNumber</td>
      <td></td>
      </tr>
      <tr>
      <td>学位名</td>
      <td>ndl:degreeName</td>
      <td></td>
      </tr>
      <tr>
      <td>学位授与年月日</td>
      <td>ndl:dateGranted</td>
      <td></td>
      </tr>
      <tr>
      <td>学位授与機関識別子</td>
      <td>degreeAwardInstitution.institutionIdentifier</td>
      <td></td>
      </tr>
      <tr>
      <td>学位授与機関名</td>
      <td>degreeAwardInstitution.jpcoar:degreeGrantorName</td>
      <td></td>
      </tr>
      <tr>
      <td>学会、会議名</td>
      <td>jpcoar:conferenceName</td>
      <td></td>
      </tr>
      <tr>
      <td>開催地</td>
      <td>jpcoar:conferencePlace</td>
      <td></td>
      </tr>
      <tr>
      <td>開催期間(開始日)</td>
      <td>jpcoar:conferenceDate.jpcoar:startDay</td>
      <td></td>
      </tr>
      <tr>
      <td>開催期間(開始月)</td>
      <td>jpcoar:conferenceDate.jpcoar:startMonth</td>
      <td></td>
      </tr>
      <tr>
      <td>開催期間(開始年)</td>
      <td>jpcoar:conferenceDate.jpcoar:startYear</td>
      <td></td>
      </tr>
      <tr>
      <td>開催期間(終了日)</td>
      <td>jpcoar:conferenceDate.jpcoar:endDay</td>
      <td></td>
      </tr>
      <tr>
      <td>開催期間(終了月)</td>
      <td>jpcoar:conferenceDate.jpcoar:endDay</td>
      <td></td>
      </tr>
      <tr>
      <td>開催期間(終了年)</td>
      <td>jpcoar:conferenceDate.jpcoar:endDay</td>
      <td></td>
      </tr>
      <tr>
      <td>助成機関名</td>
      <td>fundingProgram.notation</td>
      <td></td>
      </tr>
      <tr>
      <td>関連物関連タイプ</td>
      <td>relatedProduct.relationType</td>
      <td></td>
      </tr>
      <tr>
      <td>関連物識別子</td>
      <td>relatedProduct.productIdentifier</td>
      <td></td>
      </tr>
      <tr>
      <td>関連物タイトル</td>
      <td>relatedProduct.jpcoar:relatedTitle</td>
      <td></td>
      </tr>
      <tr>
      <td>抄録タイプ</td>
      <td>description.type</td>
      <td>typeはAbstraction固定</td>
      </tr>
      <tr>
      <td>抄録本文</td>
      <td>description.notation</td>
      <td>dc:description</td>
      </tr>
      <tr>
      <td>主題URL</td>
      <td>foaf:topic.@id</td>
      <td>jpcoar:subject</td>
      </tr>
      <tr>
      <td>主題タイトル</td>
      <td>foaf:topic.dc:title</td>
      <td>jpcoar:subject</td>
      </tr>
      <tr>
      <td>バージョン</td>
      <td>datacite:version</td>
      <td></td>
      </tr>
      <tr>
      <td>言語</td>
      <td>dc:language</td>
      <td></td>
      </tr>
      </tbody>
      </table>

---

### Jalc APIからのメタデータ取得

  - WEB API リクエスト  
    ※ API仕様： https://japanlinkcenter.org/top/doc/REST_API_Functional_Description.pdf
    - リクエストURL  
      https://api.japanlinkcenter.org/dois/{doi}
    - method  
      GET
    - パラメータ  

      <table>
      <thead>
      <tr>
      <th>パラメーター名</th>
      <th>説明</th>
      <th>値</th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>doi</td>
      <td>検索するDOI</td>
      <td>{doi}: 入力されたDOIをURLエンコードした文字列</td>
      </tr>
      </tbody>
      </table>

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される

      取得データの入力先メタデータ項目

      <table>
      <thead>
      <tr>
      <th><strong>データ</strong></th>
      <th><strong>パス</strong></th>
      <th><strong>対応するJPCOARマッピング</strong></th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>タイトル</td>
      <td>title</td>
      <td>dc:title</td>
      </tr>
      <tr>
      <td>著者名</td>
      <td>creator</td>
      <td>jpcoar:creatorName</td>
      </tr>
      <tr>
      <td>著者所属名</td>
      <td>affiliation</td>
      <td>jpcoar:affiliationName</td>
      </tr>
      <tr>
      <td>寄与者名</td>
      <td>creator</td>
      <td>jpcoar:contributorName</td>
      </tr>
      <tr>
      <td>寄与者所属名</td>
      <td>affiliationName</td>
      <td>jpcoar:affiliationName</td>
      </tr>
      <tr>
      <td>収録物名</td>
      <td>journal_title_name</td>
      <td>jpcoar:sourceTitle</td>
      </tr>
      <tr>
      <td>収録物発行日</td>
      <td>date</td>
      <td>date(dateType="Issued")</td>
      </tr>
      <tr>
      <td>巻</td>
      <td>volume</td>
      <td>jpcoar:volume</td>
      </tr>
      <tr>
      <td>号</td>
      <td>issue</td>
      <td>jpcoar:issue</td>
      </tr>
      <tr>
      <td>開始ページ</td>
      <td>first_page</td>
      <td>jpcoar:pageStart</td>
      </tr>
      <tr>
      <td>終了ページ</td>
      <td>last_page</td>
      <td>jpcoar:pageEnd</td>
      </tr>
      <tr>
      <td>日付</td>
      <td>date</td>
      <td>datacite:date</td>
      </tr>
      <tr>
      <td>収録誌のISSN</td>
      <td>journal_id_type</td>
      <td>jpcoar:sourceIdentifier</td>
      </tr>
      </tbody>
      </table>

---

### DataCite APIからのメタデータ取得

  - WEB API リクエスト  
    ※ API仕様： https://support.datacite.org/docs/api
    - リクエストURL  
      https://api.datacite.org/dois/{id}
    - method  
      GET
    - パラメータ  

      <table>
      <thead>
      <tr>
      <th>パラメーター名</th>
      <th>説明</th>
      <th>値</th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>doi</td>
      <td>検索するDOI</td>
      <td>{doi}: 入力されたDOI</td>
      </tr>
      </tbody>
      </table>

    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される

      取得データの入力先メタデータ項目

      <table>
      <thead>
      <tr>
      <th><strong>データ</strong></th>
      <th><strong>パス</strong></th>
      <th><strong>対応するJPCOARマッピング</strong></th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>タイトル</td>
      <td>title</td>
      <td>dc:title</td>
      </tr>
      <tr>
      <td>著者名</td>
      <td>creator</td>
      <td>jpcoar:creatorName</td>
      </tr>
      <tr>
      <td>著者所属名</td>
      <td>affiliation</td>
      <td>jpcoar:affiliationName</td>
      </tr>
      <tr>
      <td>寄与者名</td>
      <td>creator</td>
      <td>jpcoar:contributorName</td>
      </tr>
      <tr>
      <td>寄与者所属名</td>
      <td>affiliationName</td>
      <td>jpcoar:affiliationName</td>
      </tr>
      <tr>
      <td>識別子</td>
      <td>doi</td>
      <td>jpcoar:identifier</td>
      </tr>
      <tr>
      <td>日付</td>
      <td>date</td>
      <td>datacite:date</td>
      </tr>
      <tr>
      <td>会議名</td>
      <td>fundingReferences</td>
      <td>jpcoar:fundingReference</td>
      </tr>
      <tr>
      <td>関連識別子</td>
      <td>relationships_type</td>
      <td>jpcoar:relatedIdentifier(identifierType="DOI")</td>
      </tr>
      <tr>
      <td>権利</td>
      <td>rights</td>
      <td>jpcoar:rights</td>
      </tr>
      <tr>
      <td>バージョン</td>
      <td>version</td>
      <td>jpcoar:edition</td>
      </tr>
      </tbody>
      </table>

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

        <table>
        <thead>
        <tr>
        <th>パラメーター名</th>
        <th>説明</th>
        <th>値</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>operation</td>
        <td>操作種別</td>
        <td>SRUの場合は「searchRetrieve」固定</td>
        </tr>
        <tr>
        <td>version</td>
        <td>バージョン</td>
        <td>「1.2」固定とする</td>
        </tr>
        <tr>
        <td>startRecord</td>
        <td>開始位置</td>
        <td>「1」固定とする</td>
        </tr>
        <tr>
        <td>recordPacking</td>
        <td>レスポンス形式</td>
        <td>「xml」固定とする</td>
        </tr>
        <tr>
        <td>recordSchema</td>
        <td>取得データスキーマ</td>
        <td>「pam」固定とする</td>
        </tr>
        <tr>
        <td>query</td>
        <td>検索式</td>
        <td>{query}: 「prism.doi={doi}」をURLエンコードした文字列<br>  * {doi}: 入力されたDOI</td>
        </tr>
        </tbody>
        </table>
    
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

      <table>
      <thead>
      <tr>
      <th><strong>データ</strong></th>
      <th><strong>パス</strong></th>
      <th><strong>対応するJPCOARマッピング</strong></th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>タイトル</td>
      <td>dc:title</td>
      <td>jpcoar:titleName</td>
      </tr>
      <tr>
      <td>著者名</td>
      <td>dc:creator</td>
      <td>jpcoar:creatorName</td>
      </tr>
      <tr>
      <td>寄与者名</td>
      <td>dc:creator</td>
      <td>jpcoar:contributorName</td>
      </tr>
      <tr>
      <td>収録物名</td>
      <td>prism:publicationName</td>
      <td>jpcoar:sourceTitle</td>
      </tr>
      <tr>
      <td>収録物発行日</td>
      <td>prism:publicationDate</td>
      <td>date(dateType="Issued")</td>
      </tr>
      <tr>
      <td>巻</td>
      <td>prism:volume</td>
      <td>jpcoar:volume</td>
      </tr>
      <tr>
      <td>号</td>
      <td>prism:number</td>
      <td>jpcoar:issue</td>
      </tr>
      <tr>
      <td>開始ページ</td>
      <td>prism:startingPage</td>
      <td>jpcoar:pageStart</td>
      </tr>
      <tr>
      <td>総ページ数</td>
      <td>prism:pageRange</td>
      <td>jpcoar:numPages</td>
      </tr>
      <tr>
      <td>日付</td>
      <td>prism:publicationDatee</td>
      <td>datacite:date</td>
      </tr>
      <tr>
      <td>収録誌のISSN</td>
      <td>prism:issn</td>
      <td>jpcoar:sourceIdentifier</td>
      </tr>
      <tr>
      <td>関連識別子</td>
      <td>prism:doi</td>
      <td>jpcoar:relatedIdentifier(identifierType="DOI")</td>
      </tr>
      </tbody>
      </table>

---

### arXiv APIからのメタデータ取得

  - 【v2.1.0】WEB API リクエスト  
    ※ API仕様： https://info.arxiv.org/help/api/user-manual.html
    - リクエストURL  
      https://export.arxiv.org/api/query?search_query=doi:{doi}
    - method  
      GET
    - パラメータ  

      <table>
      <thead>
      <tr>
      <th>パラメーター名</th>
      <th>説明</th>
      <th>値</th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>search_query</td>
      <td>検索するDOI</td>
      <td><code>doi:{doi}</code> の形式（{doi}: 入力されたDOIの末尾2セグメント（<code>prefix/suffix</code>））</td>
      </tr>
      </tbody>
      </table>

    - リクエストURLは config `WEKO_WORKSPACE_ARXIV_API_URL`（既定 `https://export.arxiv.org/api/query?search_query=doi:`）に DOI を連結して生成する。レスポンスは XML 形式（Atom）で返却され、`xmltodict` で辞書に変換して解析する（`feed.entry` 配下を参照）。
    - 抽出対象のデータ（下表の「取得キー」）は config `WEKO_WORKSPACE_ARXIV_REQUIRED_ITEM`（title / identifier / date / description / creator / relation / subject）で制御される。
    - 取得したデータは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される

      取得データの入力先メタデータ項目

      <table>
      <thead>
      <tr>
      <th><strong>データ</strong></th>
      <th><strong>取得キー（arXiv応答のパス）</strong></th>
      <th><strong>対応するJPCOARマッピング</strong></th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>タイトル</td>
      <td>title（entry.title）</td>
      <td>dc:title</td>
      </tr>
      <tr>
      <td>arXivの論文ページへのURL</td>
      <td>identifier（entry.id）</td>
      <td>jpcoar:identifier(identifierType=URI)</td>
      </tr>
      <tr>
      <td>論文の提出日</td>
      <td>date（entry.published の日付部分）</td>
      <td>datacite:date(dateType=Submitted)</td>
      </tr>
      <tr>
      <td>論文の最終更新日</td>
      <td>date（entry.updated の日付部分）</td>
      <td>datacite:date(dateType=Updated)</td>
      </tr>
      <tr>
      <td>論文の要約</td>
      <td>description（entry.summary）</td>
      <td>datacite:description(descriptionType=Abstract)</td>
      </tr>
      <tr>
      <td>著者によるコメント</td>
      <td>description（entry.arxiv:comment）</td>
      <td>datacite:description(descriptionType=Other)</td>
      </tr>
      <tr>
      <td>著者の名前</td>
      <td>creator（entry.author.name）</td>
      <td>jpcoar:creator→jpcoar:creatorName</td>
      </tr>
      <tr>
      <td>著者の所属機関</td>
      <td>creator（entry.author.arxiv:affiliation）</td>
      <td>jpcoar:creator→jpcoar:affiliation→jpcoar:affiliationName</td>
      </tr>
      <tr>
      <td>論文関連リンク（HTML表示用URL・PDF表示用URL・解決済みDOI(doi.org)のURL など entry.link の全件）</td>
      <td>relation（entry.link.@href）</td>
      <td>jpcoar:relation(relationType=isFormatOf)→jpcoar:relatedIdentifier(identifierType=URI)</td>
      </tr>
      <tr>
      <td>DOI</td>
      <td>relation（entry.arxiv:doi）</td>
      <td>jpcoar:relation(relationType=isVersionOf)→jpcoar:relatedIdentifier(identifierType=DOI)</td>
      </tr>
      <tr>
      <td>論文のカテゴリ</td>
      <td>subject（entry.category.@term）</td>
      <td>jpcoar:subject(subjectScheme=Other)。主要カテゴリ（entry.arxiv:primary_category.@term）と一致するものを先頭に置く</td>
      </tr>
      </tbody>
      </table>

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

### arXiv APIからのメタデータ取得

  * 【v2.1.0】arXiv API からDOIに紐づくメタデータを取得する
    * `weko_workspace.api.arXivURL.get_data()` を呼び出し、arXiv API からデータを取得する
      * arXiv API からはXML形式でレスポンスが返却される
    * 取得したAPIレスポンス（XML）を `xmltodict` で辞書型に整形する
    * アイテムタイプのJPCOARマッピングに応じた項目にメタデータを設定する（設定対象は `WEKO_WORKSPACE_ARXIV_REQUIRED_ITEM` に従う）


## 実装補足（v2.0.2 実装との突き合わせ）

- 【v2.1.0】メタデータ自動補完：CrossRef=`weko_items_autofill.api.CrossRefOpenURL`、CiNii/JaLC/DataCite/医中誌/arXiv=`weko_workspace.api`（`CiNiiURL`/`JALCURL`/`DATACITEURL`/`JamasURL`/`arXivURL`）。外部URLは config `WEKO_WORKSPACE_*_API_URL`。CrossRef は API 証明書（`weko_admin.models.ApiCertificate`、code `"crf"`）が無い場合はリクエストしない。
- 【v2.1.0】arXiv 取得は weko-workspace で完結する。エンドポイントは `weko_workspace.views.get_auto_fill_record_data_arXivapi`（route `/get_auto_fill_record_data_arXivapi`）、取得ロジックは `weko_workspace.api.arXivURL` と `weko_workspace.utils.get_arXiv_record_data`（`get_arXiv_title_data` / `get_arXiv_identifier_data` / `get_arXiv_date_data` / `get_arXiv_description_data` / `get_arXiv_creator_data` / `get_arXiv_relation_data` / `get_arXiv_subject_data` ほか）。config は `WEKO_WORKSPACE_ARXIV_API_URL`（既定 `https://export.arxiv.org/api/query?search_query=doi:`）と `WEKO_WORKSPACE_ARXIV_REQUIRED_ITEM`（title/identifier/date/description/creator/relation/subject）。
- 【v2.1.0】各外部ソース（CiNii/JaLC/DataCite/arXiv）が生成する DOI 識別子には `relationType='isVersionOf'` が付与される（JaLC は併せて `type='DOI'` を付与）。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|---|---|---|
|2025/03/27|057e4d8985a4b5526c0db7f07f717a4bb45bc984|初版作成|
|2026/07/17||v2.1.0差分反映：arXiv メタデータ自動補完ソースを追加（`arXivURL`／`get_arXiv_*`／endpoint `get_auto_fill_record_data_arXivapi`／config `WEKO_WORKSPACE_ARXIV_API_URL`・`_REQUIRED_ITEM`）、DOI識別子への `relationType='isVersionOf'` 付与を追記|
| 2026/10/05 | 508030789 | release\_v2.1.0突合：arXiv のリクエストパラメータを `search_query=doi:{doi}` に訂正、取得データ表を `get_arXiv_*` の実装（応答パス・マッピング先）に合わせて整理、処理概要の重複節を削除 |
