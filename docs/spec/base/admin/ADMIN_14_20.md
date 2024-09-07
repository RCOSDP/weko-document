### 制限公開(v1.0.7追加)

  - > 目的・用途

本機能は、制限公開に関する機能を設定し、利用報告督促メールを送付する機能である

  - > 利用方法

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

  - 使用している画面：【Admin \> Setting \> Restricted Access画面】：制限公開に関する機能を設定し、利用報告督促メールを送付する画面である

１．シークレットURLのダウンロードについて設定する

  - 「シークレットURLダウンロード」(Secret URL Download)エリアに、機能有効化、有効期限日数とダウンロード回数を設定する
    
      - 設定内容は以下とする
        
          - 「機能有効化」（Enable）
            
              - 初期値はチェック無しとする
            
              - チェックありで保存されている場合、シークレットURLボタンの表示機能が有効となる。
            
              - チェックなしの場合、「有効期限日数」（Expiration Date）「ダウンロード回数」（Download Limit）の各項目はすべて非活性となる。（他の活性条件に優先する）
        
        <!-- end list -->
        
          - 「有効期限日数」（Expiration Date）
            
              - 「有効期限日数」（Expiration Date）テキストボックス
                
                  - 初期値は30日とする
                
                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                    エラーメッセージ：  
                    日本語：「{}は1以上の整数を設定する必要があります。」  
                    英語：「Must set a positive integer for {}. 」
            
              - 「無期限にする」(Unlimited)チェックボックス
                
                  - チェックを入れる場合、パラメータ値を9999999日に設定することとする
                
                  - チェックを入れると、「有効期限日数」（Expiration Date）テキストボックスが非活性とする
            
              - 各シークレットURLの有効期限はURL発行時点で設定される
            
              - 未設定かつ「無期限にする」チェックボックスをチェックしていない場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                エラーメッセージ：  
                日本語：「{}を設定してください。」  
                英語：「Please set {}.」
        
          - 「ダウンロード回数」（Download Limit）
            
              - 「ダウンロード回数」（Download Limit）テキストボックス
                
                  - 初期値は10回とする
                
                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                    エラーメッセージ：  
                    日本語：「{}は1以上の整数を設定する必要があります。」  
                    英語：「Must set a positive integer for {}. 」
            
              - 「無期限にする」(Unlimited)チェックボックス
                
                  - チェックを入れる場合、パラメータ値を9999999日に設定することとする
                
                  - チェックを入れると、「ダウンロード回数」（Download Limit）テキストボックスが非活性とする
            
              - ダウンロードが途中で失敗した場合でも、1回のダウンロードとしてカウントする（サーバー側でダウンロードの成功有無は確認できないため）
            
              - 各シークレットURLのダウンロード回数はURL発行時点で設定される
            
              - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを表示する  
                メッセージ：  
                日本語：「制限公開の設定を変更しました。」  
                英語：「Restricted Access was successfully updated.」
            
              - 未設定かつ「無期限にする」チェックボックスをチェックしていない場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                エラーメッセージ：  
                日本語：「{}を設定してください。」  
                英語：「Please set {}.」

２. コンテンツファイルのダウンロードについて設定する

  - 「コンテンツファイルのダウンロード」(Content File Download)エリアに、有効期限日数とダウンロード回数を設定する
    
      - 設定内容は以下とする
        
          - 「有効期限日数」（Expiration Date）
            
              - 「有効期限日数」（Expiration Date）テキストボックス
                
                  - 初期値は30日とする
                
                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                    エラーメッセージ：  
                    日本語：「{}は1以上の整数を設定する必要があります。」  
                    英語：「Must set a positive integer for {}. 」
            
              - 「無期限にする」(Unlimited)チェックボックス
                
                  - チェックを入れる場合、パラメータ値を9999999日に設定することとする
                
                  - チェックを入れると、「有効期限日数」（Expiration Date）テキストボックスが非活性とする
            
              - ダウンロードリンクの有効期限は承認者が承認した時点で設定されること
            
              - 未設定かつ「無期限にする」チェックボックスをチェックしていない場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                エラーメッセージ：  
                日本語：「{}を設定してください。」  
                英語：「Please set {}.」
        
          - 「ダウンロード回数」（Download Limit）
            
              - 「ダウンロード回数」（Download Limit）テキストボックス
                
                  - 初期値は10回とする
                
                  - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                    エラーメッセージ：  
                    日本語：「{}は1以上の整数を設定する必要があります。」  
                    英語：「Must set a positive integer for {}. 」
            
              - 「無期限にする」(Unlimited)チェックボックス
                
                  - チェックを入れる場合、パラメータ値を9999999日に設定することとする
                
                  - チェックを入れると、「ダウンロード回数」（Download Limit）テキストボックスが非活性とする
            
              - ダウンロードが途中で失敗した場合でも、1回のダウンロードとしてカウントする（サーバー側でダウンロードの成功有無は確認できないため）
            
              - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを表示する  
                メッセージ：  
                日本語：「制限公開の設定を変更しました。」  
                英語：「Restricted Access was successfully updated.」
            
              - 未設定かつ「無期限にする」チェックボックスをチェックしていない場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                エラーメッセージ：  
                日本語：「{}を設定してください。」  
                英語：「Please set {}.」

