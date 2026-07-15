### 統計情報表示

#### 目的・用途

本機能は、アイテムの利用統計情報を閲覧する機能である

#### 利用方法

アイテムの利用統計情報は、アイテム詳細画面の右端にあるViewsエリア、ファイル詳細画面(information)のstatsにおいて閲覧する。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

#### 機能内容

1. アイテムの利用統計情報を表示する

  - アイテムの利用統計情報の表示/非表示を設定する

      - 【Administration > 設定 (Setting) > 統計情報表示 (Stats)画面】での「レコード統計の表示/非表示」（Show/Hide Record Stats）エリアにアイテムの利用統計情報の表示/非表示を設定する

          - 「オン」（On）にすると、アイテム詳細表示画面に利用統計エリア[Stats]を表示する

          - 「オフ」（Off）にすると、アイテム詳細表示画面に利用統計エリア[Stats]を非表示とする

          - デフォルト：「オン」（On）

          - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する  
            メッセージ：  
            　日本語：「設定を変更しました」  
            　英語：「Successfully Changed Settings.」

  - アイテムの利用統計情報を表示する

      - アイテム単位の閲覧回数は、【アイテム詳細画面】での「Views」エリアに表示する

      - アイテム詳細画面に遷移する時に、「record_viewed」というシグナルを読み取る  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/views.py#L451-L456>

          - record_viewedのシグナルはconfigで設定されたタイミング（数秒）で実行されて、閲覧回数をDBから取得しESに登録する。

      - record_viewedのシグナル実行後、invenio-statsが閲覧回数をログ集計をする。 （invenioの処理）  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/views.py#L209-L212>

      - 閲覧回数は、全ドメインと各ドメイン毎（トップレベルドメイン毎）で集計値を表示する

          - 各ドメイン毎（トップレベルドメイン毎）はデフォルト表示を"非表示"とし、「詳細を確認」（See details）リンクを押すことで表示する

              - 確定できないドメインに対して、「UNKNOWN」として表示する

      - 閲覧回数は、集計機関プルダウン「Period」より年月を選択することで指定期間の数値を表示する

          - デフォルトは全期間の数値 (total)とする

2. コンテンツファイル単位の統計情報を表示する

  - 【ファイル詳細画面 (Information)】での「統計」（Stats）タブにコンテンツファイル単位の統計情報を表示する

      - ダウンロード回数は、Downloadsエリアに表示する

      - ファイルをダウンロードされるたびに、「file_downloaded」シグナルを読み取る。  
        このシグナルはDBからダウンロード回数を取得しESに登録する。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/views.py#L766>

      - 再生回数は、「再生回数」（Plays）エリアに表示する

      - ファイルをプレビューされるたびに、「file_previewed」シグナルを読み取る。  
        このシグナルはDBから再生回数を取得しESに登録する。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/views.py#L764>

      - 「file_downloaded」や「file_previewed」シグナル実行後、invenio-statsがダウンロード回数と再生回数をログ集計してくれる　（invenioの処理）

      - 統計情報は、全ドメインと各ドメイン毎（トップレベルドメイン毎）で集計値を表示する

      - 各ドメイン毎（トップレベルドメイン毎）はデフォルト表示を"非表示"とし、「詳細を確認」（See details）リンクを押すことで表示する

          - 確定できないドメインに対して、「UNKNOWN」として表示する

      - 統計情報は、集計機関プルダウン「total」より年月を選択することで指定期間の数値を表示する

          - デフォルトは全期間の数値 (total) とする

      - ダウンロード回数と再生回数は、ファイルの差し替えを行った場合でも統計値は引き継いで集計する

      - 集計はCELERY_BEAT_SCHEDULEのstats-aggregate-events設定に従い実施される。デフォルトでは起動時のタイミングから１日毎に集計される。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L77>

```
'stats-aggregate-events': {
    'task': 'invenio_stats.tasks.aggregate_events',
    'schedule': timedelta(days=1),
    'args': [('celery-task-agg', 'file-download-agg', 'file-preview-agg', 'item-create-agg', 'record-view-agg', 'search-agg', 'top-view-agg')],
},
```

#### 関連モジュール

  - weko_records_ui
  - invenio_stats
  - invenio_files_rest

#### 処理概要

アイテム詳細画面を開く際に、weko_records_ui.views.default_view_methodを呼び出して  
record_viewedに閲覧回数を送り出し、ESに回数を登録する。

  - invenio_stats.views.QueryRecordViewCountにおいて閲覧回数を取得する。

  - weko-admin.models.AdminSettings.getから【Administration > stas (統計情報)】で設定した統計情報の表示を読み取り、display_statsがtrueの場合に統計情報を表示する。

ファイル詳細画面を開く際に、weko_records_ui.view.get_uriを呼び出してfile_downloadedにファイルダウンロード回数を送り出し、ESに回数を登録する。  
ファイルのプレビューが行われる際に、invenio_file_rest.views.ObjectResource.send_objectを呼び出して、file_previewedに再生回数を送り出し、ESに回数を登録する。

  - invenio_stats.views.QueryFileStatsCountにおいてダウンロード回数と再生回数を取得する。weko-admin.models.AdminSettings.getから【Administration > stas (統計情報)】で設定した統計情報の表示を読み取り、display_statsがtrueの場合に統計情報を表示する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 表示回数は `default_view_method` が `record_viewed` を送出、`invenio_stats.views.QueryRecordViewCount` / `QueryFileStatsCount` で取得。`file_downloaded` は `weko_records_ui.views.get_uri` と `invenio_files_rest.views.ObjectResource.send_object` の2箇所で送出。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
