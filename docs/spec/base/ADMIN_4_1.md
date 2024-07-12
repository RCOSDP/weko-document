
### ウィジェット

<!-- end list -->

  - > 目的・用途

本機能は、ページレイアウトで利用するウィジェットを作成・編集・削除する機能である。

  - > 利用方法

【Administration \> ウェブデザイン管理（Web Design） \> ウィジェット（Widget）画面】で各リポジトリにウィジェットを作成・編集・削除する

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

1\. 概要

  - ウィジェットは、WEKO3に表示する内容を多言語で設定できる

  - 画面上の操作によって、コーディングを行わなくてもウィジェットのHTMLおよびScriptの編集ができる機能である

2\. ウィジェット一覧を表示する

  - 【ウィジェット（Widget）画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - 作成（Create）
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 選択▼（With selected▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 編集（Edit）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
    
      - 詳細（Details）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

  - 【ウィジェット（Widget）画面】の一覧タブにウィジェット一覧を表示する
    
      - 表示項目は以下の通りである
        
          - チェックボックス
        
          - アクション（作成・編集・削除を表すアイコン）
        
          - 「ID」：ウィジェットID
        
          - 「Repository」：属するリポジトリ名
        
          - 「Widget Type」：ウィジェットタイプ
        
          - 「Label」：ウィジェット名
        
          - 「Enable」：ウィジェットの状態
    
      - ［フィルターを追加▼（Add Filter▼）］ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルターの入力エリアを追加する
        
          - フィルター名
            
              - 「ID」
            
              - > フィルター方式の選択肢：等しい、等しくない、より大きい、より小さい、空、一覧にある、一覧にない
            
              - > 入力された数字を使い、選択したフィルター方式で絞り込む
            
              - 「Repository」
            
              - > フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
            
              - > 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Widget Type」
            
              - > フィルター方式の選択肢：「Repository」と同じである
            
              - > 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Enable」
            
              - > フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
            
              - > 入力エリアではなく選択肢「はい」「いいえ」を使い、「はい」なら有効なウィジェット、「いいえ」ならそうでないウィジェットを絞り込む
        
          - 設定したフィルターは［適用（Apply）］ボタンを押下することで一覧に適用される
        
          - ［フィルターをリセット（Reset filter）］ボタンを押下すると、設定したフィルターがリセットされる
    
      - ［選択▼（With selected▼）］ボタンをクリックすると、以下の追加可能な機能（現在削除ボタンのみ）を表示する
        
          - レコードにチェックを入れない場合、「削除」（Delete）ボタンを押すと、エラーメッセージを表示する  
            メッセージ：  
            　日本語：「少なくとも１つのレコードを選択してください。」  
            　英語：「Please select at least one record.」
        
          - レコードにチェックを入れる場合、［削除（Delete）］ボタンを押すと、確認ダイアログを表示する  
            メッセージ：  
            　日本語：「選択したレコードを削除してもよろしいですか。」  
            　英語：「Are you sure you want to delete selected records?」
            
              - ［OK］ボタンを押すと、該当レコードを削除し、メッセージを画面上部に表示する  
                メッセージ：  
                　日本語：「レコード数＋レコードが正常に削除されました。」  
                　英語：「Record was successfully deleted.」
            
              - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
    
      - 検索テキストボックスでロールを検索する  
        プレースホルダー：「Search」
        
          - 任意テキストを入力し、キーボードでの「Enter」を押すと、Id、リポジトリ名、ウィジェットタイプでの検索を行う
        
          - テキストボックスの右端での［X］ボタンを押すと、検索条件がクリアーされる
    
      - ウィジェット行の目アイコンを押すと、該当ウィジェットの詳細情報を「詳細」（Details）タブに表示する
        
          - 「移動」（Filter）テキストボックスにテキストを入力すると、入力値が項目名またはその値に含まれている項目に絞り込んで表示する
    
      - ウィジェット行の鉛筆アイコンを押すと、該当ウィジェットを「編集」（Edit）タブに表示し、ウィジェットの情報が編集できる
        
          - 編集中はそのウィジェットがロックされる
            
              - 一覧タブで、他のユーザーにロックされたウィジェットの鉛筆アイコンを押した場合、ロック解除の確認ダイアログを表示する  
                メッセージ：  
                日本語：「このウイジェットのロックを解除してよろしいでしょうか。」  
                英語：「Do you wan to unlock this widget?」
                
                  - ［OK］ボタンを押すと、操作中のユーザーによって該当ウィジェットをロックして、「編集」（Edit）タブを表示する
                    
                      - もともとロックしていた方の画面は変化しない
                
                  - ［閉じる］ボタンを押すと、確認ダイアログを閉じる
                    
                      - そうした場合、空白の「編集」（Edit）タブが表示される
            
              - ロックしている側の画面で［Save］［キャンセル（Cancel）］ボタンを押した場合、ロックが解除されて他のユーザーからも保存できるようになる
                
                  - 「編集」（Edit）タブの表示中に、ログアウトや他の画面への遷移を行った場合には、ロックは解除されない
                
                  - 「編集」（Edit）タブの表示中にウェブブラウザのタブを閉じた場合には、ロックが解除されず、同一のユーザーで同じウィジェットの「編集」（Edit）タブを表示した場合でも、他のユーザーにロックされた場合と同様にロック解除の確認ダイアログを表示する
        
          - ［Save］ボタンを押すと、編集内容が保存される
            
              - widget\_items、widget\_multi\_lang\_dataテーブルが更新される
            
              - ウィジェットが他のユーザーにロックされていた場合は、保存されずに以下のエラーメッセージがポップアップで表示される  
                メッセージ：「Widget is locked by another user.」
            
              - ロックして「編集」（Edit）タブで操作しているウィジェットが他のユーザーによって削除された場合に、ロックしているユーザーが削除後に保存すると、削除されなかったかのように保存される
        
          - ［Delete］ボタンを押すと、確認ダイアログを表示する  
            メッセージ：「Are you sure to delete this widget Item?」
            
              - ［OK］ボタンを押すと、ロックを無視して該当ウィジェットを削除し、メッセージをポップアップで表示する  
                メッセージ：「Widget item has deleted successfully.」
                
                  - 他のタブに移動しない。削除した後に［Save］ボタンを押すと削除されなかったかのように保存される
            
              - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
            
              - 該当ウィジェットがページレイアウトで使用されていた場合は、削除せずにエラーメッセージをポップアップで表示する  
                メッセージ：「Cannot delete this widget because it's setting in Widget Design.」
        
          - ［Cancel］ボタンを押すと、一覧タブに戻る
    
      - 「詳細」（Details）タブと「編集」（Edit）タブとは互いに行き来できる
    
      - ウィジェット行のごみ箱アイコンを押すと、ロックを無視して該当ウィジェットを削除し、メッセージを画面上部に表示する  
        メッセージ：  
        　日本語：「レコード数＋レコードが正常に削除されました。」  
        　英語：「Record was successfully deleted.」
        
          - 該当ウィジェットがページレイアウトで使用されていた場合は、削除せずにエラーメッセージをポップアップで表示する  
            メッセージ：「Cannot delete this widget because it's setting in Widget Design.」

