
# 一括出力

## 目的・用途

本機能は、著者DBの情報を一括出力する機能である。

## 利用方法

本画面にある \[エクスポート(Export)\] ボタンを押下することで、著者DBに登録されている著者情報をtsvファイルで出力する。

tsvファイルのダウンロードURLにアクセスすることでtsvファイルを取得することができる。

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## 機能内容

(1) 一括出力画面の画面構成

  - 出力対象テーブル(Export target)
      - プルダウンの選択肢としては以下のもの
          - 著者情報(Author)
          - 著者識別子(ID_Prefix)
          - 機関識別子(Affiliation_ID)
      - デフォルトでは「著者情報(Author)」が選択されている。
      - このプルダウンで選択されている情報がエクスポートの対象となる。

  - 全件エクスポート(Export all)
      - 全件エクスポートを実行する。以下の2種類のボタンがある。
          - [エクスポート(Export)] ボタン
              - ボタンを押下すると、以下のポップアップのメッセージとボタンが表示される
                  - 「対象の全件エクスポートを実行してよいですか？(Are you sure you want to export all?)」  
                      - [実行(Execute)] ボタン：対象の全件エクスポートを実行し、自画面に戻る  
                      - [キャンセル(Cancel)] ボタン：何も処理はせずに自画面に戻る
              - 対象の全件エクスポート実行中は、ボタンは非活性となる
          - [キャンセル(Cancel)] ボタン
              - 対象の全件エクスポートを中断する。エクスポート実行中以外は非活性である。
              - 対象の全件エクスポート実行中にボタンが活性化される。ボタンを押下すると、以下のポップアップのメッセージとボタンが表示される。  
                  「メッセージ」  
                  　日本語：全件エクスポートの処理をキャンセルしてよいですか？  
                  　英語：Are you sure you want to cancel process of exporting all ?  
                  「ボタン」  
                  　[実行(Execute)] ボタン：全件エクスポートを中断し、自画面に戻る。  
                  　[キャンセル(Cancel)] ボタン：中断はせずに自画面に戻る(全件エクスポート処理を継続する)。
  - ダウンロードURL(Download URL)
      - 全件エクスポートが完了すると、出力ファイル(tsv形式)をダウンロードできるURLが表示される

      - 最後に出力されたダウンロードURLが表示される（初期の全件エクスポート実行前は何も表示されない）  
          Export targetの値に応じて著者情報(Author)、著者識別子(ID_Prefix)、機関識別子(Affiliation_ID)のダウンロードURLが1つ表示される。

      - ダウンロードのURLの例(初期値)としては以下の通り（出力ファイル名はConfigで設定できるものとする）
          - 著者情報：　https://{Domain_Name}/admin/authors/export/download/Creator_export_all_{yyyyMMddhhmm}.tsv
          - 著者識別子：https://{Domain_Name}/admin/authors/export/download/Id_prefix_export_all_{yyyyMMddhhmm}.tsv
          - 機関識別子：https://{Domain_Name}/admin/authors/export/download/Affiliation_export_all_{yyyyMMddhhmm}.tsv

(2) 出力ファイル

  - 全件エクスポートされたファイルはtsv形式で出力される。

  - 著者情報のtsvファイルの構成、各ヘッダについては以下の通り

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

  - 文字コードはUTF-8(BOM付き)，改行コードはCR+LFとする。

  - １行目はヘッダ行とし、システム管理するものである。先頭に"\#"が付いている。

  - ２行目と３行目はラベルを表示し、TSV入力の補助をする。先頭に"\#"が付いている。

  - ４行目以降に著者の情報を出力する。１著者の情報を1行で出力する。

