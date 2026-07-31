# Resource Sync

Resource Syncのアクセスコントロールについて記述します。

## 目次

- [Resource List](#resource-list)
- [Change List](#change-list)
- [Resync](#resync)

## Resource List

エンドポイント：/admin/resource_list/

○に合致すれば、Resource Listページを閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ×            | ×            | ×                        |

#### Resource Listの作成・閲覧・削除・編集

いずれかの○に合致すれば、Resource Listを作成、閲覧、削除、編集することが出来ます。

| ロール                                                                 | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---------------------------------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 「Repository」に<br>自身の所属する<br>コミュニティが<br>設定されている | ○                  | ○                    | ○                      | ×            | ×            | ×                        |
| 上記以外                                                               | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

## Change List

エンドポイント：/admin/change_list/

○に合致すれば、Change Listページを閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ×            | ×            | ×                        |

#### Change Listの作成・閲覧・削除・編集

いずれかの○に合致すれば、Change Listを作成、閲覧、削除、編集することが出来ます。

| ロール                                                                 | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---------------------------------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 「Repository」に<br>自身の所属する<br>コミュニティが<br>設定されている | ○                  | ○                    | ○                      | ×            | ×            | ×                        |
| 上記以外                                                               | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

## Resync

エンドポイント：/admin/resync/

○に合致すれば、Resyncページを閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ×            | ×            | ×                        |

#### Resyncの作成・閲覧・削除・編集

いずれかの○に合致すれば、Resyncを作成、閲覧、削除、編集することが出来ます。

| ロール                                                                   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ------------------------------------------------------------------------ | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 「Target Index」に<br>自身の所属する<br>コミュニティが<br>設定されている | ○                  | ○                    | ○                      | ×            | ×            | ×                        |
| 上記以外                                                                 | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本画面のロール別アクセス可否は、`weko_admin/ext.py` の `WekoAdmin.role_has_access`（`@app.before_request` の `is_accessible_to_role` が全 Flask-Admin ビューの `is_accessible`/`is_visible` を上書き）で判定される。判定は `weko_admin/config.py` の `WEKO_ADMIN_ACCESS_TABLE`（System Administrator は全許可、Repository Administrator は `WEKO_ADMIN_REPOSITORY_ACCESS_LIST`、Community Administrator は `WEKO_ADMIN_COMMUNITY_ACCESS_LIST`）に、当該ビューの endpoint 名が含まれるかで行う。ロールを持たないユーザー（登録／一般）およびゲストは全画面 ×。画面内の作成・編集・削除（CRUD）や一覧の絞り込みは各 ModelView の `can_create`/`can_edit`/`can_delete`/`get_query` による別レイヤで、コミュニティ範囲の絞り込みは `Community.get_repositories_by_user`／`WEKO_PERMISSION_SUPER_ROLE_USER`（System＋Repository）で行われる。

### 実装上の補足（v2.0.2）

- Resource List / Change List の実体は **invenio-resourcesyncserver**（`AdminResourceListView` / `AdminChangeListView`、endpoint `resource_list` / `change_list`）、Resync の実体は **invenio-resourcesyncclient**（`AdminResyncClient`、endpoint `resync`）にある。
- `resource_list` / `change_list` / `resync` はいずれもコミュニティ・リポジトリ両リストに含まれ、上位アクセスは System ○ / Repository ○ / Community ○。サブ表（対象インデックスが自身の管理コミュニティに属するか）は `WEKO_PERMISSION_SUPER_ROLE_USER`＋`Community.get_repositories_by_user` による絞り込みで担保される。

### 実装上の変更（v2.1.0：ChangeListのエンバーゴ考慮）

`WEKO_SEARCH_FIX_ACCESSRIGHTS`（`weko_search_ui/config.py`、既定 `False`）がTrueの環境では、ResourceSync の変更差分（ChangeList）生成がエンバーゴ状態を考慮する。

- `invenio_resourcesyncserver/query.py` の `item_changes_search_factory` は、更新日ウィンドウ（from/until）による `_updated` レンジ絞り込みを、`invenio_oaiserver.query.range_query`（OAI-PMHと共通のエンバーゴ考慮クエリ）へ切り替える。エンバーゴ解除（公開日到来）アイテムを差分に反映するため、公開日と `_updated` の双方でウィンドウ内外を判定する。
- レコードの更新日時（datestamp）自体の繰り上げは `invenio_records/api.py` の `Record.updated` プロパティが担う（OAI-PMHと共通）。
- Falseの場合は素の `_updated` レンジによる従来動作。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3    | 初版作成                                                 |
| 2026/07/17 |                                            | v2.1.0差分反映：エンバーゴ考慮のaccessRights             |
