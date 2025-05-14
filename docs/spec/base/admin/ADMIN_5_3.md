
### 一括登録

  - > 目的・用途

本機能は、著者DBの情報を一括登録する機能である。

  - > 利用方法

管理者は本画面でインポート用のtsvファイルを取り込むことで、tsvファイル内の著者情報を一括で著者DBに登録することができる。

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

(1) 一括登録画面の画面構成

  - 【Admin \> 著者DB管理(Author Management) \> 一括登録(Import)】 を選択すると表示される

  - 画面構成は以下の通り。３つのタブに分かれており、動作を進めることでタブが切り替わる。

| \# | タブ名           | 機能概要                      |
| -- | ------------- | ------------------------- |
| 1  | 選択(Select)    | 著者DBのインポート用ファイル(tsv)を選択する |
| 2  | インポート(Import) | インポートファイル内の著者情報の確認・登録をする  |
| 3  | 結果(Result)    | インポート結果を表示する              |

　【補足】  
　　・タブの遷移の順番は「選択(Select)」→「インポート(Import)」→「結果(Result)」となる

「選択(Select)」タブ

  - 本タブは、ユーザが著者DBのインポート用ファイルを選択することができる。画面構成は以下の通り

  <table>
  <thead>
  <tr class="header">
  <th>#</th>
  <th>ボタン</th>
  <th>概要</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>1</td>
  <td>インポート対象(Import taret)</td>
  <td>プルダウンである。押下すると以下の三つの選択肢が出る。<br />
  著者DB・著者識別子・機関識別子</td>
  </tr>
  <tr class="odd">
  <td>2</td>
  <td>ファイル選択(Select File)</td>
  <td>ボタンを押下すると、ファイルのアップロードウィンドウを表示する。<br />
  ユーザは任意のインポート用ファイルを選択する。<br />
  なお、選択できる形式は「tsv」ファイルのみとする。</td>
  </tr>
  <tr class="even">
  <td>3</td>
  <td>次へ(Next)</td>
  <td>ボタンを押下すると、選択したファイルの形式(フォーマット)をチェックし、問題無ければ「インポート(Import)」タブへ自動遷移する。<br />
  エラーがある場合は、「選択(Select)」タブ上部に赤枠でエラーメッセージを表示し、「インポート(Import)」タブへ遷移はしない。<br />
  本ボタンの初期状態は非活性とする。<br />
  ユーザがファイルを選択後、インポート対象と選択されたファイルの形式が一致すれば活性化する。</td>
  </tr>
  <tr  class="even">
  <td>4</td>
  <td>強制変更モード</td>
  <td>強制変更モードをONにするチェックボックス<br/>
  強制変更モード時にインポートで著者DBのデータを更新するとその著者DBのデータを使っているメタデータが全て著者DBに沿って更新される。 <br/> 
  チェックボックスをONにした際にモーダルが表示され、同意チェックボックスにチェックを入れた上でＯＫボタンを押さなければONにならない。<br/> 
  具体的には以下<br/>
  ON時に更新される内容：氏名、著者識別子、E-Mail、所属機関識別子、所属機関名<br/>
  OFF時に更新される内容：著者識別子<br/>
  </td>
  </tr>
  </tbody>
  </table>

  - selectタブにてプルダウン：登録対象テーブル(Export target)を表示する。
      - プルダウンの選択肢としては以下のもの
          - 著者情報(Author)
          - 著者識別子(ID_Prefix)
          - 機関識別子(Affiliation_ID)
      - デフォルトでは「著者情報(Author)」が選択されている。
      - このプルダウンで選択されている情報がインポートの対象となる。

  - ファイル未選択の場合は[ファイル選択(Select File)]ボタン下に「選択したファイル名(Selected file name)」というラベルをグレーで表示する。  
  ファイル選択後、選択されたファイルのファイル名を表示する

  - インポートするtsv/csvファイルがブラウザに埋め込まれた際にtsvファイルの形式を読み取り、  
      プルダウンと一致しないなら「次へ」ボタンは活性化させない。
      - 判断したインポートの対象がExport targetと違う場合、
          アラートが表示され、以下のメッセージを表示する。また、「次へ」ボタンが活性化しない。
          - 日本語：選択された登録対象テーブルとインポートファイルの形式が違います。
          - 英語：The selected target table and the import file format are different.

      - 判断したインポートの対象がExport targetと一致する場合、
          「次へ」ボタンが活性化する。
  
  - 「次へ」ボタンを押下すると、「インポート(Import)」タブへ移動する。

