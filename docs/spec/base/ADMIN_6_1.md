### 運用レポート

<!-- end list -->

  - > 目的・用途

本機能は、統計情報のレポートを確認・ダウンロード・メール送信する機能である

  - > 利用方法

【Administration \> 統計（Statistics） \> 運用レポート（Report）画面】で操作を行う。

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
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

1 アイテム登録件数を確認する

  - 【Administration \> 統計（Statistics） \> 運用レポート（Report）画面】での「登録件数」（Number of items registered）エリアにアイテム登録件数を表示する
    
      - 表示項目は以下の通りである
        
          - 「登録件数」（Total number of items registered）
        
          - 「登録済み公開アイテム件数」（Number of open items registered）  
            　アイテムの所属しているインデックスおよび上位のインデックスが「公開状態」で、かつアイテムの公開状態がpublicで、アイテムの公開日が現在または過去日であるアイテムの件数
        
          - 「登録済みプライベートアイテム件数」（Number of private items registered）  
            　以下の条件に該当するアイテムの件数
            
              - アイテムの所属しているインデックスもしくは上位のインデックスが「非公開状態」を含む場合
            
              - インデックスの状態が公開状態であったとしても、インデックスの公開日が未来日の場合
            
              - インデックスの状態が公開状態であったとしても、アイテムの公開状態がprivateの場合
            
              - インデックスの状態が公開状態であったとしても、アイテムの公開日が未来日の場合
    
      - 集計対象外のアイテム
        
          - 新規アイテム登録時のワークフローが未完了のアイテム
        
          - 削除したアイテム

2 定型レポートをダウンロードする

  - 【運用レポート（Report）画面】での「定型レポート」（Fixed Form Reports）エリアに定型レポートをダウンロードできる
    
      - 「月別集計」（Aggregation month）に、定型レポートタイプ、集計年、集計月プルダウンを設ける
        
          - 集計情報はタイムゾーンをベースに処理できるように、ESDateHistogramQuery、ESTermsQuery、ESWekoTermsQueryの3か所にtimezoneを指摘する
        
          - 定型レポートタイプのプルダウンでの選択肢は以下の通りである
            
              - 「すべて」（All）
            
              - 「ファイルダウンロード」（File Downloads）
            
              - 「Paid File Downloads」
            
              - 「ファイルプレビュー」（File Previews）
            
              - 「Paid File Previews」
            
              - 「インデックスアクセス」（Index Access）
            
              - 「アイテムビュー」（Item View）
            
              - 「ユーザー毎に使用するファイル」（File Using Per User）
            
              - 「検索キーワード」（Search Keyword）
            
              - 「トップページへのアクセス」（Top Page Access）
            
              - 「ユーザー」（Users）
            
              - 「サイトアクセス」（Site Access）
        
          - 集計年と集計月で、デフォルト値は当年月とする
    
      - 「月別集計」（Aggregation month）より集計月を選択してから、「ダウンロード」（Download）ボタンを押すと、集計月期間内のレポートを取得できる。期間の終わりは当日の23：59：59となる。
        
          - レポートの出力形式は集計結果をTSV形式で出力したファイルを圧縮したZIPアーカイブをとする

  - 各定型レポートタイプに対して、レポート仕様は以下の通りである