<!-- end list -->

  - 「一覧」（List）から「作成」（Create）タブを押すと、「作成」（Create）タブに移動し、ウィジェットを新規作成できる

  - **共通の入力項目**
    
      - 「Repository」：システムでのリポジトリを選択する
        
          - 必須項目とする
    
      - 「Type」：ウィジェット種別を設定する
        
          - 必須項目とする
        
          - ウィジェット種別は以下の通りである
            
              - Free description
            
              - Access counter
            
              - Notice
            
              - New arrivals
            
              - Main contents
            
              - Menu
            
              - Header
            
              - Footer
    
      - 「Language」：ウィジェットの設定言語を選択する
        
          - 必須項目とする
        
          - 選択肢：【Administration \> 設定（Setting） \> 言語表示（Language）画面】に表示されるものと同じ言語を使用する
        
          - 表示順序について、【言語表示（Language）画面】での「登録言語」の言語を一覧の上部に表示し、「対応言語」の言語一覧を次に表示する
    
      - 「Name」：ウィジェット名を設定する
        
          - 必須項目とする
    
      - 「Theme」：枠や枠線といったWidgetのスタイルテンプレートを指定する
    
      - 「Label Enable」：ラベルの表示制御を設定する
        
          - デフォルトはチェック有りとする
    
      - 「Label Color」ラベルの背景色を設定する
        
          - 「Label Enable」がチェックなしの場合は無効になる
    
      - 「Label Text Color」：ラベルの文字色を設定する
        
          - 「Label Enable」がチェックなしの場合は無効になる
    
      - 「Border Style」：Widgetの枠線のスタイルを選択する
    
      - 3つの種類：実線、点線、二重線
    
      - 「Border Color」：Widgetの枠線の色を指定する
    
      - 「Background Color」：Widgetの背景色を指定する
    
      - 「Enable」：ウィジェット内容の表示/非表示を設定する
        
          - デフォルトはチェック有りとする

  - **テーマ（Theme）について**  
    現在3つのテーマを以下のように対応している
    
      - Default  
        枠は角丸である。枠線あり。影あり
    
      - Simple  
        枠は四角である。左枠線のみ。影なし
    
      - Side Line  
        枠は四角である。枠線なし。影なし
    
      - テーマの表示は以下になる

