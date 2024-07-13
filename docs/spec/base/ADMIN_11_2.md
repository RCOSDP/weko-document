


### レコードメタデータ

  - > 目的・用途

本機能は、レコードメタデータの閲覧、削除、復元の際に用いる機能である

  - > 利用方法

【Administration \> レコード管理（Records） \> レコードメタデータ（Record Metadata）画面】にて操作を行う

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

  - 【レコードメタデータ（Record Metadata）画面】には以下のタブが表示される
    
      - 一覧（List）
        
          - このタブの表示中のみ、タブ名の末尾に件数が表示される
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 選択▼（With selected▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 詳細（Details）
        
          - 一覧（List）タブ選択中は非表示一覧（List）タブでの操作によって表示される

  - 「一覧」（List）タブにてレコードメタデータを一覧表示する
    
      - 表示項目は以下のとおりである
        
          - アクション（閲覧・削除を表すアイコン）
        
          - UUID
        
          - Status
        
          - Revision
        
          - Updated
        
          - Created
    
      - 「フィルターを追加▼」（Add Filter▼）タブをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する
        
          - フィルター名は以下の通りである
            
              - Created
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - Updated
                
                  - フィルター方式の選択肢：上記のCreatedと同じである
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
        
          - 設定したフィルターは［適用（Apply）］ボタンを押下することで一覧に適用される
        
          - ［フィルターをリセット（Reset filter）］ボタンを押下すると、設定したフィルターがリセットされる
    
      - 「選択▼」（With selected▼）タブをクリックすると、以下の追加可能な機能（現在削除ボタンのみ）を表示する
        
          - レコードにチェックを入れない場合、［削除（Delete）］ボタンを押すと、エラーメッセージを表示する  
            メッセージ：  
            　日本語：「少なくとも1つのレコードを選択してください。」  
            　英語：「Please select at least one record.」
        
          - レコードにチェックを入れる場合、［削除（Delete）］ボタンを押すと、確認ダイアログを表示する  
            メッセージ：  
            　日本語：「選択したレコードを削除してもよろしいですか。」  
            　英語：「Are you sure you want to delete selected records?」
            
              - ［OK］ボタンを押すと、該当レコードメタデータを削除状態に変更し、メッセージを画面上部に表示する  
                メッセージ：  
                　日本語：「レコード数＋レコードが正常に削除されました。」  
                　英語：「Record was successfully deleted.」
            
              - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
        
          - この操作を行ったレコードは、詳細（Details）タブを表示するとJSONが「null」に変化している
            
              - 一覧（List）タブでも詳細（Details）タブでもStatusは変化しない
    
      - レコードメタデータ行にて目アイコンを押すと、該当レコードメタデータの詳細情報を詳細（Details）タブに表示する
    
      - レコードメタデータ行にてごみ箱アイコンを押すと、該当レコードメタデータを物理削除し、メッセージを画面上部に表示する  
        メッセージ：  
        　日本語：「レコード数＋レコードが正常に削除されました。」  
        　英語：「Record was successfully deleted.」

  - 詳細（Details）タブでは、該当レコードメタデータの詳細情報を表示する
    
      - 表示項目：UUID、Status、Revision、Updated、Created、JSON
    
      - ［削除（Delete）］ボタンは以下のようにふるまう
        
          - このボタンは、StatusがDELETED以外のときに押すことができる
        
          - このボタンを押すと、以下のメッセージがポップアップで表示される
            
              - 日本語：「サーバ内部エラー」
            
              - 英語：「Internal server error」
    
      - ［復元（Restore）］ボタンは以下のようにふるまう
        
          - このボタンは、StatusがDELETEDのときに押すことができる
        
          - このボタンを押すと、ページ未検出エラーの画面に遷移する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio\_records：画面を定義

  - weko\_records：soft\_delete処理と復元処理を定義

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 本画面は、flaskのModelViewでrecords\_metadataテーブルの内容を閲覧、編集、削除する際に用いる機能である

  - 画面で表示されるstatusはテーブルに含まれない項目で、情報取得時にpidstore\_pidテーブルから以下の条件を満たすレコードのstatusを取得している
    
      - pid\_typeが「recid」
    
      - object\_uuidがrecords\_metadataテーブルでのidと一致する

  - v0.9.22では、詳細（Details）タブでの操作は必ずエラーが発生するようになっている
    
      - ［削除（Delete）］ボタンを押したときには'/soft\_delete/\<string:id\>'の形で、［復元（Restore）］ボタンを押したときには'/restore/\<string:id\>'の形でリクエストのURLを作成するが、適切に作成できていない
        
          - ModelViewでDetailsを表示すると、URL末尾に「\&url=...」が入るようになっている
        
          - リクエストのURLは、ボタンを押したときの画面のURLから「detail」を置換して「id=」を取り除いて作成しており、末尾の「\&url=...」がそのままになっているため不正なidを指定した状態になる
        
          - これによって、soft\_delete関数やrestore関数に到達しない
            
              - テンプレートにて、［削除（Delete）］ボタンを押してエラーが発生した場合にメッセージを表示するようになっているが、［復元（Restore）］ボタンの場合にはエラー発生時の記述がないためページ未検出エラーの画面に遷移する
    
      - DetailsタブのURLから末尾の「\&url=...」を取り除いたものでも同様の画面を表示できるため、その状態でボタンを押すことで各関数に到達することができる

  - 一覧（List）タブにて、レコードをチェックして「選択▼」（With selected▼）タブの［削除（Delete）］ボタンを押すと、チェックしたレコードごとにinvenio\_records.admin. RecordMetadataModelView.delete\_modelメソッドが呼び出される
    
      - 該当レコードのJSONが「null」だった場合は処理を終了する
    
      - invenio\_records.api Record.deleteメソッドによって、該当レコードのJSONを「null」にする

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
