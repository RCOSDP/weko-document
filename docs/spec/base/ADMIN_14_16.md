### メール送信

  - > 目的・用途

本機能は、送信元の情報を設定する機能である

  - > 利用方法

【Administration \> 設定（Setting） \> メール送信（Mail）画面】に送信元の情報を設定する

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 「Mail Setting」にてメールサーバの設定をする
    
      - 設定項目は以下の通りである
        
          - 「SMTPサーバ（Server）」：メールサーバ
            
              - デフォルト：「localhost」
        
          - 「ポート（Port）」：メールポート
            
              - デフォルト：「25」
        
          - 「TLSを使用する（Use TLS）」
            
              - デフォルト：チェックなし
        
          - 「SSLを使用する（Use SSL）」
            
              - デフォルト：チェックなし
        
          - 「ユーザー名（Username）」
            
              - デフォルト：空白
        
          - 「パスワード（Password）」
            
              - デフォルト：空白
        
          - 「ドメイン（Domain）(v1.0.7追加)」
            
              - デフォルト：空白
        
          - 「デフォルト送信元（Default sender）」
            
              - デフォルト：空白
    
      - ［更新（Update）］ボタンを押すと、入力内容を確認し、エラーなしの場合、設定内容を保存し、メッセージを画面上部に表示する  
        　メッセージ：  
        　日本語：「メールの設定を更新しました」  
        　英語：「Mail settings have been updated.」
    
      - エラーの場合は以下の通りである
        
          - 「Server」に入力しない場合  
            エラーメッセージ：「Mail server can't be empty.」
        
          - 「Port」に入力しない場合  
            エラーメッセージ：「Mail port can't be empty.」
        
          - 「Default sender」に入力しない場合  
            エラーメッセージ：「Mail default sender can't be empty.」

  - 「Send Test Mail」にてテストメール送信を行う
    
      - 設定項目は以下の通りである
        
          - 「送信先（Recipient）」
        
          - 「主題（Subject）」
        
          - 「本文（Body）」
    
      - ［送信（Enable）］ボタンを押すと、設定内容でメールの送信を行う
        
          - 送信が成功の場合、以下のメッセージを画面上部に表示する  
            　メッセージ：  
            　日本語：「テストメールを送信しました。」  
            　英語：「Test mail sent.」
        
          - 送信が失敗の場合、以下のメッセージ及びエラーコードを画面上部に表示する  
            メッセージ：「Failed to send mail.」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio-mail

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 画面表示時は、invenio\_mail.admin.MailSettingVIew.indexメソッドがGETで呼び出される
    
      - このとき、mail\_configテーブルからメールサーバの設定を取得する
        
          - invenio\_mail.models.MailConfig.get\_configメソッドの中で、設定が取得できなかった場合は、デフォルトの内容のレコードを作成してからそれを取得する
    
      - 「Mail Setting」の内容を取得したもの、「Send Test Mail」の内容を空欄として表示する

  - ［更新（Update）］ボタンを押すと、invenio\_mail.admin.MailSettingVIew.indexメソッドがPOSTで呼び出される
    
      - エラーチェックを通過した場合、mail\_configテーブルのレコードを更新する
        
          - invenio\_mail.models.MailConfig.set\_configメソッドによって、１つのレコードを更新する
    
      - その後、「Mail Setting」の内容を画面で入力したもの、「Send Test Mail」の内容を空欄として画面に表示する

  - ［送信（Enable）］ボタンを押すと、invenio\_mail.admin.MailSettingVIew.send\_test\_mailメソッドが呼び出される
    
      - mail\_configテーブルから取得した情報をメールサーバの各種設定として、「Send Test Mail」の各入力欄に入力したものをメッセージとしてcurrent\_app.extensions\['mail'\]に設定して、送信する
    
      - その後、「Mail Setting」の内容をテーブルから取得したもの、「Send Test Mail」の内容を空欄として画面に表示する

  - 「ドメイン（Domain）」の値を持ちいて送信元ドメインを設定する。

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
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2023/11/11</p>
</blockquote></td>
<td>V0.9.23</td>
<td></td>
</tr>
</tbody>
</table>