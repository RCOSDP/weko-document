### バケット

## 目的・用途

本機能は、コンテンツファイルを登録しているアイテムのバケットを閲覧、編集、作成する機能である

## 利用方法

【Administration > ファイル管理(Files) > バケット(Bucket)画面】を表示する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 【バケット(Bucket)画面】には以下のタブが表示される
  - 一覧（List）
  - 作成（Create）
  - フィルターを追加▼（Add Filter▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 選択▼（With selected▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 編集（Edit）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
  - 詳細（Details）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

- 「一覧」（List）タブにバケット一覧を表示する。
  - 表示項目は以下の通りである。
    - アクセス（閲覧・編集）
      - 目のマークを押すと「詳細」タブに遷移する。
      - 鉛筆のマークを押すと「編集」タブに遷移する。
    - 「UUID」：バケットのID
    - 「Location」：バケットの設定場所
    - 「Default Storage Class」：S（Standard）、A（Archive）
      デフォルト値：「S」
    - 「Deleted」
    - 「Locked」
    - 「Size」：アップロードされたファイルの容量
    - 「Quota Size」：アップロード可能容量
    - 「Created」：アイテムの登録時間
      フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
    - 「Updated」アイテムの編集時間
      フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
    - 「Objects」リンク
      「Objects」リンクを押すと、【Administration > ファイル管理(Files) > オブジェクトバージョン(Object Version)画面】に移動し、該当オブジェクトがフィルターされる。

  - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する。
    - フィルター名
      - 「location / Files Location / Name」
        - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Default Storage Class」
        - フィルター方式の選択肢：「location / Files Location / Name」の同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Deleted」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Locked」
        - フィルター方式の選択肢：「Deleted」の同じである
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Size」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Created」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Updated」
        - フィルター方式の選択肢：「Created」の同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
    - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される。
    - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる。

  - 左端行の目アイコンを押すと、該当バケットの詳細情報を「詳細」（Details）タブに表示する。
    - 表示項目：UUID、Location、Default Storage Class、Deleted、Locked、Size、Quota Size、Max File Size、Created、Updated、Objects、Object Versions
    - 「Objects」リンクをクリックすると、【Administration > ファイル管理(Files) > オブジェクトバージョン(Object Version)画面】に移動し、該当オブジェクトがフィルターされる。
    - 「Object Versions」リンクをクリックすると、【Admin > Files > Object Version画面】に移動し、該当オブジェクトバージョンがフィルターされる。

  - 左端行の鉛筆アイコンを押すと、「編集」（Edit）タブに表示し、ユーザーの情報が編集できる。
    - 編集可能な項目は以下の通りである。
      - 「Default Storage Class」
        選択肢：Standard、Archive
      - 「Locked」
      - 「Deleted」
      - 「Quota Size」：整数のみ入力可
      - 「Max File Size」：整数のみ入力可
    - 「保存」（Save）ボタンを押すと、編集内容を保存し、メッセージを一覧画面の上部に表示する。
      メッセージ：
      　日本語：「レコードが正常に保存されました。」
      　英語：「Record was successfully saved.」

- 「作成」タブの機能は存在するが、現在画面上にロケーションを選択する欄がなく、「保存」ボタンを押下すると、エラーが出る。(v0.9.22)

## 関連モジュール

- invenio-files-rest
- flask-admin: <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

## 処理概要

- バケット画面の処理について
  - バケット画面を表示する。この操作によって、invenio_files_rest.admin.BucketModelViewが継承したModelViewよりflask_admin.model.base.index_viewメソッドを呼び出す。このメソッドでfiles_bucketテーブルよりバケット情報を取得し、BucketModelViewのcolumn_listにあるキーに対応する情報を画面に表示する。
    - バケット詳細画面を表示する。この操作によって、invenio_files_rest.admin.BucketModelViewが継承したModelViewよりflask_admin.model.base.details_viewメソッドを呼び出す。このメソッド下でfiles_bucketテーブルよりバケット情報を取得し、BucketModelViewのcolumn_details_listにあるキーに対応する情報を画面に表示する。
  - バケット編集画面を表示する。この操作によって、invenio_files_rest.admin.BucketModelViewが継承したModelViewよりflask_admin.model.base.edit_viewメソッドをGETで呼び出す。このメソッド下で開いたid列を用いて、files_bucketテーブルよりバケット情報を取得し、表示する。
    - バケット編集画面で「保存」ボタンを押下する。この操作によって、flask_admin.model.base.edit_viewメソッドをPOSTで呼び出す。このメソッド下で、get_save_return_urlメソッドが呼ばれ、編集内容をfiles_bucketテーブルに保存し、更新する。
  - バケット作成画面を開いたとき、invenio_files_rest.admin.BucketModelViewが継承したModelViewよりflask_admin.model.base.create_viewメソッドをGETで呼び出す。BucketModelViewクラスのform_columnsの項目の入力欄を表示する。
    - 入力欄に入力後「保存」ボタンを押下する。この操作によって、invenio_files_rest.admin.BucketModelViewが継承したModelViewよりflask_admin.model.base.create_viewメソッドをPOSTで呼び出す。このメソッド下でget_save_return_urlメソッドが呼ばれ、新しいバケットの情報をfiles_bucketテーブルに保存する。

- バケット情報は以下のようなデータベースに保存する。
  - テーブル名：「files_bucket」
  - フィールド名：
    ・「created」
    ・「updated」
    ・「id」
    ・「default_location」
    ・「default_storage_class」
    ・「size」
    ・「quota_size」
    ・「max_file_size」
    ・「locked」
    ・「deleted」

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_files_rest.admin.BucketModelView`（テーブル `files_bucket`、endpoint `bucket`）。`can_create=True` / `can_edit=True` / `can_delete=False` / `can_view_details=True`。`form_columns` に Location フィールドが無いため作成タブからの新規作成は成立しない（既知）。
- 実装補足：`default_storage_class` の選択肢は config `FILES_REST_STORAGE_CLASS_LIST`（`{'S':'Standard','A':'Archive'}`）、既定 `FILES_REST_DEFAULT_STORAGE_CLASS`（`S`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
