
##   

#### ADMIN-5-1-3:Affiliation ID

  - > 目的・用途

本機能は、登録済みの所属機関識別子の編集や、新たな所属機関識別子を追加するための機能である。

  - > 利用方法

【Administration\>著者DB管理（Author Management）\>編集（Edit）】の順で編集画面に遷移し、Affiliation　IDタブを押下する。

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

  - > 【Administration\>著者DB管理（Author Management）\>編集（Edit）】でのAffiliation IDタブに登録されている所属機関識別子一覧が表示される。
    
      - 表示項目は以下の通りである。
        
          - 「所属機関識別子（Name）」：所属機関の名前が表示される。
        
          - 「IDスキーマ名（Scheme）」：所属機関のSchemeが表示される。
        
          - 「URL」：所属機関のURLが表示される。
        
          - 「コントロール（Control）」：コントロールのボタンが表示される。  
            コントロールのボタンは［編集（Edit）］、［追加（Add）］である。
    
      - クリーンビルド環境での初期設定値は以下の通りである。
        
          - ISNI (URL: <https://www.isni.org/>isni/\#\#)
        
          - GRID(URL: https://www.grid.ac/institutes/\#\#)
        
          - Ringgold
        
          - Kakenhi
    
      - \[追加（Add）\]ボタンを押すと、入力内容をチェックする。
        
          - 問題があれば、外部著者ID Prefixを追加せず、エラーメッセージを表示する。
            
              - 何かの項目を入力しない場合、またはURL形式が不正場合は以下のメッセージを表示する。  
                エラーメッセージ：「Please enter the correct ＋　項目名」
            
              - 設定されたSchemeを選択する場合は以下のメッセージを表示する。  
                エラーメッセージ：「Specified scheme is already exist.」
        
          - 問題なければ、外部著者ID Prefixを追加し、以下のメッセージを表示する。  
            メッセージ：「Successfully added」
    
      - \[編集（Edit）\]ボタンを押すと、該当のAffiliation ID情報を編集可能とし、コントロールのボタンを該当行の直下に表示する。  
        コントロールのボタン：\[保存 （Save）」、\[キャンセル（Cancel）\]、\[削除（Delete）\]
        
          - 該当の外部著者ID Prefix情報を編集してから、\[保存 （Save）\]ボタンを押すと、編集内容を保存し、以下のメッセージを表示する。  
            メッセージ：「Update completed」
        
          - \[削除（Delete）\]ボタンを押すと、該当の外部著者ID Prefixを削除し、以下のメッセージを表示する  
            メッセージ：「Successfully deleted」
        
          - \[キャンセル（Cancel）\]ボタンを押すと、編集前の状態に戻る。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-authors

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - > IDスキーマ名（Scheme）プルダウンに表示するScheme一覧の設定をする。

<!-- end list -->

  - > パス：  
    > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L32>

  - > 設定キー：WEKO\_AUTHORS\_AFFILIATION

  - > 現在の設定値：  
    > WEKO\_AUTHORS\_LIST\_SCHEME\_AFFILIATION = \['ISNI', 'GRID', 'Ringgold', 'kakenhi', 'Other'\]

<!-- end list -->

  - > 「Other」のインデックスを設定する。

<!-- end list -->

  - > パス：  
    > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L36>

  - > 設定キー：WEKO\_AUTHORS\_IDENTIFIER\_ITEM\_OTHER

  - > 現在の設定値：  
    > WEKO\_AUTHORS\_AFFILIATION\_IDENTIFIER\_ITEM\_OTHER = 4

<!-- end list -->

  - > Affiliation ID画面のテンプレートを設定する。

<!-- end list -->

  - > パス：  
    > [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko\_authors/config.py\#L51](https://github.com/RCOSDP/weko/blob/0.9.22/modules/weko-authors/weko_authors/config.py#L51)

  - > 設定キー：WEKO\_AUTHORS\_ADMIN\_AFFILIATION\_TEMPLATE

  - > 現在の設定値：  
    > WEKO\_AUTHORS\_ADMIN\_AFFILIATION\_TEMPLATE = \\'weko\_authors/admin/affiliation\_list.html'

<!-- end list -->

  - > 【Administration\>著者DB管理(Author Management)\>編集(edit)】からAffiliation IDタブ押下で遷移する初期画面は、Affiliation IDタブ押下時にweko\_authors.views.get\_affiliation\_listが呼び出され、db内のauthors\_affiliation\_settingsテーブルの情報が取り出されて表示される。

  - 編集時は、\[編集（Edit）\]ボタンを押下することで編集が可能となり、内容の変更後に\[保存(Save)\]ボタンを押すことで、weko\_authors.views.update\_affiliationが呼び出されて、db内のauthors\_affiliation\_settingsテーブルの情報が更新される。

  - 削除時は、\[編集（Edit）\]ボタン押下後に出現する\[削除（Delete）\]ボタンを押下することで、weko\_authors.views.delete\_affiliationが呼び出され、db内のauthors\_affiliation\_settingsテーブルから削除対象が削除される。

  - 追加時は、追加したい情報を最下部のテキストボックスに入力後に\[追加（Add）\]ボタンを押すことで、weko\_authors.views.create\_affiliationが呼び出され、db内のauthors\_affiliation\_settingsテーブル内に情報が追加される。

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

