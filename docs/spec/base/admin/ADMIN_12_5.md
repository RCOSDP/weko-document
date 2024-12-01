### オブジェクトバージョン

  - > 目的・用途

本機能は、管理者として、アップロードしているアイテムのファイルバージョンを管理する機能である。

  - > 利用方法

【Administration \> ファイル管理(Files) \>オブジェクトバージョン(Object Version)画面】を表示する。

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

  - 【オブジェクトバージョン(Object Version)画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 詳細（Details）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 詳細（Details）タブ選択中に表示

  - 「一覧」（List）タブにアイテムにアップロードしているファイルバージョンを表示する。
    
      - 表示項目は以下の通りである
        
          - アクセス（閲覧）
            
              - 目のマークを押すと「詳細」タブに遷移する。
        
          - 「Bucket」：該当バケットのID値
        
          - 「Key」：ファイル名
        
          - 「Version」：ファイルのバージョン
        
          - 「URI」：ファイルのURI
        
          - 「Is Head」：True、False  
            True：最終版の場合
        
          - 「Deleted」：削除状態
        
          - 「Size」：ファイルの容量値
        
          - 「Created」：ファイルの作成時間  
            フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」
        
          - 「Updated」：ファイルの更新時間  
            フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」
        
          - 「Versions」リンク
            
              - リンクをクリックすると、該当オブジェクトバージョンがフィルターされる。
            
              - フィルター条件：
                
                  - 「bucket / Files Bucket / Id」：該当のバケット値
                
                  - 「key」：該当のファイル名
        
          - 「Objects」リンク
            
              - リンクをクリックすると、該当オブジェクトバージョンがフィルターされる。
            
              - フィルター条件：
                
                  - 「bucket / Files Bucket / Id」：該当のバケット値
                
                  - 「Is Head」：Yes
        
          - 「File」リンク
            
              - リンクをクリックすると、【Administration \> ファイル管理(Files) \> ファイルインスタンス(File Instance)画面】に移動し、該当ファイルがフィルターされる。
            
              - フィルター条件：  
                「ID」：該当ファイルID
    
      - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する。
        
          - フィルター名
            
              - 「bucket / Files Bucket / Id」
                
                  - フィルター方式の選択肢：等しい（equals）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「bucket / Files Bucket / Locked」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「bucket / Files Bucket / Deleted」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「bucket / Files Bucket / Name」
                
                  - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「File UUID」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Checksum」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Name」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Storage Class」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Name」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Readable」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「Key」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Name」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Version」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Id」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Is Head」
                
                  - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「Size」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - > 「Created」
                
                  - フィルター方式の選択肢：「Size」と同じである。
                
                  - > 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Updated」
                
                  - フィルター方式の選択肢：「Size」と同じである。
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
        
          - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される。
        
          - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる。
    
      - 検索テキストボックス検索する  
        プレースホルダー：「Search: key」
        
          - 任意テキストを入力し、キーボードでの「Enter」を押すと、部分一致検索を行う。
        
          - テキストボックスの右端での「X」ボタンを押すと、検索条件がクリアーされる。
    
      - 左端行の目アイコンを押すと、該当オブジェクトバージョンの詳細情報を「詳細」（Details）タブに表示する。
        
          - 表示項目：Bucket、Key、Version、File UUID、URI、Checksum、Size、Storage class、Is Head、Deleted、Created、Updated、File、Versions
        
          - 「File」リンクをクリックすると、【Administration \> ファイル管理(Files) \> ファイルインスタンス(File Instance)画面】に移動し、該当ファイルがフィルターされる。
        
          - 「Versions」リンクをクリックすると、該当オブジェクトバージョンがフィルターされる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio-files-rest

  - > flask-admin:  
    > <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

<!-- end list -->

  - > 処理概要

> オブジェクトバージョン画面の処理について

  - オブジェクトバージョン画面を表示する。この操作によって、invenio\_files\_rest.admin. ObjectModelViewが継承したModelViewよりflask\_admin.model.base.index\_viewメソッドを呼び出す。このメソッドでfiles\_objectテーブルよりバケット情報を取得し、ObjectModelViewのcolumn\_listにあるキーに対応する情報を画面に表示する。
    
      - オブジェクトバージョン詳細画面を表示する。この操作によって、invenio\_files\_rest.admin.ObjectModelViewが継承したModelViewよりflask\_admin.model.base.details\_viewメソッドを呼び出す。このメソッド下でfiles\_objectテーブルよりオブジェクトバージョン情報を取得し、ObjectModelViewのcolumn\_details\_listにあるキーに対応する情報を画面に表示する。

> オブジェクトバージョンの情報は以下のようなデータベースに保存する

  - テーブル名：「files\_object」

<!-- end list -->

  - > フィールド名：  
    > ・「version\_id」  
    > ・「key」  
    > ・「bucket\_id」  
    > ・「file\_id」  
    > ・「root\_file\_id」  
    > ・「\_mimetype」  
    > ・「is\_head」  
    > ・「created\_user\_id」  
    > ・「updated\_user\_id」  
    > ・「bucket」  
    > ・「is\_show」  
    > ・「is\_thumbnail」  
    > ・「created」  
    > ・「updated」

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