「インポート(Import)」タブ

  - 本タブは、読み込んだインポート用ファイルの内容をチェックし、登録して良いかの確認を促すものである。画面構成は以下の通り

    <table>
    <thead>
    <tr class="header">
    <th>#</th>
    <th>ボタン</th>
    <th>概要</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>1</td>
    <td>インポート(Import)</td>
    <td>ボタンを押下すると、読み込んだ著者DBのインポート用ファイルの内容を登録する。ボタン押下後は、「インポート(Import)」タブへ自動遷移する。<br />
    読み込んだ著者DBのインポート用ファイルの内容にエラーがある場合は、本ボタンは非活性となる。</td>
    </tr>
    <tr class="even">
    <td>2</td>
    <td>ダウンロード(Download)</td>
    <td>ボタンを押下すると、画面に表示されている著者のリストをTSV形式でダウンロードできる。<br />
    ・文字コードはBOM無しUTF-8、改行コードはCR+LFとする。<br />
    BOM付きのファイルのダウンロードを行うと、先頭についているBOMを文字列として取り込むため、正しく情報のダウンロードが行われない場合がある。<br />
    ・ファイル名は「{target}_Check_yyyymmdd.tsv」とする。<br />
    ・画面上トリミングされている情報があっても、ファイルにはすべて出力される</td>
    </tr>
    </tbody>
    </table>

  - 画面に読み込んだインポート用ファイルの「サマリー(Summary)」を以下のように表示する

    | \# | 項目名            | 概要                      |
    | -- | -------------- | ----------------------- |
    | 1  | 総計(Total)      | 読み込んだファイルの著者の数          |
    | 2  | New Creator    | 読み込んだファイルの内、新規登録となる著者の数 |
    | 3  | Update Creator | 読み込んだファイルの内、更新の著者の数     |
    | 4  | Delete Creator | 読み込んだファイルの内、削除となる著者の数   |
    | 5  | Result Error   | 内容のチェックでエラーとなった著者の数     |

  - 画面に表示される著者DBの詳細情報は以下の通り

    <table>
    <thead>
    <tr class="header">
    <th>#</th>
    <th>項目名</th>
    <th>概要</th>
    </tr>
    </thead>
    <tbody>
    <tr >
    <td>1</td>
    <td>No.</td>
    <td>読み込んだファイルの著者の通し番号を表示する。</td>
    </tr>
    <tr >
    <td>2</td>
    <td>Current WEKO ID</td>
    <td>上書きする著者のインポート前のWEKO著者IDを表示する。</td>
    </tr>
    <tr >
    <td>3</td>
    <td>New WEKO ID</td>
    <td>tsvから読み込んだ著者のインポート後のWEKO著者IDを表示する。</td>
    </tr>
    <tr >
    <td>4</td>
    <td>Full_Name</td>
    <td>読み込んだ著者の姓と名を表示する。<br />
    姓と名の間はカンマ＋スペース「姓, 名」で表示する。</td>
    </tr>
    <tr >
    <td>5</td>
    <td>Mail Address</td>
    <td>読み込んだ著者のメールアドレスを表示する。</td>
    </tr>
    <tr >
    <td>6</td>
    <td>チェック結果(Check Result)</td>
    <td><p>読み込んだファイルの各著者について、インポートが可能かバリデーションチェックを実施する。<br />
    ・エラーが無く、新規の著者の場合：「登録(Register)」と表示する<br />
    ・エラーが無く、更新の著者の場合：「更新(Update)」と表示する<br />
    ・削除する著者の場合：「削除(Delete)」と表示する<br />
    ・バリデーションエラーがある場合：「エラー: XXXXX (ERROR: XXXXX)」とエラー内容を表示する</p>
    <p>・登録は可能であるが、何らかの問題があるときは「警告（Warning）」と表示する。</p></td>
    </tr>
    </tbody>
    </table>

  - 画面に表示される識別子の詳細情報は以下の通り

    <table>
    <thead>
    <tr class="header">
    <th>#</th>
    <th>項目名</th>
    <th>概要</th>
    </tr>
    </thead>
    <tbody>
    <tr >
    <td>1</td>
    <td>No.</td>
    <td>読み込んだファイルのデータの通し番号を表示する。</td>
    </tr>
    <tr >
    <td>2</td>
    <td>Scheme</td>
    <td>読み込んだデータのスキーマを表示する。</td>
    </tr>
    <tr >
    <td>3</td>
    <td>Scheme_Name</td>
    <td>読み込んだデータのスキーマ名を表示する。</td>
    </tr>
    <tr >
    <td>4</td>
    <td>url</td>
    <td>読み込んだデータのスキーマurlを表示する。
    </tr>
    <tr >
    <td>5</td>
    <td>チェック結果(Check Result)</td>
    <td><p>読み込んだファイルの各データについて、インポートが可能かバリデーションチェックを実施する。<br />
    ・エラーが無く、新規の識別子スキーマの場合：「登録(Register)」と表示する<br />
    ・エラーが無く、既存の識別子スキーマの場合：「更新(Update)」と表示する<br />
    ・削除する識別子の場合：「削除(Delete)」と表示する<br />
    ・バリデーションエラーがある場合：「エラー: XXXXX (ERROR: XXXXX)」とエラー内容を表示する</p>
    <p>・登録は可能であるが、何らかの問題があるときは「警告（Warning）」と表示する。</p></td>
    </tr>
    </tbody>
    </table>


  - 結果タブへ遷移する際は、\[インポート（Import）\]ボタンを押下することで自動的に遷移し、それ以外の方法で遷移することはできない。　
  - \[インポート（Import）\]ボタンは一度押下すると、ファイルを変更するまでは非活性となる。

「結果(Result)」タブ

  - 本タブは、インポートファイルで登録・更新・削除した著者の登録結果を表示する。画面構成は以下の通り　

<table>
<thead>
<tr class="header">
<th>#</th>
<th>ボタン</th>
<th>概要</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>サマリー(Summary)</td>
<td>
  ・ 著者DBの場合のみ表示される。<br />
  ・ 表示されるのは以下の4つ<br />
  　　・「総計」<br />
  　　・「成功」<br />
  　　・「失敗」<br />
  　　・「処理待ち」<br />
</td>
</tr>
<tr class="even">
<td>2</td>
<td>ダウンロード(Download)</td>
<td>ボタンを押下すると、画面に表示されている著者のリストをTSV形式でダウンロードできる。<br />
・文字コードはBOM無しUTF-8、改行コードはCR+LFとする<br />
・ファイル名は「{target}_List_Download_yyyymmdd.tsv」とする</td>
</tr>
</tbody>
</table>

  - 画面に表示される著者のインポート結果は以下の通り
    <table>
    <thead>
    <tr class="header">
    <th>#</th>
    <th>項目名</th>
    <th>概要</th>
    </tr>
    </thead>
    <tbody>
    <tr >
    <td>1</td>
    <td>No.</td>
    <td>読み込んだファイルの著者の通し番号を表示する。</td>
    </tr>
    <tr >
    <td>2</td>
    <td>開始日(Start Date)</td>
    <td>1著者に対して登録処理を開始した日時を表示する。<br />
    フォーマット：YYYY-MM-DD hh:mm:ss</td>
    </tr>
    <tr >
    <td>3</td>
    <td>終了日(End Date)</td>
    <td>１著者に対して登録処理が完了した日時を表示する。<br />
    フォーマット：YYYY-MM-DD hh:mm:ss</td>
    </tr>
    <tr >
    <td>4</td>
    <td>Previous WEKO ID</td>
    <td>上書きする著者のインポート前のWEKO著者IDを表示する。</td>
    </tr>
    <tr >
    <td>5</td>
    <td>New WEKO ID</td>
    <td>tsvから読み込んだ著者のインポート後のWEKO著者IDを表示する。</td>
    </tr>
    <tr >
    <td>6</td>
    <td>Full_name</td>
    <td>読み込んだ著者の姓と名を表示する。<br />
    姓と名の間はカンマ＋スペース「姓, 名」で表示する。</td>
    </tr>
    <tr >
    <td>7</td>
    <td>ステータス(Status)</td>
    <td>登録した結果を表示する。<br />
    ・「Register Success」：新規登録が完了した場合に表示<br />
    ・「Update Success」：変更・更新登録が完了した場合に表示<br />
    ・「Delete Success」：削除が完了した場合に表示<br />
    ・「ERROR: XXXXX」：エラーが発生した場合に表示</td>
    </tr>
    </tbody>
    </table>

  - 画面に表示される識別子インポート結果は以下の通り
    <table>
    <thead>
    <tr class="header">
    <th>#</th>
    <th>項目名</th>
    <th>概要</th>
    </tr>
    </thead>
    <tbody>
    <tr >
    <td>1</td>
    <td>No.</td>
    <td>読み込んだファイルのデータの通し番号を表示する。</td>
    </tr>
    <tr >
    <td>2</td>
    <td>開始日(Start Date)</td>
    <td>１データに対して登録処理を開始した日時を表示する。<br />
    フォーマット：YYYY-MM-DD hh:mm:ss</td>
    </tr>
    <tr >
    <td>3</td>
    <td>終了日(End Date)</td>
    <td>１データに対して登録処理が完了した日時を表示する。<br />
    フォーマット：YYYY-MM-DD hh:mm:ss</td>
    </tr>
    <tr >
    <td>4</td>
    <td>Scheme</td>
    <td>読み込んだデータのスキーマを表示する。</td>
    </tr>
    <tr >
    <td>5</td>
    <td>Scheme_Name</td>
    <td>読み込んだデータのスキーマ名を表示する。</td>
    </tr>
    <tr >
    <td>6</td>
    <td>ステータス(Status)</td>
    <td>登録した結果を表示する。<br />
    「Register Success」：新規登録が完了した場合に表示<br />
    「Update Success」：変更・更新登録が完了した場合に表示<br />
    「Delete Success」：削除が完了した場合に表示<br />
    「ERROR: XXXXX」：エラーが発生した場合に表示</td>
    </tr>
    </tbody>
    </table>


  - 登録処理は、バックグラウンドで実行し、１データ毎にコミットしながら処理を進める

  - 著者の登録情報は、著者のテーブルとElasticSearchに登録する
  - 識別子の登録情報は、以下の場合で登録先を分ける。
      - インポート時にtarget importプルダウンが「ID prefix」の場合は、  
          authors_prefix_settingsテーブルに登録する。
      - インポート時にtarget importプルダウンが「Affiliation ID」の場合は、  
        authors_affiliation_settingsテーブルに登録する。
  - 本タブを開いた状態で画面をリロードすることで、登録状況が更新されるものとする

  - 「選択(Select)」タブ，「インポート(Import)」タブへの遷移は可能とする。ただし、登録処理実行中は、各ボタンは非活性とする

