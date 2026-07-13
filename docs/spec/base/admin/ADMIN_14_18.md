### ファイルプレビュー

## 目的・用途

本機能は、Microsoft Officeファイルをプレビュー表示する際に、PDFファイルへ指定されたファイルの変換に設定する機能である

## 利用方法

【Administration > 設定（Setting） > ファイルプレビュー（File Preview）画面】にてPDFファイルの保存先パス及び保存期間を設定する

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ |  |  |  |  |  |

## 機能内容

  - 画面表示時に、各設定値を取得して入力エリアに表示する
    
      - 「PDF Save Path」：サーバー側で変換したPDFファイルの保存先パスを設定する
        
          - デフォルトの値：「/tmp」
    
      - 「PDF TTL」：PDFファイルの保存期間を設定する
        
          - デフォルトの値：「3600」
        
          - 単位：秒
    
      - ［保存（Save）］ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する  
        メッセージ：  
        　日本語：「設定を変更しました」  
        　英語：「Successfully Changed Settings.」
        
          - 「PDF Save Path」の入力値が「/」であるか、どちらかの入力欄が空である場合、設定内容を保存せずに、エラーメッセージを画面上部に表示して、画面を再表示する  
            エラーメッセージ：  
            　日本語：「設定変更に失敗しました」  
            　英語：「Failurely Changed Settings.」
        
          - 「PDF Save Path」の入力値の末尾が「/」である場合、末尾の「/」を除いた内容が保存される
        
          - 「PDF Save Path」が変更される場合、もともとのパスにあったファイルは削除される

  - ここで設定した値を使用して、保存時間を過ぎたPDFファイルを削除する処理を定期的に実行する

## 関連モジュール

  - invenio_files_rest：各デフォルト値をコンフィグで定義している

  - weko_admin：画面表示のクラスと、設定を保存するDBを定義している

## 処理概要

  - 画面表示時は、weko_admin.admin. FilePreviewSettingsView.indexメソッドがGETで呼び出される
    
      - このとき、admin_settingsテーブルからnameが「convert_pdf_settings」であるレコードを取得する
        
          - 取得できなかった場合は、以下のコンフィグからデフォルトの内容を取得する
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/config.py#L128-L131>
            
              - 設定キー：
                
                  - FILES_REST_DEFAULT_PDF_SAVE_PATH
                
                  - FILES_REST_DEFAULT_PDF_TTL
    
      - 取得した情報を各入力欄に設定して画面表示する

  - ［保存（Save）］ボタンを押すと、weko_admin.admin. FilePreviewSettingsView.indexメソッドがPOSTで呼び出される
    
      - admin_settingsテーブルに、以下の内容で保存する  
        ※nameが同じレコードがなかった場合は新規作成、あった場合は更新する
        
          - name：「convert_pdf_settings」
        
          - settings：「{"path":「PDF Save Path」の入力値, "pdf_ttl":「PDF TTL」の入力値}」
    
      - その後、GETで呼び出されたときと同様の処理を行い、画面表示する

  - ここで設定した値は、invenio_files_rest.tasks.check_file_storage_time関数で使用する
    
      - この関数は、celeryタスクで定期的に実行する
    
    
      - admi）："の場所にある各ファイルについて、最終更新日時から（"pdf_ttl"の値）秒以上経過していた場合に、invenio_files_rest.storage.pyfs. remove_dir_with_file関数によって削除する

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
