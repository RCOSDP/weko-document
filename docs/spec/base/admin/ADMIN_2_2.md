### 一括削除

## 目的・用途

本機能は、管理者として、インデックスを対象にしてアイテムを一括削除する機能である。

## 利用方法

【Administration > アイテム管理(Items) > 一括削除(Bulk Delete)画面】を開き、インデックスツリーからインデックスを選択し、削除することでインデックスに所属するアイテムを一括削除することができる。

## 利用可能なロール

|ロール|システム<br>管理者|リポジトリ<br>管理者|サブリポジトリ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|利用可否|○|○|○| | | |

## 機能内容

- 【Administration > アイテム管理(Items) > 一括削除(Bulk Delete)画面】にてアイテムを一括削除する
  - 「インデックスツリー」（Index Tree）エリアでアイテムを一括削除するインデックスを選択する。
    - サブリポジトリ管理者の場合は管理対象のサブリポジトリに属するインデックスツリーが表示される。
  - 「子インデックスのアイテムも削除する」（Delete items of child recursively）チェックボックスにチェックを入れることで、再帰的に子インデックスに所属するアイテムも削除できる。
  - 複数インデックスに所属しているアイテムが存在する場合は、当該アイテムから削除対象インデックスの所属を外す（アイテムは削除されない）。
  - 「削除」（Delete）ボタンを押すと、確認ダイヤログが表示されます。  
    確認メッセージ：  
    日本語：「削除してよろしいですか？」  
    英語：「 Are you sure you want to delete it?」
    - 「接続」（Continue）ボタンを押すと、アイテムの一括削除が実行される
    - 「キャンセル」（Cancel）ボタンを押すと、確認ダイヤログを閉じる

- 過去のバージョンも含めて削除する（論理削除）

## 関連モジュール

- weko-search-ui
- weko_records_ui

## 処理概要

一括削除画面表示について

- 【Administration > アイテム管理(Items) > 一括削除(Bulk Delete)画面】を開いた際、以下の処理を実行する。
  - weko_index_tree.rest.IndexTreeActionResource.getメソッドを呼び出し、インデックスツリー情報を取得する。それらを「インデックスツリー」エリアに表示する。

削除機能について

- アイテムを削除したいインデックスを「インデックスツリー」エリアから選び、「削除」ボタンを押下する。この操作によって、weko_search_ui.admin.ItemManagementBulkDelete.indexにてdelete_recordsメソッドが呼び出され、論理削除を行う。なお、その際、チェックボックスにチェックを入れていた場合、削除するインデックスの子インデックス以下のアイテムも論理削除する。
- 論理削除はrecords_metadataテーブルのキーpublish_statusを-1に設定することによってweko3上で表示されなくなる。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_search_ui.admin.ItemManagementBulkDelete`（endpoint `items/bulk/delete`、**GET/PUT**。削除は PUT）。確認ダイアログ・警告は `/check`（`check`）で生成し、DOI 付与済み・編集中アイテムは削除対象から除外（`get_doi_items_in_index` + `get_editing_items_in_index`）。再帰削除は view の `recursively` パラメータで制御。
- 削除処理：`delete_records`（`weko_search_ui.utils`）→ `soft_delete`（`weko_records_ui.utils`）。`publish_status` を `PublishStatus.DELETE.value`（文字列 `"-1"`、enum は weko-schema-ui）に設定し、全バージョンの `PersistentIdentifier.status` を DELETED にする。複数インデックス所属アイテムは当該インデックスからのアンリンクのみ。副作用：FeedbackMailList/RequestMailList 削除、バケット削除、ES 更新、`ITEM_BULK_DELETE` ログ。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2025/01/23|-|サブリポジトリ対応|
