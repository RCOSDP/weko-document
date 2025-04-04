### PDFカバーページ表示

  - > 目的・用途

本機能は、PDFカバーページについて設定する際に使用する機能である。

  - > 利用方法

【Administration \> 設定（Setting） \> PDFカバーページ表示（PDF Cover Page）画面】にて操作を行う。

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
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - インデックス全体のPDFカバーページについて設定する
    
      - 「PDF Cover Page」エリアにてPDFカバーページの有効/無効を設定する
        
          - 「ON/OFF」：利用可否設定
            
              - 「Enable」を選択する場合、PDFカバーページ機能を有効とする
            
              - 「Disable」を選択する場合、PDFカバーページ機能を無効とする（デフォルト）
    
      - 「Header Settings」エリアにてヘッダのカバーページを設定する
        
          - 「Header Display Setting」：ヘッダ表示設定
            
              - 「String」：文字列表示（デフォルト）
            
              - 「Image」：画像表示
        
          - 「Header Output String Setting」：ヘッダ出力文字列設定  
            ※文字列表示の場合に使用する。操作自体はヘッダ表示設定にかかわらず可能
            
              - 半角100文字/全角50文字以内の文字列を入力する
        
          - 「Header Output Image Setting」：ヘッダ出力画像設定  
            ※画像表示の場合に使用する。操作自体はヘッダ表示設定にかかわらず可能
            
              - jpg,png,gifが設定可能
                
                  - すべての種類のファイルが設定できるが、上記以外のファイルを選択するとPDFファイルのダウンロード時にサーバ内部エラーが発生する
            
              - ［ファイルを選択（Choose File）］ボタンを押してファイルを選択する
                
                  - 設定済みかどうかにかかわらず、画面表示後に選択されていない場合はボタンの右側に以下のメッセージが表示される  
                    メッセージ：  
                    日本語：「選択されていません」  
                    英語：「No file chosen」
            
              - ファイルが設定されていない状態では、［ファイルを選択（Choose File）］ボタン上部にメッセージが表示される  
                メッセージ：「No header image set」
            
              - 画像ファイルが設定済みの状態では、［ファイルを選択（Choose File）］ボタン上部にその画像が表示される
            
              - 画像ファイルが選択された状態では、［ファイルを選択（Choose File）］ボタン下部にその画像が表示される
        
          - 「Header Display Position Setting」：ヘッダ表示位置設定
            
              - 「Left justified」：右寄り
            
              - 「Center justified」：中央寄せ（デフォルト）
            
              - 「Right justified」：左寄せ

  - ［保存（Save）］ボタンを押すと、各エリアの設定値が保存される
    
      - 「Header Output Image Setting」でファイルを選択していた場合、ヘッダ出力画像は選択したものに置き換えられる

  - インデックスごとにカバーページの有効/無効を設定する
    
      - 詳細は[ADMIN-3-1: ツリー編集](#ツリー編集)参照

  - ここで設定したPDFカバーページ設定は、PDFファイルのダウンロード時に参照する
    
      - 画像表示の場合、カバーページでは高さが30mmかつ縦横比は元画像と同じになるように拡大、縮小して表示される
    
      - 目的のPDFファイルがパスワードによって暗号化されていた場合は、カバーページをつけずにダウンロードする
    
      - カバーページをつけたPDFファイルは、ファイル名を「CV\_yyyymmdd\_もともとのファイル名.pdf」となる

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_records\_ui

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 画面表示時に、pdfcoverpage\_setテーブルから「id」フィールドが「1」であるレコードを取得する
    
      - 取得できなかった場合は、以下の処理を行う
        
          - 各フィールドを以下のように設定してレコードを作成する
            
              - 「id」：自動採番
            
              - 「avail」：disable
            
              - 「header\_display\_type」：なし（テーブルのデフォルト値のstringが入る）
            
              - 「header\_output\_string」：なし
            
              - 「header\_output\_image」：なし
            
              - 「header\_display\_position」：なし（テーブルのデフォルト値のcenterが入る）
        
          - 作成後に再度「id」フィールドが「1」であるレコードを取得する
            
              - そこで取得できなかった場合は、サーバ内部エラーが発生する
    
      - 取得した情報を表示情報とする
        
          - 「header\_output\_image」フィールドの情報は、テンプレートのimg要素のソースとなる

  - ［保存（Save）］ボタンを押すと、pdfcoverpage\_setテーブルの「id」が「1」であるレコードを以下のように更新する
    
      - 「avail」：「ON/OFF」で選択したもの
    
      - 「header\_display\_type」：「Header Display Setting」で選択したもの
    
      - 「header\_output\_string」：「Header Output String Setting」の入力値
    
      - 「header\_output\_image」：以下の２通り
        
          - ファイルが選択されていなかった場合、そのまま
        
          - ファイルが選択されていた場合、システムにそのファイルを保存して、ファイルのパスを設定する
    
      - 「header\_display\_position」：「Header Display Position Setting」で選択したもの

  - 「Header Output Image Setting」でファイルを選択したとき、そのファイルをFileReader.readAsDataURLメソッドによってBase64でエンコードする
    
      - このメソッドは、テンプレートに記述されている
    
      - エンコードした文字列を、ボタン下部のimage要素のsrc属性に設定する
    
      - 大きなファイルをエンコードする場合は、エンコード後の文字列がjavascriptの変数に入りきらずにエラーとなることがある

  - ここで設定したPDFカバーページ設定は、PDFファイルのダウンロード時に参照する
    
      - weko\_records\_ui.fd.\_download\_file関数で条件を確認して、以下のいずれかの場合には、カバーページをつけずにダウンロードする
        
          - ファイルのmimetypeがPDFでない
        
          - pdfcoverpage\_setテーブルに「id」が「1」であるレコードが存在しない
        
          - レコードで「avail」がdisableである
        
          - 対象アイテムが属するインデックスで、PDFカバーページ設定が無効である
        
          - オリジナルのPDFファイルをダウンロードできる権限がある状態で、そうする操作である
    
      - そうでない場合は、 weko\_records\_ui.pdf.make\_combined\_pdf関数を呼び出してカバーページ付きのPDFファイルを作成して、そのファイルをダウンロードする
        
          - カバーページ付きのPDFファイルは、以下の場所に作成される
            
              - tempfile.gettempdir関数の返り値+「/comb\_pdfs/」

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
</tbody>
</table>
