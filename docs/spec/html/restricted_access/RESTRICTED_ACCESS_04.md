### メールテンプレート

※v0.9.22現在、未実装。今後リリースの予定

  - 使用している画面  
    【Admin \> Setting \> メールテンプレート】：自動送信メールのタイトル、文面を設定する画面である

  - 自動送信メールの内容を設定する

  - 【Admin \> Setting \> メールテンプレート】に送信元の情報を設定する
    
      - 「Mail Template」にてメール文面の設定をする
    
      - 送信者は「設定」-\[メール送信\]-\[Mail Setting\]で設定したユーザー

設定項目は以下の2つである

  - Subject：メールタイトル

  - (メール内容）：メール内容

デフォルトで以下のメールが設定されており、それぞれ制限公開機能で用いる自動送信メールに関係している

*① 非ログインユーザに利用申請ワークフローURLを送信する  
Subject: 利用申請登録のご案内／Register Application for Use  
本文:  
\[restricted\_site\_name\_ja\]です。  
下記のリンクにアクセスしていただき、利用申請の登録を行ってください。*

*\[url\_guest\_user\]*

*このメールは自動送信されているので返信しないでください。  
お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、\[restricted\_site\_name\_ja\]までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*This is a message from \[restricted\_site\_name\_en\].  
Please access the link below and register your Application.*

*\[url\_guest\_user\]*

*Please do not reply to this email as it has been sent automatically.  
Please direct all inquiries to the following address.  
Also, if you received this message in error, please notify \[restricted\_site\_name\_en\].*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]  
E-mail：\[restricted\_site\_mail\]*

*② 利用者に対して、利用申請登録のリマインドを行う  
Subject: データ利用申請の受付のお知らせ／Your Application was Received  
本文:  
\[restricted\_institution\_name\_ja\]です。  
\[restricted\_site\_name\_ja\]をご利用いただいて、ありがとうございます。*

*下記の利用申請を受け付けました。*

*申請番号： \[restricted\_activity\_id\]  
登録者名： \[restricted\_fullname\]  
メールアドレス： \[restricted\_mail\_address\]  
所属機関：\[restricted\_university\_institution\]  
研究題目：\[restricted\_research\_title\]  
申請データ：\[restricted\_data\_name\]  
申請年月日：\[restricted\_application\_date\]*

*\[restricted\_institution\_name\_ja\]で審査しますので、結果の連絡をお待ちください。*

*このメールは自動送信されているので返信しないでください。  
お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、\[restricted\_institution\_name\_ja\]までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*Dear \[restricted\_fullname\],*

*This is a message from \[restricted\_institution\_name\_en\].  
Thank you for using \[restricted\_site\_name\_en\].*

*We received the below application:*

*Application No.：\[restricted\_activity\_id\]  
Name：\[restricted\_fullname\]  
E-mail：\[restricted\_mail\_address\]  
Affiliation：\[restricted\_university\_institution\]  
Title of research：\[restricted\_research\_title\]  
Dataset requested ：\[restricted\_data\_name\]  
Application date：\[restricted\_application\_date\]*

*You will be notified once the application is approved.*

*Please do not reply to this email as it has been sent automatically.  
Please direct all inquiries to the following address.  
Also, if you received this message in error, please notify \[restricted\_institution\_name\_en\].*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]  
E-mail：\[restricted\_site\_mail\]*

*③ 承認者に対して、利用申請の承認の依頼を行う  
Subject: 利用申請の承認のお願い／Request for Approval of Application for Use  
本文:  
\[restricted\_site\_name\_ja\]です。下記の方から利用申請がありました。*

*申請番号： \[restricted\_activity\_id\]  
登録者名： \[restricted\_fullname\]  
メールアドレス： \[restricted\_mail\_address\]  
所属機関：\[restricted\_university\_institution\]  
研究題目：\[restricted\_research\_title\]  
申請データ：\[restricted\_data\_name\]  
申請年月日：\[restricted\_application\_date\]*

