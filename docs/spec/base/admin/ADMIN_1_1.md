### メタデータ

<!-- end list -->

  - > 目的・用途

本機能は、アイテムタイプの管理を行う機能である。

アイテムタイプの新規登録、コピー、バージョンアップ、削除、エクスポート、インポート、および削除済みアイテムタイプの復元ができる。

  - > 利用方法

【Administration \> アイテムタイプ管理（Item Types） \> メタデータ（Metadata）画面】にて操作する。

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

  - > メタデータ画面の上部に、アイテムタイプの種類を選択するラジオボタン、アイテムタイプを選択するプルダウンを設ける。

  - > 上記項目の右側に、［エクスポート］ボタン、［インポート］ボタンを設ける。

  - > メタデータ画面の下部に、アイテムタイプの詳細と操作内容を表示する領域を設ける。

  - > アイテムタイプの選択
    
      - ラジオボタンで、アイテムタイプの種類を以下の3つから選択できる。選択内容によって、プルダウンに表示されるアイテムタイプが変わる。
        
          - > ［標準アイテムタイプ］ラジオボタンにチェックを入れる場合、  
            > セレクトボックスではアイテム登録に利用できるアイテムタイプが表示される。
        
          - > ［ハーベスト用アイテムタイプ］ラジオボタンにチェックを入れる場合、  
            > セレクトボックスではハーベストに利用できるアイテムタイプが表示される。
        
          - > ［削除済みアイテムタイプ］ラジオボタンにチェックを入れる場合、  
            > セレクトボックスでは削除されたアイテムタイプが表示される。
        
          - > 画面表示時は［標準アイテムタイプ］ラジオボタンが選択された状態である。
    
      - プルダウンでは、ラジオボタンの選択に応じたアイテムタイプが表示される。
        
          - > このプルダウンで選択したアイテムタイプに対して各種操作を実施する。
        
          - > 各アイテムタイプ名の末尾には、item\_typeテーブルの「tag」が追加されて表示される。
    
      - 各アイテムタイプに実施できる操作は以下の通りである。

