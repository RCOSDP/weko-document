### フロー

<!-- end list -->

  - > 目的・用途

本機能は、ワークフローに設定するフローの作成と編集を行う機能。

  - > 利用方法

【Administration＞ワークフロー管理（WorkFlow）＞フロー（Flow）】の順で画面遷移し利用する。

  - > 利用可能なロール

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
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 【Administration \> ワークフロー管理（WorkFlow） \> フロー（Flow）】のFlow Listに登録されたフローが一覧に表示される。
    
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

  - 「Create Flow」ボタンを押すと、フローの作成画面に移動する。
    
      - 「Flow Name」テキストボックスにフロー名を入力する。
    
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
    
    <!-- end list -->
    
      - 「Action Role」カラムに、アクションを実行するロールを限定できる。
        
          - 「Action Role」プルダウンから選択する。「Action Role」プルダウンの選択肢は現在システムに設定されたロールである。
        
          - 「表示しない（Deny）」チェックボックスにチェックを入れる場合、選択されているロールが実施不可とする。
    
      - 「Action User」カラムに、アクションを実行するユーザーを限定できる。
        
          - 「Action User」プルダウンから選択する。「Action User」プルダウンの選択肢は現在システムに登録されたユーザーである。
            
              - 「Approval」アクションに対して
                
                  - 選択肢はシステムに登録しているユーザーと、「プロパティを指定」(Specify Property)である
                    
                      - 「プロパティを指定」(Specify Property)を選択した場合、「プロパティを指定する」(Specify Property)モーダル画面を表示する。当該画面でプロパティを選択する。
                    
                      - モーダル画面には、プロパティ定義に「"approval":true」キーワードを持つプロパティ名を表示する。
                    
                      - モーダルに表示しているプロパティを選択して「設定」(Setting)ボタンを押すことで、プロパティを指定できる。
                    
                      - 「閉じる」（Close）ボタンを押すと、モーダルを閉じる。
                
                  - 「Approval」アクションごとにメールを自動送信するチェックボックスを追加する。
                    
                      - チェックボックス
                        
                          - 「承認依頼通知メール」（Approval Request Notification Email）  
                            承認者に承認を依頼するメールを送信する。
                        
                          - 「承認却下通知メール」（Approval Rejection Notification Email）  
                            登録者に承認者が却下された旨を通知するメールを送信する。
                        
                          - 「承認通知メール」（Approval Notification Email）  
                            登録者に承認者が承認された旨を通知するメールを送信する。
                    
                      - メール本文については、下記の「メール本文について」を参照。
        
          - 「Deny」チェックボックスにチェックを入れる場合、選択されているユーザーが実施不可とする。
    
    <!-- end list -->
    
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
            
              - \[無効（Unusable）\]ボタンを押すと、追加されたアクションがフローから削除される。追加されていないアクションの\[無効（Unusable）\]ボタンは非活性となる。
                
                  - 「Approval」アクションに対して、複数定義された場合、「無効」（Unusable）ボタンを押すと、アクション一覧に並ぶ「Approval」のうち枝番が一番大きいものから行われる
            
              - 各アクションの説明については、以下の通りである