<table>
<thead>
<tr class="header">
<th>#</th>
<th>タイプ</th>
<th>ファイル名</th>
<th>出力内容</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>ファイルダウンロード</td>
<td>logReport_FileDownload_YYYY-MM.tsv</td>
<td>ファイルごとのダウンロード回数を、次の分類順に出力します。<br />
• ファイルダウンロード回数<br />
• オープンアクセスのファイルダウンロード回数<br />
各ファイルダウンロード回数の内訳として、各分類の出力項目は以下の通りです。<br />
• ファイル名<br />
• 登録インデックス名<br />
• ファイルダウンロード回数<br />
• 未ログインユーザー<br />
• ログインユーザー<br />
• サイトライセンス認可ユーザー<br />
• 管理者<br />
• アイテム登録者<br />
※アイテム編集時にファイル差し替え機能を実施した場合、ファイルダウンロード回数は、バージョンごとに集計される</td>
</tr>
<tr class="even">
<td>2</td>
<td>Paid File Downloads</td>
<td>logReport_PayFileDownload_YYYY-MM.tsv</td>
<td>課金ファイルのダウンロード数を出力します。<br />
各ファイルダウンロード回数の内訳として、出力項目は以下の通りです。<br />
• ファイル名<br />
• 登録インデックス名<br />
• ファイルダウンロード回数<br />
• ユーザーグループごとのダウンロード回数（1回以上あるときのみ）<br />
• 未ログインユーザー<br />
• ログインユーザー<br />
• サイトライセンス認可ユーザー<br />
• 管理者<br />
• アイテム登録者</td>
</tr>
<tr class="odd">
<td>3</td>
<td>ファイルプレビュー</td>
<td>logReport_FilePreview_YYYY-MM.tsv</td>
<td>ファイルごとの再生回数を下記の分類順に出力します。<br />
• ファイルプレビュー数<br />
• オープンアクセスのファイルプレビュー数<br />
各ファイル再生回数の内訳として、各分類の出力項目は以下の通りです。<br />
• ファイル名<br />
• 登録インデックス名<br />
• ファイルダウンロード回数<br />
• 未ログインユーザー<br />
• ログインユーザー<br />
• サイトライセンス認可ユーザー<br />
• 管理者<br />
• アイテム登録者※アイテム編集時にファイル差し替え機能を実施した場合、ファイルダウンロード回数は、バージョンごとに集計される</td>
</tr>
<tr class="even">
<td>4</td>
<td>Paid File Previews</td>
<td>logReport_PayFilePreview_YYYY-MM.tsv</td>
<td>課金ファイルの再生回数を出力します。<br />
各ファイル再生回数の内訳として、出力項目は以下の通りです。<br />
• ファイル名<br />
• 登録インデックス名<br />
• ファイルダウンロード回数<br />
• ユーザーグループごとのダウンロード回数（1回以上あるときのみ）<br />
• 未ログインユーザー<br />
• ログインユーザー<br />
• サイトライセンス認可ユーザー<br />
• 管理者<br />
• アイテム登録者</td>
</tr>
<tr class="odd">
<td>5</td>
<td>インデックスアクセス</td>
<td>logReport_IndexAccess_YYYY-MM.tsv</td>
<td>各インデックスに所属するアイテムのアイテム詳細画面閲覧回数を出力します。<br />
出力項目は以下の通りです。<br />
• 詳細ビュー合計<br />
• 閲覧回数</td>
</tr>
<tr class="even">
<td>6</td>
<td>アイテムビュー</td>
<td>logReport_DetailView_YYYY-MM.tsv</td>
<td>アイテムごとの再生回数を出力します。<br />
各ファイル再生回数の内訳として、出力項目は以下の通りです。<br />
• タイトル<br />
• 登録インデックス名<br />
• 閲覧回数<br />
• 未ログインユーザー</td>
</tr>
<tr class="odd">
<td>7</td>
<td>ユーザー毎に使用するファイル</td>
<td>logReport_FileUsingPerUser_YYYY-MM.tsv</td>
<td>ユーザー別のファイルのダウンロード回数、再生回数を出力します。<br />
出力項目は以下の通りです。<br />
• メールアドレス<br />
• ユーザ名<br />
• ファイルダウンロード回数<br />
• ファイル再生回数</td>
</tr>
<tr class="even">
<td>8</td>
<td>検索キーワード</td>
<td>logReport_SearchCount_YYYY-MM.tsv</td>
<td>各検索キーワードの検索回数を出力します。<br />
出力項目は以下の通りです。<br />
• キーワード<br />
• 検索回数</td>
</tr>
<tr class="odd">
<td>9</td>
<td>トップページへのアクセス</td>
<td>logReport_TopPageAccess_YYYY-MM.tsv</td>
<td>ホスト別のトップページアクセス回数を出力します。<br />
出力項目は以下の通りです。<br />
• ホスト<br />
• IPアドレス<br />
• WEKOトップページアクセス回数</td>
</tr>
<tr class="even">
<td>10</td>
<td>ユーザー</td>
<td>logReport_UserAffiliate_YYYY-MM.tsv</td>
<td>権限別の登録ユーザー数を出力します。<br />
出力項目は以下の通りです。<br />
• ロール<br />
• ユーザー数</td>
</tr>
<tr class="odd">
<td>11</td>
<td>サイトアクセス</td>
<td>logReport_SiteAccess_YYYY-MM.tsv</td>
<td>サイトライセンスを設定しているホストまたはユーザーと、サイトライセンス以外からのアクセス回数を下記の分類順に出力します。<br />
• サイトライセンス別アクセス数<br />
• サイトライセンス別アクセス数内訳<br />
出力項目は以下の通りです。<br />
• 機関名（サイトライセンス別のアクセス回数に出力します）<br />
• WEKO3トップページアクセス回数<br />
• 検索回数<br />
• 閲覧回数<br />
• ファイルダウンロード回数<br />
• ファイル再生回数<br />
※アイテム編集時にファイル差し替え機能を実施した場合、ファイルダウンロード回数は、バージョンごとに集計される</td>
</tr>
</tbody>
</table>

  - 統計情報が存在しない場合はヘッダ行のみのレポート結果が出力される

  - 集計対象が存在しない場合は０件としてレポート結果が出力される

  - アイテム編集時にファイル差し替え機能を実施した場合、ファイルダウンロード回数は、バージョンごとに集計する