<!-- end list -->

  - 各ヘッダの情報は以下の通り

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
    <td >このリポジトリ内でのpk_idを出力する</td>
    </tr>
    <tr >
    <td>2</td>
    <td>weko_id</td>
    <td>WEKO ID</td>
    <td>WEKO ID</td>
    <td>WEKO IDを出力する</td>
    </tr>
    <tr >
    <td>3</td>
    <td>authorNameInfo[0...n].familyName</td>
    <td>姓</td>
    <td>Family Name</td>
    <td>著者の姓を出力する</td>
    </tr>
    <tr >
    <td>4</td>
    <td>authorNameInfo[0...n].firstName</td>
    <td>名</td>
    <td>Given name</td>
    <td>著者の名を出力する</td>
    </tr>
    <tr >
    <td>5</td>
    <td>authorNameInfo[0...n].language</td>
    <td>言語</td>
    <td>Language</td>
    <td>著者の言語を出力する</td>
    </tr>
    <tr >
    <td>6</td>
    <td>authorNameInfo[0...n].nameFormat</td>
    <td>フォーマット</td>
    <td>name Format</td>
    <td>著者の姓名のフォーマットを出力する<br />
    ※現状(SP67時点)は「familyNmAndNm」固定</td>
    </tr>
    <tr >
    <td>7</td>
    <td>authorNameInfo[0...n].nameShowFlg</td>
    <td>姓名・言語 表示／非表示</td>
    <td>Name Display</td>
    <td>著者の姓名と言語の表示／非表示を出力する<br />
    表示する: "Y"<br />
    表示しない: "N"</td>
    </tr>
    <tr >
    <td>8</td>
    <td>authorIdInfo[0...n].idType</td>
    <td>外部著者ID 識別子</td>
    <td>Identifier Scheme</td>
    <td>外部著者IDの識別子を出力する</td>
    </tr>
    <tr >
    <td>9</td>
    <td>authorIdInfo[0...n].authorId</td>
    <td>外部著者ID URI</td>
    <td>Identifier URI</td>
    <td>外部著者IDの値を出力する</td>
    </tr>
    <tr >
    <td>10</td>
    <td>authorIdInfo[0...n].authorIdShowFlg</td>
    <td>外部著者ID 表示／非表示</td>
    <td>Identifier Display</td>
    <td>外部著者IDの表示／非表示を出力する<br />
    表示する: "Y"<br />
    表示しない: "N"</td>
    </tr>
    <tr >
    <td>11</td>
    <td>emailInfo[0...n].email</td>
    <td>メールアドレス</td>
    <td>Mail Address</td>
    <td>著者のメールアドレスを出力する</td>
    </tr>
    <tr >
    <td>12</td>
    <td>is_deleted</td>
    <td>削除フラグ</td>
    <td>Delete Flag</td>
    <td>著者を削除する場合に "D" と出力する<br />
    ※論理削除された著者情報は出力しないため、全件エクスポートではすべて空欄となる</td>
    </tr>
    <tr  >
    <td>13</td>
    <td>authorAffiliationInfo[0...n].affiliationId[0...n].idtype</td>
    <td>外部所属機関ID 識別子</td>
    <td>Affiliation Identifier Scheme</td>
    <td>外部所属機関IDの識別子を出力する</td>
    </tr>
    <tr  >
    <td>14</td>
    <td>authorAffiliationInfo[0...n].affiliationId[0...n].uri</td>
    <td>外部所属機関ID URI</td>
    <td>Affiliation Identifier URI</td>
    <td>外部所属機関IDの値を出力する</td>
    </tr>
    <tr  >
    <td>15</td>
    <td>authorAffiliationInfo[0...n].authorIdShowFlg</td>
    <td>外部所属機関ID 表示／非表示</td>
    <td>Affiliation Identifier Display</td>
    <td>外部所属機関IDの表示／非表示を出力する<br />
    表示する: "Y"<br />
    表示しない: "N"</td>
    </tr>
    <tr  >
    <td>16</td>
    <td>authorAffiliationInfo[0...n].affiliationNameInfo[0...n].affiliationName</td>
    <td>外部所属機関名</td>
    <td>Affiliation Name</td>
    <td>外部所属機関名を出力する</td>
    </tr>
    <tr  >
    <td>17</td>
    <td>authorAffiliationInfo[0...n].affiliationNameInfo[0...n].language</td>
    <td>言語</td>
    <td>Language</td>
    <td>外部所属機関名の言語を出力する</td>
    </tr>
    <tr  >
    <td>18</td>
    <td>authorAffiliationInfo[0...n].affiliationNameInfo[0...n].nameShowFlg</td>
    <td>外部所属機関名・言語 表示／非表示</td>
    <td>Affiliation Name Display</td>
    <td>外部所属機関名と言語の表示／非表示を出力する<br />
    表示する: "Y"<br />
    表示しない: "N"</td>
    </tr>
    <tr  >
    <td>19</td>
    <td>authorAffiliationInfo[0...n].affiliationPeriod[0...n].period</td>
    <td>外部所属機関 所属期間</td>
    <td>Affiliation Period</td>
    <td>外部所属機関所属期間を出力する。<br/>
    所属開始のみ："20250127"<br/>
    所属開始・終了："20250127-20250317"</td>
    </tr>
    <tr  >
    <td>20</td>
    <td>authorAffiliationInfo[0...n].affiliationPeriod[0...n].nameShowFlg</td>
    <td>外部所属機関 所属期間 表示/非表示</td>
    <td>Affiliation Period Display</td>
    <td>外部所属機関 所属期間の表示／非表示を出力する<br />
    表示する: "Y"<br />
    表示しない: "N"</td>
    </tr>
    </tbody>
    </table>

