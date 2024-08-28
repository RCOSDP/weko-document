# インポート

## 目的・用途

本機能は、管理者として、アイテムの一括登録を実行する機能である。

## 利用方法

管理者は 【Administration > アイテム管理（Items） > インポート（Import）画面】を開き、アイテム一括登録用のzipファイルを登録する。

## 利用可能なロール

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
<td>○※</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

※コミュニティ管理者は、自身の管理下にあるコミュニティに関連付けられたインデックスへのインポートのみ可能

## 機能内容

### 1\. 概要

  - 複数のアイテムを一括で登録する機能。システム管理者、リポジトリ管理者のみ使用できる。

  - 登録形式はBagitだが、ユーザにそれを意識させないようにしている。詳細はの1を参照。

  - 機能は3つの画面で構成されている。

  - 以下は各画面の関連と役割。

> \+----------+ ≪選択画面≫
> 
> | | ●各アイテムタイプのTSVファイルテンプレートのダウンロード
> 
> | Select | ●インポートファイルの指定
> 
> | | ●「識別子変更モード」の設定と利用規約への同意
> 
> \+----------+
> 
> ↓
> 
> ↓【Next】 button click\!
> 
> ↓
> 
> \+----------+ ≪インポート画面≫
> 
> | | ●TSVファイルで指定した項目のチェック結果の確認
> 
> | Import | ●チェック結果のダウンロード
> 
> | |
> 
> \+----------+
> 
> ↓
> 
> ↓【Import】 button click\!
> 
> ↓
> 
> \+----------+ ≪結果画面≫
> 
> | | ●アイテムごとのインポート実行結果の確認
> 
> | Result | ●インポート実行結果のダウンロード
> 
> | |
> 
> \+----------+

### 2\. 画面ごとの仕様

#### 2.1 選択画面(Select)

  - 各アイテムタイプのTSVファイルテンプレートのダウンロードとインポートファイルを指定する画面。  
    また「識別子変更モード」の設定と利用規約への同意を実施する

> ────────────────────────────────────────────────
> 
> \#\# Message Area \#\# ★
> 
> ────────────────────────────────────────────────
> 
> ┌───────┐
> 
> │Select │Import Result
> 
> ┘ └─────────────────────────────────────
> 
> Select File 【Select File】①
> 
> Selected file name ②
> 
> □ Change Identifier Mode ③
> 
> 【Next】④
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> Item Type Template
> 
> Item Type:\[ ⑤ \]【Download】⑥

★Message Area（管理画面共通）

  - インポートファイルのチェックでエラーが発生した際にメッセージを表示する。

  - 表示されるエラーメッセージは3.2(4)-1参照。

①［ファイル選択（Select File）］ボタン

  - 押下するとファイル選択ダイアログを表示する。選択可能なファイルはzip形式で1つのみ。

②Selected file name ラベル

  - ①で選択したファイル名を表示する。未選択時は「選択したファイル名（Selected file name）」を表示。

③Change Identifier Mode チェックボックス

  - DOIやCNRIを変更する際に設定する。チェックありで④を押下すると「免責事項ダイアログ」が表示される。  
    免責事項の文面は以下（テキストファイルで保持。ファイルパスはコンフィグ管理→処理概要の2を参照）

  - 免責事項ダイアログには［OK］ボタンと［キャンセル（Cancel）］ボタンがある。［OK］ボタンは、「利用規約に同意します（I agree to the terms of use.）」がチェックされるまでは非活性。［OK］ボタンを押下するとインポートファイルのチェックを行い、通過するとImport画面に遷移する。

  - チェックありの状態でImport画面に遷移してから選択画面に戻ると、選択ファイルを変更するまでは非活性になっており変更できない。

> Japanese:
> 
> 免責事項：
> 
> ・本機能は設定にかかわらずDOIを強制的に変更します。
> 
> ・本機能は内容及び自機関で登録されているDOIについて十分に理解した上で作業を行なってください。
> 
> ・本機能の利用は、自機間の責任で行なってください。
> 
> ・本機能の利用により負った損害などについては、国立情報学研究所は一切の責任を追いません。
> 
> English:
> 
> \- This function forcibly changes the DOI regardless of the setting.
> 
> \- Before starting this operation, you need fully understand the contents and DOI registered at your institution.
> 
> \- Use this function on your own responsibility.
> 
> \- National Institute of Informatics (NII) does not take any responsibility for damages caused by using this function.

④［次へ（Next）］ボタン

  - ①でファイルが選択されるまでは非活性。  
    ただし、拡張子が「zip」でないファイルが選択された場合は活性化しない。  
    押下するとインポートファイルのチェックを行い、通過するとImport画面に遷移する。  
    チェック処理については、3.2(4)を参照。

⑤Item Type セレクタ―

  - TSVファイルテンプレートをダウンロードする際、対象とするアイテムタイプを選択する。  
    【Administration \> アイテムタイプ管理（Item Types） \> メタデータ（Metadata）】画面で確認できる標準アイテムタイプ（Standard Item Type）を表示。  
    表示形式は「Item Type name(Item Type ID)」。

⑥Download ボタン

  - 押下すると⑤で選択したアイテムタイプのTSVファイルテンプレートをダウンロードする。  
    ファイルについては4.1参照。

#### 2.2 インポート画面(Import)

  - TSVファイルで指定した項目のチェック結果の確認とチェック結果のダウンロードができる。

> ┌──────┐
> 
> Select │Import│ Result
> 
> ───────┘ └─────────────────────────────────────
> 
> \# Identifier Mode \#①
> 
> 【Import】②
> 
> Summary
> 
> Total: ③
> 
> New Item: ④
> 
> Update: ⑤
> 
> Check error: ⑥
> 
> 【Download】⑦
> 
> ┏━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━┓
> 
> ┃No. ┃Item Type ┃Item ID ┃Title ┃Check Result┃
> 
> ┣━━━━╋━━━━━━━━━━╋━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━┫
> 
> ┃ ⑧ ┃ ⑨ ┃ ⑩ ┃ ⑪ ┃ ⑫ ┃
> 
> ┗━━━━┻━━━━━━━━━━┻━━━━━━━━┻━━━━━━┻━━━━━━━━━━━━┛

①Message ラベル

  - ※名称は要検討  
    Select画面の「③Change Identifier Mode チェックボックス」にチェックを入れた場合。メッセージ「識別子変更モードで登録します(Register with \[Change Identigier Mode\].)」を表示する。

②Import ボタン

  - 押下するとインポートを実行する。  
    対象データがすべてエラーなど、インポートできない場合は非活性。

③Summary/Total ラベル

  - TSVファイルで設定されたアイテムの総数。TSVファイルが複数存在した場合、各ファイルで設定されたアイテムの合計を表示する。

④Summary/New Item ラベル

  - ③の内、新規登録アイテムとなる件数を表示する。

⑤Summary/Update ラベル

  - ③の内、更新アイテムとなる件数を表示する。

⑥Summary/Check error ラベル

  - ③の内、TSVファイルの設定内容にエラーがある件数を表示する。

⑦Download ボタン

  - インポートファイルのチェック結果をTSV形式で出力する。出力項目が当該画面の⑧～⑫。  
    ダウンロードするファイルは4.2を参照。

⑧表/No.

  - 項番。Not処理順。

⑨表/Item Type

  - アイテムをインポートする際に使用するアイテムタイプ名を表示する

⑩表/Item ID

  - 新規登録の場合
    
      - TSVファイルでID指定あり→「新規登録（Item ID）」
    
      - TSVファイルでID指定無し→ 空白

  - 更新の場合
    
      - TSVファイルで指定したIDを表示する

⑪表/Title

  - アイテムのタイトルを以下のルールで表示する。
    
      - システムの言語属性に合わせたタイトルを表示する
    
      - 一致するものがない場合は英語表記で表示する
    
      - 画面の横幅に応じて表示する文字数をトリミング（末尾を「…」に置換）する

⑫表/Check Result

  - TSVファイルの設定内容について、チェックした結果を以下の形式（()は英語表記）で表示する。
    
      - 新規登録→「登録(Registre)」
    
      - 更新→「更新(Update)」
    
      - エラー→「エラー(ERROR)：\<エラーメッセージ\>」
    
      - ワーニング→「警告(Warning)：\<警告メッセージ\>」

  - チェック仕様については、3.2(4)-2\~3を参照

#### 2.3 結果画面(Result)

  - アイテムごとのインポート実行結果の確認とインポート実行結果のダウンロードができる。

  - 現状、処理中に一度画面を離れた場合、処理はCeleryで管理されて継続するが、画面で進捗状況を再度確認することはできない。

> ┌──────┐
> 
> Select Import │Result│
> 
> ───────────────┘ └─────────────────────────────────────
> 
> 【Download】①
> 
> ┏━━━━┳━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━┓
> 
> ┃No. ┃Start Date ┃End Date ┃Item Id┃Action┃WrokFlow Status┃
> 
> ┣━━━━╋━━━━━━━━━━━╋━━━━━━━━━╋━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━┫
> 
> ┃ ② ┃ ③ ┃ ④ ┃ ⑤ ┃ ⑥ ┃ ⑦ ┃
> 
> ┗━━━━┻━━━━━━━━━━━┻━━━━━━━━━┻━━━━━━━┻━━━━━━┻━━━━━━━━━━━━━━━┛

①Download ボタン

  - インポート処理の実行結果を出力する。項目は当該画面の②～⑦．

  - ダウンロードファイルについては4.3参照。

②表/No.

  - 項番。Not処理順。

③表/Start Date

  - アイテムの登録処理を開始した日時。YYYY-MM-DD hh:mm:ssで表示する。

④表/End Date

  - アイテムの登録処理が完了した日時。YYYY-MM-DD hh:mm:ssで表示する。

⑤表/Item Id

  - 処理対処のアイテムIDを表示する。新規登録の場合は空欄。

⑥表/Action

  - 以下を表示する。
    
      - 「Start」：アイテム登録の処理が開始されている
    
      - 「End」：アイテム登録の処理が正常に終了している。
    
      - 「Error」：アイテム登録の処理がエラーで終了している。

⑦表/WorkFlow Status

  - 処理中のワークフローのステータスを表示する。

### 3\. インポートファイル／TSVファイルについて

#### 3.1 インポートファイル

  - エクスポート（一括出力）したファイルを流用できる

  - 対応しているファイル形式：zip（他の圧縮形式は不可）実装の詳細は処理概要の1を参照。

  - フォルダ構成

