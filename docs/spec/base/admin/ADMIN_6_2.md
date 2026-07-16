# フィードバックメール

## 目的・用途

フィードバックメールの送信有無の設定、送信除外対象者の設定、送信履歴の確認を行う。

## 利用方法

【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】で操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

1 フィードバックメール情報を表示するリポジトリを選択する

- 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】で、設定を表示するリポジトリを選択できる
  - リポジトリ選択プルダウンを設ける
    - リポジトリ選択のプルダウンでの選択肢は以下の通りである
      - システム管理者、リポジトリ管理者の場合は、システムに登録されている全てのリポジトリとする
      - サブリポジトリ管理者の場合は、管理対象のサブリポジトリとする
  - プルダウンからリポジトリを選択すると「フィードバックメール」、「送信除外対象者」、「送信履歴」エリアを選択されたリポジトリの情報に更新する

2 フィードバックメールを設定

- 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】にフィードバックメールの送信機能に対して以下ように設定できる
  - 「フィードバックメール」（Feedback email feature）領域にフィードバックメールを送信する／送信しないを設定する
    - 送信（Enable）：フィードバックメールを送信する設定となる
    - 無効（Disable）：フィードバックメールを送信しない設定となる
  - 「送信除外対象者」（Exclusion from sending）領域にフィードバックメールを送信する対象から除外を設定する
    - ［著者DBから入力（Input from author DB）］ボタン  
      ボタンを押下すると、著者DBの検索ウィンドウが表示される  
      「検索」ボタンを押すと、【Administration > 著者DB管理（Author Management） > 画面 > Author IDタブ 】にて登録された著者DB一覧を表示する  
      メールが設定されていない著者がいた場合でも著者を表示するが、Importボタンを非活性にする
      - メールアドレスがリストボックスに表示されていない著者を選択すると、リストボックス上にメールアドレスがインポートされる
      - メールアドレスがリストボックスに表示された著者を選択すると、以下のエラーメッセージを表示し、リストボックス上にインポートされない  
        エラーメッセージ：「Duplicate Email Addresses.」
    - リストボックス
      - 除外対象者となる著者のメールアドレスが表示される
      - メールアドレスはクリックすると選択できる
      - メールアドレスを選択している状態で、「削除」（Delete）ボタンを押下すると、選択した著者のメールアドレスがリストボックスから消える(除外対象者から外れる)
      - リストボックスはテキスト入力できる  
        テキスト入力されたデータの"先頭"と"末尾"にスペースがあった場合はトリム処理をした上で設定する
      - 次のアクションに進むタイミングで、リストボックス内のメールアドレスのバリデート処理(メールアドレスとして満たしているか)を行う
      - バリデート処理で問題があった場合、エラーを表示して次のアクションには進めない
        - 入力されたメールアドレスの形式が不正の場合、以下のエラーメッセージを表示する  
          エラーメッセージ：「Please input a valid email.」
        - 入力されたメールアドレスが重複している場合、以下のエラーメッセージを表示する  
          エラーメッセージ：「Duplicate Email Addresses.」
  - ［保存（Save）］ボタンを押すと、自画面の設定された情報をDBに格納する
  - 「送信履歴」（Send logs）領域に著者へのフィードバックメールの送信日時の履歴を確認する

3 アイテムのフィードバックメール送信先に指定した送信先に対して、月毎の利用統計をメールで自動送信

- 【前提条件】
  - 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】でフィードバックメールを「送信する」に設定済み
  - 【Administration > 設定（Setting） > メール送信（Mail）画面】での「デフォルト送信元（Default sender）」にメールアドレスを設定済み
- フィードバックメール送信タイミングは、以下の通りとする
  - 毎月の決まった時刻にメールが送信される
  - 送信する日時をコンフィグファイルに設定できる
    - 設定キー：「send-feedback-mail-schedules」
    - 設定値：月の日、時間、分
    - メールテンプレート：
      - EN： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/templates/weko_admin/email_templates/statistic_mail_template_en.tpl>
      - JP： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/templates/weko_admin/email_templates/statistic_mail_template_ja.tpl>
