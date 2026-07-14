### 連結アカウント識別子

## 目的・用途

本機能は、invenioデフォルト機能を使用してaccounts_useridentityテーブルをメンテナンスする際に使用する機能であるが、WEKO v0.9.22ではこのテーブルを使用していない。

## 利用方法

【Administration > ユーザー管理（User Management） > 連結アカウント識別子（Linked account identities）画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

## 関連モジュール

- invenio_accounts（関連するソースはWEKOにフォークされてない）

## 処理概要

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ（訂正）：連結アカウント識別子の実体は **invenio-oauthclient** の `UserIdentityView`（model `UserIdentity`、テーブル `oauthclient_useridentity`、`can_create=False`）。旧記述の `invenio_accounts` / `accounts_useridentity` は当バージョンでは誤り。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2022/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