(2-1) 著者情報の入力ファイル

  - 入力ファイルはtsv形式で出力される

  - 著者情報のtsvファイルの構成は以下の通り

      > ヘッダ行
          > 
          > ラベル(英語)
          > 
          > ラベル(日本語)
          > 
          > データ行（著者１）
          > 
          > データ行（著者２）
          > 
          > …

      - 文字コードはUTF-8(BOM無し)，改行コードはCR+LFとする

      - １行目はヘッダ行とし、システム管理するものである。先頭に"\#"が付いている

      - ２行目と３行目はラベルを表示し、TSV入力の補助をする。先頭に"\#"が付いている

      - ４行目以降に著者の情報を入力する。１行１著者となる

  - 著者情報の各ヘッダの情報は以下の通り

    <table>
      <thead>
      <tr class="header">
      <th >#</th> <th>ヘッダ項目</th> <th>ラベル(日本語)</th> <th>ラベル(英語)</th> <th>概要</th>
      </tr>
      </thead>
      <tbody>
      <tr  >
      <td>1</td>
      <td>pk_id</td>
      <td >著者ID</td>
      <td >Author ID</td>
      <td >このリポジトリ内でのpk_idを入力する</td>
      </tr>
      <tr >
      <td>2</td>
      <td>weko_id</td>
      <td>WEKO ID</td>
      <td>WEKO ID</td>
      <td>WEKO IDを入力する</td>
      </tr>
      <tr >
      <td>3</td>
      <td>authorNameInfo[0...n].familyName</td>
      <td>姓</td>
      <td>Family Name</td>
      <td>著者の姓を入力する</td>
      </tr>
      <tr >
      <td>4</td>
      <td>authorNameInfo[0...n].firstName</td>
      <td>名</td>
      <td>Given name</td>
      <td>著者の名を入力する</td>
      </tr>
      <tr >
      <td>5</td>
      <td>authorNameInfo[0...n].language</td>
      <td>言語</td>
      <td>Language</td>
      <td>著者の言語を入力する</td>
      </tr>
      <tr >
      <td>6</td>
      <td>authorNameInfo[0...n].nameFormat</td>
      <td>フォーマット</td>
      <td>name Format</td>
      <td>著者の姓名のフォーマットを入力する<br />
      ※現状(SP67時点)は「familyNmAndNm」固定</td>
      </tr>
      <tr >
      <td>7</td>
      <td>authorNameInfo[0...n].nameShowFlg</td>
      <td>姓名・言語 表示／非表示</td>
      <td>Name Display</td>
      <td>著者の姓名と言語の表示／非表示を入力する<br />
      表示する: "Y"<br />
      表示しない: "N"</td>
      </tr>
      <tr >
      <td>8</td>
      <td>authorIdInfo[0...n].idType</td>
      <td>外部著者ID 識別子</td>
      <td>Identifier Scheme</td>
      <td>外部著者IDの識別子を入力する</td>
      </tr>
      <tr >
      <td>9</td>
      <td>authorIdInfo[0...n].authorId</td>
      <td>外部著者ID URI</td>
      <td>Identifier URI</td>
      <td>外部著者IDの値を入力する</td>
      </tr>
      <tr >
      <td>10</td>
      <td>authorIdInfo[0...n].authorIdShowFlg</td>
      <td>外部著者ID 表示／非表示</td>
      <td>Identifier Display</td>
      <td>外部著者IDの表示／非表示を入力する<br />
      表示する: "Y"<br />
      表示しない: "N"</td>
      </tr>
      <tr >
      <td>11</td>
      <td>emailInfo[0...n].email</td>
      <td>メールアドレス</td>
      <td>Mail Address</td>
      <td>著者のメールアドレスを入力する</td>
      </tr>
      <tr >
      <td>12</td>
      <td>is_deleted</td>
      <td>削除フラグ</td>
      <td>Delete Flag</td>
      <td>著者を削除する場合に "D" と入力する</td>
      </tr>
      <tr  >
      <td>13</td>
      <td>authorAffiliationInfo[0...n].affiliationId[0...n].idtype</td>
      <td>外部所属機関ID 識別子</td>
      <td>Affiliation Identifier Scheme</td>
      <td>外部所属機関IDの識別子を入力する</td>
      </tr>
      <tr  >
      <td>14</td>
      <td>authorAffiliationInfo[0...n].affiliationId[0...n].uri</td>
      <td>外部所属機関ID URI</td>
      <td>Affiliation Identifier URI</td>
      <td>外部所属機関IDの値を入力する</td>
      </tr>
      <tr  >
      <td>15</td>
      <td>authorAffiliationInfo[0...n].authorIdShowFlg</td>
      <td>外部所属機関ID 表示／非表示</td>
      <td>Affiliation Identifier Display</td>
      <td>外部所属機関IDの表示／非表示を入力する<br />
      表示する: "Y"<br />
      表示しない: "N"</td>
      </tr>
      <tr  >
      <td>16</td>
      <td>authorAffiliationInfo[0...n].affiliationNameInfo[0...n].affiliationName</td>
      <td>外部所属機関名</td>
      <td>Affiliation Name</td>
      <td>外部所属機関名を入力する</td>
      </tr>
      <tr  >
      <td>17</td>
      <td>authorAffiliationInfo[0...n].affiliationNameInfo[0...n].language</td>
      <td>言語</td>
      <td>Language</td>
      <td>外部所属機関名の言語を入力する</td>
      </tr>
      <tr  >
      <td>18</td>
      <td>authorAffiliationInfo[0...n].affiliationNameInfo[0...n].nameShowFlg</td>
      <td>外部所属機関名・言語 表示／非表示</td>
      <td>Affiliation Name Display</td>
      <td>外部所属機関名と言語の表示／非表示を入力する<br />
      表示する: "Y"<br />
      表示しない: "N"</td>
      </tr>
      <tr  >
      <td>19</td>
      <td>authorAffiliationInfo[0...n].affiliationPeriodInfo[0...n].periodStart</td>
      <td>外部所属機関 所属期間</td>
      <td>Affiliation Period</td>
      <td>外部所属機関所属期間開始時期を入力する。<br/>
      形式：yyyy-MM-dd
      </tr>
      <tr  >
      <td>20</td>
      <td>authorAffiliationInfo[0...n].affiliationPeriodInfo[0...n].periodStart</td>
      <td>外部所属機関 所属期間</td>
      <td>Affiliation Period</td>
      <td>外部所属機関所属期間終了時期を入力する。<br/>
      形式：yyyy-MM-dd
      </tr>
      </tbody>
      </table>

