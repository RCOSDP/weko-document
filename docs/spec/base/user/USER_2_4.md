# アイテム一括出力

## 目的・用途

本機能は、検索結果に表示されているアイテムの情報を一括で出力する機能である。  
なお、出力されるファイル形式はtsv、bib、RO-Crateである。

## 利用方法

1. 【Administration > 設定(Setting) > アイテム一括出力(Item Export)画面】の「Allow/Disallow Item Exporting」及び「Export File Contents」をOnに設定する。

2. いずれかのアイテム検索を行う。

3. 検索結果エリア、あるいはアイテムリストエリア内にある[エクスポート(Export)]ボタンを押下する。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | -------------- | ---------------- | ------------------ | ------------ | ------------ | ------------------ |
| 利用可否 |       〇       |        〇        |         〇         |      〇      |      〇      |        〇          |

## 機能内容

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

    - 一括出力する形式の選択

        - 「Export Format」エリアに一括出力する形式を選択できる
        - 選択できる項目：アイテムの詳細画面でExportできる項目（TSV, BIBTEX）とRO-Crateの3種とする
        - 初期値：「TSV」

    - コンテンツファイルの出力有無

        - 「File Contents」エリアにコンテンツファイルも含めて出力するかどうかをラジオボタンで選択できる。
        - ラジオボタン：「Do Not Export File Contents」、「Export File Contents」
        - 初期値：「Do Not Export File Contents」
        - 出力形式にRO-Crateを選択した場合は、コンテンツファイルの出力有無のラジオボタンは有に固定され非活性となる。

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

    - エクスポート形式がTSV・BIBTEXの場合

        ```
        export.zip
          ├── bag-info.txt
          ├── bagit.txt
          ├── manifest-sha256.txt
          ├── manifest-sha512.txt
          ├── tagmanifest-sha256.txt
          ├── tagmanifest-sha512.txt
          └── data/
                  ├──[アイテムタイプ名(アイテムタイプバージョン)].tsv or .bib
                  └──recid_[recidの値]/
                  　　    └── ファイル（コンテンツファイルがある場合）
        ```

    - エクスポート形式はRO-Crateの場合

        ```
        export.zip
          └── recod_[recidの値].zip/
                ├── bag-info.txt
                ├── bagit.txt
                ├── manifest-sha256.txt
                ├── tagmanifest-sha256.txt
                └── data/
                        ├── ro-crate-metadata.json
                        └── ファイル（コンテンツファイルがある場合）
        ```

- Items to Exportに表示されるファイル情報は以下のように制御する

    - 「公開しない」に設定したファイル情報はItems to ExportのNo. of Filesにはカウントされない
    - 「公開しない」に設定したファイル情報はItems to Exportでも出力されない

