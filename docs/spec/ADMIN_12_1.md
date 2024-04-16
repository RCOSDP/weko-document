 ### バケット

<!-- end list -->

  - > 目的・用途

本機能は、コンテンツファイルを登録しているアイテムのバケットを閲覧、編集、作成する機能である

  - > 利用方法

【Administration \> ファイル管理(Files) \> バケット(Bucket)画面】を表示する。

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 【バケット(Bucket)画面】には以下のタブが表示される
    
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

  - 「一覧」（List）タブにバケット一覧を表示する。
    
      - 表示項目は以下の通りである。
        
          - アクセス（閲覧・編集）
            
              - 目のマークを押すと「詳細」タブに遷移する。
            
              - 鉛筆のマークを押すと「編集」タブに遷移する。
        
          - 「UUID」：バケットのID
        
          - 「Location」：バケットの設定場所
        
          - 「Default Storage Class」：S（Standard）、A（Archive）  
            デフォルト値：「S」
        
          - 「Deleted」
        
          - 「Locked」
        
          - 「Size」：アップロードされたファイルの容量
        
          - 「Quota Size」：アップロード可能容量
        
          - 「Created」：アイテムの登録時間  
            フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
        
          - 「Updated」アイテムの編集時間  
            フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
        
          - 「Objects」リンク  
            「Objects」リンクを押すと、【Administration \> ファイル管理(Files) \> オブジェクトバージョン(Object Version)画面】に移動し、該当オブジェクトがフィルターされる。
    
      - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する。
        
          - フィルター名
            
              - 「location / Files Location / Name」
                
                  - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Default Storage Class」
                
                  - フィルター方式の選択肢：「location / Files Location / Name」の同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Deleted」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「Locked」
                
                  - フィルター方式の選択肢：「Deleted」の同じである
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「Size」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Created」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Updated」
                
                  - フィルター方式の選択肢：「Created」の同じである
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
        
          - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される。
        
          - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる。
    
      - 左端行の目アイコンを押すと、該当バケットの詳細情報を「詳細」（Details）タブに表示する。
        
          - 表示項目：UUID、Location、Default Storage Class、Deleted、Locked、Size、Quota Size、Max File Size、Created、Updated、Objects、Object Versions
        
          - 「Objects」リンクをクリックすると、【Administration \> ファイル管理(Files) \> オブジェクトバージョン(Object Version)画面】に移動し、該当オブジェクトがフィルターされる。
        
          - 「Object Versions」リンクをクリックすると、【Admin \> Files \> Object Version画面】に移動し、該当オブジェクトバージョンがフィルターされる。
    
      - 左端行の鉛筆アイコンを押すと、「編集」（Edit）タブに表示し、ユーザーの情報が編集できる。
        
          - 編集可能な項目は以下の通りである。
            
              - 「Default Storage Class」  
                選択肢：Standard、Archive
            
              - 「Locked」
            
              - 「Deleted」
            
              - 「Quota Size」：整数のみ入力可
            
              - 「Max File Size」：整数のみ入力可
        
          - 「保存」（Save）ボタンを押すと、編集内容を保存し、メッセージを一覧画面の上部に表示する。  
            メッセージ：  
            　日本語：「レコードが正常に保存されました。」  
            　英語：「Record was successfully saved.」

  - 「作成」タブの機能は存在するが、現在画面上にロケーションを選択する欄がなく、「保存」ボタンを押下すると、エラーが出る。(v0.9.22)

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio-files-rest

  - > flask-admin:  
    > <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - バケット画面の処理について
    
      - バケット画面を表示する。この操作によって、invenio\_files\_rest.admin.BucketModelViewが継承したModelViewよりflask\_admin.model.base.index\_viewメソッドを呼び出す。このメソッドでfiles\_bucketテーブルよりバケット情報を取得し、BucketModelViewのcolumn\_listにあるキーに対応する情報を画面に表示する。
        
          - バケット詳細画面を表示する。この操作によって、invenio\_files\_rest.admin.BucketModelViewが継承したModelViewよりflask\_admin.model.base.details\_viewメソッドを呼び出す。このメソッド下でfiles\_bucketテーブルよりバケット情報を取得し、BucketModelViewのcolumn\_details\_listにあるキーに対応する情報を画面に表示する。
    
      - バケット編集画面を表示する。この操作によって、invenio\_files\_rest.admin.BucketModelViewが継承したModelViewよりflask\_admin.model.base.edit\_viewメソッドをGETで呼び出す。このメソッド下で開いたid列を用いて、files\_bucketテーブルよりバケット情報を取得し、表示する。
        
          - バケット編集画面で「保存」ボタンを押下する。この操作によって、flask\_admin.model.base.edit\_viewメソッドをPOSTで呼び出す。このメソッド下で、get\_save\_return\_urlメソッドが呼ばれ、編集内容をfiles\_bucketテーブルに保存し、更新する。
    
      - バケット作成画面を開いたとき、invenio\_files\_rest.admin.BucketModelViewが継承したModelViewよりflask\_admin.model.base.create\_viewメソッドをGETで呼び出す。BucketModelViewクラスのform\_columnsの項目の入力欄を表示する。
        
          - 入力欄に入力後「保存」ボタンを押下する。この操作によって、invenio\_files\_rest.admin.BucketModelViewが継承したModelViewよりflask\_admin.model.base.create\_viewメソッドをPOSTで呼び出す。このメソッド下でget\_save\_return\_urlメソッドが呼ばれ、新しいバケットの情報をfiles\_bucketテーブルに保存する。

  - バケット情報は以下のようなデータベースに保存する。
    
      - テーブル名：「files\_bucket」
    
    <!-- end list -->
    
      - > フィールド名：  
        > ・「created」  
        > ・「updated」  
        > ・「id」  
        > ・「default\_location」  
        > ・「default\_storage\_class」  
        > ・「size」  
        > ・「quota\_size」  
        > ・「max\_file\_size」  
        > ・「locked」  
        > ・「deleted」

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