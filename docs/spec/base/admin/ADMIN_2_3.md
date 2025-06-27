
# 一括エクスポート

## 目的・用途

本機能は、管理者として、アイテムの全件エクスポートを行う機能である。

## 利用方法

管理者は ```Administration→アイテム管理(Items)→一括エクスポート(Bulk Export)画面``` を開き、アイテムの全件エクスポートを行う。

## 利用可能なロール

<table>
<thead>
<tr class="header">
<th>ロール</th>
<th>システム<br />
管理者</th>
<th>リポジトリ<br />
管理者</th>
<th>サブリポジトリ<br />
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
<td>○※</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

|ロール|システム<br>管理者|リポジトリ<br>管理者|サブリポジトリ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|利用可否|○|○|○※| | | |


※サブリポジトリ管理者は、自身の管理下にあるサブリポジトリに関連付けられたインデックスのアイテムのみエクスポート可能

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

    - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに属するアイテムの中で最も新しく作られたアイテムIDを表示する。

  - 「エクスポート」（Export）ボタン  
    Exportボタンを押すと、全件出力を実行してよいかの確認ダイアログを表示する。確認ダイアログで実行/キャンセルを選択する。
    
      - 「Execute」ボタン
        
          - 「実行」ボタンを押すと、確認用ダイアログを閉じてアイテムの全件エクスポートを行う。

            - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに属するアイテムの全件エクスポートを行う。
        
          - 実行後はダウンロードのURLを画面上に表示する。
        
          - URLをクリックするとzipファイル(export-all.zip)をダウンロードする。  
            なお、このzipファイルにコンテンツファイルは含まれていない。
        
          - 他のユーザーがエクスポート実行中の場合、Exportボタンを非活性化する。
        
          - Celeryが起動していない場合は「実行」ボタンを非活性化する．「Celery is not running.」のエラーメッセージを表示する．(v0.9.22)
    
      - 「キャンセル」ボタン
        
          - 「キャンセル」ボタンを押すと、アイテムの全件エクスポートを行わず、確認用ダイアログを閉じる。

  - 「キャンセル」（Cancel）ボタン  
    初期状態は非活性とし、Exportを実行している時に活性とする。  
    Exportを実行している時に、キャンセルボタンを押すと、Export処理のキャンセルを行う。  
    ボタンを押すと、全件エクスポートの処理をキャンセルしてよいかの確認ダイアログを表示する。
    
      - 「実行」ボタン
        
          - 「実行」ボタンを押すと、全権エクスポートのキャンセルを実行する。
    
      - 「キャンセル」ボタン
        
          - 「キャンセル」ボタンを押すと、全件エクスポート処理のキャンセルを行わず、確認用ダイアログを閉じる。


## 関連モジュール

  - weko_search_ui
  - weko_admin
  - invenio_files_rest:ダウンロードファイル生成のみに使用

## 処理概要


  - 一括出力（一括エクスポート）画面表示時に以下の処理が行われる。
    
      - weko_search_ui.admin.ItemBulkExport.Indexメソッドが呼び出され画面を表示する。
    
      - weko\_search\_ui.static.js.weko\_search\_ui.export.getLastItemIdメソッドによってget\_last\_item\_idが呼び出され、一番大きなキーidを取得する。

        - Elasticsearchから以下の条件でアイテムを検索し、control_numberの最大値を取得する

          - サブリポジトリ管理者であれば、サブリポジトリに属するインデックスのリストでpathの中からフィルタリングする。

          - control_numberに.が含まれないものをフィルタリングする。
    
      - weko_search_ui.static.js.weko_search_ui.export.getListItemTypeメソッドによってget_itemtypesが呼び出され、アイテムタイプのリストを取得し、json形式にして取得する。

