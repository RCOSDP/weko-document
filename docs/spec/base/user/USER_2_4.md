
### アイテム一括出力

  - > 目的・用途

本機能は、検索結果に表示されているアイテムの情報を一括で出力する機能である。

なお、出力されるファイル形式はjson,tsv,bibである。

  - > 利用方法

1\. 【Administration \> 設定(Setting) \> アイテム一括出力(Item Export)画面】の「Allow/Disallow Item Exporting」及び「Export File Contents」をOnに設定する。

2\. いずれかのアイテム検索を行う。

3\. 検索結果エリア、あるいはアイテムリストエリア内にある\[エクスポート(Export)\]ボタンを押下する。

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

<!-- end list -->

  - 【Administration \> 設定(Setting) \> アイテム一括出力(Item Export)画面】に「Allow/Disallow Item Exporting」及び「Export File Contents」がOnに設定している場合
    
      - 検索結果一覧画面に「エクスポート」（Export）ボタンを押下すると、アイテム一括出力画面に遷移する。
    
      - アイテム一括出力画面にボタンを押下したときの検索結果一覧画面のアイテム名を全てリストとして表示する。  
        ※権限によって詳細画面で表示されないメタデータはリストに表示されない。
        
          - アイテムの順序は、ページを読み込んだ際の検索結果一覧の画面を引き継ぐ（並び替えや表示数を変更している場合も反映しないが、変更した後ページリロードをすると反映される。）
        
          - 「Items to Export」エリアの表示内容は以下の通りである。
            
              - 「チェックボックス」、「Item」、「Message」、「No. of Files」  
                が横に並んだ表を表示する。
            
              - 「チェックボックス」の列  
                　すべての項目にチェックボックスを設ける。
                
                  - 列の一番上のチェックボックスを押下することで表示されているページの列全てのチェックボックスのON/OFFができる。
                
                  - 各アイテムのチェックボックスを押下することでON/OFFができる。
                
                  - チェックボックスにチェックが入っているアイテムはエクスポートされる。
            
              - 「Item」の列  
                　各アイテムの名称がリンクとなって表示される。押下するとそのアイテムの詳細画面に遷移する。
            
              - 「Message」の列  
                　システムからのメッセージを表示する。（エラーメッセージ）
            
              - 「No. of Files」  
                　各アイテムのコンテンツファイルの件数を表示する。
    
      - 選択したアイテム数がコンフィグで設定した最大アイテム数を超えた場合、表の上にメッセージが表示される。  
        メッセージ：「Exceeded number of selectable items.」
        
          - アイテム一括出力画面にある「エクスポート」（Export）ボタンが非活性になる。
        
          - チェックを外したときに選択しているアイテムが最大アイテム数以下になった場合は、画面上のメッセージは非表示となり、ボタンも活性化する。
    
      - コンテンツファイルの出力有無
        
          - 「File Contents」エリアにコンテンツファイルも含めて出力するかどうかをラジオボタンで選択できる。
        
          - ラジオボタン：「Do Not Export File Contents」、「Export File Contents」
        
          - 初期値：「Do Not Export File Contents」
    
      - 一括出力する形式の選択
        
          - 「Export Format」エリアに一括出力する形式を選択できる
        
          - 選択できる項目：アイテムの詳細画面でExportできる項目と同様（JSON, BIBTEX）とする
        
          - 初期値：「JSON」
    
      - 「戻る」（Back）ボタン  
        ボタンを押すと、検索結果一覧画面に戻る
    
      - 「エクスポート」（Export）ボタン  
        チェックボックスにチェックがついているアイテムに関してExportできる

  - 【Administration \> 設定(Setting) \> アイテム一括出力(Item Export)画面】の「Allow/Disallow Item Exporting」がOffに設定している場合、  
    検索結果一覧画面に「エクスポート(Export)」ボタンを表示しない。

  - 【Administration \> 設定(Setting) \> アイテム一括出力(Item Export)画面】に「Allow/Disallow Item Exporting」がOnに設定している、かつ「Export File Contents」がOffに設定している場合
    
      - 検索結果一覧画面に「エクスポート(Export)」ボタンを表示する。
    
      - 「File Contents」エリアにコンテンツファイルを出力するかどうかのラジオボタンを非活性にする。
    
      - 「File Contents」エリアの上部にコンテンツファイルが出力できない旨のメッセージを表示する。  
        メッセージ：「File contents cannot be exported.」

  - アイテム一括出力時にダウンロード権限がないものを確認する。
    
      - アイテム一括出力画面を表示したタイミングで、各アイテムのコンテンツの権限を確認し、コンテンツファイルのダウンロード権限が無い場合、該当アイテム行での"Message"列にメッセージを表示する。  
        メッセージ：「Contains restricted content」
    
      - コンテンツのダウンロード権限は、アイテム登録時に設定するコンテンツの公開情報を参照する。[USER-3-2 コンテンツファイル管理](#コンテンツファイル管理)の章を参照すること。

  - エクスポートされるディレクトリ構造

> export.zip
> 
> ├── bag-info.txt
> 
> ├── bagit.txt
> 
> ├── manifest-sha256.txt
> 
> ├── manifest-sha512.txt
> 
> ├── tagmanifest-sha256.txt
> 
> ├── tagmanifest-sha512.txt
> 
> └── data

  - 「data」フォルダーの中身
    
      - エクスポート形式はJSONの場合

> data
> 
> ├──\[アイテムタイプ名(アイテムタイプバージョン)\].tsv
> 
> └──recid\[recidの値\]
> 
> 　　├──ファイル名（コンテンツファイルがある場合）
> 
> 　　└── recid\_\[recidの値\]\_metadata.json

  - エクスポート形式はBIBTEXの場合

> data
> 
> ├──\[アイテムタイプ名(アイテムタイプバージョン)\].bib
> 
> └──recid\[recidの値\]
> 
> 　　├──ファイル名（コンテンツファイルがある場合）
> 
> 　　└── recid\_\[recidの値\]\_metadata.json

  - Items to Exportに表示されるファイル情報は以下のように制御する
    
      - 「公開しない」に設定したファイル情報はItems to ExportのNo. of Filesにはカウントされない
    
      - 「公開しない」に設定したファイル情報はItems to Exportでも出力されない

  - エクスポートの処理は以下の通り
    
      - Unicode正規化（NFKD）を実施する。
    
      - 特別な文字（\&EMPTY&）を変換する（ [~~\#23229~~](https://redmine.devops.rcos.nii.ac.jp/issues/23229) ）
    
      - メタデータをエスケープして出力する（ MarkupSafeライブラリ による処理）
    
      - 改行コード（\\n）→\<br/\> に変換する（ [~~\#23229\#note-6~~](https://redmine.devops.rcos.nii.ac.jp/issues/23229#note-6) ）

  - エクスポートできるファイルサイズは定数「 WEKO\_ITEMS\_UI\_EXPORT\_MAX\_FILE\_SIZE 」にて制限できる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_items\_ui

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 検索結果画面で「エクスポート」ボタンを押下すると、weko\_search\_ui.app.checkForRestrictedContentメソッドとweko\_items\_ui.views.exportメソッドが呼び出される。  
    前者のメソッドでcheck\_restricted\_contentが呼び出され、検索結果の中でダウンロード制限がついていないアイテム情報を取得する。  
    後者のメソッドでは、アイテムエクスポートの設定、検索結果ロード時の検索設定を取得し、  
    それらが反映したアイテムリストを表示する。

  - 「エクスポート」ボタンを押下するとweko\_search\_ui.static.js.weko\_search\_ui.app.exportItemsメソッドが呼び出され、同ファイルのgetExportItemsMetadataを呼び出し選択したアイテムのメタデータを取得する。その取得したメタデータに不足した必須項目があるかを同ファイルのvalidateBibtexExportメソッドで確認し、足りなかったらエラーメッセージをウェブ上に表示する。  
    問題ない場合、weko\_items.ui.views.exportメソッドにてexport\_itemsメソッドを呼び出し、zipファイルを出力する。  
      
    以下は出力するファイルごとの処理を記述する。

  - **コンテンツファイルを含める場合はBagit形式でアイテムを一括出力する**
    
      - 仕様書： 別紙「WEKO3\_BagIt.pptx」を参照すること。
    
      - weko\_items\_ui.utils.export\_itemsメソッドにてbagit.make\_bagを実行することでbagitファイルを生成する。
    
      - コンテンツファイルを含める場合、エクスポート時には登録ファイルが1つのzipファイルに圧縮されてダウンロードされる
    
      - zipファイルは階層構成（Bagit形式）で出力できる
    
      - コンテンツファイルは個々に個別のディレクトリが作成され、その中に出力される（ディレクトリには連番が振られる）
    
      - 一括出力されるアイテムのファイル形式は、アイテム一括出力画面の出力形式に合わせる

  - **ダウンロードするメタデータファイル（tsvファイル）**
    
      - 「Item to Export」エリアの「Export Format」項目でJSONを選び、エクスポートボタンを押す。この操作によって、weko\_items\_ui.utils.export\_itemsメソッドにてwrite\_filesメソッドが呼び出され、JSON形式でtsvファイルが出力される。  
        tsvの形式についてはweko\_items\_ui.utils.make\_stats\_fileメソッドを参照すること。
    
      - ファイル名ルール：\[アイテムタイプ名(アイテムタイプバージョン)\].tsv
    
      - 基本仕様
        
          - TSV形式とする
        
          - 文字コードはBOM無しUTF-8、改行コードはCR+LFとする
        
          - アイテムタイプ毎にファイルを分けて出力する
        
          - ファイル名は「アイテム\_タイプ名.txt」とする
        
          - 1行で1アイテムを記載する
    
      - 詳細仕様
        
          - ヘッダ行
            
              - 先頭の5行はヘッダ行とする
            
              - ヘッダ行は、"\#"で開始する
        
          - ヘッダ各行の詳細
            
              - 1行目 ： アイテムタイプの名称を記載する
                
                  - 1カラム目 ： \#ItemType (固定)
                
                  - 2カラム目 ： アイテムタイプの名称を記載する
                
                  - 3カラム目 ： アイテムタイプのjsonschemaのURLを記載する
            
              - 2行目 ： 各メタデータ項目の内部キーを記載する
                
                  - 内部キーは、JSONPathのルールに従い記載する
            
              - 3行目 ： 各メタデータ項目のラベルを記載する
                
                  - メタデータの階層に応じて、各階層のラベルを"."で連結する
                
                  - 繰り返し可能な項目については、ラベルのサフィックスとして"\#"+連番(1〜)を記載する  
                    (例) 作成者\#1.作成者識別子\#1.作成者識別子
            
              - 4行目 ： 各メタデータがReadonlyであるかを記載する。
                
                  - メタデータがReadonly属性を持つ場合、該当するメタデータの列に”System”と記載する。
            
              - 5行目 ： 各メタデータの設定を記述する。
                
                  - 複数設定項目がある場合は、”,”で連結して記載する。  
                    (例)Required, Allow Multiple
        
          - 各カラム詳細
            
              - 1カラム目 ： アイテムのrecidを記載すること。アイテムの新規登録の場合は、"n"+連番をユーザーが記載する
            
              - 2カラム目 ： アイテムのランディングページのURIを記載する
            
              - 3カラム目〜4+nカラム目 ： アイテムの属するインデックスのIDを記載する  
                　複数指定可
            
              - 3+n+1カラム目〜 : アイテムタイプのメタデータをGUIの表示順に合わせて記載する
        
          - その他
            
              - インデックス  
                インデックスはインデックスIDを記載する
            
              - 作成者  
                WEKOの著者名DBに登録されている場合は、作成者の2階層目のデータとして、weko\_idを追加する【確認中】
            
              - ファイル  
                file\_path\#xxは、ファイルプロパティの\#xxと連番を合わせて対応する
        
          - メタデータファイル(tsv)サンプル  
            別紙「weko3\_tsvformat.xlsx」を参照

  - **各アイテムの情報 BIBTEX形式**  
    別紙「WEKOメタデータ取得API（JPCOAR\_BiBTEX）\_20200106NII案」を仕様書として参照すること
    
      - 「Item to Export」エリアの「Export Format」項目でBIBTEXを選び、エクスポートボタンを押す。この操作によって、weko\_items\_ui.utils.export\_itemsメソッドにてwrite\_bibtex\_filesメソッドが呼び出され、bibファイルが出力される。
    
      - ファイル名のルール：\[アイテムタイプ名(アイテムタイプバージョン)\].bib
    
      - 仕様書での「文献種別別出力フィールド」シート
        
          - 「○ ※必須」：必須項目  
            　一括出力の時に、必須チェックを行う。  
            weko\_items\_ui.utils.make\_bibtex\_dataメソッドにおいてチェックを行っている。
        
          - 「○」：任意項目（ある場合Exportする、ない場合はNULLとしてExportする(項目名のみ)）
        
          - 空白セル：Export対象外項目
    
      - 「○ ※必須」が入力されていない場合、「Export Format」で「BIBTEX」を選択したとき、「エクスポート」（Export）ボタンを押すと、  
        該当アイテム行でのMessageエリアに、以下のようなエラーメッセージを表示する  
        エラーメッセージ：  
        JP：「必須項目がありません」  
        EN：「Required item is not inputted.」
        
          - エラーになるアイテムは出力対象外となる。
    
      - ファイルサンプル  
        別紙「bibtex.txt」

  - **各アイテムのjsonファイル**
    
      - ファイル名ルール：recid\_\[recidの値\]\_metadata.json
    
      - 各アイテム詳細画面左下の「エクスポート」エリアの「JSON」リンクで展開される内容を出力する。

  - エクスポートの最大アイテム数は以下で設定する
    
      - /modules/weko-items-ui/weko\_items\_ui/config.py  
        　WEKO\_ITEMS\_UI\_DEFAULT\_MAX\_EXPORT\_NUM = 100

  - エクスポート処理実行時、weko\_items\_ui.utils.export\_itemsメソッドにてtempfile.TemporaryDirectoryによってtmpファイルが生成される。  
    テンポラリディレクトリのファイル名を以下のように設定する。  
    なお、tmpファイルはエクスポート処理実行後に自動的に削除される。
    
      - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_export\_xxxxxxxx

  - weko\_items\_ui.utils.export\_items  
    <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/utils.py#L1423-L1507>

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
<p>2023/11/11</p>
</blockquote></td>
<td>V0.9.27</td>
<td></td>
</tr>
</tbody>
</table>