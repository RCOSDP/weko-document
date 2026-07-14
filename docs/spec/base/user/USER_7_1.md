### ファイルアップロード

#### 目的・用途

大容量データを安定的にWEKO3へアップロードする

#### 利用方法

ユーザ画面のLarge File Uploadタブからファイルをアップロードする。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | ○ |  |  |

#### 機能内容

- 大容量のファイルアップロードを行う。

- 大容量ファイルアップロード失敗した場合のレジュームアップロードを行う。

- レジュームアップロードのため、ログインユーザ自身がアップロードしたファイルの履歴を確認できる

#### 関連モジュール

- invenio-files-rest

#### 処理概要

- 下記をJavaScriptから行うことでファイルアップロード・レジュームアップロードを実現する。

- 新規アップロードの場合

  - files_filesレコードを作成し、FileInstanceのUUIDを取得する

  - ObjectStorageへマルチパートアップロードの初期化APIをリクエストし、upload_idを取得する

  - upload_id, file_idでfiles_multipartobjectレコードを追加する

- レジュームアップロードの場合、upload_idが正しい形式、有効かを検証する

  その後、新規アップロード・レジュームアップロード共通で下記を行う

  - ファイルをパートごとに分割し、files_multipartobject_partにすでにレコードが存在し、パートのハッシュ値を比較する

  - files_multipartobject_partにレコードが存在しない場合、ObjectStorageにパートをアップロードし、files_multipartobject_partにレコードを追加する

- すべてのパートをアップロードし終えたら、ObjectStorageへマルチパートアップロードの完了APIをリクエストし、files_multipartobjectレコードとfiles_filesレコードを更新する

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足（訂正）：大容量（マルチパート）アップロードは weko-items-ui のタブ機能ではなく、**invenio-files-rest** のマルチパートREST（`ObjectResource` の `multipart_init`/`multipart_uploadpart`/`multipart_complete` 等）を、投稿フォームUI（ng-file-upload / weko-deposit）が駆動する。`weko_items_ui.views.index_upload`（`/items/upload`）はメタデータ一括インポート画面で大容量アップローダではない。モデル `FileInstance`/`MultipartObject`/`Part`、config `FILES_REST_MULTIPART_*`、完了タスク `merge_multipartobject`。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/12/22 | 4ec162bf3bdcf843df23863fbf7d5bb36ba875e4 | W2023-42 |
