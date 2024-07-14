
### サイトマップ

  - > 目的・用途

本機能は、サイトマップを作成しキャッシュに保存する機能である。サイトマップを作成することで、クローラビリティが向上するメリットがある。

  - > 利用方法

【Administration\>設定（Setting）\>サイトマップ（Site Map）】の順で画面遷移し、\[実行（Run）\]ボタンを押下することでサイトマップの作成が可能。

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
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

1\. システムのフォーマットでサイトマップを生成できる

  - 【Administration \> 設定（Setting） \> サイトマップ（Sitemap）】にサイトマップの生成を実行する。
    
      - \[実行（Run）\]ボタンを押すと、サイトマップの生成が実行される。
    
      - 実行された後、以下のような生成情報をSitemap画面に表示する。
        
          - 開始時間（Start Time）  
            フォーマット：YYYY-MM-DDThh:mm:ss
        
          - 終了時間（End Time）  
            フォーマット：YYYY-MM-DDThh:mm:ss
        
          - Records Processed
        
          - ステータス（status）：SUCCESS、ERROR
    
      - 出力ファイルは以下の通りである
        
          - sitemap\_\*\*\*\*.xml.gz  
            「\*\*\*\*」は対象アイテム数により10000件ごとに1ずつインクリメンタルされる（0001,0002・・・）
            
              - 1つのqzファイルの中に10000件ごとのXML（sitemap\_\*\*\*\*.xml）が一つのファイルに格納される
            
              - XMLには一つのアイテムに対して以下のような情報を出力する
                
                  - アイテム詳細URL
                
                  - lastmod  
                    フォーマット：YYYY-MM-DDThh:mm:ss.sTZD  
                    例：2019-03-07T16:36:27+09:00
            
              - アイテム詳細URLがアイテムID順に出力される
            
              - ダウンロードアドレス：「ホスト」/weko/sitemaps/sitemap\_\*\*\*\*.xml.gz
        
          - sitemapindex.xml  
            上記のsitemap\_\*\*\*\*.xml.gzを全て出力する
            
              - ダウンロードアドレス：「ホスト」/weko/sitemaps/sitemapindex.xml

2\. サイトマップ生成の定期実行を可能

  - 設定した時刻にサイトマップ更新を定期実行する。  
    （更新するタイミングの設定については、以下の処理概要に記載）

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-sitemap

<!-- end list -->

  - > 処理概要

1\. 設定

  - Sitemap画面のテンプレートURLを設定する
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L13
    
      - 設定キー：WEKO\_SITEMAP\_ADMIN\_TEMPLATE  
        現在の設定値:

> WEKO\_SITEMAP\_ADMIN\_TEMPLATE = 'weko\_sitemap/sitemap.html'

  - データベースから取得するアイテムの上限レコード数を設定する
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L16 
    
    <!-- end list -->
    
      - 設定キー：WEKO\_SITEMAP\_TOTAL\_MAX\_URL\_COUNT  
        現在の設定値:

> WEKO\_SITEMAP\_TOTAL\_MAX\_URL\_COUNT = 10000000

  - キャッシュのタイムアウト時間を設定する
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L24 
    
      - 設定キー：WEKO\_SITEMAP\_CACHE\_TIMEOUT  
        現在の設定値:

> WEKO\_SITEMAP\_CACHE\_TIMEOUT = 60 \* 60 \* 24 \* 3
> 
> URLのプレフィックスを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L30

  - 設定キー：SITEMAP\_BLUEPRINT\_URL\_PREFIX  
    現在の設定値:

<!-- end list -->

  - SITEMAP\_BLUEPRINT\_URL\_PREFIX = '/weko/sitemaps'

> 「sitemapindex」URLのエンドポイントを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L32 

  - 設定キー：SITEMAP\_ENDPOINT\_URL  
    現在の設定値:

> SITEMAP\_ENDPOINT\_URL = '/sitemapindex.xml'
> 
> 各ページURLのエンドポイントを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L34 

  - 設定キー：SITEMAP\_ENDPOINT\_PAGE\_URL  
    現在の設定値:

> SITEMAP\_ENDPOINT\_PAGE\_URL = '/sitemap\_\<int:page\>.xml.gz'
> 
> Sitemapの上限URL数を設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/config.py\#L36

  - 設定キー：SITEMAP\_MAX\_URL\_COUNT  
    現在の設定値:

