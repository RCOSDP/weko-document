
### 一括削除

  - > 目的・用途

本機能は、管理者として、インデックスを対象にしてアイテムを一括削除する機能である。

  - > 利用方法

【Administration \> アイテム管理(Items) \> 一括削除(Bulk Delete)画面】を開き、インデックスツリーからインデックスを選択し、削除することでインデックスに所属するアイテムを一括削除することができる。

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

<!-- end list -->

  - 【Administration \> アイテム管理(Items) \> 一括削除(Bulk Delete)画面】にてアイテムを一括削除する
    
      - 「インデックスツリー」（Index Tree）エリアでアイテムを一括削除するインデックスを選択する。
    
      - 「子インデックスのアイテムも削除する」（Delete items of child recursively）チェックボックスにチェックを入れることで、再帰的に子インデックスに所属するアイテムも削除できる。
    
      - 複数インデックスに所属しているアイテムが存在する場合は、当該アイテムから削除対象インデックスの所属を外す（アイテムは削除されない）。
    
      - 「削除」（Delete）ボタンを押すと、確認ダイヤログが表示されます。  
        確認メッセージ：  
        日本語：「削除してよろしいですか？」  
        英語：「 Are you sure you want to delete it?」
        
          - 「接続」（Continue）ボタンを押すと、アイテムの一括削除が実行される
        
          - 「キャンセル」（Cancel）ボタンを押すと、確認ダイヤログ’を閉じる

  - 過去のバージョンも含めて削除する（論理削除）

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-search-ui

  - > weko\_records\_ui

<!-- end list -->

  - > 処理概要

> 一括更新画面表示について

  - > 【Administration \> アイテム管理(Items) \> 一括削除(Bulk Delete)画面】を開いた際、以下の処理を実行する。
    
      - > weko\_index\_tree.rest.IndexTreeActionResource.getメソッドを呼び出し、インデックスツリー情報を取得する。それらを「インデックスツリー」エリアに表示する。

> 削除機能について

  - > アイテムを削除したいインデックスを「インデックスツリー」エリアから選び、「削除」ボタンを押下する。この操作によって、weko\_search\_ui.admin.ItemManagementBulkDelete.indexにてdelete\_recordsメソッドが呼び出され、論理削除を行う。なお、その際、チェックボックスにチェックを入れていた場合、削除するインデックスの子インデックス以下のアイテムも論理削除する。

  - > 論理削除はrecords\_metadataテーブルのキーpublsih\_statusを-1に設定することによってweko3上で表示されなくなる。

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