| \# | アクション名            | 説明                            | 制限事項              |
| -- | ----------------- | ----------------------------- | ----------------- |
| 1  | Item Registration | アイテムのメタデータとコンテンツを登録するアクションである |                   |
| 2  | Item Link         | アイテムにリンク設定するアクションである          |                   |
| 3  | Identifier Grant  | アイテムにDOIを付与するアクションである         | Approvalの前で実行すること |
| 4  | Approval          | アイテムの査読／承認するアクションである          |                   |

  - フロー名のリンクを押すと、フローの編集画面に移動する
    
      - フローの編集画面で、フローの情報を編集できる
        
          - フローの情報を編集してから、\[保存（Save）ボタン\]を押すと、フローを編集し、メッセージを一覧画面の上部に表示する。  
            メッセージ：「Updated flow action successfully」
    
      - フローの編集画面で、\[削除（Delete）\]ボタンを押すと、フローを削除する。
        
          - 対象のフローがワークフローで使用されている場合、削除できない。\[削除（Delete）\]ボタンを押すと、エラーメッセージを表示する  
            エラーメッセージ：「Cannot be deleted because flow is used.」
    
      - フローの編集画面で、\[戻る（Back）\]ボタンを押すと、フロー一覧画面に移動する。

  - システム管理者でない（リポジトリ管理者）の場合、利用申請に関するフロー（利用申請フラグがONのワークフローと紐づいているフロー）は閲覧・保存・削除ができず、権限エラーとなる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_workflow

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - > \[Create Flow\]ボタンを押下しフロー作成画面に遷移すると、初期状態ではFlowNameテキストボックスに文字列を入力するか、\[戻る（Back）\]ボタン以外の操作は不可能である。

  - > Flow Nameテキストボックスに登録したいフロー名を入力後、\[保存（Save）\]ボタン押下で、weko\_workflow.admin.FlowSettingView.new\_flowが呼び出され、すでに登録されているフロー名と重複していないかのチェックがされ、重複がなければdb内のworkflow\_flow\_defineテーブルに情報が保存され、画面下部のアクション一覧が操作可能になる。また、Flow Statusの初期値は作成中（Maiking）である。

  - > \[More Action\]ボタンを押下すると、アクション一覧がモーダル表示されアクションの追加・削除・更新が可能となる。任意の項目の変更後、\[閉じる（Close）\]ボタン押下しアクション一覧画面を閉じたのちに、画面最下部の保存ボタン押下で、weko\_workflow.admin.FlowSettingView.upt\_flow\_actionが呼び出され、フローのアクションが変更される。また、その時のアクションの情報はdb内のworkflow\_flow\_actionテーブルに保存される。具体的なカラムとの対応は以下のようになる。
    
      - > created：アクションがフロー内に追加され、保存された時間。
    
      - > updated：もともと存在するフローを更新した際の時間。
    
      - > id：自動作番される数。個々のアクションの主キーとなる。
    
      - > flow\_id：そのアクションが追加されているフローを示すUUID。
    
      - > action\_id：アクション名に対応した数。対応は以下に示す通り。
        
          - > 1：Start
        
          - > 2：End
        
          - > 3：Item Registration
        
          - > 4：Approval
        
          - > 5：Item Link
        
          - > 6：OA Policy Confirmation
        
          - > 7：Identifier Grant
    
      - > Action\_version：アクションのバージョン。
    
      - > action\_order：そのアクションが何番目に動作するかを示した数。
    
      - > action\_condition
    
      - > action\_status：そのアクションが使用可能かを示す。可能であれば「A」、そうでなければ「N」
    
      - > action\_date：そのアクションが追加された時間。
    
      - > send\_mail\_setting：approvalのメールの送信設定が記載されている。

<!-- end list -->

  - > メール本文について

メール名：承認依頼通知メール

