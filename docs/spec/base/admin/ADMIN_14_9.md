# アイテム一括出力

## 目的・用途

この機能は、USER-2-4の機能であるアイテム一括出力の可否を設定するものである。

## 利用方法

【Administration > 設定(Setting) > アイテム一括出力(Item Export)画面】を開き、設定後「保存」ボタンを押下する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

- 【Administration > 設定(Setting) > アイテム一括出力(Item Export)画面】にアイテムの一括出力を設定する。
  - アイテムの一括出力可否（Allow/Disallow Item Exporting）
    　アイテムの一括出力の機能を「設定する／設定しない」を設定する。
    - オン(On)：アイテム一括出力の機能を有効にする。
    - オフ(Off)：アイテム一括出力の機能を無効にする。
  - コンテンツファイルの出力可否（Export File Contents）
    　アイテムの一括出力をする際に、コンテンツファイルを含めて「出力する／出力しない」を設定する。
    - オン(On)：コンテンツファイルを含めて出力するように設定する。
    - オフ(Off)：コンテンツファイルは含めずに出力するように設定する。
  - 一括出力できる最大アイテム数はconfigで設定する。デフォルトは最大100件とする。
  - 「保存」（Save）ボタンを押すと、設定情報をデータベースに格納する。

- アイテム一括出力の仕方の詳細は[USER-2-4アイテム一括出力](../user/USER_2_4.md)を参照すること。

## 関連モジュール

- weko_admin

## 処理概要

アイテム一括出力画面の表示

- 【Administration > 設定 > アイテム一括出力】画面を開く。この操作によって、weko_admin.admin.ItemExportSettingsView.indexメソッドがGETで呼び出され、_get_current_settingsメソッドでadmin_settingsテーブルのキーitem_export_settingsより現在の設定を取得後画面に表示する。

アイテム一括出力の設定

- 任意の設定をした後、「保存」ボタンを押下する。この操作によって、weko_admin.admin.ItemExportSettingsView.indexメソッドがPUTで呼び出され、AdminSettings.updateでadmin_settingsテーブルのキーitem_export_settingsに設定が保存される。そして、更新された設定と"Successfully Changed Settings"を画面に表示する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_admin.admin.ItemExportSettingsView.index`（GET/POST）。保存先は `AdminSettings`（name=`item_export_settings`、`{'allow_item_exporting': bool, 'enable_contents_exporting': bool}`）。既定 `WEKO_ADMIN_DEFAULT_ITEM_EXPORT_SETTINGS`。最大出力件数は `weko_items_ui.config.WEKO_ITEMS_UI_DEFAULT_MAX_EXPORT_NUM`（既定100、ロール別上限 `WEKO_ITEMS_UI_MAX_EXPORT_NUM_PER_ROLE`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
