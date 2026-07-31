# コンテンツファイル管理

## 目的・用途

本機能は、アイテムに登録されたファイルの情報を表示し、ファイルバージョンを管理する機能である。

## 利用方法

- アイテム詳細画面にファイル一覧を表示
- 【information】を押下してファイルの詳細情報の表示
- 【download】を押下してファイルのダウンロード
- 【Import to GakuNin RDM】を押下することでGakuNin RDMへファイルを取り込み

## 利用可能なロール

|ロール|システム管理者|リポジトリ管理者|コミュニティ管理者|登録ユーザ|一般ユーザ|ゲスト(未ログイン)|
|---|---|---|---|---|---|---|
|利用可否|○|○|○|○|○|○|

## 機能内容

### 1. ファイルの情報を表示する

  - 【アイテム詳細画面】の上端にファイルの情報を表示するアイテム登録時に選択された表示形式に応じてファイルの情報を以下のように表示する
    
      - 表示形式： **簡易表示（Simple）**
        
          - 登録されたファイル一覧を表示する。「Name/File (名前 / ファイル)」列にファイル名を表示し、ラベルが登録されている場合はファイル名の代わりにラベルが表示される。  
            コンテンツファイルが登録されていない場合は、「Name/File (名前 / ファイル)」列に本文URLが表示される。ラベルが登録されている場合は本文URLの代わりにラベルが表示される。
            
              - ファイル名リンク：コンテンツファイルをダウンロードする。  
                コンテンツファイルが登録されていない場合はリンク先のURLへ遷移する。
            
              - オープンアクセス指定日より前は「Download is available from YYYY/MM/DD.」と表示する。日付が一桁の場合、0埋め表示をしない。  
                ログインしているロールが該当登録者、管理者以外の場合は、公開されていないファイルを選択すると、「権限が必要です (Permission required)」と表示する。STATS_WEKO_DEFAULT_TIMEZONEに設定されたタイムゾーンに基づく時刻を表示する。
        
          - ファイルに対してのアクション
            
              - 【ダウンロード（Download）】：該当ファイルをダウンロードする。  
                コンテンツファイルが登録されていない場合はリンク先のURLへ遷移する。
            
              - 【Information】：該当ファイル詳細画面に移動する。
              - 【Import to GakuNin RDM】:GakuNin RDMへインポートする機能を提供する。
    
      - 表示形式： **詳細（Detail）**
        
          - 登録されたファイル一覧を表示する。「Name/File (名前 / ファイル)」列にファイル名を表示し、ラベルが登録されている場合はファイル名の代わりにラベルが表示される。  
            コンテンツファイルが登録されていない場合は、「Name/File (名前 / ファイル)」列に本文URLが表示される。ラベルが登録されている場合は本文URLの代わりにラベルが表示される。
            
              - ファイル名リンク：コンテンツファイルをダウンロードする。  
                コンテンツファイルが登録されていない場合はリンク先のURLへ遷移する。
            
              - オープンアクセス指定日より前は「「Download is available from YYYY/MM/DD.」と表示する。日付が一桁の場合、0埋め表示をしない。ログインしているロールが該当登録者、管理者以外の場合は、公開されていないファイルを選択すると、「権限が必要です (Permission required)」と表示する。
        
          - ファイルのライセンス
            
              - 「Write your own license」を選択した場合、テキストボックスに入力されたライセンス値を表示する。
            
              - 「Creative Commons」ライセンスから選択した場合、該当ライセンスアイコンを表示する。
                
                  - システムの表示言語が日本語の場合、ライセンスアイコンを押すと、日本語版のリンク先へ移動する。
                
                  - システムの表示言語が日本語以外の場合、ライセンスアイコンを押すと、英語版のリンク先へ移動する。
        
          - ファイルに対してのアクション
            
              - 【ダウンロード（Download）】：該当ファイルをダウンロードする。  
                コンテンツファイルが登録されていない場合はリンク先のURLへ遷移する。
            
              - 【Information】：該当ファイル詳細画面に移動する。
              - 【Import to GakuNin RDM】:GakuNin RDMへインポートする機能を提供する。
              
    
      - 表示形式： **プレビュー（Preview）**
        
          - ファイルのプレビューを表示する（プレビューの仕様について、「3-2.2 登録されたコンテンツファイル及び課金ファイルをプレビューできる」に参考する）
            
              - プレビューエリアを開閉する。
            
              - スライドナビゲーションで、プレビュー対象を切り替える。  
                コンテンツファイルが無い場合は表示形式をプレビュー (Preview)と選択してもプレビューエリアは表示しない。また、コンテンツファイルがない場合表示形式に関係なく、【プレビュー (Preview)】、【ダウンロード (Download)】ボタンを表示しない。  
                公開前のアイテムがある場合は「Cannot preview file」と表示する。  
                該当登録者、管理者以外で公開前のアイテムがある場合は「Restricted Access」と表示する。
        
          - ファイルサイズによりプレビューできない場合は、「Cannot preview file」の表示に、「 file size exceeded. 」が表示される。表示可能なファイルサイズの閾値は定数「WEKO_ITEMS_UI_FILE_SISE_PREVIEW_LIMIT」より設定できる。登録されたファイル一覧を表示する。
            
              - ファイル名リンク：コンテンツファイルをダウンロードする。  
                コンテンツファイルが登録されていない場合はリンク先のURLへ遷移する。
        
          - ファイルに対してのアクション
            
              - 【ダウンロード（Download）】：該当ファイルをダウンロードする。  
                コンテンツファイルが登録されていない場合はリンク先のURLへ遷移する。
            
              - 【Information】：該当ファイル詳細画面に移動する。
            
              - 【プレビュー（Preview）】：該当ファイルのプレビューをプレビューエリアに表示する。
            　- 【Import to GakuNin RDM】:GakuNin RDMへインポートする機能を提供する。