3 定型レポートをメールで送信する

【前提条件】

メールを送信するため、【Administration \> 設定（Setting） \> メール送信（Mail）画面】に送信元の情報を設定したことが必要になる

  - 「メール受信」（Receive Mail）でメールアドレスを設定する
    
      - 入力エリアに定型レポートを受け取るメールアドレスを入力可能とする
    
      - ［メールアドレス（Email Address）］ボタンを押すと、入力エリアを追加で表示する
        
          - 表示している入力エリアにメールアドレスを入力しない場合、入力エリアが追加不可とする。エラーメッセージを画面の上部に表示する

> エラーメッセージ：「Please check email input fields.」

  - 一番上の入力エリアにメールアドレスを入力した状態でボタンを押すと、追加で表示した入力エリアにそのメールアドレスが設定され、一番上の入力エリアは空になる

<!-- end list -->

  - メールアドレスを入力したエリアに［X］ボタンを設ける。押すと、該当エリアを削除する

  - 「保存」（Save）ボタンを押すと、入力データをシステム内で保持して、メッセージを画面の上部に表示する

> メッセージ：「Successfully saved email addresses.」

  - 一番上の入力エリアにメールアドレスを入力した状態でボタンを押すと、追加で表示した入力エリアにそのメールアドレスが設定され、一番上の入力エリアは空になる

<!-- end list -->

  - メールを手動送信する
    
      - 「月別集計」（Aggregation month）より集計月を選択してから、「送信」（Send）ボタンを押すと、メール送信確認ダイヤログを表示する

> 確認メッセージ：  
> 日本語：「メールを送信してもよろしいですか？」  
> 英語：「Are you sure you want to send the mail?」

  - ［Confirm］ボタンを押すと、集計月期間内のレポートを取得して、「メール受信」（Receive Mail）に設定されたメール購読者に定型レポートメールが送信される
    
      - 各定型レポートタイプに対してのメール内容について、「2 定型レポートをダウンロードする」での「各定型レポートタイプ」を参照する
    
      - メールを送信した後、メッセージを画面の上部に表示する

> メッセージ：  
> 日本語：「レポートを送信しました」  
> 英語：「Successfully sent the reports to the recepients.」

  - メール送信時、エラーが出る場合、エラーメッセージを画面の上部に表示する

<!-- end list -->

  - ［閉じる（Close）］ボタンを押すと、メール送信確認ダイヤログを閉じる

