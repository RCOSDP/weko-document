
### 統計情報表示

  - > 目的・用途

本機能は、アイテムの利用統計情報を閲覧する機能である

  - > 利用方法

アイテムの利用統計情報は、アイテム詳細画面の右端にあるViewsエリア、ファイル詳細画面(information)のstatsにおいて閲覧する。

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

1\. アイテムの利用統計情報を表示する

  - アイテムの利用統計情報の表示/非表示を設定する
    
      - 【Administration \> 設定 (Setting) \> 統計情報表示 (Stats)画面】での「レコード統計の表示/非表示」（Show/Hide Record Stats）エリアにアイテムの利用統計情報の表示/非表示を設定する
        
          - 「オン」（On）にすると、アイテム詳細表示画面に利用統計エリア\[Stats\]を表示する
        
          - 「オフ」（Off）にすると、アイテム詳細表示画面に利用統計エリア\[Stats\]を非表示とする
        
          - デフォルト：「オン」（On）
        
          - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する  
            メッセージ：  
            　日本語：「設定を変更しました」  
            　英語：「Successfully Changed Settings.」

  - アイテムの利用統計情報を表示する
    
      - アイテム単位の閲覧回数は、【アイテム詳細画面】での「Views」エリアに表示する
    
      - アイテム詳細画面に遷移する時に、「record\_viewed」というシグナルを読み取る  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/views.py#L451-L456>
        
          - record\_viewedのシグナルはconfigで設定されたタイミング（数秒）で実行されて、閲覧回数をDBから取得しESに登録する。
    
      - record\_viewedのシグナル実行後、invenio-statsが閲覧回数をログ集計をする。 （invenioの処理）  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/views.py#L209-L212>
    
      - 閲覧回数は、全ドメインと各ドメイン毎（トップレベルドメイン毎）で集計値を表示する
        
          - 各ドメイン毎（トップレベルドメイン毎）はデフォルト表示を"非表示"とし、「詳細を確認」（See details）リンクを押すことで表示する
            
              - 確定できないドメインに対して、「UNKNOWN」として表示する
    
      - 閲覧回数は、集計機関プルダウン「Period」より年月を選択することで指定期間の数値を表示する
        
          - デフォルトは全期間の数値 (total)とする

2\. コンテンツファイル単位の統計情報を表示する

  - 【ファイル詳細画面 (Information)】での「統計」（Stats）タブにコンテンツファイル単位の統計情報を表示する
    
      - ダウンロード回数は、Downloadsエリアに表示する
    
      - ファイルをダウンロードされるたびに、「file\_downloaded」シグナルを読み取る。  
        このシグナルはDBからダウンロード回数を取得しESに登録する。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/views.py#L766>
    
      - 
      - 再生回数は、「再生回数」（Plays）エリアに表示する
    
      - ファイルをプレビューされるたびに、「file\_previewed」シグナルを読み取る。  
        このシグナルはDBから再生回数を取得しESに登録する。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/views.py#L764>
    
      - 「file\_downloaded」や「file\_previewed」シグナル実行後、invenio-statsがダウンロード回数と再生回数をログ集計してくれる　（invenioの処理）
    
      - 統計情報は、全ドメインと各ドメイン毎（トップレベルドメイン毎）で集計値を表示する
    
      - 各ドメイン毎（トップレベルドメイン毎）はデフォルト表示を"非表示"とし、「詳細を確認」（See details）リンクを押すことで表示する
        
          - 確定できないドメインに対して、「UNKNOWN」として表示する
    
      - 統計情報は、集計機関プルダウン「total」より年月を選択することで指定期間の数値を表示する
        
          - デフォルトは全期間の数値 (total) とする
    
      - ダウンロード回数と再生回数は、ファイルの差し替えを行った場合でも統計値は引き継いで集計する
    
      - 集計はCELERY\_BEAT\_SCHEDULEのstats-aggregate-events設定に従い実施される。デフォルトでは起動時のタイミングから１日毎に集計される。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L77>

> 'stats-aggregate-events': {
> 
> 'task': 'invenio\_stats.tasks.aggregate\_events',
> 
> 'schedule': timedelta(days=1),
> 
> 'args': \[('celery-task-agg', 'file-download-agg', 'file-preview-agg', 'item-create-agg', 'record-view-agg', 'search-agg', 'top-view-agg')\],
> 
> },

  - > 関連モジュール

<!-- end list -->

  - > weko\_records\_ui

  - > invenio\_stats

  - > invenio\_files\_rest

<!-- end list -->

  - > 処理概要

> アイテム詳細画面を開く際に、weko\_records\_ui.views.default\_view\_methodを呼び出して  
> record\_viewedに閲覧回数を送り出し、ESに回数を登録する。

  - > invenio\_stats.views.QueryRecordViewCountにおいて閲覧回数を取得する。

  - > weko-admin.models.AdminSettings.getから【Administration \> stas (統計情報)】で設定した統計情報の表示を読み取り、display\_statsがtrueの場合に統計情報を表示する。

> ファイル詳細画面を開く際に、weko\_records\_ui.view.get\_uriを呼び出してfile\_downloadedにファイルダウンロード回数を送り出し、ESに回数を登録する。  
> ファイルのプレビューが行われる際に、invenio\_file\_rest.views.ObjectResource.send\_objectを呼び出して、file\_previewedに再生回数を送り出し、ESに回数を登録する。

  - > invenio\_stats.views.QueryFileStatsCountにおいてダウンロード回数と再生回数を取得する。weko-admin.models.AdminSettings.getから【Administration \> stas (統計情報)】で設定した統計情報の表示を読み取り、display\_statsがtrueの場合に統計情報を表示する。

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