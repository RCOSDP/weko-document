### 連結アカウント識別子

## 目的・用途

本機能は、invenio デフォルト機能（Flask-Admin）を使用して外部認証との連結アカウント識別子（`oauthclient_useridentity` テーブル）をメンテナンスする際に使用する機能である。WEKO では通常このテーブルを使用しない。

## 利用方法

【Administration > ユーザー管理（User Management） > 連結アカウント識別子（Linked account identities）画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 連結アカウント識別子（`UserIdentity`）の一覧表示・編集・削除を行う。新規作成は不可（`can_create=False`）。
- 各レコードは `id`（識別子値）・`method`（認証方式）・`id_user`（ユーザーID）を持つ。

## 関連モジュール

- invenio-oauthclient（`admin.UserIdentityView`、model `UserIdentity`、テーブル `oauthclient_useridentity`。WEKO ソースにはフォークされていない外部依存）

## 処理概要

- Flask-Admin の ModelView（`invenio_oauthclient.admin.UserIdentityView`）でテーブル `oauthclient_useridentity` を保守する。`can_create=False` のため新規作成タブは表示されず、一覧・編集・削除のみ。
- ※旧記述の関連モジュール `invenio_accounts` ／テーブル `accounts_useridentity` は当バージョンでは誤り（実体は invenio-oauthclient / `oauthclient_useridentity`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2022/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
