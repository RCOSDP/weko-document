### 連結アカウントトークン

## 目的・用途

本機能は、invenio デフォルト機能（Flask-Admin）を使用して外部認証との連結アカウントトークン（`oauthclient_remotetoken` テーブル）をメンテナンスする際に使用する機能である。WEKO では通常このテーブルを使用しない。

## 利用方法

【Administration > ユーザー管理（User Management） > 連結アカウントトークン（Linked account tokens）画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 連結アカウントトークン（`RemoteToken`）の一覧表示・編集・削除を行う。
- 各レコードは `id_remote_account`（連結アカウントへの参照）・`token_type`・`access_token`・`secret` を持つ。

## 関連モジュール

- invenio-oauthclient（`admin.RemoteTokenView`、model `RemoteToken`、テーブル `oauthclient_remotetoken`。WEKO ソースにはフォークされていない外部依存）

## 処理概要

- Flask-Admin の ModelView（`invenio_oauthclient.admin.RemoteTokenView`）でテーブル `oauthclient_remotetoken` を保守する。一覧列は `id_remote_account` / `token_type`、フォームは `remote_account` / `token_type`。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