> Subject：利用申請の承認のお願い／Request for Approval of Application for Use
> 
> \[restricted\_institution\_name\_ja\]です。
> 
> \[restricted\_site\_name\_ja\]をご利用いただいて、ありがとうございます。
> 
> \[restricted\_university\_institution\]\[restricted\_fullname\]様から、下記の利用申請がありました。
> 
> 申請番号： \[restricted\_activity\_id\]
> 
> 登録者名： \[restricted\_fullname\]
> 
> メールアドレス： \[restricted\_mail\_address\]
> 
> 所属機関：\[restricted\_university\_institution\]
> 
> 研究題目：\[restricted\_research\_title\]
> 
> 申請データ：\[restricted\_data\_name\]
> 
> 申請年月日：\[restricted\_application\_date\]
> 
> \[restricted\_site\_name\_ja\]（\[restricted\_site\_url\]）にアクセスしていただき、画面左上からログインしていただけますと、「ワークフロー」タブが現れます。ここから上記の申請内容をご確認ください。「承認」または「却下」のボタンをクリックしてください。
> 
> このメールに心当たりのない方は、\[restricted\_site\_name\_ja\] までご連絡ください。
> 
> \[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]
> 
> 問い合わせ窓口：\[restricted\_site\_mail\]
> 
> \----------------------------------------------------------------------------------
> 
> This is a message from \[restricted\_site\_name\_en\].
> 
> We received the below application.
> 
> Application No.：\[restricted\_activity\_id\]
> 
> Name：\[restricted\_fullname\]
> 
> E-mail：\[restricted\_mail\_address\]
> 
> Affiliation：\[restricted\_university\_institution\]
> 
> Title of research：\[restricted\_research\_title\]
> 
> Dataset requested ：\[restricted\_data\_name\]
> 
> Application date：\[restricted\_application\_date\]
> 
> Please access \[restricted\_site\_name\_en\]（\[restricted\_site\_url\]） and log in from the upper left corner of the screen, and the \[Workflow\] tab will appear. From here, please confirm the above application by clicking on “approve” or “reject”.
> 
> If you received this message in error, please notify the \[restricted\_site\_name\_en\]
> 
> \[restricted\_site\_name\_en\]：\[restricted\_site\_url\]

E-mail：\[restricted\_site\_mail\]

メール名：承認却下通知メール

> Subject：利用申請の審査結果について／The results of the review of your application
> 
> \[restricted\_university\_institution\]
> 
> \[restricted\_fullname\]　様
> 
> \[restricted\_institution\_name\_ja\]です。
> 
> \[restricted\_site\_name\_ja\]をご利用いただいて、ありがとうございます。
> 
> 下記の利用申請を\[restricted\_institution\_name\_ja\]で審査した結果、申請データの提供を見送らせていただくことになりました。
> 
> 申請番号： \[restricted\_activity\_id\]
> 
> 登録者名： \[restricted\_fullname\]
> 
> メールアドレス： \[restricted\_mail\_address\]
> 
> 所属機関：\[restricted\_university\_institution\]
> 
> 研究題目：\[restricted\_research\_title\]
> 
> 申請データ：\[restricted\_data\_name\]
> 
> 申請年月日：\[restricted\_application\_date\]
> 
> このメールは自動送信されているので返信しないでください。
> 
> お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、\[restricted\_site\_name\_ja\] までご連絡ください。
> 
> \[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]
> 
> 問い合わせ窓口：\[restricted\_site\_mail\]
> 
> \----------------------------------------------------------------------------------
> 
> Dear \[restricted\_fullname\],
> 
> This is a message from \[restricted\_institution\_name\_en\].
> 
> Thank you for using \[restricted\_site\_name\_en\].
> 
> After reviewing the following application, \[restricted\_institution\_name\_en\] is sorry to inform you that your application has been rejected.
> 
> Application No.：\[restricted\_activity\_id\]
> 
> Name：\[restricted\_fullname\]
> 
> E-mail：\[restricted\_mail\_address\]
> 
> Affiliation：\[restricted\_university\_institution\]
> 
> Title of research：\[restricted\_research\_title\]
> 
> Dataset requested ：\[restricted\_data\_name\]
> 
> Application date：\[restricted\_application\_date\]
> 
> Please do not reply to this email as it has been sent automatically.
> 
> Please direct all inquiries to the following address.
> 
> Also, if you received this message in error, please notify \[restricted\_site\_name\_en\].
> 
> \[restricted\_site\_name\_en\]：\[restricted\_site\_url\]

E-mail：\[restricted\_site\_mail\]

メール名：承認通知メール

