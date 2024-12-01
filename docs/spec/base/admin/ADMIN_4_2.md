
### ページレイアウト

  - > 目的・用途

システムにて、各ページに作成されたウィジェットをデザインする機能である

  - > 利用方法

【Administration \> ウェブデザイン管理（Web Design） \> ページレイアウト（Page Layout）画面】：ページを管理（追加・編集・削除）し、 各リポジトリでのページごとにウィジェット位置を設定する

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

1\. リポジトリ毎にページ定義ができる

  - 【ページレイアウト（Page Layout）画面】に以下の表示項目を設ける
    
      - 「Repository」プルダウンリスト
        
          - 選択肢：システムに登録しているリポジトリ一覧である
    
      - 「Page」プルダウンリスト
        
          - 選択肢：選択しているリポジトリに属するページ一覧である
    
      - 「Widget List」エリア
        
          - 選択しているリポジトリに属するウィジェットが表示されるエリアである
    
      - 「Preview」エリア
        
          - 選択しているページにウィジェットを設定するエリアである

  - Pages領域にて、ページの追加・編集・削除ボタンを設ける
    
      - 「Main Layout」はデフォルトページとし、削除不可とする
        
          - デフォルトページは、リポジトリごとに存在する
        
          - 初期状態ではデータベース上に存在しないが、後述のページ編集ダイアログで保存することでwidget\_design\_pageテーブルにレコードが追加される
        
          - デフォルトページのみ、widget\_design\_pageテーブルでis\_main\_layoutフィールドがtrueである
    
      - 「+」ボタンを押すと、ページ追加のダイアログを表示する
        
          - 設定内容：
            
              - 「URL」：ページのURL
                
                  - 必須入力とする
                
                  - 入力欄には、初期値として「/」が入っている
                
                  - リポジトリごとにURLがユニークとなる
            
              - 「Title」  
                デフォルト値：「Page Title」
            
              - 言語プルダウンリスト
                
                  - 選択肢：【Administration \> 設定（Setting） \> 言語表示（Language）画面】に表示する言語を使用する
                
                  - 表示順序について、【言語表示（Language）画面】での「登録言語」の言語を一覧の上部に表示し、「対応言語」の言語一覧を次に表示する
        
          - ［Save］ボタンを押すと、入力内容をチェックする
            
              - チェックに問題がなければ、ページを追加して、メッセージを画面上部に表示する  
                メッセージ：「Successfully saved page.」
            
              - チェックに問題がある場合、エラーメッセージをモーダルダイアログの上部に表示する
                
                  - 「Repository」プルダウンリストで、初期状態の「Please select the Repository」を選択した状態である場合  
                    　エラーメッセージ：「Please select the repository.」
                
                  - 設定済みのURLを指定する場合  
                    　エラーメッセージ：「Unable to save page: URL already exists.」
                
                  - 入力値に「/」が含まれない場合  
                    　エラーメッセージ：「Not a valid URL.」
        
          - 「Close」ボタンを押すと、ページを追加せずにモーダルダイアログを閉じる
    
      - 鉛筆ボタンを押すと、ページ編集のダイアログを表示する
        
          - ページの情報を編集した後、［Save］ボタンを押すことで、ページの情報を更新できる
        
          - ［Close］ボタンを押すと、編集内容を反映せずにダイアログを閉じる
    
      - ゴミ箱ボタンを押すと、削除確認用のダイアログを表示する  
        確認内容：「Are you sure you want to delete the page?」  
        ※「Main Layout」ページは削除不可のため、ゴミ箱のアイコンを非表示とする
        
          - 「Submit」ボタンを押すと、該当ページを削除し、メッセージを表示する  
            メッセージ：「Successfully deleted page.」
        
          - 「Close」ボタンを押すと、モーダルダイアログを閉じる
    
      - 歯車ボタンを押すと、【ウィジェット（Widget）画面】を別ウィンドウで表示する
        
          - 【ウィジェット（Widget）画面】の詳細は[ADMIN-4-1: ウィジェット](\\l)を参照
        
          - 編集中のウィジェットはロックされる
            
              - ［Save］［Cancel］ボタンではなく［×］ボタンによって別ウィンドウを閉じた場合はロックが解除されず、再度表示した場合には、他のユーザーにロックされた場合と同様にロック解除の確認ダイアログを表示する
        
          - 【ウィジェット（Widget）画面】を別ウィンドウで表示している状態で、新たに同画面の別ウィンドウを表示する場合は、表示中の別ウィンドウで新たな【ウィジェット（Widget）画面】に遷移する
            
              - 別ウィンドウでは、ブラウザの操作によって遷移前に戻ることはできない
        
          - 【ウィジェット（Widget）画面】中で［Save］または［Cancel］ボタンを押すと、別ウィンドウは閉じる
        
          - 【ウィジェット（Widget）画面】中で［Delete］ボタンを押した場合は、別ウィンドウは閉じない
        
          - 「Widget List」「Preview」どちらからでも【ウィジェット（Widget）画面】を表示できる

  - ウィジェットデザインに以下の項目を表示する
    
      - 「Widget List」エリア：【Administration \> ウェブデザイン管理（Web Design） \> ウィジェット（Widget）画面】にて有効なウィジェットを表示する
        
          - 各ウィジェットに［Add Widget］ボタンを設ける。
        
          - > ボタンを押すと、該当ウィジェットが「Preview」エリアに追加される
    
      - 「Preview」エリア：ウィジェットの位置を整理する
        
          - ドラッグアンドドロップすることで、ウィジェットの位置を移動できる
        
          - ウィジェットの幅を変更できる
        
          - ウィジェットの高さを画面描画時は自動調整する
        
          - 各ウィジェットに［X］ボタンを設ける
        
          - > ボタンを押すと、「Preview」エリアからウィジェットを削除する
    
      - 注意事項
        
          - 「Main Contents」、「Header」、「Footer」はページ内に複数設定不可とする
        
          - 「Preview」エリアに追加された「Main Contents」、「Header」、「Footer」のウィジェットがある場合に、同じ種類のウィジェットの「Add Widget」ボタンを不活性化する
        
          - 「Main Contents」ウィジェットは、一つリポジトリに１つだけ設定できる
    
      - ［Save］ボタンを押すと、設定した内容をチェックする
        
          - 「Repository」プルダウンリストで、初期状態の「Please select the Repository」が選択されているときは、［Save］［Cancel］ボタンは非活性である
        
          - チェックに問題がなければ、設定内容を保存して、メッセージを画面上部に表示する  
            メッセージ：「Widget design has been saved successfully.」
        
          - チェックに問題がある場合、エラーメッセージを表示する
            
              - ［Main Contents］のウィジェットを複数ページに設定する場合  
                エラーメッセージ：「Failed to save design: Main contents may only be set to one layout.」
            
              - ページにウィジェットをひとつも配置していない場合  
                エラーメッセージ：「Please add Widget to Preview panel.」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-gridlayout

  - > 関連ライブラリ：Gridstack.js 0.2.7-dev（https://gridstackjs.com/）