<table>
<thead>
<tr class="header">
<th>（凡例）</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>〇：できる　×：できない</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>#</td>
<td>操作</td>
<td>標準<br />
アイテムタイプ</td>
<td>ハーベスト用<br />
アイテムタイプ</td>
<td>削除済み<br />
アイテムタイプ</td>
</tr>
<tr class="odd">
<td>1</td>
<td>追加</td>
<td>〇</td>
<td>〇</td>
<td>×</td>
</tr>
<tr class="even">
<td>2</td>
<td>メタデータ編集</td>
<td>〇</td>
<td>〇</td>
<td>×</td>
</tr>
<tr class="odd">
<td>3</td>
<td>マッピング設定</td>
<td>〇</td>
<td>〇</td>
<td>×</td>
</tr>
<tr class="even">
<td>4</td>
<td>名前の変更</td>
<td>〇</td>
<td>〇</td>
<td>×</td>
</tr>
<tr class="odd">
<td>5</td>
<td>コピー</td>
<td>〇</td>
<td>〇</td>
<td>×</td>
</tr>
<tr class="even">
<td>6</td>
<td>削除</td>
<td>〇</td>
<td>×</td>
<td>×</td>
</tr>
<tr class="odd">
<td>7</td>
<td>復元</td>
<td>×</td>
<td>×</td>
<td>〇</td>
</tr>
<tr class="even">
<td>8</td>
<td>エクスポート</td>
<td>○</td>
<td>×</td>
<td>×</td>
</tr>
<tr class="odd">
<td>9</td>
<td>インポート</td>
<td>○</td>
<td>×</td>
<td>×</td>
</tr>
</tbody>
</table>

  - マッピング設定は、マッピング画面で実施する。詳細は[ADMIN-1-2: マッピング](#マッピング)を参照。

<!-- end list -->

  - 対応している標準アイテムタイプは以下の通りである。
    
      - 「デフォルトアイテムタイプ（シンプル）」
    
      - 「デフォルトアイテムタイプ（フル）」
        
          - 「デフォルトアイテムタイプ（シンプル）」「デフォルトアイテムタイプ（フル）」の詳細は別紙「デフォルトアイテムタイプの作成v4.xlsx」を参照。
    
      - 「DDI」
        
          - 「DDI」の詳細は別紙「DDIアイテムタイプ修正の仕様ver6\_訂正案.xlsx」を参照。

  - 対応している制限公開用のアイテムタイプは以下の通りである。
    
      - 「利用申請」
    
      - 「二段階利用申請」
    
      - 「利用報告-Data Usage Report」

  - 対応しているハーベスト用アイテムタイプは以下の通りである。
    
      - 「Thesis」
    
      - 「Sound」
    
      - 「Article」
    
      - 「Report」
    
      - 「Book」
    
      - 「Patent」
    
      - 「Cartographic Material」
    
      - 「Lecture」
    
      - 「Image」
    
      - 「Conference Object」
    
      - 「Dataset」
    
      - 「Multiple」
    
      - 「Harvesting DDI」

  - アイテムタイプの追加
    
      - アイテムタイプを新規作成する場合は、アイテムタイプを選択するプルダウンで、空白を選択する。
    
      - 「公開日」（Publish Date）はデフォルトの項目として常に表示されている。アイテム登録画面で入力必須の項目のため、オプションの「必須」はチェックありで変更できない。
    
      - 「アイテムタイプ」（Item Type）テキストボックスにアイテムタイプの名前を入力する。
        
          - アイテムタイプの名前は、既存のものと重複してはならない。
    
      - 「新規登録」（New Registration）ラジオボタンを選択する。
    
      - 「メタデータ追加」（Add Metadata）を押すことで、新規メタデータを追加する。
        
          - メタデータ項目名
            
              - 「アイテム名」（Item Name）カラムのテキストボックスでメタデータ項目名を設定できる。
            
              - 「アイテム名」（Item Name）カラムに「Localization Settings」リンクを設ける。リンクを押すと、多言語の項目名の名称入力エリアを表示する。  
                ※設定された項目名はアイテム登録・編集画面、アイテム詳細画面に表示される。
                
                  - 対応している言語は日本語と英語とする。  
                    デフォルトは空白とする。
                    
                      - システム言語が日本語の場合、［Japanese］で設定された項目名が表示される。
                    
                      - システム言語が日本語以外の場合、［English］で設定された項目名が表示される。
                    
                      - 設定しない場合は、表示言語設定に関わらず、当該画面で設定している項目名が表示される。
        
          - メタデータ属性
            
              - 「属性」（Attribute）カラムのプルダウンでメタデータ属性を設定できる。※メタデータ属性の設定については、以下の「メタデータ項目の内容」を参照。
            
              - 「属性」（Attribute）カラムに「Localization Settings」リンクを設ける。リンクを押すと、多言語の子項目名の名称入力エリアを表示する。  
                ※設定された項目名はアイテム登録・編集画面、アイテム詳細画面に表示される。
                
                  - 対応している言語は日本語と英語とする。  
                    デフォルトは空白とする。
                    
                      - システム言語が日本語の場合、［Japanese］で設定された子項目名が表示される。
                    
                      - システム言語が日本語以外の場合、［English］で設定された子項目名が表示される。
                    
                      - 設定しない場合は、［Properties］画面に設定された子項目名が表示される。
        
          - メタデータ項目の内容
            
              - 項目に対して
                
                  - メタデータ行での「オプション」（Option）カラムに表示形式を設定する。表示形式を複数設定できる
                
                  - 設定できるオプションは以下の通りである。
                    
                      - 「必須」（Required）：アイテム登録時に\*を表示し、必須入力のメタデータにする。
                        
                          - 「公開日」（Publish Date）は必須項目であるため、初めからチェックが入っており、外すことができない。
                    
                      - 「Multiple」（Allow Multiple）：アイテム登録時に［+New］を表示し、メタデータの複数入力を可能にする。
                        
                          - 選択すると、最低限と最大限の項目を設定できる
                        
                          - デフォルト：  
                            最低限の項目：「1」  
                            最大限の項目：「9999」
                    
                      - 「リスト表示」（Show List）：アイテム一覧画面にメタデータをカンマ区切りで一覧に表示される。
                        - 例外：アイテムタイプのサムネイルプロパティのオプションで「Show List」が"ON"になっているときに、アイテムリストへアップロードされたサムネイルファイルを表示する。アイテムに複数のサムネイルファイルがアップロードされている場合、アイテム詳細画面の１つ目のサムネイルファイルを表示する。
                        - 例外：アイテムタイプの作成者プロパティののオプションで「Show List」が"ON"になっているときに、著者IDはアイコンで表示する。ORCIDの場合はORCIDアイコン、それ以外の識別子は頭文字を利用したアイコン表示となる。
                        - アイテムタイプのファイルプロパティののオプションで「Show List」が"ON"になっているときに、ファイルのタイプを示すボックスを表示する。
                    
                      - 「改行を指定」（Specify Newline）：アイテム一覧画面にメタデータを改行で表示される
                    
                      - 「Hide」：ログインの有無に関わらずインデックス、キーワードサーチ結果、CiteAs、アイテム詳細、OAI-PMHを含む外部出力にメタデータの詳細を表示しない。アイテムエクスポートのみ、ログインユーザにはhide項目を出力する。
                    
                      - 「Display on one line」:
                        
                          - 「トピック」のような繰り返し可の項目は1つのセルにまとめて表示して、個々の値はカンマ等で区切る。
                        
                          - アイテムタイププロパティ「Time Period」「collDate」「H\_Time Period」等、Eventのstart、endにて範囲指定が可能な日付は、横に並べてスラッシュで結ぶ。
                        
                          - 「公開日」（Publish Date）の行には表示されない。
                
                  - メタデータ行での「Notes」カラムにメモを残せる
                
                  - メタデータ行での「置換」（Replacement）カラムに［↑］または［↓］ボタンが表示される。これらを押すことで、メタデータ属性入力エリアの表示位置が入れ替わる。
                
                  - 「公開日」（Publish Date）の行にはこれらのボタンが表示されず、必ず１番上になる。
                
                  - ※「公開日」（Publish Date）の１つ下の項目は、［↑］ボタンが無効になって、1番下の項目は、［↓］ボタンが無効になる。
                
                  - メタデータ行での「削除」（Delete）カラムに［×］ボタンが表示される。これを押すことで、メタデータを削除する。
                    
                      - 「公開日」（Publish Date）は必須項目であるため、［×］ボタンが表示されず、削除できない。
            
              - 子項目に対して
                
                  - 【Properties画面】で「"editAble": true」を設定した子項目は、当該画面で設定内容を編集できる
                    
                      - 子項目について、入力形式が「Select」「Radios」「Checkboxes」の場合は当該画面でいずれかの選択ができる
                    
                      - 子項目ごとに、アイテム詳細画面およびアイテム登録画面（ワークフローのItem Registration）で表示する項目名を編集できる
                    
                      - 子項目ごとに、「Required」「Show List」「Specify Newline」「Hide」「Non Display on Detail」の設定ができる
                    
                      - 「Non Display on Detail」が指定された場合は詳細画面に当該項目を表示しない
                    
                      - システム入力項目タイプ（S\_から始まる入力項目タイプ）をプルダウンに表示しない
                
                  - 「"editAble": true」が設定されていない場合、選択肢の入力エリアは非活性で表示される
            
              - オプションの優先度について  
                親要素と子要素のオプションの優先度は、以下の通りとする。

| \[凡例\]●：チェックあり -：チェックなし |    |    |               |
| ----------------------- | -- | -- | ------------- |
| \#                      | 親  | 子  | オプション         |
| 1                       | ●  | \- | 子要素全体に適用      |
| 2                       | \- | ●  | 指定された子要素のみ適用  |
| 3                       | ●  | ●  | 親のみ選択された状況と同様 |

  - 「保存」（Save）ボタンを押すと、アイテムタイプを保存する。  
    新規作成されたアイテムタイプは「標準アイテムタイプ」のリストの末尾に追加される。

  - アイテムタイプIDは、item\_typeテーブルでシーケンスのnextvalによって払い出される。

  - 新規作成されたアイテムタイプのアイテムタイプIDは、40001以降になる。

<!-- end list -->

  - アイテムタイプのコピー
    
      - アイテムタイプ種類（標準アイテムタイプ、またはハーベスト用アイテムタイプ）を選択する。
    
      - アイテムタイプ選択プルダウンより、コピーするアイテムタイプを選択する。
    
      - アイテムタイプ名を入力して、「新規登録」（New Registration）ラジオボタンを選択した状態で、「保存」（Save）ボタンを押すと、アイテムタイプが保存される。
        
          - アイテムタイプのバージョン情報は引き継がないものとする。
        
          - ハーベスト用アイテムタイプをコピーした場合は、標準アイテムタイプとして保存する。

  - アイテムタイプの編集
    
      - アイテムタイプの名前
        
          - アイテムタイプ選択プルダウンより変更するアイテムタイプを選択された状態で、アイテムタイプ名を入力して、「バージョンアップ」（Version Upgrade）ラジオボタンを選択してから、「保存」（Save）ボタンを押すと、アイテムタイプの名前が保存される。
        
          - 「保存」（Save）ボタンを押すと、編集内容を保存する
            
              - アイテムタイプのバージョンを更新しない操作について以下の通りである
                
                  - オプションを変更する
                
                  - 項目の表示位置を並び替える
                
                  - ［Notes］にメモを変更する
                
                  - 変更しないで、［保存］を押す
    
      - インポート中はアイテムタイプの編集不可とする。

  - アイテムタイプの削除
    
      - アイテムタイプを表示した状態で「削除」（Delete）ボタンを押すと、削除確認用のダイアログが表示される  
        メッセージ：  
        日本語：「このアイテムタイプを削除してよろしいですか？」  
        英語：「Are you sure you want to delete this Item type?」
        
          - 「継続」（Continue）ボタンを押すと、アイテムタイプを選択するプルダウンで選択されているアイテムタイプが論理削除される。その後、メタデータ画面を再読み込みする。
        
          - 「キャンセル」（Cancel）ボタンを押すと、削除確認用のダイアログを閉じる
    
      - ただし、以下の場合は削除不可とする
        
          - ハーベスト用のアイテムタイプは、ハーベスト用アイテムは削除できない旨のメッセージを表示のうえ削除不可とする
        
          - 標準アイテムタイプのうち所属アイテムが存在するアイテムタイプは、所属アイテムが存在するため削除できない旨のメッセージを表示のうえ削除不可とする
    
      - インポート中はアイテムタイプの削除は不可とする。

  - 論理削除したアイテムタイプを復元できる
    
      - アイテムタイプ作成/編集画面に「復元」（Restore）ボタンを設ける
    
      - 「削除済みアイテムタイプ」（Deleted Item Type）ラジオボタンを選択した時のみに、「復元」（Restore）ボタンを活性化とする
    
      - アイテムタイプの復元手順は以下の通りである
        
          - 削除済みアイテムタイプ」（Deleted Item Type）ラジオボタンを選択すると、アイテムタイプ選択プルダウンに削除されたアイテムタイプが一覧表示される。
        
          - プルダウンより復元したいアイテムタイプを選択し、「復元」（Restore）ボタンを押すと、該当アイテムタイプが「標準アイテムタイプ」（Standard Item Type）プルダウンより選択可能となり利用可能となる。（「削除済みアイテムタイプ」（Deleted Item Type）プルダウンからは削除される）

  - テキストプロパティ⇔テキストエリアプロパティ以外のプロパティは変更できないように、アイテムタイプに存在するプロパティのプルダウンリストを非活性にする

  - 新規にプロパティを追加する場合は、従来通りプロパティは選択できるようにする

  - 以下のプロパティの子要素については「Separate options with the | character」と表示する  
    これらの項目はプロパティ画面では情報を管理せず、アイテム登録／編集時に自動的に選択肢を表示する
    
      - 作成者プロパティ「作成者識別子Scheme」
    
      - 寄与者プロパティ「寄与者識別子Scheme」
    
      - 権利者情報プロパティ「権利者識別子Scheme」
        
          - アイテム登録／編集時に表示される「作成者識別子Scheme」,「寄与者識別子Scheme」,「権利者識別子Scheme」の選択肢はAuthor Management画面のID PrefixタブにあるScheme（authors\_prefix\_settingsテーブルに登録されているもの）を参照している
    
      - ファイル情報プロパティ「日付タイプ」「グループ」「ライセンス」
        
          - 「日付タイプ」はコンテンツファイル登録時の公開日として"Available"が自動設定される（Item Registration画面にはプルダウンリストが表示されない）
        
          - 「グループ」は作成したユーザーアカウントの管理画面で作成したグループ（accounts\_groupテーブルに登録されているもの）を参照している
        
          - > 「ライセンス」はCCライセンス情報を参照している
            
              - > modules/weko-records-ui/weko\_records\_ui/config.pyのWEKO\_RECORDS\_UI\_LICENSE\_DICTで定義している。
            
              - > これを、scripts/instance.cfgのWEKO\_RECORDS\_UI\_LICENSE\_DICTで上書きしている。current\_app.config\['WEKO\_RECORDS\_UI\_LICENSE\_DICT'\]はscripts/instance.cfgの方を参照する。

  - エクスポート
    
      - ［標準アイテムタイプ］ラジオボタンを選択して、プルダウンのアイテムタイプを選択した状態で、［エクスポート］ボタンを押すと、そのアイテムタイプの定義を表すJSONファイルを含んだZIPファイルがダウンロードされる。
    
      - 存在しないアイテムタイプ、削除済みアイテムタイプ、ハーベスト用アイテムタイプの場合はエクスポートされない。

  - インポート
    
      - ［インポート］ボタンを押すと、画面に「Import」エリアが表示される。
    
      - ［ファイルを選択］ボタンを押すと表示されるファイル選択ダイアログで、エクスポートされたZIPファイルを選択する。
    
      - 「Item Type」テキストボックスにアイテムタイプ名を入力する。
    
      - ［Execute Import］ボタンを押すと、「Item Type」テキストボックスに入力したアイテムタイプ名でアイテムタイプが取り込まれる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko-itemtypes-ui

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - HTMLテンプレート
    
      - パス：<https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L29-L31>
        
          - 設定キー: WEKO\_ITEMTYPES\_UI\_ADMIN\_REGISTER\_TEMPLATE = \\  
            'weko\_itemtypes\_ui/admin/create\_itemtype.html'  
            """Register template for the item type page."""

  - デフォルトプロパティの表示・非表示
    
      - パス: <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L44-L45>
        
          - 設定キー: WEKO\_ITEMTYPES\_UI\_SHOW\_DEFAULT\_PROPERTIES = True  
            """Set to show or hide default properties on the item type page."""  
            デフォルト：True（表示）。False: 非表示。

  - デフォルトプロパティ一覧
    
      - パス: <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L47-L55>
        
          - 設定キー: WEKO\_ITEMTYPES\_UI\_DEFAULT\_PROPERTIES = {  
            '1': {'name': \_('Text Field'), 'value': 'text'},  
            '2': {'name': \_('Text Area'), 'value': 'textarea'},  
            '3': {'name': \_('Check Box'), 'value': 'checkboxes'},  
            '4': {'name': \_('Radio Button'), 'value': 'radios'},  
            '5': {'name': \_('List Box'), 'value': 'select'},  
            '6': {'name': \_('Date'), 'value': 'datetime'}  
            }  
            """Default properties of the item type."""

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

  - アイテムタイプのバージョンアップ機能を有効にする・しない設定
    
      - パス: <https://github.com/RCOSDP/weko/blob/hfix/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py#L66-L67>
        
          - 設定キー: = True  
            """Enable Upgrade Version."""  
            True: バージョンアップを有効にする.  
            False: バージョンアップを無効にする

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
