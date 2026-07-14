### フロー

## 目的・用途

本機能は、ワークフローに設定するフローの作成と編集を行う機能。

## 利用方法

【Administration＞ワークフロー管理（WorkFlow）＞フロー（Flow）】の順で画面遷移し利用する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

- 【Administration > ワークフロー管理（WorkFlow） > フロー（Flow）】のFlow Listに登録されたフローが一覧に表示される。
  - 表示項目は以下の通りである
    - 「No.」
    - 「フロー」（Flow）  
      登録されたフロー名である。リンクの形式で表示される。
    - 「ステータス」（Status）  
      フローのステータスである。
      - 「作成中」（Making）  
        フローに「Start」と「End」アクションのみが登録された状態。
      - 「利用可」（Available）  
        フローに必要なアクションが登録された状態。
    - 「更新日」（Updated）  
      フローの作成日（もしくは更新日）である。  
      フォーマット：YYYY-MM-DD
  - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに属するフローが一覧に表示される。

- 「Create Flow」ボタンを押すと、フローの作成画面に移動する。
  - 「Flow Name」テキストボックスにフロー名を入力する。
  - 「Repository」プルダウンからフローを登録するリポジトリを選択する。
    - 「Repository」プルダウンの選択肢は以下である。
      - システム管理者、リポジトリ管理者の場合、システムに登録しているリポジトリ一覧である。
      - サブリポジトリ管理者の場合、管理対象のリポジトリ一覧である。
  - 「保存」（Save）ボタンを押すと、「Start」及び「End」アクションがフローのアクション一覧に自動追加されて、フローのステータスが「作成中」（Making）となる。  
    フロー名が複数設定できない。入力されたフローの名前がシステムに存在する場合、エラーメッセージ「Create failed. Flow name is already in use.」が表示される。
    - フローのアクション一覧に表示される、表示項目は以下の通りである。
      - 「Order」  
        フローにアクションの流れの順序を示す項目
      - 「アクション名」（Name）
      - 「Action Role」  
        アクションを実行するロールを限定する項目
      - 「Action User」  
        アクションを実行するユーザーを限定する項目
      - 「Change Order」  
        アクションの順序を設定するボタン
  - 「Action Role」カラムに、アクションを実行するロールを限定できる。
    - 「Action Role」プルダウンから選択する。「Action Role」プルダウンの選択肢は以下である。
      - システム管理者、リポジトリ管理者は、システムに設定されたすべてのロールが表示される。
      - サブリポジトリ管理者は、自身が管理するサブリポジトリに関連するロールのみが表示される。
    - 「表示しない（Deny）」チェックボックスにチェックを入れる場合、選択されているロールが実施不可とする。
  - 「Action User」カラムに、アクションを実行するユーザーを限定できる。
    - 「Action User」プルダウンから選択する。「Action User」プルダウンの選択肢は以下である。
      - システム管理者、リポジトリ管理者は、システムに登録されたすべてのユーザが表示される。
      - サブリポジトリ管理者は、自身が管理するサブリポジトリに関連するユーザのみが表示される。
      - 「Item Registration」アクションに対して
        - 「Action User」プルダウンの直下にある、「登録者にメールを送信する」チェックボックスと「利用申請時に、アイテム登録者に対しメールを送信する」チェックボックスで利用申請時に送信するメールの送信可否を設定する。各々のチェックボックス直下のプルダウンで、送信するメールの内容を設定する。
          - admin_settings テーブルの name が restricted_access のレコードの settings.edit_mail_templates_enable が true の場合のみ有効
          - 「登録者にメールを送信する」チェックボックス：利用申請時に、申請者に対して送信するメールを設定する。
          - 「利用申請時に、アイテム登録者に対しメールを送信する」チェックボックス：利用登録/利用申請時に、申請先アイテムの登録者に対して送信するメールを設定する。
      - 「Approval」アクションに対して
        - 選択肢は上記のユーザーと、「アイテム登録者」、「プロパティを指定」(Specify Property)である
          - 「アイテム登録者」および「プロパティを指定」は admin_settings テーブルの name が restricted_access のレコードの settings.edit_mail_templates_enable が true の場合のみ有効
          - 「アイテム登録者」を設定した場合には、workflow_flow_action_role テーブルの action_item_registrant に true を設定する。
          - action_item_registrant が true の場合には該当フローを用いたワークフローで approval 時にアイテム登録者が承認者として action_user に設定される。
          - 「アイテム登録者」を選択した場合には、「承認依頼通知メール」は発行されない。
          - 「プロパティを指定」(Specify Property)を選択した場合、「プロパティを指定する」(Specify Property)モーダル画面を表示する。当該画面でプロパティを選択する。
          - モーダル画面には、プロパティ定義に「"approval":true」キーワードを持つプロパティ名を表示する。
          - モーダルに表示しているプロパティを選択して「設定」(Setting)ボタンを押すことで、プロパティを指定できる。
          - 「閉じる」（Close）ボタンを押すと、モーダルを閉じる。
        - 「Approval」アクションごとに通知メールを設定できるモーダル画面を表示する「通知メール設定」ボタンを表示する。
          - admin_settings テーブルの name が restricted_access のレコードの settings.edit_mail_templates_enable が true の場合のみ有効
          - モーダル画面に表示されたチェックボックスにチェックを入れ、プルダウンからメールテンプレートを設定することで、管理者画面で登録したメールを自動送信することができる。なお、このメールテンプレートはログインユーザー、非ログインユーザーで分けて設定することができる。
            - 「承認依頼通知メール」（Approval Request Notification Email）  
              承認者に承認を依頼するメールを送信する。
            - 「承認却下通知メール」（Approval Rejection Notification Email）  
              登録者に承認者が却下された旨を通知するメールを送信する。
            - 「承認通知メール」（Approval Notification Email）  
              登録者に承認者が承認された旨を通知するメールを送信する。
          - メール本文については、下記の「メール本文について」を参照。
    - 「Deny」チェックボックスにチェックを入れる場合、選択されているユーザーが実施不可とする。
  - 「Change Order」カラムにアクションの順序を設定できる。  
    一番上の項目は、［↑］ボタンが無効になる。一番下の項目は、［↓］ボタンを押下することは可能であるが動作しない。
  - 画面の下部に表示されている［保存（Save）］を押すと、フローを保存しメッセージを一覧画面の上部に表示する  
    メッセージ：「Updated flow action successfully」
  - アクションを追加するため、フローの作成画面に「More Action」ボタンを押すと、【アクション一覧画面】に移動する。
    - 表示項目は以下の通りである。
      - 「No.」
      - 「アクション名」（Name）
      - 「概要」（Summary）
      - 「最新バージョン」（Version）
      - 「更新日」（Updated）
      - 「適用バージョン」（Version）
      - 「適用日」（Updated）
    - 各アクション表示の下に「適用」（Apply）、「無効」（Unusable）、「更新」（Update）ボタンが表示される
      - 「適用」（Apply）ボタンを押すと、アクションがフローに追加される。追加されたアクションの「適用」（Apply）ボタンは非活性となる。
        - 「Approval」アクションに対して、複数定義できるため、「Approval」アクションが追加された場合、「適用」（Apply）ボタンがそのまま活性状態となり引き続き追加できる。また、アクション一覧に「Approval」を追加すると、アクション名は『Approval(1)』のように枝番を付与する
      - [無効（Unusable）]ボタンを押すと、追加されたアクションがフローから削除される。追加されていないアクションの[無効（Unusable）]ボタンは非活性となる。
        - 「Approval」アクションに対して、複数定義された場合、「無効」（Unusable）ボタンを押すと、アクション一覧に並ぶ「Approval」のうち枝番が一番大きいものから行われる
      - 各アクションの説明については、以下の通りである

        | # | アクション名 | 説明 | 制限事項 |
        |:---:|:---:|:---:|:---:|
        | 1 | Item Registration | アイテムのメタデータとコンテンツを登録するアクションである | |
        | 2 | Item Link | アイテムにリンク設定するアクションである | |
        | 3 | Identifier Grant | アイテムにDOIを付与するアクションである | Approvalの前で実行すること |
        | 4 | Approval | アイテムの査読／承認するアクションである | |