<table>
<thead>
<tr class="header">
<th><strong>テーマ</strong></th>
<th><strong>イメージ</strong></th>
<th><strong>メモ</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Default</td>
<td><img src="media/media/image3.png" style="width:1.29167in;height:0.46875in" /></td>
<td>現在のデフォルト(メインのデザイン)<br />
角丸。枠線あり。影あり。</td>
</tr>
<tr class="even">
<td>Side Line</td>
<td><img src="media/media/image3.png" style="width:1.27083in;height:0.44792in" /></td>
<td>四角。左枠線のみ。影なし。</td>
</tr>
<tr class="odd">
<td>Simple</td>
<td><img src="media/media/image3.png" style="width:1.22917in;height:0.42708in" /></td>
<td>四角。枠線なし。影なし。</td>
</tr>
</tbody>
</table>

  - 各種ウィジェットでの入力項目
    
      - **Free description**
        
          - 概要  
            自由記述コンテンツを表示するウィジェットである
        
          - 機能  
            WYSIWYGエディタである
            
              - HTMLを直に編集可能
            
              - Scriptが編集可能
            
              - 画像にリンクを貼り付け可能／解除可能
            
              - 文字にリンクを貼り付け可能／解除可能
            
              - ヘッダをフォーマット可能
            
              - フォントを選択可能
            
              - サイズを変更可能
            
              - 文字を装飾可能
            
              - 配置を変更可能
            
              - 箇条書き可能
            
              - リンクのアンダーラインを解除可能
            
              - プレビュー可能
            
              - ファイルのアップロード可能（挿入リンクは相対パス）
    
      - **Access counter**
        
          - 概要  
            アクセスカウンタを表示するウィジェットである
        
          - 機能
            
              - 「Access counter initial value」：アクセスカウンタ値の初期値を指定する  
                デフォルト：0
            
              - 「Preceding message」：アクセスカウンタ値前のメッセージを設定する
            
              - 「Following message」：アクセスカウンタ値後のメッセージを設定する
            
              - 「Other message to display」：他のメッセージを設定する
            
              - 以下のイメージはアクセスカウンタのサンプルである