　【補足】  
  - 繰り返し項目とする場合はヘッダ行の各項目名の後ろに [1], [2], ..., [N] と入力する。  
  ※1つ目の項目名には [0] が記載されている。  
  - Author ID, WEKO ID, Delete Flagは繰り返し記載することはできない。
  - 姓名のフォーマットの値が空欄の場合は「familyNmAndNm」の値を固定でシステムが登録する。
  - Author IDが空欄の場合、著者DBに新規登録する。  
      また、存在するIDの場合、該当のIDの著者データを更新する。  

(2-2) 識別子情報の入力ファイル

  - 入力ファイルはtsv形式で出力される

  - 著者識別子、機関識別子のtsvファイルの構成は以下の通り
    > テーブル情報
    > 
    > ヘッダ行
    > 
    > ラベル(英語)
    > 
    > ラベル(日本語)
    > 
    > データ行（識別子1）
    > 
    > データ行（識別子2）
    > 
    > …

    - 文字コードはUTF-8(BOM付き)，改行コードはCR+LFとする。
    - 1行目はテーブルを表す文字列とする。先頭に"#"が付いている。
        authors_prefix_settings、または、authors_affiliation_settingsが入る。
    - 2行目はヘッダ行とし、システム管理するものである。先頭に"#"が付いている。
    - 3行目と4行目はラベルを表示し、TSV入力の補助をする。先頭に"#"が付いている。
    - 5行目以降に情報を出力する。

- 著者識別子、機関識別子の各ヘッダの情報は以下の通り

    <table>
    <thead>
    <tr class="header">
    <th >#</th> <th>ヘッダ項目</th> <th>ラベル(日本語)</th> <th>ラベル(英語)</th> <th>概要</th>
    </tr>
    </thead>
    <tbody>
    <tr >
    <td>1</td>
    <td>scheme</td>
    <td>スキーマ</td>
    <td>Scheme</td>
    <td>スキーマを入力する</td>
    </tr>
    <tr >
    <td>2</td>
    <td>name</td>
    <td>名前</td>
    <td>Name</td>
    <td>スキーマに対応する識別子名を入力する</td>
    </tr>
    <tr >
    <td>3</td>
    <td>url</td>
    <td>URL</td>
    <td>URL</td>
    <td>スキーマに応じるURLを入力する</td>
    </tr>
    <tr >
    <td>4</td>
    <td>is_deleted</td>
    <td>削除フラグ</td>
    <td>Delete Flag</td>
    <td>識別子を削除する場合に "D" と出力する<br />
        エクスポートの場合は全て空欄である。</td>
    </tr>
    </tbody>
    </table>



