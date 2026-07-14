# Item Registration：メタデータ入力

## 目的・用途

Item Registrationの一部として、画面上の入力欄でメタデータを設定する。

## 利用方法

ワークフローで、Item Registration画面を表示する。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       〇       |        〇        |         〇         |      〇      |      ※      |        ×          |


※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

## 機能内容
### 1. アイテムのメタデータを入力する

- 【アイテム登録画面】に入力するアイテムのメタデータを表示する
- 【Administration > アイテムタイプ管理（Item Types） > メタデータ（Meta）画面】で設定したOptionに応じて、アイテム登録/編集画面におけるアイテムタイプ項目の表示を制御する
    - メタデータ画面のItem Nameに対するOption属性に「Required」を設定した項目は、アイテム登録/編集画面の表示時に「Required」パネルに配置し、パネルを展開可能とする  
    「Required」を設定した項目のラベルの右側に「 * 」と付けされる
        - Item Name配下のAttributeに対するOption属性「Required」はこの制御の対象としない
    - メタデータ画面のItem Nameに対するOption属性に「Multiple」、「List Display」、「Specify Newline」を設定したものを「Optional」パネルに配置し,パネルを開閉可能とする
    - 以下の項目は本ストーリーでの対応の対象としない
        - サムネイル（Thumbnail）
        - Contributor
        - 公開日（PubDate）
        - フィードバックメール送信先（Feedback Mail Destination）

- 日付のフォーマットで定義されるプロパティまたは属性に対して、3つのフォーマット（YYYY-MM-DD、YYYY-MM、YYYY）が入力できる
    - 入力方法はカレンダー入力、または手入力である
    - デフォルト値はサーバ日付（/api/admin/get_server_date）を利用する
    - 無効な日付が入力された場合のチェックを行う
        - modules/weko-theme/weko_theme/static/js/weko_theme/search_detail.js
        - modules/weko-theme/weko_theme/static/js/weko_theme/top_page.js

- 「作成者」、「寄与者」、「権利者情報」の識別子Schemeの選択肢は ID Prefix から自動で取得する （v2.0.0）
- 「作成者」、「寄与者」の所属機関識別子Schemeの選択肢は Affiliation ID から自動で取得する （v2.0.0）

- 作成者プロパティへの著者情報の入力
    - 「著者DBから入力」（From author DB）ボタンを押下すると、著者DBの検索ウィンドウが表示される
    - 「検索」ボタンを押すと、【Administration > 著者DB管理（Author Management） > 編集（Edit）】で登録された著者DB一覧を表示する
    - ［入力（import）］ ボタンを押すと、選択した著者情報をメタデータの各エリアに入力する
    - 「Add Author」ボタンを押すと、著者登録画面が表示され著者情報を登録することができる（登録すると著者DB管理画面にも反映される）
    - コミュニティ管理者、登録ユーザーの場合は著者登録画面のコミュニティ選択欄の選択肢にアクティビティを作成したコミュニティを加える。
    - アイテム作成時、作成者識別子は編集不可となる。
    - アイテム編集時、作成者識別子"WEKO"のデータ部分はユーザーでの編集は不可とする（作成者識別子Scheme, 作成者識別子URI, 作成者識別子はグレーアウトする）。それ以外の識別子は変更可能となる。
    - アイテム登録時にDB, ESに"author_link"という情報を持たせ、アイテムと著者DBの紐づけを行う
    - アイテムとの紐づけを行わない(解除する)場合は、「作成者」パネル内の各入力エリアの右上にある[×]で紐づけを解除する
    - アイテムで個別に編集した作成者の項目は、Adminの著者DBには反映されない。  
    なお、アイテムで個別に編集した後に著者DBから著者を取り込むと、個別編集した項目は上書きされる

### 2. アイテムのメタデータを自動入力できる

- Web APIのアカウント情報を設定する
    - 【Administration > 設定（Setting） > WebAPIアカウント（WebAPI Account）画面】にアイテムメタデータ自動入力機能で連携するWeb APIのアカウント情報を設定する  
      現在、CrossRefのみ対応している
    - 設定項目は以下とする
        - 「入力タイプ」（Input Type） ：タイプを選択する
        - 各種APIに必要なアカウント設定フィールド
            - 入力タイプで "CrossRef" を選択した場合は、以下の入力フィールドを表示する  
              「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）
    - Saveボタンを押すと設定情報が保存される
    - 保存した設定情報は、アイテムメタデータ自動入力機能におけるAPIアカウント認証で使用する