| **設定**                      | **表示**                      |
| --------------------------- | --------------------------- |
| ![](media/media/image4.png) | ![](media/media/image5.png) |

  - **Notice**
    
      - 概要  
        お知らせを一覧表示するウィジェットである
    
      - 機能  
        WYSIWYGエディタをである
        
          - 「自由記述」にお知らせ内容を設定可能とする  
            （「Free Description」部分のような機能がある）
        
          - お知らせ内容の全表示/部分表示を設定可能とする
            
              - 「Write More」チェックボックスにチェックを入れると、追加でお知らせの自由記述エリアを表示する
            
              - 「Read more」テキストボックス：続きを読むリンク名を指定する
            
              - 「Hide the rest」テキストボックス：続きを隠すリンク名を指定する

  - **New arrivals**
    
      - 概要
        
          - ウィジェット表示は、 公開日から指定された日数(新着日数)までのアイテム を公開日順(降順)に一覧表示する
            
              - 同一公開日の場合はタイトルの文字コードを第2の条件としてソートする
        
          - 一覧表示されたアイテムは、アクセスユーザが閲覧可能なものとする
        
          - 一覧表示されたアイテムは、アイテム詳細ページへのリンク表示とし、画面遷移可能とする
    
      - 機能
        
          - 「New date」テキストボックス：新着日数を設定する
            
              - 設定値は"Today,1,2,3,・・・30"の計31個のプルダウンとする
            
              - デフォルト値：5日
        
          - 「Display Results」テキストボックス：アイテム表示件数を設定する
            
              - 設定値は"5,10,20,50,100"の計5個のプルダウンとする
            
              - デフォルト値：5件
        
          - 「RSS feed」チェックボックス：RSS配信を設定する
            
              - デフォルト：チェックなし

  - **Main contents**
    
      - 概要
        
          - WEKO3のメイン画面は以下で構成されるものとする
            
              - ヘッダ部
            
              - メイン部(メニュータブ、アイテム検索、インデックスツリー、検索結果表示)
        
          - コンテンツ自体を編集できずに、コンテンツのラベル・テーマ・背景などしか編集できない

  - **Menu**
    
      - 概要  
        システムのページを表示するウィジェットである
    
      - 機能
        
          - 「Orientation」ラジオボタン：メニューの表示向きを設定する
            
              - 選択肢：「Horizontal」、「Vertical」
            
              - デフォルト：「Horizontal」
        
          - 「Background Color」：背景色を色の表から設定する
            
              - デフォルト色：白
        
        <!-- end list -->
        
          - 「Active Background Color」：アクティブ背景色を設定する
            
              - デフォルト色：白
        
          - 「Default Color」：テキスト色を設定する
            
              - デフォルト色：黒
        
          - 「Active Color」：アクティブテキスト色を設定する
            
              - デフォルト色：黒
        
          - 「Show/Hide Pages」エリア：メニューに表示するページを指定する
            
              - 設定対象は【ページレイアウト（Page Layout）画面】で作成したページ一覧とする
            
              - デフォルト：すべてページが「Show」エリアに表示する

  - **Header/Footer**
    
      - 概要  
        ヘッダ/フッタを表示するウィジェットである。  
        ヘッダエリアは固定のヘッダ行（言語切替，ログインボタン，サインアップボタンを表示するエリア）と、自由にカスタマイズできるエリアがある。
    
      - 機能
        
          - WYSIWYGエディタである（「Free Description」部分のような機能がある）
        
          - 固定のヘッダは既存のWidgetのHeader Widgetの中に含まれるものとする。位置はHeader Widgetの位置に従う
        
          - ヘッダWidgetで固定ヘッダの背景色・文字色は、「Fixed Header Background Color」と「Fixed Header Text Color」で設定できるものとする
        
          - 自由にカスタマイズできるエリアの背景色は、「Background Color」で設定できるものとする
        
          - 固定ヘッダの背景色・文字色のデフォルトカラーは背景は白、文字は灰色とする

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-gridlayout

<!-- end list -->

  - > 処理概要

1\. 設定

> 表示言語設定に対応するウィジェットラベルを設定しない場合、ウィジェットラベルのデフォルトを設定する

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L28>

  - 設定キー： 「WEKO\_GRIDLAYOUT\_DEFAULT\_WIDGET\_LABEL」

  - 現在の設定値：

