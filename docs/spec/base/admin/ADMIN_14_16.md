# メール送信

## 目的・用途

本機能は、送信元の情報を設定する機能である。

## 利用方法

【Administration > 設定（Setting） > メール送信（Mail）画面】に送信元の情報を設定する。

## 利用可能なロール

|ロール|システム管理者|リポジトリ管理者|コミュニティ管理者|登録ユーザー|一般ユーザー|ゲスト(未ログイン)|
|---|---|---|---|---|---|---|
|利用可否|〇||||||

## 機能内容

### メールサーバを設定する。
    
- 設定項目は以下の通りである

|設定項目|説明|デフォルト値|
|---|---|---|
|SMTPサーバ（Server）|メールサーバ|localhost|
|ポート（Port）|メールポート|25|
|TLSを使用する（Use TLS）|TLSを使用する|チェックなし|
|SSLを使用する（Use SSL）|SSLを使用する|チェックなし|
|ユーザー名（Username）|ユーザー名|空白|
|パスワード（Password）|パスワード|空白|
|ドメイン（Domain）|ドメイン(v1.0.7追加)|空白|
|デフォルト送信元（Default sender）|デフォルト送信元|空白|

- ［更新（Update）］ボタンを押すと、入力内容を確認し、エラーなしの場合、設定内容を保存し、メッセージを画面上部に表示する、

  　メッセージ：  
  　日本語：「メールの設定を更新しました」  
  　英語：「Mail settings have been updated.」
    
- エラーの場合は以下の通りである

|エラー|メッセージ|
|---|---|
|「Server」に入力しない場合|Mail server can't be empty.|
|「Port」に入力しない場合|Mail port can't be empty.|
|「Default sender」に入力しない場合|Mail default sender can't be empty.|

### テストメール送信を行う

- 設定項目は以下の通りである

|設定項目|説明|デフォルト値|
|---|---|---|
|送信先（Recipient）|送信先|
|主題（Subject）|メールの主題|
|本文（Body）|メールの本文|

    
- ［送信（Enable）］ボタンを押すと、設定内容でメールの送信を行う
  - 送信が成功の場合、以下のメッセージを画面上部に表示する  
            　メッセージ：  
            　日本語：「テストメールを送信しました。」  
            　英語：「Test mail sent.」
  - 送信が失敗の場合、以下のメッセージ及びエラーコードを画面上部に表示する  
              メッセージ：「Failed to send mail.」

## 関連モジュール

- invenio-mail

## 処理概要

  - 画面表示時は、invenio_mail.admin.MailSettingVIew.indexメソッドがGETで呼び出される
    
      - このとき、mail_configテーブルからメールサーバの設定を取得する
        
          - invenio_mail.models.MailConfig.get_configメソッドの中で、設定が取得できなかった場合は、デフォルトの内容のレコードを作成してからそれを取得する
    
      - 「Mail Setting」の内容を取得したもの、「Send Test Mail」の内容を空欄として表示する

  - ［更新（Update）］ボタンを押すと、invenio_mail.admin.MailSettingVIew.indexメソッドがPOSTで呼び出される
    
      - エラーチェックを通過した場合、mail_configテーブルのレコードを更新する
        
          - invenio_mail.models.MailConfig.set_configメソッドによって、１つのレコードを更新する
    
      - その後、「Mail Setting」の内容を画面で入力したもの、「Send Test Mail」の内容を空欄として画面に表示する

  - ［送信（Enable）］ボタンを押すと、invenio_mail.admin.MailSettingVIew.send_test_mailメソッドが呼び出される
    
      - mail_configテーブルから取得した情報をメールサーバの各種設定として、「Send Test Mail」の各入力欄に入力したものをメッセージとしてcurrent_app.extensions['mail']に設定して、送信する
    
      - その後、「Mail Setting」の内容をテーブルから取得したもの、「Send Test Mail」の内容を空欄として画面に表示する

  - 「ドメイン（Domain）」の値を持ちいて送信元ドメインを設定する。

## 設定例

### Gmail

|設定項目|説明|デフォルト値|
|---|---|---|
|SMTPサーバ（Server）|メールサーバ|smtp.gmail.com|
|ポート（Port）|メールポート|587|
|TLSを使用する（Use TLS）|TLSを使用する|チェックあり|
|SSLを使用する（Use SSL）|SSLを使用する|チェックなし|
|ユーザー名（Username）|ユーザー名|GmailアカウントID|
|パスワード（Password）|パスワード|Gmailアカウントのアプリケーションパスワード|
|送信元ドメイン（Domain）|ドメイン(v1.0.7追加)|空白|
|デフォルト送信元（Default sender）|デフォルト送信元|Gmailアカウントのメールアドレス|

※ Gmailの場合、送信元ドメイン、デフォルト送信元は利用できない。

デフォルト送信元は「X-Google-Original-From: 」ヘッダに設定される。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_mail.admin.MailSettingView`（クラス名は `MailSettingView`。「MailSettingVIew」は綴り誤り）。`index`（GET/POST）と `send_test_mail`。設定は `MailConfig.get_config` / `set_config`（テーブル `mail_config`）。「ドメイン（Domain）」欄は DB 列 `mail_local_hostname`（SMTP HELO）に対応。

## 更新履歴

|日付|GitHubコミットID|Version|更新内容|
|---|---|---|---|
|2023/11/11||V0.9.23||
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
