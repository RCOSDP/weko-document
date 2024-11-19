
### OAuthアプリケーション

  - > 目的・用途

本機能は、管理者として登録されているOAuthアプリケーション情報を閲覧、編集、削除する機能である。  
※invenioデフォルト機能を使用

  - > 利用方法

【Administration \> ユーザー管理(User Management) \> OAuthアプリケーション(OAuth Applications)】を表示する。

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

  - 【OAuthアプリケーション (OAuth Applications)画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - 作成（Create）
    
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

  - 「一覧」（List）タブにOAuthアプリケーション一覧を表示する。
    
      - 表示項目は以下の通りである。
        
          - チェックボックス
        
          - アクセス（閲覧・編集・削除）
            
              - 目のマークを押すと「詳細」タブに遷移する。
            
              - 鉛筆のマークを押すと「編集」タブに遷移する。
            
              - ゴミ箱のマークを押すとその行のレコードは削除される。  
                なお、そのレコードのClient Idを使用しているトークンはoauth2server\_ tokenテーブルから削除される。
        
          - 「Name」：OAuth表示名
        
          - 「Description」：説明、備考
        
          - 「Website」：URL
        
          - 「User Id」：ユーザー側のＩＤ
        
          - 「Client Id」：クライアント側のＩＤ
    
      - 左から2列目にある目アイコンを押すと、該当OAuthの詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目：Name, Description, Website, User Id, Client id
    
      - 左から２列目にある鉛筆アイコンを押すと、「編集」（Edit）タブに表示し、ユーザーの情報が編集できる
        
          - 編集可能な項目は以下の通りである。
            
              - 「User」
                
                  - 選択肢：登録されているユーザーから選択する。
                
                  - 部分一致検索ができる。
            
              - 「Name」：自由記述
            
              - 「Description」：自由記述
            
              - 「Client Secret」:必須項目である。Client Idとは別のものである。自由記述
            
              - 「Is Confidential」：機密であるかどうか
            
              - 「Is Internal」：内部用
            
              - 「Oauth2Tokens」
                
                  - 選択肢：登録されているトークンから複数選択する。
                
                  - 部分一致検索ができる。ただし、トークンのIDでの検索となる。
        
          - 「保存」（Save）ボタンを押すと、編集内容を保存し、メッセージを一覧画面の上部に表示する  
            メッセージ：  
            　日本語：「レコードが正常に保存されました。」  
            　英語：「Record was successfully saved.」
    
      - 複数のOAuth情報を一度に削除する。
        
          - 左端のチェックボックスにチェックを入れ、選択タブから「削除」を選ぶと、削除するかの確認アラートが表示される、
            
              - OKを押すとチェックボックスにチェックを入れた行のトークンは削除される。
            
              - キャンセルを押すとキャンセルできる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_oauth2server

  - > flask\_admin:  
    > <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - OAuthアプリケーション画面の処理について
    
      - OAuthアプリケーション画面を表示する。その場合、invenio\_oauth2server.admin.ClientViewが継承したModelViewよりflask\_admin.model.base.index\_viewメソッドを呼び出す。このメソッドでoauth2server\_clientテーブルよりOAuth情報を取得し、ClientViewのcolumn\_listにあるキーに対応する情報を画面に表示する。
        
          - OAuthアプリケーション詳細画面を表示する。この操作によって、invenio\_files\_rest.admin.ClientViewが継承したModelViewよりflask\_admin.model.base.details\_viewメソッドを呼び出す。このメソッド下でoauth2server\_clientテーブルよりOAuth情報を取得し、ClientViewのcolumn\_details\_listにあるキーに対応する情報を画面に表示する。
    
      - OAuthアプリケーション編集画面を表示する。この操作によって、invenio\_files\_rest.admin.ClientViewが継承したModelViewよりflask\_admin.model.base.edit\_viewメソッドをGETで呼び出す。このメソッド下で開いたoauth2server\_clientテーブルよりOAuth情報を取得し、表示する。
        
          - OAuthアプリケーション編集画面で「保存」ボタンを押下する。この操作によって、flask\_admin.model.base.edit\_viewメソッドをPOSTで呼び出す。このメソッド下で、get\_save\_return\_urlメソッドが呼ばれ、編集内容をoauth2server\_clientテーブルに保存し、更新する。
    
      - > OAuthアプリケーション画面に表示される表の左から２列目のゴミ箱マークを押下する。この操作によって、invenio\_files\_rest.admin.ClientViewが継承したModelViewよりflask\_admin.model.base.delete\_viewメソッドを呼び出す。このメソッド下でdelete\_modelメソッドが呼ばれ、押下したゴミ箱の行のトークンをoauth2server\_clientテーブルから削除する。
    
      - OAuthアプリケーション画面に表示される表の左端のチェックボックスにチェックを入れ、選択タブから「削除」を押下し、OKを押下する。この操作によって、invenio\_files\_rest.admin.ClientViewが継承したModelViewよりflask\_admin.model.base.action\_viewメソッドを呼び出す。ここでDeleteRowActionが呼ばれ、チェックを入れた行のトークンをoauth2server\_clientテーブルから削除する。

> OAuth情報は以下のようなデータベースに保存する。

  - テーブル名：「oauth2server\_client」

  - > フィールド名：  
    > ・「name」  
    > ・「description」  
    > ・「website」  
    > ・「user\_id」  
    > ・「client\_id」  
    > ・「client\_secret」  
    > ・「is\_confidential」  
    > ・「is\_internal」  
    > ・「\_redirect\_uris」  
    > ・「\_default\_scopes」

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
