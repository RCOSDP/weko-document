# [詳細検索](https://redmine.devops.rcos.nii.ac.jp/projects/weko-dev-doc/wiki/%E8%A9%B3%E7%B4%B0%E6%A4%9C%E7%B4%A2)

## 目的・用途

本機能は、ユーザーがアイテムを検索する際に用いる機能である。  
タイトルや著者名等の項目を指定し、複数の項目を掛け合わせて検索を行うことで、目的のアイテムを見つけることができる。

## 利用方法

トップページ画面の[Top]タブにあるキーワード検索テキストボックスの右側にある[詳細検索（Advanced）]ボタンを押下する。  
詳細検索条件入力エリアが表示されるので、条件を入力し、詳細検索エリアの最下部にある[検索(Search)]ボタンを押下することで、検索結果が表示される。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

## 機能内容

- トップページ画面［トップ（Top）］タブの上部に設けたアイテム検索エリア内に、詳細検索条件を入力できるボタン（[詳細検索(Advanced)]ボタン）を設ける。
- [検索（Sesrch）]ボタンの右にある[詳細検索(Advanced)]ボタンを押下すると、詳細検索エリアを展開表示する。
  - 詳細検索エリアを展開表示すると、本ボタンは［閉じる（Close）］ボタンに置換される。［閉じる（Close）］ボタンを押下することで、詳細検索エリアを非表示とする。詳細検索エリアを非表示にすると、本ボタンは[詳細検索(Advanced)]ボタンに置換される。
- 簡易検索のテキストフィールドと詳細検索の各項目とのAND検索を行うことが可能とする。
  - 詳細検索では、検索方式ラジオボタン（［全文（Full text）］と［キーワード（Keyword）］）は簡易検索と同じものを使用する。  
    各検索方式は簡単検索と同じ仕様とする。
- テキストボックスに入力して検索を行う場合、文字間に空白を入れることでAND検索を行うことができる。
- テキストボックスに入力して検索を行う場合、文字列を「△OR△」または「△|△」 (△は半角または全角スペース)で区切ることでOR検索を行うことができる。
  - 「OR」、「|」で区切ることによるOR検索よりも、スペースで区切ることによるAND検索の方を優先して処理する。
- 以下の特殊な意味をもつ英字のみでは検索を行うことができない。  
  a, an, and, are, as, at, be, but, by, for, if, in, into, is, it, no, not, of, on, or, such, that, the, their, then, there, these, they, this, to, was, will, with
- 以下の特殊文字は検索時に指定できる。  
  入力された特別文字は内部的にエスケープする。  
  + - = && || ! ( ) { } [ ] ^ " ~ * ? : \ /  
  エスケープできない文字(「<」「>」)で検索を行った場合は、「’<’,’>’は検索に使用できません。」とエラーメッセージを表示する。
- 日付入力において、妥当ではない日付が入力された場合は「Field does not validate」とエラーメッセージを表示する。

