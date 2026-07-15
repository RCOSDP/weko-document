### 制限公開(v1.0.7追加)

## 目的・用途

本機能は、制限公開に関する機能を設定し、利用報告督促メールを送付する機能である

## 利用方法

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

## 機能内容

  - 使用している画面：【Admin > Setting > Restricted Access画面】：制限公開に関する機能を設定し、利用報告督促メールを送付する画面である

１．コンテンツ未登録アイテムの利用申請について設定する

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 機能の有効無効はこの画面上で行うか、admin_settings テーブルの name が restricted_access であるレコードの settings 内の item_application.item_application_enable で設定可能

  - 「コンテンツ未登録アイテムの利用申請」(Application for use of items without content)エリアで機能有効化および、コンテンツ未登録状態で利用申請可能なアイテムタイプを設定する

      - 設定内容は以下とする。

          - 「機能有効化」

              - 「機能有効化」チェックボックス

                  - チェックを入れると、「コンテンツ未登録状態で利用申請可能なアイテムタイプ」および「コンテンツ未登録状態で利用申請不可能なアイテムタイプ」およびエリア移動ボタンが活性化する。

          - 「コンテンツ未登録状態で利用申請可能なアイテムタイプ」および「コンテンツ未登録状態で利用申請不可能なアイテムタイプ」

              - 「コンテンツ未登録状態で利用申請可能なアイテムタイプ」

                  - コンテンツ未登録アイテムの利用申請可能なアイテムタイプが一覧表示される。

              - 「コンテンツ未登録状態で利用申請不可能なアイテムタイプ」

                  - コンテンツ未 登録アイテムの利用申請できないアイテムタイプが一覧表示される。

              - 「コンテンツ未登録状態で利用申請可能なアイテムタイプ」からアイテムタイプを選択し、「右矢印」ボタンを押下することで、「コンテンツ未登録状態で利用申請不可能なアイテムタイプ」に移すことができる。

              - 「コンテンツ未登録状態で利用申請不可能なアイテムタイプ」からアイテムタイプを選択し、「左矢印」ボタンを押下することで、「コンテンツ未登録状態で利用申請可能なアイテムタイプ」に移すことができる。

２．各種制限公開機能の有効化、無効化について設定する。

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 機能の有効無効はこの画面上で行うか、admin_settings テーブルの name が restricted_access であるレコードの settings 内のそれぞれ以下の項目で設定可能

      - 承認アクションにおけるファイルプレビュー： preview_workflow_approval_enable

      - メールテンプレート編集： edit_mail_templates_enable

      - リクエストフォーム： display_request_form

      - 非ログインユーザーのDLにおけるパスワードチェック機能： password_enable

  - 各エリアで機能有効化を設定する。

      - 設定項目は以下とする。

          - 「承認アクションにおけるファイルプレビュー」エリア

          - 「メールテンプレート編集」エリア

          - 「リクエストフォーム」エリア
            
          - 「非ログインユーザーのDLにおけるパスワードチェック機能」エリア

      - 各設定項目の設定内容は以下とする。

          - 「機能有効化」

              - 「機能有効化」チェックボックス

                  - チェックを入れた状態で、「保存」ボタンを押下すると各種機能が有効化される。