(3) エラーチェック

  - 本画面で著者情報のチェックをしているエラー内容は以下の通り
    <table>
    <thead>
    <tr class="header"> <th>#</th> <th>チェックするタブ</th> <th>チェック内容</th> <th>処理</th> <th>エラーメッセージ(日)</th> <th>エラーメッセージ(英)</th> <th>備考</th>
    </tr>
    </thead>
    <tbody>
    <tr > <td>1</td>
    <td>選択(Select)</td>
    <td>tsvファイルの形式のチェック<br />
    #1: 選択したファイルがtsvファイルでは無い、またはtsvファイルの文字コードがUTF-8では無い<br />
    #3: tsvファイルの形式のエラー(タブ無し, ヘッダ行無し)</td>
    <td>ERROR</td>
    <td>TSVファイルを読み込めませんでした。ファイル形式がTSVであること、またそのファイルがUTF-8でエンコードされているかを確認してください。</td>
    <td>The TSV file could not be read. Make sure the file format is TSV and that the file is UTF-8 encoded.</td>
    <td></td>
    </tr>
    <tr >
    <td>2</td>
    <td>選択(Select)</td>
    <td>ヘッダ行だけの空レコードになっている</td>
    <td>ERROR</td>
    <td>インポートのデータがありません。</td>
    <td>There is no data to import.</td>
    <td></td>
    </tr>
    <tr >
    <td>3</td>
    <td>選択(Select)</td>
    <td>ヘッダの間違いからメタデータキーが重複している</td>
    <td>ERROR</td>
    <td>以下のメタデータキーが重複しています。<br />
    {1}</td>
    <td>The following metadata keys are duplicated.<br />
    {1}</td>
    <td>{1}: メタデータキー名</td>
    </tr>
    <tr >
    <td>4</td>
    <td>選択(Select)</td>
    <td>tsvに指定された項目とDBの項目が一致していない</td>
    <td>ERROR</td>
    <td>指定された項目とDBの項目が一致しません。<br />
    {1}</td>
    <td>Specified item does not consistency with DB item.<br />
    {1}</td>
    <td>{1}: 項目名</td>
    </tr>
    <tr >
    <td>5</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>Celeryが動いていない状態</td>
    <td>ERROR</td>
    <td>Celeryは動いていません。</td>
    <td>Celery is not running.</td>
    <td></td>
    </tr>
    <tr >
    <td>6</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>自分の端末にインポートを実行しているうちに、インポートを実行する</td>
    <td>ERROR</td>
    <td>インポートを実行中です。</td>
    <td>Import is in progress.</td>
    <td></td>
    </tr>
    <tr >
    <td>7</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>他の端末でインポートを実行している</td>
    <td>ERROR</td>
    <td>他の端末でインポートを実行中です。</td>
    <td>Import is in progress on another device.</td>
    <td></td>
    </tr>
    <tr >
    <td>8</td>
    <td>インポート(Import)</td>
    <td >WEKO_IDが入力されていない状態<br />
    または著者情報、機関情報で他の情報を入力されたが、idTypeとauthorIdのいずれかを入力されていない状態</td>
    <td>ERROR</td>
    <td>{}は必須項目です。</td>
    <td>{} is required item.</td>
    <td></td>
    </tr>
    <tr >
    <td>9</td>
    <td>インポート(Import)</td>
    <td >WEKO_IDが半角数字でない状態</td>
    <td>ERROR</td>
    <td>WEKO_IDは半角数字のみです。</td>
    <td>WEKO ID is Half-width digits only.</td>
    <td></td>
    </tr>
    <tr >
    <td>10</td>
    <td>インポート(Import)</td>
    <td >#4 著者が一意に定まらない(存在しないAuthor ID (author_link))<br />
    #5 削除対象の著者がDBに存在しない</td>
    <td>ERROR</td>
    <td >指定されたAuthor IDが存在していません。</td>
    <td >Specified Author ID does not exist.</td>
    <td></td>
    </tr>
    <tr >
    <td>11</td>
    <td>インポート(Import)</td>
    <td>WEKO IDが既に存在する。(既存のWEKO ID)</td>
    <td>ERROR</td>
    <td>指定されたWEKO IDが既に存在しています。</td>
    <td>Specified WEKO ID already exist.</td>
    <td></td>
    </tr>
    <tr >
    <td>12</td>
    <td>インポート(Import)</td>
    <td >#6 言語の指定でDBに存在しない言語を入力する<br />
    #8 ヘッダ項目#7の姓名・言語 表示／非表示で"Y","N"以外を入力する<br />
    #9 ヘッダ項目#10の外部著者識別子 表示／非表示で"Y","N"以外を入力する<br />
    ヘッダ項目#13の外部所属機関識別子 表示／非表示で"Y","N"以外を入力する<br />
    ヘッダ項目#16の外部所属機関名・言語 表示／非表示で"Y","N"以外を入力する
    </td>
    <td>ERROR</td>
    <td>{1}は{2}のいずれかを設定してください。</td>
    <td>{1} should be set by one of {2}.</td>
    <td>{1}: language, nameShowFlg, authorIdShowFlg<br />
    {2}: 言語の一覧、"Y","N"</td>
    </tr>
    <tr >
    <td>13</td>
    <td>インポート(Import)</td>
    <td >#10 ヘッダ項目#20の削除フラグで"D"以外を入力する<br />
    #13 姓名のフォーマットの値が「familyNmAndNm」以外の値</td>
    <td>ERROR</td>
    <td>{1}は{2}を設定してください。</td>
    <td>{1} should be set by one of {2}.</td>
    <td>{1}: is_deleted, nameFormat<br />
    {2}: "D"、"familyNmAndNm"</td>
    </tr>
    <tr >
    <td>14</td>
    <td>インポート(Import)</td>
    <td>ID PrefixでDBに存在しない識別子を入力する</td>
    <td>ERROR</td>
    <td>指定された外部著者ID 識別子'{1}'が存在していません。</td>
    <td>Specified Identifier Scheme '{1}' does not exist.</td>
    <td>{1}:外部著者ID 識別子</td>
    </tr>
    <tr  >
    <td>15</td>
    <td>インポート(Import)</td>
    <td>Affiliation IDでDBに存在しない識別子を入力する</td>
    <td>ERROR</td>
    <td>指定された外部所属機関ID 識別子'{1}'が存在していません。</td>
    <td>Specified Affiliation Identifier Scheme '{1}' does not exist.</td>
    <td>{1}:外部所属機関ID 識別子</td>
    </tr>
    <tr >
    <td>16</td>
    <td>インポート(Import)</td>
    <td>TSVファイルの中に重複するデータがある</td>
    <td>ERROR</td>
    <td>TSVファイルの中に重複するデータがあります。</td>
    <td>There is duplicated data in the TSV file.</td>
    <td>各レコードがマルチタスクで実行されているので、後勝ちで2番目のデータを上書きするのが難しい(重複する場合にどのレコードで更新されるか定まらない)。WARNING→ERRORに変更し、2つ目以降は更新されないようにする</td>
    </tr>
    <tr >
    <td>17</td>
    <td>インポート(Import)</td>
    <td>外部著者識別子がDBに存在している</td>
    <td>WARNING</td>
    <td>外部著者識別子がDBに存在しています。<br />
    {1}</td>
    <td>External author identifier exists in DB.<br />
    {1}</td>
    <td>{1}:外部著者識別子</td>
    </tr>
    <tr  >
    <td>18</td>
    <td>インポート(Import)</td>
    <td>外部所属機関所属期間が日付の形式になっていない</td>
    <td>ERROR</td>
    <td>外部所属機関所属期間が形式にあっていません。<br />
     yyyy-MM-dd、または空白であるようにしてください。<br />
     {1}</td>
    <td>Affiliation Period must be in the format:<br />
     yyyy-MM-dd, blank<br />
     {1}</td>
    <td>{1}:外部所属期間</td>
    </tr>
    <tr >
    <td>19</td>
    <td>インポート(Import)</td>
    <td>所属期間終了日が開始日より早い</td>
    <td>ERROR</td>
    <td>所属期間終了日は開始日より後の日付にしてください</td>
    <td>Period end must be after Period start.</td>
    <td></td>
    </tr>
    <tr >
    <td>20</td>
    <td>選択/インポート/結果<br />
    (Select/Import/Result)</td>
    <td>サーバ内部エラー（ネットワークの問題、予期しない例外など）が発生した</td>
    <td>ERROR</td>
    <td>サーバ内部エラー</td>
    <td>Internal server error</td>
    <td></td>
    </tr>
    <tr >
    <td>21</td>
    <td>結果(Result)</td>
    <td>登録成功</td>
    <td>INFO</td>
    <td>登録成功</td>
    <td>Register Success</td>
    <td></td>
    </tr>
    <tr >
    <td>22</td>
    <td>結果(Result)</td>
    <td>更新成功</td>
    <td>INFO</td>
    <td>更新成功</td>
    <td>Update Success</td>
    <td></td>
    </tr>
    <tr >
    <td>23</td>
    <td>結果(Result)</td>
    <td>削除成功</td>
    <td>INFO</td>
    <td>削除成功</td>
    <td>Delete Success</td>
    <td></td>
    </tr>
    <tr >
    <td>24</td>
    <td>結果(Result)</td>
    <td>エラーが発生したため、インポートに失敗した</td>
    <td>ERROR</td>
    <td>インポートに失敗しました。</td>
    <td>Failed to import.</td>
    <td></td>
    </tr>
    <tr >
    <td>25</td>
    <td>インポート(Import)</td>
    <td>削除済みの著者について、tsvに該当の著者情報を指定して更新した</td>
    <td>WARNING</td>
    <td>指定された著者は削除済です。tsvの内容で著者情報を更新しますが、著者は削除されたままです。</td>
    <td>The specified author has been deleted. Update author information with tsv content, but author remains deleted as it is.</td>
    <td></td>
    </tr>
    <tr >
    <td>26</td>
    <td>インポート/結果<br />
    (Import/Result)</td>
    <td>アイテムに紐づいている著者を削除した</td>
    <td>ERROR</td>
    <td>アイテムがリンクしているため、指定された著者は削除できません。</td>
    <td>The author is linked to items and cannot be deleted.</td>
    <td>英語のメッセージが既存<br />
    日本語のメッセージを新規追加</td>
    </tr>
    </tbody>
    </table>

  - 本画面で識別子のチェックをしているエラー内容は以下の通り
    <table>
    <thead>
    <tr class="header">
    <th>#</th>
    <th>チェックするタブ</th>
    <th>チェック内容</th>
    <th>処理</th>
    <th>エラーメッセージ(日)</th>
    <th>エラーメッセージ(英)</th>
    <th>備考</th>
    </tr>
    </thead>
    <tbody>
    <tr >
    <td>1</td>
    <td>選択(Select)</td>
    <td>tsvファイルの形式のチェック<br />
    #1: 選択したファイルがtsvファイルでは無い、またはtsvファイルの文字コードがUTF-8では無い<br />
    #3: tsvファイルの形式のエラー(タブ無し, ヘッダ行無し, テーブル名の指定がない)</td>
    <td>ERROR</td>
    <td>TSVファイルを読み込めませんでした。ファイル形式がTSVであること、またそのファイルがUTF-8でエンコードされているかを確認してください。</td>
    <td>The TSV file could not be read. Make sure the file format is TSV and that the file is UTF-8 encoded.</td>
    <td></td>
    </tr>
    <tr >
    <td>2</td>
    <td>選択(Select)</td>
    <td>ヘッダ行だけの空レコードになっている</td>
    <td>ERROR</td>
    <td>インポートのデータがありません。</td>
    <td>There is no data to import.</td>
    <td></td>
    </tr>
    <tr >
    <td>3</td>
    <td>選択(Select)</td>
    <td>ヘッダの間違いからキーが重複している</td>
    <td>ERROR</td>
    <td>キーが重複しています。</td>
    <td>The keys are duplicated.</td>
    <td></td>
    </tr>
    <tr >
    <td>4</td>
    <td>選択(Select)</td>
    <td>tsvに指定された項目とDBの項目が一致していない</td>
    <td>ERROR</td>
    <td>指定された項目とDBの項目が一致しません。<br />
    {1}</td>
    <td>Specified item does not consistency with DB item.<br />
    {1}</td>
    <td>{1}: 項目名</td>
    </tr>
    <tr >
    <td>5</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>Celeryが動いていない状態</td>
    <td>ERROR</td>
    <td>Celeryは動いていません。</td>
    <td>Celery is not running.</td>
    <td></td>
    </tr>
    <tr >
    <td>6</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>自分の端末にインポートを実行しているうちに、インポートを実行する</td>
    <td>ERROR</td>
    <td>インポートを実行中です。</td>
    <td>Import is in progress.</td>
    <td></td>
    </tr>
    <tr >
    <td>7</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>他の端末でインポートを実行している</td>
    <td>ERROR</td>
    <td>他の端末でインポートを実行中です。</td>
    <td>Import is in progress on another device.</td>
    <td></td>
    </tr>
    <tr >
    <td>8</td>
    <td>選択/インポート<br />
    (Select/Import)</td>
    <td>自分の端末でインポートを実行しているうちに、インポートを実行する</td>
    <td>ERROR</td>
    <td>インポートを実行中です。</td>
    <td>Import is in progress.</td>
    <td></td>
    </tr>
    <tr >
    <td>9</td>
    <td>インポート(Import)</td>
    <td>Schemeが記述されていない</td>
    <td>ERROR</td>
    <td>schemeを設定してください。</td>
    <td>Scheme is required item.</td>
    <td></td>
    </tr>
    <tr >
    <td>10</td>
    <td>インポート(Import)</td>
    <td>Nameが記述されていない</td>
    <td>ERROR</td>
    <td>nameを設定してください。</td>
    <td>Name is required item.</td>
    <td></td>
    </tr>
    <tr >
    <td>11</td>
    <td>インポート(Import)</td>
    <td>urlがURLの形式でない</td>
    <td>ERROR</td>
    <td>urlをURLの形式にしてください。</td>
    <td>URL is not URL format.</td>
    <td></td>
    </tr>
    <tr >
    <td>12</td>
    <td>インポート(Import)</td>
    <td>削除対象の識別子が存在しない</td>
    <td>ERROR</td>
    <td>指定された識別子が存在していません。</td>
    <td>The specified identifier does not exist.</td>
    <td></td>
    </tr>
    <tr >
    <td>13</td>
    <td>インポート(Import)</td>
    <td>TSVファイルの中に重複するデータがある</td>
    <td>ERROR</td>
    <td>TSVファイルの中に重複するデータがあります。</td>
    <td>The specified scheme is duplicated.</td>
    <td>各レコードがマルチタスクで実行されているので、後勝ちで2番目のデータを上書きするのが難しい(重複する場合にどのレコードで更新されるか定まらない)。WARNING→ERRORに変更し、2つ目以降は更新されないようにする</td>
    </tr>
    <tr >
    <td>14</td>
    <td>インポート(Import)</td>
    <td>schemaに「WEKO」が入力されている。</td>
    <td>ERROR</td>
    <td>著者識別子WEKOは編集できません。</td>
    <td>The scheme WEKO cannot be used.</td>
    <td></td>
    </tr>
    <tr >
    <td>15</td>
    <td>選択/インポート/結果<br />
    (Select/Import/Result)</td>
    <td>サーバ内部エラー（ネットワークの問題、予期しない例外など）が発生した</td>
    <td>ERROR</td>
    <td>サーバ内部エラー</td>
    <td>Internal server error</td>
    <td></td>
    </tr>
    <tr >
    <td>16</td>
    <td>結果(Result)</td>
    <td>登録成功</td>
    <td>INFO</td>
    <td>登録成功</td>
    <td>Register Success</td>
    <td></td>
    </tr>
    <tr >
    <td>17</td>
    <td>結果(Result)</td>
    <td>更新成功</td>
    <td>INFO</td>
    <td>更新成功</td>
    <td>Update Success</td>
    <td></td>
    </tr>
    <tr >
    <td>18</td>
    <td>結果(Result)</td>
    <td>削除成功</td>
    <td>INFO</td>
    <td>削除成功</td>
    <td>Delete Success</td>
    <td></td>
    </tr>
    <tr >
    <td>19</td>
    <td>結果(Result)</td>
    <td>エラーが発生したため、インポートに失敗した</td>
    <td>ERROR</td>
    <td>インポートに失敗しました。</td>
    <td>Failed to import.</td>
    <td></td>
    </tr>
    <tr >
    <td>20</td>
    <td>インポート/結果<br />
    (Import/Result)</td>
    <td>著者DBに紐づいている識別子を削除した</td>
    <td>ERROR</td>
    <td>著者DBで使用されているため、指定された識別子は削除できません。</td>
    <td>The specified scheme is used in the author ID.</td>
    <td></td>
    </tr>
    </table>
   

  - 処理の「エラー」は登録不可、「ワーニング」は登録可能とする。

