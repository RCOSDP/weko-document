
### ユーザープロファイル設定

  - > 目的・用途

本機能は、ユーザーとして、ユーザープロファイルを閲覧・編集できる機能である。

  - > 利用方法

画面ヘッダで、ログインユーザのメールアドレスが表示されている部分またはその右側の［▼］ボタンをクリックすると、【プロフィール（Profile）画面】に遷移する。画面上で操作を行う。

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

1\. ユーザープロファイルを閲覧・編集する

  - 【プロフィール（Profile）画面】にユーザーの情報を管理する
    
      - 表示項目は以下の通りである
        
          - ［確認メールを再送（Resend verification email）］ボタン  
            ボタンを押すと、確認メールを再送信し、メッセージを画面上部に表示する  
            メッセージ：  
            　日本語：「確認メールを送信しました」  
            　英語：「Verification email sent.」
        
          - 「ユーザー名」（Username）：必須項目
            
              - 入力必須は「ユーザー名」（Username）テキストボックスの下に表示する  
                日本語：「ユーザー名は3文字以上を指定してください(英数字, ハイフン, アンダーバーのみ使用可能)は入力必須です」  
                英語：「Required. Username must start with a letter, be at least three characters long and only contain alphanumeric characters, dashes and underscores.」
        
          - 「タイムゾーン」（Timezone）  
            デフォルト値：「(GMT+9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk」
        
          - 「言語」（Language）  
            選択肢：「自動」（Automatic）、「日本語」（Japanese）、「英語」（English）  
            デフォルト値：日本語
        
          - 「メールアドレス」（Email address）
        
          - 「メールアドレスの再入力」（Re-enter email address）
    
      - ［Update Profile］ボタンを押すと、設定内容をチェックし、エラーがない場合、設定内容を保存する
        
          - 「メールアドレス」を変更する場合、変更されたメールアドレスに確認メールを送信し、メッセージを画面上部に表示する  
            メッセージ：  
            　日本語：「プロフィールを更新しました+「メールアドレス」+に確認メールを送信しましたので、ご確認ください」  
            　英語：「Profile was updated. We have sent a verification email to + 「email address」 +. Please check it.」
        
          - 「メールアドレス」を変更しない場合、以下のメッセージを画面上部に表示する  
            メッセージ：  
            　日本語：「プロフィールを更新しました」  
            　英語：「Profile was updated.」
    
      - エラーメッセージは以下の通りである
        
          - 「ユーザー名」（Username）を指定しない場合、エラーメッセージを「ユーザー名」（Username）エリアの下に表示する  
            メッセージ：  
            　日本語：「ユーザー名を入力してください」  
            　英語：「Please input username」
        
          - フォーマットのチェックによるエラーメッセージが以下のように定義されているが、v0.9.22ではチェックメソッドを呼び出していないため表示されることはない
        
          - > 指定している「ユーザー名」（Username）のフォーマットが不正の場合、エラーメッセージを「ユーザー名」（Username）エリアの下に表示する  
            > メッセージ：  
            > 　日本語：「ユーザー名は3文字以上を指定してください(英数字, ハイフン, アンダーバーのみ使用可能)」  
            > 　英語：「Username must start with a letter, be at least three characters long and only contain alphanumeric characters, dashes and underscores.」
    
      - 「キャンセル」（Cancel）ボタンを押すと、プロフィール画面に再度遷移することで設定内容をリセットする
    
      - この画面では「ユーザー名」（Username）は入力必須だが、データベース上は必須ではない。空にする場合は、管理者機能で設定する。（[ADMIN-13-12: ユーザープロファイル](\\l)を参照）

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-user-proriles

<!-- end list -->

  - > 処理概要

> プロフィール入力フォームとその入力内容チェックは、以下で定義している。

  - > パス：  
    > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/forms.py>

  - > ProfileFormクラスの内容を、テンプレートprofile.htmlに設定している。

> ［Update Profile］ボタンを押すと、リクエストペイロードにsubmit: profileを含むaccount/settings/profile/ リクエストがPOSTされる。

  - > これによって、weko\_user\_profiles.views.profileメソッドが呼び出される。この中でhandle\_profile\_formメソッドを呼び出してユーザープロファイルを更新する。

> プロフィールの設定は、userprofiles\_userprofileテーブルに保存される。

  - > ユーザー名（Username）はdisplaynameカラムに保存される。

  - > タイムゾーン（Timezone）はtimezoneカラムに保存される。

  - > 言語（Language）はlanguageカラムに保存される。

> メールアドレスの変更は、flask\_loginのグローバル変数current\_user.emailを更新することで保存される。

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