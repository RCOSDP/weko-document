# アドバンスド

アドバンスドのアクセスコントロールについて記述します。

エンドポイント：/admin/profile_settings/

## 目次

- [プロフィール編集画面](#プロフィール編集画面)

## プロフィール編集画面

プロフィール編集画面（endpoint `profile_settings`）のアクセス可否は、設定値 `WEKO_USERPROFILES_CUSTOMIZE_ENABLED`（既定 False）で決まり、ロールによる差はありません。既定（False）ではシステム管理者を含め誰も本画面にアクセスできません。True の場合は、ロールを 1 つ以上持つ認証ユーザーであれば全員が、本画面の閲覧、および設定値の登録・編集・表示非表示の切り替えを行うことが出来ます。ゲスト（未ログイン）は不可です。

| 条件/ロール                                                      | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---------------------------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` = True（ロールを持つ認証ユーザー） | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` = False（既定）            | ×                  | ×                    | ×                      | ×            | ×            | ×                        |

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本画面のロール別アクセス可否は、`weko_admin/ext.py` の `WekoAdmin.role_has_access`（`@app.before_request` の `is_accessible_to_role` が全 Flask-Admin ビューの `is_accessible`/`is_visible` を上書き）で判定される。判定は `weko_admin/config.py` の `WEKO_ADMIN_ACCESS_TABLE`（System Administrator は全許可、Repository Administrator は `WEKO_ADMIN_REPOSITORY_ACCESS_LIST`、Community Administrator は `WEKO_ADMIN_COMMUNITY_ACCESS_LIST`）に、当該ビューの endpoint 名が含まれるかで行う。ロールを持たないユーザー（登録／一般）およびゲストは全画面 ×。画面内の作成・編集・削除（CRUD）や一覧の絞り込みは各 ModelView の `can_create`/`can_edit`/`can_delete`/`get_query` による別レイヤで、コミュニティ範囲の絞り込みは `Community.get_repositories_by_user`／`WEKO_PERMISSION_SUPER_ROLE_USER`（System＋Repository）で行われる。

### 実装補足（v2.0.2）

- プロフィール編集画面（endpoint `profile_settings`）は `role_has_access` の**特別分岐**で扱われ、通常のアクセスリスト判定・System Administrator バイパスより前に `WEKO_USERPROFILES_CUSTOMIZE_ENABLED`（既定 False）の値を返す。
  - False（既定）の場合は System Administrator を含め誰もアクセスできない。
  - True の場合はロールを 1 つ以上持つ認証ユーザー（System／Repository／Community／Contributor／登録ユーザー等）全員がアクセス可能で、ロール差は無い。ゲストは不可。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |   6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3     | 初版作成                                                 |
| 2026/07/14 |                                            | 本文を実装準拠に修正                                     |
