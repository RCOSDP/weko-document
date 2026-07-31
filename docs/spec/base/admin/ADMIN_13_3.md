# アクセス_ユーザー

## 目的・用途

本機能は、個別のユーザーに付与する権限を管理する機能である。

## 利用方法

【Administration > ユーザー管理（User Management） > アクセス：ユーザー（Access: Users）画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 画面の主な構成と操作方法は、【アクセス：ロール（Access: Roles）画面】と同様である。[ADMIN-13-1: アクセス_ロール](./ADMIN_13_1.md)を参照すること。
  - 一覧（List）タブでは、【アクセス：ロール（Access: Roles）画面】の「Role」と異なり「User ID」と「Email」が表示される。
    - 「User ID」と「Email」には、accounts_userテーブルの「id」「email」フィールドの値が表示される。
  - 「作成」（Create）タブでは、【アクセス：ロール（Access: Roles）画面】の「Role」と異なり「User」を選択する。
    - 「User」の選択肢として、accounts_userテーブルに登録されたユーザーが表示される。
    - 各選択肢は、「User<id=(レコードのid), email=(レコードのemail)>」の形で表示される。

## 関連モジュール

- invenio_access（WEKOソース内にforkされていない）

## 処理概要

- 画面の設定をもとに、以下のようにaccess_actionsusersテーブルに保存する。
  - 「id」フィールド：画面上の入力によらない
  - 「action」フィールド：画面上の「Action」で選択されたもの
  - 「exclude」フィールド：画面上の「Deny」にチェックが入っていたらTrue、そうでなければFalse
  - 「argument」フィールド：画面上の「Argument」の入力値
  - 「user_id」フィールド：画面上の「User」で選択されたユーザーのid
- 各actionは、関数へのアノテーションでアクセス制御に利用する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_access.admin.ActionUsersView`（model `ActionUsers`、テーブル `access_actionsusers`）。一覧の「Email」は `user.email` リレーションによる表示で、当テーブルの列ではない。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
