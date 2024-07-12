

### [詳細検索](https://redmine.devops.rcos.nii.ac.jp/projects/weko-dev-doc/wiki/%E8%A9%B3%E7%B4%B0%E6%A4%9C%E7%B4%A2)

  - > 目的・用途

本機能は、ユーザーがアイテムを検索する際に用いる機能である。  
タイトルや著者名等の項目を指定し、複数の項目を掛け合わせて検索を行うことで、目的のアイテムを見つけることができる。

  - > 利用方法

トップページ画面の\[Top\]タブにあるキーワード検索テキストボックスの右側にある\[詳細検索（Advanced）\]ボタンを押下する。  
詳細検索条件入力エリアが表示されるので、条件を入力し、詳細検索エリアの最下部にある\[検索(Search)\]ボタンを押下することで、検索結果が表示される。

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

  - トップページ画面［トップ（Top）］タブの上部に設けたアイテム検索エリア内に、詳細検索条件を入力できるボタン（\[詳細検索(Advanced)\]ボタン）を設ける。

  - \[検索（Sesrch）\]ボタンの右にある\[詳細検索(Advanced)\]ボタンを押下すると、詳細検索エリアを展開表示する。
    
      - 詳細検索エリアを展開表示すると、本ボタンは［閉じる（Close）］ボタンに置換される。［閉じる（Close）］ボタンを押下することで、詳細検索エリアを非表示とする。詳細検索エリアを非表示にすると、本ボタンは\[詳細検索(Advanced)\]ボタンに置換される。

  - 簡易検索のテキストフィールドと詳細検索の各項目とのAND検索を行うことが可能とする。
    
      - 詳細検索では、検索方式ラジオボタン（［全文（Full text）］と［キーワード（Keyword）］）は簡易検索と同じものを使用する。  
        各検索方式は簡単検索と同じ仕様とする。

  - テキストボックスに入力して検索を行う場合、文字間に空白を入れることでAND検索を行うことができる。

  - 以下の特殊な意味をもつ英字のみでは検索を行うことができない。  
    a, an, and, are, as, at, be, but, by, for, if, in, into, is, it, no, not, of, on, or, such, that, the, their, then, there, these, they, this, to, was, will, with

  - 以下の特殊文字は検索時に指定できる。  
    入力された特別文字は内部的にエスケープする。  
    \+ - = && || \! ( ) { } \[ \] ^ " \~ \* ? : \\ /  
    エスケープできない文字(「\<」「\>」)で検索を行った場合は、「’\<’,’\>’は検索に使用できません。」とエラーメッセージを表示する。

  - 日付入力において、妥当ではない日付が入力された場合は「Field does not validate」とエラーメッセージを表示する。

