### 雑誌情報

  - > 目的・用途

本機能は、インデックスの雑誌情報を管理（追加・編集・削除）、エクスポート時の出力を設定する機能である

  - > 利用方法

1\. システム管理者、リポジトリ管理者でログインする。

2\. 【Administration \> インデックスツリー管理(Index Tree) \> ツリー編集(Edit Tree)】で編集するインデックスツリーを選ぶ。

  - > 利用可能なロール


|ロール|システム<br>管理者|リポジトリ<br>管理者|サブリポジトリ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|利用可否|○|○|○| | | |

  - > 機能内容

1 インデックスの雑誌情報を追加する

  - 【Administration \> 設定(Setting) \> 雑誌情報(Index Journal)画面】でのインデックスツリーにインデックスを選択した状態でインデックスの雑誌情報が設定できる。
      - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに設定したインデックスをルートとしたインデックスツリーを表示する。

      - 「Root Index」を選択している場合、右の「ジャーナル」エリアが非活性となる。
    
      - エクスポート時の出力の設定エリアを設ける
        
          - 「ジャーナル(Journal)」エリアに、「Output」/「Do not output」ラジオボタンで設定できる。初期値は「Do not output」である
            
              - 「Output」を選択した場合、設定されたインデックスの雑誌情報を表示する。
            
              - 「Do not output」を選択した場合、すでに登録済みの情報があればデータはそのまま保持して画面表示を非表示とする。
    
      - 雑誌情報の項目は以下の通りである

| \# | 項目(英語)                                  | 項目(日本語)                | KBART項目名                          | 入力必須 | 入力インターフェース |
| -- | --------------------------------------- | ---------------------- | --------------------------------- | ---- | ---------- |
| 1  | Title                                   | タイトル                   | publication\_title                | ※    |            |
| 2  | Abstract                                | 概要                   |                                    |           |            |
| 3  | ISSN-L                                  | ISSN-L                 |                                   |      |            |
| 4  | Print-format identifier                 | プリント版ISSN/プリント版ISBN    | print\_identifier                 |      |            |
| 5  | Online-format identifier                | eISSN/eISBN            | online\_identifier                |      |            |
| 6  | Date of first issue available online    | 最古オンライン巻号の出版年月日        | date\_first\_issue\_online        | ※    | カレンダー入力    |
| 7  | Number of first volume available online | 提供最古巻                  | num\_first\_vol\_online           |      |            |
| 8  | Number of first issue available online  | 提供最古号                  | num\_first\_issue\_online         |      |            |
| 9  | Date of last issue available online     | 最新オンライン巻号の出版年月日        | date\_last\_issue\_online         |      | カレンダー入力    |
| 10 | Number of last volume available online  | 提供最新巻                  | num\_last\_vol\_online            |      |            |
| 11 | Number of last issue available online   | 提供最新号                  | num\_last\_issue\_online          |      |            |
| 12 | Embargo information                     | エンバーゴ情報                | embargo\_info                     |      |            |
| 13 | Coverage depth                          | カバー範囲                  | coverage\_depth                   | ※    | プルダウン入力    |
| 14 | Coverage notes                          | カバー範囲に関する注記            | coverage\_notes                   |      |            |
| 15 | Publisher name                          | 出版者                    | publisher\_name                   |      |            |
| 16 | Publication type                        | 資料種別                   | publication\_type                 | ※    | プルダウン入力    |
| 17 | Parent publication identifier           | シリーズのタイトルID            | parent\_publication\_title\_id    |      |            |
| 18 | Preceding publication identifier        | 変遷前誌のタイトルID            | preceding\_publication\_title\_id |      |            |
| 19 | Access type                             | アクセスモデル                | access\_type                      | ※    | プルダウン入力    |
| 10 | Language                                | 言語                     | language                          | ※    | プルダウン入力    |
| 21 | Title alternative                       | その他のタイトル（他の言語でのタイトルなど） | title\_alternative                |      |            |
| 22 | Title transcription                     | タイトルヨミ                 | title\_transcription              |      |            |
| 23 | NCID                                    | NCID                   | ncid                              |      |            |
| 24 | NDL Call No.                            | NDL請求記号                | ndl\_callno                       |      |            |
| 25 | NDL Bibliographic ID                    | NDL書誌ID                | ndl\_bibid                        |      |            |
| 26 | J-STAGE CDJOURNAL                       | J-STAGE資料コード（雑誌名の略称）   | jstage\_code                      |      |            |
| 27 | Ichushi Code                            | 医中誌ジャーナルコード            | ichushi\_code                     |      |            |

  - 入力項目の入力仕様は、  
    バリデーション仕様は、別紙「WEKO\_KBART出力項目一覧\_v1.17.xlsx」の\[ 型/入力制限 \]\[ データ長 \]\[ 備考 \]欄の記載に従う。

  - 入力項目にはバリデーション機能を用意する。  
    バリデーション仕様は、WEKO\_KBART出力項目一覧\_v1.17.xlsx の\[ 型/入力制限 \]欄の記載に従う

  - 入力必須の項目は、入力項目名に ※ を表示する。

  - 入力項目の確定は、「保存」（Save）ボタンを押すことで行う。

  - 「保存」（Save）ボタン押下時に、バリデーションチェックを行い、  
    チェックエラーがあった場合は、エラーメッセージを該当項目の直下に赤文字で表示して登録処理を中断する。

  - 追加されたインデックスの雑誌情報の表示について、 [USER-2-1 一覧形式表示](#一覧形式表示)を参照してください

入力項目のエラーチェックについては以下を参照すること  
<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-indextree-journal/weko_indextree_journal/schemas/jsonschema.json>

  - > 関連モジュール

<!-- end list -->

  - > weko-indextree-journal

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 雑誌情報画面の表示
    
      - 【Administration\>インデックスツリー管理\>雑誌情報】画面を開き、インデックスを選択する。この操作によって、weko\_indextree\_journal.admin.indexメソッドが呼び出される。メソッド内でget\_journal\_by\_index\_idを呼び出し、journalテーブルより雑誌情報を取得した後、indexメソッドによって編集画面を表示する。

  - 雑誌情報を作成する
    
      - 雑誌情報画面にてインデックスに対して「ジャーナル」エリアのoutputを選び、雑誌情報を初めて保存する。この操作によって、weko\_indextree\_journal.rest.postメソッドにて同フォルダのapi.pyのcreateメソッドを呼び出し、設定した雑誌情報をjournalテーブルに保存する。

  - 雑誌情報を更新する
    
      - 雑誌情報画面にて開いたインデックスが既にjournalテーブルで雑誌情報を持っている場合に雑誌情報を保存する。この操作によって、weko\_indextree\_journal.rest.putメソッドにて同フォルダのapi.pyのupdateメソッドを呼び出し、編集した雑誌情報をjournalテーブルに保存する。

  - 雑誌情報を削除する
    
      - 該当する機能のソースコードはweko\_indextree\_journal.rest.deleteメソッドで存在する。しかし、雑誌情報管理画面上ではその機能を実行することはできない。  
        代わりにインデックスを削除したとき、そのインデックスの雑誌情報をjournalテーブルから削除することができる。

  - バリデーションチェックについて
    
      - 雑誌情報画面にてインデックスを開いた際に、weko\_indextree\_journal.admin.get\_json\_schemaが呼び出され、weko\_indextree\_journal.schemas.jsonschemaの情報をページ上に渡す。  
        その情報のパターンにあっているかでバリデーションチェックを行っている。

<!-- end list -->

  - > 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|> 2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|> 2025/01/23|-|サブリポジトリ対応|