- アイテムメタデータを自動入力する
    - アイテムメタデータ登録画面に「メタデータをAPIから取得」（Retrieve Metadata from API）ボタンを押すと、メタデータ自動入力のポップアップが表示される  
      「ID選択」プルダウンにタイプを選択し、「取得」（Get）ボタンを押すと書誌情報が取得される形とする

- CrossRef API経由でアイテムメタデータを入力する
    - 「CrossRef」を選択し、DOIの値をテキストフィールドに入力して「取得」（Get）ボタンを押すと、【Administration > 設定（Setting） > WebAPIアカウント（WebAPI Account）画面】に設定されたAPIの利用にあたり必要なクレデンシャル情報(CrossRef Query Services Account)で書誌情報が取得される
        - 取得データは、アイテムの対応項目および対応するJPCOARマッピングが設定されたメタデータ項目に自動入力される  
          取得データの入力先メタデータ項目

| # | 要素                                                                 | JPCOARスキーマ                                  |
| -- | ------------------------------------------------------------------- | ----------------------------------------------- |
| 1  | article_title                                                       | dc:title                                        |
| 2  | author                                                              | jpcoar:creatorName                              |
| 3  | contributor(contributor_role属性が editor, chair, translator)       | jpcoar:contributorName                          |
| 4  | contributor(contributor_role属性が editor, chair, translator 以外)  | jpcoar:creatorName                              |
| 5  | organization(contributor_role属性が editor, chair, translator)      | jpcoar:affiliationName                          |
| 6  | organization(contributor_role属性が editor, chair, translator 以外) | jpcoar:affiliationName                          |
| 7  | journal_title                                                       | jpcoar:sourceTitle                              |
| 8  | volume                                                              | jpcoar:volume                                   |
| 9  | issue                                                               | jpcoar:issue                                    |
| 10 | first_page                                                          | jpcoar:pageStart                                |
| 11 | last_page                                                           | jpcoar:pageEnd                                  |
| 12 | year                                                                | datacite:date(dateType="Issued")                |
| 13 | issn                                                                | jpcoar:sourceIdentifier(identifierType="ISSN")  |
| 14 | isbn                                                                | jpcoar:relatedIdentifier(identifierType="ISBN") |
| 15 | doi                                                                 | jpcoar:relatedIdentifier(identifierType="DOI")  |

- CiNii API経由でアイテムメタデータを入力する
    - 「CiNii」を選択し、CRIDをテキストフィールドに入力して「取得」（Get）ボタンを押すと書誌情報が取得される
    - 書誌情報の取得は、CiNii API を利用する  
      [CiNii ResearchのJSON-LD]  
      https://support.nii.ac.jp/ja/cir/r_json
    - 取得データは、アイテムの対応項目および対応するJPCOARマッピング(jpcoar_v2_mapping)が設定されたメタデータ項目に自動入力される
      取得データの入力先メタデータ項目

