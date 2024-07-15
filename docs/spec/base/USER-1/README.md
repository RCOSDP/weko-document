### 簡易検索（全文検索・キーワード検索）

<!-- end list -->

#### 目的・用途

本機能は、ユーザーがアイテムを検索する際に用いる機能である。  
タイトルや著者名等の項目を指定せず、全ての項目を対象に検索を行うことで、目的のアイテムを見つけることができる。

#### 利用方法

メインコンテンツ」ウィジェットの［トップ（Top）］タブにある検索テキストボックスに文字列を入力し、入力エリア右隣の［検索（Search）］ボタンを押下することで、検索結果が表示される<span id="_Item_Registration：フィードバックメール機能" class="anchor"></span>。

#### 利用可能なロール

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

#### 機能内容

<!-- end list -->

  - 「メインコンテンツ」ウィジェットの「トップ」タブ画面の上部にアイテム検索エリアを設ける。

  - アイテム検索エリア
    
      - 検索テキストボックスを表示する。
    
      - 検索方式ラジオボタン（［全文（Full text）］と［キーワード（Keyword）］）を表示する。
        
          - ［全文（Full text）］ラジオボタンにチェックを入れる場合、  
            登録されたアイテムのメタデータと登録されたコンテンツの内容から検索される。
        
          - ［キーワード（Keyword）］ラジオボタンにチェックを入れる場合、  
            登録されたアイテムのメタデータから検索される。
        
          - デフォルトでは［全文（Full text）］ラジオボタンにチェックが入った状態である。
    
      - 検索テキストボックス右隣にある［検索（Search）］ボタンを押下することで、入力された文字列でアイテム検索を行う。
        
          - ［検索（Search）］ボタンを押下せず、テキストボックス内にカーソルキーがある状態でエンターキーを押下することでも検索できる。
        
          - > 検索文字列を入力しない場合、検索条件無しとする。（登録データの全件を対象とした検索となる。）
        
          - > 文字間に空白を入れることでAND検索を行うことができる。
        
          - > 以下の特殊な意味をもつ英字のみでは検索を行うことができない。  
            > a, an, and, are, as, at, be, but, by, for, if, in, into, is, it, no, not, of, on, or, such, that, the, their, then, there, these, they, this, to, was, will, with
        
          - > 以下の特殊文字は検索時に指定できる。  
            > 入力された特別文字は内部的にエスケープする。  
            > \+ - = && || \! ( ) { } \[ \] ^ " \~ \* ? : \\ /  
            > エスケープできない文字(「\<」「\>」)で検索を行った場合は、「’\<’,’\>’は検索に使用できません。」とエラーメッセージを表示する。
    
      - > \[検索（Search）\]ボタンの右にある［詳細検索（Advanced）］ボタンを押下することで、詳細検索エリアを表示する。詳細検索については[USER-1-2: 詳細検索](\\l)を参照。
    
      - 検索を行うと、検索結果がトップページ画面の検索結果エリアに表示される。