３．シークレットURLのダウンロードについて設定する

  - 「シークレットURLダウンロード」(Secret URL Download)エリアに、機能有効化、有効期限日数とダウンロード回数、有効期限日数上限とダウンロード回数上限を設定する

      - 設定項目は以下の5つ

          - 「機能有効化」（Enable）

              - 初期値はチェック無しとする

              - チェックありで保存されている場合、シークレットURLボタンの表示機能が有効となる。

              - チェックなしの場合、「有効期限日数」（Expiration Date）「ダウンロード回数」（Download Limit）の各項目はすべて非活性となる。（他の活性条件に優先する）

          - 「有効期限初期値」（Initial Expiration Date）

              - 「有効期限日数」（Initial Expiration Date）テキストボックス

                  - 初期値は30日とする

                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}は1以上の整数を設定する必要があります。」

                      - 英語：「Must set a positive integer for {}. 」

                  - 各シークレットURLの有効期限はURL発行前に設定する。「有効期限日数」設定値は初期値として扱う。

                  - 未設定の場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}を設定してください。」

                      - 英語：「Please set {}.」

          - 「ダウンロード回数初期値」（Initial Download Limit）

              - 「ダウンロード回数」（Initial Download Limit）テキストボックス

                  - 初期値は10回とする

                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}は1以上の整数を設定する必要があります。」

                      - 英語：「Must set a positive integer for {}. 」

          - 「有効期限上限」

              - 「有効期限上限」（Expiration Date Limit）テキストボックス

                  - 初期値は30日、入力上限は30日とする。

                  - 1以上の整数を入力するよう制御する。上限以上の入力を行うと値を30に変える。「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}は1以上の整数を設定する必要があります。」

                      - 英語：「Must set a positive integer for {}. 」

          - 「ダウンロード回数上限」

              - 「ダウンロード回数上限」（Download frequency limit）テキストボックス

                  - 初期値は10回、入力上限は10回とする。

                  - 1以上の整数を入力するよう制御する。上限以上の入力を行うと値を10に変える。「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}は1以上の整数を設定する必要があります。」

                      - 英語：「Must set a positive integer for {}. 」

  - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを表示する

      - 日本語：「制限公開の設定を変更しました。」

      - 英語：「Restricted Access was successfully updated.」

４. コンテンツファイルのダウンロードについて設定する

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 「コンテンツファイルのダウンロード」(Content File Download)エリアに、有効期限日数とダウンロード回数を設定する

      - 設定内容は以下の2つ

          - 「有効期限日数」（Expiration Date）

              - 「有効期限日数」（Expiration Date）テキストボックス

                  - 初期値は30日とする

                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}は1以上の整数を設定する必要があります。」

                      - 英語：「Must set a positive integer for {}. 」

                  - 未設定の場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}を設定してください。」

                      - 英語：「Please set {}.」

          - 「ダウンロード回数」（Download Limit）

              - 「ダウンロード回数」（Download Limit）テキストボックス

                  - 初期値は10回とする

                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                      - 日本語：「{}は1以上の整数を設定する必要があります。」

                      - 英語：「Must set a positive integer for {}. 」

      - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを表示する

          - 日本語：「制限公開の設定を変更しました。」

          - 英語：「Restricted Access was successfully updated.」

５. 利用報告ワークフローへのアクセスについて設定する

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 「利用報告ワークフローへのアクセス」(Usage Report Workflow Access)エリアに、有効期限日数を設定する

      - 設定内容は以下とする

          - 「有効期限日数」（Expiration Date）テキストボックス

              - 初期値は500日とする

              - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

                  - 日本語：「{}は1以上の整数を設定する必要があります。」

                  - 英語：「Must set a positive integer for {}. 」

          - 「無期限」(Unlimited)チェックボックス

              - チェックを入れる場合、パラメータ値を9999999日に設定することとする

              - チェックを入れると、「有効期限日数」（Expiration Date）テキストボックスが非活性とする

          - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを表示する

              - 日本語：「制限公開の設定を変更しました。」

              - 英語：「Restricted Access was successfully updated.」

          - 未設定かつ「無期限」チェックボックスをチェックしていない場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

              - 日本語：「{}を設定してください。」

              - 英語：「Please set {}.」

６. 利用規約について設定する

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 設定内容は以下の通りです。

      - 利用規約名一覧

          - 英語の利用規約名を表示する

          - 利用規約名の右端に「×」を設け、押下すると削除対象とする。削除は「保存」ボタン押下時に確定する

          - 末尾には「追加」（Add）を表示し、選択時は利用規約を新規登録する

      - 日本語利用規約名入力エリア

          - 日本語の利用規約名を設定するテキストボックス

          - アイテム登録時にWEKO3の表示言語設定が日本語の場合、選択肢として表示する項目

      - 日本語利用規約文言入力エリア

          - 登録する利用規約（日本語）の文言を入力するテキストエリア

          - 文字数上限は設けない

      - 英語利用規約名入力エリア

          - 英語の利用規約名を設定するテキストボックス。必須項目とする

          - アイテム登録時にWEKO3の表示言語設定が日本語以外の場合、選択肢として表示する項目

      - 英語利用規約文言入力エリア

          - 登録する利用規約（英語）の文言を入力するテキストエリア。必須項目とする

          - 文字数上限は設けない

  - 設定した後、「保存」（Save）ボタンを押すことで、設定している利用規約を利用規約名一覧に追加し、メッセージを表示する

      - 日本語：「制限公開の設定を変更しました。」

      - 英語：「Restricted Access was successfully updated.」

  - 英語利用規約名、または英語利用規約文言を入力しない状態で、「保存」（Save）ボタンを押すと、エラーメッセージが表示される

      - 日本語：「英語の利用規約を入力してください。」

      - 英語：「Please input the Terms and Conditions in English.」

