### インデックスリンク表示

  - > 目的・用途

この機能はweko上でインデックスリンクを表示するか否かを設定するためのものである。

  - > 利用方法

【Administration \> 設定【Setting】 \> インデックスリンク表示(Index Link)画面】を開き、設定した後、「更新」ボタンを押下する。

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
<td>〇</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

1\. インデックスリンクエリアの表示/非表示を設定する

  - > 【Administration \> 設定(Setting) \> インデックスリンク表示(Index Link)画面】にインデックスリンクエリアの表示/非表示を設定する
    
      - 「Enable」を選択する場合、インデックスリンクエリアを表示する。
    
      - 「Disable」を選択する場合、 インデックスリンクエリアを表示しない。
    
      - デフォルト：「Disable」

2\. インデックスごとにインデックスリンクの表示/非表示を設定する

  - > 【Administration \> インデックスツリー管理(index tree) \> ツリー編集(Edit Tree)画面】にインデックスごとにインデックスリンクの表示/非表示を設定できる。  
    > また、インデックスごとにインデックスリンクの”表示名”を設定できる。

  - > 設定方法の詳細は[ADMIN-3-1 ツリー編集](\\l)を参照すること。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_index\_tree

<!-- end list -->

  - > 処理概要

> インデックスリンク表示設定画面の表示

  - > 【administration \> 設定 \> インデックスリンク表示】画面を開く。この操作によって、weko\_index\_tree.admin.IndexLinkSettingView.indexメソッドがGETで呼び出され、現在のインデックスリンク表示設定をindex\_styleテーブルの列「index\_link\_enabled」から取得し、画面に表示する。  
    > デフォルトでは無効に設定されている。

> インデックスリンク表示設定について

  - > 「更新」ボタンを押下すると、weko\_index\_tree.admin.IndexLinkSettingView.indexメソッドがPOSTで呼び出され、ウェブ上で選択した「有効」または「無効」に応じて、  
    > index\_styleテーブルの列「index\_link\_enabled」を設定する。成功したらweb上側に「IndexLink flag was updated」と表示する。

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
