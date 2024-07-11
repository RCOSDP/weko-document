
### Sets

  - > 目的・用途

本機能は、setの作成・編集・削除を行う機能である。Setとは、選択的ハーベスティングを行う目的でアイテムをグループ化するための任意の構成隊のことを示す。

  - > 利用方法

【Administration＞OAI-PMH＞Sets】の順で画面遷移して利用する。

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

  - 【Administration \> OAI-PMH \> Sets 】：アイテムをグループ化する情報を設定可能。
    
      - 設定内容
        
          - Created、Updated：カレンダーから選択可能。  
            フォーマット：YYYY-MM-DD HH:MM:DD」  
            デフォルト：現在のシステム時刻を自動的に入れる
        
          - Spec：スペックの情報を入れる。ユニークとする。入力必須項目。
        
          - Name：セットの命名を入れる
        
          - Description：セットの説明を入れる
        
          - Search Pattern
    
      - 「保存（Save）」ボタンを押すと、設定されたセット内容をセット一覧に追加させ、メッセージをセット一覧に表示させる  
        メッセージ：「レコードが正常に作成されました。（Record was successfully saved）」
    
      - \[保存してもう一つ追加（Save Add Another）\]ボタンを押すと、設定されたセット内容をセット一覧に追加させ、他のセットを追加設定可能とする。
    
      - \[保存して編集を続ける（Save and Continue Editing）\]ボタンを押すと、設定されたセット内容をセット一覧に追加させ、該当セットの編集を続けることを可能とする。
    
      - Sets一覧は、更新日時降順で表示されている。

  - 使い方
    
      - 【ハーベスト機関元】
        
          - 【Administration \>コミュニティ管理（ Communities） \>コミュニティ（Community）】においてコミュニティを新規作成すると、  
            作成されたコミュニティに対して、【Administration \> OAI-PMH \> Sets】に以下のセットが自動作成される。  
            「Spec」：「user-」+ コミュニティID  
            「Name」：コミュニティID  
            「Updated」、「Created」：セット作成時間
        
          - OAISetにそれぞれのアイテムを登録する際は以下のコマンドを実行する。  
            「community\_id」：該当コミュニティ  
            「record\_id」：アイテムのuuid値

> docker-compose exec web invenio communities request -a community\_id record\_id

  - 【ハーベスト機関先】  
    ハーベスト設定画面での「Set Spec」に該当「Spec」値をいれば、登録アイテムをハーベストできる。

<!-- end list -->

  - 
<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > Invenio\_oaiserver

<!-- end list -->

  - > 処理概要

> 画面表示について

  - > 一覧タブ  
    > invenio\_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask\_admin.model.base.index\_viewが呼び出され、db内のoaiserver\_setテーブルより情報を取得し画面に表示する。

  - > 編集タブ  
    > \[鉛筆\]ボタン押下時、invenio\_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask\_admin.model.base.edit\_viewが呼び出され、db内のoaiserver\_setテーブルより情報を取得し編集画面へ遷移する。
    
      - > 編集画面で\[保存（Save）\]ボタンもしくは\[保存して編集を続ける（Save and Continue Editing）\]を押下時、flask\_admin.model.base.edit\_viewが呼び出され、編集内容をdb内のoaiserver\_setテーブルに保存し、更新する。

  - > 作成タブ  
    > 作成タブに遷移時、invenio\_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask\_admin.model.base.create\_viewが呼び出される。
    
      - > 情報の入力後に\[保存（Save）\]ボタン押下すると、invenio\_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask\_admin.model.base.create\_viewが呼び出され、新しいSetの情報をdb内のoaiserverテーブルに保存する。

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