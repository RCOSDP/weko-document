
### [RSS](https://redmine.devops.rcos.nii.ac.jp/projects/weko-dev-doc/wiki/RSS)

  - > 目的・用途

本機能は、WEKO RSS配信新着情報を取得し、インデックス単位で購読が可能となる機能である。

  - > 利用方法

インデックス検索を行った際、検索結果のインデックスに対応するRSSアイコンを押下することで、WEKO RSS配信新着情報を取得し、該当アイテム一覧のRSSを出力できる。  
また、新着アイテムのウィジェットが設定されている画面にアクセスした際に、画面に表示されているRSSアイコンを押下することで、該当アイテム一覧のRSSを出力できる。

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

<!-- end list -->

  - インデックス検索をした際に表示されるトップページ画面［トップ（Top）］タブ内の［インデックスリスト(Index List）］エリアに、RSSアイコンを表示する設定としているインデックスが表示された時、当該インデックスの右側にRSSアイコンを表示する。
    
      - RSSアイコンの表示設定は【Administration \> インデックスツリー管理 \> ツリー編集（Edit Tree）画面】で行う。設定については[ADMIN-3-1: ツリー編集](#_ツリー編集)を参照。
        
          - RSSアイコンのデフォルト表示設定：非表示

新着アイテムのウィジェットが設定されており、RSS配信を行う設定である場合、［新着アイテムウィジェット］エリア内右上にRSSアイコンを表示する。

  - 新着アイテムのウィジェット、RSS配信の設定は【Administration \> ウェブデザイン管理 \> ウィジェット　画面】で行う。設定については[ADMIN-4-1: ウィジェット](#ウィジェット)を参照。
    
      - RSS配信のデフォルト設定：配信しない

RSSアイコンを押下すると、WEKO RSS配信情報を取得し、該当アイテム一覧のRSSを出力する。

  - RSSの文書は、ブラウザの別タブに表示する。

<!-- end list -->

  - RSS文書には、以下の情報を記載する。
    
      - タイトル（WEKO3）
    
      - RSS文書のリンク
    
      - （インデックスが指定されている場合）当該インデックスに設定されているコメント
        
          - 当該インデックスにコメントが設定されていない場合は、インデックスの名前
        
          - インデックスが指定されていない場合はサイト名（WEKO3）
    
      - RSSで配信するデータを取得した日時
    
      - 条件に合致するアイテムの登録データ
        
          - インデックス検索結果で表示されているRSSアイコンを押下した場合、対応するインデックスの配下に登録されているアイテムのデータを設定されている条件で取得し、表示する。
            
              - UIから登録アイテムのデータを取得する条件を変更することはできない。
            
              - デフォルト設定は、選択したインデックスの配下に存在するアイテム検索結果のうち、2週間前以降に登録されたアイテムデータを20件まで取得し、言語データは英語を取得することとする。
        
          - 新着アイテムウィジェットで表示されているRSSアイコンを押下した場合、【Administration \> ウェブデザイン管理 \> ウィジェット　画面】で設定した日数前の日時以降に登録されたアイテムのデータを、設定した表示件数まで取得し表示する。
        
          - アイテムの登録データとして表示するのは以下の項目とする。
            
              - 論文情報
            
              - アイテムタイトル
            
              - パーマリンク
            
              - rdfへのURL
            
              - 著者名
            
              - 出版社
            
              - 雑誌名
            
              - ISSN
            
              - 巻
            
              - 号
            
              - 開始ページ
            
              - 終了ページ
            
              - 発行年月日
            
              - 抄録
            
              - 発行年月日

  - 対応するインデックスの配下に登録されているアイテムの各項目は、対応する登録データがない場合は空タグとして表示する。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_index\_tree：RSS出力するデータを取得する

  - > weko\_records：検索結果をRSS形式にシリアライズする

  - > weko\_gridlayout：RSS形式のデータをXMLフォーマットでビルドする

  - > weko\_search\_ui：検索結果をUIに表示する

  - > weko\_schema\_ui：検索用のJPCOARスキーマのマッピングを行う

  - > weko\_items\_ui

  - > weko\_theme：ウィジェットのテンプレートを作成する

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - インデックス検索をした際に表示されるトップページ画面［トップ（Top）］タブ内の［インデックスリスト(Index List）］エリアに、RSSアイコンを表示する設定としているインデックスが表示された時、当該インデックス配下に登録されているアイテムの情報を配信するRSSアイコンを表示する。

  - 新着アイテムのウィジェットが設定されており、RSS配信を行う設定である場合、［新着アイテムウィジェット］エリア内右上に新着アイテムの情報を配信するRSSアイコンを表示する。

  - RSSアイコンを押下すると、それぞれ対応するapiリクエストを送信することで該当するアイテムの登録データを取得し、RSS文書として別タブに出力する。

  - > WEKO RSS配信新着情報取得APIについて
    
      - > ［インデックスリスト（Index List）］エリアに表示されるRSSアイコンの押下で呼び出すAPIと、［新着アイテムウィジェット］エリアに表示されるRSSアイコンの押下で呼び出すAPIは異なる。
    
      - > エンドポイント（URI）
        
          - > ［インデックスリスト（Index List）］エリアのRSS

> /api/rss.xml

  - > ［新着アイテムウィジェット］エリアのRSS

> /rss/records

  - > RSSのバージョンは1.0に対応することとする。

  - > リクエストパラメータ
    
      - > RSS配信を行う新着アイテム情報の取得に用いるパラメータを、表 1-6‑1に示す。

表 1-6‑1 WEKO RSS配信を行う新着アイテム情報取得に用いるパラメータ

<table>
<thead>
<tr class="header">
<th><blockquote>
<p>項番</p>
</blockquote></th>
<th><blockquote>
<p>パラメータ</p>
</blockquote></th>
<th><blockquote>
<p>内容</p>
</blockquote></th>
<th><blockquote>
<p>デフォルト値</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>index_id</p>
</blockquote></td>
<td><blockquote>
<p>選択したインデックスのインデックスID。複数指定不可。<br />
0以下の値が指定された場合は全インデックスを検索する。</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>page</p>
</blockquote></td>
<td><blockquote>
<p>取得する検索結果一覧のページ番号を指定する。１以下の値が指定された場合は１ページ目を表示する。検索結果一覧の最大ページを超える値が指定された場合は、最後の結果一覧を表示する。</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>count</p>
</blockquote></td>
<td><blockquote>
<p>表示する検索結果件数を指定する。100以上の値が指定された場合は100として処理する。設定されない場合、または0以下の値が指定された場合は、デフォルトで設定されている表示件数として処理する。</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>term</p>
</blockquote></td>
<td><blockquote>
<p>新着アイテムとして扱う日数を指定する。指定されない場合、または0以下の値が指定された場合は、デフォルトで指定されている日数として処理する。</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>lang</p>
</blockquote></td>
<td><blockquote>
<p>検索結果の言語を指定する。指定がない場合はデフォルト設定とする。GUIからのリンクの場合、ユーザーが画面表示している言語と一致させる。</p>
</blockquote></td>
<td><blockquote>
<p>en</p>
</blockquote></td>
</tr>
</tbody>
</table>

  - > ［インデックスリスト（Index List）］エリアでの RSS配信時にアイテム情報を取得するリクエストパラメータについて
    
      - > パラメータはindex\_id, page, count, term, langの5項目とする。
    
      - > 各パラメータのデフォルト値はweko\_index\_tree/config.pyで設定し、変更可能とする。  
        > パス：  
        > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-index-tree/weko_index_tree/config.py#L69-L82>
    
    <!-- end list -->
    
      - > 選択されたインデックスのインデックスIDをパラメータindex\_idに設定し、他のパラメータはデフォルト値を設定する。
    
      - > 表示件数の設定値の上限はweko\_index\_tree/config.pyで設定し、変更可能とする。
        
          - > 表示件数の設定値の上限の値は100とする。

> WEKO\_INDEX\_TREE\_RSS\_COUNT\_LIMIT = 100

  - > 指定されたインデックスの配下のインデックスもデータの取得対象に含める。

<!-- end list -->

  - > ［新着アイテムウィジェット］エリアでのRSS配信時にアイテム情報を取得するリクエストパラメータについて
    
      - > termの値は【Administration \> ウェブデザイン管理 \> ウィジェット　画面】の「New date」の値を使用する。
    
      - > countの値は新着ウィジェットの「Display Results」の値を使用する。

<!-- end list -->

  - 取得したアイテムデータをRSS文書に出力するための処理は、［インデックスリスト(Index List）］エリアのRSSアイコンを押下した場合も［新着アイテムウィジェット］エリアのRSSアイコンを押下した場合も共通であり、weko\_gridlayout/utils.pyのbuild\_rss\_xmlで行っている。

<!-- end list -->

  - > レスポンスフォーマット  
    > 【ソートキー】  
    > 　第1ソートキー： 公開日  
    > 　第2ソートキー： タイトル

  - > 新着アイテムのRSSの配信仕様は、別紙「新着アイテムのRSSの配信仕様.xlsx」を参照。RSS表示条件
    
      - > アイテムが直接紐づいているインデックスとその上位のインデックスについて、１つでも非公開の設定のものがある場合の挙動は表 1-6‑2の通りである。

表 1-6‑2 非公開のインデックスに紐づくアイテムのRSS表示

<table>
<thead>
<tr class="header">
<th>ユーザー</th>
<th>表示制御</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>未ログイン</td>
<td>URLにアクセスしてもアイテム情報を出力しない。</td>
</tr>
<tr class="even">
<td>アイテム登録者以外の一般ユーザー(General User)</td>
<td>URLにアクセスしてもアイテム情報を出力しない。</td>
</tr>
<tr class="odd">
<td>アイテム登録者(Contributor)</td>
<td>URLにアクセスした場合アイテム情報を出力する。</td>
</tr>
<tr class="even">
<td>管理者ユーザー<br />
(Community Administrator, Repository Administrator, System Administrator)</td>
<td>URLにアクセスした場合アイテム情報を出力する。</td>
</tr>
</tbody>
</table>

  - > 登録されているアイテムが非公開の場合、当該アイテム登録者もしくは管理者ユーザーがRSS出力操作を行った際にのみ、アイテム情報は出力される。

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
<p>2022/05/19</p>
</blockquote></td>
<td>fae7741b21184fd216806f01d6019a321f97edd5</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>v0.9.22対応</td>
</tr>
</tbody>
</table>