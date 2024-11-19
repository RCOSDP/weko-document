### アイテム一括出力

  - > 目的・用途

この機能は、USER-2-4の機能であるアイテム一括出力の可否を設定するものである。

  - > 利用方法

【Administration \> 設定(Setting) \> アイテム一括出力(Item Export)画面】を開き、設定後「保存」ボタンを押下する。

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

  - 【Administration \> 設定(Setting) \> アイテム一括出力(Item Export)画面】にアイテムの一括出力を設定する。
    
      - アイテムの一括出力可否（Allow/Disallow Item Exporting）  
        　アイテムの一括出力の機能を「設定する／設定しない」を設定する。
        
          - オン(On)：アイテム一括出力の機能を有効にする。
        
          - オフ(Off)：アイテム一括出力の機能を無効にする。
    
      - コンテンツファイルの出力可否（Export File Contents）  
        　アイテムの一括出力をする際に、コンテンツファイルを含めて「出力する／出力しない」を設定する。
        
          - オン(On)：コンテンツファイルを含めて出力するように設定する。
        
          - オフ(Off)：コンテンツファイルは含めずに出力するように設定する。
    
      - 一括出力できる最大アイテム数はconfigで設定する。デフォルトは最大100件とする。
    
      - 「保存」（Save）ボタンを押すと、設定情報をデータベースに格納する。

  - アイテム一括出力の仕方の詳細は[USER-2-4アイテム一括出力](\\l)を参照すること。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_admin

<!-- end list -->

  - > 処理概要

> アイテム一括出力画面の表示

  - > 【Administration \> 設定 \> アイテム一括出力】画面を開く。この操作によって、weko\_admin.admin.ItemExportSettingView.indexメソッドがGETで呼び出され、\_get\_current\_settingsメソッドでadmin\_settingテーブルのキーitem\_export\_settingsより現在の設定を取得後画面に表示する。

> アイテム一括出力の設定

  - > 任意の設定をした後、「保存」ボタンを押下する。この操作によって、weko\_admin.admin.ItemExportSettingView.indexメソッドがPUTで呼び出され、AdminSettings.updateでadmin\_settingテーブルのキーitem\_export\_settingsに設定が保存される。そして、更新された設定と"Successfully Changed Settings"を画面に表示する。

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