*\[restricted\_site\_name\_ja\]（\[restricted\_site\_url\]）にアクセスしていただき、画面左上からログインしていただけますと、「ワークフロー」タブが現れます。ここから上記の申請内容をご確認ください。「承認」または「却下」のボタンをクリックしてください。*

*このメールに心当たりのない方は、\[restricted\_site\_name\_ja\] までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*This is a message from \[restricted\_site\_name\_en\].  
We received the below application.*

*Application No.：\[restricted\_activity\_id\]  
Name：\[restricted\_fullname\]  
E-mail：\[restricted\_mail\_address\]  
Affiliation：\[restricted\_university\_institution\]  
Title of research：\[restricted\_research\_title\]  
Dataset requested ：\[restricted\_data\_name\]  
Application date：\[restricted\_application\_date\]*

*Please access \[restricted\_site\_name\_en\]（\[restricted\_site\_url\]） and log in from the upper left corner of the screen, and the \[Workflow\] tab will appear. From here, please confirm the above application by clicking on “approve” or “reject”.*

*If you received this message in error, please notify the \[restricted\_site\_name\_en\]*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]  
E-mail：\[restricted\_site\_mail\]*

*④ 申請者に対して、利用申請が承認されたことを伝え、ダウンロードリンクを送付する  
Subject: 利用申請の承認のお知らせ／Your application was approved  
本文:  
\[restricted\_site\_name\_ja\]です。*

*下記の利用申請を承認しました。*

*申請番号： \[restricted\_activity\_id\]  
登録者名： \[restricted\_fullname\]  
メールアドレス： \[restricted\_mail\_address\]  
所属機関：\[restricted\_university\_institution\]  
研究題目：\[restricted\_research\_title\]  
申請データ：\[restricted\_data\_name\]  
申請年月日：\[restricted\_application\_date\]*

*データは、下記アドレスよりダウンロードすることができます。*

*\[restricted\_download\_link\]*

*当日より\[restricted\_expiration\_date\]\[restricted\_expiration\_date\_ja\]日後まで有効です。ダウンロード期限を過ぎると、再申請が必要です。*

*このメールは自動送信されているので返信しないでください。  
このメールに心当たりのない方は、\[restricted\_site\_name\_ja\]までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*This is a message from \[restricted\_site\_name\_en\].  
Your application below has been approved.*

*Application No.：\[restricted\_activity\_id\]  
Name：\[restricted\_fullname\]  
E-mail：\[restricted\_mail\_address\]  
Affiliation：\[restricted\_university\_institution\]  
Title of research：\[restricted\_research\_title\]  
Dataset requested ：\[restricted\_data\_name\]  
Application date：\[restricted\_application\_date\]*

*The data can be downloaded from the address below.*

*\[restricted\_download\_link\]*

*It is valid from that day until the day after \[restricted\_expiration\_date\]\[restricted\_expiration\_date\_en\]. You will need to resubmit your application once the link becomes unavailable.*

*Please do not reply to this email as it has been sent automatically.  
If you received this message in error, please notify the \[restricted\_site\_name\_en\].*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]  
E-mail：\[restricted\_site\_mail\]*

*⑤ 申請者に対して、利用申請が却下されたことを伝える  
Subject: 利用申請の審査結果について／The results of the review of your application  
本文:  
\[restricted\_site\_name\_ja\]です。*

*下記の利用申請を却下しました。*

*申請番号： \[restricted\_activity\_id\]  
登録者名： \[restricted\_fullname\]  
メールアドレス： \[restricted\_mail\_address\]  
所属機関：\[restricted\_university\_institution\]  
研究題目：\[restricted\_research\_title\]  
申請データ：\[restricted\_data\_name\]  
申請年月日：\[restricted\_application\_date\]*

*このメールは自動送信されているので返信しないでください。  
お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、\[restricted\_site\_name\_ja\] までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*This is a message from \[restricted\_site\_name\_en\].  
Your application below has been rejected.*

*Application No.：\[restricted\_activity\_id\]  
Name：\[restricted\_fullname\]  
E-mail：\[restricted\_mail\_address\]  
Affiliation：\[restricted\_university\_institution\]  
Title of research：\[restricted\_research\_title\]  
Dataset requested ：\[restricted\_data\_name\]  
Application date：\[restricted\_application\_date\]*