<!-- end list -->

  - メールを定期送信する
    
      - 「メールスケジュールの報告」（Report Email Schedule）にメールスケジュールの設定を設ける
        
          - 「送信間隔」（Transmission Interval）プルダウンに送信周期を設定する  
            選択肢：「Daily、Weekly、Monthly」
        
          - 定型レポートのオン・オフ
            
              - 定型レポートをオンと設定する場合、設定された送信周期に基づき定型レポートメールが送信される
            
              - 定型レポートをオフと設定する場合、定型レポートメールは送信されないようにする
        
          - ［保存（Save）］ボタンを押すと、確認ダイヤログを表示する

> 確認メッセージ：  
> 日本語：「変更してもよろしいですか？」  
> 英語：「Are you sure you want to save changes?」

  - ［Confirm］ボタンを押すと、設定した内容を保存し、メッセージを画面の上部に表示する

> メッセージ：  
> 日本語：「スケジュールを変更しました」  
> 英語：「Successfully Changed Schedule.」

  - ［閉じる（Close）］ボタンを押すと、確認ダイヤログを閉じる

4 カスタムレポートを設定する

  - 「Custom Report」エリアにカスタムレポートの取得条件を設定する
    
      - 設定項目は以下のように設ける
        
          - 「Start Date」- 「End Date」
            
              - カレンダーから選択し、または手入力できる
            
              - 範囲は00:00:00-23:59:59
        
          - 「Target Report」プルダウン
            
              - 必須項目とする
            
              - 以下の対象カスタムレポートを選択できる
                
                  - 「Item registration report」
                
                  - 「Item detail view report」
                
                  - 「Contents download report」
        
          - 「Unit」プルダウン
            
              - 必須項目とする
            
              - 初期状態は非活性とし、「Target Report」プルダウンを選択した後、活性化とする
            
              - 以下の単位を選択できる
                
                  - 「Day」
                
                  - 「Week」
                
                  - 「Year」
                
                  - 「Item」（「Item detail view report」、または「Contents download report」を選択する場合、表示する）
                
                  - 「Host」

  - ［Display］ボタンを押すと、各設定項目に応じた集計結果が「Result」に表示される
    
      - 「Target Report」プルダウン、「Unit」プルダウンに取得条件を選択しない場合、エラーメッセージを表示する  
        エラーメッセージ：「項目名 is required\!」
    
      - 「Unit」が「Item」または「Host」で、取得結果がない場合、メッセージを表示する  
        メッセージ：「There is no data.」
    
      - 「Start Date」及び「End Date」を入力する場合、入力値のバリデーションをチェックする
        
          - 入力によって「YYYY/M/D」形式の日付でなくなるとき、そうなった入力欄の枠が赤くなり、メッセージ「Format is incorrect\!」
            
              - この状態でも［Display］ボタンを押すことができる
            
              - 入力値によっては、この状態で［Display］ボタンを押して集計結果を表示させることができる。詳細は実装内容を参照
        
          - ［Display］ボタンを押すとバリデーションチェックを行い、エラーがある場合、エラーメッセージを表示する
            
              - 片方でも不正な日付である：「Date is not valid\!」
                
                  - ISO 8601 形式で解釈できない場合に不正となる
            
              - End Date \< Start Date：「Start date is greater than End date\!」
        
          - バリデーションチェックでエラーにならなかったとしても、入力値が「年・月・日」の順番でない場合は何も表示されない

  - 各単位に応じて、カスタムレポートに表示する項目について
    
      - 「Day」、「Week」、「Year」に対して  
        表示項目：「Period」、「Counts」  
        また、「Week」の期間は以下のようにする
        
          - 「Start Date」と「End Date」が片方でも空欄の場合は、月曜日～日曜日
        
          - 「Start Date」と「End Date」の両方に入力されている場合は、「Start Date」を起点とする一週間

> 「Start Date」と「End Date」の入力状態によって、表示内容は以下のようにする

  - 「Start Date」と「End Date」が片方でも空欄の場合は、範囲内でも０件の年、月、日は表示しない

  - 「Start Date」と「End Date」の両方に入力されている場合は、範囲内で０件の年、月、日を表示する

