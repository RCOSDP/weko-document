# メンテナンス

メンテナンス画面のアクセスコントロールについて記述します。

エンドポイント：/admin/reindex_es/

## 目次

- [ElasticSearchインデックス](#elasticsearchインデックス)

## ElasticSearchインデックス

表内のいずれかの○に合致すれば、ElasticSearchインデックスページを閲覧することが出来ます。

|ロール|システム<br>管理者|リポジトリ<br>管理者|コミュニティ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|---|---|---|---|---|---|---|
|利用可否|○|×|×|×|×|×|

表内のいずれかの○に合致すれば、「アイテムインデックスの再作成」または「アイテムの再インデックス」を実行することが出来ます。

※「アイテムインデックスの再作成」と「アイテムの再インデックス」の同時実行は不可能です。

|ロール|システム<br>管理者|リポジトリ<br>管理者|コミュニティ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|---|---|---|---|---|---|---|
|利用可否|○|×|×|×|×|×|

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本画面のロール別アクセス可否は、`weko_admin/ext.py` の `WekoAdmin.role_has_access`（`@app.before_request` の `is_accessible_to_role` が全 Flask-Admin ビューの `is_accessible`/`is_visible` を上書き）で判定される。判定は `weko_admin/config.py` の `WEKO_ADMIN_ACCESS_TABLE`（System Administrator は全許可、Repository Administrator は `WEKO_ADMIN_REPOSITORY_ACCESS_LIST`、Community Administrator は `WEKO_ADMIN_COMMUNITY_ACCESS_LIST`）に、当該ビューの endpoint 名が含まれるかで行う。ロールを持たないユーザー（登録／一般）およびゲストは全画面 ×。画面内の作成・編集・削除（CRUD）や一覧の絞り込みは各 ModelView の `can_create`/`can_edit`/`can_delete`/`get_query` による別レイヤで、コミュニティ範囲の絞り込みは `Community.get_repositories_by_user`／`WEKO_PERMISSION_SUPER_ROLE_USER`（System＋Repository）で行われる。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3     | 初版作成                                                 |
