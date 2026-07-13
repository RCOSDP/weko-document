### 一括更新

## 目的・用途

アイテムに付随しているファイルに対して、ライセンス、公開日、アクセスタイプを一括で更新する機能である。

## 利用方法

【Administration > アイテム管理(Items) > 一括更新(Bulk Update)画面】を開き、更新したいアイテムを選ぶ。  
その後更新したい情報を選び、更新する。

## 利用可能なロール

|ロール|システム<br>管理者|リポジトリ<br>管理者|サブリポジトリ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|利用可否|○|○|○| | | |

## 機能内容

- 【Administration > アイテム管理(Items) > 一括更新(Bulk Update)画面】：一括更新を実行する画面である。

- 事前に更新するアイテムの変更したい項目について設定されている必要がある。  
  ファイルが登録され、それに対して、アクセスタイプ、ライセンスをアイテムに登録しておく必要がある。

- 【一括更新画面】は、以下の表示エリアで構成する
  - 「インデックスツリー」（Index Tree）エリア
    - 【Administration > インデックスツリー管理(Index Tree) > ツリー編集(Edit Tree)画面】に設定されているインデックスツリーと同じに表示させる。
    - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに設定したインデックスをルートとしたインデックスツリーが表示される。
    - 任意のインデックスを選択するとインデックス配下のアイテムが「アイテムリスト」（Item list）エリアに表示される。
  - 「Fields For Update」エリア
    - 一括更新するメタデータ項目と更新内容を設定できる。
    - 一括更新対象のメタデータプルダウンリストは以下の項目とする。
      - Access Type
      - Licence
    - メタデータ項目を選択すると、該当設定オプションを表示する
      - Access Typeを選択すると、以下のオプションを表示する
        - 「オープンアクセス」（Open Access）
        - 「オープンアクセス日時」（Open Access Date）  
          選択すると、日時を設定できる。デフォルトはサーバから取得した日付（/api/admin/get_server_date）とする
        - 「ログインユーザのみ」（Login User Only）
      - Licenceを選択すると、ライセンスプルダウンリストを表示する。（アイテム登録画面に同じとする）
    - エリア右端に「×」ボタンが表示される。押下すると項目を削除できる。
      - 項目が一つだけの時、削除をすることはできない。
    - 複数項目を設定できるため、「フィールド追加」（Add Field）ボタンを設ける。
      - 押すと、更新内容の設定エリアを追加する。
    - メタデータプルダウンリストに同一項目を選択すると、選択不可とし、選択している項目が存在する旨のメッセージを表示する。  
      メッセージ：「Field already exists.」
  - 一括更新の対象アイテムの設定エリア
    - 「検索」（Search）エリア
      - 一括更新の対象アイテムを検索できる。
      - アイテム検索はWEKO3の詳細検索機能をそのまま利用する。
      - 最初に検索した時、「Item list」エリアの表示順設定は【設定>検索設定】画面のデフォルトソート条件(キーワード検索)に従う。
      - 検索するごとにチェックボックスは初期化される。
    - 「Index List」エリア
      - インデックスツリーからインデックスを選択した時に表示される。
      - パンくずリスト、RSSアイコン、サムネイル画像を表示する。
    - 「アイテムリスト」（Item list）エリア
      - デフォルトはすべてのアイテムを表示する。
      - アイテムリストの表示順と表示数はWEKO3のアイテムリストをそのまま利用する。初期表示は「ID asc」の組み合わせが表示されているが、実際にはアイテムリストは「Creator asc」の順番で表示がされる。
      - 一括更新の対象選択ができるため、各アイテムの行頭にチェックボックスを設ける。  
        また、アイテムリストの上部に「全選択」（Select All）リンクを設けて、リンクをクリックすると、すべての表示されているアイテムは一括更新の対象とする。
      - アイテムの詳細を確認できるため、各アイテムがリンク形式で表示されて、リンクをクリックすると、該当アイテム詳細画面に移動する。

- 一括更新を実行する
  - 一括更新の情報を設定してから、「更新」（Update）ボタンを押すと、事前確認できるため、更新内容を確認モーダルに表示する
  - 対象アイテムを選択しない状態で、「更新」（Update）ボタンを押すと  
    「Please select items to update.」
  - モーダルには以下を表示する
    - 「Item」：アイテムに登録しているファイル名
    - 「Before」
      - 「Access Type」：更新前のアクセスタイプ値
      - 「License」：更新前のライセンス値
    - 「After」
      - 「Access Type」：更新後のアクセスタイプ値
      - 「License」：更新後のライセンス値
    - 「Continue」ボタン  
      押すと、一括更新処理が行って、対応アイテムの情報とバージョンが更新される
    - 「閉じる」（Close）ボタン  
      押すと、モーダルを閉じる

## 関連モジュール

- weko_index_tree
- weko_records_ui

## 処理概要

一括更新画面表示について

- 【Administration > アイテム管理(Items) > 一括更新(Bulk Update)画面】を開いた際、以下の処理を実行する。
  - weko_index_tree.rest.IndexTreeActionResource.getメソッドを呼び出し、インデックスツリー情報を取得する。それらを「インデックスツリー」エリアに表示する。
  - weko_records_ui.admin.ItemManagementBulkUpdate.indexメソッドを呼び出す。詳細検索情報をget_search_detail_keywordメソッドで、一括更新対象の設定をWEKO_RECORDS_UI_BULK_UPDATE_FIELDSから (後述)、ライセンス情報をWEKO_RECORDS_UI_LICENSE_DICTから取得し、詳細検索情報と一括更新対象設定、ライセンス情報をそれぞれのエリアに表示する。

一括更新対象を設定する

- パス：  
  <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py>
- 設定キー：「WEKO_RECORDS_UI_BULK_UPDATE_FIELDS」
- 現在の設定値：

```python
WEKO_RECORDS_UI_BULK_UPDATE_FIELDS = {
    'fields': [{'id': '1', 'name': 'Access Type'},
               {'id': '2', 'name': 'Licence'}]
}
```

一括更新画面にてインデックス検索、詳細検索、簡易検索のいずれかを行う。

- weko_search_ui.rest.IndexSearchResource.getメソッドを呼び出し、検索条件にのっとったアイテムの情報を取得し、表示する。
- weko_search_ui.admin.ItemManagementBulkSearch.indexメソッドを呼び出し、様々な情報を取得し、画面に表示する。詳細は以下のgithubを参照すること。ソースコード：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/admin.py>

一括更新の実行

- 「Item list」エリアのチェックボックスにチェックを入れないで「更新ボタン」を押した場合、weko_records_ui.static.js.weko_records_ui.bulk_updateの135行目にてアラートが表示される処理が実行される。
- 更新をするアイテムにチェックを入れて「更新」ボタンを押下する。その場合、weko_records_ui.static.js.weko_records_ui.bulk_updateの121行目からが呼び出され、それにてget_items_metadataメソッドが呼び出され、アイテムに所属するファイルの情報を取得し、before,afterのポップアップ画面が表示される。
  - ポップアップ画面上の「閉じる」ボタンを押下すると、キャンセルされポップアップ画面は閉じる。
  - 「Continue」ボタンを押下した場合、weko_deposit.rest.publishメソッドが複数回呼ばれ、item_metadataテーブル、item_metadata_versionテーブル、records_metadataテーブルにそれぞれ更新内容を登録する。（アクセスタイプならキーaccessroleを、ライセンスならキーlicensetypeを変更して登録する。）

## 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2025/01/23|-|サブリポジトリ対応|
