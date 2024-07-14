### ファイルプレビュー

  - > 目的・用途

本機能は、Microsoft Officeファイルをプレビュー表示する際に、PDFファイルへ指定されたファイルの変換に設定する機能である

  - > 利用方法

【Administration \> 設定（Setting） \> ファイルプレビュー（File Preview）画面】にてPDFファイルの保存先パス及び保存期間を設定する

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

<!-- end list -->

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

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio\_files\_rest：各デフォルト値をコンフィグで定義している

  - weko\_admin：画面表示のクラスと、設定を保存するDBを定義している

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 画面表示時は、weko\_admin.admin. FilePreviewSettingsView.indexメソッドがGETで呼び出される
    
      - このとき、admin\_settingsテーブルからnameが「convert\_pdf\_settings」であるレコードを取得する
        
          - 取得できなかった場合は、以下のコンフィグからデフォルトの内容を取得する
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/config.py#L128-L131>
            
              - 設定キー：
                
                  - FILES\_REST\_DEFAULT\_PDF\_SAVE\_PATH
                
                  - FILES\_REST\_DEFAULT\_PDF\_TTL
    
      - 取得した情報を各入力欄に設定して画面表示する

  - ［保存（Save）］ボタンを押すと、weko\_admin.admin. FilePreviewSettingsView.indexメソッドがPOSTで呼び出される
    
      - admin\_settingsテーブルに、以下の内容で保存する  
        ※nameが同じレコードがなかった場合は新規作成、あった場合は更新する
        
          - name：「convert\_pdf\_settings」
        
          - settings：「{"path":「PDF Save Path」の入力値, "pdf\_ttl":「PDF TTL」の入力値}」
    
      - その後、GETで呼び出されたときと同様の処理を行い、画面表示する

  - ここで設定した値は、invenio\_files\_rest.tasks.check\_file\_storage\_time関数で使用する
    
      - この関数は、celeryタスクで定期的に実行する
    
    <!-- end list -->
    
      - > admi）："の場所にある各ファイルについて、最終更新日時から（"pdf\_ttl"の値）秒以上経過していた場合に、invenio\_files\_rest.storage.pyfs. remove\_dir\_with\_file関数によって削除する

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