### 2. 登録されたコンテンツファイル及び課金ファイルをプレビューできる。

  - ファイルを登録する時、アイテム登録画面での表示形式を「プレビュー(Preview)」を選択すると、アイテム詳細画面に登録されたファイルをプレビューできる。

  - invenio-previewerが提供するすべてのファイルプレビューを利用できる。

  - 対応しているファイルタイプ：
    
      - Markdown
    
      - JSON/XML
    
      - CSV
    
      - PDF
    
      - Simple Images(PNG、JPG、GIF)
    
      - Zip
    
      - Jupiter Notebook(.jpynbファイル)
    
      - MS Office
    
      - 動画、音声(MP3、MP4、WEBM、OGG、WAV)

  - 複数ファイルを登録する場合、ファイルをスライド表示でプレビューできる。
    
      - プレビューエリアにスライドナビゲーションを表示する。
        
          - プレビュー切替はコンテンツファイル一覧の並びに依存する。
        
          - スライドナビゲーションにて、先頭（|<）/前（＜）/次（＞）/末尾（>|）のスライドへ移動できる。

  - PDF形式のファイルに対して、PDFにはカバーページが付与される場合、PDFカバーページはコンテンツファイルの1ページ目に付与し、コンテンツファイルの中身と合わせてカバーページをプレビューに表示する

  - PDF形式のファイルのプレビューは、拡大率やページ数を変更する機能のあるツールバーに囲われた状態で表示される。

  - ファイルプレビューエリアを開閉できる

  - プレビューエリアでの上部に「プレビュー」リンクをクリックすると、ファイルプレビューエリアを開閉する。

  - 表示形式をプレビューとしたJPEGファイルは、ファイルバージョンの管理を行う。

### 3. コンテンツファイル及び課金ファイルにアクセス制限がかけられている。

  - アクセス制限の内容を「5.2. 実装方法」での「(1)アイテム詳細画面に表示、ダウンロードする処理」を参照する。

### 4. コンテンツファイルごとに更新履歴を表示する。

  - アイテム詳細画面の各ファイルの表示の【Information】ボタンを押すと、該当ファイル詳細画面に移動する。
    
      - アイテム詳細画面と同様にファイルのプレビューを表示する
    
      - ファイル情報の属性情報を表形式で表示する。アイテム登録／編集時に登録していない属性情報は表示されない
        
          - 公開日：　{YYYY}-{MM}-{DD} 形式　(※公開日は必須のため必ず表示される)。エンバーゴが指定されている場合は、エンバーゴ日。オープンアクセスの場合はアイテム公開日を表示する。
        
          - 表示名(FileName)：　ファイル情報の表示名
        
          - 本文URL(Text URL)：　{protocol}://{host}/records/{id}/files/{ファイル名} 形式
        
          - ラベル(Label)：　ファイル情報で入力したラベル名
        
          - オブジェクトタイプ(Object Type)：　ファイル情報で選択したオブジェクトタイプ
        
          - フォーマット(Format)：　システムが出力したフォーマットの値
        
          - サイズ(Size)：　システムが出力したサイズ、または手入力したサイズ（複数入力可能）
        
          - 日付タイプ(Date Type)：　ファイル情報で選択した日付タイプ（複数入力可能）
        
          - 日付(Date)：　{YYYY}-{MM}-{DD} 形式（複数入力可能）
        
          - バージョン情報(Version Information)：　アイテム登録／編集時に入力した値
    
      - ファイル詳細画面では、アイテム詳細画面のファイル情報に加えて、「バージョン」タブに更新履歴情報を表示する。  
        更新履歴の表示項目は、以下とする。

| # | 表示項目 | 説明 | 備考 |
| --- | --- | --- | --- |
| 1 | バージョン（Version） | ファイルのバージョンを表示する<br>最新バージョンはCurrentと表示する | コンテンツファイルが削除された場合は該当バージョンを論理削除する |
| 2 | 更新日時（Date Modified） | コンテンツファイルの登録日時 | ISO8601のTZ付き形式とする<br>形式：「YYYY-MM-DD hh:mm:ss」 |
| 3 | オブジェクトファイル名（Object File Name） | コンテンツファイルにアクセス可能なリンクになっている<br>※ファイルサイズが大きい場合はマルチパートダウンロードのURLへ差し替えとなる。 マルチパートダウンロードの詳細は、[アイテム詳細]>[コンテンツファイル管理]>[ マルチパートダウンロード処理について]を参照 | /api/files/BUCKET_ID/FileName |
| 4 | ファイル容量（File Size） | ファイル容量をバイト表示する |  |
| 5 | ファイルハッシュ値（File Hash Value） |  | sha256ハッシュ値 |
| 6 | 投稿者名（Contributor Name） | ファイルを登録したユーザ名 | ゲストユーザの場合は非表示とする |
| 7 | 表示/非表示（Show/Hide） | 本項目は管理者またはアイテム登録者のみ表示される<br>本項目を最新バージョンの行に表示しない<br>また、"表示"に設定した場合、該当行が全ユーザに表示される |  |

  - 該当アイテムが非公開と設定すれば、
    
      - 該当登録者、管理者以外の場合、ファイル詳細画面に移動せずに、「権限が必要です (Permission required)」を表示する
    
      - ゲストユーザの場合、ログインをリクエストする

  - ファイル詳細画面が既に表示される場合、ファイルが「公開しない」（Do not publish）と変更すれば、ファイル詳細画面をリロードする。  
    該当登録者、管理者以外（ゲストユーザーを含む）に対して、「アクセス制限」のエラーメッセージをプレビューエリアに表示する

  - ファイル情報エリアの表示／非表示は、以下の図の After の表に従って表示制御する  
    別紙「変更前後のマトリクス.png」を参照。
    
      - ※１　オープンアクセス指定日より前は「YYYY年MM月DD日からダウンロード可能です」とファイル情報エリアのName/File欄に表示する
    
      - ※２　登録ユーザ権限以下のユーザがログインした状態で、ファイル情報エリアのダウンロードボタン、プレビューボタンを押下した際、「権限が必要です (Permission required)」と表示する
    
      - ※３　「ログインユーザーのみ」の場合、「アクセス制限」（英「Restricted Access」）と表示する

  - コンテンツファイル登録時にオープンアクセス日を未来日に指定し、指定日より前に表示した場合、以下のメッセージをファイル情報エリアのName/File欄に表示する。オープンアクセス日はローカル時間で表示される。  
    (日)「YYYY年MM月DD日からダウンロード可能です」  
    (英)「Download is available from YYYY/MM/DD.」

  - ファイルのリンク、[ダウンロード(Download)]ボタン、[プレビュー(Preview)]ボタンを押下すると、ログイン画面を表示する（Shibboleth連携の場合はShibbolethログイン画面を表示する）
    
      - ログイン認証時、権限のチェックを行う。
        
          - ログインユーザーロール（上記マトリクス※2）の場合
            
              - ログイン認証後、以下のメッセージをポップアップ表示する。  
                (日)「YYYY年MM月DD日からダウンロード/プレビュー可能です」  
                (英)「Download / Preview is available from YYYY/MM/DD.」
            
              - 既にログインしている状態で、ファイル情報エリアのダウンロードボタンもしくはプレビューボタンを押下した際、上記メッセージを表示する
        
          - 登録ユーザーロール以上の権限の場合(登録ユーザ、リポジトリ管理者、コミュニティ管理者、システム管理者)
            
              - ログイン認証後、ファイルのダウンロード/プレビューが行える

  - ゲスト(非ログイン)ユーザが参照する場合、ファイル情報エリアを表示し、以下のメッセージをファイル情報エリアのName/File欄に表示する  
    (日)「アクセス制限」  
    (英)「Restricted Access」

  - ゲスト(非ログイン)ユーザがログイン認証後は、アイテム詳細表示画面に遷移する

  - アイテム詳細画面の各ファイルの「Actions」表示欄に「申請」ボタンを表示する。「申請」ボタンを押すと、アイテム登録時に指定した提供方法に応じたワークフローが起動すること
    
      - 提供方法に一致しないユーザが「申請」ボタンを押下した場合はモーダルで警告メッセージを表示する
    
      - 起動したワークフローが「作業済(Done)」になった際、ワークフローを起動したユーザにファイルのダウンロードリンクをメールで送信すること