| **データ**         | **パス**                                        | **対応するJPCOARマッピング**          |
| ------------------ | ----------------------------------------------- | ------------------------------------- |
| タイトル           | dc:title                                        | dc:title                              |
| 別タイトル         | dcterms:alternative                             | dc:title                              |
| 成果物識別子       | productIdentifier.identifier(type=xx)           | jpcoar:relation                       |
| 著者名             | creator.foaf:name                               | jpcoar:creatorName                    |
| 著者識別子         | creator.personIdentifier                        |                                       |
| 著者所属名         | creator.jpcoar:affiliationName                  |                                       |
| 寄与者名           | contributor.foaf:name                           | jpcoar:contributorName                |
| 寄与者所属名       | contributor.jpcoar:affiliationName              |                                       |
| 寄与者識別子       | contributor.personIdentifier                    |                                       |
| 収録物識別子       | publication.publicationidentifier               |                                       |
| 収録物名           | publication.prism:publicationName               | jpcoar:sourceTitle                    |
| 収録物発行日       | publication.prism:publicationDate               |                                       |
| 巻                 | publication.prism:volume                        | jpcoar:volume                         |
| 号                 | publication.prism:number                        | jpcoar:issue                          |
| 開始ページ         | publication.prism:startingPage                  | jpcoar:pageStart                      |
| 終了ページ         | publication.prism:endingPage                    | jpcoar:pageEnd                        |
| 総ページ数         | publication.jpcoar:numPages                     | jpcoar:numPages                       |
| 発行者             | publication.dc:publisher                        | dc:publisher                          |
| 日付               | publication.prism:publicationDate               | datacite:date                         |
| 収録誌のNCID       | publication.publicationIdentifier(@type=NCID)   |jpcoar:sourceIdentifier                |
| 収録誌のISSN       | publication.publicationIdentifier(@type=ISSN)   | jpcoar:sourceIdentifier               |
| 学位授与番号       | ndl:dissertationNumber                          |                                       |
| 学位名             | ndl:degreeName                                  |                                       |
| 学位授与年月日     | ndl:dateGranted                                 |                                       |
| 学位授与機関識別子 | degreeAwardInstitution.institutionIdentifier    |                                       |
| 学位授与機関名     | degreeAwardInstitution.jpcoar:degreeGrantorName |                                       |
| 学会、会議名       | jpcoar:conferenceName                           |                                       |
| 開催地             | jpcoar:conferencePlace                          |                                       |
| 開催期間(開始日)   | jpcoar:conferenceDate.jpcoar:startDay           |                                       |
| 開催期間(開始月)   | jpcoar:conferenceDate.jpcoar:startMonth         |                                       |
| 開催期間(開始年)   | jpcoar:conferenceDate.jpcoar:startYear          |                                       |
| 開催期間(終了日)   | jpcoar:conferenceDate.jpcoar:endDay             |                                       |
| 開催期間(終了月)   | jpcoar:conferenceDate.jpcoar:endDay             |                                       |
| 開催期間(終了年)   | jpcoar:conferenceDate.jpcoar:endDay             |                                       |
| 助成機関名         | fundingProgram.notation                         |                                       |
| 関連物関連タイプ   | relatedProduct.relationType                     |                                       |
| 関連物識別子       | relatedProduct.productIdentifier                |                                       |
| 関連物タイトル     | relatedProduct.jpcoar:relatedTitle              |                                       |
| 抄録タイプ         | description.type                                | typeはAbstraction固定                 |
| 抄録本文           | description.notation                            | dc:description                        |
| 主題URL            | foaf:topic.@id                                  | jpcoar:subject                        |
| 主題タイトル       | foaf:topic.dc:title                             | jpcoar:subject                        |
| バージョン         | datacite:version                                |                                       |
| 言語               | dc:language                                     |                                       |

- 指定したWEKOIDのデータを流用してアイテムメタデータを入力する
    - 「WEKOID」を選択し、recidの値をテキストフィールドに入力して「取得」（Get）ボタンを押すと、書誌情報が取得される
        - PersestentIdentifier.getを用い、pidstore_pidテーブルからレコードID(object_uuid)を取得する
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

- 「メタデータをAPIから取得」からメタデータを自動入力した際、ISBN/ISSN/DOIはすべて「jpcoar:sourceIdentifier」にマッピングされるが、このマッピング情報がアイテムタイプに複数存在する場合は、１つ目（１番上）のプロパティにのみセットする

### 3. Web APIによるDOIを使用したメタデータ補完機能
- 「メタデータをAPIから取得」（Retrieve Metadata from API）ボタンを押すと出現するポップアップウィンドウにて、「ID選択」プルダウンで`DOI`を選択し、DOIを入力して「取得」（Get）ボタンを押すことで、管理者によって設定された優先度順にAPIから取得したメタデータで、すでに画面に手入力したメタデータを更新する。
- `instance.cfg`にて、以下のように設定する
    ```python
    # weko_items_autofill/config.pyに利用可能なWeb APIのリストを定義する
    WEKO_ITEMS_AUTOFILL_API_LIST = [
        "JaLC API",
        "医中誌 Web API",
        "CrossRef",
        "DataCite",
        "CiNii Research"
    ]

    # instance.cfgに使用するWeb APIの優先度を定義する
    WEKO_ITEMS_AUTOFILL_TO_BE_USED = [
        # 優先度順に格納
        "医中誌 Web API",
        "CrossRef",
        "DataCite",
        "Original"
    ]
    ```