７. 利用報告督促メールを送付する

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 「利用報告督促メール」（Usage Report Reminder Email）エリアには、利用報告督促メールの送信対象となるアクティビティの情報を一覧で表示する

  - 表示項目は以下の通りである

      - 一覧にはActivityの「No」「Activity」「Item」「Workflow」「Status」「User」を表示し、メール通知対象を選択するためのチェックボックスを設ける

      - 一覧の下に通知対象を確認させるため「確認」ボタンを設ける

      - 当該ボタンを押下するとモーダル画面開き、一覧でチェックボタンを選択した対象のみを表示す

      - 　 モーダル画面の「送信」ボタンを押下すると、メールが送信される。メールの送信が完了したらメッセージを表示する

## 関連モジュール

  - weko_admin

## 処理概要

  - 設定内容をデータベースに保存する

      - テーブル：「admin_settings」

      - フィールド：'name'="restricted_access"
        例：

> {"terms_and_conditions": [{"key": "161699201191", "content": {"en": {"title": "Terms 1", "content": "Terms and Conditions Description"}, "ja": {"title": "利用規約1", "content": ""}}, "existed": true}], "content_file_download": {"download_limit": 10, "expiration_date": 9999999, "download_limit_unlimited_chk": false, "expiration_date_unlimited_chk": true}, "usage_report_workflow_access": {"expiration_date_access": 500, "expiration_date_access_unlimited_chk": false}}

  - ゲストユーザーに対して、アクティビティ画面を表示する関数（"display_guest_activity"）には"record_after_update"変数を設定する

  - メール本文について

  - メール名：利用申請WFの通知メール

> Subject: 利用申請登録のご案内／Register Application for Use
>
> 【リポジトリ名（日本語）】です。
>
> 下記のリンクにアクセスしていただき、利用申請の登録を行ってください。
>
> 【ゲストユーザ向けの利用申請WFへのアクセスリンク】
>
> このメールは自動送信されているので返信しないでください。
>
> お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、【リポジトリ名（日本語）】までご連絡ください。
>
> 【リポジトリ名（日本語）】：【リポジトリURL】
>
> 問い合わせ窓口：【リポジトリメールアドレス】
>
> ----------------------------------------------------------------------------------
>
> This is a message from 【リポジトリ名（英語）】.
>
> Please access the link below and register your Application.
>
> 【ゲストユーザ向けの利用申請WFへのアクセスリンク】
>
> Please do not reply to this email as it has been sent automatically.
>
> Please direct all inquiries to the following address.
>
> Also, if you received this message in error, please notify 【リポジトリ名（英語）】.
>
> 【リポジトリ名（英語）】：【URL】
>
> E-mail：【リポジトリメールアドレス】

  - メール名：利用報告WFの通知メール

> Subject: 利用報告の登録のお願い／Request for register Data Usage Report
>
> 【リポジトリ名（日本語）】です。
>
> 下記で申請いただいデータについてダウンロードされたことを確認しました。
>
> 申請番号：【申請番号】
>
> 登録者名：【申請者名前】
>
> メールアドレス：【申請者メールアドレス】
>
> 所属機関：【申請者所属機関】
>
> 研究題目：【研究題目】
>
> 申請データ：【データ名】
>
> 申請年月日：【申請年月日】
>
> ダウンロードしたデータについて、下記のリンクから利用報告の登録をお願いします。
>
> 【利用報告WFへのアクセスリンク】
>
> このメールは自動送信されているので返信しないでください。
>
> お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、【リポジトリ名（日本語）】までご連絡ください。
>
> 【リポジトリ名（日本語）】：【リポジトリURL】
>
> 問い合わせ窓口：【リポジトリメールアドレス】
>
> ----------------------------------------------------------------------------------
>
> This is a message from 【リポジトリ名（英語）】.
>
> We have confirmed that the dataset which you registered at below has been downloaded.
>
> Application No.：【申請番号】
>
> Name：【申請者名前】
>
> E-mail：【メールアドレス】
>
> Affiliation：【申請者所属機関】
>
> Title of research：【研究題目】
>
> Dataset requested ：【データ名】
>
> Application date：【申請年月日】
>
> For the downloaded data, please register the Data Usage Report by the link below.
>
> 【利用報告WFへのアクセスリンク】
>
> Please do not reply to this email as it has been sent automatically.
>
> Please direct all inquiries to the following address.
>
> Also, if you received this message in error, please notify 【リポジトリ名（英語）】.
>
> 【リポジトリ名（英語）】：【URL】
>
> E-mail：【リポジトリメールアドレス】

  - メール名：利用報告督促メール