検索項目は【Administration \> 設定（Setting） \> 検索設定（Search）画面】の詳細検索条件設定エリアの通りに表示される。設定については[ADMIN-14-11: 検索設定](#検索設定)を参照。

  - 詳細検索条件設定エリアの［初期選択（Initial Condition）］カラムにチェックが入っている項目は、初期状態で詳細検索エリアに表示される。

  - 各詳細検索条件の項目は、詳細検索条件設定エリアで表示されている順番で表示される。

  - ［使用項目（Useable Item）］カラムにチェックが入っている項目は初期状態では表示せず、検索条件項目のプルダウンで選択できるものとする。

  - ［アイテムタイプ（Item Type）］の検索条件項目については、現在システムに登録されているアイテムタイプを取得し、表示する。

  - 既に選択されている検索条件項目は、検索条件項目プルダウンで非活性（選択できない状態）とする。

各検索条件について、入力方式に応じて以下のいずれかの適当な入力エリアを設ける。

  - テキストボックス

  - チェックボックス

  - プルダウン

  - 範囲入力（\[テキスト\] To\[テキスト\]）

  - 日付範囲入力（範囲入力＋カレンダー入力）

  - geo\_distance

表 1-2‑1　初期登録を行った環境で詳細検索エリアに初期表示される項目

<table>
<thead>
<tr class="header">
<th><strong>No.</strong></th>
<th><strong>検索項目</strong></th>
<th><strong>入力エリア</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>タイトル<br />
(Title)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>2</td>
<td>著者名<br />
(Author Name)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>3</td>
<td>件名<br />
(Subject)</td>
<td>テキストボックス、チェックボックス</td>
</tr>
<tr class="even">
<td>4</td>
<td>地域<br />
(Region)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>5</td>
<td>内容記述<br />
(Description)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>6</td>
<td>出版者<br />
(Publisher)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>7</td>
<td>寄与者<br />
(Contributor)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>8</td>
<td>コンテンツ作成日<br />
(Contents Created Date)</td>
<td>日付範囲入力、チェックボックス</td>
</tr>
<tr class="odd">
<td>9</td>
<td>フォーマット<br />
(Format)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>10</td>
<td>ID</td>
<td>テキストボックス、チェックボックス</td>
</tr>
<tr class="odd">
<td>11</td>
<td>雑誌名<br />
(Journal Title)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>12</td>
<td>資源タイプ<br />
(Resource Type)</td>
<td>チェックボックス</td>
</tr>
<tr class="odd">
<td>13</td>
<td>アイテムタイプ<br />
(Item Type)</td>
<td>チェックボックス</td>
</tr>
<tr class="even">
<td>14</td>
<td>言語<br />
(Language)</td>
<td>チェックボックス</td>
</tr>
<tr class="odd">
<td>15</td>
<td>期間<br />
(Period)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>16</td>
<td>学位取得日<br />
(Academic Degree Date)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>17</td>
<td>著者版フラグ<br />
(Author Version Flag)</td>
<td>プルダウン</td>
</tr>
<tr class="even">
<td>18</td>
<td>学位番号<br />
(Academic Degree Number)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>19</td>
<td>学位名<br />
(Degree Name)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>20</td>
<td>学位授与機関<br />
(Institution For Academic Degree)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>21</td>
<td>著者ID<br />
(Author ID)</td>
<td>テキストボックス</td>
</tr>
<tr class="even">
<td>22</td>
<td>Index</td>
<td>チェックボックス</td>
</tr>
<tr class="odd">
<td>23</td>
<td>License</td>
<td>チェックボックス</td>
</tr>
<tr class="even">
<td>24</td>
<td>テキスト1<br />
(text1)</td>
<td>テキストボックス</td>
</tr>
<tr class="odd">
<td>25</td>
<td>float_JA_1</td>
<td>数値範囲入力</td>
</tr>
<tr class="even">
<td>26</td>
<td>geopoint_JA_1</td>
<td>geo_distance</td>
</tr>
</tbody>
</table>

検索項目ごとにある「X」ボタンを押すことで、検索条件を削除できる。

検索条件の表示の下に［検索条件追加（Add Search Condition）］ボタンを設ける。

  - ［検索条件追加（Add Search Condition）］ボタンを押下すると、検索条件エリアを追加する。

  - 選択されていない項目をデフォルト値とする。

  - 入力欄が検索可能な項目の件数と同数になった場合、このボタンは非活性とする。

［クリア（Clear）］ボタンを押下すると、入力された検索条件を取消する。

日付を入力する検索項目について、テキストボックスを押下するとカレンダーのボタンが表示され、日付を選択することで、検索条件を入力できるものとする。

  - 入力テキストフィールドでの入力とGUIでの入力の両方を可能とする。

  - GUIを使用した場合は「YYYYMMDD」を指定できる。

  - テキストフィールドから入力した場合は「YYYYMMDD」「YYYYMM」「YYYY」を指定できる。

  - 上記以外の入力値を指定した場合は「Field does not validate」を表示し、アイテム検索はできない。

［検索（Search）］ボタンを押すことで、検索条件でアイテムの検索を実施し、検索結果がトップページ画面の検索結果エリアに表示される。

  - JPCOARスキーマのマッピングでアイテム検索する。

  - 検索方式：AND

  - テキストボックス内にカーソルキーがある状態でエンターキーを押下することでも検索できる。

<!-- end list -->

  - 検索結果は【Administration \> 設定（Setting） \> 検索設定（Search）画面】での設定の通りに表示される。詳細については、[USER-2-1一覧形式表示](#一覧形式表示)を参照。

<!-- end list -->

  - 検索結果エリア
    
      - ［エクスポート（Export）］ボタンを表示する。  
        ボタンを押下すると、一括出力画面に遷移して、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](#アイテム一括出力)を参照。
    
      - アイテム表示の設定エリア  
        デフォルト値について、設定されている【Administration \> 設定（Setting） \> 検索設定（Search）画面】の検索結果表示設定エリアから取得する。
        
          - ［表示順］（Display Order）プルダウンリスト：検索結果の表示順を選択する。  
            選択肢は【Administration \> 設定（Setting） \> 検索設定（Search）画面】での「表示する」リストとする。
        
          - 順序プルダウン：昇順、降順を選択する。  
            選択肢は「asc, desc」とする。
        
          - ［表示数］（Display Number）プルダウンリスト  
            選択肢は「20,50,75,100」とする。
    
      - アイテム一覧表示
        
          - アイテムタイトルがリンク形式で表示される。  
            リンクをクリックすると、該当アイテム詳細画面に遷移する。
        
          - 表示されるアイテムはロールによって異なる。  
            システム管理者、リポジトリ管理者、コミュニティ管理者の場合はすべて表示される。  
            ただし、制限公開されているアイテムについては、公開日までシステム管理者と登録者のみ閲覧可能となる。  
            登録ユーザー、一般ユーザー、ゲストの場合はpublicなインデックスツリー内のpublicなアイテムのみ表示される。  
            ただし、登録ユーザーに関しては自身で登録したアイテムのみPrivateであっても検索対象となる。
    
      - ページング機能を設ける。
        
          - ページングナビゲーションを操作することで、表示内容が切り替わる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_search\_ui：検索結果をUIに表示する

  - > weko\_schema\_ui

  - > weko\_items\_ui

  - > weko\_theme

<!-- end list -->

  - > 処理概要

> メインコンテンツ」ウィジェットの［トップ（Top）］タブ上部にアイテム検索エリアを表示する。

  - > アイテム検索エリアには検索文字列を入力するテキストボックス、［検索（Search）］ボタン、［詳細検索（Advanced）］ボタン、全文(Full Text)/キーワード(Keyword)の検索方式を切り替えるラジオボタンを表示する。

> ［詳細検索(Advanced)］ボタンを押下すると、詳細検索エリアを展開表示する。

  - 詳細検索エリアで初期表示される検索項目は【Administration \> 設定（Setting） \> 検索設定（Search）画面】の詳細検索条件設定エリアで［初期選択（Initial Condition）］カラムにチェックが入っている項目である。

  - 詳細検索エリアが表示されている状態の時、［詳細検索(Advanced)］ボタンは［閉じる(Close)］ボタンに置換される。［閉じる(Close)］ボタンを押下することで、詳細検索エリアを非表示とする。詳細検索エリアを非表示にすると、再度［詳細検索(Advanced)］ボタンに置換される。

> 既に選択されている検索条件項目は、プルダウンで非活性（選択できない状態）とする。
> 
> 検索項目ごとにある「X」ボタンを押すことで、検索条件を削除できる。
> 
> 検索条件の表示の下にある［検索条件追加（Add Search Condition）］ボタンを押下すると、選択されていない項目の検索条件エリアを追加する。

  - 選択されていない検索項目がない場合、このボタンは非活性とする。

> 詳細検索条件を指定して、入力エリア右隣の［検索(Search)］ボタンを押下することで、weko\_search\_ui.views.searchメソッドが呼び出され、検索の処理を実行する。検索文字列を入力しない場合、登録データの全件を対象とした検索を行う。

  - > ［検索］ボタンを押下せず、テキストボックス内にカーソルキーがある状態でエンターキーを押下することでも検索処理を実行する。

<!-- end list -->

  - > 検索項目の選択肢は、weko\_search\_ui.config.py WEKO\_SEARCH\_KEYWORDS\_DICTで設定している。

  - > 検索項目と対応するキーを表 1-2‑2に示す。
    
      - > weko\_schema\_ui.mappings.v6.weko.item-v1.0.0.jsonにてElasticsearchでの文字解析方法を設定している。
    
      - > FullText: 全文検索

表 1-2‑2　検索項目と対応するキー

<table>
<thead>
<tr class="header">
<th><strong>No.</strong></th>
<th><strong>検索項目</strong></th>
<th><strong>検索方式</strong></th>
<th><strong>検索用のキー</strong></th>
<th><strong>備考</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>タイトル<br />
(Title)</td>
<td>FullText</td>
<td><p>search_title,</p>
<p>search_title.ja</p></td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>著者名<br />
(Author Name)</td>
<td>FullText</td>
<td>search_creator, search_creator.ja</td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>件名<br />
(Subject)</td>
<td>Keyword</td>
<td>subject.subjectScheme</td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>地域<br />
(Region)</td>
<td>Keyword</td>
<td>geoLocation.geoLocationPlace</td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>内容記述<br />
(Description)</td>
<td>FullText</td>
<td>search_des, search_des.ja</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>出版者<br />
(Publisher)</td>
<td>FullText</td>
<td>search_publisher. search_publisher.ja</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>寄与者<br />
(Contributor)</td>
<td>FullText</td>
<td>search_contributor, search_contributor.ja</td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>コンテンツ作成日<br />
(Contents Created Date)</td>
<td>Keyword</td>
<td>date.dateType, file.date.dateType</td>
<td>date.dateTypeが'file.date.dateType'キーで検索される</td>
</tr>
<tr class="odd">
<td>9</td>
<td>フォーマット<br />
(Format)</td>
<td>Keyword</td>
<td>file.mimeType</td>
<td></td>
</tr>
<tr class="even">
<td>10</td>
<td>ID</td>
<td>FullText</td>
<td></td>
<td>※表 1-2‑3参照<br />
追加検索用のキーはKeyword方式</td>
</tr>
<tr class="odd">
<td>11</td>
<td>雑誌名<br />
(Journal Title)</td>
<td>FullText</td>
<td>sourceTitle, sourceTitle.ja</td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>資源タイプ<br />
(ResourceType)</td>
<td></td>
<td>type.raw</td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>アイテムタイプ<br />
(ItemType)</td>
<td>FullText</td>
<td>itemtype</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>言語<br />
(Language)</td>
<td>Keyword</td>
<td>language</td>
<td></td>
</tr>
<tr class="odd">
<td>15</td>
<td>期間<br />
(Period)</td>
<td>Keyword</td>
<td>temporal</td>
<td></td>
</tr>
<tr class="even">
<td>16</td>
<td>学位取得日<br />
(Academic Degree Date)</td>
<td></td>
<td>dateGranted</td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td>著者版フラグ<br />
(Author Version Flag)</td>
<td>FullText</td>
<td>versionType</td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td>学位番号<br />
(Academic Degree Number)</td>
<td>FullText</td>
<td>dissertationNumber</td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td>学位名<br />
(Degree Name)</td>
<td>FullText</td>
<td>degreeName, degreeName.ja</td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td>学位授与機関<br />
(Institution For Academic Degree)</td>
<td>FullText</td>
<td>degreeGrantor. degreeGrantorName, dgName, dgName.ja</td>
<td><p>degreeGrantorNameが' dgName, dgName.ja 'キーで検索される</p>
<p>degreeGrantorNameはキーワード方式</p></td>
</tr>
<tr class="odd">
<td>21</td>
<td>著者ID<br />
(Author ID)</td>
<td>Keyword</td>
<td>creator.nameIdentifier</td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td>Index</td>
<td>FullText</td>
<td>path.tree</td>
<td>入力したIndex IDに所属するアイテムを検索<br />
※入力したIndex ID下にある子インデックスに所属するアイテムの検索まではしない</td>
</tr>
<tr class="odd">
<td>23</td>
<td>License</td>
<td></td>
<td>content.licensetype.raw</td>
<td>ファイル情報プロパティのライセンス情報を検索<br />
※権利情報プロパティ(dc:rights)の検索は実施しない</td>
</tr>
<tr class="even">
<td>24</td>
<td>テキスト1<br />
(text1)</td>
<td>Keyword</td>
<td>Text1</td>
<td></td>
</tr>
<tr class="odd">
<td>24</td>
<td>float_JA_1</td>
<td>float_range</td>
<td>float_range1</td>
<td></td>
</tr>
<tr class="even">
<td>25</td>
<td>geopoint_JA_1</td>
<td>geo_point</td>
<td>geo_point1</td>
<td></td>
</tr>
</tbody>
</table>

表 1-2‑3　 IDの選択肢と対応するキー

| **No.** | **選択肢**     | **検索用のキー**                 | **追加検索用のキー**           |
| ------- | ----------- | -------------------------- | ---------------------- |
| 1       | identifier  | relation.relatedIdentifier | identifierType=\*      |
| 2       | URI         | identifier                 | identifierType=\*      |
| 3       | fullTextURL | file.URI                   | objectType=\*          |
| 4       | selfDOI     | identifierRegistration     | identifierType=\*      |
| 5       | ISBN        | relation.relatedIdentifier | identifierType=ISBN    |
| 6       | ISSN        | sourceIdentifier           | identifierType=ISSN    |
| 7       | NCID        | relation.relatedIdentifier | identifierType=NCID    |
| 8       | NCID        | sourceIdentifier           | identifierType=NCID    |
| 9       | pmid        | relation.relatedIdentifier | identifierType=PMID    |
| 10      | doi         | relation.relatedIdentifier | identifierType=DOI     |
| 11      | NAID        | relation.relatedIdentifier | identifierType=NAID    |
| 12      | ichushi     | relation.relatedIdentifier | identifierType=ICHUSHI |

> 検索処理後、「メインコンテンツ」ウィジェットの［トップ（Top）］タブに検索結果エリアを表示する。

  - > ［検索結果］エリアにはエクスポートボタン、アイテムの表示順、表示数の現在の設定、検索結果のアイテム一覧、ページングナビゲーションを表示する。

  - > 最初に検索した際は、アイテム表示に関する設定のデフォルト値として、【Administration \> 設定（Setting） \> 検索設定（Search）画面】での検索結果表示設定エリアで設定された値を取得し、取得した値に従って表示する。

> ［エクスポート（Export）］ボタンを押下すると一括出力画面に遷移し、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](\\l)を参照。
> 
> アイテムタイトルのリンクをクリックすると、該当アイテムの詳細画面に遷移する。
> 
> アイテムの表示順、表示数のプルダウンを選択すると、検索結果エリアでのアイテムの表示を選択した表示順、表示数に変更する処理を行う。

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
<p>2022/04/28</p>
</blockquote></td>
<td>57247ecce9b5e0879a2538687e446e0ea310129c</td>
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
