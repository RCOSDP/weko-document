
### 一括更新

<!-- end list -->

  - > 目的・用途

アイテムに付随しているファイルに対して、ライセンス、公開日、アクセスタイプを一括で更新する機能である。

  - > 利用方法

【Administration \> アイテム管理(Items) \> 一括更新(Bulk Update)画面】を開き、更新したいアイテムを選ぶ。  
その後更新したい情報を選び、更新する。

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
<td>〇</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 【Administration \> アイテム管理(Items) \> 一括更新(Bulk Update)画面】：一括更新を実行する画面である。

  - 事前に更新するアイテムの変更したい項目について設定されている必要がある。  
    ファイルが登録され、それに対して、アクセスタイプ、ライセンスをアイテムに登録しておく必要がある。

  - 【一括更新画面】は、以下の表示エリアで構成する
    
      - 「インデックスツリー」（Index Tree）エリア
        
          - 【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集(Edit Tree)画面】に設定されているインデックスツリーと同じに表示させる。
        
          - 任意のインデックスを選択するとインデックス配下のアイテムが「アイテムリスト」（Item list）エリアに表示される。
    
      - 「Fields For Update」エリア
        
          - 一括更新するメタデータ項目と更新内容を設定できる。
        
          - 一括更新対象のメタデータプルダウンリストは以下の項目とする。
            
              - Access Type
            
              - Licence
        
          - メタデータ項目を選択すると、該当設定オプションを表示する
            
              - Access Typeを選択すると、以下のオプションを表示する
                
                  - 「オープンアクセス」（Open Access）
                
                  - 「オープンアクセス日時」（Open Access Date）  
                    選択すると、日時を設定できる。デフォルトはサーバから取得した日付（/api/admin/get\_server\_date）とする
                
                  - 「ログインユーザのみ」（Login User Only）
            
              - Licenceを選択すると、ライセンスプルダウンリストを表示する。（アイテム登録画面に同じとする）
        
          - エリア右端に「×」ボタンが表示される。押下すると項目を削除できる。
            
              - 項目が一つだけの時、削除をすることはできない。
        
          - 複数項目を設定できるため、「フィールド追加」（Add Field）ボタンを設ける。
            
              - 押すと、更新内容の設定エリアを追加する。
        
          - メタデータプルダウンリストに同一項目を選択すると、選択不可とし、選択している項目が存在する旨のメッセージを表示する。  
            メッセージ：「Field already exists.」
    
      - 一括更新の対象アイテムの設定エリア
        
          - 「検索」（Search）エリア
            
              - 一括更新の対象アイテムを検索できる。
            
              - アイテム検索はWEKO3の詳細検索機能をそのまま利用する。
            
              - 最初に検索した時、「Item list」エリアの表示順設定は【設定\>検索設定】画面のデフォルトソート条件(キーワード検索)に従う。
            
              - 検索するごとにチェックボックスは初期化される。
        
          - 「Index List」エリア
            
              - インデックスツリーからインデックスを選択した時に表示される。
            
              - パンくずリスト、RSSアイコン、サムネイル画像を表示する。
        
          - 「アイテムリスト」（Item list）エリア
            
              - デフォルトはすべてのアイテムを表示する。
            
              - アイテムリストの表示順と表示数はWEKO3のアイテムリストをそのまま利用する。初期表示は「ID asc」の組み合わせが表示されているが、実際にはアイテムリストは「Creator asc」の順番で表示がされる。
            
              - 一括更新の対象選択ができるため、各アイテムの行頭にチェックボックスを設ける。  
                また、アイテムリストの上部に「全選択」（Select All）リンクを設けて、リンクをクリックすると、すべての表示されているアイテムは一括更新の対象とする。
            
              - アイテムの詳細を確認できるため、各アイテムがリンク形式で表示されて、リンクをクリックすると、該当アイテム詳細画面に移動する。

  - 一括更新を実行する
    
      - 一括更新の情報を設定してから、「更新」（Update）ボタンを押すと、事前確認できるため、更新内容を確認モーダルに表示する
    
      - 対象アイテムを選択しない状態で、「更新」（Update）ボタンを押すと  
        「Please select items to update.」
    
      - モーダルには以下を表示する
        
          - 「Item」：アイテムに登録しているファイル名
        
          - 「Before」
            
              - 「Access Type」：更新前のアクセスタイプ値
            
              - 「License」：更新前のライセンス値
        
          - 「After」
            
              - 「Access Type」：更新後のアクセスタイプ値
            
              - 「License」：更新後のライセンス値
        
          - 「Continue」ボタン  
            押すと、一括更新処理が行って、対応アイテムの情報とバージョンが更新される
        
          - 「閉じる」（Close）ボタン  
            押すと、モーダルを閉じる

