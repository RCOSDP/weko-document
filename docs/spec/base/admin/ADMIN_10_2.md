### Change List

  - > 目的・用途

公開インデックスごとに「Change List」、「Change Dump」を出力する

  - > 利用方法

【Administration \> Resource Sync \> Change List画面】で操作を行う

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

  - Change Listの仕様： <http://www.openarchives.org/rs/1.1/resourcesync#ChangeList>

  - Change Dumpの仕様： <http://www.openarchives.org/rs/1.1/resourcesync#ChangeDump>

  - 【Change List画面】で表示されるタブは、【Resource List画面】と同様である。[ADMIN-10-1: Resource List](\\l)を参照すること

  - 「List」タブにて存在するChange Listを一覧表示する
    
      - 「List」タブを表示するたびに最新の情報を取得する
    
      - 表示項目は以下の通りである
        
          - アクション（編集・削除を表すアイコン）
        
          - Repository
            
              - そのChange Listが対象とするインデックス
            
              - フォーマット：「{インデックスの英語名} \<ID:インデックスID\>」
        
          - Change List Url
            
              - 「Change List」のURLを表示する
        
          - Change Dump Url
            
              - 「Change Dump」のURLを表示する
        
          - Status
            
              - Private/Publish

  - 「Create」タブにて「Change List」、「Change Dump」レコードを作成する
    
      - 入力情報は以下の通りである
        
          - Status
            
              - インデックスのステータスを選択する
            
              - ラジオボタン：Publish、Private
            
              - デフォルト：選択無し
        
          - Repository
            
              - 対象とするインデックスを指定する
        
          - Publish date
            
              - フォーマット：MM/DD/YYYY
            
              - デフォルト：当日
        
          - Max change list
            
              - デフォルト：10000
        
          - Interval by date
            
              - 自動実行する日間隔を設定する
            
              - デフォルト：1
        
          - Change tracking state
            
              - チェックボックス：Created、Updated、Deleted
            
              - デフォルト：すべてのチェックボックスにチェックを入れる
        
          - Change dump manifest
            
              - 「Change Dump」ごとに「manifest.xml」ファイルを出力するかどうかを設定する
            
              - デフォルト：チェック無し
        
          - Change List uri
            
              - 「Repository」で選択しているインデックスに応じて、「Change List」のURIを自動的に表示する
            
              - テンプレートのURL：「https://{weko\_url}/resync/{Index ID}/changelist.xml」
            
              - 変更不可、無効の状態とする
        
          - Change Dump uri
            
              - 「Repository」で選択しているインデックスに応じて、「Change Dump」のURIを自動的に表示する
            
              - テンプレートのURL：「https://{weko\_url}/resync/{Index ID}/changedump.xml」
            
              - 変更不可、無効の状態とする
    
      - ［Create］ボタンを押すと、入力内容をチェックし、問題がなければ、「Change List」のレコードを作成し、「List」タブに移動する
        
          - エラーの場合は以下の通りである
            
              - 既に設定されたインデックスを選択している場合、以下のようなエラーメッセージを表示する  
                エラーメッセージ：「Selected repository has been registered already. Please select another repository.」
        
          - 「Status」がチェックなしのままでレコードを作成する場合は、Privateが設定される
    
      - ［Create and Add Another］ボタンを押すと、［Create］ボタンを押したときと同様の処理によって設定された内容のレコードを作成して、タブを移動せずに他の「Change List」を作成可能とする
    
      - ［Cancel］ボタンを押すと、設定された「Change List」を追加せずに、「List」タブに移動する

  - 公開インデックスごとに「Change List」、「Change Dump」を出力する
    
      - 「Status：Publish」の場合、「Change List」及び「Change Dump」を出力する
        
          - 「Change List」を出力する
            
              - 「List」タブより「Change List Url」列でのURLを押すと、ブラウザで該当する「Change List」を表示する
            
              - 「Change List」の表示項目は以下の通りである
                
                  - 表示フォーマット：XML
                
                  - 「capability.xml」のURL
                
                  - Capabilityのタイプ：changelist
                
                  - 該当インデックスに属される更新済みアイテム一覧の「Change List」
                    
                      - 日ごとにアイテムをまとめる
                    
                      - テンプレートのURL：「https://{weko\_url}/resync/{Index ID}/{YYYYMMDD}/changelist.xml」
                
                  - from-until：「Change List」ごとに対象日
                    
                      - フォーマット：YYYY-MM-DDThh:mm:ssZ
            
              - 「Change List一覧」のサンプル