> WEKO\_GRIDLAYOUT\_DEFAULT\_WIDGET\_LABEL = "No Title"
> 
> 表示言語設定に対応するウィジェットがない場合、ウィジェット言語のデフォルトを設定する

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L31>

  - 設定キー： 「WEKO\_GRIDLAYOUT\_DEFAULT\_LANGUAGE\_CODE」

  - 現在の設定値：

> WEKO\_GRIDLAYOUT\_DEFAULT\_LANGUAGE\_CODE = "en"
> 
> 「New Arrivals」ウィジェット種類での「Display Results」のデフォルト値を設定する

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L34>

  - 設定キー： 「WEKO\_GRIDLAYOUT\_DEFAULT\_DISPLAY\_RESULT」

  - 現在の設定値：

> WEKO\_GRIDLAYOUT\_DEFAULT\_DISPLAY\_RESULT = "5"
> 
> 「New Arrivals」ウィジェット種類での「New date」のデフォルト値を設定する

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L37>

  - 設定キー： 「WEKO\_GRIDLAYOUT\_DEFAULT\_NEW\_DATE」

  - 現在の設定値：

> WEKO\_GRIDLAYOUT\_DEFAULT\_NEW\_DATE = "5"
> 
> 開発に使用しているウィジェット名を設定する

  - パス：
    
      - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L40-L49>
    
      - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L80>

  - 設定キー：
    
      - 「WEKO\_GRIDLAYOUT\_ACCESS\_COUNTER\_TYPE」
    
      - 「WEKO\_GRIDLAYOUT\_NEW\_ARRIVALS\_TYPE」
    
      - 「WEKO\_GRIDLAYOUT\_NOTICE\_TYPE」
    
      - 「WEKO\_GRIDLAYOUT\_MAIN\_TYPE」
    
      - 「WEKO\_GRIDLAYOUT\_MENU\_WIDGET\_TYPE」

  - 現在の設定値：

> WEKO\_GRIDLAYOUT\_ACCESS\_COUNTER\_TYPE = "Access counter"
> 
> WEKO\_GRIDLAYOUT\_NEW\_ARRIVALS\_TYPE = "New arrivals"
> 
> WEKO\_GRIDLAYOUT\_NOTICE\_TYPE = "Notice"
> 
> WEKO\_GRIDLAYOUT\_MAIN\_TYPE = "Main contents"
> 
> WEKO\_GRIDLAYOUT\_MENU\_WIDGET\_TYPE = 'Menu'

  - ウィジェットの高さの自動計算・不自動計算を設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L89>
    
      - 設定キー： 「WEKO\_GRIDLAYOUT\_AUTO\_ADJUST\_THE\_HEIGHT」
    
      - 現在の設定値：

> WEKO\_GRIDLAYOUT\_AUTO\_ADJUST\_THE\_HEIGHT = True

  - サーバから返却するウィジェットのデータを圧縮するかどうかを設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L95>
    
      - 設定キー：「WEKO\_GRIDLAYOUT\_IS\_COMPRESS\_WIDGET」
    
      - 現在の設定値：

> WEKO\_GRIDLAYOUT\_IS\_COMPRESS\_WIDGET = True

  - サーバから返却するウィジェットのデータの圧縮レベルを設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L92>
    
      - 設定キー：「WEKO\_GRIDLAYOUT\_COMPRESS\_LEVEL」
    
      - 現在の設定値：

> WEKO\_GRIDLAYOUT\_COMPRESS\_LEVEL = 6

  - サーバから返却するウィジェットデータのキャッシュ名を設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L98-L102>
    
      - 設定キー：
        
          - 「WEKO\_GRIDLAYOUT\_WIDGET\_CACHE\_KEY」
        
          - 「WEKO\_GRIDLAYOUT\_WIDGET\_PAGE\_CACHE\_KEY」
    
      - 現在の設定値：

