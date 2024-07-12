
### エクスポート

  - > 目的・用途

本機能は、アイテム詳細画面から特定のアイテムの情報を設定されたスキーマ形式に出力する機能である。

  - > 利用方法

エクスポートは、アイテム詳細画面の右下にあるOAI-PMH, BIBTEX, JSONのボタンを押下することで、アイテムの情報がスキーマ形式に出力される。

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
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
</tr>
</tbody>
</table>

  - > 機能内容

1\. OAI-PMHスキーマを管理

  - 【Administration \> アイテムタイプ管理 (Item Types) \> OAIスキーマ (OAI Schema)\> 作成画面】にOAI-PMHスキーマを設定できる  
    設定内容は以下の通りである
    
      - スキーマファイルをアップロードする。必須項目
        
          - DublinCore : 別紙の「oai\_dc」を参照。
        
          - JPCOAR：(<https://github.com/JPCOAR/schema/blob/master/1.0/jpcoar_scm.xsd>)  
            (<https://github.com/JPCOAR/schema/blob/master/2.0/jpcoar_scm.xsd>)
        
          - DDI : 別紙の「ddi\_2\_5\_1.zip」を参照。
    
      - ファイル名（File Name）。必須項目  
        アップロードされたスキーマファイルのファイル名を設定する
    
      - スキーマ名（Schema Name）。必須項目  
        OAI-PMH出力ができるため、以下のようなスキーマ名を設定する必要がある
        
          - DublinCoreスキーマ：「oai\_dc」
        
          - JPCOARスキーマ：「jpcoar\_1.0」
        
          - DDIスキーマ：「ddi」
    
      - ルート名（Root Name）。必須項目  
        OAI-PMH出力ができるため、以下のようなルート名を設定する必要がある
        
          - DublinCoreスキーマ：「dc」
        
          - JPCOARスキーマ：「jpcoar\_1.0」
        
          - DDIスキーマ：「codeBook」
    
      - ジップ名（Zip Name）  
        アップロードファイルのフォーマットはzipファイルの場合、必須項目になり、zipファイル名を入れる
    
      - スキーマロケーション（Schema Location）  
        スキーマの参照ロケーションを入れる
    
      - コメント（Comment）

2\. OAI-PMHスキーマをマッピング

  - 【Administration \>アイテムタイプ管理 ( Item Types) \>マッピング (Mapping)画面】：作成されたOAI-PMHスキーマにマッピングを実施
    
      - システムが付与する情報  
        「システムが付与したアイテムタイプ (親)」領域でWEKOでのシステム操作を介して作成されるデータをマッピング可能とする  
        対象データは、以下とする
        
          - 永続識別子（DOI）  
            https://schema.irdb.nii.ac.jp/ja/schema/17
        
          - 永続識別子（HDL）  
            <https://schema.irdb.nii.ac.jp/ja/schema/17>
        
          - 永続識別子（URI）  
            <https://schema.irdb.nii.ac.jp/ja/schema/17>
        
          - ファイル情報  
            <https://schema.irdb.nii.ac.jp/ja/schema/35>  
              
            updatedの日付のマッピングは、Getrecord、ListRecord、ListIdentifierのheaderにおいて、「datestamp=record.updated,」が使用されており、invenio\_records.api.get\_recordからDBのupdatedを取得している。  
              
            jpcoarスキーマガイドラインに記載されている以下の項目は不要となる
            
              - datacite:date dateType="Created"
            
              - datacite:date dateType="Updated"
    
      - アイテムタイプのメタデータ  
        「アイテムタイプ(親)」領域でアイテムタイプのメタデータをマッピング可能とする
        
          - DDI : 別紙「USER3-7\>DDIハーベスト規格ver2\_2019120」を参照。
        
          - [JPCOAR](https://support.irdb.nii.ac.jp/sites/default/files/2018-08/mapping_jpcoar_v1.0.1_1.pdf) (<https://support.irdb.nii.ac.jp/sites/default/files/2018-08/mapping_jpcoar_v1.0.1_1.pdf>)

3\. OAI-PMHのプロバイダ機能の有効・無効をインデックスごとに設定可能

  - 【Administration \> インデックスツリー管理 (Index Tree)\>ツリー編集 (Edit Tree)画面】での「ハーベスト公開 (Harvest Publish)」領域でインデックスごとにハーベスト公開制御を設定可能
    
      - 「公開する」（Open to public）チェックボックスにチェックを入れる場合、ハーベスト公開が有効になる  
        当該インデックス配下のアイテムについて、 OAI-PMHの出力を可能とする
        
          - OAI-PMHリクエスト（GetRecord）に対して、OAI-PMHの正常レスポンスを返す
        
          - アイテム詳細画面の「OAI-PMH」領域でのボタン押下に対して、OAI-PMHの正常レスポンスを返す
    
      - 「公開する」（Open to public）チェックボックスにチェックをはずす場合、ハーベスト公開が無効になる  
        当該インデックス配下のアイテムについて、 OAI-PMHの出力を不可とする
        
          - OAI-PMHリクエスト（GetRecord）に対して、OAI-PMHの「idDoesNotExist」エラーレスポンスを返す
        
          - アイテム詳細画面の「OAI-PMH」ボタン押下に対して、OAI-PMHの「idDoesNotExist」エラーレスポンスを返す
    
      - OAI-PMH機能の有効・無効の切り替え条件  
        リポジトリ管理者およびシステム管理者が切り替え可能。コミュニティ管理者は、コミュニティオーナーとなっている管理対象インデックスのみ切り替え可能。

<table>
<thead>
<tr class="header">
<th><strong>Verb</strong></th>
<th>WEKO3<br />
（oaiserver_identifyレコードなし)</th>
<th><strong>WEKO3<br />
</strong>（outPutSetting = f)</th>
<th><strong>WEKO3<br />
</strong>（outPutSetting = T)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>GetRecord</strong></td>
<td>出力なし<br />
（noRecordsMatch）</td>
<td><strong>出力</strong>なし<br />
（noRecordsMatch）</td>
<td><strong>出力</strong></td>
</tr>
<tr class="even">
<td><strong>ListRecords</strong></td>
<td>出力<strong>なし<br />
</strong>（noRecordsMatch）</td>
<td>出力なし（noRecordsMatch） ​</td>
<td><strong>出力</strong></td>
</tr>
<tr class="odd">
<td><strong>ListIdentifiers</strong></td>
<td>出力なし<br />
（noRecordsMatch）</td>
<td>出力なし<br />
（noRecordsMatch）</td>
<td>出力</td>
</tr>
<tr class="even">
<td><strong>ListMetadataFormats</strong></td>
<td><strong>出力</strong></td>
<td><strong>出力</strong></td>
<td><strong>出力</strong></td>
</tr>
<tr class="odd">
<td><strong>ListSets</strong></td>
<td>出力†</td>
<td>出力†</td>
<td><strong>出力</strong></td>
</tr>
<tr class="even">
<td><strong>Identify</strong></td>
<td><strong>出力</strong></td>
<td><strong>出力</strong></td>
<td><strong>出力</strong></td>
</tr>
</tbody>
</table>