<!-- end list -->

  - 「Item」  
    表示項目：「Item ID」、「Item Name」、「Counts」  
    「Start Date」「End Date」が入力されている場合、その範囲内の集計結果を表示する

  - 「Host」  
    表示項目：「Host」、「IP Address」、「Counts」  
    「Start Date」「End Date」が入力されている場合、その範囲内の集計結果を表示する

<!-- end list -->

  - 統計情報が存在しない場合はヘッダ行のみのレポート結果が出力される

  - 集計対象が存在しない場合は０件としてレポート結果が出力される

  - Item registration reportの集計対象はワークフローで新規登録したアイテム、インポート機能で新規登録したアイテム、ハーベスト機能で登録したアイテムとする。  
    ※アイテム編集時やResourceSyncで登録したアイテムについては集計対象外とする

  - ファイルを差し替えた場合、カスタムレポートのファイルダウンロード数の統計情報はバージョンごとに集計される

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > 「weko-admin」

  - > 「invenio-stats」：QueryItemRegReportHelper.getメソッドでカスタムレポートの表示情報を作成する

<!-- end list -->

  - > 処理概要

1\. 設定

> 送信間隔の選択肢を設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L125>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_FREQUENCIES

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_FREQUENCIES = \['daily', 'weekly', 'monthly'\]
> 
> 「メールスケジュールの報告」でのデフォルトを設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L128>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_DELIVERY\_SCHED

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_DELIVERY\_SCHED = {
> 
> 'frequency': 'daily', 'details': '', 'enabled': False
> 
> }
> 
> csvファイルに各定型レポートタイプのヘッダーを設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L139>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_HEADERS

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_HEADERS = {
> 
> 'file\_download': \_('No. Of File Downloads'),
> 
> 'file\_preview': \_('No. Of File Previews'),
> 
> 'billing\_file\_download': \_('No. Of Paid File Downloads'),
> 
> 'billing\_file\_preview': \_('No. Of Paid File Previews'),
> 
> 'index\_access': \_('Detail Views Per Index'),
> 
> 'detail\_view': \_('Detail Views Count'),
> 
> 'file\_using\_per\_user': \_('Usage Count By User'),
> 
> 'search\_count': \_('Search Keyword Ranking'),
> 
> 'top\_page\_access': \_('Number Of Access By Host'),
> 
> 'user\_roles': \_('User Affiliation Information'),
> 
> 'site\_access': \_('Access Count By Site License')
> 
> }
> 
> csvファイルに各定型レポートタイプのサブヘッダーを設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L154>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_SUB\_HEADERS

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_SUB\_HEADERS = {
> 
> 'file\_download': \_('Open-Access No. Of File Downloads'),
> 
> 'file\_preview': \_('Open-Access No. Of File Previews'),
> 
> 'site\_access': \_('Access Number Breakdown By Site License')
> 
> }
> 
> 各定型レポートの出力カラムを設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L161>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_COLS

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_COLS = {
> 
> 'file\_download': \[
> 
> \_('File Name'), \_('Registered Index Name'),
> 
> \_('No. Of Times Downloaded'), \_('Non-Logged In User'),
> 
> \_('Logged In User'), \_('Site License'), \_('Admin'),
> 
> \_('Registrar')\],
> 
> 'file\_preview': \[
> 
> \_('File Name'), \_('Registered Index Name'),
> 
> \_('No. Of Times Viewed'), \_('Non-Logged In User'),
> 
> \_('Logged In User'), \_('Site License'), \_('Admin'),
> 
> \_('Registrar')\],
> 
> 'index\_access': \[\_('Index'), \_('No. Of Views')\],
> 
> 'detail\_view': \[
> 
> \_('Title'), \_('Registered Index Name'), \_('View Count'),
> 
> \_('Non-logged-in User')\],
> 
> 'file\_using\_per\_user': \[\_('Mail address'),
> 
> \_('Username'),
> 
> \_('File download count'),
> 
> \_('File playing count')\],
> 
> 'search\_count': \[\_('Search Keyword'), \_('Number Of Searches')\],
> 
> 'top\_page\_access': \[\_('Host'), \_('IP Address'),
> 
> \_('WEKO Top Page Access Count')\],
> 
> 'user\_roles': \[\_('Role'), \_('Number Of Users')\],
> 
> 'site\_access': \[\_('WEKO Top Page Access Count'),
> 
> \_('Number Of Searches'), \_('Number Of Views'),
> 
> \_('Number Of File download'),
> 
> \_('Number Of File Regeneration')\]
> 
> }
> 
> 定型レポートのファイル名を設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L191>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_FILE\_NAMES

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_FILE\_NAMES = {
> 
> 'file\_download': \_('FileDownload\_'),
> 
> 'file\_preview': \_('FilePreview\_'),
> 
> 'billing\_file\_download': \_('PayFileDownload\_'),
> 
> 'billing\_file\_preview': \_('PayFilePreview\_'),
> 
> 'index\_access': \_('IndexAccess\_'),
> 
> 'detail\_view': \_('DetailView\_'),
> 
> 'file\_using\_per\_user': \_('FileUsingPerUser\_'),
> 
> 'search\_count': \_('SearchCount\_'),
> 
> 'user\_roles': \_('UserAffiliate\_'),
> 
> 'site\_access': \_('SiteAccess\_'),
> 
> 'top\_page\_access': \_('TopPageAccess\_'),
> 
> }
> 
> 定型レポートメールのテンプレートを設定する

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L206>

  - > 設定キー：WEKO\_ADMIN\_REPORT\_EMAIL\_TEMPLATE

  - > 現在の設定値：

