
### パスワードリセット

  - > 目的・用途

当機能は、パスワードを忘れてログインできないユーザーが再設定できるようにする機能である。

  - > 利用方法

ログイン画面で、「パスワードをお忘れの方はこちら」リンクを押す。

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
<td>○</td>
<td>○</td>
<td>○</td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - リセットパスワード画面を以下のように設ける
    
      - 表示言語はヘッダに選択しているシステム言語とする
    
      - 説明内容  
        日本語：「メールアドレスを入力していただき、パスワードリセット用のリンクをお送りいたします。」  
        英語：「Enter your email address below and we will send you a link to reset your password.」
    
      - メールアドレステキストボックス
    
      - ［リセットパスワード（Reset Password）］ボタン、 「ログイン」（Log in）リンク、「サインアップ」（Sign Up）リンク

  - ［リセットパスワード（Reset Password）］ボタンを押すと、入力したメールアドレスをチェックする
    
      - メールアドレスがシステムに登録されたものである場合、リセットパスワードのリンクを含むメールを送信する
        
          - メールを送信した後、リセットパスワード画面に説明内容を表示する  
            内容：「Instructions to reset your password have been sent to {}.」
    
      - この段階で、もともとのパスワードでログインすることはできなくなる
    
      - エラーがあった場合、エラー内容をメールアドレスのテキストボックスの下部に表示させる
        
          - メールアドレスの形式が不正である場合  
            エラーメッセージ：「Invalid email address」
        
          - メールアドレスがシステムに登録されたものではない場合  
            エラーメッセージ：「Specified user does not exist」

  - リセットパスワードリンクにアクセスする
    
      - メール本文から、リンクをクリックすると、リセットパスワード画面に移動される
        
          - リセットパスワード画面に「パスワード入力」、「パスワード再入力」テキストボックスを設ける
        
          - 「パスワード入力」、「パスワード再入力」を入力した後、［リセットパスワード（Reset Password）］ボタンを押すと、入力した情報をチェックする
            
              - それぞれのテキストボックスには、キーボードからは半角英数字のみ入力できるように入力制限がかかっている
        
          - チェック上、問題なければ、パスワードが再設定されて、WEKOに自動ログインされる
            
              - トップページ画面の上部にパスワードが成功にリセットされた旨を通知する  
                通知内容：「You successfully reset your password and you have been logged in automatically.」
        
          - チェックに問題がある場合、エラーメッセージをテキストボックスの下部に表示させる
            
              - パスワード、またはパスワードの再入力を入力しない場合  
                エラーメッセージ：「Password not provided」
            
              - パスワードを6文字未満で入力する場合  
                エラーメッセージ：「Password must be at least 6 characters」
            
              - パスワードがパスワードの再入力と統一しない場合  
                エラーメッセージ：「Passwords do not match」
    
      - アクセスリンクが送信されたリンクと統一しない場合、リセットパスワード画面にエラーメッセージを表示する  
        エラーメッセージ：「Invalid reset password token.」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_accounts

<!-- end list -->

  - > 処理概要

> リセットパスワード画面で［リセットパスワード（Reset Password）］ボタンを押すと、invenio\_accounts.tasks.send\_security\_emailにて、セロリタスクでメールを送信する

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