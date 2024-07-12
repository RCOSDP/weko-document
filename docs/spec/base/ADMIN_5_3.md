
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
<td>ファイル選択(Select File)</td>
<td>ボタンを押下すると、ファイルのアップロードウィンドウを表示する。<br />
ユーザは任意の著者DBのインポート用ファイルを選択する。<br />
なお、選択できる形式は「tsv」ファイルのみとする。</td>
</tr>
<tr class="even">
<td>2</td>
<td>次へ(Next)</td>
<td>ボタンを押下すると、選択したファイルの形式(フォーマット)をチェックし、問題無ければ「インポート(Import)」タブへ自動遷移する。<br />
エラーがある場合は、「選択(Select)」タブ上部に赤枠でエラーメッセージを表示し、「インポート(Import)」タブへ遷移はしない。<br />
本ボタンの初期状態は非活性とする。<br />
ユーザがファイルを選択後、活性化する。</td>
</tr>
</tbody>
</table>

  - ファイル未選択の場合は\[ファイル選択(Select File)\]ボタン下に「選択したファイル名(Selected file name)」というラベルをグレーで表示する。  
    ファイル選択後、選択されたファイルのファイル名を表示する

  - 　

「インポート(Import)」タブ

  - 本タブは、読み込んだ著者DBのインポート用ファイルの内容をチェックし、登録して良いかの確認を促すものである。画面構成は以下の通り

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
・ファイル名は「Creator_Check_yyyymmdd.tsv」とする。<br />
・画面上トリミングされている情報があっても、ファイルにはすべて出力される</td>
</tr>
</tbody>
</table>

  - 画面に読み込んだ著者DBのインポート用ファイルの「サマリー(Summary)」を以下のように表示する

| \# | 項目名            | 概要                      |
| -- | -------------- | ----------------------- |
| 1  | 総計(Total)      | 読み込んだファイルの著者の数          |
| 2  | New Creator    | 読み込んだファイルの内、新規登録となる著者の数 |
| 3  | Update Creator | 読み込んだファイルの内、更新の著者の数     |
| 4  | Delete Creator | 読み込んだファイルの内、削除となる著者の数   |
| 5  | Result Error   | 内容のチェックでエラーとなった著者の数     |

  - 画面に表示される著者の詳細情報は以下の通り

<table>
<thead>
<tr class="header">
<th>#</th>
<th>項目名</th>
<th>概要</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>No.</td>
<td>読み込んだファイルの著者の通し番号を表示する。</td>
</tr>
<tr class="even">
<td>2</td>
<td>WEKOID</td>
<td>読み込んだ著者のWEKO著者IDを表示する。</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Full_Name</td>
<td>読み込んだ著者の姓と名を表示する。<br />
姓と名の間はカンマ＋スペース「姓, 名」で表示する。</td>
</tr>
<tr class="even">
<td>4</td>
<td>Mail Address</td>
<td>読み込んだ著者のメールアドレスを表示する。</td>
</tr>
<tr class="odd">
<td>5</td>
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
<td>ダウンロード(Download)</td>
<td>ボタンを押下すると、画面に表示されている著者のリストをTSV形式でダウンロードできる。<br />
・文字コードはBOM無しUTF-8、改行コードはCR+LFとする<br />
・ファイル名は「Creator_List_Download_yyyymmdd.tsv」とする</td>
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
<tr class="odd">
<td>1</td>
<td>No.</td>
<td>読み込んだファイルの著者の通し番号を表示する。</td>
</tr>
<tr class="even">
<td>2</td>
<td>開始日(Start Date)</td>
<td>１著者に対して登録処理を開始した日時を表示する。<br />
フォーマット：YYYY-MM-DD hh:mm:ss</td>
</tr>
<tr class="odd">
<td>3</td>
<td>終了日(End Date)</td>
<td>１著者に対して登録処理が完了した日時を表示する。<br />
フォーマット：YYYY-MM-DD hh:mm:ss</td>
</tr>
<tr class="even">
<td>4</td>
<td>WEKOID</td>
<td>読み込んだ著者のWEKO著者IDを表示する。</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Full_name</td>
<td>読み込んだ著者の姓と名を表示する。<br />
姓と名の間はカンマ＋スペース「姓, 名」で表示する。</td>
</tr>
<tr class="even">
<td>6</td>
<td>ステータス(Status)</td>
<td>登録した結果を表示する。<br />
・「Register Success」：新規登録が完了した場合に表示<br />
・「Update Success」：変更・更新登録が完了した場合に表示<br />
・「Delete Success」：削除が完了した場合に表示<br />
・「ERROR: XXXXX」：エラーが発生した場合に表示</td>
</tr>
</tbody>
</table>

  - 登録処理は、バックグラウンドで実行し、１著者毎にコミットしながら処理を進める

  - 登録情報は、著者のテーブルとESに登録する

  - 本タブを開いた状態で画面をリロードすることで、登録状況が更新されるものとする

  - 「選択(Select)」タブ，「インポート(Import)」タブへの遷移は可能とする。ただし、登録処理実行中は、各ボタンは非活性とする