> import.zip
> 
> │
> 
> ├bag-info.txt ※
> 
> ├bagit.txt ※
> 
> ├manifest-sha256.txt ※
> 
> ├manifest-sha512.txt ※
> 
> ├tagmanifest-sha256.txt ※
> 
> ├tagmanifest-shar512.txt ※
> 
> │
> 
> └/data
> 
> │
> 
> ├/recid\_n
> 
> │ └\<Files\>
> 
> │
> 
> ├ItemTypeName1(ItemType ID).tsv
> 
> └ItemTypeName2(ItemType ID).tsv
> 
> ※はBagit形式のファイル。インポート時は省略可能

  - 「/data」は変更不可

  - 「/recid\_n」は変更可

  - アイテムタイプのTSVファイルは複数指定可能

#### 3.2 アイテムタイプごとのTSVファイル

当該ファイルは以下で共通のレイアウトとしている。
    
- Select画面でダウンロードできるテンプレートファイル(4.1)
- インポートファイルに含めるアイテムタイプTSVファイル
- エクスポート（一括出力）ファイルに含まれるアイテムタイプTSVファイル

##### (1) ヘッダ行

ヘッダ行は先頭が「#」とする。

###### 1行目：インポートするアイテムタイプの情報

| 1列目 | 「\#ItemType」固定                                                            |
| --- | ------------------------------------------------------------------------- |
| 2列目 | アイテムタイプ名                                                                  |
| 3列目 | アイテムタイプのjsonschemaのURI。形式は「https://FQDN/items/jsonschema/\<ItemType ID\>」 |

###### 2行目：各項目のJSONパス。各種処理に使用される項目。

###### 3行目：各項目のラベル。
    
      - アイテムタイプ以外の項目  
        → 項目ごとにラベルの内容を定義。
    
      - アイテムタイプ項目  
        → 【Administration \> アイテムタイプ管理（ItemTypes） \> メタデータ（Metadata）画面】のLocalization Settingで設定している内容を出力。設定がない場合は項目名を出力。

###### 4行目：インポート実行時に値を自動で設定する項目について「System」を出力 。対象はプロパティ定義内で「"readonly":true」を設定している項目。

###### 5行目：各項目について「Allow Multiple」（繰り返し可）「Requierd」（必須）を出力
    
      - アイテムタイプ以外の項目  
        → 項目ごとにラベルの内容を定義。
    
      - アイテムタイプ項目  
        → 【Administration \> アイテムタイプ管理（ItemTypes） \> メタデータ（Metadata）画面】のOptionの設定内容がチェックありの項目について出力

##### (2) アイテムタイプ項目以外の項目

<table>
<thead>
<tr class="header">
<th><strong>JSONパス</strong></th>
<th><strong>ラベル</strong></th>
<th><strong>説明</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.id</td>
<td>ID</td>
<td>アイテムID。新規登録時、指定なしの場合は自動採番、未使用の番号を指定することもできる。更新時は登録済みの内容が必須。</td>
</tr>
<tr class="even">
<td>.uri</td>
<td>URI</td>
<td>アイテムのURI。新規登録時は指定なし。更新時は登録済みの内容が必須となる。</td>
</tr>
<tr class="odd">
<td>.metadata.path[0]</td>
<td>.IndexID[0]</td>
<td>アイテムを登録するインデックスをID指定する。複数指定可。<br />
.pos_index[n]とペアで指定する。<br />
.pos_index[n]が指定されていない場合は必須。存在しないインデックスを指定した場合はエラーメッセージを出力する。</td>
</tr>
<tr class="even">
<td>.pos_index[0]</td>
<td>.POS_INDEX[0]</td>
<td>アイテムを登録するインデックスを名称(※1)で指定する。<br />
.metadata.path[n]とペアで指定する。<br />
.metadata.path[n]が指定されてない場合は必須。</td>
</tr>
<tr class="odd">
<td>.publish_status</td>
<td>.PUBLISH_STATUS</td>
<td>アイテムの公開／非公開を指定する。public/privateのいずれかを設定する。必須項目。</td>
</tr>
<tr class="even">
<td>.feedback_mail[0]</td>
<td>.FEEDBACK_MAIL[0]</td>
<td>フィードバックメールの送信先メールアドレスを指定する。複数指定可。</td>
</tr>
<tr class="odd">
<td>.cnri</td>
<td>.CNRI</td>
<td>CNRIハンドルサーバを使用する場合(※2)に設定できる。CNRIは「prefix/suffix」の形式で設定される。通常モードの時は自動採番(※3)される。識別子変更モードの時は「prefix/suffix」を設定する。識別子変更モードの時に「prefix」または「prefix/」を指定すると自動採番となる。</td>
</tr>
<tr class="even">
<td>.doi_ra</td>
<td>.DOI_RA</td>
<td>DOIの種類を指定する。JaLC/Crossref/DataCite(※4)/NDL JaLC (※5)のいずれかを設定する。</td>
</tr>
<tr class="odd">
<td>.doi</td>
<td>.DOI</td>
<td>DOIを「prefix/suffix」の形式で設定する。通常モードの時は自動採番(※3)される。識別子変更モードの時は手入力で変更可能。</td>
</tr>
<tr class="even">
<td>.edit_mode</td>
<td>Keep/Upgrade Version</td>
<td>対象のアイテムのバージョン更新可否を指定する。新規登録の場合は空、更新の場合は必須でKeep/Upgradeのいずれかを指定する。<br />
※インポートファイル（zip）に既存アイテムの元ファイルが同名、ファイルパスも同一で含まれていた場合（元ファイルを変更しない）<br />
　・Keep: 重複登録されない<br />
　・Upgrade: 重複登録する。ファイル名だけでは、同名同ファイルなのか同名異ファイルなのかが判断できない</td>
</tr>
</tbody>
</table>

  - ※1) インデックス名称について  
    POS\_INDEXは階層を指定して記述する。階層の区切り文字はデフォルトで「///」。weko\_items\_ui/config.py の WEKO\_ITEMS\_UI\_INDEX\_PATH\_SPLIT にて区切り文字の変更が可能。  
    同名のインデックスが複数存在した場合は、すべてのインデックスに登録される。  
    日本語名称、英語名称のいずれかを指定できる。日本語名称のインデックスと英語名称のインデックスをまぜて指定することはできない。

<table>
<thead>
<tr class="header">
<th><strong>IndexID</strong></th>
<th><strong>POS_INDEX</strong></th>
<th><strong>説明</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>指定あり</td>
<td>指定なし</td>
<td>IndexID に指定されたインデックスに登録。</td>
</tr>
<tr class="even">
<td>指定なし</td>
<td>指定あり</td>
<td>POS_INDEX に指定されたインデックスに登録。</td>
</tr>
<tr class="odd">
<td>指定あり</td>
<td>指定あり</td>
<td>IndexID と POS_INDEX の組み合わせが正しい場合、該当するインデックスに登録。<br />
不整合の場合、IndexID で指定されたインデックスに登録。<br />
システムに存在しない IndexID と POS_INDEX を指定した場合はエラーとなる。</td>
</tr>
<tr class="even">
<td>指定なし</td>
<td>指定なし</td>
<td>エラーとなる。</td>
</tr>
</tbody>
</table>

##### ※2) CNRIハンドルサーバの使用について  
    CNRIハンドルの使用状態は「WEKO\_HANDLE\_ALLOW\_REGISTER\_CRNI」(modules/weko-handle/weko\_handle/config.py)の設定値で判断している
    
      - 「False」：初期値。CNRIハンドルサーバを使用しない
    
      - 「True」：CNRIハンドルサーバを使用する

##### ※3) CNRIとDOIの自動採番時の指定について  
    
現状は以下の通り。
    
- 識別子変更モード
  - DOIの自動採番は行わない。  
    インポートファイルにdoiやprefixが含まれている場合はエラーメッセージを表示する。
  - DOIが空欄の場合  
    「Please specify DOI prefix/suffix.」
  - インポートファイルにdoiやprefixが含まれている場合　(「prefix」もしくは「prefix/」を指定した場合）  
    「DOI suffixを設定してください。」／「Please specify DOI suffix.」
- Not 識別子変更モード        
  - Admin \> Setting \> Identifier でprefixの設定があること
    - DOI：空欄であること
    - DOI\_RA：JaLC, Crossref, DataCite のいずれかであること
    - DOI_RA：NDL JaLCの場合、自動採番は行われない。
      インポートファイルにdoiやprefixが含まれている場合はエラーメッセージを表示する。
    - DOIが空欄の場合
　     「Please specify DOI prefix/suffix.」
    - インポートファイルにdoiやprefixが含まれている場合　(「prefix」もしくは「prefix/」を指定した場合）
　      「DOI suffixを設定してください。」／「Please specify DOI suffix.」

※4) DataCiteについて  
    制限等は現状設けていない

※5) NDL JaLCについて  
DOI RA：NDL JaLCの場合、資源タイプは「doctoral thesis」である必要があります。

CNRIハンドルの未設定・設定ユーザーのDOI付与状況は以下の通り。

<table>
<thead>
<tr class="header">
<th></th>
<th>識別子変更モード</th>
<th></th>
<th>Not 識別子変更モード</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>登録時のモード</td>
<td>新規</td>
<td>更新</td>
<td>新規</td>
<td>更新</td>
</tr>
<tr class="even">
<td>CNRI<br />
（CNRIハンドル未設定ユーザー）</td>
<td>空欄</td>
<td>空欄</td>
<td>空欄</td>
<td>空欄</td>
</tr>
<tr class="odd">
<td>CNRI<br />
（CNRIハンドル設定ユーザー）</td>
<td>必須。「prefix」または「prefix/」を指定すると自動採番。「prefix/suffix」を指定すると指定された形式でCNRIハンドルを発行。</td>
<td>変更可能</td>
<td>空欄</td>
<td>変更不可</td>
</tr>
<tr class="even">
<td>DOI_RA</td>
<td>設定可能</td>
<td>DOI付与前は設定可能<br />
DOI付与後は変更不可</td>
<td>設定可能</td>
<td>DOI付与前は設定可能<br />
DOI付与後は変更不可</td>
</tr>
<tr class="odd">
<td>DOI</td>
<td>設定可能</td>
<td>変更可能</td>
<td>空欄</td>
<td>DOI付与前は空欄<br />
DOI付与後は変更不可</td>
</tr>
</tbody>
</table>

  - 
(3) アイテムタイプ項目

基本はアイテムタイプに定義されている項目（プロパティ）に対して、TSVファイル内で設定されている内容を登録する。  
次の項目は項目の設定以外の処理を行っている。

－1. コンテンツファイル

コンテンツファイルを指定してアップロードする。  
自動設定は本文URLのみ対応済。

