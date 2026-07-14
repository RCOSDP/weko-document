### サイトマップ

## 目的・用途

本機能は、サイトマップを作成しキャッシュに保存する機能である。サイトマップを作成することで、クローラビリティが向上するメリットがある。

## 利用方法

【Administration>設定（Setting）>サイトマップ（Site Map）】の順で画面遷移し、[実行（Run）]ボタンを押下することでサイトマップの作成が可能。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

## 機能内容

1. システムのフォーマットでサイトマップを生成できる

  - 【Administration > 設定（Setting） > サイトマップ（Sitemap）】にサイトマップの生成を実行する。
    
      - [実行（Run）]ボタンを押すと、サイトマップの生成が実行される。
    
      - 実行された後、以下のような生成情報をSitemap画面に表示する。
        
          - 開始時間（Start Time）  
            フォーマット：YYYY-MM-DDThh:mm:ss
        
          - 終了時間（End Time）  
            フォーマット：YYYY-MM-DDThh:mm:ss
        
          - Records Processed
        
          - ステータス（status）：SUCCESS、ERROR
    
      - 出力ファイルは以下の通りである
        
          - sitemap_****.xml.gz  
            「****」は対象アイテム数により10000件ごとに1ずつインクリメンタルされる（0001,0002・・・）
            
              - 1つのqzファイルの中に10000件ごとのXML（sitemap_****.xml）が一つのファイルに格納される
            
              - XMLには一つのアイテムに対して以下のような情報を出力する
                
                  - アイテム詳細URL
                
                  - lastmod  
                    フォーマット：YYYY-MM-DDThh:mm:ss.sTZD  
                    例：2019-03-07T16:36:27+09:00
            
              - アイテム詳細URLがアイテムID順に出力される
            
              - ダウンロードアドレス：「ホスト」/weko/sitemaps/sitemap_****.xml.gz
        
          - sitemapindex.xml  
            上記のsitemap_****.xml.gzを全て出力する
            
              - ダウンロードアドレス：「ホスト」/weko/sitemaps/sitemapindex.xml

2. サイトマップ生成の定期実行を可能

  - 設定した時刻にサイトマップ更新を定期実行する。  
    （更新するタイミングの設定については、以下の処理概要に記載）

## 関連モジュール

  - weko-sitemap

## 処理概要

1. 設定

  - Sitemap画面のテンプレートURLを設定する
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L13
    
      - 設定キー：WEKO_SITEMAP_ADMIN_TEMPLATE  
        現在の設定値:

> WEKO_SITEMAP_ADMIN_TEMPLATE = 'weko_sitemap/sitemap.html'

  - データベースから取得するアイテムの上限レコード数を設定する
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L16 
    
    
      - 設定キー：WEKO_SITEMAP_TOTAL_MAX_URL_COUNT  
        現在の設定値:

> WEKO_SITEMAP_TOTAL_MAX_URL_COUNT = 10000000

  - キャッシュのタイムアウト時間を設定する
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L24 
    
      - 設定キー：WEKO_SITEMAP_CACHE_TIMEOUT  
        現在の設定値:

> WEKO_SITEMAP_CACHE_TIMEOUT = 60 * 60 * 24 * 3
> 
> URLのプレフィックスを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L30

  - 設定キー：SITEMAP_BLUEPRINT_URL_PREFIX  
    現在の設定値:

  - SITEMAP_BLUEPRINT_URL_PREFIX = '/weko/sitemaps'

> 「sitemapindex」URLのエンドポイントを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L32 

  - 設定キー：SITEMAP_ENDPOINT_URL  
    現在の設定値:

> SITEMAP_ENDPOINT_URL = '/sitemapindex.xml'
> 
> 各ページURLのエンドポイントを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L34 

  - 設定キー：SITEMAP_ENDPOINT_PAGE_URL  
    現在の設定値:

> SITEMAP_ENDPOINT_PAGE_URL = '/sitemap_<int:page>.xml.gz'
> 
> Sitemapの上限URL数を設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py#L36

  - 設定キー：SITEMAP_MAX_URL_COUNT  
    現在の設定値:

> SITEMAP_MAX_URL_COUNT = 10000
> 
> 自動更新タイミングを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L119

  - 設定キー：update_sitemap

  - 設定値：days、minutes、hours  
    現在の設定値：