- フロー名のリンクを押すと、フローの編集画面に移動する
  - フローの編集画面で、フローの情報を編集できる
    - フローの情報を編集してから、[保存（Save）ボタン]を押すと、フローを編集し、メッセージを一覧画面の上部に表示する。  
      メッセージ：「Updated flow action successfully」
  - フローの編集画面で、[削除（Delete）]ボタンを押すと、フローを削除する。
    - 対象のフローがワークフローで使用されている場合、削除できない。[削除（Delete）]ボタンを押すと、エラーメッセージを表示する  
      エラーメッセージ：「Cannot be deleted because flow is used.」
  - フローの編集画面で、[戻る（Back）]ボタンを押すと、フロー一覧画面に移動する。

- WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True かつシステム管理者でない（リポジトリ管理者）の場合、利用申請に関するフロー（利用申請フラグがONのワークフローと紐づいているフロー）は閲覧・保存・削除ができず、権限エラーとなる。

- フロー編集画面

  フロー編集画面において、[approval]の[action user]を編集する際に、「アイテム登録者」、「リクエスト送信先(Request mail)」を表示する。
  - 「action user」にアイテム登録者を設定する際の仕様
    - 「action user」に「アイテム登録者」を設定した場合には、[action user]のvalueを-2とする。
    - 「action user」に「アイテム登録者」を設定した場合には、DBのworkflow_flow_action_roleテーブルに新規作成するカラムaction_item_registrantをTrueとする。
    - action_item_registrantがTrueの場合には該当フローを用いたワークフローでapproval時にアイテム登録者が承認者としてaction_userに設定される。
    - 「アイテム登録者」を選択した場合には、「承認依頼通知メール」は発行されない。
  - 「action user」に「リクエスト送信先」を設定する際の仕様
    - 「action user」に「リクエスト送信先」を設定した場合には、[action user]のvalueを-3とする。
    - 「action user」に「リクエスト送信先」を設定した場合には、DBのworkflow_flow_action_roleテーブルに新規作成するカラムaction_request_mailをTrueとする。
    - action_request_mailがTrueの場合には該当フローを用いたワークフローでapproval時に、「リクエスト送信先」のメールアドレスでユーザー登録しているユーザーが承認者として「action_user」に設定される。
      - リポジトリ管理者、システム管理者のロールを持つユーザーが「リクエスト送信先」に選ばれていた場合、そのユーザーは承認者になる。
      - 「Action role」が設定されていた場合、「リクエスト送信先」のユーザーの中でも「Action role」を満たしているユーザーのみ承認者になる。
      - 一般ユーザー（ロールなし）のメールアドレスが「リクエスト送信先」に設定されていた場合、そのメールアドレスのユーザーは承認者として設定されない。
    - 承認者となった「リクエスト送信先」のユーザーには承認依頼通知メールが発行される。