(2) 入力ファイル

  - 入力ファイルはtsv形式で出力される

  - tsvファイルの構成は以下の通り

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

<!-- end list -->

  - 各ヘッダの情報は以下の通り

<table>
<thead>
<tr class="header">
<th>#</th>
<th>ヘッダ項目</th>
<th>ラベル(日本語)</th>
<th>ラベル(英語)</th>
<th>概要</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>pk_id</td>
<td>WEKO ID</td>
<td>WEKO ID</td>
<td>WEKO3の著者ID(author_link)を入力する</td>
</tr>
<tr class="even">
<td>2</td>
<td>authorNameInfo[0...n].familyName</td>
<td>姓</td>
<td>Family Name</td>
<td>著者の姓を入力する</td>
</tr>
<tr class="odd">
<td>3</td>
<td>authorNameInfo[0...n].firstName</td>
<td>名</td>
<td>Given name</td>
<td>著者の名を入力する</td>
</tr>
<tr class="even">
<td>4</td>
<td>authorNameInfo[0...n].language</td>
<td>言語</td>
<td>Language</td>
<td>著者の言語を入力する</td>
</tr>
<tr class="odd">
<td>5</td>
<td>authorNameInfo[0...n].nameFormat</td>
<td>フォーマット</td>
<td>name Format</td>
<td>著者の姓名のフォーマットを入力する<br />
※現状(SP67時点)は「familyNmAndNm」固定</td>
</tr>
<tr class="even">
<td>6</td>
<td>authorNameInfo[0...n].nameShowFlg</td>
<td>姓名・言語 表示／非表示</td>
<td>Name Display</td>
<td>著者の姓名と言語の表示／非表示を入力する<br />
表示する: "Y"<br />
表示しない: "N"</td>
</tr>
<tr class="odd">
<td>7</td>
<td>authorNameInfo[0...n].idType</td>
<td>外部著者ID 識別子</td>
<td>Identifier Scheme</td>
<td>外部著者IDの識別子を入力する</td>
</tr>
<tr class="even">
<td>8</td>
<td>authorNameInfo[0...n].authorId</td>
<td>外部著者ID URI</td>
<td>Identifier URI</td>
<td>外部著者IDの値を入力する</td>
</tr>
<tr class="odd">
<td>9</td>
<td>authorNameInfo[0...n].authorIdShowFlg</td>
<td>外部著者ID 表示／非表示</td>
<td>Identifier Display</td>
<td>外部著者IDの表示／非表示を入力する<br />
表示する: "Y"<br />
表示しない: "N"</td>
</tr>
<tr class="even">
<td>10</td>
<td>emailInfo[0...n].email</td>
<td>メールアドレス</td>
<td>Mail Address</td>
<td>著者のメールアドレスを入力する</td>
</tr>
<tr class="odd">
<td>11</td>
<td>is_deleted</td>
<td>削除フラグ</td>
<td>Delete Flag</td>
<td>著者を削除する場合に "D" と入力する</td>
</tr>
</tbody>
</table>

　【補足】  
　　・繰り返し項目とする場合はヘッダ行の各項目名の後ろに \[1\], \[2\], ..., \[N\] と入力する。  
　　　※1つ目の項目名には \[0\] が記載されている。  
　　・WEKO ID, Delete Flagは繰り返し記載することはできない。  
　　・姓名のフォーマットの値が空欄の場合は「familyNmAndNm」の値を固定でシステムが登録する。