<!-- end list -->

  - > 関連モジュール

weko\_records\_ui

  - 
  - > weko\_index\_tree

  - > weko\_records\_ui

<!-- end list -->

  - > 処理概要

> 一括更新画面表示について

  - > 【Administration \> アイテム管理(Items) \> 一括更新(Bulk Update)画面】を開いた際、以下の処理を実行する。
    
      - > weko\_index\_tree.rest.IndexTreeActionResource.getメソッドを呼び出し、インデックスツリー情報を取得する。それらを「インデックスツリー」エリアに表示する。
    
      - > weko\_records\_ui.admin. ItemManagementBulkUpdate.indexメソッドを呼び出す。詳細検索情報をget\_search\_detail\_keywordメソッドで、一括更新対象の設定をWEKO\_RECORDS\_UI\_BULK\_UPDATE\_FIELDSから (後述)、ライセンス情報をWEKO\_RECORDS\_UI\_LICENSE\_DICTから取得し、詳細検索情報と一括更新対象設定、ライセンス情報をそれぞれのエリアに表示する。

> 一括更新対象を設定する

  - パス：  
    <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py>

  - 設定キー：「WEKO\_RECORDS\_UI\_BULK\_UPDATE\_FIELDS」

  - 現在の設定値：

> WEKO\_RECORDS\_UI\_BULK\_UPDATE\_FIELDS = {
> 
> 'fields': \[{'id': '1', 'name': 'Access Type'},
> 
> {'id': '2', 'name': 'Licence'}\]
> 
> }
> 
> 一括更新画面にてインデックス検索、詳細検索、簡易検索のいずれかを行う。

  - > weko\_search\_ui.rest.IndexSearchResource.getメソッドを呼び出し、検索条件にのっとったアイテムの情報を取得し、表示する。

  - > weko\_search\_ui.admin.ItemManagementBulkSearch.indexメソッドを呼び出し、様々な情報を取得し、画面に表示する。詳細は以下のgithubを参照すること。ソースコード：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/admin.py>

> 一括更新の実行

  - > 「Item list」エリアのチェックボックスにチェックを入れないで「更新ボタン」を押した場合、weko\_records\_ui.static.js.weko\_records\_ui.bulk\_updateの135行目にてアラートが表示される処理が実行される。

  - > 更新をするアイテムにチェックを入れて「更新」ボタンを押下する。その場合、weko\_records\_ui.static.js.weko\_records\_ui.bulk\_updateの121行目からが呼び出され、それにてget\_items\_metadataメソッドが呼び出され、アイテムに所属するファイルの情報を取得し、before,afterのポップアップ画面が表示される。
    
      - > ポップアップ画面上の「閉じる」ボタンを押下すると、キャンセルされポップアップ画面は閉じる。
    
      - > 「Continue」ボタンを押下した場合、weko\_deposit.rest.publishメソッドが複数回呼ばれ、item\_metadataテーブル、item\_metadata\_versionテーブル、records\_metadataテーブルにそれぞれ更新内容を登録する。（アクセスタイプならキーaccessroleを、ライセンスならキーlicensetypeを変更して登録する。）

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
