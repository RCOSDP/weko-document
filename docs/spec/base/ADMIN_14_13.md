### サイト情報

  - > 目的・用途

リポジトリ管理者として、サイトの情報を登録する機能である。また、サイト名は多言語対応できる

  - > 利用方法

【Administration＞設定（Setting）＞サイト情報（Site Info）】の順でSite Info画面へ遷移して利用する。

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

  - 【Admin \> Setting \> Site Info】：サイトの情報を登録する。
    
      - 登録項目は以下通りである。
        
          - 「サイト名」（Site Name）
            
              - サイト名称を入力するテキストエリア
            
              - デフォルト値は、「サイト名未設定」（Site name is not set）とする。
            
              - 「サイト名の追加」（Add site name）ボタン及び言語プルダウンを設ける。
                
                  - 「サイト名の追加」（Add site name）ボタンを押すと、「サイト名」および「言語」の入力欄を最下段に1行追加表示する。
                
                  - 言語プルダウンの選択肢は【Administration \>設定（ Setting）\> 言語表示（Language）】での「登録言語」に登録されている言語一覧とする。デフォルト値は「登録言語」の1番目の言語とする。
                
                  - 入力欄がシステム言語の数と同数になったら、このボタンは不活性とする。
                
                  - 同一言語に一つサイト名のみを設定できる。
        
          - 「ファビコン」（Favicon）
            
              - 「アイコンファイルの選択」（Select icon file）ボタンを設ける。
            
              - デフォルトは、JAIRO Cloudのアイコンを設定しておく。
            
              - 押下するとファイル選択ダイアログが表示される。
            
              - 選択ダイアログはアイコンファイルのみ選択可能とする。
            
              - ファイル選択が完了すると、ファイル名表示欄に選択ファイル名を、アイコンプレビュー表示欄にプレビューを表示する。
        
          - 「著作権」（CopyRight）
            
              - このサイトの著作権を設定する。ここで入力された項目は、htmlの\<head\>\<meta\>のname="copyright\>属性に出力する。
            
              - デフォルト：空白
        
          - 「記述」（Description）
            
              - このサイトの概要を設定する。ここで入力された項目は、htmlの\<head\>\<meta\>のname="Description"属性に出力する。
            
              - デフォルト：空白
        
          - 「キーワード」（Keyword）
            
              - このサイトの概要を設定する。ここで入力された項目は、htmlの\<head\>\<meta\>のname="keyword"属性に出力する
            
              - デフォルト：空白
        
          - 「トラッキングID」（Tracking ID）
            
              - Google AnalyticsのトラッキングIDを設定する。Admin画面で設定した値は GOOGLE\_TRACKING\_ID\_USER として admin\_setting テーブルに保存する。
            
              - デフォルト：空白
        
          - 「AddThis ID」（AddThis ID）
            
              - AddThisのトラッキングIDを設定する。Admin画面で設定した値は ADDTHIS\_USER\_ID として site\_infoテーブルに保存する。
            
              - デフォルト：ra-5d8af23e9a3a2633
        
          - 「OGPイメージ」（OGP Image）
            
              - og:imageへ設定するための画像アップロード機能を追加する。ファイル形式は JPG, PNG, WEBP, GIF フォーマット、ファイルサイズは 5MB 未満とする。  
                アップロードしたファイルの保存ディレクトリは Files \> Location で設定しているディレクトリに統一する。  
                本画面で設定した画像ファイルは、WEKO3のWeb画面のheadタブ内にあるmetaタグのcontentにファイルのフルパスで表示する。  
                ※OGP Imageに画像をアップロードしていない場合: content="" となる。
            
              - デフォルト：空白
    
      - 「保存」（Save）ボタンを押すと、
        
          - バリデーションを実施し、問題がなければデータベースに設定値を保存し、メッセージを画面の上部に表示する  
            メッセージ：  
            日本語：「サイト情報が正常に保存されました。」  
            英語：「Site info is saved successfully.」
        
          - データベースには、設定された値を記録する。
        
          - バリデーションエラーが発生したら、エラーダイアログを表示後、入力画面に戻る。
        
          - エラーダイアログにはバリデーションエラー内容を表示する。
    
      - バリデーション及びエラーメッセージ
        
          - サイト名が一つも設定されていないとき  
            エラーメッセージ：  
            日本語：「サイト名は少くとも１つ設定する必要があります。」  
            英語：「Must set at least 1 site name.」
        
          - サイト名を複数設定する際に、同一言語を選択したとき  
            エラーメッセージ：  
            日本語：「同一言語を複数のサイト名に設定されています。」  
            英語：「The same language is set for many site names.」
        
          - トリミングしたサイト名が空文字であるとき  
            エラーメッセージ：  
            日本語：「×サイト情報を空のフィールドに入力してください。」  
            英語：「Please input site information for empty field.」
        
          - 選択していた言語が登録言語から削除されたとき  
            エラーメッセージ：  
            日本語：「削除された言語は利用できません」  
            英語：「Language is deleted from Registered Language of system」
        
          - サイト名はトリミングした入力値を保存すること  
            ※サイト名をHTMLとして埋め込む際はエンコード処理を実施するなど配慮すること

  - 設定されたサイト名及びファビコン表示について
    
      - サイト名表示
        
          - 設定されたサイト名は、全ての画面で\<title\>タグの値に設定する。
        
          - \<title\>に設定する値は、システムの言語設定に合わせた言語のサイト名を表示する  
            なお、システム言語にマッチするサイト名が設定されていない場合は、英語、もしくは最上位の言語のサイト名を表示する。
    
      - ファビコン表示
        
          - 設定されたアイコンをシステムのfaviconとして設定する。

  - OGP対応
    
      - サイト情報をOGP(Open Graph protocol)で出力する。
    
      - meta要素としてog:titleを出力する。
    
      - meta要素としてog:urlを出力する。
    
      - meta要素としてog:imageを出力する。
    
      - meta要素としてog:descriptionを出力する。
    
      - meta要素としてog:localeを出力する。。値としてリポジトリサイトのデフォルトロケールを出力すること
    
      - meta要素としてog:locale:alternateを出力する。値としてリポジトリサイトが対応するデフォルト以外のロケールを出力すること

  - Admin/setting/site info の「サイト名」に入力された値をフィードバックメールの件名、本文内に反映する。
    
      - 日本語メールには日本語サイト名を、英語メールには英語サイト名をセットする。
    
      - 空欄のサイト名の場合は「No Site Name」と表示する。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-admin

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - > 登録するサイト情報を入力後に\[保存（Save）\]ボタン押下すると、weko\_admin.views.update\_site\_infoが呼び出され、その中でweko\_admin.utils.validation\_site\_infoを使用し、入力値のエラーチェックを行う。  
    > 入力値に問題がなければ、db内のsite\_infoテーブルに情報が保存される。

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



