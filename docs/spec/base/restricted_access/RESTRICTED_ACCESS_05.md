### プロフィール表示設定

#### 目的・用途

本機能は、プロフィール画面にて表示される項目の表示、非表示を設定する機能である

#### 利用方法

【Administration＞アドバンスド（Advanced）＞プロフィール表示設定】の順でプロフィール表示設定画面へ遷移して利用する。

> 実装（v2.0.2）の補足：メニューの実際の表記は **「Profile Settings」**（"Item" は付かない）である。画面・保存処理は `weko-admin`（`ProfileSettingView`）に実装されている（後述「関連モジュール」参照）。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

#### 機能内容

- 各項目で表示・非表示の設定
  - 各項目に設置されている表示フラグを設定するチェックボックスにチェックが入った状態で保存　することで、プロフィール画面に表示される。
    - 項目が非表示である場合、その項目を自動入力機能の対象外とする

- 各項目で、ラベル名の編集
  - 各項目に設置されているラベル名のテキストボックスを編集することで、ラベル名を自由に変更でき、プロフィール編集画面に反映される。

- 各項目の入力方式の編集
  - 各項目に設置されている入力方式の変更プルダウンを編集することで、項目の入力方式を変更することができる。[select]を選択した場合、項目の下部にオプション記入テキストボックスが出てくるので、記入すること。

- 自動登録機能ヘの項目追加
  - 既存の自動登録機能に項目を追加。プロフィール表示設定画面にて表示フラグを設定するチェックボックスにチェックが入っている項目を自動入力の対象とし、表示フラグのチェックボックスにチェックされていないものを自動登録の対象外とする。
    - ※実装上、この「表示フラグ（visible）による自動入力対象の出し分け」は `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` が True の場合にのみ有効（既定は False）。データ生成は `weko-user-profiles/utils.py` の `get_user_profile_info` / `models.py` の `get_institute_data` で行われる。

#### 関連モジュール

- weko-admin（設定画面・保存処理の実体：`ProfileSettingView`、保存API、React画面 `user-profile-settings.js`）
- weko-user-profiles（設定値の消費側：プロフィールフォーム生成、自動入力（autofill）のデータ生成、デフォルト設定値の定義）
- weko-workflow / weko-workspace（autofill でプロフィール情報を利用する呼び出し元）

> 注：旧記述では関連モジュールを `weko-user-profiles` のみとしていたが、v2.0.2 実装では設定画面・保存は `weko-admin` にあり、`weko-user-profiles` は設定を消費する側である。

#### 設定の格納・デフォルト

- 設定は `AdminSettings` テーブルの name=`profiles_items_settings`（JSON）に格納される。
- デフォルト値は `weko-user-profiles/weko_user_profiles/config.py` の `WEKO_USERPROFILES_DEFAULT_FIELDS_SETTINGS`（対象：fullname / university / department / position / item1〜item16）。
- 各項目の構造：`{order:int, visible:bool, label_name:str, format:str, options:list}`

#### 主要設定値（config）

| キー | 既定値 | 用途 |
| --- | --- | --- |
| `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` | False | プロフィール表示設定（visible／label／format）の有効化スイッチ。**False（既定）の場合は表示制御・autofill対象制御が効かず全項目が従来通り出力される** |
| `USERPROFILES_FORMAT_OPTION_LIST` | `['text','select','identifier','phonenumber','position(other)']` | 入力方式の選択肢 |
| `WEKO_USERPROFILES_DEFAULT_FIELDS_SETTINGS` | （項目デフォルト定義） | 設定の初期値 |
| `WEKO_ADMIN_PROFILE_SETTING_TEMPLATE` | `'weko_admin/admin/profiles_settings.html'` | 画面テンプレート |

#### 処理概要

- プロフィール表示設定画面 初期表示（`ProfileSettingView.index`、`GET /admin/profile_settings/`）
  - `AdminSettings` の `profiles_items_settings`（無ければデフォルト）を画面に渡し、React（`ProfilesList`／`user-profile-settings.js`）で order 順に描画する。
  - プロフィール画面に表示できる各項目の項目名、表示フラグ、ラベル名、入力方式をすべて表示する。
    - 表示フラグ：チェックボックス。チェックが入っている場合、True。チェックナシの場合はFalse
    - 入力方式プルダウン：プルダウンメニュー、selectが選択された場合オプション記入ボックスを表示する。(テキスト、セレクト（例：a|b|c）、識別子)
      - ※実装上の選択肢は `USERPROFILES_FORMAT_OPTION_LIST` により5種類：`text` / `select` / `identifier` / `phonenumber` / `position(other)`
      - オプション記入ボックス内メッセージ
        - 英語： 「separate option with the | character」（`user-profile-settings.js` にハードコード）
        - 日本語：（未対応）※実装ではi18n化されておらず、英語文言が固定表示される

- 設定内容を保存（`send_profile_settings_save`、`POST /api/admin/profile_settings/save`。`@roles_required(['System Administrator','Repository Administrator'])`）
  - `AdminSettings.update("profiles_items_settings", ...)` で保存する。
  - 未入力項目がないことをチェック
    - 未入力項目がある場合、項目のボックスを赤く表示し、以下のエラーメッセージを表示し、保存をキャンセルする
      - 項目名未記入
        - 日本語：「項目名が未入力です」
        - 英語：「Item name has not been entered. 」
      - ラベル名未記入
        - 日本語：「ラベル名が未記入です」
        - 英語：「label name has not been entered. 」
      - オプション項目未記入
        - 日本語：「オプションが未記入です」
        - 英語：「Option has not been entered. 」
  - 必須入力項目がすべて入力済みの場合、保存し以下メッセージを表示
    - 保存完了
      - 日本語：「変更が保存されました」
      - 英語： 「Saved successfully. 」
  - 保存された結果をプロフィール画面に渡す。

> 実装（v2.0.2）の補足（本節の記述と現行実装の差異）：
> - クライアント側（`user-profile-settings.js` の `handleSave`）で実際に行う検証は「ラベル名（label_name）が未入力」または「入力方式が select で options に空要素がある」場合のみ。「項目名（キー）」は固定表示・編集不可のため未記入チェックは存在しない。
> - エラー表示は項目個別の文言・入力欄の赤表示ではなく、汎用メッセージ「Failed to update settings.」（英語のみ）を表示する。
> - 保存成功時のメッセージはバックエンド返却の「Settings updated successfully」（英語）。本文の「項目名が未入力です／ラベル名が未記入です／オプションが未記入です／変更が保存されました」等の個別・日本語文言は現行実装では未対応（将来対応または要文言修正）。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2024/8/27 |  | 初版作成 |
| 2026/07/13 |  | 実装(v2.0.2)と突き合わせ。関連モジュールをweko-admin主体に訂正、メニュー名・入力方式5種・設定格納/デフォルト・configキー・保存ルート/権限・autofill前提フラグを追記。バリデーション文言等が現行実装で未対応である旨を注記 |