プロパティID：  
項目：

<table>
<thead>
<tr class="header">
<th><strong>JSONパス</strong></th>
<th><strong>初期設定ラベル</strong></th>
<th><strong>System(自動設定)</strong></th>
<th><strong>説明</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.file_path[0]</td>
<td>.ファイルパス[0]</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>.upload_id[0]</td>
<td>. ファイルアップロードID[0]</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].accessrole</td>
<td>ファイル情報[0].アクセス</td>
<td>空欄で「オープンアクセス」を自動設定／手入力</td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].date[0].dateType</td>
<td>ファイル情報[0].公開日[0].タイプ</td>
<td>「Available」を自動設定（値があっても無視）</td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].date[0].dateValue</td>
<td>ファイル情報[0].公開日[0].公開日</td>
<td>「アクセス」＝オープンアクセスの際は自動設定／「アクセス」＝オープンアクセス日を指定 の際に手入力可／それ以外は空白</td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].displaytype</td>
<td>ファイル情報[0].表示形式</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].fileDate[0].fileDateType</td>
<td>ファイル情報[0].日付[0].日付タイプ</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].fileDate[0].fileDateValue</td>
<td>ファイル情報[0].日付[0].日付</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].filename</td>
<td>ファイル情報[0].ファイル名</td>
<td>空欄で自動設定／手入力</td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].filesize[0].value</td>
<td>ファイル情報[0].サイズ[0].サイズ</td>
<td>空欄で自動設定／手入力</td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].format</td>
<td>ファイル情報[0].フォーマット</td>
<td><p>空欄で自動設定／手入力</p>
<p>ファイルアップロードIDを入力の場合、必須</p></td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].groups</td>
<td>ファイル情報[0].グループ</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].licensefree</td>
<td>ファイル情報[0].自由ライセンス</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].licensetype</td>
<td>ファイル情報[0].ライセンス</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].url.label</td>
<td>ファイル情報[0].本文URL.ラベル</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].url.objectType</td>
<td>ファイル情報[0].本文URL.オブジェクトタイプ</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.metadata.item_files[0].url.url</td>
<td>ファイル情報[0].本文URL.本文URL</td>
<td>空欄で自動設定(※1)／手入力</td>
<td></td>
</tr>
<tr class="even">
<td>.metadata.item_files[0].version</td>
<td>ファイル情報[0].バージョン情報</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

※1: 本文URLは「THEME\_SITEURL」(/home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg") を利用して生成している。ルールは以下の通り。

  - file\_path & 本文URLの両方を指定された場合、本文URLを無視し、システムがURLを生成し上書きする。

  - file\_path のみ指定された場合、URLを生成し登録する。

  - 本文URLのみ指定された場合、URLを使って登録する。

－2. サムネイルファイル

プロパティID：  
項目：

| **JSONパス**                                                                  | **初期設定ラベル**                       | **System(自動設定)** | **説明**                                               |
| --------------------------------------------------------------------------- | --------------------------------- | ---------------- | ---------------------------------------------------- |
| .thumbnail\_path\[0\]                                                       | .サムネイルパス\[0\]                     |                  | 設定値ありで登録、設定値なしで削除する。指定したパスに該当ファイルがあれば常にアップロードして登録する。 |
| .metadata.item\_1568286766453\[0\].subitem\_thumbnail\[0\].thumbnail\_label | Thumbnail\[0\].URI\[0\].URI Label | 〇                | インポート時に設定されても無視する                                    |
| .metadata.item\_1568286766453\[0\].subitem\_thumbnail\[0\].thumbnail\_url   | Thumbnail\[0\].URI\[0\].URI       | 〇                | インポート時に設定されても無視する                                    |

－3. 自動設定の項目

  - **出版タイプ** （JPCOARスキーマ「出版タイプ」：<https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/16> の統制語彙に基づく）  
    プロパティID：  
    項目：

| **JSONパス**                                           | **初期設定ラベル**         | **JPCOAR\[※\]**           | **System(自動設定)** | **説明** |
| ---------------------------------------------------- | ------------------- | ------------------------- | ---------------- | ------ |
| .metadata.item\_1531978917933.subitem\_1522305645492 | 出版タイプ.出版タイプ         | versiontype               |                  |        |
| .metadata.item\_1531978917933.subitem\_1600292170262 | 出版タイプ.出版タイプResource | versiontype.@rdf:resource | 〇                |        |

  - **アクセス権** （JPCOARスキーマ「アクセス権」：<https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/5> の統制語彙に基づく）  
    プロパティID：  
    項目：

| **JSONパス**                                           | **初期設定ラベル**           | **JPCOAR\[※\]**            | **System(自動設定)** | **説明** |
| ---------------------------------------------------- | --------------------- | -------------------------- | ---------------- | ------ |
| .metadata.item\_1531978848664.subitem\_1522299639480 | Access Right.アクセス権    | accessRights               |                  |        |
| .metadata.item\_1531978848664.subitem\_1600958577026 | Access Right.アクセス権URI | accessRights.@rdf:resource | 〇                |        |

  - **資源タイプ** （JPCOARスキーマ「資源タイプ」：https://schema.irdb.nii.ac.jp/ja/schema/1.0.2/14 の統制語彙に基づく）  
    プロパティID：  
    項目：

| **JSONパス**                                 | **初期設定ラベル**            | **JPCOAR\[※\]**    | **System(自動設定)** | **説明** |
| ------------------------------------------ | ---------------------- | ------------------ | ---------------- | ------ |
| .metadata.item\_1569380275317.resourcetype | Resource Type.Type     | type               |                  |        |
| .metadata.item\_1569380275317.resourceuri  | Resource Type.Resource | type.@rdf:resource | 〇                |        |

\[※\]各Resource項目の自動設定機能は、【Administration \> アイテムタイプ管理（ItemTypes） \> マッピング（Mapping）画面】で対象のアイテムタイプについてJPCOARスキーマのマッピングが設定されている必要があります。  
　「出版タイプ」と「アクセス権」については、移行ツール作成のアイテムタイプに含まれていない項目なので、該当環境で項目を追加した際は必ずマッピング設定をしてください。

(4) チェック仕様

\-1. インポートファイル、TSVファイルの形式チェック

最初に実施。  
エラーの場合は、Select（選択）画面の\#Message Area\#にメッセージを出力する。ただし、\#2はImport（インポート）画面の表/Check Resultに出力。

<table>
<thead>
<tr class="header">
<th><strong>#</strong></th>
<th><strong>条件</strong></th>
<th><strong>処理</strong></th>
<th><strong>メッセージ(日本語)</strong></th>
<th><strong>メッセージ(英語)</strong></th>
<th><strong>備考</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>指定された項目が一括登録対象のアイテムタイプと一致しない（項目不足）</td>
<td>エラー</td>
<td>指定されたアイテムタイプと項目が一致しません。</td>
<td>The item does not consistent with the specified item type.</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>指定された項目が一括登録対象のアイテムタイプと一致しない（項目追加）</td>
<td>警告</td>
<td>次の項目指定されたアイテムタイプに存在しないため登録されません。{}</td>
<td>The following items are not registered because they do not exist in the specified item type. {}</td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>指定された圧縮ファイルの形式がzip以外</td>
<td>エラー</td>
<td>指定されたファイル{}の形式はインポートに対応していません。zip ,tar,gztar,bztar,xztarいずれかの形式を指定してください。</td>
<td>The format of the specified file {} does not support import. Please specify one of the following formats: zip, tar, gztar, bztar, xztar.</td>
<td><p>対応している圧縮形式がzipのみで、</p>
<p>ファイル選択時のバリデーションチェックでzip以外のファイルでは［次へ（Next）］ボタンが活性化しないためこのチェックに到達しない。</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>指定された圧縮ファイル内でTSVファイルが見つからない（フォルダ構成誤り）</td>
<td>エラー</td>
<td>指定されたファイル{}にtsv/csvファイルが見つかりませんでした。ディレクトリ構成が正しいか確認してください。</td>
<td>The tsv/csv file was not found in the specified file {}. Check if the directory structure is correct.</td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>UTF-8でエンコードされていない</td>
<td>エラー</td>
<td>{}ファイルを読み込めませんでした。ファイル形式が{}であること、またそのファイルがUTF-8でエンコードされているかを確認してください。</td>
<td>The {} file could not be read. Make sure the file format is {} and that the file is UTF-8 encoded.</td>
<td>{}に拡張子が入る</td>
</tr>
<tr class="even">
<td>6</td>
<td>ファイルの１行目のフォーマットが正しくない（3列名にアイテムタイプIDが指定されていない など）</td>
<td>エラー</td>
<td>{}ファイルのヘッダ１行目の形式に誤りがあります。</td>
<td>There is an error in the format of the first line of the header of the {} file.</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>指定したアイテムタイプが存在しない</td>
<td>エラー</td>
<td>{}ファイルで指定されたアイテムタイプIDは存在しません。</td>
<td>The item type ID specified in the {} file does not exist.</td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>TSV ファイルに改行が含まれている場合</td>
<td>エラー</td>
<td>{}ファイルが正しく読み込めません。</td>
<td>Cannot read {} file correctly.</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>指定したアイテムタイプが一括登録可能（最新版）でない場合</td>
<td>エラー</td>
<td>指定されたアイテムタイプが最新のバージョンでないため登録できません。</td>
<td>Cannot register because the specified item type is not the latest version.</td>
<td>現在はアイテムタイプのバージョン管理はしていないため使用していない</td>
</tr>
<tr class="even">
<td>10</td>
<td>Runtimeエラー（ElasticSearchがロックされた、サーバ接続不可、ネットワーク接続不可など）</td>
<td>エラー</td>
<td>サーバ内部エラー</td>
<td>Internal server error</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>エラー</td>
<td></td>
<td>The specified {} does not exist in system.</td>
<td></td>
</tr>
</tbody>
</table>

\-2. メタデータ項目以外のチェック

アイテムタイプのメタデータ以外の項目についてチェック仕様。  
各項目は「JSONパス（ラベル）」で記載。  
エラーメッセージはImport（インポート）画面の表/Check Resultに出力。

  - .id（ID）

| **\#** | **条件**                          | **処理** | **メッセージ(日本語)**                       | **メッセージ(英語)**                                                              | **備考**                 |
| ------ | ------------------------------- | ------ | ------------------------------------ | -------------------------------------------------------------------------- | ---------------------- |
| 1      | 半角数字以外                          | エラー    | アイテムIDは半角数字で指定してください。                | Please specify item ID by half-width number.                               |                        |
| 2      | 指定されたアイテムIDをpidとしてもつアイテムが存在しない  | エラー    |                                      | Item does not exits in the system                                          | 多言語対応ができていない           |
| 3      | 指定されたアイテムIDがシステムでは削除済み          | エラー    |                                      | Item already DELETED in the system                                         | 多言語対応ができていない           |
| 4      | アイテムIDが指定されていて、項目「status」が「new」 | ワーニング  | 新規登録アイテムにIDが指定されています。IDを無視して登録を行います。 | ID is specified for the newly registered item. Ignore the ID and register. | 項目「status」はチェック中に付与される |

  - .id（ID）と.uri（URI）

| **\#** | **条件**                 | **処理** | **メッセージ(日本語)**           | **メッセージ(英語)**                              | **備考** |
| ------ | ---------------------- | ------ | ------------------------ | ------------------------------------------ | ------ |
| 1      | アイテムIDとURIの組み合わせが一致しない | エラー    | 指定されたURIとシステムURIが一致しません。 | Specified URI and system URI do not match. |        |

  - .metadata.path\[0\]（.IndexID\[0\]）

| **\#** | **条件**        | **処理** | **メッセージ(日本語)**       | **メッセージ(英語)**                                  | **備考**          |
| ------ | ------------- | ------ | -------------------- | ---------------------------------------------- | --------------- |
| 1      | 指定された内容が存在しない | エラー    | 指定された{}はシステムに存在しません。 | The specified {} does not exist in the system. | {}に「IndexID」が入る |

  - .pos\_index\[0\]（.POS\_INDEX\[0\]）

| **\#** | **条件**                                 | **処理** | **メッセージ(日本語)**       | **メッセージ(英語)**                                | **備考**             |
| ------ | -------------------------------------- | ------ | -------------------- | -------------------------------------------- | ------------------ |
| 1      | IndexIDが指定されていない際、指定したPOS\_INDEXが存在しない | エラー    | 指定された{}はシステムに存在しません。 | The specified {}does not exist in the system | {}に「POS\_INDEX」が入る |

  - .metadata.path\[0\]（.IndexID\[0\]）と.pos\_index\[0\]（.POS\_INDEX\[0\]）

| **\#** | **条件**                                                | **処理** | **メッセージ(日本語)**                    | **メッセージ(英語)**                                     | **備考**                     |
| ------ | ----------------------------------------------------- | ------ | --------------------------------- | ------------------------------------------------- | -------------------------- |
| 1      | 組合せチェック（IndexID→存在している、POS\_INDEX→指定されたIndexIDと一致しない） | 警告     | 指定された{}はシステムのものと一致していません。         | Specified {} does not match with existing index.  | {}に「POS\_INDEX」が入る         |
| 2      | 組合せチェック（IndexID→存在していない、POS\_INDEX→存在している）            | エラー    | 指定された{}はシステムに存在しません。              | The specified {} does not exist in system.        | {}に「IndexID」が入る            |
| 3      | 組合せチェック（指定されたIndexIDとPOS\_INDEXがどちらも存在しない）            | エラー    | 指定された{}はシステムに存在しません。              | The specified {} does not exist in system.        | {}に「IndexID,POS\_INDEX」が入る |
| 4      | 組合せチェック（IndexIDとPOS\_INDEXIDがどちらも指定されていない）            | エラー    | IndexID,POS\_INDEXがどちらも設定されていません。 | Both of Index ID and POS INDEX are not being set. |                            |

  - .publish\_status（.PUBLISH\_STATUS）

| **\#** | **条件**                     | **処理** | **メッセージ(日本語)**                   | **メッセージ(英語)**                            | **備考**                  |
| ------ | -------------------------- | ------ | -------------------------------- | ---------------------------------------- | ----------------------- |
| 1      | 指定されていない                   | エラー    | {}は必須項目です。                       | {} is required item.                     | {}に「PUBLISH\_STATUS」が入る |
| 2      | 指定された内容が不正（public/private） | エラー    | {}はpublic,privateのいずれかを設定してください。 | Please set "public" or "private" for {}. | {}に「PUBLISH\_STATUS」が入る |

  - .feedback\_mail\[0\]（.FEEDBACK\_MAIL\[0\]）

| **\#** | **条件**               | **処理** | **メッセージ(日本語)** | **メッセージ(英語)**            | **備考**        |
| ------ | -------------------- | ------ | -------------- | ------------------------ | ------------- |
| 1      | 形式チェック（メールアドレスの形式不正） | エラー    | 指定された{}が不正です。  | Specified {} is invalid. | {}にメールアドレスが入る |

  - .cnri（.CNRI）

<table>
<thead>
<tr class="header">
<th><strong>#</strong></th>
<th><strong>条件</strong></th>
<th><strong>処理</strong></th>
<th><strong>メッセージ(日本語)</strong></th>
<th><strong>メッセージ(英語)</strong></th>
<th><strong>備考</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>CNRI使用フラグが「False」の時にCNRIを設定した</td>
<td>エラー</td>
<td>{}は設定できません。</td>
<td>{} cannot be set.</td>
<td>{}に「CNRI」が入る</td>
</tr>
<tr class="even">
<td>2</td>
<td>通常モードで新規登録時に指定</td>
<td>エラー</td>
<td>{}は設定できません。</td>
<td>{} cannot be set.</td>
<td>{}に「CNRI」が入る</td>
</tr>
<tr class="odd">
<td>3</td>
<td>通常モードで更新時に登録内容から変更</td>
<td>エラー</td>
<td>指定されたCNRIは登録しているCNRIと異なっています。</td>
<td>Specified {} is different from existing {}.</td>
<td>両方の{}に「CNRI」が入る</td>
</tr>
<tr class="even">
<td>4</td>
<td>識別子変更モードで新規／更新時にCNRIを設定しない</td>
<td>エラー</td>
<td>{}を設定してください。</td>
<td>Please specify {}.</td>
<td>{}に「CNRI」が入る</td>
</tr>
<tr class="odd">
<td>5</td>
<td>形式チェック（管理画面で登録されているPrefixと一致しない)</td>
<td>エラー</td>
<td>指定された{}のPrefixが誤っています。</td>
<td>Specified Prefix of {} is incorrect.</td>
<td>{}に「CNRI」が入る</td>
</tr>
<tr class="even">
<td>6</td>
<td>形式チェック（Suffixに半角英数字、半角記号「_-.;()/」以外を使用）</td>
<td>エラー</td>
<td>CNRIのSuffixは半角英数字、半角記号「_-.;()/」以外使用できません。</td>
<td>Suffix of CNRI can only be used with half-width alphanumeric characters and half-width symbols “_-.; () /”.</td>
<td>エラーチェックが存在しない</td>
</tr>
<tr class="odd">
<td>7</td>
<td>形式チェック（最大長超え）</td>
<td>エラー</td>
<td>指定された{}が最大長を超えています。</td>
<td>The specified {} exceeds the maximum length.</td>
<td><p>{}に「CNRI」が入る</p>
<p>pidstoreの上限が255のため、http://～とprefix/を含めて255が上限となるようにチェックする</p></td>
</tr>
</tbody>
</table>

  - .doi\_ra（.DOI\_RA）と.doi（.DOI）