## 関連モジュール

- weko_workflow

## 処理概要

- [Create Flow]ボタンを押下しフロー作成画面に遷移すると、初期状態ではFlowNameテキストボックスに文字列を入力するか、[戻る（Back）]ボタン以外の操作は不可能である。
- Flow Nameテキストボックスに登録したいフロー名を入力後、[保存（Save）]ボタン押下で、weko_workflow.admin.FlowSettingView.new_flowが呼び出され、すでに登録されているフロー名と重複していないかのチェックがされ、重複がなければdb内のworkflow_flow_defineテーブルに情報が保存され、画面下部のアクション一覧が操作可能になる。また、Flow Statusの初期値は作成中（Making）である。
- [More Action]ボタンを押下すると、アクション一覧がモーダル表示されアクションの追加・削除・更新が可能となる。任意の項目の変更後、[閉じる（Close）]ボタン押下しアクション一覧画面を閉じたのちに、画面最下部の保存ボタン押下で、weko_workflow.admin.FlowSettingView.upt_flow_actionが呼び出され、フローのアクションが変更される。また、その時のアクションの情報はdb内のworkflow_flow_actionテーブルに保存される。具体的なカラムとの対応は以下のようになる。
  - created：アクションがフロー内に追加され、保存された時間。
  - updated：もともと存在するフローを更新した際の時間。
  - id：自動作番される数。個々のアクションの主キーとなる。
  - flow_id：そのアクションが追加されているフローを示すUUID。
  - action_id：アクション名に対応した数。対応は以下に示す通り。
    - 1：Start
    - 2：End
    - 3：Item Registration
    - 4：Approval
    - 5：Item Link
    - 6：OA Policy Confirmation
    - 7：Identifier Grant
  - Action_version：アクションのバージョン。
  - action_order：そのアクションが何番目に動作するかを示した数。
  - action_condition
  - action_status：そのアクションが使用可能かを示す。可能であれば「A」、そうでなければ「N」
  - action_date：そのアクションが追加された時間。
  - send_mail_setting：approvalのメールの送信設定が記載されている。