### 5. コンテンツファイルのアクセス制御

コンテンツファイルが「未来日」・「ログインユーザのみ」・「公開しない」設定であり、インデックス条件が、アイテムが所属するインデックスとその上位のインデックスが「公開」設定(未来日では無い)の場合、以下のようにアクセス制御を行う

  - Guest
    
      - 【ダウンロード (Download)】押下：　ログイン要求をする
    
      - DLのURLを入力：　ログイン要求をする  
        ※入力するURLは登録者(Contributor)以上がボタンを押下したときのURL( } )とする
    
      - ログイン要求でログインしたあと、ロールの種類に応じて画面遷移する
        
          - 登録者以外(ログインユーザ)：　"Permission required"を表示
        
          - 登録者以上：　DL可能
    
      - Informatonボタン押下：　ログイン要求をする
    
      - Informaton画面のURLを入力：　ログイン要求をする
    
      - ログイン要求でログインしたあと、ロールの種類に応じて画面遷移する
        
          - 登録者以外(ログインユーザ)：　"Permission required"を表示
        
          - 登録者以上：Information画面を表示

  - Authenticated User
    
      - 【ダウンロード (Download)】ボタン押下：　"Permission required"を表示する
    
      - DLのURLを入力：　"Permission required"を表示する  
        ※入力するURLは登録者(Contributor)以上がボタンを押下したときのURL( } )とする
    
      - 【Informaton】押下：　"Permission required"を表示する
    
      - 「Informaton」画面のURLを入力：　"Permission required"を表示する

  - 「制限公開」設定のファイルについては、下記条件の場合、DLボタンの代わりにApply（申請）ボタンが表示される。
    
      - 1.対象のコンテンツ（＝ファイル）のアクセスロールが「制限公開」（open_restricted）である。
    
      - 2.該当コンテンツをダウンロードする権限が、画面表示しているユーザ（未ログイン含む）に無い。

      - 3.WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True である。
    
      - 　※アイテム登録者やリポジトリ管理者のみならず、申請によって権限を得ているログインユーザもダウンロード権限があるとみなす。
        
          - Applyボタン押下の処理は、本書「実装方法」の「ダウンロード処理について」にある、「アクセスが「制限公開」（Restricted Access）と設定されているコンテンツに対して」の説明を参照
    
      - Information画面にて、「シークレットURLボタン」が表示される。
        
          - 下記をすべて満たす場合表示
            
              - 1.アイテム登録者・代理投稿者、またはリポジトリ管理者・システム管理者である。
            
              - 2.管理画面の制限公開画面にて、シークレットURLの表示が有効である。
            
              - 3.ファイルが「公開しない」である。または、ファイルが「オープンアクセス日を指定する」かつ指定日が未来日である（WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が False の際の「制限公開」は対象外）。
        
          - シークレットURLボタンを押下すると、URL編集エリアを表示する。URL表示エリアには以下の項目があり、保存されるURLの項目を編集できる

              - 1.リンク名を入力する項目

                  - 最大文字数：50文字

                  - 最小文字数：1文字

                  - 50文字まで入力を受け付ける

              - 2.発行されるシークレットURLの使用期限を設定する項目

                  - 初期値は管理者画面で設定される「有効期限日数」の値

                  - 最大値は管理者画面で設定される「有効期限日数上限」の値

                  - カレンダーから日付を選択

                  - フィールド下部に「有効期限日数上限」の上限日が表示される。

              - 3.配布されたシークレットURLの使用回数を設定する項目

                  - 初期値は管理者画面で設定される「ダウンロード回数」の値

                  - 最大値は管理者画面で設定される「ダウンロード回数上限」の値

                  - 数字でのみ入力が可能。管理者画面で設定される「ダウンロード回数上限」以上の入力は受け付けない

                  - フィールド下部に「ダウンロード回数上限」の上限値が表示される

              - 4.メール通知の無効化を設定できるチェックボックス

                  - デフォルトでチェック状態

              - 5.シークレットURLを発行するボタン

          - 「リンク名項目」「使用回数項目」の二つの項目は未入力の場合以下のメッセージが表示される

              - 日本語：「項目が未入力です」

              - 英語：「Item has not been filled in.」

            シークレットURLはURLを知っていれば誰でも対象のコンテンツファイルをダウンロードできるURL。（有効期限とダウンロード回数の制限を設定可能）作成されたシークレットURLはテーブルfile_secret_downloadに保存される。

      - Informamation画面にて、アイテムにおいて発行したシークレットURLの一覧を表示する

          - 下記を全てを満たす場合表示

              - 1.アイテム登録者・代理投稿者およびリポジトリ管理者・システム管理者である

              - 2.該当アイテムのシークレットURLが発行されていること

          - 発行済みのシークレットURLの以下の項目を表示する

              - 1.URL発行時に設定したリンク名

              - 2.URLを発行した日付

              - 3.URL発行時に設定したURLの有効期限

              - 4.URL発行時に設定したダウンロード回数制限

              - 5.URLの削除ボタン

              - 6.URLのコピーボタン

          - 削除ボタンを押下すると、該当URLの論理削除フラグがチェックされ、非表示状態になる

          - コピーボタンを押下すると、該当URLをクリップボードにコピーする