> これらの取得した情報から一括出力画面を表示する。

  - 一括出力（一括エクスポート）画面
    
      - 一括出力画面を表示している間、３秒ごとにweko_search_ui.static.js.weko_search_ui.export.checkExportStatusメソッドが呼び出される。このメソッド下でcheck_export_statusメソッドが呼び出され、これによってceleryが起動しているか、エクスポートできるかを確認する。

        - エクスポートが完了済みの場合、キャッシュから一時ディレクトリのパスを取得し、zipファイルを作成する。また一時ディレクトリのttlとしてその時刻からWEKO_SEARCH_UI_EXPORT_FILE_RETENTION_DAYS日を記録する
    
      - celeryが起動していない、uri_statusがfalseの場合は「エクスポート」ボタンを不活性化する。
    
      - アイテムタイプのプルダウンからアイテムタイプを選択すると、そのアイテムタイプに属するアイテムをエクスポート対象になるようweko_search_ui.static.js.weko_search_ui.export.SelectItemChangeメソッドで設定する。
    
      - アイテムIDの入力欄に数字を入力すると出力するアイテムIDをweko_search_ui.static.js.weko_search_ui.export.InputItemIdChangeメソッドで制限する。
    
      - 「エクスポート」ボタンを押し、更にポップアップの「Excute」ボタンを押下する。その場合、weko_search_ui.static.js.weko_search_ui.export.handleExportメソッドによってexport_allメソッドが呼び出され、更にexport_all_taskメソッドを呼び出す。これらによってエクスポートするアイテムのメタデータを集め、ダウンロードURLを生成し、表示させる。

        - export_all_taskでWEKO_SEARCH_UI_BULK_EXPORT_LIMIT件ごとでpickleファイルの作成を行いwrite_files_tasksを実行する
        - write_files_taskでpickleファイルからエクスポート対象のデータを取得し、tsvファイルを作成する
        - export_all_task, write_files_taskでエラーが発生した場合、その回のエクスポートの一時ディレクトリを削除する

      - エクスポートして、URLが表示されるまでの間に、「キャンセル」ボタンを押し、「execute」ボタンを押す。その場合、weko_search_ui.admin.ItemBulkExport.cancel_exportメソッドが呼び出され、ダウンロードURLの生成、表示をキャンセルする。またその回のエクスポートで作成された一時ディレクトリを削除する
    
      - 画面上に表示されたダウンロードURLを押下する。その場合、weko_search_ui.admin.ItemBulkExport.export_allメソッドにて、 FileInstance.get_by_uriメソッドが呼び出され、ダウンロードファイルを生成し、ダウンロードする。なお、ダウンロードされるファイル形式はzipであり、アイテムのメタデータについてのファイルはtsv形式である。

        - エクスポート結果のzipファイルのttlがWEKO_SEARCH_UI_FILE_DOWNLOAD_TTL_BUFFER秒以下だった場合、ttlの時間をWEKO_SEARCH_UI_FILE_DOWNLOAD_TTL_BUFFER秒延長する
    
      - 一括エクスポートはHide項目も含めて出力する。(メタデータプロパティがHideのものも表示する。)
    
      - エクスポート中にcheck_celery_is_runメソッド、get_export_statusメソッドでエクスポートに必要な情報がとれない場合、ダウンロードURLは表示されない。

  - エクスポート処理実行時、テンポラリディレクトリのファイル名を以下のように設定する
    
      - > /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko_export_xxxxxxxx

  - 以下の変数はweko_admin.configで設定されている。
    
      - > 一括エクスポートはアイテムタイプ単位で出力する．1ファイルあたりの出力件数は　WEKO_SEARCH_UI_BULK_EXPORT_LIMIT　で設定する．(v0.9.22)
    
      - > 一括エクスポート中にエラーが発生した場合は，WEKO_SEARCH_UI_BULK_EXPORT_RETRYに指定された回数リトライする．(v0.9.22)

      - WEKO_ADMIN_CACHE_PREFIX : REDISキーフォーマット

各設定値
|設定値名|説明|デフォルト値|
|:--:|:--|:--|
|WEKO_SEARCH_UI_BULK_EXPORT_EXPIRED_TIME|一括エクスポート結果の保存期間（日）|7|
|WEKO_SEARCH_UI_FILE_DOWNLOAD_TTL_BUFFER|一括エクスポート結果ダウンロードの際のバッファ（秒）|3600|
|WEKO_SEARCH_UI_BULK_EXPORT_LIMIT|1ファイルあたりの出力件数。500件以上の場合エラーが発生する恐れあり|300|
|WEKO_SEARCH_UI_BULK_EXPORT_RETRY|一括エクスポート中でエラーが発生した際のリトライ数|5|
|WEKO_SEARCH_UI_BULK_EXPORT_RETRY_INTERVAL|一括エクスポート中のエラーの際におけるリトライ間のインターバル（秒）|1|

##

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|> 2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|> 2025/01/23|-|サブリポジトリ対応|
