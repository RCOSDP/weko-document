### オブジェクトバージョン

## 目的・用途

本機能は、管理者として、アップロードしているアイテムのファイルバージョンを管理する機能である。

## 利用方法

【Administration > ファイル管理(Files) > オブジェクトバージョン(Object Version)画面】を表示する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 【オブジェクトバージョン(Object Version)画面】には以下のタブが表示される
  - 一覧（List）
  - フィルターを追加▼（Add Filter▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 詳細（Details）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 詳細（Details）タブ選択中に表示

- 「一覧」（List）タブにアイテムにアップロードしているファイルバージョンを表示する。
  - 表示項目は以下の通りである
    - アクセス（閲覧）
      - 目のマークを押すと「詳細」タブに遷移する。
    - 「Bucket」：該当バケットのID値
    - 「Key」：ファイル名
    - 「Version」：ファイルのバージョン
    - 「URI」：ファイルのURI
    - 「Is Head」：True、False
      True：最終版の場合
    - 「Size」：ファイルの容量値
    - 「Created」：ファイルの作成時間
      フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」
    - 「Updated」：ファイルの更新時間
      フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」
    - 「Versions」リンク
      - リンクをクリックすると、該当オブジェクトバージョンがフィルターされる。
      - フィルター条件：
        - 「bucket / Files Bucket / Id」：該当のバケット値
        - 「key」：該当のファイル名
    - 「Objects」リンク
      - リンクをクリックすると、該当オブジェクトバージョンがフィルターされる。
      - フィルター条件：
        - 「bucket / Files Bucket / Id」：該当のバケット値
        - 「Is Head」：Yes
    - 「File」リンク
      - リンクをクリックすると、【Administration > ファイル管理(Files) > ファイルインスタンス(File Instance)画面】に移動し、該当ファイルがフィルターされる。
      - フィルター条件：「ID」：該当ファイルID

  - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する。
    - フィルター名
      - 「bucket / Files Bucket / Id」
        - フィルター方式の選択肢：等しい（equals）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「bucket / Files Bucket / Locked」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「bucket / Files Bucket / Deleted」
        - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「bucket / Files Bucket / Name」
        - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「File UUID」
        - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Checksum」
        - フィルター方式の選択肢：「bucket / Files Bucket / Name」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Storage Class」
        - フィルター方式の選択肢：「bucket / Files Bucket / Name」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Readable」
        - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Key」
        - フィルター方式の選択肢：「bucket / Files Bucket / Name」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Version」
        - フィルター方式の選択肢：「bucket / Files Bucket / Id」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Is Head」
        - フィルター方式の選択肢：「bucket / Files Bucket / Locked」と同じである。
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Size」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Created」
        - フィルター方式の選択肢：「Size」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Updated」
        - フィルター方式の選択肢：「Size」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
    - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される。
    - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる。

  - 検索テキストボックスで検索する
    プレースホルダー：「Search: key」
    - 任意テキストを入力し、キーボードでの「Enter」を押すと、部分一致検索を行う。
    - テキストボックスの右端での「X」ボタンを押すと、検索条件がクリアーされる。

  - 左端行の目アイコンを押すと、該当オブジェクトバージョンの詳細情報を「詳細」（Details）タブに表示する。
    - 表示項目：Bucket、Key、Version、File UUID、URI、Checksum、Size、Storage class、Is Head、Deleted、Created、Updated、File、Versions
    - 「File」リンクをクリックすると、【Administration > ファイル管理(Files) > ファイルインスタンス(File Instance)画面】に移動し、該当ファイルがフィルターされる。
    - 「Versions」リンクをクリックすると、該当オブジェクトバージョンがフィルターされる。

## 関連モジュール

- invenio-files-rest
- flask-admin: <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

## 処理概要

オブジェクトバージョン画面の処理について

- オブジェクトバージョン画面を表示する。この操作によって、invenio_files_rest.admin.ObjectModelViewが継承したModelViewよりflask_admin.model.base.index_viewメソッドを呼び出す。このメソッドでfiles_objectテーブルよりバケット情報を取得し、ObjectModelViewのcolumn_listにあるキーに対応する情報を画面に表示する。
  - オブジェクトバージョン詳細画面を表示する。この操作によって、invenio_files_rest.admin.ObjectModelViewが継承したModelViewよりflask_admin.model.base.details_viewメソッドを呼び出す。このメソッド下でfiles_objectテーブルよりオブジェクトバージョン情報を取得し、ObjectModelViewのcolumn_details_listにあるキーに対応する情報を画面に表示する。

オブジェクトバージョンの情報は以下のようなデータベースに保存する

- テーブル名：「files_object」
- フィールド名：
  ・「version_id」
  ・「key」
  ・「bucket_id」
  ・「file_id」
  ・「root_file_id」
  ・「_mimetype」
  ・「is_head」
  ・「created_user_id」
  ・「updated_user_id」
  ・「bucket」
  ・「is_show」
  ・「is_thumbnail」
  ・「created」
  ・「updated」

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