※非公開状態にある**アイテム**は出力しない  
†ただし、非公開インデックス（非公開、OAI-PMH非公開）は出力しない

4\. アイテムのメタデータをOAI-PMH出力

  - 【前提条件】  
    「3.1. OAI-PMHスキーマを管理」及び「3.2. OAI-PMHスキーマをマッピング」が設定済み

  - 対応しているOAI-PMHスキーマ
    
      - JPCOAR
    
      - DDI
    
      - DublinCore

  - アイテム詳細画面での「OAI-PMH」領域にOAI-PMHスキーマボタンを押すと、該当フォーマットとしてアイテムのメタデータをOAI-PMH出力する
    
      - OAI-PMHの要求リクエストでエラーまたは例外状況が発生した場合に下記のOAI-PMHエラーを返せる  
        「3.6 エラーと例外状況 」(<https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/OpenArchivesProtocol.htm#ErrorConditions>)  
        ※DDIマッピングがない場合のエラーコード修正は以下の様に設定されている。  
        <https://github.com/RCOSDP/weko/blob/0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py#L207-L212>
    
      - 公開／非公開インデックスに属するアイテムのOAI-PMHの出力を制御する
        
          - アイテムが非公開の場合はdelete情報を出力する
        
          - アイテムが非公開インデックスにのみ属している場合は、アイテムが公開でも非公開でもdelete情報を出力する
        
          - アイテムが非公開インデックスと公開インデックスの両方に属している場合は、delete情報は出力しない（アイテムが公開の場合）
    
      - DOI有無での出力条件  
        インデックスの設定について、  
        ・「公開する」にチェックがついている、かつ「公開日が未来の日付」である  
        ・「ハーベスト公開」の「公開する」にチェックがついている  
        上記の条件を満たすとき、OAI-PMH出力は以下のように対応する。
        
          - アイテムにDOI付与がある場合  
            OAI-PMH出力しない  
            ListRecordsではrecordを出力しない  
            GetRecordではnoRecordsMatchを出力する
        
          - アイテムにDOI付与が無い場合  
            削除レコードを出力する  
            ListRecords、GetRecordでは\<header status="deleted"\>を出力する
    
      - 項目が複数登録される場合、DDIスキーマでの「titl」以外、繰り返し出力する
    
      - JPCOARのOAI-PMH出力にて、定められた統制語彙でない値が設定されている項目は対象外とする
        
          - 対象項目：以下の項目の属性「nameIdentifierScheme」の値
            
              - 作成者識別子（jpcoar:creator -\> jpcoar:nameIdentifier）
            
              - 寄与者識別子（jpcoar:contributor -\> jpcoar:nameIdentifier）
            
              - 権利者識別子（jpcoar:rightsHolder -\> jpcoar:nameIdentifier）
        
          - 定められた統制語彙は以下のリンクを参照する  
            <https://schema.irdb.nii.ac.jp/en/schema>
    
      - identifierTypeに関して、JPCOARのOAI-PMH出力では以下の通りに出力をする（※最大で3つ（URI、HDL、DOI）、最小で1つ（URIのみ）のidentifierが出力される）
        
          - URI（必ず存在する。https://FQDN/records/item\_id）：　"identifierType=URI" として出力する
        
          - HDLが存在する場合：　"identifierType=HDL" として出力する
        
          - DOIが存在する場合：　"identifierType=DOI" として出力する
    
      - DDIのOAI-PMH出力にて、親タグが言語ごとに繰返し出力できる
        
          - 対応している親タグ
            
              - 「stdyDscr\>citation」
            
              - 「stdyDscr\>stdyInfo」
            
              - 「stdyDscr\>method」
            
              - 「stdyDscr\>dataAccs」
            
              - 「stdyDscr\>othrStdyMat」
        
          - 「citation」親タグに対して出力を以下のように制限する
            
              - 「citation\>titlStmt\>titl」が繰り返し不可により、同一言語にtitlの値が複数定義される場合、最初に出るtitlを出力する
            
              - 「citation\>titlStmt\>titl」が必須項目により、titlの値が無い場合は取得する最初のtitlを設定する
            
              - 「citation\>rspStmt\>AuthEnty」にて「ja-kana」の言語を選択する場合、jaの扱いとして出力する
        
          - DDIスキーマにOAI-PMH出力構築  
            <https://ddialliance.org/sites/default/files/ddi-lite.html>

  - 以下のハーベスト出力条件に従って出力する
    
      - インデックスの公開／非公開、ハーベスト設定のON/OFFの設定は、アイテムが直接紐づいているインデックスとその上位のインデックスについても対象とする
    
      - 複数のインデックスに所属する場合、インデックスの公開が優先される。
    
      - 複数のインデックスに所属する場合、ハーベスト設定のOFFが優先される。

  - インデックス状態によるアイテム公開制御仕様：  
    別紙「ItemACL\_latest.xlsx」を参照。

  - アイテムの公開日について、以下の制御を行う
    
      - Administration \> ItemTypes \> Metadata でアイテムタイプの"公開日"の「Hide」オプションがON（非表示とする）の場合、アイテムの「公開日」はOAI-PMH出力しない
    
      - Admin \> ItemTypes \> Metadata でアイテムタイプの"公開日"の「Hide」オプションがOFF（表示する）の場合、アイテムの「公開日」をOAI-PMHに出力する

  - 公開日が未来日のアイテムに関しては以下の制御を行う
    
      - アイテムの公開日が未来日の場合
        
          - アイテムにDOI付与がある場合
            
              - OAI-PMH出力しない
            
              - ListRecordsではrecordを出力しない
            
              - GetRecordではidDoesNotExistを出力する
        
          - アイテムにDOI付与が無い場合
            
              - 削除レコードを出力する
            
              - ListRecords、GetRecordでは\<header status="deleted"\>を出力する
    
      - インデックスについて、以下の場合  
        　・「公開する」にチェックがついている、かつ「公開日が未来の日付」である  
        　・「ハーベスト公開」の「公開する」にチェックがついている
        
          - アイテムにDOI付与がある場合
            
              - OAI-PMH出力しない
            
              - ListRecordsではrecordを出力しない
            
              - GetRecordではidDoesNotExistを出力する
        
          - アイテムにDOI付与が無い場合
            
              - 削除レコードを出力する
            
              - ListRecords、GetRecordでは\<header status="deleted"\>を出力する

  - 親インデックスが非公開または公開日が未来の日付の場合のとき、非ログイン状態で以下の挙動をする
    
      - アイテム詳細画面やコンテンツファイルのURLに直接アクセスすると、ログイン画面に遷移する
    
      - OAI-PMHで\<header status="deleted"\>を出力する（DOIが付与されていない場合）
    
      - OAI-PMHのGetRecordでidDoesNotExistを出力する（DOIが付与されている場合）
    
      - ランキング表示で、当該インデックスのみに紐づいたアイテムは表示しない
    
      - 新着情報やインデックスのRSSで、当該インデックスのみに紐づいたアイテムは表示されない

5\. Sets

  - インデックス単位でのOAI-PMHによるSet提供ができる  
    当該Setには当該インデックスの下位のインデックスも含む

  - 【Administaration\>インデックスツリー編集 (Index Tree) \> Edit Tree画面】にて公開のインデックスを追加/更新/削除するとSetsの情報も自動的に反映される

  - 【Administration \> OAI-PMH \> Sets画面】でのSetsの設定が可能
    
      - Created: Sets 情報作成日時
    
      - Updated: Sets 情報更新日時
    
      - id: Sets 情報のID（システム設定)
    
      - Spec: インデックスパス ※パスの区切りは:(コロン)  
        例 1628576973067:1628576975817
    
      - Name: Sets 情報の名前(システムインデックス名)
    
      - Description: 概要
    
      - Search Pattern: 検索パターン ※パスの区切りは/(スラッシュ)  
        例 path:"1628576973067/1628576975817"