> WEKO\_GRIDLAYOUT\_WIDGET\_CACHE\_KEY = "widget\_cache"
> 
> WEKO\_GRIDLAYOUT\_WIDGET\_PAGE\_CACHE\_KEY = "widget\_page\_cache"

  - ウィジェットに関するファイルアップロードのBucketIDを設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L104>
    
      - 設定キー：「WEKO\_GRIDLAYOUT\_BUCKET\_UUID」
    
      - 現在の設定値：

> WEKO\_GRIDLAYOUT\_BUCKET\_UUID = "517f7d98-ab2c-4736-91ea-54ba34e7905d"

  - 静的なウィジェットファイルサイズの上限を設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L107>
    
      - 設定キー：「WEKO\_GRIDLAYOUT\_FILE\_MAX\_SIZE」
    
      - 現在の設定値：

> WEKO\_GRIDLAYOUT\_FILE\_MAX\_SIZE = 1024 \* 1024 \* 16 \# 16 MB

2\. ウィジェットの実装方法

  - 対応しているライブラリ：
    
      - Trumbowyg（<https://alex-d.github.io/Trumbowyg/>）
        
          - 本ライブラリはウィジェットでのWYSIWYGエディタ機能を対応している
    
      - Gridstack.js（<https://gridstackjs.com/>）
        
          - トップページにてウィジェットデザインのレンダーを対応している

  - トップページにて、表示ページに関する特別なウィジェット設定があるかどうかチェックする
    
      - ウィジェット設定がない場合　=\> デフォルトとし「Main Layout」の設定を読み出し、gridstackJSでレイアウトをレンダーする
    
      - ウィジェット設定がある場合　=\> 該当するページの設定を読み出し、gridstackJSでレイアウトをレンダーする

  - ウィジェットの高さの自動計算
    
      - 概要的にスクロールバー高さの単位をgridstackライブラリでの単位に変換するのを行う方法である
    
      - ウィジェットをレンダーした上で、対象ウィジェットにスクロールバーが表示されるかどうかチェックする
        
          - スクロールバーが表示されない場合　（スクロールバーの高さ = ウィジェットの高さ）  
            　　=\> 変換を行わずに、ウィジェットを表示する
        
          - スクロールバーが表示される場合　（スクロールバーの高さ \> ウィジェットの高さ）  
            　　=\> スクロールバー高さの単位をgridstackライブラリでの単位に変換する（ピクセル→セルの変換）
    
      - その後、gridstackでのリサイズメソッドでウィジェットの高さを計算された値で更新する

  - **導入しているTrumbowygプラグイン**
    
      - Base64（<https://alex-d.github.io/Trumbowyg/demos/#plugins-base64>）
    
      - Colors（<https://alex-d.github.io/Trumbowyg/demos/#plugins-colors>）
    
      - Font family（<https://alex-d.github.io/Trumbowyg/demos/#plugins-fontfamily>）
    
      - Font size（<https://alex-d.github.io/Trumbowyg/demos/#plugins-fontsize>）
    
      - Paste image（<https://alex-d.github.io/Trumbowyg/demos/#plugins-pasteimage>）
    
      - Resizimg（<https://alex-d.github.io/Trumbowyg/demos/#plugins-resizimg>）
    
      - Table（<https://alex-d.github.io/Trumbowyg/documentation/plugins/#plugin-table>）

3\. 各種タブの操作

  - 画面表示、フィルターの操作、ウィジェット削除でウィジェット一覧を表示するときは、weko\_gridlayout.admin.WidgetSettingView.index\_viewメソッドで表示のためのウィジェット一覧を作成する

  - 目アイコンをクリックして「詳細」（Details）タブを表示するときは、WidgetSettingViewのdetails\_viewメソッドでウィジェットの詳細情報を取得する

  - 鉛筆アイコンをクリックして「編集」（Edit）タブを表示するときは、WidgetSettingViewのedit\_viewメソッドでウィジェットの情報を取得する
    
      - WidgetItemServices.get\_locked\_widget\_infoメソッドで、該当ウィジェットがロックされているか確認する
    
      - ロックされていなかった場合、ウィジェットをロックする

