### ハーベスト

## 目的・用途

本機能は、外部機関からデータを設定されたスキーマ形式で取得する機能である。

## 利用方法

【Administration＞OAI-PMH＞ハーベスト（Harvesting）】の順で画面遷移して利用する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

1. OAI-PMHスキーマに対してマッピングを実施

   - 【Administration > アイテムタイプ管理（Item Types） > マッピング（Mapping）】：作成されたOAI-PMHスキーマにマッピングを実施する画面である。実施についての詳細は[ADMIN1-2 マッピング](./ADMIN_1_2.md)を参照するものとする。

2. ハーベスト情報を設定

   - 【Administration > OAI-PMH > ハーベスト（Harvesting）】で以下のハーベスト情報を設定。
     - Repository Name：メタデータ取得先のリポジトリ名称。必須項目。繰り返し不可。テキストを入力。
     - Base URL：メタデータ取得先のOAI-PMH出力APIのURL。必須項目。テキストを入力。
     - From Date：アイテム更新日時（期間‐開始日時）。カレンダーから選択。
     - Until Date：アイテム更新日時（期間‐終了日時）。カレンダーから選択。
     - Set Spec：アイテムをハーベストする条件を指定。テキストを入力。
     - Metadata Prefix：メタデータスキーマを指定。必須項目。  
       oai_dc、jpcoar（またはjpcoar_1.0）、jpcoar_2.0、ddi（またはoai_ddi25）のいずれかを入力する必要がある。前述以外でも登録は可能であるが、実行はできない。
     - Target Index：ハーベストされたアイテムに対して登録先インデックスを指定。必須項目。インデックスツリー一覧からプルダウン形式で選択。サブリポジトリ管理者の場合は管理対象のサブリポジトリに属するインデックスのみ表示。
     - Update Style：更新方法。Bulk/Differenceからプルダウン形式で選択。初期値はBulk。
       - Bulkを選択すると、ハーベストで取得したアイテムすべてをハーベスト対象とする。
       - Differenceを選択すると、ハーベストで取得したアイテムのうちdatestampが未来日のものだけをハーベスト対象とする。
     - Auto Distribution：子インデックスへの自動振り分けを指定。Run/Do not runから選択
       - Runを選択すると、登録先インデックス直下にハーベスト対象リポジトリのインデックスツリーを作成し、ハーベストで取得したアイテムがそれぞれのインデックスに配置される
       - Do not runを選択すると、登録先インデックス直下にはインデックスツリーが作成されず、ハーベストで取得したアイテムが登録先インデックス直下に全て配置される
   - [保存（Save）]ボタンを押すと、設定されたハーベストレコードをHarvesting一覧に追加させ、メッセージをハーベスティング一覧に表示させる  
     メッセージ：「レコードが正常に作成されました。」
   - [保存してもう一つ追加（Save Add Another）]ボタンを押すと、設定されたハーベストレコードをHarvesting一覧に追加させ、他のリポジトリを追加設定可能とする。
   - [保存して編集を続ける（Save and Continue Editing）]ボタンを押すと、設定されたハーベストレコードをHarvesting一覧に追加させ、該当ハーベストレコードの編集を続けることを可能とする。
   - ハーベスト用アイテムタイプの用意については、[ADMIN1 アイテムタイプ管理](./ADMIN_1_1.md)を参照。