6\. Other Formats

  - アイテム詳細画面の「Other Formats」で以下の形式でアイテム情報を出力できる
    
      - > JSON
        
          - > アイテムのメタデータをJSON形式でエクスポートする。
        
          - > アイテム詳細画面のエクスポートエリアに表示されているJSONリンクを押下する。/records/\<item\_id\>/export/json
        
          - > 表示例は別紙「JSON出力例.txt」を参照。
        
          - > 設定
            
              - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L198-L202>
            
              - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records-rest/invenio_records_rest/serializers/__init__.py#L17>
        
          - > シリアライザ：
            
              - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records-rest/invenio_records_rest/serializers/json.py#L70>
    
      - > BIBTEX
        
          - > アイテムのメタデータをBIBTEX形式でエクスポートする。
        
          - > アイテム詳細画面のエクスポートエリアに表示されているBIBTEXリンクを押下する。/records/\<item\_id\>/export/bibtex
        
          - > 表示例は別紙「BIBTEX出力例.txt」を参照。
        
          - > 設定
            
              - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L203-L207>
            
              - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/box/export.html>
        
          - > シリアライザ：
            
              - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-schema-ui/weko_schema_ui/serializers/WekoBibTexSerializer.py>

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-schema-ui

  - > invenio-oaiserver

  - > invenio\_records

