# プロフィール表示設定

## 目的・用途

本機能は、プロフィール画面にて表示される項目の表示・非表示、ラベル名、入力方式を設定する機能である。

## 利用方法

【Administration＞アドバンスド（Advanced）＞プロフィール表示設定（Profile Settings）】の順で画面へ遷移して利用する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

保存APIは `@roles_required(['System Administrator', 'Repository Administrator'])` で保護される。画面表示は Flask-Admin の標準管理者アクセス制御に従う。

## 機能内容

- 各項目で表示・非表示の設定
  - 各項目に設置されている表示フラグ（visible）のチェックボックスにチェックが入った状態で保存することで、プロフィール画面に表示される。
    - 表示フラグがOFFの項目は自動入力機能の対象外となる（ただし後述の `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` が True の場合）。

- 各項目でラベル名の編集
  - 各項目のラベル名テキストボックスを編集することで、ラベル名を変更でき、プロフィール編集画面に反映される。

- 各項目の入力方式の編集
  - 各項目の入力方式プルダウンで入力方式を変更できる。入力方式は `USERPROFILES_FORMAT_OPTION_LIST` により `text` / `select` / `identifier` / `phonenumber` / `position(other)` の5種類。`select` を選択した場合、項目下部にオプション記入テキストボックスが表示されるので記入する。

- 自動入力機能への項目反映
  - `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` が True の場合、表示フラグ（visible）がONの項目のみを自動入力の対象とし、OFFの項目は対象外とする。既定（False）では全項目が従来通り自動入力に用いられる。

## 関連モジュール

- weko-admin（設定画面・保存処理の実体：`ProfileSettingView`、保存API `send_profile_settings_save`、React画面 `user-profile-settings.js`）
- weko-user-profiles（設定値の消費側：プロフィールフォーム生成 `forms.py`、自動入力データ生成 `utils.py` の `get_user_profile_info` / `models.py` の `get_institute_data`、デフォルト設定値の定義 `config.py`）
- weko-workflow / weko-workspace（自動入力でプロフィール情報を利用する呼び出し元）

## 設定の格納・デフォルト

- 設定は `AdminSettings` テーブルの name=`profiles_items_settings`（JSON）に格納される。
- デフォルト値は `weko-user-profiles/weko_user_profiles/config.py` の `WEKO_USERPROFILES_DEFAULT_FIELDS_SETTINGS`（対象：fullname / university / department / position / item1〜item16）。
- 各項目の構造：`{order:int, visible:bool, label_name:str, format:str, options:list}`

## 主要設定値（config）

| キー | 既定値 | 用途 |
| --- | --- | --- |
| `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` | False | プロフィール表示設定（visible／label／format）の有効化スイッチ。False（既定）では表示制御・自動入力対象制御が効かず全項目が従来通り出力される |
| `USERPROFILES_FORMAT_OPTION_LIST` | `['text','select','identifier','phonenumber','position(other)']` | 入力方式の選択肢 |
| `WEKO_USERPROFILES_DEFAULT_FIELDS_SETTINGS` | （項目デフォルト定義） | 設定の初期値 |
| `WEKO_ADMIN_PROFILE_SETTING_TEMPLATE` | `'weko_admin/admin/profiles_settings.html'` | 画面テンプレート |

## 処理概要

- プロフィール表示設定画面 初期表示（`ProfileSettingView.index`、`GET /admin/profile_settings/`）
  - `AdminSettings` の `profiles_items_settings`（無ければデフォルト）を画面に渡し、React（`ProfilesList`／`user-profile-settings.js`）で order 順に描画する。
  - 各項目の項目名（固定キー、表示のみ）、表示フラグ（チェックボックス）、ラベル名（テキスト）、入力方式（プルダウン）を表示する。
    - 入力方式で `select` を選択した場合、オプション記入ボックスを表示する。プレースホルダ文言は英語固定「separate option with the | character」（`user-profile-settings.js` にハードコードされておりi18n化されていない）。

- 設定内容を保存（`send_profile_settings_save`、`POST /api/admin/profile_settings/save`）
  - クライアント側（`user-profile-settings.js` の `handleSave`）で以下を検証する。
    - ラベル名（label_name）が未入力
    - 入力方式が `select` で options に空要素がある
  - 検証エラー時は汎用メッセージ「Failed to update settings.」（英語、赤アラート）を表示し保存を中止する（項目個別の文言・入力欄の赤表示は行わない）。
  - 検証を通過した場合、`AdminSettings.update("profiles_items_settings", ...)` で保存し、成功メッセージ「Settings updated successfully」（青のinfo表示）を表示する。
  - AJAX通信失敗時は「Profile Settings Update Failed.」を表示する。
  - 保存された設定はプロフィール編集画面・自動入力の生成時に参照される。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2024/8/27 |  | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)準拠に更新。画面・保存の実体をweko-adminと明記、メニュー名・入力方式5種・設定格納/デフォルト・configキー・保存ルート/権限・自動入力の前提フラグ・実際のメッセージ／バリデーションに書き換え |
