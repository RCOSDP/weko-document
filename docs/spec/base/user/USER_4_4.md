# Item Registration

## 目的・用途

本機能は、アイテムを新規登録／編集するためのメタデータ登録、ファイルアップロード、代理投稿の有無、フィードバックメール設定、所属するインデックス選択をする際に用いる機能である。

## 利用方法

「Item Registration」アクションを含むフローを使ったワークフローによるアクティビティを開始していることを前提とする。

フローで「Item Registration」アクションより前に設定されたアクションが完了すると、「Item Registration」アクションが表示される。

ワークフローのアイテムタイプで定められた項目を入力後、[次へ]ボタンを押下することで、インデックス選択の画面に遷移する。

インデックス選択の画面で登録するアイテムが所属するインデックスを選択後、[次へ]ボタンを押下することで、次のアクションに進む。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       ○        |        ○         |         ○          |      ○       |      ※       |                    |

※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

## 機能内容

- アイテムを編集する場合には、タイトルのリンクを押下すると、編集前のアイテムの情報をポップアップで表示する。

## 関連モジュール

- weko-workflow（ワークフロー／アクティビティ進行）
- weko-items-ui（アイテム登録画面・メタデータ入力・重複チェック）
- weko-deposit（アイテムの永続化）

## 処理概要

処理についてはそれぞれの項目（[USER-4-5〜4-9](./USER_4_5.md)、[4-16](./USER_4_16.md)、[4-17](./USER_4_17.md)）に記述する。Item Registration アクション（endpoint `item_login`、action_id 3）は `weko_workflow.views` が制御し、入力画面は `weko-items-ui` のアイテム編集 iframe（`views.iframe_items_index` 等）で描画される。

## 実装補足（v2.0.2 実装との突き合わせ）

- 本ページは Item Registration の概要。関連モジュール：weko-workflow（アクティビティ）/ weko-items-ui（登録画面）/ weko-deposit（永続化）。詳細は子ページ（USER_4_5〜4_9, 4_16, 4_17）参照。

- 実装補足（v2.1.0、編集・更新系の権限）：アイテム編集画面（`DEPOSIT_RECORDS_UI_ENDPOINTS` の `depid` `/item/edit/<pid_value>`・`iframe_depid` `/item/iframe/edit/<pid_value>`）の `weko_items_ui.permissions.edit_permission_factory` は、閲覧用の `page_permission_factory` への委譲をやめて `check_created_id`（作成者・所有者・共有ユーザー・システム／リポジトリ管理者・該当コミュニティのコミュニティ管理者）で判定する（以前は公開アイテムなら匿名でも通っていた）。デポジット REST（`/api/deposits/items/<pid_value>`、`weko_deposit.rest.ItemResource`）の POST／PUT はデコレータ `require_item_edit_permission` で未ログイン 401、アイテム不存在 404、編集権限なし 403 とし（バージョン付き pid は親 recid で判定）、`DEPOSIT_REST_ENDPOINTS['depid']` の `update_permission_factory_imp` にも `edit_permission_factory` を設定した。個別の更新権限を持たないエンドポイントは `RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY = deny_all` で拒否される。公開 `/api/deposits/publish/<pid_value>`（`weko_deposit.rest.publish`）も `@login_required` と `edit_permission_factory` で判定する（不存在 404、権限なし 403、公開処理失敗 400）。

## 更新履歴

| 日付       | GitHubコミットID                         | 更新内容 |
| ---------- | ---------------------------------------- | -------- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：編集画面・デポジット REST・公開 API の編集権限判定を追記 |