<!-- end list -->

  - > 処理概要

1\. 設定

  - プロバイダ不可の場合に対してのエラーコードを設定する  
    設定キー：OAISERVER\_CODE\_NO\_RECORDS\_MATCH  
    パス：  
    <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py#L207>

  - プロバイダ不可の場合に対してのエラーメッセージを設定する  
    設定キー：OAISERVER\_MESSAGE\_NO\_RECORDS\_MATCH  
    パス：  
    <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py#L210>

2\. 実装方法

  - OAI-PMHスキーマボタンを押すと、以下のフローを実施する

(1)「identifier」の値を元に、対象アイテムに対してプロバイダの有効・無効をチェックする

  - /oaiにアクセスすることで、invenio\_oaiserver.views.server.responseが呼び出され、リクエストのverbの値によってinvenio\_oaiserver.response.pyのが呼び出される。

  - verbの値によって呼び出されたでinvenio\_oaiserver.api.OaiIdentify.get\_allを呼び出す。そしてinvenio\_oaiserver.models.Identifyを呼び出して、「oaiserver\_identify」テーブルから「Administration＞OAI-PMH＞Identify」に設定したデータを取得して「Identify」の値とする。

  - 「Identify」の値を元にプロバイダ機能が無効の場合にinvenio\_oaiserver.response.get\_error\_code\_msgを呼び出して使用する。  
    なおverbの値がgetreccordの場合は、invenio\_oaiserver.response.errorを呼び出して使用する。

  - 以下のケースに当たれば、プロバイダ機能が無効とし、エラーレスポンスを返す
    
      - ケース
        
          - アイテムがプロバイダ機能の無効と設定しているインデックスに属する
        
          - アイテムが非公開と設定しているインデックスに属する
        
          - アイテムが非公開と設定する
    
      - エラー内容
        
          - エラーコード：コンフィグに設定している「OAISERVER\_CODE\_NO\_RECORDS\_MATCH」キー
        
          - > エラーメッセージ：コンフィグに設定している「OAISERVER\_MESSAGE\_NO\_RECORDS\_MATCH 」キー
        
          - > getrecordのエラーコード：errorに渡す引数  
            > 「idDoesNotExist」
        
          - > getrecordのエラーメッセージ：errorに渡す引数  
            > 「No matching identifier」

  - プロバイダ機能が有効になる場合、(2)に進む

