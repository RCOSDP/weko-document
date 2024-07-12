### 永続識別子

<!-- end list -->

  - > 目的・用途

<!-- end list -->

  - システムに登録しているアイテムの永続識別子を閲覧する機能である

  - 一つのオブジェクトに対して複数の永続識別子があることができる

  - 永続識別子の値はユニークとする

<!-- end list -->

  - > 利用方法

【Administration \> レコード管理（Records） \> 永続識別子（Persistent Identifier）画面】にて閲覧する

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

  - 【永続識別子（Persistent Identifier）画面】には以下のタブが表示される
    
      - 一覧（List）
        
          - このタブの表示中のみ、タブ名の末尾に件数が表示される
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 詳細（Details）
        
          - 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブでの操作によって表示される

  - 「一覧」（List）タブにて永続識別子一覧を表示する
    
      - 表示項目は以下の通りである
        
          - アクション（閲覧を表すアイコン）
        
          - 「PID Type」
            
              - 「oai」：OAIの値  
                PIDのフォーマット：「scheme ":" namespace-identifier ":" local-identifier」  
                scheme = "oai"  
                namespace-identifier = "invenio"
            
              - 「depid」：デポジット識別子の値
            
              - 「recid」：レコード識別子の値
            
              - 「parent」：親レコードの値
            
              - 「actid」：アクティビティID
            
              - 「doi」：付与されたDOIの値
            
              - 「hdl」：付与されたCNRIの値
            
              - 「hvstid」：アイテムがハーベスト機能でインポートした場合の値
        
          - 「PID」
        
          - 「Status」
            
              - 「NEW」：PIDが登録されない状態である
            
              - 「RESERVED」：予約済みで完全登録されない状態である
            
              - 「REGISTERED」：登録された状態である
            
              - 「REDIRECTED」：他の永続識別子にリダイレクトされた状態である
            
              - 「DELETED」：削除された状態である
        
          - 「Object Type」
        
          - 「Object UUID」
        
          - 「Created」：アイテムの登録時間  
            フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
        
          - 「Updated」：アイテムの編集時間  
            フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
        
          - 「Object」リンク  
            「View」リンクを押すと、【Administration \> レコード管理（Records） \> レコードメタデータ（Record Metadata）画面】に移動、該当オブジェクト詳細画面が表示される

  - 「フィルターを追加▼」（Add Filter▼）タブをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルターの入力エリアを追加する
    
      - フィルター名
        
          - 「PID Type」  
            フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        
          - 「PID」  
            フィルター方式の選択肢：「PID Type」の同じである
        
          - 「Object Type」  
            フィルター方式の選択肢：「PID Type」の同じである
        
          - 「Object UUID」  
            フィルター方式の選択肢：等しい（equals）
        
          - 「Status」  
            フィルター方式の選択肢：等しい（equals）  
            フィルターの選択肢：「新規」（New）、「予約済み」（Reserved）、「登録された」（Registered）、「リダイレクトされた」（Redirected）、「削除日」（Deleted）
    
      - 設定したフィルターは［適用（Apply）］ボタンを押下することで一覧に適用される
    
      - ［フィルターをリセット（Reset filter）］ボタンを押下すると、設定したフィルターがリセットされる

  - 永続識別子行にて目アイコンを押すと、該当永続識別子の詳細情報を「詳細」（Details）タブに表示する
    
      - 表示項目：Created、Updated、PID Type、PID、Provider、Status、Object Type、Object UUID、Redirects、Child Relations、Parent Relations

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio\_pidstore（WEKOソース内にforkされていない）

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 本機能は、flaskのModelViewでpidstore\_pidテーブルの内容を閲覧する際に用いる機能である

  - ソースとしては以下を参照
    
      - パス：<https://github.com/inveniosoftware/invenio-pidstore/blob/v1.0.0/invenio_pidstore/admin.py#L46-L75>

  - pidstore\_pidテーブルのstatusフィールドについては、値のかわりにinvenio\_pidstore.models.PIDStatusクラスで関連付けられた文字列を表示する

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