3. ハーベストを実行

   - 【前提条件】  
     【1.1. OAIスキーマに対してマッピングを実施】及び【1.2. ハーベスト情報を設定】が設定済み。
   - 【Administration > OAI-PMH > ハーベスト（Harvesting） 】から実行したいハーベストの左にある[目]ボタンを押して詳細画面へと遷移し、そこで[Run]ボタンを押すと、当該画面上の設定内容をもとにハーベストを実行する。
     - ハーベスト開始直後
       - ハーベストはCeleryタスクとして実行される。実行時のtask id をharvest_settings テーブルの task_idカラムに格納する。
     - ハーベスト処理
       - 「identifier」をキーとして以下の判定をおこなう。  
         「identifier」値はoaiserverで出力された値である。  
         フォーマット：「oai:invenio:recid/<id>」
         - WEKOリポジトリに存在しないものは新規登録をする。
         - 「identifier」が同じものはアイテムのメタデータ、アイテムのバージョン及び所属インデックスを更新する。
         - アイテムが削除されている(OAI-PMHの削除フラグがセットされている)ものはハーベストし、ハーベストされた場合、削除されてないアイテムとして登録する。
         - 非公開アイテムはハーベストし、ハーベストされた場合、公開アイテムとして登録する。
         - ハーベストの時に、対象のアイテムが削除された場合（ハーベスト先のリポジトリからdelete情報を受け取った際）最新バージョンが論理削除される。
     - ハーベスト後
       - ハーベストによりWEKOリポジトリに登録されたアイテムは、通常のアイテムと同様にメタデータの編集、所属インデックスの変更、アイテムの削除を実行する。ハーベストして登録したアイテムの公開日は"ハーベスト先のdatestamp"を設定し、公開ステータスは"公開"とする。
       - ハーベスト後にWEKOリポジトリで編集されたアイテムは、次回ハーベスト実行時に対象リポジトリのアイテムで上書き更新される。
       - ハーベスト後にWEKOリポジトリで削除されたアイテムでも、次回ハーベスト実行時に対象であった場合は、復活して上書き更新される。
       - harvest_settings テーブルの task_idカラムにnullを格納する。
   - ハーベストの実行中に[中断（Suspected）]ボタンを表示させる。[中断（Suspected）]ボタンを押すと、ハーベスト処理を中断する。
   - 中断したハーベスト処理に対して、中断した箇所から再開できる。
   - ハーベストの処理結果をメール通知できる。
     - 当該メールの宛先は、リポジトリ管理者 及び コミュニティ管理者 とする。
     - 通知タイミングは、ハーベスト処理が完了（中断など正常に終了しなかった場合を含む）した時点とする。
     - メール通知に使う言語は【Administration > 設定（Setting） > Language】に一番上の設定された言語とする。
     - 通知内容は、以下を含む
       - 処理ステータス（正常終了、中断、キャンセル、エラー）
       - 処理件数
       - 処理時間
       - 処理開始時刻
       - 処理終了時刻
   - ハーベスト処理が完了した時、OAI-PMHの各リクエストごとに対して、ElasticSearchにシステムログを出力する。
     - ハーベスト処理が成功になる場合、以下のような内容を出力する。  
       'task_id': request.id
     - ハーベスト処理が失敗になる場合、以下のような内容を出力する。  
       'task_state': 'FAILURE',  
       'start_time': start_time.strftime('%Y-%m-%dT%H:%M:%S%z'),  
       'end_time': end_time.strftime('%Y-%m-%dT%H:%M:%S%z'),  
       'total_records': 0,  
       'execution_time': str(end_time - start_time),  
       'task_name': 'harvest',  
       'repository_name': 'weko', # TODO: Grab from config  
       'task_id': request.id

4. ハーベストのインターバル設定でハーベスト処理の定期実行を可能。

   - 【Administration > OAI-PMH > ハーベスト（Harvesting） 】から実行したいハーベストの左にある[鉛筆]ボタンを押して編集画面へと遷移し、ハーベストのインターバルを以下のように設定する。
     - 周期：Daily/Weekly/Monthlyから選択する。
       - Weeklyを選択すると、選択可能曜日一覧（Monday～Sunday）を右側に表示する。
       - Monthlyを選択すると、選択可能日一覧（01～30）を右側に表示する。
     - オン/オフを選択する。
       - オンを選択する場合、設定された実行間隔でハーベスト処理を自動実行する。
       - オフを選択する場合、ハーベスト処理は実行しない。

5. OAI-PMHのハーベスト記録を確認可能

   - 【Administration > OAI-PMH > ハーベスト（Harvesting） 】から実行したいハーベストの左にある[目]ボタンを押して詳細画面へと遷移し、ハーベスト設定エリアの下側に実行履歴を表形式で表示する。  
     リストは新しいものを上から順に表示していく。
     - 履歴のリストの項番。
       - リンク形式で表示する。
       - リンクを押下すると、ハーベスト実行時の以下の情報をポップアップで表示する。
         - Repository Name
         - Base URL
         - From Date
         - Until Date
         - Set Spec
         - Metadata Prefix
         - Target Index
         - Update Style
         - Auto Distribution
     - 開始日時（Start Time）。フォーマット：YYYY-MM-DDThh:mm:ss.sTZD  
       例：2020-06-05T14:16:38.807296+09:00
       - ハーベスト処理を開始した（「Run」ボタンを押下した）時点の日時を記録する。
     - 終了日時（End Time）フォーマット：YYYY-MM-DDThh:mm:ss.sTZD
       - ハーベスト処理が完了した時点の日時を記録する。  
         エラーで終了した場合は、その日時を記録する。  
         また、管理者が[中止（Cancel）]ボタンを押下した際には、そのときの日時を記録する。
     - ステータス（Status）
       - ：現在ハーベストの処理を実施している状態。この状態のとき、終了日時は記録されない。
       - Successful：ハーベストの処理がエラー無く正常に終了した状態。
       - Failed：ハーベストの処理でエラーが発生して終了した状態。
       - Suspended：ハーベストの処理を管理者が[Pause]ボタンを押下している状態。この状態のときは終了日時は記録されない。  
         なお、中断から再開をした場合、状態は"実行中"となる。
       - Cancel：ハーベストの処理を管理者が[Clear]ボタンを押下して終了した状態
     - エラーメッセージ・URL（Error Message, Url）
       - ハーベストの処理が異常終了で終了したときにメッセージとリクエストURLが表示される。
         - エラーメッセージは、どのようなエラーが発生したのかを表示する（ログからエラーメッセージを取得して表示する）
         - URLはエラーが発生した時点でのリクエストURLを表示する（後々、どこまで登録できたのかをURLから追える）
     - 処理件数（Processed Items）
     - 登録件数（Created Items）
     - 更新件数（Updated Items）
     - 削除件数（Deleted Items）
     - エラー件数（Error Items）
   - 実行履歴の表示件数をコンフィグファイルに設定できる  
     設定キー：OAIHARVESTER_NUMBER_OF_HISTORIES