(2)システムプロパティーを処理する  
(2.1)ファイル情報のプロパティー

  - invenio\_oaiserver.response.combine\_record\_file\_urlsを使用する。

  - ファイルのマッピングがメタデータレコードに含まれる場合、ファイルのURLを生成し、「File」プロパティーとし情報を返す

(2.2)識別子のプロパティー

  - invenio\_oaiserver.response. get\_identifierを使用する。

  - DOI、またはHDLのURLがメタデータレコードに含まれる場合、「system\_identifier\_doi」プロパティーとし情報を返す

  - DOI、またはHDLのURLがメタデータレコードに含まれない場合、レコードIDを元に、識別子の値を生成し、「system\_identifier\_doi」プロパティーとし情報を返す

(3)「\_init\_」メソッドで以下の情報を取得し、メタデータレコードにマッピングデータを組み込む

  - weko\_schema\_ui.schema.SchemaTree.\_init\_を使用する。

  - メタデータレコード

  - マッピングデータ

  - 非表示の属性

  - スキーマオブジェクト

(4)weko\_schema\_ui.schema.SchemaTree.create\_xmlで以下の処理を実施する  
(4.1)メタデータレコードでの各データを処理する

  - 非表示の属性に属するデータ、または値が空白のデータが対象外とする

  - 「get\_mapping\_value」関数でメタデータレコードをXML構成に変換する

(4.2)対象OAI-PMHスキーマがDDIスキーマであるかどうか、チェックする

  - 対象OAI-PMHスキーマがDDIスキーマの場合、以下の処理を実施する
    
      - 階層にある子タグ（node）をマージする
    
      - 繰り返し用の親タグを指定する。現在対応している親タグ（5件）は以下の通りである
        
          - 「stdyDscr\>citation」
        
          - 「stdyDscr\>stdyInfo」
        
          - 「stdyDscr\>method」
        
          - 「stdyDscr\>dataAccs」
        
          - 「stdyDscr\>othrStdyMat」

  - 対象OAI-PMHスキーマがDDIスキーマ以外の場合、(4.3)に進む

(4.3)メタデータレコードをOAI-PMHスキーマでの該当ノードに指定する  
(4.4)（4.3）での結果をOAI-PMHスキーマの構築にビルドし、該当スキーマのOAI-PMH出力を返す

  - 対象OAI-PMHスキーマがDDIスキーマの場合、追加で処理を実施する
    
      - (4.2)に指定された親タグを言語ごとに分ける
    
      - 「citation」親タグに対して以下のように制限する
        
          - 「citation\>titlStmt\>titl」が繰り返し不可により、同一言語にtitlの値が複数定義される場合、最初に出るtitlを出力する
        
          - 「citation\>titlStmt\>titl」が必須項目により、titlの値が無い場合は取得する最初のtitlを設定する
        
          - 「citation\>rspStmt\>AuthEnty」にて「ja-kana」の言語を選択する場合、jaの扱いとして出力する

  - １つのインデックスに対して１つのクエリを作成しているが、クエリの数(インデックスの件数が多い)が1024を超えている場合は、クエリのインデックスリスト部分を分割する

Elasticsearch の利用

  - scroll APIを利用している。 ESの index.max\_result\_window 以上の結果を取得することができる。
    
      - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/query.py#L192>

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