### 6. 「Import to GakuNin RDM」機能

この機能は、WEKO3で公開されているGakuNin RDMプロジェクトアーカイブを、GakuNin RDMに新しいプロジェクトとしてインポートするためのものです。GakuNin RDMプロジェクトアーカイブはGakuNin RDM上でプロジェクトをエクスポートすることで作成されます。

**主な動作と条件**

- ボタンの表示条件: ファイルのMIME TYPEが application/rdm-project である場合にのみ、アクションボタンとして「Import to GakuNin RDM」が表示されます。

- ボタンの活性条件: インポート対象のファイルが公開状態である必要があります。ファイルが非公開の場合、ボタンは表示されますが**非活性（押せない状態）**になります。

- インポート処理: ユーザーが「Import to GakuNin RDM」ボタンを押すと、GakuNin RDMへ移動します。インポートが完了すると、アーカイブが展開され、GakuNin RDM上に新たなプロジェクトとして登録されます。

- URL設定: ボタンを押した後の遷移先となるGakuNin RDMのURLは、設定項目 WEKO_RECORDS_UI_GAKUNIN_RDM_URL で変更することが可能です。


## 関連モジュール

  - weko-records-ui

## 処理概要

### 1. 設定

#### FILES_REST_DEFAULT_PDF_SAVE_PATH

  - ファイルをプレビュー表示するため、ファイルからPDF形式に変換し、テンポラリーフォルダーに書き込む処理を行う

  - テンポラリーフォルダーの初期値は「/var/tmp」であり、以下のConfigファイルで設定できる  
    <https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/invenio-files-rest/invenio_files_rest/config.py#L132>
    
      - 設定キー：「FILES_REST_DEFAULT_PDF_SAVE_PATH」
    
      - 現在の設定値：FILES_REST_DEFAULT_PDF_SAVE_PATH = tempfile.gettempdir()

  - 予期せぬエラーによりファイルをテンポラリーフォルダーに書き込むことができない場合、以下のメッセージがプレビュー画面に表示される  
    メッセージ：「Unexpected server response (502) while retrieving PDF + ファイルパス」

#### WEKO_RECORDS_UI_GAKUNIN_RDM_URL

【Import to GakuNin RDM】ボタンを押下したときに、アクセスするGakuNin RDMのURLを指定する。

- 設定キー：WEKO_RECORDS_UI_GAKUNIN_RDM_URL
- 現在の設定値："https://rdm.nii.ac.jp"

指定されたGakuNin RDMはボタン押下後、WEKO3からファイルをダウンロードする。

### 2. 実装方法

  - ファイルビューアのライブラリ：pdfjs-dist (ver. 1.4.192)

  - weko_records_ui.permissions.check_file_download_permissionを使用する。