> WEKO\_ADMIN\_REPORT\_EMAIL\_TEMPLATE = 'weko\_admin/email\_templates/report.html'
> 
> aggregateionsデータをDBに格納するかを設定する。

  - > パス： modules/invenio-stats/invenio\_stats/config.py

  - > 設定キー：STATS\_WEKO\_DB\_BACKUP\_EVENTS, STATS\_WEKO\_DB\_BACKUP\_AGGREGATION, STATS\_WEKO\_DB\_BACKUP\_BOOKMARK

  - > 現在の設定値：

> STATS\_WEKO\_DB\_BACKUP\_EVENTS = True
> 
> """Enable DB backup of events."""
> 
> STATS\_WEKO\_DB\_BACKUP\_AGGREGATION = False
> 
> """Enable DB backup of aggregation."""
> 
> STATS\_WEKO\_DB\_BACKUP\_BOOKMARK = False
> 
> """Enable DB backup of bookmark."""
> 
> invenio\_stats.tasks.aggregate\_events 実行時の集計範囲は --start-date, --end-date に指定された日付を元に集計する。

  - > 関連コード： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/aggregations.py#L385>

> Celeryタスクとしてinvenio\_stats.tasks.aggregate\_eventsが実行された場合の集計範囲は start\_date, end\_date と、update\_bookmark を元に集計する。デフォルト値は以下の通り。

  - > start\_date, end\_date: None

  - > update\_bookmark: True  
    > （メモ：Celeryタスクが１分に１回、自動的に実行している）

> start\_date は以下のデータ値を取得する

1.  > bookmarkから取得された日付。すなわち、前回に集計された時の end\_date。

2.  > 1.のデータがなければ、events-statsから取得された最古の日付。

> 参照コード： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/aggregations.py#L391-L395>
> 
> end\_date は以下のデータの一番小さい値となる

1.  > 現在の日付

2.  > start\_date + 7 days

> 参照コード: <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/aggregations.py#L400-L406>
> 
> update\_bookmark はパフォーマンスを改善するために、以前に集計された events-stats を再実行しないように制御するもの。デフォルト値はTrue。
> 
> events-stats があって stats の集計がないものはすべて対象になる

  - > bookmarkに保存されているデータを元に判断し、以前に集計されたevents-statsを再実行しないように制御している

【補足】