- 処理概要
  - `WEKO_ITEMS_AUTOFILL_API_LIST`に設定されたAPIのリストから、`WEKO_ITEMS_AUTOFILL_TO_BE_USED`に設定されたWEB APIからDOIをもとにメタデータを取得し、プロパティごとに自動入力する。
  - 同じプロパティに対して複数のAPIからメタデータが取得された場合は、`WEKO_ITEMS_AUTOFILL_TO_BE_USED`に設定された順番で優先度をつけて最上位のAPIから取得したメタデータを入力する。
  - 上記の例だと、`Original`のメタデータに対して、`DataCite`、`CrossRef`、`医中誌 Web API`の順にメタデータを取得し、プロパティ単位で上書きする。
    `Original`は、画面に手入力したメタデータを指す。
  - 各APIについては、[ADMIN_X_X：メタデータ補完機能](../admin/ADMIN_X_X.md)を参照のこと。

### 4. アイテム重複チェック機能
メタデータの入力後に、同一のメタデータを持つアイテムがすでに登録されていないかをチェックする。  
以下の条件で登録済みのアイテムのメタデータを検索し、同一のメタデータを持つアイテムが存在する場合は、モーダルで警告を表示する。

1. 論文の識別子による検索  
  DOIが**完全一致**するアイテムがあるか  
  ┗  DOIが完全一致すれば同一判定とし、2.以降の検索は行わない ※DOIは一意であるため

2. 「タイトル」「資源タイプ」「著者」の組み合わせによる検索  
    1. タイトルが**完全一致**するアイテムを検索（大文字小文字・全角半角の表記ゆれは補正）  
       ┗ タイトルの完全一致を対象とする。言語は検索対象外とする
    2. i.でヒットしたアイテムの内、資源タイプが**完全一致**するものを検索
    3. ii.でヒットしたアイテムの内、著者全員が一致するものを検索  
       ┗ 著者が複数あった場合、一つでも一致する著者があれば同一判定とし警告のメッセージを表示する

キャンセルボタンを押下すると、モーダルが閉じる。


## 関連モジュール

-  「weko_workflow」：アイテム編集可能な権限をチェックする処理モジュールである
-  「weko_items_ui」：メタデータ登録を管理する処理モジュールである
-  「weko-items-autofill」：メタデータ自動入力用のデータを取得する処理モジュールである


## 処理概要

選択されたメタデータを表示する処理

-  パネルがオープンか、クローズかの状態を取得する
   -  すべての項目に対してデフォルトの状態はクローズとする
   - 「$rootScope.recordsVM.invenioRecordsSchema.required」から必須項目を取得し、それらの項目のパネルが初期としとオープンの状態とする

-  パネルの中身に表示する処理はプロパティのデータを取得し、タイプに応じて以下のテンプレートで表示する
   -  form.html（https://github.com/inveniosoftware/invenio-records-js/blob/master/src/invenio-records-js/templates/form.html）
   -  decorators（https://github.com/inveniosoftware/invenio-records-js/tree/master/src/invenio-records-js/templates/decorators）

1. 設定

| **設定**                           | **説明**               | **デフォルト値** | **実装箇所**                                        |
| -------------------------------- | -------------------- | ---------- | ----------------------------------------------- |
| WEKO_ITEMS_UI_SAVE_FREQUENCY | メタデータ登録画面における自動セーブ機能 | 10分        | modules/weko-items-ui/weko_items_ui/config.py |

## 実装補足（v2.0.2 実装との突き合わせ）

- 自動保存間隔 `WEKO_ITEMS_UI_SAVE_FREQUENCY`（600000ms＝10分）。自動入力対象は `WEKO_ITEMS_AUTOFILL_API_LIST`（JaLC/医中誌/CrossRef/DataCite/CiNii Research。`WEKO_ITEMS_AUTOFILL_TO_BE_USED` の既定は空で instance.cfg が全6種を設定）。重複チェックは `weko_items_ui.utils.is_duplicate_record`。

## 詳細リファレンス（v2.0.2 実装：入力検証・重複チェック・自動補完）

対象：weko-items-ui / weko-items-autofill / weko-records / weko-admin。

### 1. 入力バリデーション（必須・型）