> Subject: 利用報告の登録のお願い／Request for register Data Usage Report
>
> 【リポジトリ名（日本語）】です。
>
> 現時点で、下記の利用報告が登録されていません
>
> 報告番号：【報告番号】
>
> 登録者名：【報告-申請者名前】
>
> メールアドレス：【報告-申請者メールアドレス】
>
> 所属機関：【報告-申請者所属機関】
>
> 利用データ：【報告-データ名】
>
> データダウンロード日：【報告-WF起票日】
>
> 下記のリンクから利用報告の登録をお願いします。
>
> 【利用報告WFへのアクセスリンク】
>
> このメールは自動送信されているので返信しないでください。
>
> お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、【リポジトリ名（日本語）】までご連絡ください。
>
> 【リポジトリ名（日本語）】：【リポジトリURL】
>
> 問い合わせ窓口：【リポジトリメールアドレス】
>
> ----------------------------------------------------------------------------------
>
> This is a message from 【リポジトリ名（英語）】.
>
> At this time, the Data Usage Report below has not been registered.
>
> Usage Report No.：【報告番号】
>
> Name：【報告-申請者名前】
>
> E-mail：【報告-申請者メールアドレス】
>
> Affiliation：【報告-申請者所属機関】
>
> Usage Dataset：【報告-データ名】
>
> Download date：【報告-WF起票日】
>
> Please register the Data Usage Report from the link below.
>
> 【利用報告WFへのアクセスリンク】
>
> Please do not reply to this email as it has been sent automatically.
>
> Please direct all inquiries to the following address.
>
> Also, if you received this message in error, please notify 【リポジトリ名（英語）】.
>
> 【リポジトリ名（英語）】：【URL】
>
> E-mail：【リポジトリメールアドレス】

埋め込み文字の整理

  - 【リポジトリ名（日本語）】：Admin>Settings>Site Info に設定されている日本語のSite Name

  - 【リポジトリ名（英語）】：Admin>Setting>Site Info に設定されている英語のSite Name

  - 【ゲストユーザ向けの利用申請WFへのアクセスリンク】： #24088 で対応したテンポラリリンク

  - 【リポジトリURL】：「THEME_SITEURL」 に設定されているURL

  - 【リポジトリメールアドレス】：Admin>Setting>Mail のDefault sender

  - 【申請番号】：対象となる利用申請のアクティビティID

  - 【申請者名前】：利用申請アイテムタイプ項目の申請者・名前の設定値

  - 【申請者メールアドレス】：利用申請アイテムタイプ項目の申請者・メールアドレスの設定値

  - 【申請者所属機関】：利用申請アイテムタイプ項目の申請者・所属機関の設定値

  - 【研究題目】：利用申請アイテムタイプ項目の研究題目の設定値

  - 【データ名】利用申請アイテムタイプ項目のデータ名の設定値

  - 【申請年月日】利用申請アイテムタイプ項目の申請日の設定値

  - 【ダウンロードリンク】： #24088 で対応したテンポラリリンク

  - 【データのダウンロード期限日】：利用申請アイテムタイプ項目の承認日からAdmin>Setting>Restricted AccessのExpiration Date経過した日付

  - 【利用報告WFへのアクセスリンク】： #24327 で対応したアクセスリンク

  - 【報告番号】：対象となる利用報告のアクティビティID

  - 【報告-申請者名前】：利用報告アイテムタイプ項目の申請者・名前の設定値

  - 【報告-申請者メールアドレス】：利用報告アイテムタイプ項目の申請者・メールアドレスの設定値

  - 【報告-申請者所属機関】：利用報告アイテムタイプ項目の申請者・所属機関の設定値

  - 【報告-データ名】：利用報告アイテムタイプ項目のデータ名の設定値

  - 【報告-WF起票日】：利用報告アイテムタイプ項目のWF起票日の設定値