　【補足】  
　　・同じ項目名を複数持つ場合は、各項目名の後ろに\[0\],\[1\],…,\[N\]と記載された状態で出力される。  
　　　※1つ目の項目名には \[0\] が記載されている。  
　　・Author ID, WEKO ID, Delete Flagは繰り返し記載することはできない。

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


(3) エラーメッセージ

  - 全件エクスポート処理においてエラーが発生した場合はその制御を行う

  - エラーメッセージは画面上部に赤く表示される。

  - 本画面でチェックしているエラー内容は以下の通り。

<table>
<thead>
<tr class="header">
<th>エラー発生条件</th>
<th>表示されるエラーメッセージ</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>エクスポートのキャンセルに失敗した場合<br />
（キャンセル中にエラーが発生した、またはキャンセルが実行される前にエクスポートが完了した場合）</td>
<td>エクスポートのキャンセルに失敗しました。<br />
（Failed to cancel export.）</td>
</tr>
<tr class="even">
<td>他のユーザが全件エクスポート処理を実行中の場合</td>
<td>他の端末でエクスポートを実行中です。<br />
（Export is in progress on another device.）</td>
</tr>
<tr class="odd">
<td>予期せぬエラーが発生した場合<br />
（ネットワークに問題があった場合など）</td>
<td>サーバ内部エラー<br />
（Internal server error）</td>
</tr>
</tbody>
</table>

(4) その他

  - バックグラウンドでエクスポート処理を実行する。

  - 論理削除された著者情報は出力されない。

  - 全件エクスポートで出力されたファイルと、著者の一括登録で登録するファイルの形式は同じものとする。

  - 実行結果をサーバ上（オブジェクトストレージのファイルインスタンス）に配置することで、管理者がダウンロードできるようにする。

  - 既に実行結果がファイルインスタンスに保存されている場合は上書きする。

  - 著者情報, 著者識別子, 機関識別子は1つのファイルインスタンスに保存される。
<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-authors

<!-- end list -->

- 処理概要