３. 利用報告ワークフローへのアクセスについて設定する

  - 「利用報告ワークフローへのアクセス」(Usage Report Workflow Access)エリアに、有効期限日数を設定する
    
      - 設定内容は以下とする
        
          - 「有効期限日数」（Expiration Date）テキストボックス
            
              - 初期値は500日とする
            
              - 1以上の整数を入力する制御とする。不正な値を入力する場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
                エラーメッセージ：  
                日本語：「{}は1以上の整数を設定する必要があります。」  
                英語：「Must set a positive integer for {}. 」
        
          - 「無期限にする」(Unlimited)チェックボックス
            
              - チェックを入れる場合、パラメータ値を9999999日に設定することとする
            
              - チェックを入れると、「有効期限日数」（Expiration Date）テキストボックスが非活性とする
        
          - 
          - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを表示する  
            メッセージ：  
            日本語：「制限公開の設定を変更しました。」  
            英語：「Restricted Access was successfully updated.」
        
          - 未設定かつ「無期限にする」チェックボックスをチェックしていない場合、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
            エラーメッセージ：  
            日本語：「{}を設定してください。」  
            英語：「Please set {}.」

４. 利用規約について設定する

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
    メッセージ：  
    日本語：「制限公開の設定を変更しました。」  
    英語：「Restricted Access was successfully updated.」

  - 英語利用規約名、または英語利用規約文言を入力しない状態で、「保存」（Save）ボタンを押すと、エラーメッセージが表示される  
    エラーメッセージ：  
    日本語：「英語の利用規約を入力してください。」  
    英語：「Please input the Terms and Conditions in English.」

５. 利用報告督促メールを送付する

  - 「利用報告督促メール」（Usage Report Reminder Email）エリアには、利用報告督促メールの送信対象となるアクティビティの情報を一覧で表示する

  - 表示項目は以下の通りである
    
      - 一覧にはActivityの「No」「Activity」「Item」「Workflow」「Status」「User」を表示し、メール通知対象を選択するためのチェックボックスを設ける
    
      - 一覧の下に通知対象を確認させるため「確認」ボタンを設ける
    
      - 当該ボタンを押下するとモーダル画面開き、一覧でチェックボタンを選択した対象のみを表示す
    
      - 　 モーダル画面の「送信」ボタンを押下すると、メールが送信される。メールの送信が完了したらメッセージを表示する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_admin

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 設定内容をデータベースに保存する
    
      - テーブル：「admin\_settings」
    
      - フィールド：'name'="restricted\_access"  
        例：

> {"terms\_and\_conditions": \[{"key": "161699201191", "content": {"en": {"title": "Terms 1", "content": "Terms and Conditions Description"}, "ja": {"title": "利用規約1", "content": ""}}, "existed": true}\], "content\_file\_download": {"download\_limit": 10, "expiration\_date": 9999999, "download\_limit\_unlimited\_chk": false, "expiration\_date\_unlimited\_chk": true}, "usage\_report\_workflow\_access": {"expiration\_date\_access": 500, "expiration\_date\_access\_unlimited\_chk": false}}

  - > ゲストユーザーに対して、アクティビティ画面を表示する関数（"display\_guest\_activity"）には"record\_after\_update"変数を設定する

<!-- end list -->

  - > メール本文について

<!-- end list -->

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
> \----------------------------------------------------------------------------------
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
> \----------------------------------------------------------------------------------
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
> \----------------------------------------------------------------------------------
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

  - 【リポジトリ名（日本語）】：Admin\>Settings\>Site Info に設定されている日本語のSite Name

  - 【リポジトリ名（英語）】：Admin\>Setting\>Site Info に設定されている英語のSite Name

  - 【ゲストユーザ向けの利用申請WFへのアクセスリンク】： \#24088 で対応したテンポラリリンク

  - 【リポジトリURL】：「THEME\_SITEURL」 に設定されているURL

  - 【リポジトリメールアドレス】：Admin\>Setting\>Mail のDefault sender

  - 【申請番号】：対象となる利用申請のアクティビティID

  - 【申請者名前】：利用申請アイテムタイプ項目の申請者・名前の設定値

  - 【申請者メールアドレス】：利用申請アイテムタイプ項目の申請者・メールアドレスの設定値

  - 【申請者所属機関】：利用申請アイテムタイプ項目の申請者・所属機関の設定値

  - 【研究題目】：利用申請アイテムタイプ項目の研究題目の設定値

  - 【データ名】利用申請アイテムタイプ項目のデータ名の設定値

  - 【申請年月日】利用申請アイテムタイプ項目の申請日の設定値

  - 【ダウンロードリンク】： \#24088 で対応したテンポラリリンク

  - 【データのダウンロード期限日】：利用申請アイテムタイプ項目の承認日からAdmin\>Setting\>Restricted AccessのExpiration Date経過した日付

  - 【利用報告WFへのアクセスリンク】： \#24327 で対応したアクセスリンク

  - 【報告番号】：対象となる利用報告のアクティビティID

  - 【報告-申請者名前】：利用報告アイテムタイプ項目の申請者・名前の設定値

  - 【報告-申請者メールアドレス】：利用報告アイテムタイプ項目の申請者・メールアドレスの設定値

  - 【報告-申請者所属機関】：利用報告アイテムタイプ項目の申請者・所属機関の設定値

  - 【報告-データ名】：利用報告アイテムタイプ項目のデータ名の設定値

  - 【報告-WF起票日】：利用報告アイテムタイプ項目のWF起票日の設定値

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
<td><strong>8c312e8cb1db9c6479b86d1443a38720079838b0</strong></td>
<td>シークレットURL機能追加</td>
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