#### (1)アイテム詳細画面に表示、ダウンロードする処理

  - ファイル情報の表示処理について  
    アクセスしているユーザーの権限が管理者であるかどうか、weko_records_ui.permissions.check_file_download_permissionにて「WEKO_PERMISSION_SUPER_ROLE_USER」を使用する
    
      - 権限が管理者の場合、アイテムに登録されるファイルの表示形式に応じてファイルの情報を取得し、表示する
    
      - 権限が管理者ではない場合、ユーザーの権限及びアクセス権限をチェックする
        
          - コンテンツファイルに対して
            
              - コンテンツのアクセスが「オープンアクセス」とした場合、ファイルの情報を取得し、表示する
            
              - コンテンツのアクセスが「オープンアクセス日を指定する」とした場合、以下のように制限する
                
                  - オープンアクセス日が経過していない場合、管理者または登録者、または設定されているグループに所属するユーザーには該当コンテンツファイルを表示、ダウンロードできる
                
                  - オープンアクセス日が経過していない場合、権限がないユーザーには該当コンテンツファイルを表示しない  
                    　 ⇒権限が無いユーザーには「Download is available from YYYY/MM/DD.」と表示する
                
                  - オープンアクセス日が経過した場合、すべてのユーザーは該当コンテンツファイルを表示、ダウンロードができる
            
              - コンテンツのアクセスが「ログインユーザのみ」とした場合、以下のように制限する
                
                  - weko_records_ui.permissions.check_file_download_permissionでcheck_user_group_permissionを呼び出して使用する。
                
                  - 設定されているグループに所属するユーザーには該当コンテンツファイルを表示する
                
                  - 設定されているグループに所属しないユーザーには、該当コンテンツファイルを表示しない
            
              - コンテンツのアクセスが「公開しない」とした場合、以下のように制限する
                
                  - weko_records_ui.permissions.check_file_download_permissionでcheck_user_permissionを呼び出して使用する。
                
                  - 管理者またはアイテム登録者には該当コンテンツファイルを表示する
                
                  - 権限がないユーザーには該当コンテンツファイルを表示しない
            
              - コンテンツのアクセスが「制限公開」とした場合、以下のように制限する
              
                  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が False の場合は「公開しない」と同様の制限を行う

                  - 管理者またはアイテム登録者には該当コンテンツファイルを表示する
                
                  - 権限がないユーザーには、「アクセス制限（Restricted Access）」と表示する
                    
                      - 「Actions」に、ダウンロードボタンのかわりに、「申請」（Apply）ボタンを表示する
        
          - 課金ファイルに対して
            
              - コンテンツのアクセスを「オープンアクセス」とした場合、ファイルの情報を表示する
            
              - コンテンツのアクセスを「オープンアクセス日を指定する」とした場合、以下のように制限する  
                ・オープンアクセス日が経過していない場合、該当コンテンツファイルを表示する  
                ・オープンアクセス日が経過した場合、該当コンテンツファイルを表示しない
            
              - コンテンツのアクセスが「ログインユーザのみ」とした場合、  
                ・設定されているグループに所属するユーザーには該当コンテンツファイルを表示する  
                ・設定されているグループに所属しないユーザーには、該当コンテンツファイルを表示しない
            
              - コンテンツのアクセスが「公開しない」とした場合、ファイルの情報を表示しない

  - ダウンロード処理について
    
      - コンテンツファイルに対して  
        アイテム詳細画面に表示している、かつログインしている場合、ダウンロードできる
    
      - 課金ファイルに対して
        
          - コンテンツのアクセスが「オープンアクセス」とした場合、ファイルの情報を取得し、ダウンロードできる
        
          - コンテンツのアクセスが「オープンアクセス」以外とした場合、ファイルの情報を取得し、追加で以下の制限を実施する
            
              - 価格が設定されていないグループのユーザーは課金ファイルをダウンロードできない
                
                  - アイテム詳細画面及び課金ファイルのリンクを押下したときに、ダウンロード可能かを判断する  
                    ・ゲストユーザの場合：ログイン画面に遷移する  
                    ・設定されていないグループの場合：「本ファイルの参照権限がないためダウンロードできません。」とポップアップでエラーメッセージを表示する  
                    ・設定されているグループの場合：「本ファイルは課金ファイルです。 （価格：XXXXX）。 ダウンロードしますか。」とポップアップで確認メッセージを表示する  
                    　はい：ファイルをダウンロードする  
                    　いいえ：ファイルをダウンロードせず、自画面に戻る
            
              - 複数のグループに所属するユーザーには該当する価格の最低値が適用される
                
                  - アイテム詳細画面及びファイル詳細画面のコンテンツファイルのリンクを押下したときに、ユーザが所属しているグループを確認する  
                    対象のユーザが複数のグループに所属していた場合は、各グループで設定している課金ファイルの価格のうち、最低値のものを採用する
    
      - アクセスが「制限公開」（Restricted Access）と設定されているコンテンツに対して

          - weko_records_ui.permissions.check_file_download_permissionでcheck_open_restricted_permissionを呼び出して使用する。
           
          - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が False の場合は「公開しない」と同様の制限となる

          - 管理者またはアイテム登録者本人は常時ダウンロード可

          - その他のユーザーには、ダウンロードボタンではなく「利用申請」ボタンが表示される

          - その他のユーザーがファイルをダウンロードする場合、上記ボタンから利用申請を行い、管理者による承認を受けなければならない

              - アイテム登録・編集画面内で、制限公開用のコンテンツファイルの「提供方法」を編集することで、どのロールのユーザーに対して利用申請を許可するかを選択できる

                  - 上記で設定された条件に合致しないユーザが「申請」ボタンを押下した場合はモーダルで警告メッセージを表示する

                      - 日本語：「このデータは利用できません（権限がないため）。」

                      - 英語：「This data is not available for this user.」

                  - 上記で設定された条件に合致するユーザーがアイテム詳細画面の【申請 (Apply)」ボタンを押下した際に利用申請設定時に設定されている利用規約をモーダル画面に表示する

                      - 利用規約について

                          - 利用規約文表示エリア上部に「利用規約 (Terms and Conditions)」を固定で表示する

                          - 利用規約文表示エリア下部に「利用規約を確認の上、スクロール最下部にある「利用規約に同意する」にチェックを入れてください (I have read and agreed to the Terms and conditions)」を固定で表示する

                          - 「利用規約に同意する」ラベルクリック時もチェックボックスのオンオフができるようにする

                          - 利用規約を最後まで確認すると「利用規約に同意する」チェックボックスをチェックできる。チェック前は「次へ」ボタンを非活性とする

                      - 利用規約画面での「次へ」ボタンを押下する挙動について

                          - 「 提供方法：ロール (Providing Method: Role)」が「Guest（非ログインユーザ）」で設定される場合、メールアドレスが入力できるモーダル画面が表示される。メールアドレスを入力し「Enable」ボタンを押下するとメールが送付される。

                              - 受信したメール文のリンクをクリックするとワークフローに定義されているアクション画面（アイテム登録画面など）に遷移する

                              - リンクはランダムなURLとトークン値から構成し、両者が一致した場合に利用登録ワークフローへのリンクとして機能する

                          - 「Contributor」等の任意のロールが「提供方法：ワークフロー (Providing Method: WorkFlow)」で設定される場合、指定されたワークフローの画面に遷移する

              - 利用申請が管理者によって承認された場合、対象ファイルをダウンロードできる一時的なURL(以下、ワンタイムURL)が発行される

                  - ワンタイムURLはメール送信によって利用申請者に通達される

                  - ワンタイムURLの有効期限及びダウンロード回数上限は、【Administration > 設定 (Setting) > 制限公開 (Restricted Access)画面】での「コンテンツファイルのダウンロード」(Content File Download)エリアで設定される

                  - 作成されたワンタイムURLはテーブルfile_onetime_downloadに保存される

