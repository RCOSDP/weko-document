### 共有

#### 目的・用途

本機能は、アイテムの詳細情報を共有する機能である。

#### 利用方法

共有は、アイテム詳細画面の右端のShareエリアの共有ボタンを押下して行う。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

#### 機能内容

  - アイテム詳細画面での「共有」（Share）エリアに共有ボタンを表示する

      - 表示する共有ボタンは html ファイル（`templates/weko_records_ui/box/share.html`）に指定する

          - 表示される共有ボタンは以下の通りである。

              - 「Facebook」

              - 「Twitter(X)」

              - 「Print（印刷）」

  - 「Facebook」「Twitter(X)」ボタンを押すと、該当サイトの共有画面に移動する。「Print（印刷）」ボタンを押すと、印刷ダイアログ（`window.print()`）を表示する。

#### 関連モジュール

  - 対応しているモジュール：「weko_records_ui」

#### 処理概要

共有ボタンは `templates/weko_records_ui/box/share.html` に定義され、Facebook・Twitter(X) はそれぞれネイティブの Facebook SDK / Twitter ウィジェットを、Print（印刷）は `window.print()` を使用する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 共有ボタンは `templates/weko_records_ui/box/share.html` の Facebook・Twitter(X)・Print（印刷）のみで、ネイティブの Facebook SDK / Twitter widget / `window.print()` を使用する。`weko_theme/static/js/addthis/addthis_widget.js` は残存するが share.html から読み込まれていない（孤立）。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
