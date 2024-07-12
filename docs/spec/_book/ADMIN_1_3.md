

### OAIスキーマ

  - > 目的・用途

<!-- end list -->

  - > 利用方法

【Administration \> アイテムタイプ管理（Item Types） \> OAIスキーマ（OAI Schema）画面】にて操作する。

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

  - ［Add Schema］ボタンを押すと、アップロード画面が表示される。必要情報を入力して［保存］ボタンを押すことで、以下のスキーマとの関連付けを設定できる。
    
      - JPCOAR
    
      - JPCOAR v1
    
      - JPCOAR v2
    
      - Dublin Core
    
      - DDI
    
      - lom

  - 設定内容は以下の通りである
    
      - スキーマファイル：必須項目  
        スキーマを定義したxsdファイル、またはそれを圧縮したzipファイルをアップロードする。  
        複数ファイルをアップロードできるが、新規設定処理に使用するのは「File Name」で指定された名前のファイルのみである。
    
      - File Name：必須項目  
        アップロードしたxsdファイルのファイル名を１つだけ入力する。  
        入力値の末尾に「.xsd」がない場合、末尾に「.xsd」を加えた文字列を使用する。
    
      - Schema Name：画面では必須項目と表示されるが、処理上は必須ではない  
        OAI-PMH出力ができるように、以下のようなスキーマ名を設定する必要がある。  
        画面で入力せずに［保存］ボタンを押すと、かわりに「Root Name」の入力値を使用する。また、使用する値の末尾に「\_mapping」がない場合、末尾に「\_mapping」を加えた文字列を使用する。
        
          - Dublin Coreスキーマ：「oai\_dc」
        
          - JPCOARスキーマ：「jpcoar」
        
          - JPCOAR v1スキーマ：「jpcoar\_v1l
        
          - JPCOAR v1スキーマ：「jpcoar\_v2l
        
          - omスキーマ：「lom」
    
      - Root Name：必須項目  
        OAI-PMH出力ができるように、以下のようなルート名を設定する必要がある。  
        入力値は、「Schema Name」の入力値がない場合に使用するほか、oaiserver\_schemaテーブルのnamespacesカラム、target\_namespaceカラムの内容を作成するために使用する。
        
          - Dublin Coreスキーマ：「dc」
        
          - JPCOARスキーマ：「jpcoar」
        
          - JPCOAR v1スキーマ：「jpcoarlomスキーマ：「lom」
    
      - Zip Name  
        アップロードファイルのフォーマットがzipファイルの場合、必須項目になる。  
        末尾が「.zip」である入力値が存在する場合に限り、ここで入力したzipファイル名を用いて、zipファイルを展開する。
    
      - Schema Location  
        参考情報として、スキーマが定義されているURLを入力する。
    
      - Comment  
        コメント

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko-schema-ui

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 全ての設定はconfig.pyに定義される。
    
      - <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-schema-ui/weko_schema_ui/config.py>

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
<tr class="even">
<td><blockquote>
<p>2022/11/11</p>
</blockquote></td>
<td>V0.9.27</td>
<td></td>
</tr>
</tbody>
</table>
