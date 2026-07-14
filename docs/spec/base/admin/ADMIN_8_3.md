### 参加リクエスト

## 目的・用途

本機能は、コミュニティへの参加（登録）リクエスト（InclusionRequest）の一覧確認及び削除を行う機能である。

## 利用方法

【Administration > コミュニティ管理（Communities） > Inclusion Request画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

- 【仕様の確認中】

## 関連モジュール

- invenio_communities

## 処理概要

- 【仕様の確認中】

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_communities.admin.InclusionRequestModelView`（テーブル `communities_community_record`）。`can_create=False` / `can_edit=False` / `can_delete=True` / `can_view_details=True`（一覧確認・詳細・削除のみ）。`column_list=('id_community','id_record','expires_at','id_user')`。
- 実装補足：flask-admin 既定の一覧/詳細/削除ビューを使用（独自オーバーライドなし）。中間テーブルは Community–Record（`communities_community_record`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
