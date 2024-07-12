

### プロパティ

  - > 目的・用途

本機能は、アイテムタイプのメタデータが持つプロパティを管理する機能である。新規登録、および保存済みプロパティの更新ができる。

  - > 利用方法

【Administration \> アイテムタイプ管理（Item Types） \> プロパティ（Properties）画面】にて操作する。

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

  - 【Administration \> Item Types \> Properties画面】：プロパティを新規登録、保存済みプロパティを更新する画面である

  - プロパティを追加する
    
      - 【Administration \> Item Types \> Properties画面】にプロパティを新規登録できる
    
      - 入力項目は以下の通りである
        
          - 「プロパティ名」（Property Name）テキストボックス  
            プロパティ名を入力する
        
          - 「+Add」ボタンを押すことで、プロパティ属性の入力エリアを表示する
            
              - 項目名のテキストエリア
                
                  - デフォルト：空白
            
              - 入力形式プルダウン
                
                  - デフォルト：「Text」
                
                  - 「Text」：1行のテキストで値を入力する
                
                  - 「Textarea」：複数行のテキストで値を入力する
                
                  - 「Checkboxes」：複数選択のチェックボックスで値を入力する
                
                  - 「Radios」：単一選択のラジオボタンで値を入力する
                
                  - 「Select」：単一選択のプルダウンメニューで値を入力する
                
                  - 「Datetime」：以下の形式で値を入力する
                    
                      - yyyy-mm-dd、yyyy-mm、yyyy形式で入力
                    
                      - エリアフォーカス時に表示するカレンダーで日付を選択して入力する
                
                  - 「List」：複数の項目を繰り返し入力できる。入力項目がセットになっている  
                    例：「権利者情報」プロパティの「権利者識別子」が該当する
                
                  - 「Object」：複数の項目を入力する。入力項目がセットになっている  
                    例：「作成者」プロパティの「作成者所属」が該当する
                
                  - 注意事項
                    
                      - 入力形式で、「Checkboxes」、「Radios」、または「Select」を選択した場合、選択肢入力欄が表示される。選択肢入力欄には、各選択肢を「|」（半角パイプ）区切りでする  
                        例：AAA|BBB|CCC
                    
                      - また、選択式(プルダウン)を選択した場合、選択肢を選択した後未選択状態に戻るため、選択肢の先頭に空白が追加される
        
          - 入力が必須な属性を設定できるように、「Required」チェックボックスを設ける
        
          - 「JSONスキーマ」（Json Schema）ボタンを押すと、設定したプロパティ情報が、項目の下のテキストエリア、「フォーム(単数)」（Form(Singular)）及び「フォーム(複数)」（Form(Multiple)）にJSON形式で表示する
            
              - 注意事項
                
                  - システムプロパティとして追加する場合、該当subitemに「"system\_prop" : true 」を追加する
                    
                      - 課金ファイルのプロパティとして追加する場合、該当subitemに「"billing\_file\_prop":true」を追加する
                
                  - 入力形式で、「Checkboxes」、「Radios」、または「Select」を選択した場合、該当subitemに「"editAble": true」を追加することで［Meta］画面に選択肢を編集できるようになる
        
          - 項目の下のテキストエリアに直接設定した後、「リセット」（Reset）を押すと、設定した内容がプロパティ情報に反映される
    
      - 「保存」（Save）ボタンを押すと、プロパティを追加し、メッセージを表示する  
        メッセージ：「Saved property successfully.」
    
      - プロパティIDは、item\_type\_propertyテーブルでシーケンスのnextvalによって払い出される。

  - プロパティを編集する
    
      - 【Administration \> Item Types \> Properties画面】に保存されたプロパティを更新できる
    
      - 保存されたプロパティのプルダウンを画面の上部に設ける
    
      - プロパティのプルダウンからプロパティを選択すると、プロパティの情報を表示する
    
      - プロパティの情報を編集してから、「保存」（Save）ボタンを押すと、プロパティの情報を更新し、メッセージを表示する  
        メッセージ：「Saved property successfully.」
    
      - 注意事項
        
          - 編集不可として、プルダウンに表示されないプロパティがある。
            
              - システムプロパティ（subitemに「"system\_prop" : true 」が含まれるもの）は表示されない。
            
              - 課金ファイルをプロパティ画面に表示しない設定であるとき、課金ファイルのプロパティ（subitemに「"billing\_file\_prop":true」が含まれるもの）は表示されない。

