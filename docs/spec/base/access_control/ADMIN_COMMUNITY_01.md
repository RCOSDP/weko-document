# コミュニティ管理

コミュニティ管理のアクセスコントロールについて記述します。

## 目次

- [コミュニティ](#コミュニティ)
- [参加リクエスト](#参加リクエスト)
- [注目のコミュニティ](#注目のコミュニティ)

## コミュニティ

エンドポイント：/admin/community/

表内の○に合致すれば、コミュニティ一覧を閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ×            | ×            | ×                        |

#### 閲覧・編集・削除

表内のいずれかの○に合致すれば、コミュニティの閲覧・編集・削除を行うことが出来ます。

| ロール                     | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 自身が所属する<br>グループ | ○                  | ○                    | ○                      | ×            | ×            | ×                        |
| 上記以外                   | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

#### 作成

表内の○に合致すれば、コミュニティの作成を行うことが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

## 参加リクエスト

エンドポイント：/admin/inclusionrequest/

表内の○に合致すれば、参加リクエスト一覧を閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ×                    | ×                      | ×            | ×            | ×                        |

## 注目のコミュニティ

エンドポイント：/admin/featuredcommunity/

表内の○に合致すれば、注目のコミュニティページの以下機能を利用することが出来ます。

利用出来る機能：コミュニティ一覧の閲覧、およびコミュニティの作成・閲覧・編集・削除

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ×                    | ×                      | ×            | ×            | ×                        |

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本画面のロール別アクセス可否は、`weko_admin/ext.py` の `WekoAdmin.role_has_access`（`@app.before_request` の `is_accessible_to_role` が全 Flask-Admin ビューの `is_accessible`/`is_visible` を上書き）で判定される。判定は `weko_admin/config.py` の `WEKO_ADMIN_ACCESS_TABLE`（System Administrator は全許可、Repository Administrator は `WEKO_ADMIN_REPOSITORY_ACCESS_LIST`、Community Administrator は `WEKO_ADMIN_COMMUNITY_ACCESS_LIST`）に、当該ビューの endpoint 名が含まれるかで行う。ロールを持たないユーザー（登録／一般）およびゲストは全画面 ×。画面内の作成・編集・削除（CRUD）や一覧の絞り込みは各 ModelView の `can_create`/`can_edit`/`can_delete`/`get_query` による別レイヤで、コミュニティ範囲の絞り込みは `Community.get_repositories_by_user`／`WEKO_PERMISSION_SUPER_ROLE_USER`（System＋Repository）で行われる。

### 実装上の変更（v2.1.0：GakuNin mAP ロール／グループの判定条件）

コミュニティ作成・編集画面の「オーナー」「グループ」選択肢に関わる GakuNin mAP のロール／グループ判定が、release_v2.1.0 で変更された（PR #1891）。`invenio_communities/admin.py` の `CommunityModelView` は、オーナー（`owner`）の選択肢を mAP ロール以外のロール、グループ（`group`）の選択肢を mAP グループのロールとする。一覧等でのオーナー表示名（`invenio_communities/models.py` の `Community.owner_display`）は、`sysadm_group` なら `WEKO_ADMIN_PERMISSION_ROLE_SYSTEM`、`<prefix>_<fqdn>_<role_keyword>_<suffix>` と完全一致すれば `role_mapping[suffix]` の表示名に置き換える。

判定は `weko_accounts/api.py` の関数に集約された（`map_role_condition` / `map_group_condition` / `is_map_role` / `is_map_group` / `is_map_managed_name` / `is_map_sysadm_role`）。`WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT`（`prefix`、`role_keyword`、`group_keyword`（v2.1.0 で追加、既定 `gr`）、`sysadm_group`、`role_mapping`）と `WEKO_ACCOUNTS_IDP_ENTITY_ID` の両方が設定されている場合のみ有効で、`<fqdn>` は `WEKO_ACCOUNTS_IDP_ENTITY_ID` のホスト名の `.`・`-` を `_` に置換した値（`create_fqdn_from_entity_id`）。

| 区分 | ロール名の条件 |
| --- | --- |
| mAP ロール | `sysadm_group` と一致、または `<prefix>_<fqdn>_<role_keyword>_` で始まる |
| mAP グループ | `<prefix>_<fqdn>_<group_keyword>_` で始まる |

いずれかの設定が無い場合はどのロールも mAP ロール／グループとして扱われない（v2.0.x までの「`role_keyword` を含み `prefix` で始まる」「`_groups_` を含む」という部分一致判定は廃止）。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |   6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3   | 初版作成                                                 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：GakuNin mAP ロール／グループの判定条件（map conditions）を追記 |
