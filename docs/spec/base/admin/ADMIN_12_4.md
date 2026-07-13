### マルチパートオブジェクト

## 目的・用途

本機能は、マルチパートアップロードが使用されているオブジェクトを閲覧する機能である。

※invenioデフォルト機能を使用

## 利用方法

【Administration > ファイル管理(Files) > マルチパートオブジェクト(Multipart Object)画面】を表示する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | | | | |

## 機能内容

- 【マルチパートオブジェクト(Multipart Object)画面】には以下のタブが表示される
  - 一覧（List）
  - フィルターを追加▼（Add Filter▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 詳細（Details）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 詳細（Details）タブ選択中に表示

- 「一覧」（List）タブにマルチパートオブジェクト一覧を表示する。
  - 表示項目は以下の通りである。
    - アクセス（閲覧）
      - 目のマークを押すと「詳細」タブに遷移する。
    - 「Upload Id」
    - 「Complete」
    - 「Created」：アイテムの登録時間
      フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
    - 「Updated」アイテムの編集時間
      フォーマット：YYYY-MM-DDThh:mm:ss.tttttt
    - 「File」リンク
      - リンクをクリックすると、【Administration > ファイル管理(Files) > ファイルインスタンス(File Instance)画面】に移動し、該当ファイルがフィルターされる。
      - フィルター条件：「ID」：該当ファイルID

  - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する。
    - フィルター名
      - 「Upload Id」
        - フィルター方式の選択肢：等しい(equals)
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「completed」
        - フィルター方式の選択肢：等しい(equals)、等しくない(not equal)
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Created」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Updated」
        - フィルター方式の選択肢：「Created」と同じである。
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
    - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される。
    - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる。

  - 左端の目アイコンを押すと、該当マルチパートオブジェクトの詳細情報を「詳細」（Details）タブに表示する
    - 表示項目は一覧タブで表示されたものと同じである（Upload Id、Complete、Created、Updated、File）。

  - 本画面には編集・作成・削除の機能はない。

## 関連モジュール

- invenio_files_rest
- flask-admin: <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

## 処理概要

マルチパートオブジェクト画面の処理について

- マルチパートオブジェクト画面を表示する。この操作によって、invenio_files_rest.admin.MultipartObjectModelViewが継承したModelViewよりflask_admin.model.base.index_viewメソッドを呼び出す。このメソッドでfiles_multipartobjectテーブルよりマルチパートオブジェクト情報を取得し、MultipartObjectModelViewのcolumn_listにあるキーに対応する情報を画面に表示する。
  - マルチパートオブジェクト詳細画面を表示する。この操作によって、invenio_files_rest.admin.MultipartObjectModelViewが継承したModelViewよりflask_admin.model.base.details_viewメソッドを呼び出す。このメソッド下でfiles_multipartobjectテーブルよりマルチパートオブジェクト情報を取得し、MultipartObjectModelViewのcolumn_details_listにあるキーに対応する情報を画面に表示する。

マルチパートオブジェクトの情報は以下のようなデータベースに保存する

- テーブル名：「files_multipartobject」
- フィールド名：
  ・「created」
  ・「updated」
  ・「upload_id」
  ・「bucket_id」
  ・「key」
  ・「file_id」
  ・「chunk_size」
  ・「size」
  ・「completed」

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2023/12/22 | 4ec162bf3bdcf843df23863fbf7d5bb36ba875e4 | W2023-42 |