> **\<urlset** xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:rs="http://www.openarchives.org/rs/terms/"**\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/capability.xml" rel="up"**/\>**
> 
> **\<rs:md** capability="changelist"**/\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200717/changelist.xml**\</loc\>**
> 
> **\<rs:md** capability="changelist" from="2020-07-17T00:00:00Z" until="2020-07-18T00:00:00Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200718/changelist.xml**\</loc\>**
> 
> **\<rs:md** capability="changelist" from="2020-07-18T00:00:00Z" until="2020-07-19T00:00:00Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200719/changelist.xml**\</loc\>**
> 
> **\<rs:md** capability="changelist" from="2020-07-19T00:00:00Z" until="2020-07-20T00:00:00Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200720/changelist.xml**\</loc\>**
> 
> **\<rs:md** capability="changelist" from="2020-07-20T00:00:00Z" until="2020-07-20T08:59:58.606915Z"**/\>**
> 
> **\</url\>**
> 
> **\</urlset\>**

  - 「Change List」を出力する  
    出力された「Change List一覧」より、日ごとの「Change List」を出力する
    
      - 「Change List」に表示項目は以下の通りである
        
          - 表示フォーマット：XML
        
          - 「capability」のURL
        
          - 属される「Change List一覧」のURL
        
          - Capabilityのタイプ：changelist
        
          - アイテムに登録されているファイルのURL
        
          - \<lastmod\>：アイテムの更新日付
        
          - 「change」タイプ：created、updated、deleted
    
      - 「Change List」のサンプル

> **\<urlset** xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:rs="http://www.openarchives.org/rs/terms/"**\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/capability.xml" rel="up"**/\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/1594710457918/changelist.xml" rel="index"**/\>**
> 
> **\<rs:md** capability="changelist"**/\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/records/55**\</loc\>**
> 
> **\<lastmod\>**2020-07-22T01:17:12.177328Z**\</lastmod\>**
> 
> **\<rs:md** at="2020-07-22T01:17:12.177328Z" change="created"**/\>**
> 
> **\</url\>**
> 
> **\</urlset\>**

  - 「Change Dump一覧」を出力する
    
      - 「Change List」の「List」タブより「Change Dump Url」列でのURLを押すと、該当する「Change Dump一覧」にアクセスする
    
      - 「Change Dump一覧」に表示項目は以下の通りである
        
          - 表示フォーマット：XML
        
          - 「capability」のURL
        
          - Capabilityのタイプ：changedump
        
          - 該当インデックスに属されるアイテムのZipパッケージにアクセスできる「Change Dump」
            
              - 日ごとにアイテムをまとめる
            
              - テンプレートのURL：「https://{weko\_url}/resync/{Index ID}/{YYYYMMDD}/changelist.xml」
        
          - from-until：「Change Dump」ごとに対象日
            
              - フォーマット：YYYY-MM-DDThh:mm:ssZ
    
      - 「Change Dump一覧」のサンプル

> **\<urlset** xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:rs="http://www.openarchives.org/rs/terms/"**\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/capability.xml" rel="up"**/\>**
> 
> **\<rs:md** capability="changedump"**/\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200717/changedump.xml**\</loc\>**
> 
> **\<rs:md** capability="changedump" from="2020-07-17T00:00:00Z" until="2020-07-18T00:00:00Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200718/changedump.xml**\</loc\>**
> 
> **\<rs:md** capability="changedump" from="2020-07-18T00:00:00Z" until="2020-07-19T00:00:00Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200719/changedump.xml**\</loc\>**
> 
> **\<rs:md** capability="changedump" from="2020-07-19T00:00:00Z" until="2020-07-20T00:00:00Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/20200720/changedump.xml**\</loc\>**
> 
> **\<rs:md** capability="changedump" from="2020-07-20T00:00:00Z" until="2020-07-20T09:01:55.926748Z"**/\>**
> 
> **\</url\>**
> 
> **\</urlset\>**

  - 「Change Dump」を出力する  
    出力された「Change Dump一覧」より、日ごとの「Change Dump」を出力する
    
      - 「Change Dump」に表示項目は以下の通りである
        
          - 表示フォーマット：XML
        
          - 「capability」のURL
        
          - 属される「Change Dump一覧」のURL
        
          - Capabilityのタイプ：changedump
        
          - アイテムに登録されているファイルのZipパッケージのURL
        
          - \<lastmod\>：アイテムの更新日付
    
      - 「Change Dump」のサンプル

