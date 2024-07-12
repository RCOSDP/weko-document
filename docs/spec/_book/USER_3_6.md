### 共有

  - > 目的・用途

本機能は、アイテムの詳細情報を共有する機能である。

  - > 利用方法

共有は、アイテム詳細画面の右端のShareエリアの共有ボタンを押下して行う。

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
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 本機能に対応していた「AddThis」は2023年5月31日にサービスを終了しているため、共有機能を使用することは出来ない。

  - アイテム詳細画面での「共有」（Share）エリアに共有ボタンを表示する
    
      - 表示しておく共有ボタンをhtmlファイルに指定する
        
          - パス：  
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/box/share.html#L25-L33>
        
          - 表示される共有ボタンは以下の通りである。また、共有アイコンをマウスホバーすると、共有サイト名を表示する
            
              - 「mendeley」
            
              - 「citeulike」(2019年サービス終了により表示されない)
            
              - 「twitter」
            
              - 「facebook」
            
              - 「print」
        
          - 「+」ボタンを設ける
            
              - 「+」ボタンをマウスホバーすると、共有サイト名一覧を表示する
            
              - 「+」ボタンを押すと、共有モデルを表示する

  - 共有ボタンを押すと、該当サイトに移動する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > 対応しているモジュール：「weko\_records\_ui」

  - > 対応しているプラグイン：「AddThis」

<!-- end list -->

  - > 処理概要

> weko\_theme.static.js.addthis.addthis\_widgetにおいてAddThisのアイテムの共有を設定している。  
> <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/static/js/addthis/addthis_widget.js>

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