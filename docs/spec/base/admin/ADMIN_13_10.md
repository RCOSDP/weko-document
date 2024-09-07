### セッションアクティビティ

  - > 目的・用途

本機能は、活動セッションを確認する際に使用する機能である。

  - > 利用方法

【Administration \> ユーザー管理（User Management） \> セッションアクティビティ（Session Activity）画面】にて操作を行う。

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

  - 【セッションアクティビティ（Session Activity）画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 選択▼（With selected▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー

  - 「一覧」（List）タブでの表示項目は以下の通りである
    
      - チェックボックス
    
      - アクション（削除を表すアイコン）
    
      - 「User ID」
    
      - 「Email」
    
      - 「Session ID」
    
      - 「Created」  
        フォーマット：「YYYY-MM-DDThh:mm:ss.tttttt」

  - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する
    
      - フィルター名
        
          - 「User ID」
            
              - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        
          - 「Email」
            
              - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        
          - 「Session ID」
            
              - フィルター方式の選択肢：上記の「Email」と同じである
        
          - 「Created」
            
              - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
            
              - フォーマット：「YYYY-MM-DD hh:mm:ss」
    
      - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される
    
      - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる

  - 「選択▼」（With selected▼）ボタンをクリックすると、以下の追加可能な機能（「Delete selected sessions」ボタン）を表示する
    
      - レコードにチェックを入れない場合、「Delete selected sessions」ボタンを押すと、エラーメッセージを表示する  
        メッセージ：  
        　日本語：「少なくとも一つのレコードを選択してください。」  
        　英語：「Please select at least one record.」
    
      - レコードにチェックを入れる場合、「Delete selected sessions」ボタンを押すと、確認ダイアログを表示する  
        メッセージ：「Are you sure you want to delete selected sessions?」
        
          - 「OK」ボタンを押すと、該当活動セッションを削除する
            
              - チェックを入れていたレコードに現在のセッションを指すレコードが含まれていた場合、削除されずに以下のエラーメッセージが表示される  
                エラーメッセージ：「You could not remove your current session」
        
          - 「キャンセル」（Cancel）ボタンを押すと、確認ダイアログを閉じる

  - 活動セッション行にて削除アイコンを押すと、該当活動セッションを削除する
    
      - 現在のセッションを指す行では、削除されずに以下のエラーメッセージが表示される  
        エラーメッセージ：「You could not remove your current session」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio\_accounts

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - ごみ箱ボタンによってレコードを削除する場合は、invenio\_accounts.admin.SessionActivityView. delete\_modelメソッドが呼び出される
    
      - 現在のログインのセッションのID（session.sid\_s）と対象レコードのSession IDとを比較して、同じだった場合には削除せずエラーメッセージを表示する

  - 「Delete selected sessions」によってレコードを削除する場合は、invenio\_accounts.admin.SessionActivityView.action\_deleteメソッドが呼び出される
    
      - 現在のセッションのID（session.sid\_s）と選択した各レコードのSession IDとを比較して、同じであるレコードがあった場合には削除せずエラーメッセージを表示する

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