<!-- end list -->

  - > 処理概要

> 画面表示時は、weko\_gridlayout.admin.WidgetDesign.indexメソッドにより、以下のコンフィグで定められたテンプレートを用いる。

  - > パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L20>

  - > 設定キー：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py#L20>

> 「Repository」プルダウンの選択を変更したとき、以下のメソッドが呼び出される。

  - > weko\_gridlayout.views. load\_widget\_list\_design\_settingメソッドの中で、widget\_itemsから選択したリポジトリに属するウィジェット群を、widget\_multi\_lang\_dataテーブルからそれらのウィジェットの多言語設定を、widget\_design\_settingテーブルから選択したリポジトリのデフォルトページに配置されたウィジェットの情報を取得する。

  - > weko\_gridlayout.views. load\_widget\_design\_pagesメソッドで、widget\_design\_pageテーブルから選択したリポジトリに属するページ群を取得する。

> 「Pages」プルダウンの選択を変更したとき、変更先によって異なるメソッドが呼び出される。

  - > デフォルトページに変更した場合は、o weko\_gridlayout.views.load\_widget\_design\_settingメソッドの中で、widget\_design\_settingテーブルからデフォルトページに配置されたウィジェットの情報を取得する。

  - > デフォルトページ以外に変更した場合は、weko\_gridlayout.views.load\_widget\_design\_page\_settingメソッドの中で、widget\_design\_pageテーブルからページに配置されたウィジェットの情報を取得する。