各プロパティの構成

  - ファイル
    
      - アイテム登録画面でファイルをアップロードすると、表示名、フォーマット、サイズを自動設定する
    
      - アップロードしたファイルのフォーマット・ファイルサイズをDBに格納する  
        \*\*Meta画面のAllow Multipleのオプションはオンに設定し非活性

| プロパティ定義     | 備考       |           |          |                                                             |
| ----------- | -------- | --------- | -------- | ----------------------------------------------------------- |
| アクセス        | Radios   | \-        | \-       |                                                             |
| オープンアクセスの日付 | List     | 日付        | Datetime | "アクセス"で"オープンアクセス日を指定する"を選択したときに登録する                         |
|             |          | タイプ       | Select   | 日付タイプは「Available」固定（Item Registration画面では入力エリアは存在しない）       |
| 表示形式        | Select   | \-        | \-       |                                                             |
| 日付          | List     | 日付        | Datetime |                                                             |
|             |          | 日付タイプ     | Select   | JPCOAR v1の日付のdateTypeの統制語彙の内容（Available以外）がJSONスキーマで設定されている |
|             |          |           |          | https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/12            |
| 表示名         | Text     | \-        | \-       | ファイル名を登録する                                                  |
| サイズ         | List     | サイズ       | Text     | コンテンツファイルのサイズを取得して自動で登録される                                  |
| フォーマット      | Text     | \-        | \-       | コンテンツファイルのMIMEタイプを取得して自動で登録される                              |
| グループ        | Select   | \-        | \-       | "アクセス"で"ログインユーザのみ"を選択したときに登録する                              |
| 自由ライセンス     | Textarea | \-        | \-       | "ライセンス"で"write your own license"を選択した場合に登録する                |
| ライセンス       | Select   | \-        | \-       |                                                             |
| 本文URL       | Object   | 本文URL     | Text     | コンテンツファイルの格納先が自動で登録される                                      |
|             |          |           |          | コンテンツファイルが無い場合は手入力でURLを入力可能                                 |
|             |          | ラベル       | Text     |                                                             |
|             |          | オブジェクトタイプ | Select   | 選択肢                                                         |
|             |          |           |          | abstract/summary/fulltext/thumbnail/other                   |
| バージョン情報     | Text     | \-        | \-       |                                                             |

  - 課金ファイル
    
      - コンテンツのアクセスを「ログインユーザのみ」とした場合、グループと金額を入力するエリアを表示する
    
      - グループと金額は複数設定でき、\[New\]ボタン押下で追加できる
    
      - 削除時は\[×\]ボタンで削除する(他の要素と同じ仕様にする)
    
      - アイテム登録画面でファイルをアップロードすると、表示名を自動設定する
    
      - アップロードしたファイルのフォーマット・ファイルサイズをDBに格納する
    
      - Meta画面のAllow Multipleのオプションはオンに設定し非活性

