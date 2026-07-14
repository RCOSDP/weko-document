### ファイルインスタンス

## 目的・用途

本機能は、管理者として、アップロードしているファイルを管理する機能である

## 利用方法

【Administration > ファイル管理（Files） > ファイルインスタンス（File Instance）画面】からファイルインスタンスを表示する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 【ファイルインスタンス(File Instance)画面】には以下のタブが表示される
  - 一覧（List）
  - フィルターを追加▼（Add Filter▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 選択▼（With selected▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 詳細（Details）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 詳細（Details）タブ選択中に表示

- 「一覧」（List）タブにアップロードしているファイルを表示する
  - 表示項目は以下の通りである
    - チェックボックス
    - アクション（閲覧）
    - 「ID」：ファイルのID
    - 「URI」：ファイルのURI
      「Location」画面に設定している配置先を元に、ファイルのURIを指定する
      押下すると一覧のロケーションをソートする。
    - 「Storage Class」：S（Standard）、A（Archive）
      押下すると一覧のロケーションをソートする。
    - 「Size」：ファイルの容量値
      押下すると一覧のロケーションをソートする。
    - 「Checksum」
      押下すると一覧のロケーションをソートする。
    - 「Readable」
      押下すると一覧のロケーションをソートする。
    - 「Writable」
      押下すると一覧のロケーションをソートする。
    - 「Fixity」
      押下すると一覧のロケーションをソートする。
    - 「Checked」
      押下すると一覧のロケーションをソートする。
    - 「Created」
      フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」
      押下すると一覧のロケーションをソートする。
    - 「Updated」
      フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」
      押下すると一覧のロケーションをソートする。
    - 「Objects」リンク
      リンクをクリックすると、【Administration > ファイル管理（Files）> オブジェクトバージョン（Object Version）画面】に移動し、該当オブジェクトバージョンがフィルターされる

  - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する
    - フィルター名
      - 「ID」
        - フィルター方式の：等しい（equals）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「URI」
        - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Storage Class」
        - フィルター方式の選択肢：「URI」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Size」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Checksum」
        - フィルター方式の選択肢：「URI」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Readable」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Writable」
        - フィルター方式の選択肢：「Readable」と同じである
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Fixity」
        - フィルター方式の選択肢：「Readable」と同じである
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Checked」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Created」
        - フィルター方式の選択肢：「Checked」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Updated」
        - フィルター方式の選択肢：「Checked」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Created」
        - フィルター方式の選択肢：「Checked」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Updated」
        - フィルター方式の選択肢：「Checked」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Key」
        - フィルター方式の選択肢：「URI」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object /Root File id」
        - フィルター方式の選択肢：「ID」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Mimetype」
        - フィルター方式の選択肢：「URI」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Is Head」
        - フィルター方式の選択肢：「Readable」と同じである
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Files Object / Created User Id」
        - フィルター方式の選択肢：「Size」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Updated User Id」
        - フィルター方式の選択肢：「Size」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Files Object / Is Show」
        - フィルター方式の選択肢：「Readable」と同じである
        - 選択したフィルター方式に対して「はい」「いいえ」
      - 「Files Object / Is Thumbail」
        - フィルター方式の選択肢：「Readable」と同じである
        - 選択したフィルター方式に対して「はい」「いいえ」
    - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される
    - 「フィルターをリセット」（Reset Filters）ボタンを押下すると、設定したフィルターがリセットされる

  - 「選択▼」（With selected▼）ボタンをクリックすると、以下の追加可能な機能を表示する
    機能：「Run fixity check」
    - レコードにチェックを入れない場合、「Run fixity check」ボタンを押すと、エラーメッセージを表示する
      メッセージ：
      　日本語：「少なくとも一つのレコードを選択してください。」
      　英語：「Please select at least one record.」
    - レコードにチェックを入れる場合、「Run fixity check」ボタンを押すと、「checksum」値の確認を行う
      - 表示している「checksum」値が実際の「checksum」値と一致する場合
        - 以下のメッセージを画面上部に表示する
          メッセージ：「Fixity check(s) sent to queue.」
        - 実行の時間を「Checked」に更新する
      - 表示している「checksum」値が実際の「checksum」値と一致しない場合
        - 表示している「checksum」値が空白になる
        - 実行の時間を「Checked」に更新する

  - 検索テキストボックスでユーザーを検索する
    プレースホルダー：「Search: URI, size, checksum」
    - 任意テキストを入力し、キーボードでの「Enter」を押すと、ファイルインスタンス検索を行う
    - テキストボックスの右端での「X」ボタンを押すと、検索条件がクリアーされる

  - ファイルインスタンス左端の行の目アイコンを押すと、該当ファイルインスタンスの詳細情報を「詳細」（Details）タブに表示する
    - 表示項目：ID、URIl、Storage Class、Size、Checksum、Readable、Writable、Fixity、Checked、Created、Updated、Objects
    - 「Objects」リンクをクリックすると、【Administration > Files (ファイル管理)> Object Version(オブジェクトバージョン)画面】に移動し、該当オブジェクトバージョンがフィルターされる

## 関連モジュール

- invenio-files-rest

## 処理概要

ファイルインスタンス画面の処理について

- ファイルインスタンス画面を表示すると、invenio_files_rest.admin.FileInstanceModelViewが継承したModelViewのBaseModelViewより、flask_admin.model.base.BaseModelView.index_viewを呼び出す。このメソッドでfiles_filesテーブルからバケット情報を取得し、FileInstanceModelView.column_listのキーに対応する情報を表示する。
  - ファイルインスタンス詳細画面を表示する。invenio_files_rest.admin.FileInstanceModelViewが継承したModelViewのBaseModelViewよりflask_admin.model.base.BaseModelView.details_viewを呼び出す。このメソッド下でfiles_filesテーブルよりバケット情報を取得し、FileInstancetModelViewのcolumn_details_listのキーに対応する情報をdetailsタブ画面に表示する。

ファイルインスタンスを選択し、【With Selected (選択)】から【Run fixity check】を押下する。invenio_files_rest.admin.FileInstanceModelViewが継承したModelViewのBaseModelViewより、flask_admin.model.base.BaseModelView.action_viewを呼び出して使用する。invenio_files_rest.admin.FileInstanceModelView.action_verify_checksumを呼び出す。このメソッド下でinvenio_files_rest.tasks.verify_checksumを呼び出してfiles_filesテーブルのchecksumの値を確認し、last_check_atカラムを更新し、ファイルインスタンス画面のcheckedの欄に実行時間を表示する。

バケット情報を以下のようなデータベースに保存する

- テーブル名：「files_files」
- フィールド名：
  ・「id」
  ・「uri」
  ・「storage_class」
  ・「size」
  ・「checksum」
  ・「readable」
  ・「writable」
  ・「last_check_at」
  ・「last_check」
  ・「created」
  ・「updated」

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_files_rest.admin.FileInstanceModelView`（テーブル `files_files`、endpoint `fileinstance`）。`can_create/can_edit/can_delete=False`・`can_view_details=True`（閲覧のみ）。`@action('verify_checksum')` → `verify_checksum.delay(file_id)`（「Fixity check(s) sent to queue.」）。チェック不一致時は `last_check=False`（Fixity フラグ）を設定。
- 実装補足：詳細に表示される多数の「Files Object / …」フィルタは `column_filters` に `objects`（リレーション）を含めたことによる展開。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