- 「Approval」アクションの「Action User」カラムでUserにプルダウンから選択されていた場合、保存ボタン押下時にworkflow_flow_action_roleテーブルにその情報を追加する。
  - Userに「Item Registrant」が選択されていた場合、「action_user」カラムの値を空にして、「action_item_registrant」カラムの値をTrueにして保存する。
  - Userに「Request Mail」が選択されていた場合、「action_user」カラムの値を空にして、「action_request_mail」カラムの値をTrueにして保存する。
  - Userに「プロパティを指定」が選択されていた場合、「action_user」カラムの値を空にして、specify_propertyの値を選択されたプロパティの値にして、保存する。
  - それ以外の場合、「action_user」カラムの値をプルダウンで選択されたメールアドレスのユーザーIDにして保存する。

- 「利用申請時に、アイテム登録者に対しメールを送信する」チェックボックスにチェックを入れ、直下のタブからメールを選択し「保存」ボタンを押下することで、アイテム登録者に対して送信するメールの情報がworkflow_flow_actionテーブルのsend_mail_settingカラムに辞書形式で保存される。

- 「Action User」カラムの「通知メール設定」ボタンを押下したとき、通知メールの現在の設定がモーダル画面で示され、「承認依頼通知メール」、「承認却下通知メール」、「承認通知メール」のログインユーザーと日ログインユーザーそれぞれに送信するメールテンプレートを設定する。
  - モーダル画面を閉じ、「保存」ボタンを押下することで、設定したメールテンプレートの情報を workflow_flow_action テーブルの send_mail_setting カラムに辞書形式で保存される。

### メール本文について

メール名：承認依頼通知メール