<table>
<thead>
<tr class="header">
<th>プロパティ定義　</th>
<th>備考</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>アクセス</td>
<td>Radios</td>
<td>-</td>
<td>-</td>
<td></td>
</tr>
<tr class="even">
<td>オープンアクセスの日付</td>
<td>List</td>
<td>日付</td>
<td>Datetime</td>
<td><p>"アクセス"で"オープンアクセス日を指定する"を選択したときに登録する</p>
<p>Item Registration画面では「公開日」と表示される</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>タイプ</td>
<td>Select</td>
<td>日付タイプは「Available」固定（Item Registration画面では入力エリアは存在しない）</td>
</tr>
<tr class="even">
<td>表示形式</td>
<td>Select</td>
<td>-</td>
<td>-</td>
<td></td>
</tr>
<tr class="odd">
<td>日付</td>
<td>List</td>
<td>日付</td>
<td>Datetime</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>日付タイプ</td>
<td>Select</td>
<td>JPCOAR v1の日付のdateTypeの統制語彙の内容（Available以外）がJSONスキーマで設定されている</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/12</td>
</tr>
<tr class="even">
<td>表示名</td>
<td>Text</td>
<td>-</td>
<td>-</td>
<td>ファイル名を登録する</td>
</tr>
<tr class="odd">
<td>サイズ</td>
<td>List</td>
<td>サイズ</td>
<td>Text</td>
<td>コンテンツファイルのサイズを取得して自動で登録される（Item Registration画面では入力エリアは存在しない）</td>
</tr>
<tr class="even">
<td>フォーマット</td>
<td>Text</td>
<td>-</td>
<td>-</td>
<td>コンテンツファイルのMIMEタイプを取得して自動で登録される（Item Registration画面では入力エリアは存在しない）</td>
</tr>
<tr class="odd">
<td>グループ・価格</td>
<td>List</td>
<td>グループ</td>
<td>Select</td>
<td>"アクセス"で"ログインユーザのみ"を選択したときに登録する</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>価格</td>
<td>Text</td>
<td></td>
</tr>
<tr class="odd">
<td>自由ライセンス</td>
<td>Textarea</td>
<td>-</td>
<td>-</td>
<td>"ライセンス"で"write your own license"を選択した場合に登録する</td>
</tr>
<tr class="even">
<td>ライセンス</td>
<td>Select</td>
<td>-</td>
<td>-</td>
<td></td>
</tr>
<tr class="odd">
<td>本文URL</td>
<td>Object</td>
<td>本文URL</td>
<td>Text</td>
<td>コンテンツファイルの格納先が自動で登録される（Item Registration画面では入力エリアは存在しない）</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ラベル</td>
<td>Text</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>オブジェクトタイプ</td>
<td>Select</td>
<td>JPCOAR v1のファイル情報の本文URLのobjectTypeの統制語彙の内容がJSONスキーマで設定されている</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/35-.1</td>
</tr>
<tr class="odd">
<td>バージョン情報</td>
<td>Text</td>
<td>-</td>
<td>-</td>
<td></td>
</tr>
<tr class="even">
<td>Is Billing</td>
<td>Text</td>
<td></td>
<td></td>
<td>Item Registration画面では入力エリアは存在しない</td>
</tr>
</tbody>
</table>

  - サムネイル
    
      - サムネイルプロパティがアイテムタイプに含まれていると、アイテム登録時にサムネイルアップロードエリアが表示される
    
      - オプションHideのチェックがオフの場合に、アイテム詳細画面でサムネイル画像が表示される

| プロパティ定義 | 備考   |     |      |  |
| ------- | ---- | --- | ---- |  |
| URI     | List | ラベル | Text |  |
|         |      | URI | Text |  |

  - 作成者
    
      - 作成者識別子SchemeをID Prefixから自動で取得する
    
      - 作成者識別子と作成者識別子Schemeから自動設定されるため、作成者識別子URIは非活性項目になっている
    
      - アイテム詳細画面でリンク形式（押下後ポップアップ）として表示される

| プロパティ定義    | 備考   |              |        |               |        |  |
| ---------- | ---- | ------------ | ------ | ------------- | ------ |  |
| 作成者識別子     | List | 作成者識別子       | Text   |               |        |  |
|            |      | 作成者識別子Scheme | Select |               |        |  |
|            |      | 作成者識別子URI    | Text   |               |        |  |
| 作成者姓名      | List | 姓名           | Text   |               |        |  |
|            |      | 言語           | Select |               |        |  |
| 作成者姓       | List | 姓            | Text   |               |        |  |
|            |      | 言語           | Select |               |        |  |
| 作成者名       | List | 名            | Text   |               |        |  |
|            |      | 言語           | Select |               |        |  |
| 作成者別名      | List | 別名           | Text   |               |        |  |
|            |      | 言語           | Select |               |        |  |
| 作成者メールアドレス | Text | \-           | \-     |               |        |  |
| 作成者所属      | List | 所属機関識別子      | List   | 所属機関識別子       | Text   |  |
|            |      |              |        | 所属機関識別子Scheme | Select |  |
|            |      |              |        | 所属機関識別子URI    | Text   |  |
|            |      | 所属機関名        | List   | 所属機関名         | Text   |  |
|            |      |              |        | 言語            | Select |  |

  - 寄与者
    
      - 寄与者識別子SchemeをID Prefixから自動で取得する
    
      - 寄与者識別子と寄与者識別子Schemeから自動設定されるため、寄与者識別子URIは非活性項目になっている

