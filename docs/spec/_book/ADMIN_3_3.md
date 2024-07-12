### カスタムソート

  - > 目的・用途

本機能は、インデックスに属するアイテムの表示順序を設定する機能である。

  - > 利用方法

1\. システム管理者、リポジトリ管理者でログインする。

2\. 【Administration \> インデックスツリー管理(Index Tree) \> カスタムソート(Custom Sort)画面】を開き、編集したいインデックスを選び、編集する。

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

  - 【Administration \> インデックスツリー管理(Index Tree) \> カスタムソート(Custom Sort)画面】にインデックスに属するアイテムの表示順序を設定できる。
    
      - 「インデックスツリー」（Index Tree）エリアから設定するインデックスを選択すると、選択しているインデックスに属するアイテムが「ターゲットインデックス」（Target Index）に表示される。
    
      - 「編集」（Edit）ボタンを押すことで、アイテムの表示順序を設定できる。
    
      - 「Display Priority」に各アイテムに表示順序を入力する。
        
          - 数字のみ(全角を許容)を入力可能とする。不正な文字を入力する場合、入力した文字が保存されない。
    
      - 表示順が指定されないアイテムについては、表示順序が指定されたアイテムの後に表示される。
    
      - 検索結果の「アイテムリスト」エリアで、「表示順」プルダウンで「Custom」を選択すると、カスタムソートの設定が適用された並び順になる。
        
          - なお、「custom」の際の優先順位としては以下のルールがある。
            
              - 昇順(asc)、降順(desc)の基準値はカスタムソートの値である。
            
              - カスタムソートの値が存在するアイテムは存在しないアイテムよりも優先される。
            
              - カスタムソートの値が存在しないアイテムは作成日時の並び順になる。

<!-- end list -->

  - > 関連モジュール

> weko\_index\_tree
> 
> weko\_search\_ui
> 
> weko\_theme

  - > 処理概要

> カスタムソート編集画面表示について

  - > 【Administration \> インデックスツリー管理(Index Tree) \> カスタムソート(Custom Sort)画面】を開いた際、weko\_search.ui.admin.ItemManagementCustomSort.indexが呼び出される。それによってインデックスツリーを表示する。次に「インデックスツリー」エリアから編集したいインデックスを選ぶ。この操作によってweko\_search\_ui.admin.ItemManagementBulkSeach.indexが呼び出され、選択されたインデックスに属するアイテム一覧と順番を入力するテキストボックスを非活性状態で「対象インデックス」エリアに表示する。

> カスタムソート編集について

  - > 「対象インデックス」にて編集ボタンを押下すると、「Display Priority」列のテキストボックス全てが活性化し、入力可能になる。並び替えを指定したいテキストボックスに表示順位を入力し、保存ボタンを押下する。そのとき、weko\_search\_ui.static.js.weko\_serach\_ui.app.searchResCtrl.itemManagementSaveが動き、weko\_search\_ui.admin.ItemManagementCustomSort.save\_sortメソッドが呼び出される。これによってset\_item\_sort\_customメソッドが呼び出され、編集したカスタムソートの順番をindexテーブルのキーitem\_custom\_sortの値に保存する。

  - > 数字(半角、全角許容)以外の文字を入力した場合、set\_item\_sort\_customでNoneと変換され、そのアイテムのカスタムソート設定はなくなる。

> 検索結果にてカスタムソートを選んだ際の処理

  - > .query.pyにてget\_custom\_sortメソッドが呼び出され、Elasticsearch用のscriptを作成し、それをElastcsearchインスタンスに渡すことで、カスタムソートの設定どおりに検索結果をソートする。

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
<p>2024/04/14</p>
</blockquote></td>
<td>cd0183f59a16928be2511e33e4495a3376f143c9</td>
<td>v1.0.6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>