　　　　　　　　　　- ワンタイムURLは以下のロジックにより生成される

                      - 「シークレットキー」「URL発行日」「URLのID」「アイテムID」「ファイル名」「有効期限」「ダウンロード上限回数」を足し合わせたバイト列から、SHA-256アルゴリズムでハッシュ値を作成

                      - 上記「ハッシュ値」と「デリミタ(アンダースコア)」,「URLのID」を連結しbase64形式でエンコードし、これをトークンとする

                  - アイテム登録者と管理者には、ファイルのInformamation画面に現在「有効」であるワンタイムURLの一覧が表示される

                      - 以下の要件をすべて満たす場合、そのURLは「有効」であると見なされる

                          - ダウンロードされた回数が、指定されたダウンロード回数上限に満たない

                          - 有効期限内である

                          - 削除フラグが無効である

                      - ワンタイムURL一覧表には以下の項目が表示される

                          - 1.URL利用者(=利用申請を行ったユーザー)のメールアドレス

                          - 2.URLが発行された日付

                          - 3.URLの有効期限

                          - 4.ダウンロード回数制限

                          - 5.URLの削除ボタン

                          - 6.URLのコピーボタン

                              - 削除ボタンを押下すると、該当URLの論理削除フラグがチェックされ、非表示状態になる

                              - コピーボタンを押下すると、該当URLをクリップボードにコピーする

              - 有効なワンタイムURLにアクセスした場合、コンテンツファイルがダウンロードできる。

                  - 有効期限を超過している場合、エラーメッセージが表示される

                      - 日本語：「ダウンロード有効期限を超過しています。」

                      -  英語：「 The expiration date for download has been exceeded. 」

                  - ダウンロード回数を超過している場合、エラーメッセージが表示される

                      - 日本語：「ダウンロード上限回数を超過しています。」

                      - 英語：「 The download limit has been exceeded. 」

                  - 論理削除フラグが立っている場合、エラーメッセージが表示される

                      - 日本語：「このURLは削除されました。」

                      - 英語：「 This URL has been deactivated. 」

              - 利用申請を承認されたユーザーには、申請ボタンではなくダウンロードボタンが表示されるようになる

                  - 発行されたワンタイムURLが失効した場合、申請ボタンに戻る

                  - 申請ボタンからダウンロードボタンになるのは、そのアイテムの制限公開のコンテンツファイルすべて（承認が行われた時点でのすべて）である。

                      - ひとつの制限公開ファイルに対して利用申請が行われ、それが承認された場合、同アイテムに含まれるすべての制限公開ファイルに対するURLがそれぞれ発行される

                      - 利用申請後にダウンロードボタンを使用する場合、ワンタイムURLへリダイレクトが行われるため、リンクに直接アクセスする場合と内部の処理は同様である

              - 各ワンタイムURLの初回利用時、ユーザーのアカウントに応じた利用報告ワークフローのリンクが利用者にメールで通知される

                  - ゲストユーザの利用報告ワークフローに対して、
                    リンクの有効期限は【Administration > Setting > Restricted Access画面】での「利用報告ワークフローへのアクセス」(Usage Report Workflow Access)エリアで設定される

                      - 設定された有効期限を超過した場合、対象の利用報告ワークフローのステータスを「キャンセル」に自動で更新する

                      - 設定された有効期限を超過したリンクにアクセスした場合は、エラーページを表示する

                          - weko_workflow.utils.validate_guest_activity_expiredを使用する。

                          - 日本語：「指定したリンクはアクセス有効期限を超過しています。 」

                          - 英語：「The specified link has expired.」
<!-- 
              - シークレットURLを使用しダウンロードした場合運用側で以下の内容を取得しログをテーブルfile_url_download_logにレコードを作成、査読者を追跡できる

                  - 「作成日時」

                  - 「更新日時」

                  - 「識別子」

                  - 「URL種別」

                  - 「シークレットURLID」

                  - 「IPアドレス」

                  - 「ファイルのアクセス形態」

                  - 「URLトークン」 -->

  - シークレットURLについて

      - シークレットURLへアクセスしたとき、URL論理削除フラグが立っておらず、またURLの有効期限とダウンロード回数が超えない場合、コンテンツファイルがダウンロードされる

          - 有効期限を超過している場合、エラーメッセージが表示される

              - 日本語：「ダウンロード有効期限を超過しています。」

              - 英語：「 The expiration date for download has been exceeded. 」

          - ダウンロード回数を超過している場合、エラーメッセージが表示される

              - 日本語：「ダウンロード上限回数を超過しています。」

              - 英語：「 The download limit has been exceeded. 」

          - URL論理削除フラグが立っている場合

              - 日本語：「このURLは削除されました。」

              - 英語：「This URL has been deactivated.」

      - 有効期限とダウンロード回数は、URLごとに管理される。（制限公開の有効期限・ダウンロード回数とは別管理となる）

      - シークレットURLは以下のロジックにより生成される

          - 「シークレットキー」「URL発行日」「URLのID」「アイテムID」「ファイル名」「有効期限」「ダウンロード上限回数」を足し合わせたバイト列から、SHA-256アルゴリズムでハッシュ値を作成

          - 上記「ハッシュ値」と「デリミタ(アンダースコア)」,「URLのID」を連結しbase64形式でエンコードし、これをトークンとする

      - ダウンロード時は上記トークンをbase64形式でデコードし、取得されたURLのIDから再度ハッシュ値を生成し、両者の値を比較検証する

      - 上記の仕様によりURL情報を格納するテーブルのスキーマに変更が生じた場合は全シークレットURLが無効となるため、各URLに対して再発行を行う必要がある

  - 「PDFカバーページ」処理について
    
      - ファイルのプレビュー及びファイルダウンロードにて、「PDFカバーページ」処理を実施する
    
      - weko_records_ui.admin.PdfCoverPageSettingView.indexを使用する。
    
      - 以下の条件を満たす場合、PDFカバーページを作成する
        
          - ファイルのプレビューの権限がある
        
          - 【Administration > Setting > PDF Cover Page】及び【Administration > インデックスツリー管理 (Index Tree) > ツリー編集 (Edit Tree)】でPDFカバーページの設定が有効になっている
        
          - 対象ファイルの形式は「PDF」形式である
        
          - 対象ファイルがパスワード付かない

  - プレビュー表示処理について
    
      - コンテンツファイルが「preview」の場合、詳細画面にプレビューを表示する。  
        weko_records_ui.utils.get_file_info_listを使用する

#### (2) ファイル詳細画面に表示、ダウンロードする処理

  - 表示処理について
    
      - 該当アイテムが公開しているかどうか、チェックする
        
          - 該当アイテムが非公開である場合
            
              - ゲストユーザに対してログインリクエストとする
            
              - 該当登録者、管理者の場合、ファイルの情報（バージョン情報を含む）を取得し、表示する
            
              - 他の権限に対して、「権限が必要です」のエラーメッセージを表示する
        
          - 該当アイテムが公開している場合  
            (1)での「ファイル情報の表示処理について」のようにチェックする
    
      - 権限があるユーザには、該当するファイル詳細画面に表示する
    
      - 権限がないユーザには、「アクセス権限」のエラーメッセージを表示する

  - プレビュー表示処理について(1)での「プレビュー表示処理について」のようにチェックする

  - ダウンロード処理について  
    (1)での「ダウンロード処理について」のようにチェックする

