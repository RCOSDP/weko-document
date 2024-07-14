### アイテム表示

<!-- end list -->

  - > 目的・用途

本機能は、アイテム表示・検索に関する設定機能である

  - > 利用方法

【Administration \> Setting (設定) \> Item (アイテム表示)】からアイテム表示における条件の設定を行う。

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

使用している画面

  - > 【Administration \> Setting (設定) \> Items（アイテム表示）画面】アイテム表示・検索に関する機能を設定する画面である

E-mailの表示/非表示を設定する

  - > 【Administration \> Setting (設定) \> Items (アイテム表示) 画面】の「Display Email」エリアにてE-Mailの表示（Display Email ）/非表示（Hide Email）を設定することができる。本設定によりアイテム詳細画面、ADMIN14-4 PDFカバーページ および <https://redmine.devops.rcos.nii.ac.jp/projects/weko-dev-doc/wiki/JSON>USER3-7 Export(JSON) 機能 におけるE-Mail出力を制御する。
    
      - Display Email が設定されている場合、アイテム詳細画面、PDFカバーページおよびJSON Export機能にてメールアドレスを表示する。
    
      - Hide Email が設定されている場合、アイテム詳細画面、PDFカバーページおよびJSON Export機能にてメールアドレスを表示しない。
    
      - 「保存」（Save）ボタンを押すと、設定内容を保存する

<!-- end list -->

  - 【Administration \> Setting (設定)\> Items(アイテム表示) 画面】でのOpen Dateエリアにファイルの公開日の表示/非表示を設定する
    
      - 「表示」（Display）を設定する場合、すべてのユーザにはアイテムリスト、アイテム詳細画面に公開日を表示とする
    
      - 「非表示」（Hide Open Date）を設定する場合、ゲストユーザにはアイテムリスト、アイテム詳細画面に公開日を非表示とする
    
      - デフォルト：「表示」（Display）
    
      - 「保存」（Save）ボタンを押すと、設定内容を保存する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-records-ui

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - > 【Save (保存)】を押下した際に、weko\_records\_ui.admin.ItemSettingView.indexを呼び出して使用する。
    
      - > weko\_admin.models.AdminSettingを呼び出し、admin\_settingsテーブルを更新する。

  - > weko-records-ui.utils.is\_show\_email\_of\_creator
    
      - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/utils.py#L578-L624>
    
      - 当該アイテムタイプについて、E-Mail表示する場合はTrueを返す。

<!-- end list -->

  - ファイルの公開日の表示/非表示を設定する
    
      - デフォルト状態の設定：
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L68>
        
          - 設定キー： OPEN\_DATE\_DISPLAY\_FLG
        
          - 現在の設定値：

> OPEN\_DATE\_DISPLAY\_FLG = True

  - > 表示/非表示状態の値を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L69-L70>
    
      - 設定キー：OPEN\_DATE\_DISPLAY\_VALUE、OPEN\_DATE\_HIDE\_VALUE
    
      - 現在の設定値：

> OPEN\_DATE\_DISPLAY\_VALUE = '1'
> 
> OPEN\_DATE\_HIDE\_VALUE = '0'

  - > E-mailの表示/非表示を設定する
    
      - デフォルト状態の設定：
        
          - パス：   
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L65>
        
          - 設定キー： EMAIL\_DISPLAY\_FLG
        
          - 現在の設定値：

<!-- end list -->

  - > EMAIL\_DISPLAY\_FLG = True更新履歴

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
