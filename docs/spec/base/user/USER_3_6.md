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

  - 本機能に対応していた「AddThis」は2023年5月31日にサービスを終了しているため、共有機能を使用することは出来ない。

  - アイテム詳細画面での「共有」（Share）エリアに共有ボタンを表示する

      - 表示しておく共有ボタンをhtmlファイルに指定する

          - パス：  
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/box/share.html#L25-L33>

          - 表示される共有ボタンは以下の通りである。また、共有アイコンをマウスホバーすると、共有サイト名を表示する

              - 「mendeley」

              - 「citeulike」(2019年サービス終了により表示されない)

              - 「twitter」

              - 「facebook」

              - 「print」

          - 「+」ボタンを設ける

              - 「+」ボタンをマウスホバーすると、共有サイト名一覧を表示する

              - 「+」ボタンを押すと、共有モデルを表示する

  - 共有ボタンを押すと、該当サイトに移動する

#### 関連モジュール

  - 対応しているモジュール：「weko_records_ui」
  - 対応しているプラグイン：「AddThis」

#### 処理概要

weko_theme.static.js.addthis.addthis_widgetにおいてAddThisのアイテムの共有を設定している。  
<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/static/js/addthis/addthis_widget.js>

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足（重要な訂正）：v2.0.2 の `templates/weko_records_ui/box/share.html` には AddThis / mendeley / citeulike / 「＋」ボタンは**存在しない**。現在の共有ボタンは Facebook・Twitter(X)・Print（印刷）のみで、ネイティブの Facebook SDK / Twitter widget / `window.print()` を使用する。`weko_theme/static/js/addthis/addthis_widget.js` は残存するが share.html から読み込まれていない（孤立）。機能内容・処理概要は現行実装に合わせて要修正。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