#### (3)ファイルバージョンの情報をweko_records_ui.view.default_view_methodで取得し、更新履歴情報を表示する

  - データベースから該当ファイルの情報を以下のように取得する
    
      - 更新日時：files_object.updated
    
      - オブジェクトファイル名：files_objectkey
    
      - ファイル容量：files_files.size
    
      - ファイルハッシュ値：files_files.checksum
    
      - 投稿者名：userprofiles_userprofile.username
    
      - 表示/非表示：files_object.is_show

【補足】

  - ファイルプレビューのビューアは、ファイルのアクセス権限と同様。  
    ファイルのアクセス権限がないユーザーは、ファイルプレビュー及びファイルの情報を見ることはできない

#### (4)マルチパートダウンロード処理について
  
  - ファイルダウンロードの際にテーブルfile_url_download_logにレコードを作成し、査読者を追跡できる。ログは以下のように情報を記録する。

    - 作成日時：ダウンロード日時
    - 更新日時：作成日時と同値。原則作成日時と別の値にはならない
    - 識別子：自動生成の連番
    - URL種別：2つの値のうち1つを取る列挙型。シークレットURLの場合「secret」、ワンタイムURLの場合は「onetime」という値を取る
    - シークレットURL ID：種別が「onetime」の場合null
    - ワンタイムURL ID：種別が「secret」の場合null
    - IPアドレス：種別が「onetime」の場合null
    - ファイルのアクセス形態：3つの値のうち１つを取る列挙型。非公開の場合「open_no」、エンバーゴの場合「open_date」、制限公開の場合「open_restricted」
    - URLトークン：URLのトークン
  
(4)マルチパートダウンロード処理について

  - 閾値を超えるサイズのファイルについては、マルチパートダウンロードを行う。マルチパートダウンロードは、本文URLとは異なるURLからファイルをダウンロードできる。

  - 閾値は、定数「WEKO_RECORDS_UI_S3_TRANSFER_MULTIPART_THRESHOLD」にて設定できる。1パートあたりのサイズは、定数「WEKO_RECORDS_UI_S3_TRANSFER_MULTIPART_CHUNKSIZE」にて設定できる（いずれもS3サーバ側転送用）。

  - ダウンロードのボタン・リンクを押下すると、大容量ファイルダウンロードを開始する旨のメッセージが表示される。

  - OK押下すると、「名前を付けて保存」のファイルピッカーを表示する。

  - ファイルピッカーにて、ダウンロードファイルの名前を指定すると、ファイルダウンロードが開始される。ダウンロード中は画面操作が行えなくなり、また画面を閉じるとダウンロードが中断されてしまう。

  - ダウンロード処理が完了すると、画面操作が行えるようになり、成功時は緑の帯で、失敗時は赤帯でメッセージが表示される。

  - マルチパートダウンロードでは、通常のダウンロードと同じファイルアクセス権限チェックが行われる。

  - マルチパートダウンロードでは、パートの一番最後のダウンロードのタイミングで統計情報が送信される。

  - マルチパートダウンロードでは、PDFカバーページには対応していない。

1TBファイルまではダウンロードの動作を確認済みだが、それより大きいファイルについては、動作を保証していない。

## 実装補足（v2.0.2 実装との突き合わせ）

- 権限判定：`weko_records_ui.permissions.check_file_download_permission`（内部ヘルパー `__check_user_permission`）/ `check_open_restricted_permission` / `check_user_group_permission`。ダウンロード処理は `weko_records_ui.fd`（`file_download_ui` / `file_preview_ui` / `_download_file`）。ワンタイム／シークレットURLモデルは `file_onetime_download` / `file_secret_download` / `file_url_download_log`。`WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` は weko-admin、プレビューサイズ上限 `WEKO_ITEMS_UI_FILE_SISE_PREVIEW_LIMIT` は weko-items-ui（形式別 dict）。
- 大容量（マルチパート）ダウンロードの閾値・パートサイズは S3 サーバ側転送用の `WEKO_RECORDS_UI_S3_TRANSFER_MULTIPART_THRESHOLD` / `_CHUNKSIZE` で設定する。

## 詳細リファレンス（v2.0.2 実装：エラー処理・分岐・データモデル）

判定の起点は `weko_records_ui.permissions.check_file_download_permission`、URL 型ダウンロードの検証は `weko_records_ui.utils.validate_url_download`。

### 1. アクセス権限の分岐（accessrole 別）

`check_file_download_permission(record, fjson, is_display_file_info, item_type)` は `fjson['accessrole']` で分岐する。分岐前に以下の「無条件許可」が先に評価される。

- 登録者系：`current_user.id` が `user_id_list`（`record._deposit.created_by` / `record.owner` / `record.weko_shared_ids`。`WEKO_ITEMS_UI_PROXY_POSTING` が True なら全共有者、False なら最後の1件）に含まれれば許可。
- スーパーユーザー系：`current_user` のロール名が `WEKO_PERMISSION_SUPER_ROLE_USER` + `WEKO_PERMISSION_ROLE_COMMUNITY` に含まれれば許可。
- 上記に該当しない場合のみ accessrole 別判定へ進む。処理中の例外は `abort(500)`。