## 関連モジュール

- invenio-oaiharvester

## 処理概要

**1. 設定**

OAI-PMHハーベスト実行履歴の表示件数を設定

- 設定内容：  
  OAIHARVESTER_NUMBER_OF_HISTORIES = 20
- パス： <https://github.com/RCOSDP/invenio-oaiharvester/blob/feature/weko/invenio_oaiharvester/config.py#L46>

- それぞれの取得されたアイテムを以下のように処理する
  - アイテムの「pid_type」と「pid_value」の値を元に、該当アイテムがリポジトリに存在するかどうかをチェックする
    - 存在しない場合、新規登録をする
      - Metadata Prefix の設定によって、アイテムタイプを決まる （v2.0.0）

        | Metadata Prefix の値 | 使用しているハーベスト用アイテムタイプ |
        |:--|:--|
        | oai_dc | Multiple |
        | jpcoar | Multiple |
        | jpcoar_1.0 | Multiple |
        | jpcoar_2.0 | Multiple |
        | oai_ddi25 | Harvesting DDI |
        | ddi | Harvesting DDI |

- 新規アイテムの「pid_id」、「pid_value」の値を設定する。
  - 「pid_id」= hvstid
  - 「pid_value」= identifier値（oai:invenio:recid/<id>）

- 存在している場合、アイテムのメタデータおよび所属インデックスを更新する。
- 削除されている(OAI-PMHの削除フラグがセットされている)アイテムは、WEKOリポジトリに登録されているアイテムを削除する
- 非公開アイテムは、「公開アイテム」とする
- current_userの条件を追加し、ない場合user_idを1を設定

- ハーベストが完了する時、ハーベスト結果を表に総計する。  
  詳細は「4.1.5. OAI-PMHのハーベスト記録を確認可能」になる。

(2)ハーベスト実行中に、[Clear]ボタンを押すと、ハーベスト処理がキャンセルとする。

- 実行ステータスの状況をメール通知する。  
  メールテンプレート：https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/invenio-oaiharvester/invenio_oaiharvester/templates/invenio_oaiharvester/run_stat_mail.html#L27C11-L27C11

(3)ハーベスト実行中に、[Pause]ボタンを押すと、ハーベスト処理が中断とする  
中断したハーベスト処理に[Resume]ボタンを押すと、ハーベスト処理が再開とする

(4)ハーベストのインターバル設定があれば、設定時間の通りにハーベスト処理を定期実行する。

(5)ハーベスト処理が完了した時、OAI-PMHの各リクエストに対して、ElasticSearchにシステムログをinvenio_stats.contrib.event_builders.celery_task_event_builderで出力する。

- ハーベスト処理が成功になる場合、以下のような内容を出力する。  
  （ここでいう成功とは、処理が最後まで正常に行われたことを示している。）  
  'task_id': request.id  
  'task_state': 'SUCCESS',  
  'task_name': 'harvest',  
  'start_time': start_time.strftime('%Y-%m-%dT%H:%M:%S%z'),  
  'end_time': end_time.strftime('%Y-%m-%dT%H:%M:%S%z'),  
  'total_records': 0,  
  'repository_name': 'weko',  
  'execution_time': str(end_time - start_time),
- ハーベスト処理が失敗になる場合、以下のような内容を出力する。  
  （ここでいう失敗とは、処理が最後まで行われなかったことを示している。）  
  'task_id': request.id,  
  'task_state': 'FAILURE',  
  'task_name': 'harvest',  
  'start_time': start_time.strftime('%Y-%m-%dT%H:%M:%S%z'),  
  'end_time': end_time.strftime('%Y-%m-%dT%H:%M:%S%z'),  
  'total_records': 0,  
  'execution_time': str(end_time - start_time),  
  'repository_name': 'weko',

**2. Harvesting画面について**

- 一覧タブ  
  invenio_oaiharvester.admin.HarvestSettingViewが継承しているModelViewにより、flask_admin.model.base.index_view が呼び出され、db内のharvest_settingsの情報を取得し表示している。  
  [run]ボタン：詳細画面から押下可能。押下時にinvenio_oaiharvester.admin.runが呼び出され、ハーベストが実行される。  
  [Pause]ボタン：ハーベスト実行中にのみ押下可能。押下時にinvenio_oaiharvester.admin.pauseが呼び出され、ハーベストを中断する。その後[Resume]ボタン押下で処理を再開する。
- 作成タブ・編集タブ  
  invenio.oaiharvester.admin.HarvestSettingView.edit_viewが呼び出され、作成画面もしくは編集画面へと遷移する。必須項目を入力後、保存処理をすることでdb内のharvester_settingsが更新される。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2025/01/23 | - | サブリポジトリ対応 |
| 2025/12/22 | 3746dcec79f1b508e40d8ba078c3165cd8acca3a | v2.0.0 対応 |