> 'update_sitemap': {
> 
> 'task': 'weko_sitemap.tasks.update_sitemap',
> 
> 'schedule': timedelta(days=3, minutes=0, hours=0),
> 
> 'args': [],
> 
> },

2. 実装方法

  - 【Administration > Setting（設定） > Sitemap】を以下のテンプレートで表示する
    
      - 設定キー：WEKO_SITEMAP_ADMIN_TEMPLATE
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/templates/weko_sitemap/sitemap.html

  - Sitemapを更新する処理
    
      - 【Administration > （設定）Setting > Sitemap】の順でサイトマップ画面へ遷移し[実行（Run）」ボタンを押すと、weko_sitemap.admin.update_sitemapが呼び出され、sitemapの情報を以下のように取得する。
        
          - データベースからの値：pidstore_pid.pid_value、records_metadata.updated
        
        
          - 条件：「pidstore_pid.status = 'R' (registered)」AND「pidstore_pid.pid_type = 'recid'」
        
          - 上限レコード数：「WEKO_SITEMAP_TOTAL_MAX_URL_COUNT」の値
        
          - 取得されたデータをファイルに分ける  
            1つのファイルに格納される上限URL数：「SITEMAP_MAX_URL_COUNT」の値
    
      - 取得されたデータから、Sitemapの情報を以下のように作成する
        
          - アイテム詳細のURLは以下のように構築される

> {
> 
> loc: <invenio_records_ui.recidのURL> + pidstore_pid.pid_value,
> 
> lastmod: records_metadata.updated
> 
> }

  - Sitemapの情報をキャッシュに保存する
    
      - sitemap_<page>.xml.gz

> 'sitemap_' + page_number: {
> 
> lastmod: <現在のシステム日時>,
> 
> page: <アイテム詳細のURL>
> 
> }

  - sitemapindex.xml

> sitemap_page_keys: [
> 
> 'sitemap_' + page_number,
> 
> ...
> 
> ]

  - Sitemap情報をキャッシュから自動的に削除される処理
    
      - キャッシュのタイムアウト時間を以下のコンフィグで設定する  
        設定キー：WEKO_SITEMAP_CACHE_TIMEOUT
    
      - 「page_number」及び「sitemap_page_keys」キャッシュに対してweko_sitemap.ext.set_cache_pageでタイムアウト時間を指定している

  - 「sitemapindex」URL及び各ページURLを構築する
    
      - 「sitemapindex」URL

> WEKO_SITEMAP_URL_SCHEME + <ホスト> + SITEMAP_BLUEPRINT_URL_PREFIX + SITEMAP_ENDPOINT_URL

  - 各ページURL

> WEKO_SITEMAP_URL_SCHEME + <ホスト> + SITEMAP_BLUEPRINT_URL_PREFIX + SITEMAP_ENDPOINT_PAGE_URL

  - Sitemap情報をダウンロードする処理
    
      - sitemapindex.xmlweko_sitemap.ext.get_cache_pageで 上記の「sitemap_page_keys」からのデータを取得し、weko_sitemap.ext.sitemapで以下のように出力する。

> [
> 
> {
> 
> loc: <ファイルのURL>,
> 
> lastmod: 'sitemap_ + page_number'.lastmod
> 
> },
> 
> ...
> 
> ]

  - sitemap_<page>.xml.gz  
    weko_sitemap.ext.pageでURLに入力しているページ番号に応じて、該当「page_number」から取得するデータを出力、weko_sitemap.ext.gzip_responseでデータを「gz」ファイルに圧力する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_sitemap.admin.SitemapSettingView`（endpoint 由来）。[Run] は `POST /update_sitemap`（`SitemapSettingView.update_sitemap`）で Celery タスク `weko_sitemap.tasks.update_sitemap` を `apply_async`（実際のDBクエリ・gz生成はタスク側）。状態表示は `get_task_status`（`/task_status/<task_id>`）。config：`WEKO_SITEMAP_ADMIN_TEMPLATE` / `WEKO_SITEMAP_TOTAL_MAX_URL_COUNT` / `WEKO_SITEMAP_CACHE_TIMEOUT` 等。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
