### Item Registration：メタデータ入力

#### 目的・用途

Item Registrationの一部として、画面上の入力欄でメタデータを設定する。

#### 利用方法

ワークフローで、Item Registration画面を表示する。

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
<td>※</td>
<td></td>
</tr>
</tbody>
</table>

※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

#### 機能内容

1\. アイテムのメタデータを入力する

  - 【アイテム登録画面】に入力するアイテムのメタデータを表示する

  - 【Administration \> アイテムタイプ管理（Item Types） \> メタデータ（Meta）画面】で設定したOptionに応じて、アイテム登録/編集画面におけるアイテムタイプ項目の表示を制御する
    
      - メタデータ画面のItem Nameに対するOption属性に「Required」を設定した項目は、アイテム登録/編集画面の表示時に「Required」パネルに配置し、パネルを展開可能とする  
        「Required」を設定した項目のラベルの右側に「 \* 」と付けされる
        
          - Item Name配下のAttributeに対するOption属性「Required」はこの制御の対象としない
    
      - メタデータ画面のItem Nameに対するOption属性に「Multiple」、「List Display」、「Specify Newline」を設定したものを「Optional」パネルに配置し,パネルを開閉可能とする
    
      - 以下の項目は本ストーリーでの対応の対象としない
        
          - サムネイル（Thumbnail）
        
          - Contributor
        
          - 公開日（PubDate）
        
          - フィードバックメール送信先（Feedback Mail Destination）

  - 日付のフォーマットで定義されるプロパティまたは属性に対して、3つのフォーマット（YYYY-MM-DD、YYYY-MM、YYYY）が入力できる
    
      - 入力方法はカレンダー入力、または手入力である
    
      - デフォルト値はサーバ日付（/api/admin/get\_server\_date）を利用する
    
      - 無効な日付が入力された場合のチェックを行う
        
          - modules/weko-theme/weko\_theme/static/js/weko\_theme/search\_detail.js
        
          - modules/weko-theme/weko\_theme/static/js/weko\_theme/top\_page.js

  - 作成者プロパティへの著者情報の入力
    
      - 「著者DBから入力」（From author DB）ボタンを押下すると、著者DBの検索ウィンドウが表示される
    
      - 「検索」ボタンを押すと、【Administration \> 著者DB管理（Author Management） \> 編集（Edit）】で登録された著者DB一覧を表示する
    
      - ［入力（import）］ ボタンを押すと、選択した著者情報をメタデータの各エリアに入力する
    
      - 「Add Author」ボタンを押すと、著者登録画面が表示され著者情報を登録することができる（登録すると著者DB管理画面にも反映される）
    
      - 作成者識別子"WEKO"のデータ部分はユーザーでの編集は不可とする（作成者識別子Scheme, 作成者識別子URI, 作成者識別子はグレーアウトする）
    
      - アイテム登録時にDB, ESに"author\_link"という情報を持たせ、アイテムと著者DBの紐づけを行う
    
      - アイテムとの紐づけを行わない(解除する)場合は、「作成者」パネル内の各入力エリアの右上にある\[×\]で紐づけを解除する
    
      - アイテムで個別に編集した作成者の項目は、Adminの著者DBには反映されない。  
        なお、アイテムで個別に編集した後に著者DBから著者を取り込むと、個別編集した項目は上書きされる

2\. アイテムのメタデータを自動入力できる

  - Web APIのアカウント情報を設定する
    
      - 【Administration \> 設定（Setting） \> WebAPIアカウント（WebAPI Account）画面】にアイテムメタデータ自動入力機能で連携するWeb APIのアカウント情報を設定する  
        現在、CrossRefのみ対応している
    
      - 設定項目は以下とする
        
          - 「入力タイプ」（Input Type） ：タイプを選択する
        
          - 各種APIに必要なアカウント設定フィールド
            
              - 入力タイプで "CrossRef" を選択した場合は、以下の入力フィールドを表示する  
                「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）
    
      - Saveボタンを押すと設定情報が保存される
    
      - 保存した設定情報は、アイテムメタデータ自動入力機能におけるAPIアカウント認証で使用する

  - アイテムメタデータを自動入力する
    
      - アイテムメタデータ登録画面に「メタデータ自動入力」（Automatic Metadata Input）ボタンを押すと、メタデータ自動入力のポップアップが表示される  
        「ID選択」プルダウンにタイプを選択し、「取得」（Get）ボタンを押すと書誌情報が取得される形とする

  - CrossRef API経由でアイテムメタデータを入力する
    
      - 「CrossRef」を選択し、DOIの値をテキストフィールドに入力して「取得」（Get）ボタンを押すと、【Administration \> 設定（Setting） \> WebAPIアカウント（WebAPI Account）画面】に設定されたAPIの利用にあたり必要なクレデンシャル情報(CrossRef Query Services Account)で書誌情報が取得される
        
          - 取得データは、アイテムの対応項目および対応するJPCOARマッピングが設定されたメタデータ項目に自動入力される  
            取得データの入力先メタデータ項目

