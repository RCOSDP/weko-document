
### サインアップ

  - > 目的・用途

本機能は、ゲストが登録してユーザーになるための機能である。

  - > 利用方法

ユーザー画面のヘッダから「サインアップ」（Sign up）ボタンを押す。

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>○</td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - ユーザー画面から［サインアップ（Sign up）］ボタンを押すと、サインアップ画面に移動する

  - サインアップ画面を以下のように設ける
    
      - 表示言語はヘッダに選択しているシステム言語とする
    
      - メールアドレスとパスワードのテキストボックス
    
      - ［サインアップ（Sign Up）］ボタン、「ログイン」（Log In）リンク

  - ［サインアップ（Sign Up）］ボタンを押すと、入力した情報をチェックする
    
      - メールアドレスに対して
        
          - メール形式で入力すること
        
          - システムに登録されていないこと
    
      - パスワードのテキストボックスには、キーボードからは半角英数字のみ入力できるように入力制限がかかっている

  - チェック上、問題なければ、アカウントが登録されて、自動ログインされる  
    ※登録されたアカウントに対して、ロールが付与されない状態とする
    
      - トップページ画面の上部にメール確認用のリンクが送信された旨を通知する  
        通知内容：「Thank you. Confirmation instructions have been sent to {}.」

  - チェックに問題がある場合、エラーメッセージをテキストボックスの上部に表示させる
    
      - メールアドレス、またはパスワードを入力しない場合  
        エラーメッセージ：「{} not provided」
    
      - メールアドレスの形式が不正である場合  
        エラーメッセージ：「Invalid email address」
    
      - メールアドレスがシステムに登録されている場合  
        エラーメッセージ：「{} is already associated with an account.」
    
      - パスワードを6文字未満で入力する場合  
        エラーメッセージ：「Password must be at least 6 characters」

  - メール確認リンクにアクセスする
    
      - メール本文から、リンクをクリックすると、WEKOトップページに移動して、登録されたユーザーが自動ログインされる  
        また、トップページ画面の上部にメールが確認された旨を通知する  
        通知内容：「Thank you. Your email has been confirmed.」
    
      - アクセスリンクが送信されたリンクと統一しない場合、確認メールを再送信するため、メールの再入力画面に移動、登録メールを再入力するリクエストとする
        
          - メールアドレスを入力して、［確認を送信する（Send Confirmation）］ボタンを押すと、確認用のメールを再送信する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_accounts

<!-- end list -->

  - > 処理概要

> ［サインアップ（Sign Up）］ボタンを押すと、invenio\_accounts.tasks.send\_security\_emailにて、celeryタスクでメールを送信する
> 
> アカウント登録によって、accounts\_userテーブルにレコードが作成される

  - > 画面で入力したメールアドレスとパスワードが、ログイン時のemailとpasswordになる

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
</tbody>
</table>