> **\<urlset** xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:rs="http://www.openarchives.org/rs/terms/"**\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/capability.xml" rel="up"**/\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/1594710457918/changedump.xml" rel="index"**/\>**
> 
> **\<rs:md** capability="changedump"**/\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/49.1/change\_dump\_content.zip**\</loc\>**
> 
> **\<lastmod\>**2020-07-21T03:47:43.254174Z**\</lastmod\>**
> 
> **\<rs:md** from="2020-07-21T03:47:43.254174Z" type="application/zip" until="2020-07-21T05:44:21.697630Z"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/50.1/change\_dump\_content.zip**\</loc\>**
> 
> **\<lastmod\>**2020-07-21T05:43:05.066272Z**\</lastmod\>**
> 
> **\<rs:md** from="2020-07-21T05:43:05.066272Z" type="application/zip" until="2020-07-21T05:44:21.698327Z"**/\>**
> 
> **\</url\>**
> 
> **\</urlset\>**

  - 「Status：Private」の場合、、または対象インデックスが「公開しない」と設定する場合、「Change List」及び「Change Dump」を出力すると、以下のようなエラーメッセージを表示する  
    エラーメッセージ：  
    　　　　　　　JP：「ページが見つかりません。」  
    　　　　　　　EN：「Page not found」

<!-- end list -->

  - 「List」タブ各行の鉛筆アイコンをクリックすると、「Edit」タブに移動してその行のレコードを表示し、内容を編集できる
    
      - 入力情報は、「Create」タブと同じである
    
      - ［Save］ボタンを押すと、編集内容を保存して「List」タブに移動する
    
      - ［Cancel］ボタンを押すと、編集内容を保存せず「List」タブに移動する

  - 「List」タブ各行のごみ箱アイコンをクリックすると、確認ダイアログを表示する  
    メッセージ：「Are you sure to delete it ?」
    
      - ［OK］ボタンを押すと、該当レコードを削除する
    
      - ［キャンセル］ボタンを押すと、確認ダイアログを閉じる

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_resourcesyncserver

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 本画面では、changelist\_indexesテーブルの情報を閲覧、作成、編集、削除する
    
      - 画面表示時に、invenio\_resourcesyncserver.admin.AdminChangeListView.indexメソッドによってテンプレートを指定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py#L25>
        
          - 設定キー：INVENIO\_RESOURCESYNC\_CHANGE\_LIST\_ADMIN
    
      - 「List」タブの表示時に、同クラスのget\_listメソッドによってテーブルの情報を全件取得する
        
          - 画面の「Change List Url」と「Change Dump Url」の表示内容は、内容の表示時にchange\_list.js中でそれぞれ「url\_path」フィールドの値に「/changelist.xml」「/changedump.xml」を結合して作成している
        
          - 「status」フィールドは真偽値であるが、内容の表示時にchange\_list.js中でフィールドの値によって「Publish」か「Private」を表示するようにしている
    
      - 「Create」タブで［Create］ボタンを押したとき、同クラスのcreateメソッドによって、テーブルに対象インデックスについてのレコードがない場合に、新たにレコードを作成する
        
          - 対象インデックスについてのレコードがすでにあった場合には、作成せずに以下のコンフィグで指定されたメッセージを返す
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py#L44-L45>
            
              - 設定キー：VALIDATE\_MESSAGE
    
      - 「Edit」タブで［Save］ボタンを押したとき、同クラスのupdateメソッドによってレコードを更新する
    
      - 「List」タブでごみ箱アイコンを押したとき、同クラスのdeleteメソッドによってレコードを物理削除する

  - 公開インデックスごとに「Change List」、「Change Dump」を出力する
    
      - 「Change List」を出力する
        
          - 「List」タブにて「Change List Url」列のURLを押すと、invenio\_resourcesyncserver.views. change\_list\_index関数が呼び出される
            
              - この中で、invenio\_resourcesyncserver.api. ChangeListHandler. get\_change\_list\_indexメソッドによってchangelist.xmlを出力する
    
      - 「Change Dump」を出力する
        
          - 「List」タブにて「Change Dump Url」列のURLを押すと、invenio\_resourcesyncserver.views. change\_dump\_index関数が呼び出される
            
              - この中で、invenio\_resourcesyncserver.api. ChangeListHandler. get\_change\_dump\_indexメソッドによってchangedump.xmlを出力する

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

##   
