### Item Registration：フィードバックメール機能

#### 目的・用途

フィードバックメールの送信有無をアイテム単位で設定する。

#### 利用方法

#### 利用可能なロール

| ロール   | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| :------: | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       ○       |        ○        |         ○         |      ○      |      ※      |                    |

※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

#### 機能内容

【前提条件】

- 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】で、フィードバックメールを送信する設定になっていること。

- 詳細は、管理機能の[フィードバックメール](#_フィードバックメール)を参照。

- アイテム登録画面の一番下での「フィードバックメール送信先」領域にフィードバックメール送信先を設定できる

  - ［著者DBから入力（From author DB）］ボタン

    - ボタンを押下すると、著者DBの検索ウィンドウが表示される

    - 「検索」ボタンを押すと、【Admin > Setting > Author Management > Author ID 】登録された著者DB一覧を表示する

    - メールが設定されていない著者がいた場合でも著者を表示するが、Importボタンを非活性にする

      - メールアドレスがリストボックスに表示されていない著者を選択すると、リストボックス上にメールアドレスがインポートされる

      - メールアドレスがリストボックスに表示された著者を選択すると、以下のエラーメッセージを表示し、リストボックス上にインポートされない  
        エラーメッセージ：「Duplicate Email Addresses.」

  - リストボックス

    - 送信対象者となる著者のメールアドレスが表示される

    - メールアドレスはクリックすると選択できる

    - メールアドレスを選択している状態で、[Delete]ボタンを押下すると、選択した著者のメールアドレスがリストボックスから消える(送信対象者から外れる)

    - リストボックスはテキスト入力できる  
      テキスト入力されたデータの"先頭"と"末尾"にスペースがあった場合はトリム処理をした上で設定する

    - 次のアクションに進むタイミングで、リストボックス内のメールアドレスのバリデート処理(メールアドレスとして満たしているか)を行う。

    - バリデート処理で問題があった場合、エラーを表示して次のアクションには進めない。

      - 入力されたメールアドレスの形式が不正の場合、以下のエラーメッセージを表示する  
        エラーメッセージ：「Invalid email format.」

      - 入力されたメールアドレスが重複している場合、以下のエラーメッセージを表示する  
        エラーメッセージ：「Duplicate Email Addresses.」

- フィードバックメール送信先の設定はアイテムタイプによらず表示されるものとする

- フィードバックメール送信先は必須項目ではないため、入力しなくても次のアクションへ進める

- フィードバックメール送信先はメタデータの登録・編集時のみ表示され、当該アイテムの登録者及び管理者は表示される  
  ただし、Contributorとして指定されたユーザは、 アイテム登録者と同様に該当アイテムの登録(編集)権限が付与されるため、フィードバックメール送信先も設定できるものとする

- フィードバックメール送信先は、承認者が承認をした時点から有効となる

#### 関連モジュール

#### 処理概要

1. 設定

フィードバックメール送信タイミングを設定

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L98>
- 設定キー：「send-feedback-mail-schedules」
- 設定値: day_of_month、hour、minute  
  現在の設定値：day_of_month='1', hour=0, minute=0

フィードバックメールの送信履歴の表示件数

- パス：modules/weko-admin/weko_admin/config.py
- 設定値：WEKO_ADMIN_NUMBER_OF_SEND_MAIL_HISTORY = 20

フィードバックメールの送信履歴の送信失敗の表示件数

- パス：modules/weko-admin/weko_admin/config.py
- 設定値：WEKO_ADMIN_NUMBER_OF_FAILED_MAIL = 10

フィードバックメールの送信件数を設定

- パス：modules/weko-search-ui/weko_search_ui/config.py
- 設定値：WEKO_SEARCH_MAX_FEEDBACK_MAIL = 10000

１メールアドレスで送信できるアイテムの数： 最大10,000件を取得(ESの制限値)

2. 実装方法

実装モジュール：weko-admin

設定情報を保存する

- アイテム登録時、 フィードバックメール送信先を入力する場合、「Approval」ステップに承認した後、  
  フィードバックメール送信先の情報を以下のように保存される

  - データベースに保存する  
    テーブル名：feedback_mail_list  
    保存情報：item_id、mail_list、repository_id

  - ~~ Elasticsearchに「feedback_mail_list」属性に保存する ~~ v1.0.8よりDBのみに記録するように変更。

- 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）】に入力した情報をデータベースに以下のように保存する  
  テーブル名：feedback_email_setting  
  保存情報：is_sending_feedback、manual_mail、repository_id

フィードバックメール送信のフロー  
celaryタスクでフィードバックメールを送信するかどうか、チェックする  
「schedule」に設定された時刻にフィードバックメール送信を「task」でのタスク（weko_admin.tasks.send_feedback_mail）で実施する  
「feedback_email_setting」テーブルの行数だけ以下の処理を繰り返す

(1) 「feed_back_email_setting」の情報を「feedback_email_setting」テーブルから取得する

　・「is_sending_feedback = false」の場合、対象リポジトリの処理をスキップする

　・「is_sending_feedback = true」の場合、(2)に進む

(2)Elasticsearchからフィードバックメールの情報を取得する

　・アイテムごとの最新版に"feedback_mail_list"のデータがあるかどうか、チェックする

　"feedback_mail_list"のデータがある場合、フィードバックメールの情報を取得する

(3)アイテムごとの統計情報を「invenio-stats」から「get_list_statistic_data」メソッドで取得する

　・閲覧回数

　　アイテムID及び統計期間（年、月）の情報を元に「get_item_view」メソッドでアイテムごとの閲覧回数を取得する

　・ファイルダウンロード回数

　　バケツID（bucket_id）及びファイル名及び統計期間（年、月）の情報を元に、「get_item_download」メソッドでファイルダウンロード回数を取得する

(4)フィードバックメール送信先ごとにアイテムをまとめ、以下の情報を合計する

　・アイテム総数

　・ファイル総数

　・閲覧回数合計

　・ファイルダウンロード回数合計

(5)送信除外対象者を「get_banned_mail」メソッドで取得し、送信除外対象者一覧に含まれてないメールアドレスへフィードバックメール送信を実施する

　・送信が完了した後、送信履歴をデータベースに保存する

　　テーブル名：feedback_mail_history

　　履歴内容：id、start_time、end_time、stats_date、total_mail、failed_mail

　・送信が失敗になる場合、送信が失敗する情報をデータベースに保存する

　　テーブル名：feedback_mail_failed

　　履歴内容：id、history_id、author_id、mail

(6)送信履歴を【Admin > Statistics > Feedback Mail画面】に表示させる

　送信失敗行にて、送信できなかった件数（「エラー」カラム）をアンカーで表示する

フィードバックメールを再送信する処理に対して「resend_failed_mail」のAPIを実施する  
再送信結果をデータベースでの該当レコードに更新する

3. 手動実行

タスクを呼び出すことで任意のタイミングでフィードバックメールを送信する。

```
celery -A invenio_app.celery call weko_admin.tasks.send_feedback_mail
```

## 実装補足（v2.0.2 実装との突き合わせ）

- 送信は Celery `weko_admin.tasks.send_feedback_mail`、再送 `weko_admin.views.resend_failed_mail`。テーブル `feedback_email_setting` / `feedback_mail_history` / `feedback_mail_failed`（weko-admin）と `feedback_mail_list`（**weko-records** の `FeedbackMailList`）。config `WEKO_ADMIN_NUMBER_OF_SEND_MAIL_HISTORY`(20)/`_FAILED_MAIL`(10)、`WEKO_SEARCH_MAX_FEEDBACK_MAIL`(10000)。

#### 更新履歴

| 日付       | GitHubコミットID                         | 更新内容           |
| :--------: | :--------------------------------------: | :----------------: |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成           |
| 2024/08/27 | f49b016c92ef98e0656947bf651ca1a2f3dbc286 | v1.0.8             |
| 2025/01/23 | -                                        | サブリポジトリ対応 |
