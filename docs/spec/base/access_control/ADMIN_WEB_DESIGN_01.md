# ウェブデザイン管理

ウェブデザイン管理のアクセスコントロールについて記述します。

## 目次

- [ウィジェット](#ウィジェット)
- [ページレイアウト](#ページレイアウト)

## ウィジェット

エンドポイント：/admin/widgetitem/

○に合致すれば、ウィジェットページを閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ×            | ×            | ×                        |

#### ウィジェットページの機能

いずれかの○に合致すれば、以下のウィジェットページの機能を利用することが出来ます。

利用出来る機能：ウィジェットが一覧に表示される、ウィジェットの作成・閲覧・編集・削除

| 条件/ロール                                                                              | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---------------------------------------------------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| ウィジェットの<br>「Repository」に<br>自身の管理する<br>コミュニティが<br>登録されている | ○                  | ○                    | ○                      | ×            | ×            | ×                        |
| 上記以外                                                                                 | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

## ページレイアウト

エンドポイント：/admin/widgetdesign/

○に合致すれば、ページレイアウトページを閲覧することが出来ます。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ×            | ×            | ×                        |

#### ページレイアウトページの機能

いずれかの○に合致すれば、以下のページレイアウトページの機能を利用することが出来ます。

利用出来る機能：「Repository」の選択肢にコミュニティが表示される、ページレイアウトの保存

| 条件/ロール                    | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ------------------------------ | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 自身の管理する<br>コミュニティ | ○                  | ○                    | ○                      | ×            | ×            | ×                        |
| 上記以外                       | ○                  | ○                    | ×                      | ×            | ×            | ×                        |

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本画面のロール別アクセス可否は、`weko_admin/ext.py` の `WekoAdmin.role_has_access`（`@app.before_request` の `is_accessible_to_role` が全 Flask-Admin ビューの `is_accessible`/`is_visible` を上書き）で判定される。判定は `weko_admin/config.py` の `WEKO_ADMIN_ACCESS_TABLE`（System Administrator は全許可、Repository Administrator は `WEKO_ADMIN_REPOSITORY_ACCESS_LIST`、Community Administrator は `WEKO_ADMIN_COMMUNITY_ACCESS_LIST`）に、当該ビューの endpoint 名が含まれるかで行う。ロールを持たないユーザー（登録／一般）およびゲストは全画面 ×。画面内の作成・編集・削除（CRUD）や一覧の絞り込みは各 ModelView の `can_create`/`can_edit`/`can_delete`/`get_query` による別レイヤで、コミュニティ範囲の絞り込みは `Community.get_repositories_by_user`／`WEKO_PERMISSION_SUPER_ROLE_USER`（System＋Repository）で行われる。

### 実装上の変更（v2.1.0：ウィジェット関連 API の認可強化）

release_v2.1.0 では、ウィジェット・ページレイアウト画面が内部で呼び出す API（`weko_gridlayout/views.py`）に認可が追加され、上記サブ表の「自身の管理するコミュニティ」の条件が API 側でも担保されるようになった（issue62569 PR #1901、ウィジェット権限 No.290/303/304 PR #1930、issue62783 PR #1923）。

リポジトリスコープ検証は `weko_admin.permissions.repository_scope_required` で行う。

- 未ログインは 401。System / Repository Administrator（`WEKO_PERMISSION_SUPER_ROLE_USER`）は無条件で許可。
- Community Administrator は、検証対象のリポジトリ ID がすべて `Community.get_repositories_by_user` の返すコミュニティに含まれる場合のみ許可。それ以外は 403。
- 検証対象は、リクエストで指定された所属先（`repository_id_param`）と、既存レコードの現在の所属（`id_param` で指定された ID から `id_model` を引いて得た `repository_id`）の両方。既存レコードが見つからない場合は 404。担当外コミュニティへの移動・担当外レコードの更新を防ぐ。

| API | 追加された認可 |
| --- | --- |
| `POST /api/admin/load_widget_list_design_setting` | `repository_scope_required(repository_id_param='repository_id')` |
| `POST /api/admin/save_widget_layout_setting` | `repository_scope_required(repository_id_param='repository_id', id_param='page_id', id_model=WidgetDesignPage)` |
| `POST /api/admin/save_widget_design_page` | 同上 |
| `POST /api/admin/delete_widget_design_page` | `repository_scope_required(id_param='page_id', id_model=WidgetDesignPage)` |
| `POST /api/admin/save_widget_item` | `repository_scope_required(repository_id_param='data.repository', id_param='data_id', id_model=WidgetItem, pk_attr='widget_id')` |
| `POST /api/admin/delete_widget_item` | `repository_scope_required(id_param='data_id', id_model=WidgetItem, pk_attr='widget_id')` |
| `GET /api/admin/load_widget_type` | `login_required` ＋ `roles_required`（System / Repository / Community Administrator） |
| `POST /widget/uploads/<community_id>`、`POST /widget/uploads/`（ウィジェット用ファイルのアップロード） | `login_required` |
| `GET /widget/uploaded/<filename>`、`GET /widget/uploaded/<filename>/<community_id>`（アップロード済みファイルの取得） | `roles_required`（System / Repository / Community Administrator。未ログインは 401、その他ロールは 403） |
| `POST /api/admin/widget/unlock` | `login_required` |

> 実装補足（v2.1.0）：`/widget/uploaded/...` は管理者ロールのみ取得可能となったため、フリー記述ウィジェット等に埋め込んだアップロード画像は、ゲスト・一般ユーザーの閲覧時に表示されない（401/403）可能性がある。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3      | 初版作成                                                 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：ウィジェット・ページレイアウト関連APIの認可（リポジトリスコープ検証・ロール制限）を追記 |
