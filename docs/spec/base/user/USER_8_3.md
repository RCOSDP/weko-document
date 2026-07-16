# パスワードリセット

## 目的・用途

当機能は、パスワードを忘れてログインできないユーザーが再設定できるようにする機能である。

## 利用方法

ログイン画面で、「パスワードをお忘れの方はこちら」リンクを押す。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ |  |

## 機能内容

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

## 関連モジュール

- Flask-Security（パスワードリセット画面・文言を提供）
- invenio_accounts（メール送信タスクを提供）

## 処理概要

パスワードリセットの画面・文言は依存ライブラリ Flask-Security（`flask_security.views.forgot_password`（route `/lost-password/`）/ `reset_password`（route `/reset/<token>`）、`SECURITY_MSG_*` 既定）に由来する。

リセットパスワード画面で［リセットパスワード（Reset Password）］ボタンを押すと、invenio_accounts.tasks.send_security_emailにてメールを送信する（`ACCOUNTS_USE_CELERY=True` の場合のみCeleryタスク経由）

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足：パスワードリセットの画面・文言は **Flask-Security**（`flask_security.views.forgot_password`（`/lost-password/`）/ `reset_password`（`/reset/<token>`）、`SECURITY_MSG_*`）由来。メール送信は `invenio_accounts.tasks.send_security_email`（Celery、`ACCOUNTS_USE_CELERY` 依存）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