　　・コンテンツのファイルサイズが空欄の場合はシステムが登録する。

(3) エラーチェック

  - 本画面でチェックしているエラー内容は以下の通り

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
<tr class="odd">
<td>1</td>
<td>選択(Select)</td>
<td>tsvファイルの形式のチェック<br />
#1: 選択したファイルがtsvファイルでは無い、またはtsvファイルの文字コードがUTF-8では無い<br />
#3: tsvファイルの形式のエラー(タブ無し, ヘッダ行無し)</td>
<td>ERROR</td>
<td>TSVファイルを読み込めませんでした。ファイル形式がTSVであること、またそのファイルがUTF-8でエンコードされているかを確認してください。</td>
<td>The TSV file could not be read. Make sure the file format is TSV and that the file is UTF-8 encoded.</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>選択(Select)</td>
<td>ヘッダ行だけの空レコードになっている</td>
<td>ERROR</td>
<td>インポートのデータがありません。</td>
<td>There is no data to import.</td>
<td></td>
</tr>
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
<td>5</td>
<td>選択/インポート<br />
(Select/Import)</td>
<td>Celeryが動いていない状態</td>
<td>ERROR</td>
<td>Celeryは動いていません。</td>
<td>Celery is not running.</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>選択/インポート<br />
(Select/Import)</td>
<td>自分の端末にインポートを実行しているうちに、インポートを実行する</td>
<td>ERROR</td>
<td>インポートを実行中です。</td>
<td>Import is in progress.</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>選択/インポート<br />
(Select/Import)</td>
<td>他の端末でインポートを実行している</td>
<td>ERROR</td>
<td>他の端末でインポートを実行中です。</td>
<td>Import is in progress on another device.</td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>インポート(Import)</td>
<td>他の著者情報を入力されたが、idTypeとauthorIdのいずれかを入力されていない状態</td>
<td>ERROR</td>
<td>{}は必須項目です。</td>
<td>{} is required item.</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>インポート(Import)</td>
<td>#4 著者が一意に定まらない(存在しないWEKO ID (author_link)<br />
#5 削除対象の著者がDBに存在しない</td>
<td>ERROR</td>
<td>指定されたWEKO IDが存在していません。</td>
<td>Specified WEKO ID does not exist.</td>
<td></td>
</tr>
<tr class="even">
<td>10</td>
<td>インポート(Import)</td>
<td>#6 言語の指定でDBに存在しない言語を入力する<br />
#8 ヘッダ項目#5の姓名・言語 表示／非表示で"Y","N"以外を入力する<br />
#9 ヘッダ項目#8の外部著者識別子 表示／非表示で"Y","N"以外を入力する</td>
<td>ERROR</td>
<td>{1}は{2}のいずれかを設定してください。</td>
<td>{1} should be set by one of {2}.</td>
<td>{1}: language, nameShowFlg, authorIdShowFlg<br />
{2}: 言語の一覧、"Y","N"</td>
</tr>
<tr class="odd">
<td>11</td>
<td>インポート(Import)</td>
<td>#10 ヘッダ項目#10の削除フラグで"D"以外を入力する<br />
#13 姓名のフォーマットの値が「familyNmAndNm」以外の値</td>
<td>ERROR</td>
<td>{1}は{2}を設定してください。</td>
<td>{1} should be set by one of {2}.</td>
<td>{1}: is_deleted, nameFormat<br />
{2}: "D"、"familyNmAndNm"</td>
</tr>
<tr class="even">
<td>12</td>
<td>インポート(Import)</td>
<td>ID PrefixでDBに存在しない識別子を入力する</td>
<td>ERROR</td>
<td>指定された外部著者ID 識別子'{1}'が存在していません。</td>
<td>Specified Identifier Scheme '{1}' does not exist.</td>
<td>{1}:外部著者ID 識別子</td>
</tr>
<tr class="odd">
<td>13</td>
<td>インポート(Import)</td>
<td>TSVファイルの中に重複するデータがある</td>
<td>ERROR</td>
<td>TSVファイルの中に重複するデータがあります。</td>
<td>There is duplicated data in the TSV file.</td>
<td>各レコードがマルチタスクで実行されているので、後勝ちで2番目のデータを上書きするのが難しい(重複する場合にどのレコードで更新されるか定まらない)。WARNING→ERRORに変更し、2つ目以降は更新されないようにする</td>
</tr>
<tr class="even">
<td>14</td>
<td>インポート(Import)</td>
<td>外部著者識別子がDBに存在している</td>
<td>WARNING</td>
<td>外部著者識別子がDBに存在しています。<br />
{1}</td>
<td>External author identifier exists in DB.<br />
{1}</td>
<td>{1}:外部著者識別子</td>
</tr>
<tr class="odd">
<td>15</td>
<td>選択/インポート/結果<br />
(Select/Import/Result)</td>
<td>サーバ内部エラー（ネットワークの問題、予期しない例外など）が発生した</td>
<td>ERROR</td>
<td>サーバ内部エラー</td>
<td>Internal server error</td>
<td></td>
</tr>
<tr class="even">
<td>16</td>
<td>結果(Result)</td>
<td>登録成功</td>
<td>INFO</td>
<td>登録成功</td>
<td>Register Success</td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td>結果(Result)</td>
<td>更新成功</td>
<td>INFO</td>
<td>更新成功</td>
<td>Update Success</td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td>結果(Result)</td>
<td>削除成功</td>
<td>INFO</td>
<td>削除成功</td>
<td>Delete Success</td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td>結果(Result)</td>
<td>エラーが発生したため、インポートに失敗した</td>
<td>ERROR</td>
<td>インポートに失敗しました。</td>
<td>Failed to import.</td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td>インポート(Import)</td>
<td>削除済みの著者について、tsvに該当の著者情報を指定して更新した</td>
<td>WARNING</td>
<td>指定された著者は削除済です。tsvの内容で著者情報を更新しますが、著者は削除されたままです。</td>
<td>The specified author has been deleted. Update author information with tsv content, but author remains deleted as it is.</td>
<td></td>
</tr>
<tr class="odd">
<td>21</td>
<td>インポート/結果<br />
(Import/Result)</td>
<td>アイテムに紐づいている著者を削除した</td>
<td>ERROR</td>
<td>アイテムがリンクしているため、指定された著者は削除できません。</td>
<td>The author is linked to items and cannot be deleted.</td>
<td>英語のメッセージが既存<br />
日本語のメッセージを新規追加</td>
</tr>
<tr class="even">
<td>22</td>
<td>インポート(Import)</td>
<td>存在しないインデックスにインポートしようとした</td>
<td>ERROR</td>
<td>指定された{}はシステムに存在しません。</td>
<td>The specified {} does not exist in system.</td>
<td></td>
</tr>
<tr class="odd">
<td>22</td>
<td>インポート(Import)</td>
<td></td>
<td>ERROR</td>
<td>ロールの権限が足りずこのインデックスにアイテム登録ができません。</td>
<td>Your role cannot register items in this index.</td>
<td></td>
</tr>
</tbody>
</table>

  - 処理の「エラー」は登録不可、「ワーニング」は登録可能とする。

(4) その他

  - バックグラウンドでインポート処理を実行する。

  - 著者情報は論理削除とする。

  - 著者DBのインポート機能により、著者DBを更新／削除した際は、紐づくアイテムの著者情報までは更新を行わない。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-authors

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - > ファイル選択を押下し、任意のtsvファイルを選択したのちに\[次へ（Next）\]ボタンを押下することでweko\_authors.admin.ImportView.check\_import\_fileが呼び出されファイルの内容のバリデーションチェックが行われる。問題がなければファイルの内容をjson形式で返し、インポート画面へと自動で遷移する。

  - > インポート画面で、\[インポート（import）\]ボタンを押下することで、weko\_authors.task.import\_authorが呼び出され、その中でweko\_authors.util.import\_author\_to\_systemが呼ばれ、db内のauthorsテーブルの情報が更新される。問題なく更新されるとweko\_authors.admin.check\_import\_statusが呼び出され結果画面に表示される情報を取得し、自動で結果画面に遷移する。

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
