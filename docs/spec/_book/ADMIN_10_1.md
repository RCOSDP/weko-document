### Resource List

<!-- end list -->

  - > 目的・用途

公開インデックスごとに「Resource List」、「Resource Dump」を出力する

  - > 利用方法

【Administration \> Resource Sync \> Resource List画面】にて操作を行う

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

  - Resource Listの仕様：   
    <http://www.openarchives.org/rs/1.1/resourcesync#ResourceList>

  - Resource List Indexの仕様：   
    <http://www.openarchives.org/rs/1.1/resourcesync#ResourceListIndex>

  - Resource Dumpの仕様：   
    <http://www.openarchives.org/rs/1.1/resourcesync#ResourceDump>

  - 【Resource List画面】には以下のタブが表示される
    
      - List
    
      - Create
    
      - Edit
        
          - > 「List」、「Create」タブ選択中は非表示
        
          - > 「List」タブでの操作によって表示される
        
          - 他のタブに移動すると非表示になる

  - 「List」タブにて存在するResourceを一覧表示する
    
      - 「List」タブを表示するたびに最新の情報を取得する
    
      - 表示項目は以下の通りである
        
          - アクション（編集・削除を表すアイコン）
        
          - Repository
            
              - そのResource Listが対象とするインデックス
            
              - フォーマット：「{インデックスの英語名} \<ID:インデックスID\>」
        
          - Resource List Url
            
              - 「Resource List」のURLを表示する
        
          - Resource Dump Url
            
              - 「Resource Dump」のURLを表示する
        
          - Status
            
              - Private/Publish

  - 「Create」タブにて「Resource List」、「Resource Dump」レコードを作成する
    
      - 入力情報は以下の通りである
        
          - Status
            
              - インデックスのステータスを選択する
            
              - ラジオボタン：Publish、Private
            
              - デフォルト：選択無し
        
          - Repository
        
          - > 対象とするインデックスを指定する
        
          - Resource Dump Manifest
            
              - Resource Dumpごとに「manifest.xml」ファイルを出力するかどうかを設定する
            
              - チェックが入っている場合に出力する
            
              - デフォルト：チェック無し
        
          - Resource List uri
            
              - 「Repository」で選択しているインデックスに応じて、「Resource List」のURIを自動的に表示する
            
              - テンプレートのURL：「https://{weko\_url}/resync/{Index ID}/resourcelist.xml」
            
              - 変更不可、無効の状態とする
        
          - Resource Dump uri
            
              - 「Repository」で選択しているインデックスに応じて、「Resource Dump」のURIを自動的に表示する
            
              - テンプレートのURL：「https://{weko\_url}/resync/{Index ID}/resourcedump.xml」
            
              - 変更不可、無効の状態とする
    
      - ［Create］ボタンを押すと、入力内容をチェックし、問題がなければ、「Resource List」レコードを作成し、「List」タブに移動する
        
          - エラーの場合は以下の通りである
            
              - 既に設定されたインデックスを選択している場合、以下のようなエラーメッセージを表示する  
                エラーメッセージ：「Selected repository has been registered already. Please select another repository.」
        
          - 「Status」がチェックなしのままでレコードを作成する場合は、Publishが設定される
    
      - ［Create and Add Another］ボタンを押すと、［Create］ボタンを押したときと同様の処理によって設定された内容のレコードを作成して、タブを移動せずに他の「Resource List」を作成可能とする
    
      - ［Cancel］ボタンを押すと、設定された「Resource List」を追加せずに、「List」タブに移動する

  - 公開インデックスごとに「Resource List」、「Resource Dump」を出力する
    
      - 「Status：Publish」の場合、「Resource List」及び「Resource Dump」を出力する
    
      - 「Resource List」を出力する
        
          - 「List」タブにて「Resource List Url」列のURLを押すと、該当する「Resource List」を出力して、ブラウザで表示する
            
              - 「Resource List」の表示項目は以下の通りである
                
                  - 表示フォーマット：XML
                
                  - 「capability.xml」のURL
                
                  - Capabilityのタイプ：resourcelist
                
                  - 該当インデックスに属するアイテム一覧
                    
                      - \<loc\>：アイテムのURL
                    
                      - \<lastmod\>：アイテムの更新日付。フォーマット：YYYY-MM-DDThh:mm:ss.ttttttZ
        
          - 「Resource List」のサンプル

> **\<urlset** xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:rs="http://www.openarchives.org/rs/terms/"**\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/capability.xml" rel="up"**/\>**
> 
> **\<rs:md** capability="resourcelist"**/\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/records/29**\</loc\>**
> 
> **\<lastmod\>**2020-07-14T10:27:28.329486Z**\</lastmod\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/records/30**\</loc\>**
> 
> **\<lastmod\>**2020-07-14T08:06:35.785168Z**\</lastmod\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/records/32**\</loc\>**
> 
> **\<lastmod\>**2020-07-14T08:30:04.372277Z**\</lastmod\>**
> 
> **\</url\>**
> 
> **\</urlset\>**

  - 「Resource Dump」を出力する
    
      - 「List」タブにて「Resource Dump Url」列のURLを押すと、該当する「Resource Dump」を出力して、ブラウザで表示する
        
          - 「Resource Dump」の表示項目は以下の通りである
            
              - 表示フォーマット：XML
            
              - 「capability.xml」のURL
            
              - Capabilityのタイプ：resourcedump
            
              - 該当インデックスに属するアイテム一覧
            
              - > \<loc\>：該当インデックスに属されるアイテムに登録されているファイルのZipパッケージのURL
            
              - > \<lastmod\>：アイテムの更新日付。フォーマット：YYYY-MM-DDThh:mm:ss.ttttttZ
            
              - > 該当「resource Dump Manifest」のURL(「Resource Dump」詳細画面での設定に応じて表示する)
    
      - 「Resource Dump」のサンプル