| **\#** | **条件**                              | **処理** | **メッセージ(日本語)**              | **メッセージ(英語)**                                 | **備考**                     |
| ------ | ----------------------------------- | ------ | --------------------------- | --------------------------------------------- | -------------------------- |
| 1      | 組合せチェック（通常モードで新規登録時にどちらも指定）         | エラー    | {}は設定できません。                 | {} cannot be set.                             | {}に「DOI」が入る                |
| 2      | 組合せチェック（通常モードで更新時に登録内容から変更）         | エラー    | 指定された{ }が登録している{ }と異なっています。 | Specified { } is different from existing { }. | 両方の{}に「DOI\_RA」または「DOI」が入る |
| 3      | 組合せチェック（識別子変更モードで新規登録時にDOIのみ指定）     | エラー    | DOI\_RAを設定してください。           | Please specify DOI\_RA.                       |                            |
| 4      | 組合せチェック（識別子変更モードで新規登録時にDOI\_RAのみ指定） | エラー    | {}を設定してください。                | Please specify {}.                            | {}に「DOI」が入る                |

  - .doi\_ra（.DOI\_RA）

| **\#** | **条件**                                                               | **処理** | **メッセージ(日本語)**                                          | **メッセージ(英語)**                                                                          | **備考**       |
| ------ | -------------------------------------------------------------------- | ------ | ------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------ |
| 1      | 指定された内容が不正（DOI\_RAが設定されており、JaLC,Crrossref,DataCite,NDL JaLCのいずれでもない） | エラー    | DOI\_RAはJaLC,Crrossref,DataCite,NDL JaLCのいずれかを設定してください。 | DOI\_RA should be set by one of JaLC, Crossref, DataCite, NDL JaLC.                    |              |
| 2      | 通常モードで更新時に登録内容から変更                                                   | ワーニング  |                                                         | The specified DOI RA is wrong and fixed with the correct DOI RA of the registered DOI. | 多言語対応ができていない |

  - .doi（.DOI）

| **\#** | **条件**                                   | **処理** | **メッセージ(日本語)**                            | **メッセージ(英語)**                                                                                              | **備考**                                                    |
| ------ | ---------------------------------------- | ------ | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1      | 形式チェック（管理画面で登録されているPrefixと一致しない)         | エラー    | 指定されたDOIのPrefixが誤っています。                   | Specified Prefix of DOI is incorrect.                                                                      |                                                           |
| 2      | 形式チェック（Suffixに半角英数字、半角記号「\_-.;()/」以外を使用) | エラー    | DOIのSuffixは半角英数字、半角記号「\_-.;()/」以外使用できません。 | Suffix of {} can only be used with half-width alphanumeric characters and half-width symbols "\_-.; () /". | エラーチェックがなく、このメッセージは表示されない                                 |
| 3      | 形式チェック（最大長超え)                            | エラー    | 指定されたDOIが最大長を超えています                       | The specified DOI exceeds the maximum length.                                                              | pidstoreの上限が255のため、http://～とprefix/を含めて255が上限となるようにチェックする |
| 4      | 指定された内容が不正（通常モードで更新時に登録内容から変更）           | ワーニング  |                                           | The specified DOI is wrong and fixed with the registered DOI.                                              | 多言語対応ができていない                                              |
| 5      | 識別子変更モードでDOIが指定されていない                    | エラー    |                                           | Please specify DOI prefix/suffix.                                                                          | 多言語対応ができていない                                              |
| 6      | 識別子変更モードでDOIに「/」が含まれていない                 | エラー    |                                           | Please specify DOI suffix.                                                                                 | 多言語対応ができていない                                              |

  - .edit\_mode（Keep/Upgrade Version）