検索結果は【Administration \> 設定（Setting） \> 検索設定（Search）画面】での設定の通りに表示される。詳細については、[USER-2-1一覧形式表示](#一覧形式表示)を参照。

検索結果エリア

  - ［エクスポート（Export）］ボタンを表示する。  
    ボタンを押下すると、一括出力画面に遷移して、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](#アイテム一括出力)を参照。

  - アイテム表示の設定エリア  
    デフォルト値について、設定されている【Administration \> 設定（Setting） \> 検索設定（Search）画面】の検索結果表示設定エリアから取得する。
    
      - ［表示順］（Display Order）プルダウンリスト：検索結果の表示順を選択する。  
        選択肢は【Administration \> 設定（Setting） \> 検索設定（Search）画面】での「表示する」リストとする。
    
      - 順序プルダウン：昇順、降順を選択する。  
        選択肢は「asc, desc」とする。
    
      - ［表示数］（Display Number）プルダウンリスト選択肢は「20,50,75,100」とする。

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

#### 関連モジュール

##### weko\_search\_ui：検索結果をUIに表示する

config.WEKO_SEARCH_UI_JSTEMPLATE_LIST_RESULTS : アイテム一覧のテンプレート

##### weko\_records

utils.sort_meta_data_by_options: 

##### weko\_items\_ui

##### weko\_theme

<!-- end list -->

#### 処理概要

> メインコンテンツ」ウィジェットの、［トップ（Top）］タブ上部にアイテム検索エリアを表示する。

  - > アイテム検索エリアには検索文字列を入力するテキストボックス、［検索（Search）］ボタン、［詳細検索（Advanced）］ボタン、全文/キーワードの検索方式を切り替えるラジオボタンを表示する。

> メインコンテンツ」ウィジェットの［トップ（Top）］タブにある検索テキストボックスに文字列を入力し、入力エリア右隣の［検索（Search）］ボタンを押下することで、weko\_search\_ui.views.searchメソッドが呼び出され、検索の処理を実行する。検索文字列を入力しない場合、登録データの全件を対象とした検索を行う。

  - > ［検索（Search）］ボタンを押下せず、テキストボックス内にカーソルキーがある状態でエンターキーを押下することでも、同様に検索処理を実行する。

> 検索処理後、メインコンテンツ」ウィジェットの［トップ（Top）］タブに検索結果エリアを表示する。検索結果エリアの表示形式はdb内のSearchManagementテーブルの情報から作成される。

  - > 検索結果エリアにはエクスポートボタン、アイテムの表示順、表示数の現在の設定、検索結果のアイテム一覧、ページングナビゲーションを表示する。

  - > 最初に検索した際は、アイテム表示に関する設定のデフォルト値として、【Administration \> 設定（Setting） \> 検索設定（Search）画面】での［検索結果表示設定］エリアで設定された値を取得し、取得した値に従って表示する。

> ［エクスポート（Export）］ボタンを押下すると一括出力画面に遷移し、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](\\l)を参照。
> 
> アイテムタイトルのリンクをクリックすると、該当アイテムの詳細画面に遷移する。
> 
> アイテムの表示順、表示数のプルダウンを選択すると、検索結果エリアでのアイテムの表示を選択した表示順、表示数に変更する処理を行う。

#### 更新履歴

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
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>


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
### [インデックス検索](https://redmine.devops.rcos.nii.ac.jp/projects/weko-dev-doc/wiki/%E3%82%A4%E3%83%B3%E3%83%87%E3%83%83%E3%82%AF%E3%82%B9%E3%83%84%E3%83%AA%E3%83%BC%E6%A4%9C%E7%B4%A2)

  - > 目的・用途

本機能は、ユーザーが「インデックスツリー」エリアまたは、「インデックスリンク」エリアからインデックスを選択してアイテムを検索する際に用いる機能である。  
選択したインデックスに所属するアイテムを検索することができる。

  - > 利用方法

