### 統計情報表示

  - > 目的・用途

本機能は、アイテムの利用統計情報を閲覧を設定する機能である

  - > 利用方法

【Administration \> Setting (設定) \> Stats (統計情報表示) 画面】から、アイテムの統計情報の表示/非表示を設定する。

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

  - 【Administration \> Setting (設定) \> Stats (統計情報表示) 画面】：アイテムの利用統計情報の表示/非表示を設定する画面である

  - 【アイテム詳細画面】：利用統計情報を表示する画面である

  - 【ファイル詳細画面 (information)】：コンテンツファイル単位の統計情報を表示する画面である

1\. アイテムの利用統計情報を表示する

  - アイテムの利用統計情報の表示/非表示を設定する
    
      - 【Administration \> Setting (設定) \> Stats (統計情報表示) 画面】での「統計設定」における「レコード統計の表示/非表示」（Show/Hide Record Stats）エリアにアイテムの利用統計情報の表示/非表示を設定する
        
          - 「オン」（On）にすると、アイテム詳細表示画面に利用統計エリア\[Stats\]を表示する
        
          - 「オフ」（Off）にすると、アイテム詳細表示画面に利用統計エリア\[Stats\]を非表示とする
        
          - デフォルト：「オン」（On）
        
          - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する  
            メッセージ：  
            　日本語：「設定を変更しました」  
            　英語：「Successfully Changed Settings.」

  - アイテムの利用統計情報を表示する
    
      - アイテム単位の閲覧回数は、【アイテム詳細画面】での「Views」エリアに表示する
    
      - 閲覧回数は、 invenio-statsにてログ集計した値とする
    
      - 閲覧回数は、全ドメインと各ドメイン毎（トップレベルドメイン毎）で集計値を表示する
        
          - 各ドメイン毎（トップレベルドメイン毎）はデフォルト表示は"非表示"とし、「詳細を確認」（See details）リンクを押すことで表示する
            
              - 確定できないドメインに対して、「UNKNOWN」として表示する
    
      - 閲覧回数は、集計機関プルダウン「Period」より年月を選択することで指定期間の数値を表示する
        
          - デフォルトは全期間の数値（total）とする

2\. コンテンツファイル単位の統計情報を表示する

  - 【ファイル詳細画面 (Information)】での「統計」（Stats）タブにコンテンツファイル単位の統計情報を表示する
    
      - 表示項目は以下の通りである
        
          - ダウンロード回数は、「ダウンロード数」（Downloads）エリアに表示する
        
          - 再生回数は、「再生回数」（Plays）エリアに表示する
    
      - ダウンロード回数と再生回数は、invenio-statsにてログ集計した値とする
        
          - 統計情報は、全ドメインと各ドメイン毎（トップレベルドメイン毎）で集計値を表示する
        
          - 各ドメイン毎（トップレベルドメイン毎）はデフォルト表示は"非表示"とし、「詳細を確認」（See details）リンクを押すことで表示する
            
              - 確定できないドメインに対して、「UNKNOWN」として表示する
        
          - 統計情報は、集計機関プルダウン「Period」より年月を選択することで指定期間の数値を表示する
            
              - デフォルトは全期間の数値 (total) とする

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_admin

  - > weko\_records\_ui

  - > invenio\_stats

<!-- end list -->

  - > 処理概要

> 【Administration \> Setting (設定) \> Stats (統計情報表示)】において、統計情報の表示/非表示を選択して【Save (保存)】を押下すると、weko\_admin.StatsSettingsView.indexを呼び出して使用する。

  - > weko\_admin.models.AdminSettings.updateを呼び出して、admin\_settingsテーブルから、「display\_stats\_settings」カラムを更新する。

> weko\_admin.models.AdminSettings.getで「display\_stats\_settings」を取得して、  
> 「WEKO\_ADMIN\_STATS\_SETTINGS\_TEMPLATE」に沿って、  
> flask\_admin.base.BaseView.renderで更新した状態の統計情報表示設定画面を表示する。「WEKO\_ADMIN\_STATS\_SETTINGS\_TEMPLATE」：weko\_admin.config

  - > 'weko\_admin/admin/stats\_settings.html'

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
