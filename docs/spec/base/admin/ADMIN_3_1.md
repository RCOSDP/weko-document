# ツリー編集

<!-- end list -->

  - > <span id="_ツリー編集" class="anchor"></span>目的・用途

本機能は、インデックスツリーの追加、編集、削除を担当している機能である。  
インデックスツリー情報の公開設定、閲覧権限、投稿権限などを編集できる。

  - > 利用方法

1\. システム管理者、リポジトリ管理者でログインする。

2.【Administration\>インデックスツリー管理(Index Tree)\>ツリー編集(Edit Tree)】画面を開く。

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

> 1\. インデックスツリーを追加する  
> 【Administration \> インデックスツリー管理 \> ツリー編集（Edit Tree）】画面に移動する。  
> その後新しく作成するインデックスの親となるインデックスをRootIndex以下から選択する。  
> そして、Edit Treeエリア左上にある「追加」（Add）ボタンを押すことで、インデックスが新規登録される。

  - 「追加」（Add）ボタンを押す時に選択しているインデックスの最下行に、インデックス（New Index）を配置する。  
    「Root Index」を選択している場合、インデックス一覧の最下行に配置する。

> 2\. インデックスツリーを編集する  
> 【Administration \> インデックスツリー管理 \> ツリー編集（Edit Tree）】画面にて編集したいインデックスを押下することでそのインデックスの編集画面が右に表示される。  
> なお、Root Indexは選択することができるが、編集することはできない。
> 
> インポート中はインデックスツリーの編集ができない。

  - 入力内容は以下の通りである。
    
      - 「インデックス」（Index）
        
          - 日本語と英語のインデックス名用のテキストボックスを設ける。  
            日本語：サイトの表示言語が日本語の時に表示される。  
            英語：サイトの表示言語が日本語以外の時に表示される。
        
          - 英語のインデックス名は必須項目とする。
        
          - デフォルト値：「New Index」
    
      - 「コメント」（Comment）
        
          - インデックスのコメントを入力する。
        
          - URLを表示する場合、次の形式で入力する。  
            形式：