> **\<urlset** xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:rs="http://www.openarchives.org/rs/terms/"**\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/capability.xml" rel="up"**/\>**
> 
> **\<rs:md** capability="resourcedump"**/\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/29/file\_content.zip**\</loc\>**
> 
> **\<lastmod\>**2020-07-14T10:27:28.329486Z**\</lastmod\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/1594710457918/29/resourcedump\_manifest.xml" rel="contents" type="application/xml"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/30/file\_content.zip**\</loc\>**
> 
> **\<lastmod\>**2020-07-14T08:06:35.785168Z**\</lastmod\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/1594710457918/30/resourcedump\_manifest.xml" rel="contents" type="application/xml"**/\>**
> 
> **\</url\>**
> 
> **\<url\>**
> 
> **\<loc\>**https://18.182.214.241:8024/resync/1594710457918/32/file\_content.zip**\</loc\>**
> 
> **\<lastmod\>**2020-07-14T08:30:04.372277Z**\</lastmod\>**
> 
> **\<rs:ln** href="https://18.182.214.241:8024/resync/1594710457918/32/resourcedump\_manifest.xml" rel="contents" type="application/xml"**/\>**
> 
> **\</url\>**
> 
> **\</urlset\>**

  - 「Status：Private」の場合、または対象インデックスが「公開しない」と設定する場合、「Resource List」及び「Resource Dump」を出力すると、以下のようなエラーメッセージを表示する  
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

  - Resource Sync処理実行時、テンポラリディレクトリのファイル名を以下のように設定する
    
      - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_resync\_xxxxxxxx

  - 以下のopenarchivesのサイトにSource Descriptionの仕様を確認できる
    
      - <http://www.openarchives.org/rs/1.1/resourcesync#SourceDesc>

  - WEKOには、以下の機能に対応している
    
      - Resource List:
        
          - 参照リンク: <http://www.openarchives.org/rs/1.1/resourcesync#ResourceList>
    
      - Change List:
        
          - 参照リンク: <http://www.openarchives.org/rs/1.1/resourcesync#ChangeList>
    
      - Resync: Resource ListとChange Listから構成され、ハーベスト機能と同じ。他のサイトからの情報を取得し登録する。

  - 本画面では、resourcelist\_indexesテーブルの情報を閲覧、作成、編集、削除する
    
      - 画面表示時に、invenio\_resourcesyncserver.admin.AdminResourceListView.indexメソッドによってテンプレートを指定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py#L21>
        
          - 設定キー：INVENIO\_RESOURCESYNCSERVER\_ADMIN\_TEMPLATE
    
      - 「List」タブの表示時に、同クラスのget\_listメソッドによってテーブルの情報を全件取得する
        
          - 画面の「Resource List Url」と「Resource Dump Url」の表示内容は、内容の表示時にresource.js中でそれぞれ「url\_path」フィールドの値に「/resourcelist.xml」「/resourcedump.xml」を結合して作成している
        
          - 「status」フィールドは真偽値であるが、内容の表示時にresource.js中でフィールドの値によって「Publish」か「Private」を表示するようにしている
    
      - 「Create」タブで［Create］ボタンを押したとき、同クラスのcreateメソッドによって、テーブルに対象インデックスについてのレコードがない場合に、新たにレコードを作成する
        
          - 対象インデックスについてのレコードがすでにあった場合には、作成せずに以下のコンフィグで指定されたメッセージを返す
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py#L44-L45>
            
              - 設定キー：VALIDATE\_MESSAGE
    
      - 「Edit」タブで［Save］ボタンを押したとき、同クラスのupdateメソッドによってレコードを更新する
    
      - 「List」タブでごみ箱アイコンを押したとき、同クラスのdeleteメソッドによってレコードを物理削除する

  - 公開インデックスごとに「Resource List」、「Resource Dump」を出力する
    
      - 「Resource List」を出力する
        
          - 「List」タブにて「Resource List Url」列のURLを押すと、invenio\_resourcesyncserver.views.resource\_list関数が呼び出される
            
              - この中で、invenio\_resourcesyncserver.api.ResourceListHandler. get\_resource\_list\_xmlメソッドによってresourcelist.xmlを出力する
    
      - 「Resource Dump」を出力する
        
          - 「List」タブにて「Resource Dump Url」列のURLを押すと、invenio\_resourcesyncserver.views.resource\_dump関数が呼び出される
            
              - この中で、invenio\_resourcesyncserver.api.ResourceListHandler. get\_resource\_dump\_xmlメソッドによってresourcedump.xmlを出力する

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