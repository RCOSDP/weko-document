# アクセス_システムロール

## 目的・用途

本機能は、全ユーザーに一括付与する権限を管理する機能である。

## 利用方法

【Administration > ユーザー管理（User Management） > アクセス：システムロール（Access: System Roles）画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 画面の主な構成と操作方法は、【アクセス：ロール（Access: Roles）画面】と同様である。[ADMIN-13-1: アクセス_ロール](./ADMIN_13_1.md)を参照すること。
  - 一覧（List）タブでは、【アクセス：ロール（Access: Roles）画面】の「Role」と異なり「System Role」が表示される。
  - 「作成」（Create）タブでは、【アクセス：ロール（Access: Roles）画面】の「Role」と異なり「System Role」を選択する。
    - 「System Role」の選択肢は以下の通りである。
      - 「any_user」：ゲストを含むすべての操作者を対象とする。
      - 「authenticated_user」：ログインしているすべての操作者を対象とする。

## 関連モジュール

- invenio_access（WEKOソース内にforkされていない）

## 処理概要

- 画面の設定をもとに、以下のようにaccess_actionssystemrolesテーブルに保存する。
  - 「id」フィールド：画面上の入力によらない
  - 「action」フィールド：画面上の「Action」で選択されたもの
  - 「exclude」フィールド：画面上の「Deny」にチェックが入っていたらTrue、そうでなければFalse
  - 「argument」フィールド：画面上の「Argument」の入力値
  - 「role_name」フィールド：画面上の「System Role」で選択されたもの（実カラム名は `role_name`）
- 各actionは、関数へのアノテーションでアクセス制御に利用する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_access.admin.ActionSystemRolesView`（テーブル `access_actionssystemroles`）。実カラムは `role_name`（`role` ではない）で、登録済みシステムロール（`any_user` / `authenticated_user` 等）に対して検証される。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