- 検証は `weko_items_ui.utils.validate_form_input_data` がアイテムタイプの JSON Schema を基準に実行。スキーマは `ItemTypes.get_by_id(id).schema` を複製し、除外項目削除（`remove_excluded_items_in_json_schema`）・著者テーブル補正（`set_scheme_by_author_table`）後に `RecordBase(data).validate()`（jsonschema）で検証。
- エラー整形：`required`→「Please input all required item.」、`pattern`→「Please input the correct data.」、`SchemaError`→「Schema Error:」＋詳細、他→原文。多言語サブ項目の言語重複は `validation_duplication_error_checker`、日付は `date_pattern_list`（YYYY / YYYY-MM / YYYY-MM-DD / ISO8601+TZD 等）で検査。
- 赤枠表示の仕組み：検証で得たエラー分類（either/either_key/mapping/pattern/required/required_key）を Redis（`updated_json_schema_{activity_id}`）に保存 → `get_json_schema` → `update_json_schema_by_activity_id` が該当ノードを解析しスキーマの `required` に注入して再描画。エラー確認 API は `GET /check_validation_error_msg/<activity_id>`（存在すれば `code=1`＋`msg`/`error_list`、無ければ `code=0`）。

### 2. 重複チェックの分岐

- 入口：`is_duplicate_record(data, exclude_ids)`（`data['metainfo']` 対象）／`is_duplicate_item(metadata, exclude_ids)`。共通処理 `check_duplicate`。
- 機能フラグ `WEKO_ITEMS_UI_ENABLE_DUPLICATE_CHECK`（既定 False）。無効時は即 `(False,[],[])`。
- 判定フィールド（`get_duplicate_fields`）：resourcetype／`subitem_identifier_uri`（DOI等）／`subitem_title`／creator名／`nameIdentifierScheme=="WEKO"` の author_link。検索対象は `records_metadata` の `publish_status='0'`（公開）かつ非バージョン（recid に `.` を含まない）、`exclude_ids` は除外。
- 判定順（短絡）：1) 識別子 AND 一致でヒットすれば即 `(True, recid_list, recid_links)`。2) タイトル（NFKC正規化＋小文字化＋空白/カンマ除去、多重集合一致）。3) リソースタイプ一致（積集合）。4) 著者（author_link を authors の fullName で解決、または creator 名を正規化して一致）。`recid_links` は `https://{host}/records/{recid}`。
- iframe 保存（`iframe_save_model`、`POST /iframe/model/save`）は保存前に重複チェックし、重複時は保存せず `{"code":1,"msg":"The same item may have been registered.","recid_list":...,"is_duplicate":true}` を返す。

### 3. メタデータ自動補完

- 対応API（`WEKO_ITEMS_AUTOFILL_API_LIST`）：JaLC API / 医中誌 Web API / CrossRef / DataCite / CiNii Research。UI 入力方式は DOI/CrossRef/CiNii/WEKOID/researchmap。
- DOI一括補完 `fetch_metadata_by_doi(doi, item_type_id, original, **kwargs)`：優先順位は `kwargs['meta_data_api']`（SWORD経由時）→ `WEKO_ITEMS_AUTOFILL_TO_BE_USED`（既定空）→ 空なら `["Original"]`。`reversed(api_priority)` で低優先から `result.update` するため高優先が後勝ち。各API呼出は try/except で失敗時スキップ。
- CrossRef は `get_crossref_record_data_with_pid` が `weko_admin.utils.get_current_api_certification("crf")`（`ApiCertificate`、table `api_certificate`、`api_code='crf'`）の PID を要し、未設定なら空リストを返し補完しない。
- DOI未一致時：各API該当なしは空リストを返し補完は行われない。`get_auto_fill_record_data` は例外時のみ `result['error']` を設定。
- 自動保存：`WEKO_ITEMS_UI_SAVE_FREQUENCY`（既定 600000ms＝10分）。`iframe/item_edit.html` の hidden input を `app.js` が読み `setInterval` で下書き保存（重複チェックを伴う）。


## 更新履歴

| 日付     | GitHubコミットID                       |更新内容|
| -------- | -------------------------------------- | ------ |
|2025/12/08|0ecc4cc7112aa59c2bc52f97fe3c3836aec5fd206|v2.0.0|
|2025/10/10|                                        |v2.0.0  |
|2025/03/13|94a0d70019b3dbf7ed6c01692b75a3dbad640db6|v1.1.0  |
|2025/01/01|09c6391d2ed1bae053fee9f8dfc98e95e1e1b87f|v1.0.7a2|
|2024/04/14|cd0183f59a16928be2511e33e4495a3376f143c9|v1.0.6  |
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|

