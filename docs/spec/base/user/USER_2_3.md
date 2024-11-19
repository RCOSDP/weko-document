### 雑誌情報

<!-- end list -->

  - > 目的・用途

本機能は、インデックスの雑誌情報を管理（追加・編集・削除）、エクスポート時の出力を設定する機能である

  - > 利用方法

1.【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集(Edit Tree)】で編集するインデックスツリーを選ぶ。

2.「表示形式(検索結果)」の選択肢から「一覧形式」を設定する。

3.【Administration \> インデックスツリー管理(Index Tree) \> 雑誌情報(Journal Information)】で編集するインデックツリーを選ぶ。

4\. ジャーナルエリアの「Output」を選び、雑誌情報の必須項目他を設定し、保存する。

5\. インデックス検索を行う。

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
<td>○</td>
</tr>
</tbody>
</table>

  - > 機能内容

1 インデックスの雑誌情報を追加する

  - インデックスの雑誌情報の表示は、  
    【Administration \> インデックスツリー管理(Edit Tree) \> 雑誌情報(Journal Information)】での「表示形式(検索結果)」（Display Format(Search Results)）が「一覧形式(List)」である場合のみである。
    
      - インデックス雑誌情報  
        【Administration \> インデックスツリー管理(Edit Tree) \> 雑誌情報(Journal Information)】にて雑誌情報を登録済み、および「出力する」に設定されている場合のみ、以下のインデックス情報および雑誌情報を初期表示する。
        
          - > インデックスリスト
        
          - > インデックス.サムネイル画像
        
          - > 「タイトル」
        
          - 雑誌情報.雑誌名
        
          - 雑誌情報.別タイトル
        
          - 雑誌情報.出版者
        
          - 雑誌情報.言語
        
          - 雑誌情報.プリント版ISSN / プリント版ISBN
        
          - 雑誌情報.eISSN / eISBN
        
          - インデックス.コメント
        
          - 表示しているインデックスの検索URL
    
      - 詳細表示リンク  
        その他の登録されている雑誌情報は、初期表示では［▷詳細］リンクを表示し、非表示とする。［▷詳細］リンクをクリックすると、以下の情報が表示される。
        
          - カバー範囲
        
          - 変遷前誌のタイトルID
        
          - NCID
        
          - プリント版ISSN/プリント版ISBN
        
          - 最古オンライン巻号の出版年月日
        
          - NDL請求記号
        
          - 提供最古号
        
          - 資料種別
        
          - 提供最新号
        
          - 提供最新巻
        
          - タイトルヨミ
        
          - NDL書誌ID
        
          - 提供最古巻
        
          - カバー範囲に関する注記
        
          - シリーズのタイトルID
        
          - J-STAGE資料コード（雑誌名の略称）
        
          - その他のタイトル（他の言語でのタイトルなど）
        
          - 最新オンライン巻号の出版年月日
        
          - 医中誌ジャーナルコード
        
          - エンバーゴ情報
        
          - アクセスモデル

  - 【Administration \> インデックスツリー管理(Edit Tree) \> 雑誌情報(Journal Information)】でのインデックスツリーにインデックスを選択した状態でインデックスの雑誌情報が設定できる
    
      - 「Root Index」を選択する場合、雑誌情報の入力エリアが非活性とする
    
      - 一覧形式表示する際の雑誌情報出力の設定エリア
        
          - 「ジャーナル(Journal)」に、「Output」/「Do not output」ラジオボタンで設定できる。初期値は「Do not output」である
            
              - 「Output」を選択する場合、設定されたインデックスの雑誌情報を表示させる。
            
              - 「Do not output」を選択する場合、すでに登録済みの情報があればデータはそのまま保持して画面表示のみ非表示とする。
            
              - 必須項目を入力後、最下部の「保存」ボタンを押下することで雑誌情報の初期登録は完了となる。
            
              - 必須項目は「タイトル(Title)」、「最古オンライン巻号の出版年月日(Date of first issue available online)」、「カバー範囲(Coverage depth)」、「資料種別(Publication type)」、「アクセスモデル(Access type)」、「言語(langueage)」である。
            
              - 項目の詳細については[ADMIN-3-2 雑誌情報](#雑誌情報-1)を参照すること。

2 インデックスの雑誌情報をKBART形式で出力できる

  - 本機能は、RabbitMQ/Celeryを用いて非同期バッチ処理とする。

  - 登録された雑誌情報は、  
    ERDB（Electronic Resources Database = 電子リソース管理データベース）が  
    取り込めるKBART2拡張形式で出力可能とする　【参考情報】 [ERDB-JP連携マニュアル.pdf](https://redmine.devops.rcos.nii.ac.jp/attachments/download/4308/ERDB-JP%E9%80%A3%E6%90%BA%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB.pdf)
    
      - 出力対象は、インデックスの雑誌出力設定が "出力する（Output）" となっているもの全てとする
    
      - 出力項目は、「 [WEKO\_KBART出力項目一覧\_v1.17.xlsx](https://redmine.devops.rcos.nii.ac.jp/attachments/download/4677/WEKO_KBART%E5%87%BA%E5%8A%9B%E9%A0%85%E7%9B%AE%E4%B8%80%E8%A6%A7_v1.17.xlsx) 」に記載される下記 34項目 とする
    
      - 出力形式は、tsv形式とする。
    
      - 出力は自動で行われる。デフォルトでは1日おきに出力される。間隔の変更、手動での出力方法については処理概要を参照すること
    
      - 出力されたファイルのweb上での確認方法について  
        出力された際には、最も新しく出力されたファイルの名前が  
        URL:「自機関のリポジトリURL」＋「/static/weko/kbart/filelist.txt」  
        に出力され、確認できる。  
          
        「自機関のリポジトリURL」＋「/static/weko/kbart/”確認したいファイルの名前”」で出力されたファイルを確認できる。  
        例https://192.168.56.103/static/weko/kbart/WEKO\_AllTitles\_2023-07-25.txt
    
      - 出力順序は、下記項目を上から順に出力する
        
        1.  publication\_title
        
        2.  print\_identifier
        
        3.  online\_identifier
        
        4.  date\_first\_issue\_online
        
        5.  num\_first\_vol\_online
        
        6.  num\_first\_issue\_online
        
        7.  date\_last\_issue\_online
        
        8.  num\_last\_vol\_online
        
        9.  num\_last\_issue\_online
        
        10. title\_url
        
        11. first\_author
        
        12. title\_id
        
        13. embargo\_info
        
        14. coverage\_depth
        
        15. notes
        
        16. publisher\_name
        
        17. publication\_type
        
        18. date\_monograph\_published\_print
        
        19. date\_monograph\_published\_online
        
        20. monograph\_volume
        
        21. monograph\_edition
        
        22. first\_editor
        
        23. parent\_publication\_title\_id
        
        24. preceding\_publication\_title\_id
        
        25. access\_type
        
        26. language
        
        27. title\_alternative
        
        28. title\_transcription
        
        29. ncid
        
        30. ndl\_callno
        
        31. ndl\_bibid
        
        32. jstage\_code
        
        33. ichushi\_code
        
        34. deleted
    
      - 雑誌情報出力処理（RabbitMQ/Celery非同期処理）について、出力インターバルをコンフィグファイルに設定可能とする
    
      - また、雑誌情報の出力結果をログ出力できる
        
          - ログ出力は invenio-loggingを利用して実装する
        
          - ログ出力内容は以下とする  
            （ただし、ステータスコードはinvenio-loggingの仕様に準拠する）

| \# | ログレベル | ステータスコード | ログ内容                 |
| -- | ----- | -------- | -------------------- |
| 1  | INFO  | 0        | 正常終了                 |
| 2  | ERROR | 1        | 不明なエラーによる終了          |
| 3  | ERROR | 3        | 多重実行エラーにより実行が行われなかった |
| 4  | ERROR | 100      | データ取得エラー(DBエラー)      |
| 5  | ERROR | 101      | 設定ファイル不正エラー          |

  - > 関連モジュール

<!-- end list -->

  - > weko\_search\_ui

  - > weko-indextree-journal

<!-- end list -->

  - > 処理概要

雑誌情報の表示

  - 雑誌情報の表示
    
      - > 雑誌情報の設定が「出力する」になっていて、かつ、雑誌情報が設定されている状態でインデックスツリー検索、またはインデックスリンク検索を行う。その時、weko\_search\_ui.views.searchメソッドにてget\_journal\_infoを使ってそのインデックスに所属する雑誌情報を取得し、表示する。  
        > なお、「出力する」の設定はjournalテーブルの列「is\_output」を参照する。
    
      - > 初期表示は雑誌情報をキー名"publication\_title"、"publisher\_name"、"language”、"online\_identifier"、"openSearchUrl"の順に値を表示していく。詳細表示のキー名についてはweko\_search\_ui.indexlist.htmlを参照すること

  - 雑誌情報設定画面の処理については[ADMIN-3-2 雑誌情報](#雑誌情報-1)を参照すること。

  - 雑誌情報出力処理について。
    
      - 雑誌情報出力処理はweko\_indextree\_journal.tasks.export\_journal\_taskメソッドで行われ、kbart2拡張形式のtxtファイルで出力される。同ディレクトリにfilelist.txtとして出力されたファイル名を記載したtxtファイルも出力する。
    
      - デフォルトの実行スケジュールは以下のセロリタスクで設定される。  
        パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg>
    
      - タスク名：「indextree-journal-export-journal」
    
      - スケジュールを変更したい場合は、キー’schedule’の値を変更すること

> 'indextree-journal-export-journal': {
> 
> 'task': 'weko\_indextree\_journal.tasks.export\_journal\_task',
> 
> 'schedule': timedelta(days=1),
> 
> 'args': \[('p\_path')\],
> 
> },

  - 雑誌情報出力結果をログ出力の処理について、  
    別紙「weko-logging-instruction.xlsx」 を参照すること。

  - ファイルの出力先
    
      - var/instance/static/weko/kbart（web container）
    
      - 以下のコマンドを実行することで、ファイルの参照が可能

> docker-compose exec web bash
> 
> cdvirtualenv
> 
> cd var/instance/static/weko/kbart
> 
> ls

  - filelist.txt（ファイル名の情報）  
    var/instance/static/weko/kbart/filelist.txt

  - 登録済みの雑誌情報：
    
      - 例：  
        var/instance/static/weko/kbart/WEKO\_AllTitles\_2021-09-28.txt  
        var/instance/static/weko/kbart/WEKO\_AllTitles\_2021-09-27.txt

<!-- end list -->

  - ログの出力先
    
      - /work/weko\_devXX/celery.log
    
      - ログはファイル出力であり、APIは実装していない。登録された雑誌情報をログファイルで出力している。
    
      - 雑誌情報を含むcelery.logのサンプルは [こちら](https://redmine.devops.rcos.nii.ac.jp/attachments/26367/celery.log)

  - 手動での雑誌情報出力方法について  
    以下のコードをターミナルに入力する。

> docker-compose exec -u root web celery -A invenio\_app.celery call weko\_indextree\_journal.tasks.export\_journal\_task --args='\[{"p\_path":"var/instance/static/weko/kbart/"}\]'

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