- メールの件名には、【Administration > 設定（setting） > サイト情報（site info）画面】 の「サイト名」を使用する  
  　日本語メールには日本語サイト名を、英語メールには英語サイト名をセットする
- アイテム登録時（[USER-4-8: Item Registration：フィードバックメール機能](#_Item_Registration：フィードバックメール機能)を参照）にフィードバックメールを受信する設定にしている方を対象とする
- ユーザ情報にメールアドレスが登録されていない場合は対象者にならず、メールは送信されない
- 対象者が複数のアイテムで受信する設定となっている場合、メールは1通のみ(まとめて)送信されるようにする
- 閲覧回数、ファイル再生回数、ファイルダウンロード回数等がすべてゼロであるアイテムでもメールに記載する
- 対象期間は１ヶ月分のデータを集計する
- 送信するメールのフォーマットは別紙「利用統計レポートメールひな形」に合わせる
- 日本語/英語のメール送信判定は、システムのデフォルト言語(日本語以外の場合は英語メール)とする
- ダウンロード回数と再生回数は、ファイルの差し替えを行った場合でも統計値は引き継いで集計する

4 フィードバックメールの送信履歴を確認

- 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】での「送信履歴」（Send logs）領域にフィードバックメールの送信履歴を表示する
  - 送信履歴がない場合、「検索結果はありません.」（No search result）メッセージを表示する
  - 送信履歴がある場合、送信履歴の情報を以下のように表示する
    - 送信履歴は、一括処理での単位(1回の送信のトランザクションごと)での履歴とする
    - 表示する順序は、最新のものが一番上(送信日の降順)で並ぶように表示する
    - 履歴は20件を表示し、残りはページング表示で切り替える
    - 表示情報
      - 「#」：番号順
      - 「リポジトリ」（Repository）：フィードバックメールの処理の対象となるリポジトリを出力する
      - 「送信開始日時」（Start time）：フィードバックメールの処理が開始したときの日時を出力する
      - 「送信終了日時」（End time）：フィードバックメールの処理が終了したときの日時を出力する
      - 「送信件数」（Counts）：1回の処理で何人の著者にメール送信を実行したか、その件数を表示する
      - 「成功」（Success）：1回の処理で送信したメールのうち、送信できたものの件数を表示する
      - 「エラー」（Error）
        - 1回の処理で送信したメールのうち、送信できなかったものの件数を表示する（送信時に送れたかどうかで判断）
        - 送信できなかった件数をアンカーで表示する
        - アンカーを選択すると、画面レイアウトのようにモーダル画面上に失敗した著者のリストを表示する

5 フィードバックメールを再送信

- 送信失敗した著者に対してのメールを再送信できる
  - 送信履歴のテーブルでの失敗した件数のアンカーを表示し、モーダル画面を開いたときにある[Resend]ボタンを押下すると、メールが送信されるようにする
  - 送信される対象者は、リスト上にいる失敗したユーザーとする
  - 再送信時の集計期間は、送信失敗時と同じ集計期間で再度集計してメール送信を行う
  - 送信時のフォーマットはアイテムのフィードバックメール送信と同様のフォーマットを使用する
  - 送信する対象者が複数のアイテムで受信する設定となっている場合、メールは1通のみ(まとめて)送信されるようにする
  - 閲覧回数、ファイル再生回数、ファイルダウンロード回数等がすべてゼロであるアイテムでもメールに記載する
  - 日本語/英語のメール送信判定は、システムのデフォルト言語(日本語以外の場合は英語メール)とする
- メールの送信中
  - 画面上には「メール送信中」であることを表示する
- メールの送信後
  - 送信完了した場合は「メール送信中」の表示は消える
  - 送信履歴に再送した送信履歴が新たに追加される

## 関連モジュール

- weko-admin
- weko-search-ui
- weko-records
- invenio-stats

## 処理概要

**1. 設定**

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

**2. 実装方法**

実装モジュール：weko-admin

設定情報を保存する

- アイテム登録時、フィードバックメール送信先を入力する場合、「Approval」ステップに承認した後、フィードバックメール送信先の情報を以下のように保存される
  - データベースに保存する  
    テーブル名：feedback_mail_list  
    保存情報：item_id、mail_list、repository_id
  - Elasticsearchに「feedback_mail_list」属性に保存する
- 【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】に入力した情報をデータベースに以下のように保存する  
  テーブル名：feedback_email_setting  
  保存情報：is_sending_feedback、manual_mail、repository_id

フィードバックメール送信のフロー

- celaryタスクでフィードバックメールを送信するかどうか、チェックする
- 「schedule」に設定された時刻にフィードバックメール送信を「task」でのタスク（weko_admin.tasks.send_feedback_mail）で実施する
- 「feedback_email_setting」テーブルの行数だけ以下の処理を繰り返す
  1. 「feed_back_email_setting」の情報を「feedback_email_setting」テーブルから取得する
     - 「is_sending_feedback = false」の場合、対象リポジトリの処理をスキップする
     - 「is_sending_feedback = true」の場合、(2)に進む
  2. Elasticsearchからフィードバックメールの情報を取得する
     - アイテムごとの最新版に"feedback_mail_list"のデータがあるかどうか、チェックする
     - "feedback_mail_list"のデータがある場合、フィードバックメールの情報を取得する
  3. アイテムごとの統計情報を「invenio-stats」から「get_list_statistic_data」メソッドで取得する
     - 閲覧回数  
       アイテムID及び統計期間（年、月）の情報を元に「get_item_view」メソッドでアイテムごとの閲覧回数を取得する
     - ファイルダウンロード回数  
       バケツID（bucket_id）及びファイル名及び統計期間（年、月）の情報を元に、「get_item_download」メソッドでファイルダウンロード回数を取得する
  4. フィードバックメール送信先ごとにアイテムをまとめ、以下の情報を合計する
     - アイテム総数
     - ファイル総数
     - 閲覧回数合計
     - ファイルダウンロード回数合計
  5. 送信除外対象者を「get_banned_mail」メソッドで取得し、送信除外対象者一覧に含まれてないメールアドレスへフィードバックメール送信を実施する
     - 送信が完了した後、送信履歴をデータベースに保存する  
       テーブル名：feedback_mail_history  
       履歴内容：id、start_time、end_time、stats_date、total_mail、failed_mail、repository_id
     - 送信が失敗した場合、送信が失敗した情報をデータベースに保存する  
       テーブル名：feedback_mail_failed  
       履歴内容：id、history_id、author_id、mail
  6. 送信履歴を【Administration > 統計（Statistics） > フィードバックメール（Feedback Mail）画面】に表示させる  
     送信失敗行にて、送信できなかった件数（「エラー」カラム）をアンカーで表示する
- フィードバックメールを再送信する処理に対して「resend_failed_mail」のAPIを実施する  
  再送信結果をデータベースでの該当レコードに更新する

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_admin.admin.FeedbackMailView`（endpoint `feedbackmail`、画面描画）＋ API（`weko_admin.views`：`update_feedback_mail` / `get_feedback_mail` / `get_send_mail_history` / `get_failed_mail` / `resend_failed_mail`）。送信は Celery `weko_admin.tasks.send_feedback_mail`（crontab：毎月1日 0:00、スケジュールキー `send-feedback-mail-schedules`）。
- config：最大送信件数 `WEKO_SEARCH_MAX_FEEDBACK_MAIL` は 10000。テーブル `feedback_email_setting`（`account_author`（NOT NULL）・`root_url` 列を含む）/ `feedback_mail_history` / `feedback_mail_failed` / `feedback_mail_list`（weko-records）。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2024/08/27|f49b016c92ef98e0656947bf651ca1a2f3dbc286|v1.0.8|
|2025/01/23|-|サブリポジトリ対応|
