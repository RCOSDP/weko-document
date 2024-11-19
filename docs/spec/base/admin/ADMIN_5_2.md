
### 一括出力

  - > 目的・用途

本機能は、著者DBの情報を一括出力する機能である。

  - > 利用方法

本画面にある \[エクスポート(Export)\] ボタンを押下することで、著者DBに登録されている著者情報をtsvファイルで出力する。

tsvファイルのダウンロードURLにアクセスすることでtsvファイルを取得することができる。

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

(1) 一括出力画面の画面構成

  - 【Administration \> 著者DB管理(Author Management) \> 一括出力(Export)】 を選択すると表示される。

  - 画面構成は以下の通り
    
      - 全件エクスポート(Export all creator)
    
      - ダウンロードURL(Download URL)

  - 全件エクスポート(Export all creator)
    
      - 全件エクスポートを実行する。以下の2種類のボタンがある。
        
          - \[エクスポート(Export)\] ボタン
            
              - ボタンを押下すると、以下のポップアップのメッセージとボタンが表示される
                
                  - 「著者DBの全件エクスポートを実行してよいですか？(Are you sure you want to export all creator?)」  
                    　　\[実行(Execute)\] ボタン：著者DBの全件エクスポートを実行し、自画面に戻る  
                    　　\[キャンセル(Cancel)\] ボタン：何も処理はせずに自画面に戻る
            
              - 著者DBの全件エクスポート実行中は、ボタンは非活性となる
        
        <!-- end list -->
        
          - \[キャンセル(Cancel)\] ボタン
            
              - 著者DBの全件エクスポートを中断する。エクスポート実行中以外は非活性である。

  - 著者DBの全件エクスポート実行中にボタンが活性化される。ボタンを押下すると、以下のポップアップのメッセージとボタンが表示される。  
    「メッセージ」  
    　日本語：著者DBの全件エクスポートの処理をキャンセルしてよいです　　か？  
    　英語：Are you sure you want to cancel process of exporting all creator?  
    「ボタン」  
    　\[実行(Execute)\] ボタン：著者DBの全件エクスポートを中断し、自画面に戻る。  
    　\[キャンセル(Cancel)\] ボタン：中断はせずに自画面に戻る(全件エクスポート処理を継続する)。ダウンロードURL(Download URL)
    
      - 全件エクスポートが完了すると、出力ファイル(tsv形式)をダウンロードできるURLが表示される
    
      - 最後に出力されたダウンロードURLが表示される（初期の全件エクスポート実行前は何も表示されない）
    
      - ダウンロードのURLの例(初期値)としては以下の通り（出力ファイル名はConfigで設定できるものとする）
        
          - 
(2) 出力ファイル

  - 全件エクスポートされたファイルはtsv形式で出力される。

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

  - 文字コードはUTF-8(BOM付き)，改行コードはCR+LFとする。

  - １行目はヘッダ行とし、システム管理するものである。先頭に"\#"が付いている。

  - ２行目と３行目はラベルを表示し、TSV入力の補助をする。先頭に"\#"が付いている。

  - ４行目以降に著者の情報を出力する。１著者の情報を1行で出力する。

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
<td>WEKO3の著者ID(author_link)を出力する</td>
</tr>
<tr class="even">
<td>2</td>
<td>authorNameInfo[0...n].familyName</td>
<td>姓[0...n]</td>
<td>Family Name[0...n]</td>
<td>著者の姓を出力する</td>
</tr>
<tr class="odd">
<td>3</td>
<td>authorNameInfo[0...n].firstName</td>
<td>名[0...n]</td>
<td>Given name[0...n]</td>
<td>著者の名を出力する</td>
</tr>
<tr class="even">
<td>4</td>
<td>authorNameInfo[0...n].language</td>
<td>言語[0...n]</td>
<td>Language[0...n]</td>
<td>著者の言語を出力する</td>
</tr>
<tr class="odd">
<td>5</td>
<td>authorNameInfo[0...n].nameFormat</td>
<td>フォーマット[0...n]</td>
<td>name Format[0...n]</td>
<td>著者の姓名のフォーマットを出力する<br />
※現状(SP67時点)は「familyNmAndNm」固定</td>
</tr>
<tr class="even">
<td>6</td>
<td>authorNameInfo[0...n].nameShowFlg</td>
<td><p>姓名・言語</p>
<p>表示／非表示[0...n]</p></td>
<td>Name Display[0...n]</td>
<td>著者の姓名と言語の表示／非表示を出力する<br />
表示する: "Y"<br />
表示しない: "N"</td>
</tr>
<tr class="odd">
<td>7</td>
<td>authorNameInfo[0...n].idType</td>
<td>外部著者ID 識別子[0...n]</td>
<td>Identifier Scheme[0...n]</td>
<td>外部著者IDの識別子を出力する</td>
</tr>
<tr class="even">
<td>8</td>
<td>authorNameInfo[0...n].authorId</td>
<td>外部著者ID URI[0...n]</td>
<td>Identifier URI[0...n]</td>
<td>外部著者IDの値を出力する</td>
</tr>
<tr class="odd">
<td>9</td>
<td>authorNameInfo[0...n].authorIdShowFlg</td>
<td><p>外部著者ID</p>
<p>表示／非表示[0...n]</p></td>
<td>Identifier Display[0...n]</td>
<td>外部著者IDの表示／非表示を出力する<br />
表示する: "Y"<br />
表示しない: "N"</td>
</tr>
<tr class="even">
<td>10</td>
<td>emailInfo[0...n].email</td>
<td>メールアドレス[0...n]</td>
<td>Mail Address[0...n]</td>
<td>著者のメールアドレスを出力する</td>
</tr>
<tr class="odd">
<td>11</td>
<td>is_deleted</td>
<td>削除フラグ</td>
<td>Delete Flag</td>
<td>著者を削除する場合に "D" と出力する<br />
※論理削除された著者情報は出力しないため、全件エクスポートではすべて空欄となる</td>
</tr>
</tbody>
</table>

　【補足】  
　　・同じ項目名を複数持つ場合は、各項目名の後ろに\[0\],\[1\],…,\[N\]と記載された状態で出力される。  
　　　※1つ目の項目名には \[0\] が記載されている。  
　　・WEKO ID, Delete Flagは繰り返し記載することはできない。

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

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-authors

<!-- end list -->

  - > 処理概要

> modules/weko-authors/weko\_authors/config.py

  - > 全件エクスポートのファイル名の設定値
    
      - > WEKO\_AUTHORS\_EXPORT\_FILE\_NAME = 'Creator\_export\_all.tsv'

> \[（Export）\]ボタンを押下すると、weko\_authors.admin.ExportView.exportが呼び出され、著者情報のファイルのURIのidをdb内のfilies\_filesテーブルのidカラムから取得する。（URIがない場合は、invenio\_files\_rest.models.FileInstance.createが呼び出され作成される。）  
> 次に、weko\_authors.admin.ExportView.check\_statusが呼び出され、Download URLが作成される。
> 
> Download URLを押下することで、weko\_authors.admin.ExportView.downloadが呼び出されてファイルがダウンロードされる。

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