| \# | 要素                                                              | JPCOARスキーマ                                      |
| -- | --------------------------------------------------------------- | ----------------------------------------------- |
| 1  | article\_title                                                  | dc:title                                        |
| 2  | author                                                          | jpcoar:creatorName                              |
| 3  | contributor(contributor\_role属性が editor, chair, translator)     | jpcoar:contributorName                          |
| 4  | contributor(contributor\_role属性が editor, chair, translator 以外)  | jpcoar:creatorName                              |
| 5  | organization(contributor\_role属性が editor, chair, translator)    | jpcoar:affiliationName                          |
| 6  | organization(contributor\_role属性が editor, chair, translator 以外) | jpcoar:affiliationName                          |
| 7  | journal\_title                                                  | jpcoar:sourceTitle                              |
| 8  | volume                                                          | jpcoar:volume                                   |
| 9  | issue                                                           | jpcoar:issue                                    |
| 10 | first\_page                                                     | jpcoar:pageStart                                |
| 11 | last\_page                                                      | jpcoar:pageEnd                                  |
| 12 | year                                                            | datacite:date(dateType="Issued")                |
| 13 | issn                                                            | jpcoar:sourceIdentifier(identifierType="ISSN")  |
| 14 | isbn                                                            | jpcoar:relatedIdentifier(identifierType="ISBN") |
| 15 | doi                                                             | jpcoar:relatedIdentifier(identifierType="DOI")  |

  - CiNii API経由でアイテムメタデータを入力する
    
      - 「CiNii」を選択し、CRIDをテキストフィールドに入力して「取得」（Get）ボタンを押すと書誌情報が取得される
    
      - 書誌情報の取得は、CiNii API を利用する  
        \[CiNii ResearchのJSON-LD\]  
        https://support.nii.ac.jp/ja/cir/r\_json
    
      - 取得データは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される
        
        取得データの入力先メタデータ項目

| **データ**   | **パス**                                          | **対応するJPCOARマッピング**                   |
| --------- | ----------------------------------------------- | ------------------------------------- |
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

  - 指定したWEKOIDのデータを流用してアイテムメタデータを入力する
    
      - 「WEKOID」を選択し、recidの値をテキストフィールドに入力して「取得」（Get）ボタンを押すと、書誌情報が取得される
        
          - PersestentIdentifier.getを用い、pidstore\_pidテーブルからレコードID(object\_uuid)を取得する
        
          - JPCOARスキーママッピングが一致した項目について、メタデータを流用入力する
            
              - recidに指定したアイテムと、編集対象のアイテムのアイテムタイプが異なっていても、JPCOARマッピングが一致した項目について流用入力する
            
              - マッピングしていない項目は流用入力対象外とする
        
          - データ流用時（「Get」ボタン押下時）に、取り込み対象アイテムの参照権限があるか権限チェックを行う
            
              - 非公開のアイテムについては、自分が参照できるアイテムでなければ流用入力できない
            
              - ただし、参照権限があっても(ロールによらず)Hide設定がされた項目については流用入力できない

  - 制限公開用のアイテムタイプに対して、いくつかの項目が自動入力されて、アイテム登録画面に非活性の状態で表示される  
    対象項目は、以下のファイルを参照する
    
      - ファイル： 別紙「利用申請および利用報告アイテムタイプ.xlsx」
        
          - 「利用申請」シート：「利用申請」と「二段階利用申請」アイテムタイプの説明
        
          - 「利用報告」シート：「利用報告」アイテムタイプの説明

  - 「Automatic metadata input」からメタデータを自動入力した際、ISBN/ISSN/DOIはすべて「jpcoar:sourceIdentifier」にマッピングされるが、このマッピング情報がアイテムタイプに複数存在する場合は、１つ目（１番上）のプロパティにのみセットする

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > 「weko\_workflow」：アイテム編集可能な権限をチェックする処理モジュールである

  - > 「weko\_items\_ui」：メタデータ登録を管理する処理モジュールである

  - > 「weko-items-autofill」：メタデータ自動入力用のデータを取得する処理モジュールである

<!-- end list -->

  - > 処理概要

> 選択されたメタデータを表示する処理

  - > パネルがオープンか、クローズかの状態を取得する
    
      - > すべての項目に対してデフォルトの状態はクローズとする
    
      - > 「$rootScope.recordsVM.invenioRecordsSchema.required」から必須項目を取得し、それらの項目のパネルが初期としとオープンの状態とする

  - > パネルの中身に表示する処理はプロパティのデータを取得し、タイプに応じて以下のテンプレートで表示する
    
      - > form.html（https://github.com/inveniosoftware/invenio-records-js/blob/master/src/invenio-records-js/templates/form.html）
    
      - > decorators（https://github.com/inveniosoftware/invenio-records-js/tree/master/src/invenio-records-js/templates/decorators）

2\. 設定

| **設定**                           | **説明**               | **デフォルト値** | **実装箇所**                                        |
| -------------------------------- | -------------------- | ---------- | ----------------------------------------------- |
| WEKO\_ITEMS\_UI\_SAVE\_FREQUENCY | メタデータ登録画面における自動セーブ機能 | 10分        | modules/weko-items-ui/weko\_items\_ui/config.py |

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
<p>2024/04/14</p>
</blockquote></td>
<td>cd0183f59a16928be2511e33e4495a3376f143c9</td>
<td>v1.0.6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>
