# アイテム表示

## 目的・用途

本機能は、アイテム表示・検索に関する設定機能である

## 利用方法

【Administration > Setting (設定) > Item (アイテム表示)】からアイテム表示における条件の設定を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | | | | |

## 機能内容

使用している画面

- 【Administration > Setting (設定) > Items（アイテム表示）画面】アイテム表示・検索に関する機能を設定する画面である

E-mailの表示/非表示を設定する

- 【Administration > Setting (設定) > Items (アイテム表示) 画面】の「Display Email」エリアにてE-Mailの表示（Display Email ）/非表示（Hide Email）を設定することができる。本設定によりアイテム詳細画面、ADMIN14-4 PDFカバーページ および <https://redmine.devops.rcos.nii.ac.jp/projects/weko-dev-doc/wiki/JSON>USER3-7 Export(JSON) 機能 におけるE-Mail出力を制御する。
  - Display Email が設定されている場合、アイテム詳細画面、PDFカバーページおよびJSON Export機能にてメールアドレスを表示する。
  - Hide Email が設定されている場合、アイテム詳細画面、PDFカバーページおよびJSON Export機能にてメールアドレスを表示しない。
  - 「保存」（Save）ボタンを押すと、設定内容を保存する

- 【Administration > Setting (設定)> Items(アイテム表示) 画面】でのOpen Dateエリアにファイルの公開日の表示/非表示を設定する
  - 「表示」（Display）を設定する場合、すべてのユーザにはアイテムリスト、アイテム詳細画面に公開日を表示とする
  - 「非表示」（Hide Open Date）を設定する場合、ゲストユーザにはアイテムリスト、アイテム詳細画面に公開日を非表示とする
  - デフォルト：「表示」（Display）
  - 「保存」（Save）ボタンを押すと、設定内容を保存する

## 関連モジュール

- weko-records-ui

## 処理概要

- 【Save (保存)】を押下した際に、weko_records_ui.admin.ItemSettingView.indexを呼び出して使用する。
  - weko_admin.models.AdminSettingsを呼び出し、admin_settingsテーブルを更新する。

- weko-records-ui.utils.is_show_email_of_creator
  - <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/utils.py#L578-L624>
  - 当該アイテムタイプについて、E-Mail表示する場合はTrueを返す。

- ファイルの公開日の表示/非表示を設定する
  - デフォルト状態の設定：
    - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L68>
    - 設定キー： OPEN_DATE_DISPLAY_FLG
    - 現在の設定値：
      - OPEN_DATE_DISPLAY_FLG = True

- 表示/非表示状態の値を設定する
  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L69-L70>
  - 設定キー：OPEN_DATE_DISPLAY_VALUE、OPEN_DATE_HIDE_VALUE
  - 現在の設定値：
    - OPEN_DATE_DISPLAY_VALUE = '1'
    - OPEN_DATE_HIDE_VALUE = '0'

- E-mailの表示/非表示を設定する
  - デフォルト状態の設定：
    - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L65>
    - 設定キー： EMAIL_DISPLAY_FLG
    - 現在の設定値：
      - EMAIL_DISPLAY_FLG = True

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_records_ui.admin.ItemSettingView.index`（GET/POST）。保存先は `AdminSettings`（name=`items_display_settings`、サブキー `items_display_email` / `item_display_open_date`）。メール表示判定は `weko_records_ui.utils.is_show_email_of_creator`。config：`EMAIL_DISPLAY_FLG` / `OPEN_DATE_DISPLAY_FLG` / `OPEN_DATE_DISPLAY_VALUE` / `OPEN_DATE_HIDE_VALUE`。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
