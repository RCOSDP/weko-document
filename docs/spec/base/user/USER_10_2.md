### ワークスペース：簡易アイテム登録機能

#### 目的・用途

本機能は、WEKO3のシステム内で入力内容をDOI、ファイル本体、および最小限のメタデータのみとして、登録者の入力内容を極力減らした登録機能である。

#### 利用方法

【ワークスペース（WorkSpace） \> アイテム一覧（Item List） \> アイテム登録（Item Register）】にアイテム登録画面が表示される。

#### 利用可能なロール

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
<td>○</td>
<td>○</td>
<td>○</td>
<td></td>
</tr>
</tbody>
</table>

#### 機能内容

- 【ワークスペース（WorkSpace） \> アイテム一覧（Item List） \> アイテム登録（Item Register）】にアイテム登録画面が表示される。
    
    - 表示項目は以下の通りである
      
        - 「DOI入力」（DOI Input）  
          Inputの形式で表示される。
      
        - 「CrossRef MetaData」  
          Radioの形式で表示される。
      
        - 「JaLC MetaData」  
          Radioの形式で表示される。
      
        - 「CiNii MetaData」  
          Radioの形式で表示される。
      
        - 「DataCite MetaData」  
          Radioの形式で表示される。
                                
        - 「メタデータ」（Metadata）  
          Titleの形式で表示される。
                  
        - 「ファイル名」（File Name）    
          Inputの形式で表示される。
                  
        - 「公開日」（PubDate）  
          Inputの形式で表示される。
                  
        - 「タイトル」（Title）  
          Inputの形式で表示される。
                  
        - 「著者名」（Creator）  
          Inputの形式で表示される。
                  
        - 「アクセス権」（Access Rights）  
          プルダウンの形式で表示される。
                  
        - 「資源タイプ」（Resource Type）  
          プルダウンの形式で表示される。
                  
        - 「出版タイプ」（Version）  
          プルダウンの形式で表示される。
                  
        - 「識別子」（Identifier）  
          Inputの形式で表示される。
                  
        - 「関連識別子」（Relation Identifier）  
          Inputの形式で表示される。
                  
        - 「資金名」（Funding Name）  
          Inputの形式で表示される。
                  
        - 「ジャーナル名」（Bibliographic Name）  
          Inputの形式で表示される。
                  
        - 「会議名」（Conference Name）  
          Inputの形式で表示される。
                                                  
        - 「ファイル」（File）  
          Titleの形式で表示される。
                  
        - 「インデックス」（Index）  
          CheckBoxの形式で表示される。

    <!-- end list -->
    
      - \[取得（Get）\]ボタンを押すと、CrossRef MetaData、JaLC MetaData、CiNii MetaData、DataCite MetaDataラジオボタンを非活性から活性に変更する。DOIに該当するメタデータが見つかりませんでした場合は下記のメッセージが表示される。
        メッセージ：「DOIに該当するメタデータが見つかりませんでした。」
    
      - \[登録（Register）\]ボタンを押すと、weko\_workspace.views.item_register_saveが呼び出され、入力された情報がDBとESに保存される。保存が正常終了の場合は下記のメッセージが表示される。
        メッセージ：「アイテムが正常に登録されました。」
      保存が異常終了の場合は下記のメッセージが表示される。
        メッセージ：「エラーのステータスコード + エラー内容。」

<!-- end list -->

#### 関連モジュール
- weko\_deposit
- weko\_items_ui
- weko\_workflow

<!-- end list -->

#### 処理概要

- 【ワークスペース（WorkSpace） \> アイテム一覧（Item List） \> アイテム登録（Item Register）】の順で画面遷移すると、weko\_workspace.views.item_registerが呼び出され、アイテム登録画面が表示される

  -  各項目の初期値は以下のようになる。
        
      - 「DOI入力」（DOI Input）：空欄。
      - 「CrossRef MetaData」：非活性。 
      - 「JaLC MetaData」：非活性。
      - 「CiNii MetaData」：非活性。
      - 「DataCite MetaData」：非活性。
      - 「ファイル名」（File Name）：空欄。
      - 「公開日」（PubDate）：デフォルト(当日)。
      - 「タイトル」（Title）：空欄。
      - 「著者名」（Creator）：空欄。
      - 「アクセス権」（Access Rights）：空欄。
      - 「資源タイプ」（Resource Type）：空欄。
      - 「出版タイプ」（Version）：空欄。
      - 「識別子」（Identifier）：空欄。
      - 「関連識別子」（Relation Identifier）：空欄。
      - 「資金名」（Funding Name）：空欄。
      - 「ジャーナル名」（Bibliographic Name） ：空欄。
      - 「会議名」（Conference Name）：空欄。
      - 「インデックス」（Index）：チェックされない。


- メタデータ自動補完し、必須項目情報の入力後に\[登録（Register）\]ボタン押下で、weko\_workspace.views.item_register_saveが呼び出される。入力された情報がDBとESに保存される。

* メタデータ自動補完処理についてはそれぞれの項目に記述する(./user/USER_10_2.md)。
* ファイルアップロード処理についてはそれぞれの項目に記述する(./user/USER_4_5.md)。
* インデックス選択処理についてはそれぞれの項目に記述する(./user/USER_1_3.md)。

#### 更新履歴

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
<p>2025/03/27</p>
</blockquote></td>
<td>057e4d8985a4b5526c0db7f07f717a4bb45bc984</td>
<td>初版作成</td>
</tr>
</tbody>
</table>