| プロパティ定義    | 備考     |              |        |                                                        |        |  |
| ---------- | ------ | ------------ | ------ | ------------------------------------------------------ | ------ |  |
| 寄与者タイプ     | Select | \-           | \-     | JPCOAR v1の寄与者のcontributorTypeの統制語彙の内容がJSONスキーマで設定されている |        |  |
|            |        |              |        | https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/4        |        |  |
| 寄与者識別子     | List   | 寄与者識別子       | Text   |                                                        |        |  |
|            |        | 寄与者識別子Scheme | Select |                                                        |        |  |
|            |        | 寄与者識別子URI    | Text   |                                                        |        |  |
| 寄与者姓名      | List   | 姓名           | Text   |                                                        |        |  |
|            |        | 言語           | Select |                                                        |        |  |
| 寄与者姓       | List   | 姓            | Text   |                                                        |        |  |
|            |        | 言語           | Select |                                                        |        |  |
| 寄与者名       | List   | 名            | Text   |                                                        |        |  |
|            |        | 言語           | Select |                                                        |        |  |
| 寄与者別名      | List   | 別名           | Text   |                                                        |        |  |
|            |        | 言語           | Select |                                                        |        |  |
| 寄与者メールアドレス | Text   | \-           | \-     |                                                        |        |  |
| 寄与者所属      | List   | 所属機関識別子      | List   | 所属機関識別子                                                | Text   |  |
|            |        |              |        | 所属機関識別子Scheme                                          | Select |  |
|            |        |              |        | 所属機関識別子URI                                             | Text   |  |
|            |        | 所属機関名        | List   | 所属機関名                                                  | Text   |  |
|            |        |              |        | 言語                                                     | Select |  |

  - 権利者情報
    
      - 権利者識別子SchemeをID Prefixから自動で取得する
    
      - 権利者識別子と権利者識別子Schemeから自動設定されるため、権利者識別子URIは非活性項目になっている

| プロパティ定義 | 備考   |              |        |  |
| ------- | ---- | ------------ | ------ |  |
| 権利者識別子  | List | 権利者識別子       | Text   |  |
|         |      | 権利者識別子Scheme | Select |  |
|         |      | 権利者識別子URI    | Text   |  |
| 権利者名    | List | 名            | Text   |  |
|         |      | 言語           | Select |  |

  - 書誌情報
    
      - アイテム詳細画面で巻・号・ページ数などをまとめて表示する

| プロパティ定義 | 備考   |       |          |  |
| ------- | ---- | ----- | -------- |  |
| 雑誌名     | List | タイトル  | Text     |  |
|         |      | 言語    | Select   |  |
| 巻       | Text |       |          |  |
| 号       | Text |       |          |  |
| 開始ページ   | Text |       |          |  |
| 終了ページ   | Text |       |          |  |
| ページ数    | Text |       |          |  |
| 発行日     | List | 日付    | Datetime |  |
|         |      | 日付タイプ | Text     |  |

  - 資源タイプ
    
      - 資源タイプ識別子が非活性項目になっている
    
      - 資源タイプを選択すると、対応する資源タイプ識別子が自動で設定される