> Subject：利用申請の承認のお知らせ／Your application was approved
> 
> \[restricted\_university\_institution\]
> 
> \[restricted\_fullname\]　様
> 
> \[restricted\_institution\_name\_ja\]です。
> 
> \[restricted\_site\_name\_ja\]をご利用いただいて、ありがとうございます。
> 
> 下記の利用申請を承認しました。
> 
> 申請番号： \[restricted\_activity\_id\]
> 
> 登録者名： \[restricted\_fullname\]
> 
> メールアドレス： \[restricted\_mail\_address\]
> 
> 所属機関：\[restricted\_university\_institution\]
> 
> 研究題目：\[restricted\_research\_title\]
> 
> 申請データ：\[restricted\_data\_name\]
> 
> 申請年月日：\[restricted\_application\_date\]
> 
> データは、下記アドレスよりダウンロードすることができます。
> 
> \[restricted\_download\_link\]
> 
> データは、\[restricted\_site\_name\_ja\]から、\[restricted\_expiration\_date\]\[restricted\_expiration\_date\_ja\]までダウンロードすることができます。
> 
> ダウンロード期限を過ぎると、再申請が必要です。
> 
> このメールは自動送信されているので返信しないでください。
> 
> このメールに心当たりのない方は、\[restricted\_site\_name\_ja\]までご連絡ください。
> 
> \[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]
> 
> 問い合わせ窓口：\[restricted\_site\_mail\]
> 
> \----------------------------------------------------------------------------------
> 
> Dear \[restricted\_fullname\],
> 
> This is a message from \[restricted\_institution\_name\_en\].
> 
> Thank you for using \[restricted\_site\_name\_en\].
> 
> Your application below has been approved.
> 
> Application No.：\[restricted\_activity\_id\]
> 
> Name：\[restricted\_fullname\]
> 
> E-mail：\[restricted\_mail\_address\]
> 
> Affiliation：\[restricted\_university\_institution\]
> 
> Title of research：\[restricted\_research\_title\]
> 
> Dataset requested ：\[restricted\_data\_name\]
> 
> Application date：\[restricted\_application\_date\]
> 
> The data can be downloaded from the address below.
> 
> \[restricted\_download\_link\]
> 
> Above dataset is available to download from \[restricted\_site\_name\_en\] until \[restricted\_expiration\_date\]\[restricted\_expiration\_date\_en\].
> 
> You will need to resubmit your application once the link becomes unavailable.
> 
> Please do not reply to this email as it has been sent automatically.
> 
> If you received this message in error, please notify the \[restricted\_site\_name\_en\].
> 
> \[restricted\_site\_name\_en\]：\[restricted\_site\_url\]
> 
> E-mail：\[restricted\_site\_mail\]

埋め込み文字の整理

  - \[restricted\_site\_name\_ja\]：【Administration\>設定（Settings）\>Site Info】 に設定されている日本語のSite Name

  - \[restricted\_site\_name\_en\]：【Administration\>設定（Settings）\>Site Info】に設定されている英語のSite Name

  - \[restricted\_site\_url\]：「THEME\_SITEURL」 に設定されているURL

  - \[restricted\_site\_mail\]：【Administration\>設定（Setting）\>メール送信（Mail）】 のデフォルト送信元（Default sender）

  - \[restricted\_activity\_id\]：対象となる利用申請のアクティビティID

  - \[restricted\_fullname\]：利用申請アイテムタイプ項目の申請者・名前の設定値

  - \[restricted\_mail\_address\]：利用申請アイテムタイプ項目の申請者・メールアドレスの設定値

  - \[restricted\_university\_institution\]：利用申請アイテムタイプ項目の申請者・所属機関の設定値

  - \[restricted\_research\_title\]：利用申請アイテムタイプ項目の研究題目の設定値

  - \[restricted\_data\_name\]：利用申請アイテムタイプ項目のデータ名の設定値

  - \[restricted\_application\_date\]：利用申請アイテムタイプ項目の申請日の設定値

  - \[restricted\_download\_link\]：データファイルのURL

  - \[restricted\_expiration\_date\]：利用申請アイテムタイプ項目の承認日から【Administration\>設定（Setting）\>Restricted Access】のExpiration Date経過した日付

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
<td>2024/01/19</td>
<td>8c312e8cb1db9c6479b86d1443a38720079838b0</td>
<td>制限公開機能追記</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>