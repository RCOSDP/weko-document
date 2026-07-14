### レコードメタデータ

## 目的・用途

本機能は、レコードメタデータの閲覧、削除、復元の際に用いる機能である

## 利用方法

【Administration > レコード管理（Records） > レコードメタデータ（Record Metadata）画面】にて操作を行う

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 【レコードメタデータ（Record Metadata）画面】には以下のタブが表示される
  - 一覧（List）
    - このタブの表示中のみ、タブ名の末尾に件数が表示される
  - フィルターを追加▼（Add Filter▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 選択▼（With selected▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 詳細（Details）
    - 一覧（List）タブ選択中は非表示一覧（List）タブでの操作によって表示される

- 「一覧」（List）タブにてレコードメタデータを一覧表示する
  - 表示項目は以下のとおりである
    - アクション（閲覧・削除を表すアイコン）
    - UUID
    - Status
    - Revision
    - Updated
    - Created
  - 「フィルターを追加▼」（Add Filter▼）タブをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する
    - フィルター名は以下の通りである
      - Created
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - Updated
        - フィルター方式の選択肢：上記のCreatedと同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
    - 設定したフィルターは［適用（Apply）］ボタンを押下することで一覧に適用される
    - ［フィルターをリセット（Reset filter）］ボタンを押下すると、設定したフィルターがリセットされる
  - 「選択▼」（With selected▼）タブをクリックすると、以下の追加可能な機能（現在削除ボタンのみ）を表示する
    - レコードにチェックを入れない場合、［削除（Delete）］ボタンを押すと、エラーメッセージを表示する  
      メッセージ：  
      　日本語：「少なくとも1つのレコードを選択してください。」  
      　英語：「Please select at least one record.」
    - レコードにチェックを入れる場合、［削除（Delete）］ボタンを押すと、確認ダイアログを表示する  
      メッセージ：  
      　日本語：「選択したレコードを削除してもよろしいですか。」  
      　英語：「Are you sure you want to delete selected records?」
      - ［OK］ボタンを押すと、該当レコードメタデータを削除状態に変更し、メッセージを画面上部に表示する  
        メッセージ：  
        　日本語：「レコード数＋レコードが正常に削除されました。」  
        　英語：「Record was successfully deleted.」
      - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
    - この操作を行ったレコードは、詳細（Details）タブを表示するとJSONが「null」に変化している
      - 一覧（List）タブでも詳細（Details）タブでもStatusは変化しない
  - レコードメタデータ行にて目アイコンを押すと、該当レコードメタデータの詳細情報を詳細（Details）タブに表示する
  - レコードメタデータ行にてごみ箱アイコンを押すと、該当レコードメタデータを物理削除し、メッセージを画面上部に表示する  
    メッセージ：  
    　日本語：「レコード数＋レコードが正常に削除されました。」  
    　英語：「Record was successfully deleted.」

- 詳細（Details）タブでは、該当レコードメタデータの詳細情報を表示する
  - 表示項目：UUID、Status、Revision、Updated、Created、JSON
  - ［削除（Delete）］ボタンは以下のようにふるまう
    - このボタンは、StatusがDELETED以外のときに押すことができる
    - このボタンを押すと、該当レコードメタデータを論理削除する
      - 対象がロックされている場合は削除されず、code=-1・is_locked=Trueが返る
  - ［復元（Restore）］ボタンは以下のようにふるまう
    - このボタンは、StatusがDELETEDのときに押すことができる
    - このボタンを押すと、該当レコードメタデータを復元する

## 関連モジュール

- invenio_records：画面を定義
- weko_records_ui：soft_delete処理と復元処理（`weko_records_ui.utils`）を定義

## 処理概要

- 本画面は、flaskのModelViewでrecords_metadataテーブルの内容を閲覧、編集、削除する際に用いる機能である
- 画面で表示されるstatusはテーブルに含まれない項目で、情報取得時にpidstore_pidテーブルから以下の条件を満たすレコードのstatusを取得している
  - pid_typeが「recid」
  - object_uuidがrecords_metadataテーブルでのidと一致する
- 詳細（Details）タブでの操作は、以下のように処理される
  - ［削除（Delete）］ボタンを押したときには'/soft_delete/<string:id>'の形で、［復元（Restore）］ボタンを押したときには'/restore/<string:id>'の形でリクエストのURLを作成する
    - ［削除（Delete）］ボタンではweko_records_ui.utils.soft_delete関数、［復元（Restore）］ボタンではweko_records_ui.utils.restore関数が呼び出される
    - 対象レコードがロックされている場合は、削除されずにcode=-1・is_locked=Trueが返る
- 一覧（List）タブにて、レコードをチェックして「選択▼」（With selected▼）タブの［削除（Delete）］ボタンを押すと、チェックしたレコードごとにinvenio_records.admin.RecordMetadataModelView.delete_modelメソッドが呼び出される
  - 該当レコードのJSONが「null」だった場合は処理を終了する
  - invenio_records.api Record.deleteメソッドによって、該当レコードのJSONを「null」にする

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_records.admin.RecordMetadataModelView`（テーブル `records_metadata`、`record_adminview`、カテゴリ Records）。`can_create=False` / `can_edit=False` / `can_delete=True` / `can_view_details=True`。`status` は `PersistentIdentifier`（pid_type='recid'）を参照する hybrid property。
- 実装補足：論理削除・復元は **`weko_records_ui.utils`** の `soft_delete` / `restore` を呼ぶ。ロック時は `code=-1, is_locked=True` を返す。`delete_model` は `json is None` を早期 return、それ以外は `Record.delete()`（`json=None` 化のソフト削除）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