> lock\_key = WEKO\_GRIDLAYOUT\_WIDGET\_ITEM\_LOCK\_KEY.format(widget\_id)
> 
> session\[lock\_key\] = locked\_value

  - locked\_valueは、str(datetime.utcnow().timestamp())で作成する

  - widget\_itemsテーブルの該当ウィジェットについてのレコードで、「locked」をtrueにして、「locked\_by\_user」にロックしたユーザのidを記録する

<!-- end list -->

  - 編集（Edit）タブの［Save］ボタンでウィジェットを保存するときは、weko\_gridlayout.views. save\_widget\_itemメソッドの中で、WidgetItemServices.save\_commandメソッドから\_\_edit\_widgetメソッドを呼び出して保存する
    
      - widget\_itemsテーブルの該当ウィジェットについてのレコードを更新する
        
          - 「widget\_id」：該当ウィジェットのもの
        
          - 「repository\_id」：「Repository」プルダウンで選択したリポジトリのid
        
          - 「widget\_type」：「Type」プルダウンで選択したウィジェットタイプ
        
          - 「setings」：「Background Color」、「Fixed Header Background Color」、「Fixed Header Text Color」の設定
        
          - 「is\_enabled」：「Enable」がチェックされていればtrue、そうでなければfalse
    
      - widget\_multi\_lang\_dataテーブルの該当ウィジェットについてのレコードはすべて論理削除して、多言語設定があれば新たに言語ごとのレコードを作成する
        
          - 「id」：自動採番
        
          - 「widget\_id」：該当ウィジェットのもの
        
          - 「lang\_code」：設定した言語の言語コード
        
          - 「label」：該当ウィジェットで、その言語で設定した「Name」の入力値
        
          - 「description\_data」：ウィジェットタイプと設定内容に応じて、以下のようになる
            
              - ウィジェットタイプに固有の設定項目がない場合：null
            
              - ウィジェットタイプに固有の設定項目があり、設定されていない場合：{}
            
              - ウィジェットタイプに固有の設定項目があり、設定されている場合：その内容

  - ウィジェットを削除するときは、どの操作で削除するかによって呼び出されるメソッドが異なる
    
      - 一覧（List）タブのごみ箱アイコンでウィジェットを削除する場合、WidgetSettingViewのdelete\_modelメソッドの中で、WidgetItemServices.delete\_by\_idメソッドによって削除する
    
      - 編集（Edit）タブの［Delete］ボタンでウィジェットを削除する場合、weko\_gridlayout.views.delete\_widget\_itemメソッドの中で、WidgetItemServices.delete\_by\_idメソッドによって削除する
    
      - WidgetItemServices.delete\_by\_idメソッドでは、該当ウィジェットがページレイアウトに使用されているかどうかのチェックをWidgetDesignServices.is\_used\_in\_widget\_designメソッドによって行う
        
          - 使用されていた場合は、削除せずにメッセージを返す
        
          - 使用されていなければ、widget\_itemsテーブルとwidget\_multi\_lang\_dataテーブルから該当ウィジェットのレコードを論理削除する

  - 作成（Create）タブを表示するときは、WidgetSettingViewのcreate\_viewメソッドで作成タブのテンプレートを呼び出す

  - 作成（Create）タブの［Save］ボタンでウィジェットを保存するときは、weko\_gridlayout.views. save\_widget\_itemメソッドの中でWidgetItemServices.save\_commandメソッドからcreateメソッドを呼び出して保存する
    
      - widget\_itemsテーブルに、該当ウィジェットについてのレコードを作成する
    
      - 多言語設定があれば、widget\_multi\_lang\_dataテーブルに該当ウィジェットについてのレコードを作成する
    
      - それぞれの設定内容は、編集時と同様

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
</tbody>
</table>