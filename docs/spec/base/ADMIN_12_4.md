### マルチパートオブジェクト

  - > 目的・用途

本機能は、マルチパートアップロードが使用されているオブジェクトを閲覧する機能である。

※invenioデフォルト機能を使用

  - > 利用方法

【Administration \> ファイル管理(Files) \> マルチパートオブジェクト(Multipart Object)画面】を表示する。

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

<!-- end list -->

  - 【ファイルインスタンス(File Instance)画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - フィルターを追加▼（Add Filter▼）
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 選択（With selected）
    
      - 詳細（Details）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 詳細（Details）タブ選択中に表示

  - 「一覧」（List）タブにマルチパートオブジェクト一覧を表示する。
    
      - 表示項目は以下の通りである。
        
          - アクセス（閲覧）
            
              - 目のマークを押すと「詳細」タブに遷移する。
        
          - 「Upload Id」
        
          - 「Complete」
        
          - 「Created」：アイテムの登録時間  
            フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
        
          - 「Updated」アイテムの編集時間  
            フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
        
          - 「Key」：ファイル名
        
          - 「Size」：ファイルサイズ
        
          - 「Created By」：ファイルアップロードしたユーザのメールアドレス
        
          - 「File」リンク
            
              - リンクをクリックすると、【Administration \> ファイル管理(Files) \> ファイルインスタンス(File Instance画面)】に移動し、該当ファイルがフィルターされる。RepositoryAdminはリンクではなくラベル。
            
              - フィルター条件：  
                「ID」：該当ファイルID
        
          - Item Bucket
            
              - 「Item Bucket（紐付済）」リンクをクリックすると【Administration \> ファイル管理(Files) \> バケット（Bucket）】に移動し、該当バケットがフィルタされる。RepositoryAdminの場合は、リンクではなくラベル。バケット未設定の場合は、「Unbind（未紐付）」ラベル表記される。
    
      - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する。
        
          - フィルター名
            
              - 「Upload Id」
                
                  - フィルター方式の選択肢：等しい(equals)
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「completed」
                
                  - フィルター方式の選択肢：等しい(equals)、等しくない(not equal)
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「Created」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Updated」
                
                  - フィルター方式の選択肢：「Created」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Item Bucket」
                
                  - フィルター方式の選択肢：「is Unbind」
                
                  - 入力された文字列は使わず、Unbind（未紐付）のレコードだけ
        
          - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される。
        
          - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる。
    
      - 選択（With selected）ボタンをクリックすると、以下の一括処理可能な処理リストを表示し、処理をクリックすると選択したレコードに対して一括で処理を行う
        
          - 処理名
            
              - 削除（Delete）
    
      - 左端の目アイコンを押すと、該当オブジェクトバージョンの詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目は一覧タブで表示されたものと同じである。
    
      - 左端のゴミ箱アイコンを押すと、該当オブジェクトバージョンを削除する
    
      - 「完了済みかつ紐付先あり」または、レコードが排他中の場合は削除エラーとなる。「File」リンクをクリックすると、【Administration \> ファイル管理(Files) \> ファイルインスタンス(File Instance)画面】に移動し、該当ファイルがフィルターされる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > Invenio\_files\_rest

  - > flask-admin:  
    > <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

<!-- end list -->

  - > 処理概要

> マルチパートオブジェクト画面の処理について

  - マルチパートオブジェクト画面を表示する。この操作によって、invenio\_files\_rest.admin. MultipartObjectModelViewが継承したModelViewよりflask\_admin.model.base.index\_viewメソッドを呼び出す。このメソッドでfiles\_multipartobjectテーブルよりバケット情報を取得し、MultipartObjectModelViewのcolumn\_listにあるキーに対応する情報を画面に表示する。
    
      - マルチパートオブジェクト詳細画面を表示する。この操作によって、invenio\_files\_rest.admin. MultipartObjectModelViewが継承したModelViewよりflask\_admin.model.base.details\_viewメソッドを呼び出す。このメソッド下でfiles\_multipartobjectテーブルよりマルチパートオブジェクト情報を取得し、MultipartObjectModelViewのcolumn\_details\_listにあるキーに対応する情報を画面に表示する。

> オブジェクトバージョンの情報は以下のようなデータベースに保存する

  - テーブル名：「files\_multipartobject」

> フィールド名：  
> ・「created」  
> ・「updated」  
> ・「upload\_id」  
> ・「bucket\_id」  
> ・「key」  
> ・「file\_id」  
> ・「chunk\_size」  
> ・「size」  
> ・「comleted」

  - > ・「created\_by\_id」更新履歴

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
<td>2023/12/22</td>
<td>4ec162bf3bdcf843df23863fbf7d5bb36ba875e4</td>
<td>W2023-42</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>