> Subject：利用申請の承認のお願い／Request for Approval of Application for Use
>
> [restricted_institution_name_ja]です。
>
> [restricted_site_name_ja]をご利用いただいて、ありがとうございます。
>
> [restricted_university_institution][restricted_fullname]様から、下記の利用申請がありました。
>
> 申請番号： [restricted_activity_id]
>
> 登録者名： [restricted_fullname]
>
> メールアドレス： [restricted_mail_address]
>
> 所属機関：[restricted_university_institution]
>
> 研究題目：[restricted_research_title]
>
> 申請データ：[restricted_data_name]
>
> 申請年月日：[restricted_application_date]
>
> [restricted_site_name_ja]（[restricted_site_url]）にアクセスしていただき、画面左上からログインしていただけますと、「ワークフロー」タブが現れます。ここから上記の申請内容をご確認ください。「承認」または「却下」のボタンをクリックしてください。
>
> このメールに心当たりのない方は、[restricted_site_name_ja] までご連絡ください。
>
> [restricted_site_name_ja]：[restricted_site_url]
>
> 問い合わせ窓口：[restricted_site_mail]
>
> ----------------------------------------------------------------------------------
>
> This is a message from [restricted_site_name_en].
>
> We received the below application.
>
> Application No.：[restricted_activity_id]
>
> Name：[restricted_fullname]
>
> E-mail：[restricted_mail_address]
>
> Affiliation：[restricted_university_institution]
>
> Title of research：[restricted_research_title]
>
> Dataset requested ：[restricted_data_name]
>
> Application date：[restricted_application_date]
>
> Please access [restricted_site_name_en]（[restricted_site_url]） and log in from the upper left corner of the screen, and the [Workflow] tab will appear. From here, please confirm the above application by clicking on “approve” or “reject”.
>
> If you received this message in error, please notify the [restricted_site_name_en]
>
> [restricted_site_name_en]：[restricted_site_url]
>
> E-mail：[restricted_site_mail]

メール名：承認却下通知メール

> Subject：利用申請の審査結果について／The results of the review of your application
>
> [restricted_university_institution]
>
> [restricted_fullname]　様
>
> [restricted_institution_name_ja]です。
>
> [restricted_site_name_ja]をご利用いただいて、ありがとうございます。
>
> 下記の利用申請を[restricted_institution_name_ja]で審査した結果、申請データの提供を見送らせていただくことになりました。
>
> 申請番号： [restricted_activity_id]
>
> 登録者名： [restricted_fullname]
>
> メールアドレス： [restricted_mail_address]
>
> 所属機関：[restricted_university_institution]
>
> 研究題目：[restricted_research_title]
>
> 申請データ：[restricted_data_name]
>
> 申請年月日：[restricted_application_date]
>
> このメールは自動送信されているので返信しないでください。
>
> お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、[restricted_site_name_ja] までご連絡ください。
>
> [restricted_site_name_ja]：[restricted_site_url]
>
> 問い合わせ窓口：[restricted_site_mail]
>
> ----------------------------------------------------------------------------------
>
> Dear [restricted_fullname],
>
> This is a message from [restricted_institution_name_en].
>
> Thank you for using [restricted_site_name_en].
>
> After reviewing the following application, [restricted_institution_name_en] is sorry to inform you that your application has been rejected.
>
> Application No.：[restricted_activity_id]
>
> Name：[restricted_fullname]
>
> E-mail：[restricted_mail_address]
>
> Affiliation：[restricted_university_institution]
>
> Title of research：[restricted_research_title]
>
> Dataset requested ：[restricted_data_name]
>
> Application date：[restricted_application_date]
>
> Please do not reply to this email as it has been sent automatically.
>
> Please direct all inquiries to the following address.
>
> Also, if you received this message in error, please notify [restricted_site_name_en].
>
> [restricted_site_name_en]：[restricted_site_url]
>
> E-mail：[restricted_site_mail]

メール名：承認通知メール