> SITEMAP\_MAX\_URL\_COUNT = 10000
> 
> 自動更新タイミングを設定する

  - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg\#L119

  - 設定キー：update\_sitemap

  - 設定値：days、minutes、hours  
    現在の設定値：

> 'update\_sitemap': {
> 
> 'task': 'weko\_sitemap.tasks.update\_sitemap',
> 
> 'schedule': timedelta(days=3, minutes=0, hours=0),
> 
> 'args': \[\],
> 
> },

2\. 実装方法

  - 【Administration \> Setting（設定） \> Sitemap】を以下のテンプレートで表示する
    
      - 設定キー：WEKO\_SITEMAP\_ADMIN\_TEMPLATE
    
      - パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko\_sitemap/templates/weko\_sitemap/sitemap.html

  - Sitemapを更新する処理
    
      - 【Administration \> （設定）Setting \> Sitemap】の順でサイトマップ画面へ遷移し\[実行（Run）」ボタンを押すと、weko\_sitemap.admin.update\_sitemapが呼び出され、sitemapの情報を以下のように取得する。
        
          - データベースからの値：pidstore\_pid.pid\_value、records\_metadata.updated
        
        <!-- end list -->
        
          - 条件：「pidstore\_pid.status = 'R' (registered)」AND「pidstore\_pid.pid\_type = 'recid'」
        
          - 上限レコード数：「WEKO\_SITEMAP\_TOTAL\_MAX\_URL\_COUNT」の値
        
          - 取得されたデータをファイルに分ける  
            1つのファイルに格納される上限URL数：「SITEMAP\_MAX\_URL\_COUNT」の値
    
      - 取得されたデータから、Sitemapの情報を以下のように作成する
        
          - アイテム詳細のURLは以下のように構築される

> {
> 
> loc: \<invenio\_records\_ui.recidのURL\> + pidstore\_pid.pid\_value,
> 
> lastmod: records\_metadata.updated
> 
> }

  - Sitemapの情報をキャッシュに保存する
    
      - sitemap\_\<page\>.xml.gz

> 'sitemap\_' + page\_number: {
> 
> lastmod: \<現在のシステム日時\>,
> 
> page: \<アイテム詳細のURL\>
> 
> }

  - sitemapindex.xml

> sitemap\_page\_keys: \[
> 
> 'sitemap\_' + page\_number,
> 
> ...
> 
> \]

  - Sitemap情報をキャッシュから自動的に削除される処理
    
      - キャッシュのタイムアウト時間を以下のコンフィグで設定する  
        設定キー：WEKO\_SITEMAP\_CACHE\_TIMEOUT
    
      - 「page\_number」及び「sitemap\_page\_keys」キャッシュに対してweko\_sitemap.ext.set\_cache\_pageでタイムアウト時間を指定している

<!-- end list -->

  - 「sitemapindex」URL及び各ページURLを構築する
    
      - 「sitemapindex」URL

> WEKO\_SITEMAP\_URL\_SCHEME + \<ホスト\> + SITEMAP\_BLUEPRINT\_URL\_PREFIX + SITEMAP\_ENDPOINT\_URL

  - 各ページURL

> WEKO\_SITEMAP\_URL\_SCHEME + \<ホスト\> + SITEMAP\_BLUEPRINT\_URL\_PREFIX + SITEMAP\_ENDPOINT\_PAGE\_URL

  - Sitemap情報をダウンロードする処理
    
      - sitemapindex.xmlweko\_sitemap.ext.get\_cache\_pageで 上記の「sitemap\_page\_keys」からのデータを取得し、weko\_sitemap.ext.sitemapで以下のように出力する。

> \[
> 
> {
> 
> loc: \<ファイルのURL\>,
> 
> lastmod: 'sitemap\_ + page\_number'.lastmod
> 
> },
> 
> ...
> 
> \]

  - sitemap\_\<page\>.xml.gz  
    weko\_sitemap.ext.pageでURLに入力しているページ番号に応じて、該当「page\_number」から取得するデータを出力、weko\_sitemap.ext.gzip\_responseでデータを「gz」ファイルに圧力する。

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