*Please do not reply to this email as it has been sent automatically.  
Please direct all inquiries to the following address.  
Also, if you received this message in error, please notify \[restricted\_site\_name\_en\].*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]  
E-mail：\[restricted\_site\_mail\]*

*⑥ DLリンクをクリックし、DLした申請者に対して利用報告のアドレスが送付される  
Subject: 利用報告の登録のお願い／Request for register Data Usage Report  
本文:  
\[restricted\_site\_name\_ja\]です。  
下記で申請いただいデータについてダウンロードされたことを確認しました。*

*申請番号： \[restricted\_usage\_activity\_id\]  
登録者名： \[restricted\_fullname\]  
メールアドレス： \[restricted\_mail\_address\]  
所属機関：\[restricted\_university\_institution\]  
研究題目：\[restricted\_research\_title\]  
申請データ：\[restricted\_data\_name\]  
申請年月日：\[restricted\_application\_date\]*

*ダウンロードしたデータについて、下記のリンクから利用報告の登録をお願いします。*

*\[usage\_report\_url\]*

*このメールは自動送信されているので返信しないでください。  
お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、\[restricted\_site\_name\_ja\]までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*This is a message from \[restricted\_site\_name\_en\].  
We have confirmed that the dataset which you registered at below has been downloaded.*

*Application No.：\[restricted\_usage\_activity\_id\]  
Name：\[restricted\_fullname\]  
E-mail：\[restricted\_mail\_address\]  
Affiliation：\[restricted\_university\_institution\]  
Title of research：\[restricted\_research\_title\]  
Dataset requested ：\[restricted\_data\_name\]  
Application date：\[restricted\_application\_date\]*

*For the downloaded data, please register the Data Usage Report by the link below.*

*\[usage\_report\_url\]*

*Please do not reply to this email as it has been sent automatically.  
Please direct all inquiries to the following address.  
Also, if you received this message in error, please notify \[restricted\_site\_name\_en\].*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]*

*E-mail：\[restricted\_site\_mail\]*

*⑦ 管理者画面より、申請者に対して利用報告のリマインドを行う  
Subject: 利用報告の登録のお願い／Request for register Data Usage Report  
本文:  
\[restricted\_site\_name\_ja\]です。  
現時点で、下記の利用報告が登録されていません*

*報告番号：\[restricted\_activity\_id\]  
登録者名：\[restricted\_fullname\]  
メールアドレス：\[restricted\_mail\_address\]  
所属機関：\[restricted\_university\_institution\]  
利用データ：\[restricted\_data\_name\]  
データダウンロード日：\[data\_download\_date\]*

*下記のリンクから利用報告の登録をお願いします。*

*\[usage\_report\_url\]*

*このメールは自動送信されているので返信しないでください。  
お問い合わせは下記までお願いします。また、このメールに心当たりのない方は、\[restricted\_site\_name\_ja\]までご連絡ください。*

*\[restricted\_site\_name\_ja\]：\[restricted\_site\_url\]  
問い合わせ窓口：\[restricted\_site\_mail\]*

*This is a message from \[restricted\_site\_name\_en\].  
At this time, the Data Usage Report below has not been registered.*

*Usage Report No.：\[restricted\_activity\_id\]  
Name：\[restricted\_fullname\]  
E-mail：\[restricted\_mail\_address\]  
Affiliation：\[restricted\_university\_institution\]  
Usage Dataset：\[restricted\_data\_name\]  
Download date：\[data\_download\_date\]*

*Please register the Data Usage Report from the link below.*

*\[usage\_report\_url\]*

*Please do not reply to this email as it has been sent automatically.  
Please direct all inquiries to the following address.  
Also, if you received this message in error, please notify \[restricted\_site\_name\_en\].*

*\[restricted\_site\_name\_en\]：\[restricted\_site\_url\]  
E-mail：\[restricted\_site\_mail\]*

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
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>