> Subject：利用申請の承認のお知らせ／Your application was approved
>
> [restricted_university_institution]
>
> [restricted_fullname]　様
>
> [restricted_institution_name_ja]です。
>
> [restricted_site_name_ja]をご利用いただいて、ありがとうございます。
>
> 下記の利用申請を承認しました。
>
> 申請番号： [restricted_activity_id]
>
> 登録者名： [restricted_fullname]
>
> メールアドレス： [restricted_mail_address]
>
> 所属機関：[restricted_university_institution]
>
> 研究題目：[restricted_research_title]
>
> 申請データ：[restricted_data_name]
>
> 申請年月日：[restricted_application_date]
>
> データは、下記アドレスよりダウンロードすることができます。
>
> [restricted_download_link]
>
> データは、[restricted_site_name_ja]から、[restricted_expiration_date][restricted_expiration_date_ja]までダウンロードすることができます。
>
> ダウンロード期限を過ぎると、再申請が必要です。
>
> このメールは自動送信されているので返信しないでください。
>
> このメールに心当たりのない方は、[restricted_site_name_ja]までご連絡ください。
>
> [restricted_site_name_ja]：[restricted_site_url]
>
> 問い合わせ窓口：[restricted_site_mail]
>
> ----------------------------------------------------------------------------------
>
> Dear [restricted_fullname],
>
> This is a message from [restricted_institution_name_en].
>
> Thank you for using [restricted_site_name_en].
>
> Your application below has been approved.
>
> Application No.：[restricted_activity_id]
>
> Name：[restricted_fullname]
>
> E-mail：[restricted_mail_address]
>
> Affiliation：[restricted_university_institution]
>
> Title of research：[restricted_research_title]
>
> Dataset requested ：[restricted_data_name]
>
> Application date：[restricted_application_date]
>
> The data can be downloaded from the address below.
>
> [restricted_download_link]
>
> Above dataset is available to download from [restricted_site_name_en] until [restricted_expiration_date][restricted_expiration_date_en].
>
> You will need to resubmit your application once the link becomes unavailable.
>
> Please do not reply to this email as it has been sent automatically.
>
> If you received this message in error, please notify the [restricted_site_name_en].
>
> [restricted_site_name_en]：[restricted_site_url]
>
> E-mail：[restricted_site_mail]

### 埋め込み文字の整理

- [restricted_site_name_ja]：【Administration>設定（Settings）>Site Info】 に設定されている日本語のSite Name
- [restricted_site_name_en]：【Administration>設定（Settings）>Site Info】に設定されている英語のSite Name
- [restricted_site_url]：「THEME_SITEURL」 に設定されているURL
- [restricted_site_mail]：【Administration>設定（Setting）>メール送信（Mail）】 のデフォルト送信元（Default sender）
- [restricted_activity_id]：対象となる利用申請のアクティビティID
- [restricted_fullname]：利用申請アイテムタイプ項目の申請者・名前の設定値
- [restricted_mail_address]：利用申請アイテムタイプ項目の申請者・メールアドレスの設定値
- [restricted_university_institution]：利用申請アイテムタイプ項目の申請者・所属機関の設定値
- [restricted_research_title]：利用申請アイテムタイプ項目の研究題目の設定値
- [restricted_data_name]：利用申請アイテムタイプ項目のデータ名の設定値
- [restricted_application_date]：利用申請アイテムタイプ項目の申請日の設定値
- [restricted_download_link]：データファイルのURL
- [restricted_expiration_date]：利用申請アイテムタイプ項目の承認日から【Administration>設定（Setting）>Restricted Access】のExpiration Date経過した日付

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_workflow.admin.FlowSettingView`（endpoint `flowsetting`）。`index` / `flow_detail` / `new_flow`（flow_id='0' で作成、それ以外は `update_flow`）/ `del_flow` / `upt_flow_action`。アクション保存成功「Updated flow action successfully」。使用中フローは削除不可「Cannot be deleted because flow is used.」。名称重複は「Flow name is already in use.」（400）。
- 実装補足：アイテム登録者 value=`WEKO_WORKFLOW_ITEM_REGISTRANT_ID`（-2）、リクエスト送信先 value=`WEKO_WORKFLOW_REQUEST_MAIL_ID`（-3）。選択可能アクションは `WEKO_WORKFLOW_ACTIONS`（Start/End/Item Registration/Approval/Item Link/Identifier Grant）、削除可能は `WEKO_WORKFLOW_DELETION_ACTIONS`（Start/End/Approval）。制限公開フローの編集は `_check_auth` によりシステム管理者限定。「プロパティを指定」候補は `get_specified_properties`（`"approval":true` プロパティ）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2024/01/19 | 8c312e8cb1db9c6479b86d1443a38720079838b0 | 制限公開機能追記 |
| 2025/01/23 | - | サブリポジトリ対応 |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | 要素の表示条件・アクセス権限を記載 |