> aggregation情報の、ESへの登録、削除を行うコマンド操作についての説明は以下を参考
> 
> **ESから**aggregation**情報を消せるCLI:**  
> Usage: invenio stats aggregations delete-index \[OPTIONS\] \[AGGREGATION\_TYPES\]  
> AGGREGATION\_TYPES: The aggregation types. (Aggregation type value: celery-task|file-download|file-preview|record-view|item-create|search|top-view)
> 
> Options:
> 
> \-b, --bookmark: Delete bookmark index on Elasticsearch.
> 
> \-s, --suffix: Suffix of index, if not entered then default is \*. Ex: 2020
> 
> \-f, --force: Ignore Elasticsearch errors when performing Elasticsearch index deletion
> 
> \-v, --verbose: Displays information about indexes to be deleted
> 
> \--yes-i-know: Confirm deletion of the Elasticsearch index
> 
> Example:

  - > a. Command line to delete all aggregations index and bookmark in Elasticsearch and ignore Elasticsearch error:

> invenio stats aggregations delete-index -b -f --yes-i-know

  - > b. Delete all indexes of an aggregation (Ex: record-view).

> invenio stats aggregations delete-index --yes-i-know record-view

  - > c. Delete all indexes of multiple aggregation (Ex: record-view and item-create)

> invenio stats aggregations delete-index --yes-i-know record-view item-create

  - > d. Exactly delete an index of an aggregation (Ex: tenant1-events-stats-item-create-2020)

> invenio stats aggregations delete-index -s 2020 --yes-i-know item-create
> 
> **aggregation情報をDBからESに登録できるCLI:**  
> Usage: invenio stats aggregations restore \[OPTIONS\] \[AGGREGATION\_TYPES\]  
> AGGREGATION\_TYPES: The aggregation types. (Aggregation type value: celery-task|file-download|file-preview|record-view|item-create|search|top-view)
> 
> Options:
> 
> \-b, --bookmark: Restore bookmark index on Elasticsearch.
> 
> \-s, --suffix: Suffix of index, if not entered then default is \*. Ex:2020
> 
> \-f, --force: Ignore Elasticsearch errors when performing Elasticsearch index restoration.
> 
> \-v, --verbose: Displays information about indexes to be restored.
> 
> Example:

  - > a. Command line to restore all aggregation and bookmark data in DB to ES and ignore Elasticsearch error:

> invenio stats aggregation restore -b -f

  - > b. Restore all data from DB of an aggregation(Ex: record-view).

> invenio stats aggregation restore record-view

  - > c. Restore all data of multiple aggregations from DB (Ex: record-view and item-create)

> invenio stats aggregation restore record-view item-create

  - > d. Exactly restore data of an index of an aggregation (Ex: tenant1-stats-item-create-2020)

> invenio stats aggregation restore -s 2020 item-create

2\. 実装方法

> 対応しているモジュール：「weko-admin, weko-search-ui, invenio\_stats」
> 
> フィードバックメールは、ESから全件を取得後に条件で絞り込む。

  - > 実装箇所:modules/weko-search-ui/weko\_search\_ui/query.py

  - > 実装箇所:modules/weko-search-ui/weko\_search\_ui/utils.py

> 「Custom Report」エリアの「Start Date」「End Date」の入力値のチェックは、以下のようになっている。

  - > https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko\_admin/static/js/weko\_admin/custom\_report.js
    
      - > 入力すると、ComponentDatePickerのhandleChangeEventで、以下のどちらかでフォームの外観を変更する。どちらも満たさなくなると元に戻る。
        
          - > JavascriptのDate.parse()メソッドで解釈できない
        
          - > 入力値を「/」で分割した配列の長さが3でない
    
      - > ［Display］ボタンを押すと、ComponentComboboxのhandleClickEvent中でcheckValidDateメソッドによるチェックを行う。以下のどちらかで、エラーメッセージをポップアップで表示する。
        
          - > 「Start Date」「End Date」の入力値の片方でもJavascriptのDate.parse()メソッドで解釈できない
        
          - > 「Start Date」\>「End Date」

  - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/utils.py>
    
      - > QueryItemRegReportHelper.getメソッドで、入力値を受け取ってカスタムレポートを返す。
        
          - > ここでは、pythonのdatetime.strptime(入力値, '%Y-%m-%d')で入力値を日付オブジェクトに変換している。入力値が'%Y-%m-%d'のフォーマットで構文解析できない場合、ValueErrorによって処理が中断され、カスタムレポートが返されない。

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
<td>V0.9.27</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>