> 鉛筆アイコンを押してページ編集のダイアログを出すとき、weko\_gridlayout.views.load\_widget\_design\_pageメソッドが呼び出される。

  - > その中で呼ばれるweko\_gridlayout.services.WidgetDesignPageServices.get\_pageメソッドで、widget\_design\_pageテーブルから情報を取得する。
    
      - > 画面に表示しているのがデフォルトページで、テーブルに情報がなかった場合、デフォルトページの内容を以下の内容で作成して返す。
        
          - > 「title」：「Main Layout」
        
          - > 「url」：「/community=リポジトリ名」
        
          - > 「is\_main\_layout」：true

> ページ追加のダイアログで［Save］ボタンを押すと、widget.design.jsのvalidateInputメソッドによって入力内容のチェックを行う。

  - > URLの入力値は、以下のようにチェックする。

> if (\!/\\/\[a-z0-9?&/=\]\*/.test(this.state.url)) {
> 
> this.setState({'errorMessage': 'Not a valid URL.'});
> 
> return false;
> 
> }

  - > チェックを通過すると、weko\_gridlayout.views.save\_widget\_design\_pageメソッドが呼び出される。

  - > weko\_gridlayout.views.save\_widget\_design\_pageメソッドの中で、widget\_design\_pageテーブルでレコード作成または更新を行う。
    
      - > widget\_design\_pageテーブルの操作はweko\_gridlayout.models.WidgetDesignPage.create\_or\_updateメソッドで行う。
        
          - > 以下の内容で保存する。
            
              - > 「id」：作成時に自動採番
            
              - > 「title」：「Title」の入力値
            
              - > 「repository\_id」選択中のリポジトリのid
            
              - > 「is\_main\_layout」：ページ作成時はfalseを設定、そうでなければもともとの値
        
          - > このメソッド中で、多言語設定をwidget\_design\_page\_multi\_lang\_dataテーブルに保存する。

> ウィジェットデザインエリアは、Gridstack.js 0.2.7-devによって実装している。
> 
> ページ本体で［Save］ボタンを押すと、widget.design.jsのsaveWidgetDesignSettingメソッドでエラーチェックを行う。

  - > 以下のパスの部分でウィジェット配置情報を取得して、空だった場合はエラーメッセージ「Please add Widget to Preview panel.」を表示する。
    
      - > パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/static/js/weko_gridlayout/widget.design.js#L1027-L1054>

  - > エラーがなければ、weko\_gridlayout.views. save\_widget\_layout\_settingメソッドがajaxで呼び出される。
    
      - > このメソッド中でweko\_gridlayout.services.WidgetDesignPageServices. update\_widget\_design\_settingメソッドを呼び出し、その中で以下のテーブルのレコードを作成または更新する。
        
          - > widget\_design\_page（デフォルトページ以外。更新のみ）
            
              - > 「settings」：「Preview」エリアのウィジェット配置情報
        
          - > widget\_design\_setting（デフォルトページ）
            
              - > 「repository\_id」：選択中のリポジトリのid
            
              - > 「settings」：「Preview」エリアのウィジェット配置情報

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