(4) その他

  - バックグラウンドでインポート処理を実行する。

  - 著者情報は論理削除とする。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-authors

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - **インポート対象の判定**
      - TSV ファイルの **1行目** に記載された情報をもとに、インポート対象を判定する。

          | **1行目の内容** | **インポート対象** |
          |----------------------|----------------------|
          | 記載なし | 著者 (`authors` テーブル) |
          | `authors_prefix_settings` | 著者識別子 (`authors_prefix_settings` テーブル) |
          | `authors_affiliation_settings` | 機関識別子 (`authors_affiliation_settings` テーブル) |

      - フロントエンドで **「次へ」ボタン** を押せるのは、TSV の形式が Export target の値と一致した場合のみ。

  - **インポート前のチェック**  
      「次へ」を押した際、`check_import_file` メソッドを実行し、以下のチェックを行う。

      **(1) Import target の検証**
      - **TSV の 1行目** が `Import target`(Author, ID_Prefix, Affiliation_ID) に対応するものかを確認。
      - 一致しない場合、エラーメッセージを表示し、選択タブに戻す。

      **(2) Redis キーの確認**
      - `WEKO_AUTHORS_IMPORT_CACHE_KEY` が既に存在する場合、前回のインポート処理が完了していないと判断し、インポートを許可しない。

      **(3) Celery ワーカーの確認**
      - Celery ワーカー (`celery worker`) が稼働していない場合、インポートを許可しない。
      

      **(4) ファイルフォーマットの検証**  
      各 TSV ファイルの **各行のデータチェック** を行う。  
      以下では識別子の場合のチェック項目のみとする。

      | **チェック項目** | **エラー条件** |
      |----------------|----------------|
      | **TSV フォーマット** | 列の数が不足または過剰 |
      | **name 列** | 空欄の場合 |
      | **scheme 列** | 空欄の場合 |
      | **scheme の重複** | 同一ファイル内に重複がある場合 |
      | **URL の形式** | `http://` または `https://` で始まっていない場合 |
      | **削除対象の識別子** | DB内に対象が存在しない場合 |

      - schemeの値が対象となるDBに既存で存在する場合、更新とする。
      - schemeの値が対象となるDBに存在しない場合、新規登録となる。

  - **インポート処理**  
  チェックを通過し、インポートボタンを押下するとインポートタスクが非同期で実行される。
      1. `check_import_data` メソッドを実行し、Redisに定数WEKO_AUTHORS_IMPORT_CACHE_KEYの値に `import_type` を保存する。
      2. **「インポート」ボタン** を押すと、非同期タスク (`Celery`) が開始する。
      3. `import_type` に応じて、適切なインポートメソッドを呼び出す。

          | **import_type の値** | **実行する処理** |
          |----------------|----------------|
          | `Author` | 著者DB用のインポート (`authors` テーブル) |
          | `ID_Prefix` | 著者識別子用のインポート (`authors_prefix_settings` テーブル) |
          | `Affiliation_ID` | 機関識別子用のインポート (`authors_affiliation_settings` テーブル) |

  - **インポートステータスの管理**
      - 各インポートタスクの ID を Redis (`WEKO_AUTHORS_IMPORT_CACHE_KEY`) に保存。
      - `check_import_status` メソッドが定期的に実行され、処理が完了したタスクに関して **結果タブの画面が自動更新** される。
      - すべてのタスクが完了した時点で、Redis の `WEKO_AUTHORS_IMPORT_CACHE_KEY` を削除。

  - **エラーハンドリング**
      | **エラー発生箇所** | **対応** |
      |----------------|----------------|
      | **TSV のフォーマット不一致** | エラーメッセージを表示し、次のステップへ進めない |
      | **Celery ワーカーが停止** | エラーメッセージを表示し、インポートを禁止 |
      | **Redis キーが既に存在** | 前回の処理が完了していないため、インポートを禁止 |
      | **DB エラー (SQLAlchemyError)** | リトライ（最大 `5回`）、失敗した場合はスキップ |
      | **Redis エラー (RedisError)** | リトライ（最大 `5回`）、失敗した場合はエラーを表示 |

  - **著者DBのインポートについて**
      - 著者DBのインポートについては著者の量によっては処理が重くなるためバッチ処理を行う。
      - 関係メソッド：
          - ImportView.check_import_file  
          - ImportView.check_pagination
          - ImportView.check_file_download
          - ImportView.import_authors
          - ImportView.result_file_download

      - 定数は以下 =右はデフォルト値
          - `WEKO_AUTHORS_IMPORT_CACHE_USER_TSV_FILE_KEY`= 'authors_import_user_file_key'
              - インポート時にユーザーからのファイルを一時ファイルとして取り込んだ際のパスをredisに保存する目的
          - `WEKO_AUTHORS_IMPORT_CACHE_BAND_CHECK_USER_FILE_PATH_KEY` = "authors_import_band_check_user_file_path"
              - インポートタブにてチェック結果tsvのパスをredisに保存する目的
          - `WEKO_AUTHORS_IMPORT_CACHE_RESULT_OVER_MAX_FILE_PATH_KEY` = "authors_import_result_file_of_over_path"
              - 最大表示数を超えた分のインポート結果tsvのパスをredisに保存する目的
          - `WEKO_AUTHORS_IMPORT_CACHE_RESULT_FILE_PATH_KEY` = "authors_import_result_file_path"
              - 全てのインポート結果をまとめたtsvのパスをredisに保存する目的
          - `WEKO_AUTHORS_IMPORT_CACHE_OVER_MAX_TASK_KEY` = "authors_import_over_max_task"
              - 最大表示数を超えた分のインポートタスクのtaskIDをredisに保存する目的
          - `WEKO_AUTHORS_IMPORT_CACHE_RESULT_SUMMARY_KEY` = "authors_import_summary"
              - 最大表示数を超えた分のタスクの成功数、失敗数をredisに保存する目的
          - `WEKO_AUTHORS_IMPORT_BATCH_SIZE` = 100
              - インポートタスクのバッチサイズ
          - `WEKO_AUTHORS_IMPORT_MAX_NUM_OF_DISPLAYS` = 1000
              - 結果タブにおける最大表示数
          - `WEKO_AUTHORS_BULK_IMPORT_MAX_RETRY` = 5
              - インポート処理時の最大リトライ数
          - `WEKO_AUTHORS_BULK_IMPORT_RETRY_INTERVAL` = 5
              - インポート処理時のリトライ間隔
      1. **インポートチェック結果・インポート結果について**

          - **ページネーションの仕様**
              - フロント側で表示レコード数の制限を行う
              - ページネーションの流れ
                  1. ユーザーがページを選択すると、フロント側で `page` パラメータを API に渡す  
                  2. サーバサイドは以下の処理を実行  
                      - 指定された TSV ファイルを開く  
                      - `page` パラメータに基づいてデータを抽出  
                      - フロントへ返却  
                  3. フロントは取得したデータを表に表示する
              - なお、結果タブの方ではcelorytaskの進捗管理の兼ね合いで表示数をWEKO_AUTHORS_IMPORT_MAX_NUM_OF_DISPLAYSまで制限する。  
                表示されていないものの進捗確認はサマリーをページ上部に追加することで対応、結果はダウンロードボタンからtsvで確認するものとする。


          -  **一時ファイルの管理**
              -  **保存ディレクトリ**
                  - `/var/tmp/authors_import`

              - **生成される一時ファイル**
                  - インポートでユーザーから埋め込まれたtsvファイルは一時ファイルとして以下のようなファイル名で保存するものとする。  
                      import_author_{yyyymmddhhmm}.tsv 
                  - インポートチェック結果を一時ファイルとして保存する。
                      - データ数が定数`WEKO_AUTHORS_IMPORT_BATCH_SIZE`を超える場合、分割してチェック結果を一時ファイルとして保存する。  
                          ファイル名は**定数WEKO_AUTHORS_IMPORT_TMP_PREFIX+_{yyyymmddhhmm}_part{}** として保存する。
                      - ダウンロードする際には分割したファイルを合体させ、ファイル名としては**import_author_check_result_{yyyymmddhhmm}.tsv**とする。
                          インポートチェック結果のtsvで保存する情報としては以下
                          - No.
                          - Current WEKO ID	
                          - New WEKO ID
                          - full_name
                          - Mail Address
                          - チェック結果
                  - インポート結果を一時ファイルとしてtsvファイルで保存する。
                      - ファイル名としては**import_author_result_{yyyymmddhhmm}.tsv**とする。
                          インポート結果のtsvで保存する情報としては以下
                          - NO.
                          - Start Date
                          - End Date
                          - Previous WEKO ID
                          - New WEKO ID
                          - full_name
                          - status

              - **ファイル削除のタイミング**
                  | ファイル | 削除条件 |
                  |-----------------|------------------------------------------------|
                  | `import_author_{yyyymmddhhmm}.tsv` | インポートチェック完了時 / 保存期間24 時間経過時|
                  | `import_author_check_result_{yyyymmddhhmm}.tsv` | 別インポートチェック時 / 保存期間24 時間経過時 |
                  | `import_author_result_{yyyymmddhhmm}.tsv` | 別インポート開始時 / インポート完了後 24 時間経過時（Celery タスクで削除） |

              - 保存期間は （デフォルト: 24時間）で管理
              - 削除処理は Celery タスクが定期的に実行

          - **インポートタブでの表示処理の流れ**
              1. **フロント側**
                  - ユーザーがページを選択
                  - `GET /api/import/results?page={page}` のような API リクエストを送信

              2. **サーバ側**
                  - `page` に基づき、該当 TSV ファイルの該当データを取得
                  - 以下のtsvからデータを返却
                      - **インポートタブ**: `import_author_check_result_{yyyymmddhhmm}_part{}.tsv`

              3. **フロント側**
                  - 取得したデータを表に表示

          - **インポート処理**
              - 定数`WEKO_AUTHORS_IMPORT_MAX_NUM_OF_DISPLAYS`までのデータは既存の処理通り、フロントにtaskidを渡し、都度更新する。
                  - 定数`WEKO_AUTHORS_IMPORT_MAX_NUM_OF_DISPLAYS`以降のデータは先に処理しているタスクが終了後バックエンド側で  
                      定数`WEKO_AUTHORS_IMPORT_BATCH_SIZE`分ずつインポートタスクを実行する。  
                      - インポートタスクが終了するごとに以下の処理を行う。
                          - 一時ファイルに結果を書き込んでいく。  
                              なお、パスは定数`WEKO_AUTHORS_IMPORT_CACHE_RESULT_OVER_MAX_FILE_PATH_KEY`を用いてRedisに保存する。
                          - 成功数、失敗数をカウントし、定数`WEKO_AUTHORS_IMPORT_CACHE_RESULT_SUMMARY_KEY`を用いてRedisに保存する。
                              - 結果タブでのサマリーはこれを用いて表示する。

          - **ダウンロード機能**
              - **インポートタブの「ダウンロード」ボタン**  
                  - `import_author_check_result_{yyyymmddhhmm}.tsv` が既にあればダウンロード
                  - ない場合、partごとに分けられているインポートチェック結果の一時ファイルからそれらを合体させ、  
                      `import_author_check_result_{yyyymmddhhmm}.tsv`を生成し保存する。
              - **結果タブの「ダウンロード」ボタン**  
                  - `import_author_result_{yyyymmddhhmm}.tsv` が既にあればダウンロード
                  - ない場合、`WEKO_AUTHORS_IMPORT_CACHE_RESULT_OVER_MAX_FILE_PATH_KEY`でredisから取得したファイルパスのファイルと
                      フロントで表示されている分のインポート結果を合体させ、`import_author_result_{yyyymmddhhmm}.tsv`を生成し、保存する。


      2. **エラー時のリトライ機能**

          - **リトライ対象のエラー**
              - 以下の例外が発生した場合にリトライ対象とする：
                  - `SQLAlchemyError`（DB 接続エラー、タイムアウトエラー）
                  - `ElasticsearchException`（ElasticSearch 接続エラー、タイムアウトエラー）
                  - `RedisError`（Redis 接続エラー、タイムアウトエラー）
                  - `TimeoutError`（システムタイムアウトエラー）

          - **リトライのルール**
              - DB のセッションについて、エラー発生時に必ずロールバックする
              - 最大リトライ回数: `WEKO_AUTHORS_BULK_IMPORT_MAX_RETRY`（デフォルト 5 回）
              - リトライ間隔: `WEKO_AUTHORS_BULK_IMPORT_RETRY_INTERVAL`（デフォルト 5 秒）

          - **エラー発生時の処理フロー**
              - リトライ可能なエラーの場合
                  1. 指定回数 (`WEKO_AUTHORS_BULK_IMPORT_MAX_RETRY`) までリトライを実行する。
                  2. リトライで成功した場合 → 通常通り処理を継続
                  3. 指定回数リトライしても解決しなかった場合：
                      - そのデータを処理対象から除外
                      - エラーとなったデータは `FAILURE` ステータスを設定
                      - 次のデータの処理へ進む

              - リトライ不可のエラー（例外）発生時
                  - 予期しないエラー（例: プログラムエラー、致命的なシステム障害）が発生した場合：
                      - そのデータを処理対象から除外
                      - 該当タスクのステータスを `FAILURE` とする
                      - エラーログに詳細を記録し、復旧対応が可能なようにする

          - ログ・エラーハンドリング
              - リトライ回数をログに記録
              - リトライ失敗時にはエラーログにエラー内容を出力

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
<td></td>
<td>V0.9.27
</td>
</tr><tr class="even">
<td><blockquote>
<p>2025/03/27</p>
</blockquote></td>
<td></td>
<td>v1.1.0対応</td>
</tr>
</tbody>
</table>