メインコンテンツ」ウィジェットの［トップ（Top）］タブにある［インデックスツリー］エリア、または「インデックスリンク」エリアを使用する。インデックス名を選択することで、選択したインデックスに所属するアイテムを検索する。

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

  - 設定されているインデックスツリーが存在し、インデックスリンク表示を有効に設定している時、トップページ画面の［インデックスツリー(Index Tree)］エリアの上部に［インデックスリンク(Index Link)］エリアを表示する。
    
      - ［インデックスリンク］エリアは［インデックスツリー］エリアと同じ表示幅で表示する。
    
      - 【Administration \> インデックスツリー管理 \> ツリー編集（Edit Tree）】画面にてインデックスツリーを追加することができる。詳細は[ADMIN-3-1 ツリー編集](\\l)を参照すること。
    
      - ［インデックスリンク］エリアの表示設定は【Administration \> 設定（Setting） \> インデックスリンク表示（Index Link）画面】で行う。設定については[ADMIN-14-2: インデックスリンク表示](#インデックスリンク表示)を参照。
        
          - デフォルト設定：無効

  - ［インデックスリンク］エリアには、インデックスリンク表示を有効に設定しているインデックスをプルダウンの選択肢として表示する。
    
      - インデックスごとのインデックスリンクの表示設定は【Administration \> インデックスツリー(Index Tree)管理 \> ツリー編集（Edit Tree）画面】で行う。設定については[ADMIN-3-1: ツリー編集](#ツリー編集)を参照すること。
        
          - デフォルト設定：すべての初期設定されるインデックスについて無効
        
          - 表示名の言語は「英語」「日本語」とする。
        
          - 表示画面で指定した言語の言語リソースが設定されていない場合は英語表示とする。
    
      - ユーザーの閲覧権限があるインデックスを「インデックスリンク」プルダウンに表示する。
    
      - 親インデックスに閲覧権限がなく、その親に連なる子インデックスに閲覧権限がある場合、子インデックスのインデックスリンクは表示されない。

  - 設定されているインデックスツリーが存在し、インデックスツリーを表示する設定にしている場合、トップページ画面［トップ（Top）］タブ内の［インデックスツリー（Index Tree）］エリアに、各インデックスへのリンクを表示する。
    
      - 【Administration \> インデックスツリー管理 \> ツリー編集（Edit Tree）】画面にてインデックスツリーを追加、編集、設定することができる。詳細は[ADMIN-3-1 ツリー編集](#_ツリー編集)を参照すること。
    
    <!-- end list -->
    
      - インデックスツリーの表示設定は【Administration \> 設定（Setting） \> 検索設定（Search）画面】の［インデックスツリー／ファセット表示設定］エリアでの設定に応じて表示される。設定については[ADMIN-14-11: 検索設定](#検索設定)を参照すること。
        
          - インデックスツリーのデフォルト表示設定：表示（Display）
    
    <!-- end list -->
    
      - インデックスが子インデックスを持つ場合、インデックスの左の図形▶をクリックすると、子インデックスへのリンクを当該インデックスの下に表示する。再度クリックすると子インデックスを非表示とする。
    
      - インデックスが子インデックスを持たない場合、インデックスの左の図形は▷とする。
    
      - ［インデックスツリー（Index Tree）］エリアの見出しのリンク［インデックスツリー］は、「Root Index」へのリンクとする。
    
      - > 閲覧権限を持たないユーザーに対しては、非公開インデックスは表示しないものとする。
    
      - 親インデックスに閲覧権限がなく、その親に連なる子インデックスに閲覧権限がある場合、親だけでなく子インデックスのインデックスリンクも表示されない。
    
      - ツリー編集画面にて「表示範囲」項目を設定している場合、設定された数を超える子インデックスは初回で表示されず、\[more...\]を押すことでそれらが表示されるようになる。詳細は[ADMIN-3-1 ツリー編集](#_ツリー編集)を参照すること

  - ［インデックスツリー（Index Tree）］エリアのリンク、または\[インデックスリンク\]エリアのプルダウンを押下すると、当該インデックスに所属する子インデックスとアイテムを検索できる。
    
      - トップページ画面［トップ］タブ内の［Index List］エリアに選択したインデックスに所属するインデックスのリストを、［アイテムリスト］エリアに選択したインデックスに所属するアイテムのリストを表示する。
    
      - > 閲覧権限を持たないユーザーに対しては、検索結果に非公開インデックスは表示しないものとする。

<!-- end list -->

  - > ［Index List］エリア
    
      - エリア内の上部にパンくずリストを表示する。  
        パンくずリストのリンクを押下すると、上位のインデックスへ遷移可能とする。  
        なお、「Root Index」の場合はパンくずリストを表示しない。
    
      - > 選択したインデックスに所属する子インデックスのリストを表示する。
        
          - 各インデックスをリンク形式で以下のテンプレートのように表示する。  
            リンクをクリックすると、当該インデックスを検索条件としたアイテム検索を実施する。

> テンプレート：
> 
> インデックス名 + 空白文字 + "\<" + インデックスID + "\>"

  - インデックスIDはリポジトリ管理者以上の権限のみに対して表示する。

<!-- end list -->

  - 各インデックスに所属しているアイテムの公開アイテム件数と非公開のアイテム及び、公開日が未来であるアイテムの合計件数をPrivateのアイテム件数として表示する。なお、ゲストユーザーの場合、非公開のアイテム件数は表示されず、表示可能なアイテムの件数を表示する。
    
      - 子インデックスがあれば、全ての子インデックスに所属しているアイテムの件数を取得する。
    
      - 非公開のインデックスであれば、そのインデックスに所属しているアイテムを非公開のアイテムとして数える。

  - インデックスの初期表示設定が「Root Index」のとき、または［インデックスツリー］エリアの見出しのリンク［インデックスツリー］を押下したとき、［インデックスリスト(Index List)］エリアに「Root Index」の子インデックスのリストが表示され、パンくずリストは表示しない。  
    ※コミュニティ画面の「Root Index」は［アイテムリスト(Item Lists)］エリアを表示する。

  - 「Root Index」以外の最下層でないインデックスを表示した際、［インデックスリスト(Index List)］エリアにはパンくずリストと下位のインデックスを表示する。
    
      - 該当インデックスにリンクするアイテムがある場合はアイテムリストにアイテムを表示する。
    
      - 該当インデックスにリンクするアイテムが無い場合はアイテムリストのエリアのみ表示する。

  - 「Root Index」以外の最下層のインデックスを表示した際、［インデックスリスト(Index List)］エリアにはパンくずリストを表示する。
    
      - 該当インデックスにリンクするアイテムがある場合はアイテムリストにアイテムを表示する。
    
      - 該当インデックスにリンクするアイテムが無い場合はアイテムリストのエリアのみ表示する。

  - 検索結果は、【Administration \> インデックスツリー管理 \> ツリー編集（Edit Tree）画面】の［表示形式(検索結果) ］（Display Format(Search Results)）の設定に応じて表示される。設定については[ADMIN-3-1: ツリー編集](#ツリー編集)を参照すること。
    
      - 「一覧形式」（List）
        
          - インデックスリスト
        
          - インデックス.サムネイル画像
        
          - インデックス雑誌情報  
            （【Administration \> インデックスツリー管理 \> 雑誌情報　画面】で該当インデックスの雑誌情報を出力する設定がされている場合のみ表示される。）
        
          - インデックスコメント
        
          - 表示しているインデックスの検索URL  
            インデックス雑誌情報を出力する設定がされている場合のみ表示される。
        
          - アイテムリスト（一覧形式）
    
      - 「目次形式」（Table Of Contents）
        
          - インデックスリスト
        
          - インデックスサムネイル画像
        
          - インデックスコメント
        
          - アイテムリスト（目次形式）

  - インデックス雑誌情報としては、雑誌情報を登録済みであり、【Administration \> インデックスツリー管理 \> 雑誌情報　画面】で「出力する」に設定されている場合のみ、以下の雑誌情報を初期表示する。雑誌情報の登録、設定については[ADMIN-3-2: 雑誌情報](#雑誌情報-1)を参照すること。
    
      - 雑誌名
    
      - 出版者
    
      - 言語
    
      - eISSN / eISBN
    
      - 表示しているインデックスの検索URL
    
      - その他の登録されている雑誌情報は、初期表示では［▷詳細］リンクを表示し、非表示とする。［▷詳細］リンクをクリックすると、情報が表示される。詳細は[USER-2-3 雑誌情報](#雑誌情報-1)を参照すること

  - インデックスサムネイル画像は、【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集（Edit Tree）画面】に設定されたサムネイル画像から取得し、表示する。

<!-- end list -->

  - インデックスコメントは、【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集（Edit Tree）画面】に設定された「コメント」（Comment）から取得し、表示する。［アイテムリスト］エリア
    
      - インデックスに所属するアイテムの検索結果を表示する。
    
      - アイテムリストの表示についての詳細は  
        一覧形式表示の際は[USER-2-1一覧形式表示](#一覧形式表示)を、目次形式表示の際は[USER-2-2 目次形式表示](#目次形式表示)を参照すること。デフォルトでは一覧形式表示で表示される。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_search\_ui：検索結果をUIに表示する

  - > weko\_index\_tree

  - > weko\_theme

  - 
<!-- end list -->

  - > 処理概要

<!-- end list -->

  - インデックスリンクを表示する設定にしている時に、トップページ画面にアクセスする。  
    この操作によって、weko\_theme.views.indexメソッドにてget\_weko\_contentsを呼び出し、更にget\_index\_link\_listを呼び出して、インデックスリンクの情報を取得し、プルダウンに表示する。
    
      - なお、インデックスリンクがONになっているか否かはget\_index\_link\_listメソッドで確認する。

  - インデックスツリーを表示する設定にしている場合、トップページ画面にアクセスする。  
    この操作によって、weko\_index\_tree.rest.getメソッドにてget\_browsing\_treeメソッドまたは、get\_more\_browsing\_treeメソッドで設定されたインデックスツリー情報をredisから取得し、「インデックスツリー」エリアを表示する。
    
      - なお、インデックスツリーの表示は以下のソースコードを元にしている。<https://github.com/RCOSDP/weko-angular/blob/master/app-tree-items-detail/src/app/tree-list2/tree-list2.component.html>
    
    <!-- end list -->
    
      - > ［インデックスツリー］エリアには、現在設定されているインデックスツリーのリンクを表示する。
    
      - > 閲覧権限のないインデックスはweko\_index\_tree.utils. reduce\_index\_by\_roleメソッドにてroleにアクセス権限がないインデックスを非表示とする。
    
    <!-- end list -->
    
      - インデックスが子インデックスを持つ場合、インデックスの左の図形▶をクリックすると、子インデックスへのリンクを当該インデックスの下に表示し、図形を▼に変化させる。再度図形▼をクリックすると子インデックスを非表示とする。

> メインコンテンツ」ウィジェットの［トップ（Top）］タブ内に表示される、［インデックスツリー］エリア内のインデックスのリンクを押下する、または、\[インデックスリンク\]エリアのプルダウンからインデックスを選択する。この操作によって以下の処理をする。

  - > weko\_search\_ui.static.js.weko\_search\_ui.app getPathNameメソッドを呼び出す。そして、get\_path\_name\_dictメソッドによってindexテーブルより選択したインデックスのパンくずリストを取得する。なお、権限がないインデックスはfilter\_index\_list\_by\_roleメソッドで非表示になる。

  - > 検索結果の表示設定が一覧形式の時、選択したインデックスに登録されている公開設定の雑誌情報をweko\_search\_ui.views.searchメソッドにてget\_journal\_infoを使って取得し、表示する。処理の詳細についてはUSER-2-3雑誌情報を参照すること

  - > weko\_search\_ui.static.js.weko\_search\_ui.app.getChildListメソッドを呼び出す。そして、get\_child\_listメソッドによってindexテーブルより選択したインデックスに所属する子インデックスのデータを取得し、表示する。

  - > weko\_search\_ui.static.js.weko\_search\_ui.app.dispaly\_comment\_journalメソッドにて、format\_commentを呼び出し、コメントを整形し表示する。

  - > weko\_search\_ui.rest.IndexSearchResource.getメソッドにて、searchインスタンスで処理を行い、インデックスに所属するアイテムの情報を取得する。

  - > invenio\_records\_rest.serializers.response.search\_responsifyメソッドを呼び出し、アイテムリストにて表示する情報(リンク、メタデータ表示設定など)を取得する。

> ［アイテムリスト］エリア
> 
> 取得してある該当インデックスに所属するアイテム情報を表示する。

  - > アイテムリストについての処理概要は一覧形式表示の際はUSER-2-1一覧形式表示を、目次形式表示の際はUSER-2-2 目次形式表示を参照してください。デフォルトでは一覧形式表示で表示されます。

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
<p>2022/05/10</p>
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

### ファセット検索

  - > 目的・用途

本機能は、ユーザーがアクセス制限やデータタイプなどの検索条件を選択して、アイテムを絞り込む際に用いる機能である。  
複数の項目を選択して絞り込むことで、目的のアイテムに効率よく辿り着くことができる。

  - > 利用方法

トップページ画面の［Top］タブにあるインデックスツリーエリアの下にあるファセット検索エリアを利用する。  
ファセット検索の項目名をクリックまたは対応するチェックボックスをオンにした際に、当該項目で検索を行う。

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

  - ファセット検索を表示する設定にしている場合、トップページ画面［トップ（Top）］タブ内のインデックスツリー（Index Tree）エリアの下に、ファセット検索エリアを表示する。
    
      - ファセット検索の表示設定は【Administration \> 設定（Setting） \> 検索設定（Search）画面】の［インデックスツリー／ファセット表示設定］エリアでの設定に応じて表示される。設定については[ADMIN-14-11: 検索設定](#検索設定)を参照。
        
          - ファセット検索のデフォルト表示設定：非表示

ファセット検索機能の対象はアイテム一覧画面のみとする。

ファセット検索の対象とする項目は【Administration \> 設定（Setting） \> ファセット検索　画面】で設定する。設定については[ADMIN-14-12: ファセット検索](#ファセット検索-1)を参照。

  - メインコンテンツ」ウィジェットの［トップ（Top）］タブに表示されるファセット検索エリアの表示順はファセット項目の登録順(ID順)とする。

  - デフォルト設定で表示されるのは以下の検索項目とする。
    
      - データの言語(Data Language)
    
      - アクセス制限(Access)
    
      - 地域(Location)
    
      - 時間的範囲(Temporal)
    
      - トピック(Topic)
    
      - 配布者(Distributor)
    
      - データタイプ(Data Type)

ファセット検索の対象項目のマッピングに対応するデータを持つ登録アイテムがある場合、各項目のプルダウンに選択肢と、各選択肢に該当する登録アイテム数を表示する。ただし、表示される登録アイテムの数は、ユーザーのロールの閲覧範囲内の登録アイテム数をカウントしたものとなる。

  - ファセット検索の対象項目のマッピングに対応するデータを持つ登録アイテムがない場合、検索対象項目のエリアは表示し、プルダウンの選択肢には「No options」と表示する。

ファセット検索の項目のプルダウンを選択した際に、当該項目で検索を行う。  
選択を解除した際にも同様に検索を行う。

  - ファセット検索を単独で行った場合の検索結果は検索結果エリアに表示する。

  - 簡易検索や詳細検索の検索結果をファセット検索により絞り込むことを可能とする。検索情報はAND条件として検索を実行し、検索結果エリアに結果を表示する。
    
      - 簡易・詳細検索→ファセット検索：AND条件とした検索が実行される。
    
      - ファセット検索→簡易・詳細検索：ファセット検索の条件は反映されない。

  - > インデックス検索とファセット検索を組み合わせてアイテム検索を行うことを可能とする。検索情報はAND条件として検索を実行し、アイテムリストエリアに検索結果を表示する。アイテムリストエリアでの検索結果の表示については、[USER-1-3: インデックスリンク検索](#_インデックスリンク検索)を参照。
    
      - インデックス検索→ファセット検索：AND条件とした検索が実行される。
    
      - ファセット検索→インデックス検索：ファセット検索の条件は反映されない。

<!-- end list -->

  - トップページ画面［トップ］タブ内の検索結果エリアに、選択した項目に当てはまるデータを持つアイテムのリストを表示する。

  - 検索結果エリア
    
      - アイテムの検索結果は【Administration \> 設定（Setting） \> 検索設定（Search）画面】の［検索結果表示設定］の通りに表示される。設定については[ADMIN-14-11: 検索設定](\\l)を参照。
    
      - ［エクスポート（Export）］ボタンを表示する。  
        ボタンを押下すると、一括出力画面に遷移して、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](#アイテム一括出力)を参照。
    
      - アイテム表示の設定エリア  
        デフォルト値について、設定されている【Administration \> 設定（Setting） \> 検索設定（Search）画面】の検索結果表示設定エリアから取得する。
        
          - ［表示順］（Display Order）プルダウンリスト：検索結果の表示順を選択する。  
            選択肢は【Administration \> 設定（Setting） \> 検索設定（Search）画面】での「表示する」リストとする。
        
          - 順序プルダウン：昇順、降順を選択する。  
            選択肢は「asc, desc」とする。
        
          - アイテムタイトルがリンク形式で表示される。  
            リンクをクリックすると、該当アイテム詳細画面に遷移する。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_records\_rest：ファセット検索を実施する

  - > weko\_search\_ui：検索結果をUIに表示する

  - > weko-react/app-facet-search：weko\_searchのjsファイルを生成する

  - > weko\_schema\_ui：検索用のJPCOARスキーマのマッピングを行う

  - > weko\_items\_ui

  - > weko\_theme

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - ファセット検索を表示する設定にしている場合、メインコンテンツ」ウィジェットの［トップ（Top）］タブにアクセスすると、インデックスツリーエリアの下に、現在設定されている項目のファセット検索エリアを表示する。

> １つのファセット項目の中に表示される件数はconfigファイルで設定される。初期値は以下の通り。
> 
> weko/blob/develop/modules/weko-admin/weko\_admin/config.py  
> WEKO\_ADMIN\_FACET\_SEARCH\_SETTING\_BUCKET\_SIZE = 1000
> 
> JPCOARの索引定義（/weko-schema-ui/weko\_schema\_ui/mappings/v6/weko/item-v1.0.0.json）にファセット検索用の項目をマッピングする。

ファセット検索の対象項目のマッピングに対応するデータを持つ登録アイテムが存在する場合、当該ファセット項目のプルダウンに選択肢と、各選択肢に該当する登録アイテム数を表示する。

  - 現在のファセット検索の対象を「get\_facet\_search\_list」メソッドで取得する。  
    パス： <https://github.com/RCOSDP/weko-react/blob/5a0f077939ebd520294e16ec241c26f78bff5338/app-facet-search/src/App.js#L43>

> 各ファセット項目エリア内のプルダウンに表示されている選択肢を押下することで、選択した内容を検索条件として以下の検索処理を実行する。

  - > 「invenio-records-rest」モジュールの「/api/records」APIを呼び出す。

  - > 上記のAPIでは、「RECORDS\_REST\_FACETS\[SEARCH\_UI\_SEARCH\_INDEX\]」コンフィグを元にマッピング情報を取得し、条件を満たすアイテムを検索する。

> 各ファセット項目の選択を解除した際にも同様に検索処理を行う。
> 
> 選択肢を押下した後、メインコンテンツ」ウィジェットの［トップ（Top）］タブに検索結果を表示する。

  - ファセット検索を単独で行った場合の検索結果は検索結果エリアに表示する。

  - 簡易検索や詳細検索の検索結果をファセット検索により絞り込むことを可能とする。検索情報はAND条件として検索を実行し、検索結果エリアに結果を表示する。
    
      - 簡易・詳細検索→ファセット検索：AND条件とした検索が実行される。
    
      - ファセット検索→簡易・詳細検索：ファセット検索の条件は反映されない。

  - インデックス検索とファセット検索を組み合わせてアイテム検索を行うことを可能とする。検索情報はAND条件として検索を実行し、アイテムリストエリアに検索結果を表示する。
    
      - > インデックス検索→ファセット検索：AND条件とした検索が実行される。
    
      - ファセット検索→インデックス検索：ファセット検索の条件は反映されない。アイテムリストエリアでの検索結果の表示については、[USER-1-3: インデックスリンク検索](#_インデックスリンク検索)を参照。

  - > 検索結果エリアには、選択した項目に当てはまるデータを持つアイテムのリストを表示する。
    
      - > 検索結果エリアにはエクスポートボタン、検索結果のアイテム一覧、アイテム表示の設定エリア、ページングナビゲーションを表示する。
        
          - > アイテム表示の設定エリアにはアイテムの表示順の現在の設定を表示する。
        
          - > 最初に検索した際は、アイテム表示に関する設定のデフォルト値として、【Administration \> 設定（Setting） \> 検索設定（Search）画面】での［検索結果表示設定］エリアで設定された値を取得し、取得した値に従って表示する。

> ［エクスポート（Export）］ボタンを押下すると一括出力画面に遷移し、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](\\l)を参照。
> 
> アイテムタイトルのリンクをクリックすると、該当アイテムの詳細画面に遷移する。
> 
> アイテムの表示順のプルダウンを選択すると、検索結果エリアでのアイテムの表示を選択した表示順に変更する処理を行う。

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
<p>2022/05/12</p>
</blockquote></td>
<td>5401f42b6db01103bd1ad4a948025dda1dadb6ed</td>
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