８. 制限公開アイテムに非対象ユーザーがアクセスを試みた際に表示されるエラーメッセージについて設定する

  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True の場合のみ表示

  - 「エラーメッセージ」（Error Message）テキストエリアで、日本語と英語それぞれのエラーメッセージを編集できる。テキストエリアには初期状態として以下のエラーメッセージが記載されている。  
     エラーメッセージ  
     日本語：「このデータは利用できません（権限がないため）。」  
     英語：「This data is not available for this user.」

  - [保存（Save）]ボタンを押すと、設定内容を保存し、メッセージを表示する。  
    ただし、「エラーメッセージ」（Error Message）テキストエリアが空白である場合に保存を行うことはできない。  
    メッセージ  
    日本語：「制限公開の設定を変更しました。」
    英語：「Restricted Access was successfully updated.」

## 関連モジュール
    
  - weko_admin
    
## 処理概要
    
  - 設定内容をデータベースに保存する

      - テーブル：「admin_settings」

      - フィールド：'name'="restricted_access"  
        例：
        > {"error_msg": {"key": "", "content": {"en": {"content": "This data is not available for this user"}, "ja": {"content": "このデータは利用できません（権限がないため）。"}}},{"terms_and_conditions": [{"key": "161699201191", "content": {"en": {"title": "Terms 1", "content": "Terms and Conditions Description"}, "ja": {"title": "利用規約1", "content": ""}}, "existed": true}], "content_file_download": {"download_limit": 10, "expiration_date": 9999999, "download_limit_unlimited_chk": false, "expiration_date_unlimited_chk": true}, "usage_report_workflow_access": {"expiration_date_access": 500, "expiration_date_access_unlimited_chk": false}}}
        
  - ゲストユーザーに対して、アクティビティ画面を表示する関数（"display_guest_activity"）には"record_after_update"変数を設定する

  - データベース内に"error_msg"というキーを持たない場合は、weko_admin.utils.get_restricted_access で初期状態のものが作成される。その後、設定が変更されるたび値が更新される。

## 設定値
    
      - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG
        
          - パス：<https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/weko-admin/weko_admin/config.py#L1298>

          - 初期値：False

          - 制限公開機能の設定画面表示非表示および利用申請系機能と制限公開コンテンツ機能の有効無効を切り替える。

          - scripts/instance.cfg で定義されている場合は、そちらの設定を優先する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_admin.admin.RestrictedAccessSettingView`（endpoint `restricted_access`）。保存は `views.save_restricted_access`（`/restricted_access/save`）→ `utils.update_restricted_access`。設定は `AdminSettings`（name=`restricted_access`。フィールド：`item_application` / `preview_workflow_approval_enable` / `edit_mail_templates_enable` / `display_request_form` / `password_enable` / `secret_URL_file_download` / `content_file_download` / `usage_report_workflow_access` / `terms_and_conditions` / `error_msg`）。
- 実装補足（追記）：画面（メニュー）の表示可否は `WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS`（既定 **True**、`ext.py`）で制御され、各セクションの表示は `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG`（既定 **False**）で制御される（両者は別物）。「無期限」は `WEKO_ADMIN_RESTRICTED_ACCESS_MAX_INTEGER`（9999999）。`edit_mail_templates_enable=False` で保存すると `reset_flow_action_roles_restricted_access` が走る。error_msg 既定は `WEKO_ADMIN_RESTRICTED_ACCESS_ERROR_MESSAGE`。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | 各機能の表示・有効の条件を追加 |
| 2024/07/12 | a27f536b5e375ada10a651ba1f13a589c9243ca1 | コンテンツ未登録アイテムの利用申請設定、各種制限公開機能の有効化、無効化設定機能追加 |
| 2024/01/19 | 8c312e8cb1db9c6479b86d1443a38720079838b0 | シークレットURL機能追加 |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
