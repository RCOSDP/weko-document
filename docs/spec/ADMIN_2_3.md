
### 一括エクスポート

  - > 目的・用途

本機能は、管理者として、アイテムの全件エクスポートを行う機能である。

  - > 利用方法

管理者は 【Administrationistration \> アイテム管理(Items) \> 一括エクスポート(Bulk Export)画面】を開き、アイテムの全件エクスポートを行う。

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
<td>〇</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - Filter：一括出力するアイテムを制限する。(v0.9.22)
    
      - 一括出力するアイテムをアイテムタイプにより制限することができる。ALLを選択した場合はすべてのアイテムタイプを出力する。
    
      - 一括出力するアイテムをアイテムIDにより制限することができる。
        
          - 全件。 何も入力していない場合。 （デフォルト）
        
          - 単一のアイテムID。 例： 50
        
          - アイテムID範囲。 例： 10‐100
        
          - あるアイテムID以後。 例： 10‐
        
          - あるアイテムID以前。 例： ‐10
    
      - 出力の結果は選択したアイテムタイプと入力したアイテムIDの積集合。 デフォルトは全件出力。
    
      - 違うユーザーが違う条件で一緒に出力可能。ダウンロードURLが同じであるが、各ユーザーが設定した条件のエクスポートが可能。
    
      - 一人のユーザーが当時に出力できる条件は一つのみである。完了しない限り、次の出力はできない。

  - the last item ID: 最も新しく作られたアイテムIDを表示する。(v0.9.2)

  - 「エクスポート」（Export）ボタン  
    Exportボタンを押すと、全件出力を実行してよいかの確認ダイアログを表示する。確認ダイアログで実行/キャンセルを選択する。
    
      - 「Execute」ボタン
        
          - 「実行」ボタンを押すと、確認用ダイアログを閉じてアイテムの全件エクスポートを行う。
        
          - 実行後はダウンロードのURLを画面上に表示する。
        
          - URLをクリックするとzipファイル(export-all.zip)をダウンロードする。  
            なお、このzipファイルにコンテンツファイルは含まれていない。
        
          - 他のユーザーがエクスポート実行中の場合、Exportボタンを非活性化する。
        
          - Celeryが起動していない場合は「実行」ボタンを非活性化する．「Celery is not running.」のエラーメッセージを表示する．(v0.9.22)
    
      - 「キャンセル」ボタン
        
          - 「キャンセル」ボタンを押すと、アイテムの全件エクスポートを行なわずわ、確認用ダイアログを閉じる。

  - 「キャンセル」（Cancel）ボタン  
    初期状態は非活性とし、Exportを実行している時に活性とする。  
    Exportを実行している時に、キャンセルボタンを押すと、Export処理のキャンセルを行う。  
    ボタンを押すと、全件エクスポートの処理をキャンセルしてよいかの確認ダイアログを表示する。
    
      - 「実行」ボタン
        
          - 「実行」ボタンを押すと、アイテムの全件エクスポートを行なわずわ、確認用ダイアログを閉じる。
    
      - 「キャンセル」ボタン
        
          - 「キャンセル」ボタンを押すと、全件エクスポート処理のキャンセルを行わず、確認用ダイアログを閉じる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_search\_ui

  - > weko\_admin

  - > invenio\_files\_rest:ダウンロードファイル生成のみに使用

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 一括出力（一括エクスポート）画面表示時に以下の処理が行われる。
    
      - weko\_search\_ui.admin.ItemBulkExport.Indexメソッドが呼び出され画面を表示する。
    
      - weko\_search\_ui.static.js.weko\_search\_ui.export.getLastItemIdメソッドによってget\_last\_item\_idが呼び出され、一番大きなキーidを取得する。
    
      - weko\_search\_ui.static.js.weko\_search\_ui.export.getListItemTypeメソッドによってget\_itemtypesが呼び出され、アイテムタイプのリストを取得し、json形式にして取得する。

> これらの取得した情報から一括出力画面を表示する。

  - 一括出力（一括エクスポート）画面
    
      - 一括出力画面を表示している間、３秒ごとにweko\_search\_ui.static.js.weko\_search\_ui.export.checkExportStatusメソッドが呼び出される。このメソッド下でcheck\_export\_statusメソッドが呼び出され、これによってceleryが起動しているか、エクスポートできるかを確認する。
    
      - celeryが起動していない、uri\_statusがfalseの場合は「エクスポート」ボタンを不活性化する。
    
      - アイテムタイプのプルダウンからアイテムタイプを選択すると、そのアイテムタイプに属するアイテムをエクスポート対象になるようweko\_search\_ui.static.js.weko\_search\_ui.export.SelectItemChangeメソッドで設定する。
    
      - アイテムIDの入力欄に数字を入力すると出力するアイテムIDをweko\_search\_ui.static.js.weko\_search\_ui.export.InputItemIdChangeメソッドで制限する。
    
      - 「エクスポート」ボタンを押し、更にポップアップの「Excute」ボタンを押下する。その場合、weko\_search\_ui.static.js.weko\_search\_ui.export.handleExportメソッドによってexport\_allメソッドが呼び出され、更にexport\_all\_taskメソッドを呼び出す。これらによってエクスポートするアイテムのメタデータを集め、ダウンロードURLを生成し、表示させる。
        
          - エクスポートして、URLが表示されるまでの間に、「キャンセル」ボタンを押し、「execute」ボタンを押す。その場合、weko\_search\_ui.admin.ItemBulkExport.cancel\_exportメソッドが呼び出され、ダウンロードURLの生成、表示をキャンセルする。
    
      - 画面上に表示されたダウンロードURLを押下する。その場合、weko\_search\_ui.admin.ItemBulkExport.export\_allメソッドにて、 FileInstance.get\_by\_uriメソッドが呼び出され、ダウンロードファイルを生成し、ダウンロードする。なお、ダウンロードされるファイル形式はzipであり、アイテムのメタデータについてのファイルはtsv形式である。
    
      - 一括エクスポートはHide項目も含めて出力する。(メタデータプロパティがHideのものも表示する。)
    
      - エクスポート中にcheck\_celery\_is\_runメソッド、get\_export\_statusメソッドでエクスポートに必要な情報がとれない場合、ダウンロードURLは表示されない。

  - エクスポート処理実行時、テンポラリディレクトリのファイル名を以下のように設定する
    
      - > /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_export\_xxxxxxxx

  - 以下の変数はweko\_admin.configで設定されている。
    
      - > 一括エクスポートはアイテムタイプ単位で出力する．1ファイルあたりの出力件数は　WEKO\_SEARCH\_UI\_BULK\_EXPORT\_LIMIT　で設定する．(v0.9.22)
    
      - > 一括エクスポート中にエラーが発生した場合は，WEKO\_SEARCH\_UI\_BULK\_EXPORT\_RETRYに指定された回数リトライする．(v0.9.22)

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