> modules/weko-authors/weko\_authors/config.py
    
  - **出力対象テーブルの設定**
      - **著者DB（Author DB）**
          - エクスポート画面のプルダウンで「Author DB」を選択した場合、出力対象は `authors` テーブル。
  
      - **著者識別子（ID Prefix）**
          - エクスポート画面のプルダウンで「ID Prefix」を選択した場合、出力対象は `authors_prefix_settings` テーブル。
          - 1行目には `authors_prefix_settings` の文字列を出力。

      - **機関識別子（Affiliation ID）**
          - エクスポート画面のプルダウンで「Affiliation ID」を選択した場合、出力対象は `author_affiliation_settings` テーブル。
          - 1行目には `author_affiliation_settings` の文字列を出力。

  - **全件エクスポートのファイル名の設定値（デフォルト値）**
      - 著者DB
          - `WEKO_AUTHORS_EXPORT_FILE_NAME = 'Creator_export_all'`
      - 著者識別子
          - `WEKO_AUTHORS_ID_PREFIX_EXPORT_FILE_NAME = 'Id_prefix_export_all'`
      - 機関識別子
          - `WEKO_AUTHORS_AFFILIATION_EXPORT_FILE_NAME = 'Affiliation_id_export_all'`

  - **エクスポート処理の流れ**
      1. **[エクスポート] ボタン押下**
        - `weko_authors.admin.ExportView.export` が呼び出される。 
      2. **非同期処理の開始**
          - `export_all` メソッドが非同期で実行される。
          - 引数として `Export target` の値を渡し、この値でエクスポート対象を決定する。
      3. **エクスポート対象テーブルの特定**
          - `Export target` の値に応じて、以下のテーブルをエクスポート対象とする。
              - 著者（authors） → `authors` テーブル
              - 著者識別子（authors_prefix） → `authors_prefix_settings` テーブル
              - 機関識別子（authors_affiliation） → `author_affiliation_settings` テーブル
      4. **RedisにファイルURIを保存**
          - キーを使ってredisに `file_uri` を保存。
              - 定数`WEKO_AUTHORS_EXPORT_CACHE_URL_KEY`の値を使う。
      5. **エクスポート状態の確認**
          - `check_status` メソッドが定期的に実行され、エクスポートの状態を確認。
          - キーが存在する場合、 `WEKO_AUTHORS_EXPORT_CACHE_URL_KEY` を使用して `file_uri` を取得し、次の6へ進む。
          - キーが存在しない場合、check_statusの処理を終了する。
      6. **ダウンロードリンクの表示**
          - 取得した `file_uri` を基に、ダウンロードリンクを画面に表示。
          - リンクのファイル名は `_{yyyyMMddhhmm}` を付加。
          - `Export target` に応じて、ファイル名を以下の定数から取得。
              - 著者 → `WEKO_AUTHORS_EXPORT_FILE_NAME`
              - 著者識別子 → `WEKO_ID_PREFIX_EXPORT_FILE_NAME`
              - 機関識別子 → `WEKO_AFFILIATION_ID_EXPORT_FILE_NAME`
      7. **ダウンロード処理**
        - ダウンロードリンクを押下すると、 `weko_authors.admin.ExportView.download` が呼び出され、ファイルをダウンロードする。

  - **著者DBのエクスポートについて**
      - 著者DBのエクスポートについては著者の量によっては処理が重くなるためバッチ処理を行う。
      - 定数は以下 =右はデフォルト値
          - `WEKO_AUTHORS_EXPORT_CACHE_TEMP_FILE_PATH_KEY` = 'weko_authors_export_temp_file_path_key'
              - exportを行うための一時ファイルのパスをredisに保存する目的
          - `WEKO_AUTHORS_EXPORT_CACHE_STOP_POINT_KEY` = "weko_authors_export_stop_point"
              - exportが一時停止した際に止まった位置をredisに記録する目的
          - `WEKO_AUTHORS_EXPORT_TMP_PREFIX` = 'authors_export_'
              - export時の一時ファイルの命名が目的
          - `WEKO_AUTHORS_EXPORT_BATCH_SIZE` = 1000
              - export時のバッチサイズ
          - `WEKO_AUTHORS_BULK_EXPORT_MAX_RETRY` = 5
              - export時のコネクションエラー用の最大リトライ回数
          - `WEKO_AUTHORS_BULK_EXPORT_RETRY_INTERVAL` = 5
              - export時のコネクションエラー用のリトライインターバル
          - `WEKO_AUTHORS_CACHE_TTL` = 60 * 60 * 24
              - キャッシュの維持時間

      1. **DB接続処理のバッチ処理化**
          1. エクスポート開始時の処理
              - 一時ファイルを作成する。
              -  Redisのキー `weko_authors_export_temp_file_path_key` に以下の情報を書き込む。
                  - **値:** 一時ファイルのパス  
                      `/var/tmp/authors_export/authors_export_xxxxxxxx.tsv`
          2. バッチ処理の実行（非同期処理）
              Celeryで以下の処理をタスク化し、非同期で実行する。
              1. 定数 `WEKO_AUTHORS_EXPORT_BATCH_SIZE` をバッチサイズとして、  
              `authors` テーブルから `id` カラムの昇順でレコードを取得する。  
              2. `folder_path` で指定された一時ファイル（TSV）に取得したレコードを書き込む。  
                  - バッチごとに追記する形式とする。  
              3. 2を繰り返し、authorsテーブルの全てのレコードを書き終えた後、以下を実行する。  
                  - 完成したTSVファイルを**ファイルインスタンス**に保存する。  
                  - Redisのキー `weko_author_export_cache_key` に `status: success` を設定する。  
                  - **ファイルインスタンスの保存ルール:**  
                      - 既存のファイルがある場合は上書きする。  
                      - 保存時のファイル名は、定数 `WEKO_AUTHORS_EXPORT_FILE_NAME` に `yyyyMMddhhmm` を付加した形式とする。  
                      （例: `Creator_export_all_{yyyyMMddhhmm}`）  
              4. ファイルインスタンスへの保存後、一時ファイルを削除する。  

          3. フロントエンド側の処理
              フロントエンドは定期的に Redis のキー `weko_authors_export_status` の `status` をチェックし、エクスポートの状態を取得する。

              - **3.1 エクスポートステータスの取得**
                  1. `get_export_status()` を呼び出し、現在のエクスポートステータスを取得する。  
                  2. ステータスが存在しない場合、 `get_export_url()` を呼び出して新しいステータスを取得する。  

              - **3.2 タスクの状態確認**
                  1. ステータスに `task_id` が含まれている場合、非同期タスクの状態を確認する。  
                  2. タスクの状態が **成功・失敗・キャンセル** のいずれかであれば、  
                  `delete_export_status()` を呼び出してステータスを削除し、新しいステータスを取得する。  
                  3. タスク結果が存在せず、stop_pointがredisに存在しない場合、ステータスに `export_fail` のエラーメッセージを追加する。  

              - **3.3 stop_pointの確認**
                  1. redisのキー`weko_authors_export_stop_point`の値(stop_point)が存在する場合、ステータスにstop_pointを追加する。

              - **3.4 ダウンロードリンクの設定**
                  1. `url_for('authors/export.download', _external=True)` を使用してダウンロードURLを設定する。  
                  2. ステータスに `file_uri` が含まれていない場合、ダウンロードURLを空とする。  
                  3. 最終的に、ステータスから `file_uri` を削除する。  

              - **3.5 フロントエンドへのレスポンス**
                  1. **ダウンロードURLとエラー情報**などのステータスをフロントエンドに返す。  
                      - stop_pointが在する場合、ボタンの表示を「Resume」に変える。
                      - ダウンロードURLが空の場合、フロントエンド側では何も処理を行わない。  
                      - ダウンロードURLが存在する場合、フロントエンドに表示する。 
                  

      2. **エクスポート処理の一時停止・再開・キャンセル機能**

          - 一時停止機能
              - 一時停止の条件  
                  - リトライ機能が最大回数を超えた場合  
              - 処理内容  
                  1. 処理途中のデータを破棄する。  
                  2. Redisの `weko_authors_export_stop_point` に以下を設定する。  
                      - **値:** 定数`WEKO_AUTHORS_EXPORT_BATCH_SIZE` の倍数で一時ファイルに書き込まれているレコード数  
                  3. Celeryタスクを停止・削除する。  
              - **エクスポートの制限**  
                  - `stop_point` が存在する間、新規エクスポートは不可とする。  
                  - フロントのExportボタンがResumeボタンに変わる。  

          -  再開機能
              - 再開の流れ 
                  1. **再開ボタン** 押下時に Redis から `stop_point` と `tmp_file_path` を取得する。  
                  2. `authors` テーブルの `id` カラム順に`stop_point`の行からデータ取得を再開する。  
                      - 処理再開時に Redis の `stop_point` を削除する。  
                  3. `tmp_file_path` のTSVファイルに続きのデータを書き込む。  

          - キャンセル機能
              - 一時停止時のキャンセルについて
                  - Redisの `weko_authors_export_stop_point`に値が存在する場合、以下の処理を行う。
                      - Redisの `weko_authors_export_stop_point`を削除する。
                      - Redisの `weko_authors_export_temp_file_path_key`から一時ファイルのパスを取得する。
                          - 一時ファイルのパスが存在すれば一時ファイルを削除する。
                          - キー`weko_authors_export_temp_file_path_key`の値は削除する。
                  
      3. **エラー時のリトライ機能**

          - リトライ対象のエラー
              - **以下のエラー発生時にリトライを行う**  
                  - `SQLAlchemyError`（接続エラー・タイムアウトエラー）  
                  - `RedisError`（接続エラー・タイムアウトエラー）  
                  - `TimeoutError`（システムタイムアウトエラー）  

          - リトライの設定
              - 最大リトライ回数: 定数`WEKO_AUTHORS_BULK_EXPORT_MAX_RETRY`（デフォルト: 5回）  
              - リトライ間隔: 定数`WEKO_AUTHORS_BULK_EXPORT_RETRY_INTERVAL`（デフォルト: 5秒）  

          - リトライの流れ
              1. エラーが発生した場合、リトライ処理を行う。  
              2. 最大リトライ回数を超えた場合、一時停止状態とする。
                  - Redisの `weko_authors_export_stop_point` に以下を設定する。  
                      - **値:** 定数`WEKO_AUTHORS_EXPORT_BATCH_SIZE` の倍数で一時ファイルに書き込まれているレコード数を記録する。   
                  - Celeryタスクを停止・削除する。  

          - その他のエラー発生時の処理
              - **リトライ対象外のエラー発生時**（例: データ整合性エラー、権限エラー など） 
                  - 発生したエラーに関わらず、以下のリソースを削除する。  
                      - 一時ファイル (weko_authors_export_temp_file_path_keyに保存されたパスのファイル) 

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
<td>
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