| accessrole | ダウンロード可否の条件 |
| --- | --- |
| `open_access` | ファイル情報表示は常に可。実DLは `fjson.date[0].dateValue` が未来日でなければ可（未設定は可）。 |
| `open_date` | 情報表示は常に可。実DLは (a) 公開日 `fjson.accessdate`（無ければ `date[0].dateValue`）が未来でない、(b) `record.publish_date` が未来でない、(c) ロール条件（`fjson.roles` 一致、未指定は可）の AND。不可でも `site_license_check`（アイテムタイプ `has_site_license` かつ IP 判定 or `check_user_group_permission`）が真なら可。 |
| `open_login` | 情報表示は常に可。実DLは (a) ログイン済み、(b) ロール条件、(c) 課金/グループ条件（`fjson.groupsprice` があれば該当グループ所属、無ければ `fjson.groups` 所属、未設定は可）の AND。**AND の結果が偽でも `site_license_check`（アイテムタイプ `has_site_license` が真、かつ IP 判定 or グループ課金）が真ならサイトライセンス利用者として可**。 |
| `open_no` | 情報表示は原則可だが未ログイン・非許可・サイトライセンス該当時は非表示。実DLは `current_user.email` が登録者メール一覧に含まれる場合のみ可。 |
| `open_restricted` | `check_open_restricted_permission` に委譲。承認済み `FilePermission`（`status==1`）が存在し、かつ `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` が True の場合のみ `check_permission_period`（有効なワンタイムDLの有無）を評価。DISPLAY_FLAG が False または未承認は不可。**ただし判定が偽でも `site_license_check` が真ならサイトライセンス利用者として可**。 |

補足：`fd.py` の `file_ui` の実DL時、`open_restricted` で所有者・スーパーユーザーでなければ有効なワンタイムDLを取得（無ければ `abort(403)`）し token を生成して `validate_onetime_token` に委譲する。ファイル未存在は `abort(404)`、未ログインはログイン要求。**ただしサイトライセンス利用者（`weko_records_ui.ipaddr.check_site_license_permission()` が真）は、この open_restricted のワンタイムDL強制フローをスキップして直接DLする。**

### 2. ワンタイム／シークレットURL のエラー・分岐

中核は `validate_url_download`。`(bool, error_message)` を返し、呼び出し元が `error_response(msg, 403|404|500)` で応答する。主なエラー（EN原文、`_()` で i18n）と条件：

| メッセージ | 条件 | HTTP |
| --- | --- | --- |
| The type of URL is not specified. | URL 種別未指定 | 403 |
| The provided token is invalid. | トークン不正・改ざん | 403 |
| This feature is currently disabled. | シークレットURL機能が無効 | 403 |
| This file is currently not available for this feature. | 対象外ファイル/レコード | 403 |
| This URL has been deactivated. | `is_deleted is True`（論理削除） | 403 |
| The download limit has been exceeded. | `download_count >= download_limit` | 403 |
| The expiration date for download has been exceeded. | `expiration_date < 現在(UTC)` | 403 |
| Restricted access is disabled. | `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` が False | 403 |
| The file "%s" does not exist. | ファイルオブジェクト取得不可 | 404 |
| Invalid token. | 非ゲストで未ログイン or `current_user.email != user_mail`／セッション token 不一致 | 403 |
| Could not download file. | 入力 `mail_address` が `user_mail` と不一致 | 403 |
| Invalid verification info. | パスワード保護有効（`restricted_access.password_enable` かつ `extra_info.password_for_download`）で入力パスワード不正 | 403 |
| Unexpected error occurred. | ログ保存/カウント加算/`extra_info` 更新中の例外 | 500 |

分岐：ゲスト作成 token（`is_guest`）は `validate_onetime_guest` でメール確認画面へリダイレクトし、確認後 `file_download_onetime` でメール・パスワード照合。利用報告が必要な場合は `process_onetime_file_download` 内で `check_and_send_usage_report` を実行。正常時は `save_download_log`（`FileUrlDownloadLog` 追加）→ `increment_download_count` → `_download_file` の順。

### 3. データモデル（テーブル／主要カラム）

共通 mixin `DownloadMixin` を `FileOnetimeDownload` と `FileSecretDownload` が継承。共通メソッド：`increment_download_count`（+1。上限到達で `ValueError`）／`delete_logically`（`is_deleted=True`）／`fetch_active_urls`（未失効・未達・未削除の有効URL取得）。

- `FileOnetimeDownload`（`file_onetime_download`）：`id` / `approver_id`(FK accounts_user) / `record_id` / `file_name` / `expiration_date` / `download_limit` / `download_count`(既定0) / `user_mail` / `is_guest`(既定False) / `is_deleted`(既定False) / `extra_info`(JSON。`password_for_download`・利用報告関連) ＋ `created`/`updated`。制約：`created < expiration_date` / `download_limit > 0` / `download_count <= download_limit`。
- `FileSecretDownload`（`file_secret_download`）：`id` / `creator_id`(FK, NOT NULL) / `record_id` / `file_name` / `label_name` / `expiration_date` / `download_limit` / `download_count` / `is_deleted` ＋ `created`/`updated`。
- `FileUrlDownloadLog`（`file_url_download_log`）：`id` / `url_type`(Enum SECRET/ONETIME) / `secret_url_id`(FK) / `onetime_url_id`(FK) / `ip_address`(INET) / `access_status`(Enum OPEN_NO/OPEN_DATE/OPEN_RESTRICTED) / `used_token` ＋ `created`/`updated`。CHECK制約：SECRET は `secret_url_id` 必須・`ip_address` 必須・status は OPEN_NO/OPEN_DATE；ONETIME は `onetime_url_id` 必須・`ip_address` NULL・status は OPEN_RESTRICTED。
- 関連：`file_permission`（`FilePermission`）は制限公開の申請・承認状態（`status`：-1 初期 / 0 処理中 / 1 承認）を保持し `open_restricted` 判定で参照される。


## 更新履歴

|日付|GitHubコミットID|更新内容|
|---|---|---|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2023/11/11||V0.9.27|
|2023/12/22|4ec162bf3bdcf843df23863fbf7d5bb36ba875e4|W2023-42|
|2024/07/1|7733de131da9ad59ab591b2df1c70ddefcfcad98|v1.0.7対応|
|2025/09/15|c387c0a978c9eb318044b3d17d72838872012370|Import to GakuNin RDM機能を追加|
|2025/10/31|160a811eed2c61492558905db34fa0619da6b18f|設定値による機能制御を記載|
|2026/07/17||v2.1.0差分反映：サイトライセンス利用者は open_login/open_restricted で実DL可（`check_file_download_permission` のフォールバック）、および open_restricted のワンタイムDL強制フローをスキップ（`fd.py file_ui`）する点を追記|