<table>
<thead>
<tr class="header">
<th>プロパティ定義</th>
<th>備考</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>資源タイプ</td>
<td>Select</td>
<td>JPCOAR v1のobjectType統制語彙の内容にJPCOAR v2の資源タイプのdc:typeの統制語彙の一部を加えたものがJSONスキーマで設定されている</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p><a href="https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/14">https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/14</a></p>
<p>https://schema.irdb.nii.ac.jp/ja/schema/2.0/15</p></td>
</tr>
<tr class="odd">
<td>資源タイプ識別子</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

  - ID登録
    
      - 非活性項目になっている
    
      - ワークフローの IdentifierGrant を経てアイテム登録が完了後、編集画面で入力された値を確認できる

| プロパティ定義 | 備考     |  |
| ------- | ------ |  |
| ID登録タイプ | Select |  |
| ID登録    | Text   |  |

  - 出版タイプ
    
      - 出版タイプresourceが非活性項目になっている
    
      - 出版タイプを選択すると、対応する出版タイプresourceが自動で設定される

| プロパティ定義       | 備考     |                                                        |
| ------------- | ------ | ------------------------------------------------------ |
| 出版タイプ         | Select | JPCOAR v1の出版タイプのoaire:versionの統制語彙の内容がJSONスキーマで設定されている |
|               |        | https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/16       |
| 出版タイプResource | Text   |                                                        |

  - アクセス権
    
      - アクセス権URIが非活性項目になっている
    
      - アクセス権を選択すると、対応するアクセス権URIが自動で設定される

| プロパティ定義  | 備考     |                                                               |
| -------- | ------ | ------------------------------------------------------------- |
| アクセス権    | Select | JPCOAR v1のアクセス権のdcterms:accessRightsの統制語彙の内容がJSONスキーマで設定されている |
|          |        | https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/5               |
| アクセス権URI | Text   |                                                               |

  - 識別子
    
      - OAI-PMH出力として用意されているもの
    
      - メタデータのエリアには表示せず、Permalink欄に「DOI \> HDL \> URI」の優先順で表示する（永続識別子）

  - 公開日
    
      - WEKO3のアイテムの表示／非表示として管理しているもの
    
      - アイテム登録時の必須項目であり、アイテム詳細画面に表示される
    
      - 「Hide」オプションの制御に従って、アイテムの「公開日」をOAI-PMH出力する

<!-- end list -->

  - 
  - > 関連モジュール

<!-- end list -->

  - weko-itemtypes-ui

<!-- end list -->

  - > 関連テーブル

<!-- end list -->

  - 画面の一番上のプルダウン：item\_type\_propertyテーブルから取得したプロパティ一覧
    
      - １つプロパティを選択する場合、item\_type\_propertyテーブルから該当のプロパティの情報を読み取る。

  - 画面の「保存」ボタンを押下する場合、画面に設定している情報をitem\_type\_propertyテーブルの該当プロパティに反映する。

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - HTMLテンプレート
    
      - パス: <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L33-L35>　
        
          - 設定キー: WEKO\_ITEMTYPES\_UI\_ADMIN\_CREATE\_PROPERTY = \\  
            'weko\_itemtypes\_ui/admin/create\_property.html'  
            """Create property template."""

  - 課金ファイルをプロパティ画面に表示する・しないかの設定
    
      - パス: <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L57-L58>
        
          - 設定キー: WEKO\_BILLING\_FILE\_ACCESS = 1  
            """Show billing file property in list."""  
            1: システム管理者のユーザーID。  
            1のみ表示する。1以外、プロパティ画面に表示しない。

  - 課金ファイルのプロパティであるかどうか判断するための設定
    
      - パス: <https://github.com/RCOSDP/weko/blob/b81efc2b8d1b3af838c0910798050c25a19f1f41/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L60-L61>
        
          - 設定キー: WEKO\_BILLING\_FILE\_PROP\_ATT = 'billing\_file\_prop'  
            """Attribute to detect billing file property."""  
            （課金ファイルをプロパティ画面に表示する・しない時に合わせて利用される。）

  - システムプロパティであるかどうか判断するための設定
    
      - パス: <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L63-L64>
        
          - 設定キー: WEKO\_ITEMTYPES\_UI\_DEFAULT\_PROPERTIES\_ATT = 'system\_prop'  
            """Attribute to detect property is default property which is not shown at properties screen."""

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