> \[\[URL|表示名\]\]
> 
> 上記のように入力すると、表示名をリンクで表示する。「|表示名」を省略した場合、URLをリンク形式で表示する。

  - 「公開」（Publish）
    
      - 「公開する」（Open to public）チェックボックスを設ける。
    
      - チェックを入れた場合
        
          - インデックスの公開日の入力欄を表示させる。
        
          - 「子インデックスの公開日にも再帰的に反映させる」（Set the publication date of child indexes recursively）チェックボックスを表示させる。  
            チェックを入れた場合、所属する子インデックスと子孫インデックスすべてに公開日の設定が再帰的に設定される。

  - 「インデックスリンク」（Index Link）
    
      - 「Enable」チェックボックスを設ける  
        チェックを入れた場合、インデックスリンク検索が有効になっている時インデックスリンク検索の際にプルダウンに表示される。
        
          - インデックスリンク検索を有効にするには[ADMIN-14-2 インデックスリンク表示](\\l)を参照すること
    
      - インデックスリンクの表示を決めるテキストボックスを「日本語」と「英語」の二つとして設ける。
    
      - なお、「英語」は必須項目となっていて、初期値は「New Index」とする。インデックスリンクの仕様については[USER-1-3インデックス検索](\\l)を参照すること。
    
      - 「表示範囲」（More Function）  
        「公開する」（Limit the number of child indexes to show.）チェックボックスを設ける。チェックを入れた場合、初回表示個数を設定できる。デフォルト値が「5」とする。
    
      - 選択しているインデックスに子インデックスを登録しない場合、このチェックボックスは非活性とする。

  - 「RSSアイコン」（RSS Icon）  
    「表示する」（Display）チェックボックスを設ける。
    
      - チェックを入れた場合、インデックスリストにRSSアイコンが表示される。
    
      - RSSの機能詳細は[USER-1-6 RSS](\\l)を参照すること。

  - 「PDF Cover Page (JA)」（PDF Cover Page）  
    「Enable」チェックボックスを設ける。  
    このチェックボックスは【Administration\>設定(Setting)\>PDFカバーページ表示】画面にて「PDF Cover Page」エリアで「Enable」を選んでいると編集が可能になる。設定の詳細は[ADMIN-14-4 PDFカバーページ表示](\\l)を参照すること。
    
      - チェックを入れる場合、PDFカバーページが作成される。
    
      - 編集が可能になっている場合、「Also reflect recursively on child index」チェックボックスが表示される。
        
          - チェックを入れて保存した場合、所属する子インデックスと子孫インデックスすべてにこのエリアのPDFカバーページの設定が再帰的に設定される。

  - 「ハーベスト公開」（Harvest Publish）  
    「公開する」（Open to public）チェックボックスを設ける
    
      - チェックを入れた場合、インデックスへのハーベスト要求に対して、所属するデータを提供できる。

  - 「ONLINE ISSN」（Online ISSN）  
    インデックスにオンラインISSNの値を入力する。  
    「このインデックス直下のアイテムの利用統計を集計する」（Aggregate usage statistics of items belonging to this index.)チェックボックスを設ける。
    
      - チェックを入れた場合、子インデックスへの再帰的な設定値反映および利用統計集計する。  
        \[注意！\]  
        ただし、WEKO3側で、ONLINE ISSN ごとに集計する機能は存在しない。  
        利用統計通常は、インデックス単位でとる仕様である。  
        将来的にONLINE ISSN ごとに集計するようになった場合に備えて移行をしておく。

  - 「閲覧権限」（Browsing Privilege）
    
      - ロール権限の設定には、  
        「ロール権限あり」（Role Authorized）と「権限なし」（Unauthorized）エリアを設ける。
        
          - 「ロール権限あり」（Role Authorized）は、デフォルトとして、以下の権限が表示される。
            
              - Contributor
            
              - Authenticated User
            
              - Guest
        
          - 「子インデックスのロール権限にも再帰的に反映させる」（Set the base authorities of child indexes recursively）チェックボックスにチェックを入れることで、所属するすべての子インデックスと子孫インデックスにロール権限の設定が再帰的に設定される。
    
      - グループ権限の設定には、  
        「グループ権限あり」（Group Authorized）と「権限なし」（Unauthorized）エリアを設ける。
        
          - 「グループ権限あり」（Group Authorized）は、デフォルトとして、登録されているグループが表示される。
        
          - 「子インデックスのグループ権限にも再帰的に反映させる」（Set the base authorities of child indexes recursively）チェックボックスにチェックを入れることで、所属する子インデックスと子孫インデックスすべてにグループの設定が再帰的に設定される。

  - 「投稿権限」（Deposit Privilege）
    
      - ロール権限の設定には、  
        「ロール権限あり」（Role Authorized）と「権限なし」（Unauthorized）エリアを設ける。
        
          - 「ロール権限あり」（Role Authorized）は、デフォルトとして、以下の権限が表示される。
            
              - System Administrator
            
              - Repository Administrator
            
              - Contributor
            
              - Community Administrator 
            
              - Authenticated User : -98
            
              - Guest : -99
        
          - 「子インデックスのロール権限にも再帰的に反映させる」（Set the base authorities of child indexes recursively）チェックボックスにチェックを入れることで、所属するすべての子インデックスと子孫インデックスにロール権限の設定が再帰的に設定される。
    
      - グループ権限の設定には、  
        「グループ権限あり」（Group Authorized）と「権限なし」（Unauthorized）エリアを設ける。
        
          - 「グループ権限あり」（Group Authorized）は、デフォルトとして、登録されているグループが表示される。
        
          - 「子インデックスのグループ権限にも再帰的に反映させる」（Set the base authorities of child indexes recursively）チェックボックスにチェックを入れることで、所属する子インデックスと子孫インデックスすべてにグループの設定が再帰的に設定される。

  - 「表示形式(検索結果)」（Display Format(Search Results)）  
    検索結果の表示形式を選択する。
    
      - 「一覧形式」（List）  
        検索結果をアイテムの一覧で表示する。デフォルトはこの形式で設定されている。  
        一覧形式の詳細は[USER-2-1 一覧形式表示](\\l)を参照すること。
    
      - 「目次形式」（Table Of Contents）  
        検索結果を見出しの一覧で表示する。  
        目次形式の詳細は[USER-2-2 目次形式表示](#目次形式表示)を参照すること。

  - インデックスサムネイル画像のアップロードエリア

<!-- end list -->

  - 「送信」（Send）ボタンを押すと、編集したインデックスが保存される。

  - 親インデックスにサムネイルが登録されている場合、子インデックス作成時にサムネイルは引き継がれない。

  - サムネイルの添付可能な形式は「gif, jpg, jpe, jpeg, png, bmp」のみ。  
    その他の形式を選択すると、「画像ファイル（gif, jpg, jpe, jpeg, png, bmp）以外のファイルはアップロードできません。」とエラーメッセージを表示する

  - サムネイルを登録後、「削除」ボタンを配置し、登録したサムネイルを削除できるようにする  
    ※「削除」ボタン押下時に、メッセージ等は表示しない。「送信」ボタンを押下することでサムネイルの削除が反映されるようにする。

  - サムネイル画像は表示時の画面サイズに応じて縮小される。画像を拡大表示することはしない。

<!-- end list -->

  - 必須項目を入力しない場合、インデックスが追加されずに、エラーメッセージがポップアップアラートで表示される。また、必須項目の直下にエラーメッセージも表示される。  
    ポップアップアラートで表示されるエラーメッセージ：「必須入力項目を入力してください」  
    該当項目下に表示されるエラーメッセージ：「英語で入力は必要です。」

  - エラーがない場合は「正常にインデックスを更新しました。(Index is updated successfully.)」というポップアップが表示される。

  - DOI(デジタルオブジェクト識別子)付与済アイテムがインデックスに存在した場合、インデックス状態の「公開」から「非公開」への変更を認めない。  
    日本語：DOIが付与されているアイテムからのリンクがあるため、インデックスを非公開にすることはできません。  
    英語：The index cannot be kept private because there are links from items that have a DOI.

  - DOI付与済アイテムがインデックスに存在した場合、ハーベスト状態の「公開」から「非公開」への変更を認めない。  
    日本語：DOIが付与されているアイテムからのリンクがあるため、インデックスのハーベストを非公開にすることはできません。  
    英語：Index harvests cannot be kept private because there are links from items that have a DOI.

3\. インデックスツリーを削除する

  - 削除したいインデックスを選択した状態で、「削除」（Delete）ボタンを押すと、確認ダイヤログを表示させる。  
    削除処理中はインデックス操作ができなくなる。(\[追加\]ボタン，\[削除\]ボタン，\[送信\]ボタンが非活性となる)  
    確認メッセージ：  
    日本語：「DELETEインデックス以下のインデックスおよびアイテムに対する処理を選択してください」  
    英語：「Please choose processing about index and items\!」
    
      - 「すべて削除」(Delete All)ボタンを押すと、インデックスを削除する。子インデックスおよびアイテムが、すべて削除される。
    
      - 「キャンセル」(Cancel)ボタンを押すと、確認ダイアログを閉じる。
    
      - 当該インデックスのみに所属するDOI付与済アイテムが存在した場合、インデックス自身の削除を認めない。  
        日本語：DOIが付与されているアイテムからのリンクがあるため、インデックスを削除することはできません。  
        英語：The index cannot be deleted because there is a link from an item that has a DOI.
    
      - 当該インデックス以外にもインデックス状態が「公開」かつハーベスト公開が「公開」のインデックスにリンクするDOI付与済アイテムが存在する場合、編集・削除の操作への制限はしない。
    
      - エラーがない場合は「正常にインデックスを削除しました。(Index is deleted successfully.)」というポップアップが表示される。その後、画面がリフレッシュされ、該当のインデックスは削除される。

  - ハーベスト設定で利用されているインデックスは削除できない。

  - アイテムインポート中はインデックスを削除できない。

4\. インデックスツリーを移動する。

  - > インデックスの順序の変更と所属する親インデックスの変更はドラッグ&ドロップにより可能である。  
    > なお、Root Indexを動かすことはできない。アイテムインポート中はインエックスを移動できない。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_index\_tree

  - > weko\_search\_ui

  - > weko\_admin

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - インデックスツリー編集画面表示について
    
      - 【Administration\>インデックスツリー管理\>ツリー編集】画面を開く。そのとき、weko\_index\_tree.admin.indexメソッドを呼び出し、indexテーブルよりインデックスツリー情報を取得し、表示する。

  - インデックス追加について
    
      - 【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集（Edit Tree）】画面にて追加ボタンを押下すると、weko\_index\_tree.rest.postメソッドにてweko\_index\_tree.api.createが呼び出される。  
        それによって初期値が以下の表であるインデックスを生成され、indexテーブルに登録される。

  - インデックスのキャッシュについて
    
      - インデックスのキャッシュはRedisサーバに以下キー名でインデックス保存時に作成される。
        
          - index\_tree\_view\_" + os.environ.get('INVENIO\_WEB\_HOST\_NAME') + "\_" + lang

<table>
<thead>
<tr class="header">
<th>インデックスツリー設定値</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#</td>
<td>項目(日本語)</td>
<td>DBキー</td>
<td>デフォルト値</td>
<td>備考</td>
</tr>
<tr class="even">
<td>1</td>
<td>なし</td>
<td>id</td>
<td>(現在の時間を元にしたもの)</td>
<td>time.timeメソッドに1000を掛けた値</td>
</tr>
<tr class="odd">
<td>2</td>
<td>なし</td>
<td>parent</td>
<td>(親インデックスのID)</td>
<td>rootindex下なら初期値0</td>
</tr>
<tr class="even">
<td>3</td>
<td>インデックス</td>
<td>index_name</td>
<td>New Index</td>
<td></td>
</tr>
<tr class="odd">
<td>4</td>
<td></td>
<td>index_name_english</td>
<td>New Index</td>
<td>必須事項</td>
</tr>
<tr class="even">
<td>5</td>
<td>コメント</td>
<td>comment</td>
<td>None</td>
<td></td>
</tr>
<tr class="odd">
<td>6</td>
<td>公開</td>
<td>public_state</td>
<td>false</td>
<td></td>
</tr>
<tr class="even">
<td>7</td>
<td></td>
<td>public_date</td>
<td>None</td>
<td>yyyy/MM/dd HH:mm:ssの形式</td>
</tr>
<tr class="odd">
<td>8</td>
<td></td>
<td>recursive_public_state</td>
<td>false</td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>インデックスリンク</td>
<td>index_link_enabled</td>
<td>false</td>
<td></td>
</tr>
<tr class="odd">
<td>10</td>
<td></td>
<td>index_link_name</td>
<td>None</td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td></td>
<td>index_link_name_english</td>
<td>New Index</td>
<td>必須事項</td>
</tr>
<tr class="odd">
<td>12</td>
<td>表示範囲</td>
<td>more_check</td>
<td>false</td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td></td>
<td>display_no</td>
<td>5</td>
<td>表示数</td>
</tr>
<tr class="odd">
<td>14</td>
<td>RSSアイコン</td>
<td>rss_status</td>
<td>false</td>
<td></td>
</tr>
<tr class="even">
<td>15</td>
<td>PDFCoverPage</td>
<td>coverpage_state</td>
<td>false</td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td></td>
<td>recursive_coverpage_state</td>
<td>None</td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>ハーベスト公開</td>
<td>harvest_public_state</td>
<td>true</td>
<td></td>
</tr>
<tr class="odd">
<td>18</td>
<td>ONLINE_ISSN</td>
<td>online_issn</td>
<td>None</td>
<td></td>
</tr>
<tr class="even">
<td>19</td>
<td></td>
<td>biblio_flag</td>
<td>None</td>
<td></td>
</tr>
<tr class="odd">
<td>20</td>
<td>閲覧権限</td>
<td>browsing_role</td>
<td>3,-98,-99</td>
<td>ロールID</td>
</tr>
<tr class="even">
<td>21</td>
<td></td>
<td>recursive_browsing_role</td>
<td>false</td>
<td></td>
</tr>
<tr class="odd">
<td>22</td>
<td></td>
<td>browsing_group</td>
<td>(現在存在するすべてのグループを許可)</td>
<td></td>
</tr>
<tr class="even">
<td>23</td>
<td></td>
<td>recursive_browsing_group</td>
<td>false</td>
<td></td>
</tr>
<tr class="odd">
<td>24</td>
<td>投稿権限</td>
<td>contribute_role</td>
<td>1,2,3,4,-98,-99</td>
<td></td>
</tr>
<tr class="even">
<td>25</td>
<td></td>
<td>recursive_contribute_role</td>
<td>false</td>
<td></td>
</tr>
<tr class="odd">
<td>26</td>
<td></td>
<td>contribute_group</td>
<td>(現在存在するすべてのグループを許可)</td>
<td></td>
</tr>
<tr class="even">
<td>27</td>
<td></td>
<td>recursive_contribute_group</td>
<td>false</td>
<td></td>
</tr>
<tr class="odd">
<td>28</td>
<td>表示形式</td>
<td>display_format</td>
<td>1(一覧形式を表す)</td>
<td><p>1:一覧形式</p>
<p>2:目次形式</p></td>
</tr>
<tr class="even">
<td>29</td>
<td>サムネイル</td>
<td>image_name</td>
<td>None</td>
<td>値に入るのはサムネイル画像のパスを表す文字列</td>
</tr>
</tbody>
</table>

  - インデックス編集について
    
      - 【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集（Edit Tree）】画面にてインデックスを編集後、「送信」ボタンを押下することでweko\_index\_tree.rest.putメソッドを呼び出し、同フォルダのapi.pyのupdateメソッドでテーブルを更新する。それによって編集した箇所が上記の表の対応するテーブルキーでindexテーブルの値を更新する。
    
      - なおweko\_index\_tree.api.updateメソッド実行時、表の\#8,16,21,23,25,27がtrueの場合、それに対応するメソッドが呼び出される。それによって対応する設定が編集されたインデックスの子以下で同じように適用され、indexテーブルを更新する。

  - インデックス削除について
    
      - 【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集（Edit Tree）】画面にてインデックスを選択後、「削除」ボタンを押し、ポップアップの選択肢「すべて削除」を押下する。この操作によってweko\_index\_tree.rest.deleteにて同フォルダのutil.pyのperform\_delete\_indexメソッドが呼び出される。このメソッドによってindexテーブルから該当インデックスとその子インデックスを論理削除する。

  - インデックス移動について
    
      - 【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集（Edit Tree）】画面にてインデックスをドラッグアンドドロップすることで親インデックスの変更、または表示する順番の変更ができる。その変更をした際に、weko\_index\_tree.rest.putメソッドにて同フォルダのapi.pyのmoveメソッドが呼び出される。このメソッドによってindexテーブルのキー「parent」、「position」の値を変更する。

  - キャッシュについて
    
      - インデックスを作成、編集、削除、移動した際に、weko\_index\_tree.utils.save\_index\_trees\_to\_redisメソッドを用いて、インデックスツリーの日英の親子関係をredisに保存している。

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
<p>2024/08/27</p>
</blockquote></td>
<td>f49b016c92ef98e0656947bf651ca1a2f3dbc286</td>
<td>v1.0.8</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
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
