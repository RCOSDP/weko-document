### Resync

  - > 目的・用途

resyncを利用して外部機関からデータを収集する

  - > 利用方法

【Administration \> Resource Sync \> Resync画面】にて操作を行う

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

  - resync: <https://github.com/resync/resync>

  - 【Resync画面】には以下のタブが表示される
    
      - List
    
      - Create
    
      - Edit
        
          - > Listタブ選択中は非表示
        
          - Listタブの操作によって表示される
        
          - EditタブまたはDetailsタブ選択中に表示
    
      - Detail
        
          - > Listタブ選択中は非表示
        
          - Listタブの操作によって表示される
        
          - EditタブまたはDetailタブ選択中に表示

  - 「List」タブにて存在するResync Indexを一覧表示する
    
      - 「List」タブを表示するたびに最新の情報を取得する
    
      - 表示項目は以下の通りである
        
          - アクション（詳細・編集・削除を表すアイコン）
        
          - Repository name
            
              - そのResyncの名前
        
          - Target Index
            
              - そのResyncが対象とするインデックス
            
              - フォーマット：「{インデックスの英語名} \<ID:インデックスID\>」
        
          - Base Url
            
              - データ取得先のURL
        
          - Status
            
              - Manual/ Automatic
        
          - Resync mode
            
              - Baseline/Incremental/Audit
        
          - Saving format
            
              - JPCOAR-XMLのみ

  - 「Create」タブにて「Resync」を作成する
    
      - 入力情報は以下の通りである
        
          - Repository name：データ取得先のリポジトリ名称。必須項目。テキストを入力
        
          - Base Url：データ取得先のURL。必須項目。テキストを入力
        
          - Status
            
              - ラジオボタン：Manual、Automatic
            
              - 「Automatic」を選択する場合、「Interval By Day」の入力エリアを表示する
            
              - デフォルト：Automatic
        
          - Interval By Day：自動実行する間隔
        
          - Statusが「Automatic」の場合のみに表示する
            
              - 入力欄は空にできず、1以上の整数のみ設定可能
            
              - デフォルト：1
        
          - From Date：期間‐開始日時。カレンダーから選択
        
          - Until Date：期間‐開始日時。カレンダーから選択
        
          - Target Index：収集されたアイテムに対して登録先インデックスを指定。必須項目。インデックスツリー一覧から選択
        
          - Resync Mode
            
              - 選択肢：Audit、Baseline、Incremental
                
                  - Baselineの時に、resourcelistのURLのみを「Base URL」に指定できる  
                    ResourceListを使ってその中の日付をベースにデータを取得しているので、From date/Until dateの指定は不要になる
                
                  - Incrementialの時に、changelistのURLのみを「Base URL」に指定できる
                
                  - Auditの時に、Sourceサーバーと実行しているかどうか、  
                    ResourceListの変更があるかどうかチェックする機能なのでImportボタンを表示されない
            
              - デフォルト：Baseline
        
          - Saving format
            
              - 値：JPCOAR-XML
    
      - ［Create］ボタンを押すと、入力内容をチェックし、問題がなければ、「Resync」のレコードを作成し、「List」タブに移動する
        
          - エラーの場合は以下の通りである
            
              - 必須項目を入力しない場合、以下のようなエラーメッセージを表示する  
                エラーメッセージ：「{項目名} is required」
    
      - ［Create and Add Another］ボタンを押すと、［Create］ボタンを押したときと同様の処理によって設定された内容のレコードを作成して、他の「Resync」を作成可能とする
    
      - ［Cancel］ボタンを押すと、設定された「Resync」を追加せずに、「List」タブに移動する

  - 外部機関からデータを「Manual」で収集する
    
      - 「Status：Manual」を設定するresyncに対して「Detail」タブにて、「Action」での「Sync」ボタンを押すと、当該画面上の設定内容を元にデータ収集を実行する
        
          - 以下のメッセージがポップアップで表示される
            
              - データ収集が開始された場合のメッセージ：「Sync Success」
            
              - データ収集が開始されなかった場合のメッセージ：「Error in Sync」
        
          - データ収集が完了した後、「Import」ボタンを押すと、収集されたデータをシステムに登録する
        
          - 以下のメッセージがポップアップで表示される
            
              - 登録が開始された場合のメッセージ：「Import Success」
            
              - 登録が開始されなかった場合のメッセージ：「Error in Import」

  - 外部機関からデータを「Automatic」で収集する
    
      - 「Status：Automatic」を設定するresyncに対して  
        【Admin \> Resource Sync \> Resync画面】での「Detail」タブにて、「Running」で収集処理が自動実行するかどうかを設定する
        
          - ONを表示している場合、設定された実行間隔で収集処理を自動実行する  
            ONを押すと、OFFに変更する
        
          - OFFを表示している場合、収集処理は実行しない  
            OFFを押すと、ONに変更する

  - 収集情報の実行履歴を確認する「Detail」タブにて、「Running logs」エリアに実行履歴を表形式で表示する
    
      - 収集処理が完了するまで、3秒ごとに取得して表示エリアを更新し続ける
    
      - 表示項目は以下の通りである
        
          - \#
            
              - ログ番号
        
          - Start Time
        
          - 収集処理を開始した時点の日時
        
          - End Time
        
          - 収集処理を完了した時点の日時
        
          - Status
            
              - コンフィグ「INVENIO\_RESYNC\_LOGS\_STATUS」で設定されたもの
            
              - Successful
                
                  - Running
                
                  - Failed
        
          - Log Type
            
              - sync
            
              - import
        
          - Processed Items
        
          - Created Items
        
          - Updated Items
        
          - Deleted Items
        
          - Error Items
        
          - Error Message, Url
            
              - 収集処理が異常終了で終了したときにメッセージとリクエストURLが表示される

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_resourcesyncclient

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 本画面では、resync\_indexesテーブルの情報を閲覧、作成、編集、削除して、その情報をもとにデータ収集を行う
    
      - 画面表示時に、invenio\_resourcesyncclient.admin. AdminResyncClient.indexメソッドによってテンプレートを指定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncclient/invenio_resourcesyncclient/config.py#L22>
        
          - 設定キー：INVENIO\_RESOURCESYNCCLIENT\_ADMIN\_TEMPLATE
    
      - 「List」タブの表示時に、同クラスのget\_listメソッドによってテーブルの情報をid昇順で取得する
    
      - 「Create」タブで［Create］ボタンを押したとき、同クラスのcreateメソッドによって、テーブルに対象インデックスについてのレコードがない場合に、新たにレコードを作成する
        
          - 「resync\_save\_dir」フィールドの値は、以下のコンフィグで指定する文字列にレコードのidを加えた文字列を設定する
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncclient/invenio_resourcesyncclient/config.py#L51>
            
              - 設定キー：INVENIO\_RESYNC\_SAVE\_PATH
    
      - 「Edit」タブで［Edit］ボタンを押したとき、同クラスのupdate\_resyncメソッドによってレコードを更新する
    
      - 「List」タブでごみ箱アイコンを押したとき、同クラスのdelete\_resyncメソッドによって該当レコードを物理削除する

  - データ収集は、Sync（データ収集）とImport（データ登録）の２段階で行う
    
      - 以下の場合に、invenio\_resourcesyncclient.tasks. resync\_sync関数が非同期で呼び出される
        
          - Detailタブで、「Action」で［Sync］ボタンを押す
        
          - Detailタブで、「Running」でボタンを［ON］にする
        
          - 「Running」のボタンが［ON］の状態で、前回実行時から（interval\_by\_day）日経過したときにrun\_sync\_auto関数が実行される
    
      - resync\_sync関数の中で、invenio\_resourcesyncclient.utils. process\_sync関数によってSyncを行う
        
          - resync\_sync関数が呼び出されると、画面には200のレスポンスが返却される
        
          - ログのLog Typeは「sync」となる
        
          - 処理が終了したとき、ログのStatusは結果にかかわらず「Successful」となる
        
          - resync\_indexesテーブルで、引数のidと等しいidのレコードの情報を用いる
        
          - 以下の場合に、ValueErrorが発生する
            
              - base\_urlフィールドで指定されたxmlファイルのcapabilityを取得できなかった場合
            
              - resync\_modeが「Baseline」で、取得したcapabilityが「resourcelist」でも「resourcedump」でもない場合
            
              - resync\_modeが「Audit」で、取得したcapabilityが「resourcelist」でも「changelist」でもない場合
        
          - 以下の場合に例外クラスを指定しない例外が発生する
            
              - resync\_modeが「Incremental」で、取得したcapabilityが「changelist」でも「changedump」でもない場合
        
          - resync\_modeが「Baseline」または「Audit」のとき、resyncのbaseline\_or\_audit関数によってデータ収集を行う
            
              - baseline\_or\_audit関数については以下を参照
                
                  - <https://github.com/resync/resync/blob/v1.0.9/resync/client.py#L241-L326>
        
          - resync\_modeが「Incremental」のとき、resyncのincremental関数によってSyncを行う
            
              - incremental関数については以下を参照
                
                  - <https://github.com/resync/resync/blob/v1.0.9/resync/client.py#L328-L474>
    
      - 以下の場合に、invenio\_resourcesyncclient.tasks. run\_sync\_import関数が非同期で呼び出される
        
          - Detailタブで、「Action」で［Import］ボタンを押す
        
          - statusが「Automatic」かつresync\_modeが「Audit」でSyncが終了する
            
              - Sync終了時に呼び出されるfinish関数の中で呼び出す
        
          - 「Running」のボタンが［ON］の状態で、前回実行時から（interval\_by\_day）日経過したときにrun\_sync\_auto関数が実行されるようにceleryタスクに登録される
    
      - run\_sync\_import関数の中で、invenio\_resourcesyncclient.utils. process\_item関数によってImportを行う
        
          - run\_sync\_import関数が呼び出されると、画面には200のレスポンスが返却される
        
          - そのResyncでBase Urlに指定したxmlファイルの情報をもとに登録を行う

  - invenio\_resourcesyncclient.tasks. resync\_sync関数、invenio\_resourcesyncclient.tasks. run\_sync\_import関数の中で、invenio\_resourcesyncclient.tasks. prepare\_log関数によってログを作成する
    
      - 作成したログは、resync\_logsテーブルに保存する

  - Detailタブを表示したとき、および［Sync］ボタンまたは［Import］ボタンを押して200のレスポンスを受け取ったときに、resync\_client.jsのhandleGetLogs関数が呼び出される
    
      - handleGetLogs関数の中で、invenio\_resourcesyncclient.admin. AdminResyncClient. get\_logsメソッドによってresync\_logsテーブルからログを取得する
    
      - 取得したテーブルのend\_timeフィールドが空だった場合には、3000ミリ秒後に再度handleGetLogs関数を実行する

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
