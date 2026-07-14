### カスタムソート

## 目的・用途

本機能は、インデックスに属するアイテムの表示順序を設定する機能である。

## 利用方法

1\. システム管理者、リポジトリ管理者、サブリポジトリ管理者でログインする。

2\. 【Administration > インデックスツリー管理(Index Tree) > カスタムソート(Custom Sort)画面】を開き、編集したいインデックスを選び、編集する。

## 利用可能なロール

|ロール|システム<br>管理者|リポジトリ<br>管理者|サブリポジトリ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|利用可否|○|○|○| | | |

## 機能内容

- 【Administration > インデックスツリー管理(Index Tree) > カスタムソート(Custom Sort)画面】にインデックスに属するアイテムの表示順序を設定できる。
  - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに設定したインデックスをルートとしたインデックスツリーが「インデックスツリー」（Index Tree）エリアに表示される。
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

## 関連モジュール

- weko_index_tree
- weko_search_ui
- weko_theme

## 処理概要

カスタムソート編集画面表示について

- 【Administration > インデックスツリー管理(Index Tree) > カスタムソート(Custom Sort)画面】を開いた際、weko_search_ui.admin.ItemManagementCustomSort.indexが呼び出される。それによってインデックスツリーを表示する。次に「インデックスツリー」エリアから編集したいインデックスを選ぶ。この操作によってweko_search_ui.admin.ItemManagementBulkSearch.indexが呼び出され、選択されたインデックスに属するアイテム一覧と順番を入力するテキストボックスを非活性状態で「対象インデックス」エリアに表示する。

カスタムソート編集について

- 「対象インデックス」にて編集ボタンを押下すると、「Display Priority」列のテキストボックス全てが活性化し、入力可能になる。並び替えを指定したいテキストボックスに表示順位を入力し、保存ボタンを押下する。そのとき、weko_search_ui.static.js.weko_search_ui.app.searchResCtrl.itemManagementSaveが動き、weko_search_ui.admin.ItemManagementCustomSort.save_sortメソッドが呼び出される。これによってset_item_sort_customメソッドが呼び出され、編集したカスタムソートの順番をindexテーブルのキーitem_custom_sortの値に保存する。
- 数字(半角、全角許容)以外、または0以下の値を入力した場合、set_item_sort_customでそのアイテムはカスタムソートのマップから除外され、カスタムソート設定はなくなる。

検索結果にてカスタムソートを選んだ際の処理

- weko_search_ui.api.SearchSettingのget_custom_sortメソッドが呼び出され、Elasticsearch用のscriptを作成し、それをElasticsearchインスタンスに渡すことで、カスタムソートの設定どおりに検索結果をソートする。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_search_ui.admin.ItemManagementCustomSort`（endpoint `items/custom_sort`）＋ `ItemManagementBulkSearch`。保存は `POST /admin/items/custom_sort/save`（`save_sort`）→ `weko_index_tree.api.Indexes.set_item_sort_custom`。ソート適用時は `weko_search_ui.api.SearchSetting.get_custom_sort`（`query.py` ではない）が ES painless スクリプトソートを生成。
- 補足：非数値・0以下の値はマップから除外される。保存時の ES 同期はコメントアウトされており、カスタムソートはクエリ時に DB 列（`Index.item_custom_sort`、JSONB）を読んで適用する。画面テンプレートは weko-theme の `WEKO_THEME_ADMIN_ITEM_MANAGEMENT_TEMPLATE`。専用のロールガードは無い。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2024/04/14|cd0183f59a16928be2511e33e4495a3376f143c9|v1.0.6|
|2025/01/23|-|サブリポジトリ対応|