| **\#** | **条件**                                            | **処理** | **メッセージ(日本語)**              | **メッセージ(英語)**                              | **備考** |
| ------ | ------------------------------------------------- | ------ | --------------------------- | ------------------------------------------ | ------ |
| 1      | 指定されていない、指定された内容が不正（edit\_modeがKeepでもUpgradeでもない） | エラー    | Keep、Upgradeのいずれかを指定してください。 | Please specify either “Keep” or “Upgrade”. |        |

  - .file\_path\[0\]（.ファイルパス\[\#\]）または.thumbnail\_path\[\#\]（.サムネイルパス\[\#\]）

| **\#** | **条件**                      | **処理** | **メッセージ(日本語)**                                                         | **メッセージ(英語)**                                                                                                                           | **備考**                                              |
| ------ | --------------------------- | ------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 1      | 新規登録時に指定したパスに該当するファイルが存在しない | エラー    | （.file\_path\[\#\]）に指定したファイルが存在しません。                                   | The file specified in (.file\_path \[\#\]) does not exist.                                                                              | 複数ファイルの場合は（.file\_path\[0\],.file\_path\[1\]…）と表示する |
| 2      | 更新時に指定したパスに該当するファイルが存在しない   | ワーニング  | file\_path\[\#\]）に指定したファイルが存在しません。ファイルの更新はしません。csv/tsv内容でメタデータのみ更新します。 | The file specified in (.file\_path \[\#\]) does not exist.The file will not be updated. Update only the metadata with csv/tsv contents. | 複数ファイルの場合は（.file\_path\[0\],.file\_path\[1\]…）と表示する |

  - .file\_path\[0\]（.ファイルパス\[\#\]）とメタデータのファイル名／表示名 ※メタデータ項目の関連チェックだがここに記載

| **\#** | **条件**                                  | **処理** | **メッセージ(日本語)**            | **メッセージ(英語)**                                       | **備考**                                                 |
| ------ | --------------------------------------- | ------ | ------------------------- | --------------------------------------------------- | ------------------------------------------------------ |
| 1      | ファイルパスで指定したファイル名とメタデータに設定されたファイル名が一致しない | エラー    | {}に指定されたファイル名と{ }が一致しません。 | The file name specified in {} and { } do not match. | ひとつ目の{}には.file\_path\[\#\]、ふたつ目の{}にはファイル名のJSON Pathが入る |

  - .thumbnail\_path\[\#\]（.サムネイルパス\[\#\]）

| **\#** | **条件**      | **処理** | **メッセージ(日本語)**                                                   | **メッセージ(英語)**                                                                              | **備考** |
| ------ | ----------- | ------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------ |
| 1      | 画像ファイル以外を指定 | エラー    | サムネイルは画像ファイル（gif, jpg, jpe, jpeg, png, bmp, tiff, tif）を指定してください。 | Please specify the image file(gif, jpg, jpe, jpeg, png, bmp, tiff, tif) for the thumbnail. |        |

  - .upload\_id\[\#\]（.ファイルアップロードID\[\#\]）

<table>
<thead>
<tr class="header">
<th><strong>#</strong></th>
<th><strong>条件</strong></th>
<th><strong>処理</strong></th>
<th><strong>メッセージ(日本語)</strong></th>
<th><strong>メッセージ(英語)</strong></th>
<th><strong>備考</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td>アップロードIDがUUID型でない</td>
<td>エラー</td>
<td>アップロードIDを正しく入力してください</td>
<td>Upload_id is invalid format</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>アップロードIDが見つからない</td>
<td>エラー</td>
<td>指定されたアップロードIDが見つかりません</td>
<td>Specified upload_id is not found</td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>未完了かすでにアイテムのバケットに紐づいているアップロードIDを指定している</td>
<td>エラー</td>
<td>指定されたアップロードIDは完了していないか、すでにアイテムに紐づけられています</td>
<td>Specified upload_id not completed or already linked to the item</td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>アップロードIDがファイル内で被っている</td>
<td>エラー</td>
<td>アップロードIDが重複しています</td>
<td>Duplicate upload_id</td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>クォータサイズ超過</td>
<td>エラー</td>
<td>ファイルの合計サイズがバケットのサイズを超えています</td>
<td>Total file size exceeds bucket size</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>ファイルパス[0],</p>
<p>.ファイルアップロードID[0]が同時に入力</p></td>
<td>エラー</td>
<td>ファイルパスかアップロードIDのみ入力してください</td>
<td>Please enter only file_path or upload_id</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>.ファイルアップロードID[0]が入力されているが、</p>
<p>File[0].フォーマットが未入力または正しくない場合</p></td>
<td>エラー</td>
<td>ファイル形式を正しく設定してください</td>
<td>Please set the file format corrctly</td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>アップロードIDで指定されているファイルと、ロケーションが異なる。</td>
<td>エラー</td>
<td>ファイルとアイテムのロケーションが異なります</td>
<td>Files and Items have different locations</td>
<td></td>
</tr>
</tbody>
</table>

\-3. メタデータ項目のチェック

基本的なチェックはライブラリを使用している。(\#1～3が該当)  
4～8はそれぞれ実装。  
エラーメッセージはImport（インポート）画面の表/Check Resultに出力。

<table>
<thead>
<tr class="header">
<th><strong>#</strong></th>
<th><strong>対象項目</strong></th>
<th><strong>条件</strong></th>
<th><strong>処理</strong></th>
<th><strong>メッセージ(日本語)</strong></th>
<th><strong>メッセージ(英語)</strong></th>
<th><strong>備考</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>入力形式がselect,checkboxes,radiosの項目</td>
<td>プロパティに定義されている選択肢以外を指定した</td>
<td>エラー</td>
<td>{}は次の決められた選択肢に含まれていません。{}</td>
<td>"%r is not one of %r"</td>
<td>英語はライブラリ出力メッセージ。日本語はマッピングして出力。</td>
</tr>
<tr class="even">
<td>2</td>
<td>Optoinで「Required」を指定している項目</td>
<td>指定されていない</td>
<td>エラー</td>
<td>{}は必須項目です。</td>
<td>"%r is a required property"</td>
<td>英語はライブラリ出力メッセージ。日本語はマッピングして出力。</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Multipleで繰り返しの上限数が指定されている</td>
<td>上限数を超えている</td>
<td>エラー</td>
<td>{} の数が上限数を超えています。</td>
<td>{} is too long</td>
<td>英語はライブラリ出力メッセージ。日本語はマッピングして出力。</td>
</tr>
<tr class="even">
<td>4</td>
<td>項目</td>
<td>メタデータキーが重複指定している場合</td>
<td>エラー</td>
<td><p>以下のメタデータキーが重複しています。</p>
<p>｛｝</p></td>
<td><p>The following metadata keys are duplicated.</p>
<p>{}</p></td>
<td>重複するメタデータは改行で区切って出力</td>
</tr>
<tr class="odd">
<td>5</td>
<td>タイトル</td>
<td>指定されていない</td>
<td>エラー</td>
<td>{}は必須項目です。</td>
<td>Title is required item.</td>
<td><p>2のエラーメッセージも同時に出力</p>
<p>日本語ではフォーマットできずに｛｝のまま表示される</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>日付項目</td>
<td>日付形式チェック（YYYY/MM/DDで指定）</td>
<td>ワーニング</td>
<td>日付はYYYY-MM-DD、YYYY-MM、YYYYのいずれかで指定してください。</td>
<td>Please specify the date with any format of YYYY-MM-DD, YYYY-MM, YYYY.</td>
<td>YYYY-MM-DD 形式で解釈できないときのエラーメッセージは設定されているが、YYYY-MM-DD 形式でYYYY/MM/DDを解釈できるため実際には出力されない</td>
</tr>
<tr class="odd">
<td>7</td>
<td>日付項目</td>
<td>日付形式チェック（YYYY-MM-DD、YYYY-MM、YYYY以外で指定）</td>
<td>エラー</td>
<td>日付はYYYY-MM-DD、YYYY-MM、YYYYのいずれかで指定してください。</td>
<td>Please specify the date with any format of YYYY-MM-DD, YYYY-MM, YYYY.</td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>.metadata.pubdate（公開日）</td>
<td>形式チェック（YYYY-MM-DD以外で指定）</td>
<td>エラー</td>
<td>公開日はYYYY-MM-DDで指定してください。</td>
<td>Please specify PubDate with YYYY-MM-DD.</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>.metadata.pubdate（公開日）</td>
<td>指定されていない</td>
<td>エラー</td>
<td>%rは必須項目です。</td>
<td>%r is a required property</td>
<td>%rが「’pubdate’」 と置き換わる</td>
</tr>
<tr class="even">
<td>10</td>
<td>コンテンツファイルのオープンアクセスの日付</td>
<td>形式チェック（YYYY-MM-DD以外で指定）</td>
<td>エラー</td>
<td>オープンアクセスの日付はYYYY-MM-DDで指定してください。</td>
<td>Please specify Open Access Date with YYYY-MM-DD.</td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>マッピングによって必須になっている項目</td>
<td>設定されていない</td>
<td>エラー</td>
<td>{}は必須項目です。</td>
<td><p>The following metadata are required.</p>
<p>{}</p></td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>マッピングによって必須になっている項目（複数のうちいずれか１つを設定するもの）</td>
<td>１つも設定されていない</td>
<td>エラー</td>
<td>{}のいずれかを設定してください。</td>
<td><p>One of the following metadata is required.</p>
<p>{}</p></td>
<td></td>
</tr>
</tbody>
</table>

\-4. DOI付与アイテムの項目チェック

DOIを指定したアイテムについて、指定された項目が各DOI付与の要件を見ているかを確認。  
当該処理は個別登録のチェック処理を呼び出し実施している。

| **\#** | **対象項目** | **条件**                                                        | **処理** | **メッセージ(日本語)**                                                   | **メッセージ(英語)**                                                                                                                          | **備考**      |
| ------ | -------- | ------------------------------------------------------------- | ------ | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| 1      | 各項目      | DOIを指定した際に入力項目が不足している                                         | エラー    | PID付与の条件を満たしていません。                                               | PID does not meet the conditions.                                                                                                      |             |
| 2      | \-       | DOI が付与されているアイテムに対して、アイテムを非公開として更新しようとした場合                    | エラー    | アイテムにDOIが付与されているため、アイテムを非公開にすることはできません。                          | You cannot keep an item private because it has a DOI.                                                                                  |             |
| 3      | \-       | インデックス状態が「公開」かつハーベスト公開が「公開」のインデックスに紐づいていないアイテムにDOIを付与しようとした場合 | エラー    | アイテムにDOIが付与されているため、インデックス状態が「公開」かつハーベスト公開が「公開」のインデックスに関連付けが必要です。 | Since the item has a DOI, it must be associated with an index whose index status is "Public" and whose Harvest Publishing is "Public". |             |
| 4      | \-       | 既存アイテムに付与されているDOIとインポートファイルで指定されたDOIの値が異なる場合                  | エラー    | 指定された{}が登録している{}と異なっています。                                        | Specified {} is different from existing {}.                                                                                            | {}に「DOI」が入る |

\-5. ファイル以外のチェック

操作アカウントの権限チェックを行う。

| **\#** | **対象** | **条件**                                                      | **処理** | **メッセージ(日本語)**                   | **メッセージ(英語)**                                  | **備考** |
| ------ | ------ | ----------------------------------------------------------- | ------ | -------------------------------- | ---------------------------------------------- | ------ |
| 1      | \-     | 操作アカウントが、アイテムの登録先インデックス（またはその親インデックス）へのインポートに必要な権限を持っていない場合 | エラー    | ロールの権限が足りずこのインデックスにアイテム登録ができません。 | Your role cannot register items in this index. |        |

4\. ダウンロードファイルについて

4.1 テンプレートファイル

  - Select（選択）画面でダウンロードできる。アイテムタイプ（Item Type）セレクタ―で選択したアイテムタイプについて、ヘッダ行のみ出力したインポートに使用するTSVファイル。

  - ファイル名は「アイテムタイプ名(アイテムタイプID).tsv」で、詳細は3.2を参照。

  - TSV形式で文字コードはBOMありUTF-8、改行コードはLF

◆出力イメージ

> \#ItemType 紀要論文（出版者版、オープンアクセス、JaLC\_DOI\_登録あり）(16) https://FQDN/items/jsonschema/16
> 
> \#.id .uri .metadata.path\[0\] .pos\_index\[0\] .publish\_status .feedback\_mail\[0\] .cnri .doi\_ra .doi .edit\_mode .metadata.pubdate　 …
> 
> \#ID URI .IndexID\[0\] .POS\_INDEX\[0\] .PUBLISH\_STATUS .FEEDBACK\_MAIL\[0\] .CNRI .DOI\_RA .DOI Keep/Upgrade Version PubDate …
> 
> \# …
> 
> \# Allow Multiple Allow Multiple Required Allow Multiple Required Required …

4.2 インポート前チェック結果ファイル

  - Import（インポート）画面でダウンロードできる。同画面の表に表示されているチェック結果をTSV形式で出力したファイル。

  - ファイル名は「Check\_ダウンロード日付.tsv」で、2.2⑧～⑫の項目を出力。

> ◆出力イメージ
> 
> \#No. Item Type Item ID Title Check Result

4.3 インポート実行結果ファイル

  - Result（結果）画面でダウンロードできる。同画面の表に表示されているインポート実行結果をTSV形式で出力したファイル。

  - ファイル名は「List\_ダウンロード日付.tsv」で、2.3②～⑦の項目を出力。

  - TSV形式で文字コードはBOM無しUTF-8、改行コードはLF

> ◆出力イメージ
> 
> \#No. Start Date End Date Item Id Action WorkFlow Status

4.4. 「インポート」（Import）タブで一括登録のアイテムを確認・登録する

  - インポート」（Import）タブ  
    読み込んだzipファイルの内容を表示し、一括登録して良いかの確認を促す  
    表示項目は以下の通りである
    
      - 「識別子 変更モード」で登録する旨のメッセージを表示する
        
          - ［Import］ボタンの上に赤字で以下のメッセージを表示する  
            メッセージ：  
            日本語：「 識別子で登録します」  
            英語：「Register with \[Change Identifier Mode\].」
        
          - 「Import」タブから「Selectタブ」に遷移した場合、「識別子変更モード」チェックボックスはチェックありで非活性となっている
    
      - 「サマリー」(Summary)  
        読み込んだファイルのアイテム情報について、以下の件数を表示する
        
          - 総計(Total)：読み込んだファイルのアイテム数
        
          - 新規登録アイテム(New Item)：読み込んだファイルのアイテムの内、新規登録となるアイテム数
        
          - 更新アイテム(Update Item)：読み込んだファイルのアイテムの内、更新のアイテム数
        
          - チェックエラー(Result Error)：バリデートチェックでバリデートエラーとなったアイテム数
    
      - 詳細情報
        
          - 「No.」  
            読み込んだファイルのアイテムの通し番号を表示する
        
          - 「アイテムタイプ」（Item Type）  
            読み込んだファイルのアイテムについて、登録されるアイテムタイプ名を表示する
        
          - 「アイテムID」（Item Id）  
            読み込んだファイルのアイテムについて、新規登録／更新によって表示する内容を変更する
            
              - 新規：””表示なし
            
              - 更新：画面上にアイテムIDを表示する
        
          - 「タイトル」（Title）  
            読み込んだファイルのアイテム名を表示する
            
              - タイトル名はシステムの言語属性に合わせたtitleを表示する
            
              - システムの言語属性に合うtitleが無い場合は英語表記で表示する
            
              - タイトルが長い場合は、横スクロールにならないようにタイトルをトリミングする
                
                  - タイトルを表示上限文字数まで表示して、その直後に「...」をつける
        
          - 「チェック結果」（Check Result）  
            読み込んだファイルの各アイテムについて、インポートが可能かバリデートチェックを実施する  
            エリアに表示する内容は以下の通りである
            
              - エラーが無く、新規のアイテムの場合：「登録」（Register）と表示する
            
              - エラーが無く、アイテムの「.edit\_mode」が「Upgrade」の場合：「バージョンの変更」（Upgrade Version）と表示する
            
              - エラーが無く、アイテムの「.edit\_mode」が「Keep」の場合：「バージョンの維持」（Keep Version）と表示する
            
              - バリデーションエラーがある場合：「エラー: XXXXX」（Error: XXXXX）とエラー内容を表示する
            
              - バリデーションワーニングがある場合：「警告: XXXXX」（Warning: XXXXX）とワーニング内容を表示する
    
      - インポートファイルのバリデーションチェックは以下とする
        
          - Bagit形式の仕様に従っていること
        
          - メタデータの必須項目が入力されていること
        
          - メタデータの入力内容が、入力制約に合致していること
            
              - DOI付与：DOI\_RA の設定に従い、資源タイプ、必須、いずれか必須のチェックを行うこと  
                <https://redmine.devops.rcos.nii.ac.jp/attachments/download/6107/JPCOAR_JaLC_Guideline_appendix_v1.pdf>
            
              - dc:titleのxml:langは必須としない。
            
              - 日付項目：ISO-8601で規定する3 形式（YYYY-MM-DD、YYYY-MM、YYYY）のチェックを行うこと
        
          - 存在するインデックスツリーであること
        
          - 新規登録の場合、既に登録されているDOIが割当されないこと
        
          - 更新の場合、アイテムがWEKO上に存在し、論理削除されていないこと
        
          - 更新の場合、更新前のアイテムタイプが変更後のアイテムタイプと一致していること
        
          - WEKOに登録されていないアイテムタイプがインポートファイルに含まれる場合はエラーとすること
        
          - TSVファイルの項目のバリデーションチェックは以下とする
            
              - POS\_INDEX\[n\]：インデックス名
                
                  - インデックス名が指定されていること
                
                  - 指定したインデックス名が存在していること
            
              - FEEDBACK\_MAIL：フィードバックメール送信先メールアドレス
                
                  - 指定されたメールアドレスはメールアドレスの形式チェックをすること
            
              - PUBLISH\_STATUS：アイテムの公開／非公開設定
                
                  - 指定されたPUBLISH\_STATUSがprivate, publicのいずれかであること
            
              - CNRI：CNRIハンドル
                
                  - 「 識別子 変更モード」を指定している場合  
                    ・CNRIの値が空白になること
                
                  - 「 識別子 変更モード」を指定していない場合  
                    ・新規アイテム登録の場合、CNRIが指定されること  
                    ・既存アイテムへの更新の場合、指定されたCNRIが登録内容と同一であること
            
              - DOI\_RA：DOI付与の種類
                
                  - DOIが指定されている場合、DOI\_RAが指定していることは必須である
                
                  - DOI\_RAが空白になること
                
                  - 指定されたDOI\_RAがJaLC, Crossref, DataCite, NDL JaLC のいずれかであること
                
                  - 「 識別子 変更モード」を指定している場合  
                    ・指定した形式に応じてメタデータの項目チェックを行うこと  
                    ・既存アイテムへの更新の場合、指定された内容が登録内容と同一であること
                
                  - 「 識別子 変更モード」を指定していない場合  
                    ・新規アイテム登録の場合、 DOIが指定されていること  
                    ・既存アイテムへの更新の場合、指定された内容が登録内容と同一であること
            
              - DOI ：DOI
                
                  - 「 識別子 変更モード」を指定している場合  
                    ・DOIが空白になること
                
                  - 「 識別子 変更モード」を指定していない場合  
                    ・新規アイテム登録の場合、 DOIが指定されていること  
                    ・既存アイテムへの更新の場合、指定された内容が登録内容と同一であること
        
          - 環境変数で設定した格納先が下記の状況の場合エラーメッセージを出力する。あわせて、エラーログにも出力する
            
              - 格納先のパスが無かった場合
            
              - 格納先の書き込み権限が無かった場合
            
              - 格納先の容量が不足している場合
        
          - 一括登録の実行時に他端末から実行した場合エラーメッセージを出力する。
            
              - 一括登録を実行中に他の端末が【Administration \> アイテム管理（Items） \> （Import）画面を開いた場合
            
              - 一括登録を実行している端末が【Administration \> アイテム管理（Items） \> インポート（Import）画面を開いた場合（他のブラウザで開いたとき，"Result"タブから再度"Import"タブに遷移したとき等）
            
              - 個別のアイテム編集中に、一括登録を実施した場合
            
              - 個別のアイテム削除後に、一括登録を実施した場合
    
      - バリデーションのエラーメッセージ及びワーニングメッセージは以下の通りである

<table>
<thead>
<tr class="header">
<th><strong>No.</strong></th>
<th><strong>タイプ</strong></th>
<th><strong>英語</strong></th>
<th><strong>日本語</strong></th>
<th><strong>利用場合</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>エラー</td>
<td>Specified item type does not exist.</td>
<td>指定されたアイテムタイプが存在していません。</td>
<td>指定されたアイテムタイプがシステムに存在しない場合</td>
</tr>
<tr class="even">
<td>2</td>
<td>エラー</td>
<td>Please specify item ID by half-width number.</td>
<td>アイテムIDは半角数字で指定してください。</td>
<td>アイテムIDが不正な形式で指定した場合</td>
</tr>
<tr class="odd">
<td>3</td>
<td>エラー</td>
<td>Item ID does not match the specified URI information.</td>
<td>アイテムIDが指定されたURIの情報と一致しません</td>
<td>アイテムIDが指定されたURIの情報と一致しない場合</td>
</tr>
<tr class="even">
<td>4</td>
<td>エラー</td>
<td>Specified URI and system URI do not match.</td>
<td>指定されたURIとシステムURIが一致しません。</td>
<td>指定されたURIとシステムURIが一致しない場合</td>
</tr>
<tr class="odd">
<td>5</td>
<td>エラー</td>
<td>Please specify {}.</td>
<td>{}を設定してください。</td>
<td>PUBLISH_STATUS, CNRI, DOI_RA, DOI, POS_INDEX, IndexIDが空白の場合</td>
</tr>
<tr class="even">
<td>6</td>
<td>エラー</td>
<td>{} is required item.</td>
<td>{}は必須項目です。</td>
<td>DOI_RA, DOI, PUBLISH_STATUSが指定されない場合</td>
</tr>
<tr class="odd">
<td>7</td>
<td>エラー</td>
<td>{} cannot be set.</td>
<td>{}は設定できません。</td>
<td>指定できない識別子（CNRI, DOI_RA, DOI）を指定した場合</td>
</tr>
<tr class="even">
<td>8</td>
<td>エラー</td>
<td>{} must be one of JaLC, Crossref, DataCite.</td>
<td>{}は JaLC, Crossref, DataCiteのいずれかである必須があります。</td>
<td>DOI_RAにJaLC, Crossref, DataCite以外のものを指定した場合</td>
</tr>
<tr class="odd">
<td>9</td>
<td>エラー</td>
<td>Specified {} is different from existing {}.</td>
<td>指定された{}は登録している{}と異なっています。</td>
<td>CNRI, DOI_RA, DOIに指定された内容が登録内容と異なる場合</td>
</tr>
<tr class="even">
<td>10</td>
<td>エラー</td>
<td>Specified {} is invalid.</td>
<td>指定された{}は不正です。</td>
<td>FEEDBACK_MAIL, DOI, PUBLISH_STATUSが不正な形式で指定した場合</td>
</tr>
<tr class="odd">
<td>11</td>
<td>エラー</td>
<td>PID does not meet the conditions.</td>
<td>PID付与の条件を満たしていません。</td>
<td>DOIバリデーションチェックの場合</td>
</tr>
<tr class="even">
<td>12</td>
<td>エラー</td>
<td>The storage path is incorrect.{} Please contact the administrator.</td>
<td>格納先のパスが正しくありません。{} 管理者へお問い合わせください。</td>
<td><p>格納先のパスが無かった場合</p>
<p>※v0.9.22ではエラーチェックがないため出力されない</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td>エラー</td>
<td>The storage location cannot be accessed.{} Please contact the administrator.</td>
<td>格納先にアクセスできません。{} 管理者へお問い合わせください。</td>
<td><p>格納先の書き込み権限が無かった場合</p>
<p>※v0.9.22ではエラーチェックがないため出力されない</p></td>
</tr>
<tr class="even">
<td>14</td>
<td>エラー</td>
<td>There is not enough storage space. Please contact the administrator.</td>
<td>格納先の容量が不足しています。管理者へお問い合わせください。</td>
<td><p>格納先の容量が不足している場合</p>
<p>※v0.9.22ではエラーチェックがないため出力されない</p></td>
</tr>
<tr class="odd">
<td>15</td>
<td>エラー</td>
<td>Import is in progress on another device.</td>
<td>他の端末でインポートを実行中です。</td>
<td>一括登録を実行中に他の端末が Admin&gt;Items&gt;Import 画面を開いた場合</td>
</tr>
<tr class="even">
<td>16</td>
<td>エラー</td>
<td>Import is in progress.</td>
<td>インポートを実行中です。</td>
<td>一括登録を実行している端末が Admin&gt;Items&gt;Import 画面を開いた場合（他のブラウザで開いたとき，"Result"タブから再度"Import"タブに遷移したとき等）</td>
</tr>
<tr class="odd">
<td>17</td>
<td>エラー</td>
<td>Cannot update because the corresponding item is being edited.</td>
<td>該当アイテムが編集中のため更新できません。</td>
<td>個別のアイテム編集中に、一括登録を実施した場合</td>
</tr>
<tr class="even">
<td>18</td>
<td>エラー</td>
<td>The corresponding item has been deleted.</td>
<td>該当アイテムは削除済です。</td>
<td>個別のアイテム削除後に、一括登録を実施した場合</td>
</tr>
<tr class="odd">
<td>19</td>
<td>ワーニング</td>
<td>The specified {} does not exist in system.</td>
<td>指定された{}はシステムに存在しません。</td>
<td>指定したPOS_INDEXなどの指定した１つの項目がシステムに存在しない場合</td>
</tr>
<tr class="even">
<td>20</td>
<td>ワーニング</td>
<td>Specified {} and {} do not exist in system.</td>
<td>指定された{}と{}はシステムに存在していません。</td>
<td>指定したPOS_INDEX、INDEX_IDなどの複数項目がシステムに存在しない場合</td>
</tr>
<tr class="odd">
<td>21</td>
<td>ワーニング</td>
<td>Specified {} does not match with existing index.</td>
<td>指定された{}はシステムのものと一致していません。</td>
<td>指定したPOS_INDEXはシステムのものと一致していない場合</td>
</tr>
</tbody>
</table>

  - 「ダウンロード」（Download）ボタン  
    画面に表示されているアイテムのリストをTSV形式でダウンロードできる
    
      - 文字コードはBOM無しUTF-8、改行コードはLFとする
    
      - タイトル等トリミングされている場合は、ファイルにはすべて出力されるようにする
    
      - ファイル名は「Check\_ダウンロード日付.tsv」とする

  - 「インポート」（Import）ボタン  
    読み込んだTSVファイルのアイテムを登録する
    
      - 処理途中に問題があるアイテムがあっても、一括登録処理は中断させず、次のアイテムの処理に進む
    
      - 大量登録時のセッションタイムアウトを防ぐように、処理は非同期処理とする
    
      - インデックスには
        
          - インデックスID及びPOS\_INDEX\[n\]を元に指定する
            
              - POS\_INDEX\#nnが複数指定されている場合はそれぞれに登録する
            
              - インデックスIDとPOS\_INDEX\[n\]が不整合の場合は、ワーニングメッセージを出力して、IndexID\[n\]で指定したインデックスに登録する
    
      - DOI/CNRI付与には（「識別子変更モード」（Change Identifier Mode.）チェックボックスにチェックを入れる場合）
        
          - 新規で一括登録するアイテムに、DOI\_RAの設定に従い、指定したDOI（JaLC, Crossref, DataCite, NDL JaLC）及びCNRIをpidstoreに登録できる
        
          - 既存のアイテムに、DOI\_RAの設定に従い、登録されているDOI（JaLC, Crossref, DataCite, NDL JaLC）及びCNRIを変更できる  
            pidstoreに存在する該当レコードを論理削除して指定したDOIを登録する
        
          - DOI/CNRI付与の処理はワークフローのIdentifier Grantで指定した時と同じ処理である
    
      - ワークフローには
        
          - 該当アイテムタイプのワークフローが存在する場合、このワークフローが対象とする
        
          - 該当アイテムタイプのワークフローが存在しない場合、新しいワークフローを作成、メタデータ登録(Item Registrationアクション)まで完了している
        
          - デフォルトフロー名：「Registration Flow」  
            アクション：Start -\> Item registration -\> End
        
          - デフォルトワークフロー名：該当アイテムタイプ名
    
      - アイテム公開／非公開は、一括登録用ファイルの内容に合わせる
    
      - 既存のアイテムを更新するときに値（必須項目以外）を空欄にしてインポート更新をした場合、空欄となったメタデータは削除として更新される
    
      - 「インポート」（Import）ボタン押下後、結果タブの画面に遷移する

4.5. 「結果」（Result）タブで一括登録の結果を表示する

  - 「結果」（Result）タブ  
    最後に実施したアイテム一括登録の状況をリスト形式で確認する  
    初期値は表のヘッダ部分のみ表示されているものとし、以降は最後に一括登録を実施したときのリストが表示される  
    1000ミリ秒ごとに状況を取得し、画面に表示する  
    すべてのインポートが成功または失敗したら、それ以降は状況を取得しない
    
      - 表示項目は以下の通りである
        
          - 「No.」  
            読み込んだTSVファイルのアイテムの通し番号を表示する
        
          - 「開始日」（Start Date）  
            \[Import\]ボタン押下後、1アイテムに対して登録処理を開始した日時を表示する  
            フォーマット：YYYY-MM-DD hh:mm:ss  
            登録処理開始後でも、ソース上で定義されていないエラーによる異常終了の場合は空白となる
        
          - 「終了日」（End Date）  
            1アイテムに対して登録処理が完了した日時を表示する
        
          - フォーマット：YYYY-MM-DD hh:mm:ss
        
          - 「アイテムID」（Item Id）  
            各アイテムのアイテムIDを表示する
        
          - 「アクション」（Action）  
            各アイテムがワークフローのどのアクションにいるかを表示する  
            初期状態では空欄、開始後に「Start」、正常終了で「終了（End）」、異常終了で「Error:（エラーメッセージ）」  
            ただし、ソース上で定義されていないエラーによる異常終了の場合は「Start」
        
          - 「ワークフローステータス」（Work Flow Status）  
            各アイテムのワークフローのステータスがどの状態かを表示する
    
      - 「ダウンロード」（Download）ボタン  
        画面に表示されているアイテムのリストをTSV形式でダウンロードできる
        
          - 文字コードはBOM無しUTF-8、改行コードはLFとする
        
          - タイトル等トリミングされている場合は、ファイルにはすべて出力されるようにする
        
          - ファイル名は「List\_ダウンロード日付.tsv」とする

その他

  - インポートのtsvファイルでファイル情報が無いにもかかわらず、「ファイル情報 \[1\] 」や「ファイル情報 \[2\] 」のヘッダがインポートファイルの中に存在している（ファイル情報 \[0\] は存在している）場合であっても、エラーとならないように対応

  - DOIの自動採番ルールは以下の通り
    
      - 識別子変更モード
    
      - DOIの自動採番は行わない
        
          - インポートファイルにdoiやprefixが含まれている場合はエラーメッセージを表示する。
            
              - DOIが空欄の場合  
                　「Please specify DOI prefix/suffix.」
            
              - インポートファイルにdoiやprefixが含まれている場合　(「prefix」もしくは「prefix/」を指定した場合）  
                　「DOI suffixを設定してください。」／「Please specify DOI suffix.」
    
      - Not 識別子変更モード
        
          - 以下の条件をすべて満たしたときにDOIを付与する
            
              - Admin \> Setting \> Identifier でprefixの設定があること
            
              - DOI：空欄であること
            
              - DOI\_RA：JaLC, Crossref, DataCite, NDL JalC のいずれかであること

  - 「Not 識別子変更モード」で、既存アイテム(DOI付与無し)に自由記述でDOIをインポートしようとした際にエラーメッセージを出す
    
      - 「指定された{DOI}が登録済みの{DOI}と異なっています」

  - DOIの付与はPID付与の制約条件表 ( JPCOAR\_JaLC\_Guideline\_appendix\_v1.pdf ) に従って、「必須」と「いずれか必須」の条件をもとにDOI付与可否を決定している。  
    なお、必須のマッピング項目がひとつのアイテムタイプ内に複数ある場合、複数あるうちのひとつだけ入力されていれば、DOI付与の条件を満たすものとする。

  - DOI付与済みアイテムを新規登録後、更新時に必須項目の値の削除や必須項目のプロパティの削除はできない。  
    削除をした場合、インポートタブのチェック処理で「PID付与の条件を満たしていません。」とエラーメッセージが表示される。  
    また、更新時に資源タイプ（dc:type）の変更は同じコンテンツ種類内でのみ許可される。それ以外の資源タイプに変更した場合、インポートタブのチェック処理で「DOI付与済みアイテムの資源タイプの変更はできません。」とエラーメッセージが表示される。

  - 制限公開用プロパティもインポートすることができる
    
      - 制限公開用プロパティ: 利用規約情報、アクセス(制限公開)、データタイプ、提供方法（ワークフロー、ロール）

  - インポートしたアイテムは、操作アカウントによって作成されたものとして扱われる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-admin

  - > weko-search-ui

<!-- end list -->

  - > 処理概要

1 処理に関するエトセトラ

  - アイテムタイプ項目のチェックに使用しているライブラリ

  - zipファイルの解凍に使用しているライブラリ：zipfile

  - インポート実行時のceleryタスク

  - 識別子変更モードを指定した際のpidstroreの処理について

  - 作成者プロパティの「iscreator」画面表示同様、TSVファイルに出力しないよう制御している

  - depositの「owners」が空欄になっていた場合でも"list index out of range"のエラーが発生しないようにエラーハンドリング処理を追加

  - インポート処理に例外が発生してもESに存在しているアイテム情報が消えないように実装

  - DOIを取り下げたアイテムは、インデックスの状態に関係なくインポートが機能し、ワークフローで編集できる

  - ユーザのセッション有効時間を超過した場合でもインポート処理は完了する

  - ※インポート処理完了後に、celeryタスクの処理で、作業用のテンポラリディレクトリを削除する

2\. tmpディレクトリ

  - 登録されたインポートファイルのチェックをする際に作成するテンポラリファイルは以下のように生成する
    
      - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_import\_xxxxxxxx

  - アイテムをインポートする際に作成するテンポラリファイルは以下のように生成する
    
      - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_import\_YYYYMMDDhhmmss

3\. 設定

  - 一括登録画面のテンプレートを設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L87>
    
      - 設定キー：WEKO\_ITEM\_ADMIN\_IMPORT\_TEMPLATE
    
      - 現在の設定値：

> WEKO\_ITEM\_ADMIN\_IMPORT\_TEMPLATE = 'weko\_search\_ui/admin/import.html'

  - 「インポート」（Import）タブ にてダウンロードファイルに表示する項目を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L512>
    
      - 設定キー：WEKO\_IMPORT\_CHECK\_LIST\_NAME
    
      - 現在の設定値：

> WEKO\_IMPORT\_CHECK\_LIST\_NAME = \["No", "Item Type", "Item Id", "Title", "Check result"\]

  - 「結果」（Result）タブにてダウンロードファイルに表示する項目を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L514>
    
      - 設定キー：WEKO\_IMPORT\_LIST\_NAME
    
      - 現在の設定値：

> WEKO\_IMPORT\_LIST\_NAME = \[
> 
> "No",
> 
> "Start Date",
> 
> "End Date",
> 
> "Item Id",
> 
> "Action",
> 
> "Work Flow ",
> 
> \]

  - メール形式（フィードバックメール）を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L524>
    
      - 設定キー：WEKO\_IMPORT\_EMAIL\_PATTERN
    
      - 現在の設定値：

> WEKO\_IMPORT\_EMAIL\_PATTERN = r"(^\[a-zA-Z0-9\_.+-\]+@\[a-zA-Z0-9-\]+\\.\[a-zA-Z0-9-.\]+$)"

  - tsvファイルに正当となる公開ステータスを設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L525>
    
      - 設定キー：WEKO\_IMPORT\_PUBLISH\_STATUS
    
      - 現在の設定値：

> WEKO\_IMPORT\_PUBLISH\_STATUS = \['public', 'private'\]

  - tsvファイルに正当となるDOI\_RAの値を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L526>
    
      - 設定キー：WEKO\_IMPORT\_DOI\_TYPE
    
      - 現在の設定値：

> WEKO\_IMPORT\_DOI\_TYPE = \["JaLC", "Crossref", "DataCite", "NDL JaLC" \]

  - 日付(ISO-8601)プロパティのサブアイテムキーを設定する  
    日付形式のバリデーションチェックに使用する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L528>
    
      - 設定キー：WEKO\_IMPORT\_SUBITEM\_DATE\_ISO
    
      - 現在の設定値：

> WEKO\_IMPORT\_SUBITEM\_DATE\_ISO = "subitem\_1582683677698"

  - 免責事項表示の対応言語を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L532>
    
      - 設定キー：WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FILE\_LANGUAGES
    
      - 現在の設定値：

> WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FILE\_LANGUAGES = \['en', 'ja'\]

  - 免責事項ファイルの配置先を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L534>
    
      - 設定キー：WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FILE\_LOCATION
    
      - 現在の設定値：

> WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FILE\_LOCATION = (
> 
> "/code/modules/weko-search-ui/weko\_search\_ui/static/change\_identifier\_mode/"
> 
> )

  - 免責事項ファイルのプレフィックスを設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L538>
    
      - 設定キー：WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FIRST\_FILE\_NAME
    
      - 現在の設定値：

> WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FIRST\_FILE\_NAME = "change\_identifier\_mode"

  - 免責事項ファイルの拡張子を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py#L540>
    
      - 設定キー：WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FILE\_EXTENSION
    
      - 現在の設定値：

> WEKO\_ADMIN\_IMPORT\_CHANGE\_IDENTIFIER\_MODE\_FILE\_EXTENSION = ".txt"

  - POS\_INDEXの区切り文字を設定する
    
      - パス：modules/weko-items-ui/weko\_items\_ui/config.py
    
      - 設定キー：WEKO\_ITEMS\_UI\_INDEX\_PATH\_SPLIT
    
      - 現在の設定値：

> WEKO\_ITEMS\_UI\_INDEX\_PATH\_SPLIT = '///'

  - インポート実行時のセッション
    
      - パス：modules/ weko-admin/weko\_admin/config.py
    
      - 設定キー：WEKO\_ADMIN\_IMPORT\_PAGE\_LIFETIME
    
      - 現在の設定値：

> WEKO\_ADMIN\_IMPORT\_PAGE\_LIFETIME = 43200

4\. 実装方法

  - 対応しているモジュール：weko\_search\_ui

  - depositの「owners」が空欄になっていた場合でも"list index out of range"のエラーが発生しないようにエラーハンドリング処理を追加

  - インポート処理に例外が発生してもESに存在しているアイテム情報が消えないように実装

5\. tmpディレクトリ

  - 登録されたインポートファイルのチェックをする際に作成するテンポラリファイルは以下のように生成する
    
      - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_import\_xxxxxxxx

  - アイテムをインポートする際に作成するテンポラリファイルは以下のように生成する
    
      - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_import\_YYYYMMDDhhmmss

  - テンポラリファイルの格納先は環境変数(docker-compose.yml) で設定できるようにする  
    <https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir>

6. 排他処理

インポート処理中「cache::import_start_time」キーに現在時間を格納する。キーは/admin/items/import/check_import_is_availableを呼び出すことでインポート処理の有無を確認しキーを削除する。


【補足】Import機能と個別登録(WorkFlow)の違い

  - Import機能はTSVファイルの文法チェックを実施しています。

  - メタデータ項目チェック（※）は共通処理（Draft4Validator）を使っていますが、他のチェック処理（tsvのインデックス名・ID、CNRI/DOIのチェック）は共通化できないので、別々に実装されています。  
    ※必須項目チェック、入力データ型とアイテムタイプに定義されたデータ型と同じになるかのチェック。

  - 個別登録と一括登録のチェック処理を別に実装している理由は、チェックするタイミングでデータの構成が違っているため、共通処理が使えません。
    
      - 個別登録のチェックタイミング：Identifier Grantの時に、メタデータが存在しているので、それを元にチェックする。
    
      - 一括登録のチェックタイミング：メタデータがなくて、tsvファイルに指定されたデータを変換しチェックする。

その他補足

（Wikiより）

  - 「System」としている項目（"資源タイプResource", "出版タイプResource", "アクセス権Resource"）を一括登録時に自動で設定する機能に関して、  
    自動設定の前提として、対象のアイテムタイプについて各項目がAdmin\>ItemTypes\>MappingでJPCOARスキーマのマッピングが設定されている必要があります

  - インポート更新時にに資源タイプ（dc:type）の変更は同じコンテンツ種類内でのみ許可される。それ以外の資源タイプにを変更した場合、インポートタブのチェック処理で以下のようにエラーメッセージが表示される。
    
      - 「DOI 付与済みアイテムの資源タイプの変更はできません。」

  - 同じコンテンツファイル（ファイル名とファイルパスが同一）を含んだインポートファイル（zip）をインポートした場合のファイルの格納方法は以下の通り。
    
      - Keep: ファイルは上書きされる
    
      - Upgrade: ファイルは新しく格納される

  - インポートのtsvファイル内のメタデータにおける"\<br/\>"は、インポートの際に"\\n"に置換する

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
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>