検索項目は【Administration > 設定（Setting） > 検索設定（Search）画面】の詳細検索条件設定エリアの通りに表示される。設定については[ADMIN-14-11: 検索設定](#検索設定)を参照。

- 詳細検索条件設定エリアの［初期選択（Initial Condition）］カラムにチェックが入っている項目は、初期状態で詳細検索エリアに表示される。
- 各詳細検索条件の項目は、詳細検索条件設定エリアで表示されている順番で表示される。
- ［使用項目（Useable Item）］カラムにチェックが入っている項目は初期状態では表示せず、検索条件項目のプルダウンで選択できるものとする。
- ［アイテムタイプ（Item Type）］の検索条件項目については、現在システムに登録されているアイテムタイプを取得し、表示する。
- 既に選択されている検索条件項目は、検索条件項目プルダウンで非活性（選択できない状態）とする。

各検索条件について、入力方式に応じて以下のいずれかの適当な入力エリアを設ける。

- テキストボックス
- チェックボックス
- プルダウン
- 範囲入力（[テキスト] To[テキスト]）
- 日付範囲入力（範囲入力＋カレンダー入力）
- geo_distance

表 1-2‑1　初期登録を行った環境で詳細検索エリアに初期表示される項目

| **No.** | **検索項目** | **入力エリア** |
| --- | --- | --- |
| 1 | タイトル (Title) | テキストボックス |
| 2 | 著者名 (Author Name) | テキストボックス |
| 3 | 件名 (Subject) | テキストボックス、チェックボックス |
| 4 | 地域 (Region) | テキストボックス |
| 5 | 内容記述 (Description) | テキストボックス |
| 6 | 出版者 (Publisher) | テキストボックス |
| 7 | 寄与者 (Contributor) | テキストボックス |
| 8 | コンテンツ作成日 (Contents Created Date) | 日付範囲入力、チェックボックス |
| 9 | フォーマット (Format) | テキストボックス |
| 10 | ID | テキストボックス、チェックボックス |
| 11 | 雑誌名 (Journal Title) | テキストボックス |
| 12 | 資源タイプ (Resource Type) | チェックボックス |
| 13 | アイテムタイプ (Item Type) | チェックボックス |
| 14 | 言語 (Language) | チェックボックス |
| 15 | 期間 (Period) | テキストボックス |
| 16 | 学位取得日 (Academic Degree Date) | テキストボックス |
| 17 | 著者版フラグ (Author Version Flag) | プルダウン |
| 18 | 学位番号 (Academic Degree Number) | テキストボックス |
| 19 | 学位名 (Degree Name) | テキストボックス |
| 20 | 学位授与機関 (Institution For Academic Degree) | テキストボックス |
| 21 | 著者ID (Author ID) | テキストボックス |
| 22 | Index | チェックボックス |
| 23 | License | チェックボックス |
| 24 | テキスト1 (text1) | テキストボックス |
| 25 | float_JA_1 | 数値範囲入力 |
| 26 | geopoint_JA_1 | geo_distance |
| 27 | アクセス権 (Access Rights) | チェックボックス |

検索項目ごとにある「X」ボタンを押すことで、検索条件を削除できる。

検索条件の表示の下に［検索条件追加（Add Search Condition）］ボタンを設ける。

- ［検索条件追加（Add Search Condition）］ボタンを押下すると、検索条件エリアを追加する。
- 選択されていない項目をデフォルト値とする。
- 入力欄が検索可能な項目の件数と同数になった場合、このボタンは非活性とする。

［クリア（Clear）］ボタンを押下すると、入力された検索条件を取消する。

日付を入力する検索項目について、テキストボックスを押下するとカレンダーのボタンが表示され、日付を選択することで、検索条件を入力できるものとする。

- 入力テキストフィールドでの入力とGUIでの入力の両方を可能とする。
- GUIを使用した場合は「YYYYMMDD」を指定できる。
- テキストフィールドから入力した場合は「YYYYMMDD」「YYYYMM」「YYYY」を指定できる。
- 上記以外の入力値を指定した場合は「Field does not validate」を表示し、アイテム検索はできない。

［検索（Search）］ボタンを押すことで、検索条件でアイテムの検索を実施し、検索結果がトップページ画面の検索結果エリアに表示される。

- JPCOARスキーマのマッピングでアイテム検索する。
- 検索方式：AND
- テキストボックス内にカーソルキーがある状態でエンターキーを押下することでも検索できる。
- 検索結果は【Administration > 設定（Setting） > 検索設定（Search）画面】での設定の通りに表示される。詳細については、[USER-2-1一覧形式表示](#一覧形式表示)を参照。
- 検索結果エリア
  - ［エクスポート（Export）］ボタンを表示する。  
    ボタンを押下すると、一括出力画面に遷移して、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](#アイテム一括出力)を参照。
  - アイテム表示の設定エリア  
    デフォルト値について、設定されている【Administration > 設定（Setting） > 検索設定（Search）画面】の検索結果表示設定エリアから取得する。
    - ［表示順］（Display Order）プルダウンリスト：検索結果の表示順を選択する。  
      選択肢は【Administration > 設定（Setting） > 検索設定（Search）画面】での「表示する」リストとする。
    - 順序プルダウン：昇順、降順を選択する。  
      選択肢は「asc, desc」とする。
    - ［表示数］（Display Number）プルダウンリスト  
      選択肢は「20,50,75,100」とする。
  - アイテム一覧表示
    - アイテムタイトルがリンク形式で表示される。  
      リンクをクリックすると、該当アイテム詳細画面に遷移する。
    - 表示されるアイテムはロールによって異なる。  
      システム管理者、リポジトリ管理者、コミュニティ管理者の場合はすべて表示される。  
      ただし、制限公開されているアイテムについては、公開日までシステム管理者と登録者のみ閲覧可能となる。  
      登録ユーザー、一般ユーザー、ゲストの場合はpublicなインデックスツリー内のpublicなアイテムのみ表示される。  
      ただし、登録ユーザーに関しては自身で登録したアイテムのみPrivateであっても検索対象となる。
  - ページング機能を設ける。
    - ページングナビゲーションを操作することで、表示内容が切り替わる。

## 関連モジュール

- weko_search_ui：検索結果をUIに表示する
- weko_schema_ui
- weko_items_ui
- weko_theme

## 処理概要

「メインコンテンツ」ウィジェットの［トップ（Top）］タブ上部にアイテム検索エリアを表示する。

- アイテム検索エリアには検索文字列を入力するテキストボックス、［検索（Search）］ボタン、［詳細検索（Advanced）］ボタン、全文(Full Text)/キーワード(Keyword)の検索方式を切り替えるラジオボタンを表示する。

［詳細検索(Advanced)］ボタンを押下すると、詳細検索エリアを展開表示する。

- 詳細検索エリアで初期表示される検索項目は【Administration > 設定（Setting） > 検索設定（Search）画面】の詳細検索条件設定エリアで［初期選択（Initial Condition）］カラムにチェックが入っている項目である。
- 詳細検索エリアが表示されている状態の時、［詳細検索(Advanced)］ボタンは［閉じる(Close)］ボタンに置換される。［閉じる(Close)］ボタンを押下することで、詳細検索エリアを非表示とする。詳細検索エリアを非表示にすると、再度［詳細検索(Advanced)］ボタンに置換される。

既に選択されている検索条件項目は、プルダウンで非活性（選択できない状態）とする。

検索項目ごとにある「X」ボタンを押すことで、検索条件を削除できる。

検索条件の表示の下にある［検索条件追加（Add Search Condition）］ボタンを押下すると、選択されていない項目の検索条件エリアを追加する。

- 選択されていない検索項目がない場合、このボタンは非活性とする。

詳細検索条件を指定して、入力エリア右隣の［検索(Search)］ボタンを押下することで、weko_search_ui.views.searchメソッドが呼び出され、検索の処理を実行する。検索文字列を入力しない場合、登録データの全件を対象とした検索を行う。

- ［検索］ボタンを押下せず、テキストボックス内にカーソルキーがある状態でエンターキーを押下することでも検索処理を実行する。
- 検索項目の選択肢は、weko_search_ui.config.py WEKO_SEARCH_KEYWORDS_DICTで設定している。
- 検索項目と対応するキーを表 1-2‑2に示す。
  - weko_schema_ui.mappings.v6.weko.item-v1.0.0.jsonにてElasticsearchでの文字解析方法を設定している。
  - FullText: 全文検索

表 1-2‑2　検索項目と対応するキー

| **No.** | **検索項目** | **検索方式** | **検索用のキー** | **備考** |
| --- | --- | --- | --- | --- |
| 1 | タイトル (Title) | FullText | search_title, search_title.ja | |
| 2 | 著者名 (Author Name) | FullText | search_creator, search_creator.ja | |
| 3 | 件名 (Subject) | Keyword | subject.subjectScheme | |
| 4 | 地域 (Region) | Keyword | geoLocation.geoLocationPlace | |
| 5 | 内容記述 (Description) | FullText | search_des, search_des.ja | |
| 6 | 出版者 (Publisher) | FullText | search_publisher. search_publisher.ja | |
| 7 | 寄与者 (Contributor) | FullText | search_contributor, search_contributor.ja | |
| 8 | コンテンツ作成日 (Contents Created Date) | Keyword | date.dateType, file.date.dateType | date.dateTypeが'file.date.dateType'キーで検索される |
| 9 | フォーマット (Format) | Keyword | file.mimeType | |
| 10 | ID | FullText | | ※表 1-2‑3参照 追加検索用のキーはKeyword方式 |
| 11 | 雑誌名 (Journal Title) | FullText | sourceTitle, sourceTitle.ja | |
| 12 | 資源タイプ (ResourceType) | | type.raw | |
| 13 | アイテムタイプ (ItemType) | FullText | itemtype | |
| 14 | 言語 (Language) | Keyword | language | |
| 15 | 期間 (Period) | Keyword | temporal | |
| 16 | 学位取得日 (Academic Degree Date) | | dateGranted | |
| 17 | 著者版フラグ (Author Version Flag) | FullText | versionType | |
| 18 | 学位番号 (Academic Degree Number) | FullText | dissertationNumber | |
| 19 | 学位名 (Degree Name) | FullText | degreeName, degreeName.ja | |
| 20 | 学位授与機関 (Institution For Academic Degree) | FullText | degreeGrantor. degreeGrantorName, dgName, dgName.ja | degreeGrantorNameが' dgName, dgName.ja 'キーで検索される degreeGrantorNameはキーワード方式 |
| 21 | 著者ID (Author ID) | Keyword | creator.nameIdentifier | |
| 22 | Index | FullText | path.tree | 入力したIndex IDに所属するアイテムを検索 ※入力したIndex ID下にある子インデックスに所属するアイテムの検索まではしない |
| 23 | License | | content.licensetype.raw | ファイル情報プロパティのライセンス情報を検索 ※権利情報プロパティ(dc:rights)の検索は実施しない |
| 24 | テキスト1 (text1) | Keyword | Text1 | |
| 24 | float_JA_1 | float_range | float_range1 | |
| 25 | geopoint_JA_1 | geo_point | geo_point1 | |

表 1-2‑3　 IDの選択肢と対応するキー

| **No.** | **選択肢** | **検索用のキー** | **追加検索用のキー** |
| --- | --- | --- | --- |
| 1 | identifier | relation.relatedIdentifier | identifierType=* |
| 2 | URI | identifier | identifierType=* |
| 3 | fullTextURL | file.URI | objectType=* |
| 4 | selfDOI | identifierRegistration | identifierType=* |
| 5 | ISBN | relation.relatedIdentifier | identifierType=ISBN |
| 6 | ISSN | sourceIdentifier | identifierType=ISSN |
| 7 | NCID | relation.relatedIdentifier | identifierType=NCID |
| 8 | NCID | sourceIdentifier | identifierType=NCID |
| 9 | pmid | relation.relatedIdentifier | identifierType=PMID |
| 10 | doi | relation.relatedIdentifier | identifierType=DOI |
| 11 | NAID | relation.relatedIdentifier | identifierType=NAID |
| 12 | ichushi | relation.relatedIdentifier | identifierType=ICHUSHI |

表 1-2-3の追加検索用のキーが「*」の場合、キーに対応する値が存在すればよいものとして検索する。

検索項目がタイトル、著者名、内容記述、出版者、寄与者、ID、雑誌名、学位名、学位授与機関、テキストX (Xは1~10の整数) のいずれかで、検索文字列に「△OR△」または「△|△」(△は半角または全角スペース)が含まれる場合

- 「△OR△」、「△|△」を区切りとして検索文字列を分割する。分割後の各文字列にそれぞれ対応するshould条件を作成する。それらの条件を`minimum_shoud_match=1`として検索することにより、OR検索を行う。

検索処理後、「メインコンテンツ」ウィジェットの［トップ（Top）］タブに検索結果エリアを表示する。

- ［検索結果］エリアにはエクスポートボタン、アイテムの表示順、表示数の現在の設定、検索結果のアイテム一覧、ページングナビゲーションを表示する。
- 最初に検索した際は、アイテム表示に関する設定のデフォルト値として、【Administration > 設定（Setting） > 検索設定（Search）画面】での検索結果表示設定エリアで設定された値を取得し、取得した値に従って表示する。

［エクスポート（Export）］ボタンを押下すると一括出力画面に遷移し、アイテムの情報をエクスポートできる。アイテムの一括出力については[USER-2-4: アイテム一括出力](#アイテム一括出力)を参照。

アイテムタイトルのリンクをクリックすると、該当アイテムの詳細画面に遷移する。

アイテムの表示順、表示数のプルダウンを選択すると、検索結果エリアでのアイテムの表示を選択した表示順、表示数に変更する処理を行う。

| **No.** | **検索項目** | **検索方式** | **検索用のキー** | **備考** |
| --- | --- | --- | --- | --- |
| 1 | タイトル (Title) | FullText | search_title, search_title.ja | |
| 2 | 著者名 (Author Name) | FullText | search_creator, search_creator.ja | |
| 3 | 件名 (Subject) | Keyword | subject.subjectScheme | |
| 4 | 地域 (Region) | Keyword | geoLocation.geoLocationPlace | |
| 5 | 内容記述 (Description) | FullText | search_des, search_des.ja | |
| 6 | 出版者 (Publisher) | FullText | search_publisher, search_publisher.ja | |
| 7 | 寄与者 (Contributor) | FullText | search_contributor, search_contributor.ja | |
| 8 | コンテンツ作成日 (Contents Created Date) | Keyword | date.dateType, file.date.dateType | date.dateTypeが'file.date.dateType'キーで検索される |
| 9 | フォーマット (Format) | Keyword | file.mimeType | |
| 10 | ID | FullText | | ※表 1-2‑3参照。追加検索用のキーはKeyword方式 |
| 11 | 雑誌名 (Journal Title) | FullText | sourceTitle, sourceTitle.ja | |
| 12 | 資源タイプ (ResourceType) | | type.raw | |
| 13 | アイテムタイプ (ItemType) | FullText | itemtype | |
| 14 | 言語 (Language) | Keyword | language | |
| 15 | 期間 (Period) | Keyword | temporal | |
| 16 | 学位取得日 (Academic Degree Date) | | dateGranted | |
| 17 | 著者版フラグ (Author Version Flag) | FullText | versionType | |
| 18 | 学位番号 (Academic Degree Number) | FullText | dissertationNumber | |
| 19 | 学位名 (Degree Name) | FullText | degreeName, degreeName.ja | |
| 20 | 学位授与機関 (Institution For Academic Degree) | FullText | degreeGrantor.degreeGrantorName, dgName, dgName.ja | degreeGrantorNameが'dgName, dgName.ja'キーで検索される。degreeGrantorNameはキーワード方式 |
| 21 | 著者ID (Author ID) | Keyword | creator.nameIdentifier | |
| 22 | Index | FullText | path.tree | 入力したIndex IDに所属するアイテムを検索。※入力したIndex ID下にある子インデックスに所属するアイテムの検索まではしない |
| 23 | License | | content.licensetype.raw | ファイル情報プロパティのライセンス情報を検索。※権利情報プロパティ(dc:rights)の検索は実施しない |
| 24 | テキスト1 (text1) | Keyword | Text1 | |
| 25 | float_JA_1 | float_range | float_range1 | |
| 26 | geopoint_JA_1 | geo_point | geo_point1 | |
| 27 | アクセス権 (Access Right) | Keyword | Access Right | |

## 実装補足（v2.0.2 実装との突き合わせ）

- 詳細検索は `weko_search_ui.query.default_search_factory._get_detail_keywords_query`。検索キーと内部フィールドの対応は config `WEKO_SEARCH_KEYWORDS_DICT`。`exact_title_match`（タイトル完全一致）の分岐あり。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2022/04/28 | 57247ecce9b5e0879a2538687e446e0ea310129c | 初版作成 |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | v0.9.22対応 |