- エクスポートの処理は以下の通り

    - Unicode正規化（NFKD）を実施する。
    - 特別な文字（\&EMPTY&）を変換する（ [~~\#23229~~](https://redmine.devops.rcos.nii.ac.jp/issues/23229) ）
    - メタデータをエスケープして出力する（ MarkupSafeライブラリ による処理）
    - 改行コード（\\n）→\<br/\> に変換する（ [~~\#23229\#note-6~~](https://redmine.devops.rcos.nii.ac.jp/issues/23229#note-6) ）

  - エクスポートできるファイルサイズは定数「 WEKO\_ITEMS\_UI\_EXPORT\_MAX\_FILE\_SIZE 」にて制限できる。



## 関連モジュール

-  weko_items_ui

## 処理概要

検索結果画面で「エクスポート」ボタンを押下すると、weko_search_ui.app.checkForRestrictedContentメソッドとweko_items_ui.views.exportメソッドが呼び出される。  
 前者のメソッドでcheck_restricted_contentが呼び出され、検索結果の中でダウンロード制限がついていないアイテム情報を取得する。  
 後者のメソッドでは、アイテムエクスポートの設定、検索結果ロード時の検索設定を取得し、  
 それらが反映したアイテムリストを表示する。

「エクスポート」ボタンを押下するとweko_search_ui.static.js.weko_search_ui.app.exportItemsメソッドが呼び出され、同ファイルのgetExportItemsMetadataを呼び出し選択したアイテムのメタデータを取得する。  
その取得したメタデータに不足した必須項目があるかを同ファイルのvalidateBibtexExportメソッドで確認し、足りなかったらエラーメッセージをウェブ上に表示する。  
 問題ない場合、weko_items.ui.views.exportメソッドにてexport_itemsメソッドを呼び出し、zipファイルを出力する。  

以下は出力するファイルごとの処理を記述する。

### コンテンツファイルを含める場合はBagit形式でアイテムを一括出力する

- 仕様書： 別紙「WEKO3_BagIt.pptx」を参照すること。
- weko_items_ui.utils.export_itemsメソッドにてbagit.make_bagを実行することでbagitファイルを生成する。
- コンテンツファイルを含める場合、エクスポート時には登録ファイルが1つのzipファイルに圧縮されてダウンロードされる
- zipファイルは階層構成（Bagit形式）で出力できる
- コンテンツファイルは個々に個別のディレクトリが作成され、その中に出力される（ディレクトリには連番が振られる）
- 一括出力されるアイテムのファイル形式は、アイテム一括出力画面の出力形式に合わせる

### ダウンロードするメタデータファイル（tsvファイル）

「Item to Export」エリアの「Export Format」項目でTSVを選び、エクスポートボタンを押す。  
この操作によって、weko_items_ui.utils.export_itemsメソッドにてwrite_filesメソッドが呼び出され、tsvファイルが出力される。  
tsvの形式についてはweko_items_ui.utils.make_stats_fileメソッドを参照すること。

ファイル名ルール：[アイテムタイプ名(アイテムタイプバージョン)].tsv

- 基本仕様

   - TSV形式とする
   - 文字コードはBOM無しUTF-8、改行コードはCR+LFとする
   - アイテムタイプ毎にファイルを分けて出力する
   - ファイル名は「アイテム_(タイプ名).tsv」とする
   - 1行で1アイテムを記載する

- 詳細仕様

   - ヘッダ行

       - 先頭の5行はヘッダ行とする
       - ヘッダ行は、"#"で開始する

   - ヘッダ各行の詳細

       - 1行目 ： アイテムタイプの名称を記載する

           - 1カラム目 ： #ItemType (固定)
           - 2カラム目 ： アイテムタイプの名称を記載する
           - 3カラム目 ： アイテムタイプのjsonschemaのURLを記載する

       - 2行目 ： 各メタデータ項目の内部キーを記載する

           - 内部キーは、JSONPathのルールに従い記載する

       - 3行目 ： 各メタデータ項目のラベルを記載する

           - メタデータの階層に応じて、各階層のラベルを"."で連結する
           - 繰り返し可能な項目については、ラベルのサフィックスとして"[n]"(n:連番(0〜))を記載する  
             (例) 作成者[0].作成者識別子[0].作成者識別子

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
         WEKOの著者名DBに登録されている場合は、作成者の2階層目のデータとして、weko_idを追加する【確認中】

       - ファイル  
         file_path[n]は、ファイルプロパティのnと連番を合わせて対応する

   - メタデータファイル(tsv)サンプル  
     別紙「weko3\_tsvformat.xlsx」を参照

### ダウンロードするアイテム情報 BIBTEX形式

別紙「WEKOメタデータ取得API（JPCOAR_BiBTEX）_20200106NII案」を仕様書として参照すること

- 「Item to Export」エリアの「Export Format」項目でBIBTEXを選び、エクスポートボタンを押す。  
  この操作によって、weko_items_ui.utils.export_itemsメソッドにてwrite_bibtex_filesメソッドが呼び出され、bibファイルが出力される。

- ファイル名のルール：[アイテムタイプ名(アイテムタイプバージョン)].bib

- 仕様書での「文献種別別出力フィールド」シート

   - 「○ ※必須」：必須項目  
     　一括出力の時に、必須チェックを行う。  
     weko_items_ui.utils.make_bibtex_dataメソッドにおいてチェックを行っている。
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

### ダウンロードするメタデータファイル RO-Crate形式

RO-Crateの形式については[ADMIN_2.5 RO-Crateインポート](../admin/ADMIN_2_5.md)を参照すること。

- 「Item to Export」エリアの「Export Format」項目でRO-Crateを選び、エクスポートボタンを押す。  
  この操作によって、weko_items_ui.utils.export_itemsメソッドにてwrite_rocrateメソッドが呼び出され、RO-Crateファイルが出力される。
- tsvの形式の場合と同様にweko_items_ui.utils.make_stats_fileから出力可能なメタデータを取得し、
  weko_search_ui.mapper.JsonLdMapper.to_rocrate_metadataメソッドでRO-Crateのメタデータを作成する。  
- RO-CrateのメタデータはJsonldMappingより取得したマッピング定義をもとに、アイテムタイプから変換される。
- 作成したRO-Crateのメタデータはro-crate-metadata.jsonとして出力される。
- 出力するアイテムが複数ある場合は、recidごとにzipファイルを作成する。  
  zipファイル名は「recod_[recidの値].zip」とする。


### その他

- エクスポートの最大アイテム数は以下で設定する  
  /modules/weko-items-ui/weko\_items\_ui/config.py  
 　WEKO\_ITEMS\_UI\_DEFAULT\_MAX\_EXPORT\_NUM = 100

- エクスポート処理実行時、weko\_items\_ui.utils.export\_itemsメソッドにてtempfile.TemporaryDirectoryによってtmpファイルが生成される。  
 テンポラリディレクトリのファイル名を以下のように設定する。  
 なお、tmpファイルはエクスポート処理実行後に自動的に削除される。

   - /home/invenio/.virtualenvs/invenio/var/instance/data/tmp/weko\_export\_xxxxxxxx

- weko\_items\_ui.utils.export\_items  
 <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/utils.py#L1423-L1507>


## 更新履歴


| 日付       | GitHubコミットID                           | 更新内容                                        |
| ---------- | ------------------------------------------ | ----------------------------------------------- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562   | 初版作成                                        |
| 2023/11/11 |                                            | V0.9.27                                         |
| 2025/06/27 |                                            | RO-Crate形式のエクスポートを追加                |
