# 制限公開

制限公開に関するAPIのアクセスコントロールについて記述します。

## 目次

- [GET /api/\<version>/workflow/activities](#get-apiversionworkflowactivities)
- [POST /api/\<version>/workflow/activities/\<activity_id>/approve](#post-apiversionworkflowactivitiesactivity_idapprove)
- [POST /api/\<version>/workflow/activities/\<activity_id>/throw-out](#post-apiversionworkflowactivitiesactivity_idthrow-out)
- [GET /api/\<version>/records/\<pid>/files/\<filename>/terms](#get-apiversionrecordspidfilesfilenameterms)
- [POST /api/\<version>/records/\<pid>/files/\<filename>/application](#post-apiversionrecordspidfilesfilenameapplication)
- [POST /api/\<version>/workflow/activities/\<activity_id>/application](#post-apiversionworkflowactivitiesactivity_idapplication)
- [GET /api/\<version>/records/\<pid>/need-restricted-access](#get-apiversionrecordspidneed-restricted-access)

## GET /api/\<version>/workflow/activities

表内のいずれかの○に合致すれば、アクティビティの一覧を取得することが出来ます。

| 条件/ロール                                 | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>user:activityがある | ○                  | ○                    | ○ ※1                   | ○ ※1         | ×            | ×                        |
| 上記以外                                    | ×                  | ×                    | ×                      | ×            | ×            | ×                        |

※1 自身が担当するアクティビティのみ取得することが出来ます。

## POST /api/\<version>/workflow/activities/\<activity_id>/approve

表内の○に合致すれば、承認待ちのアクティビティを承認することが出来ます。

| 条件/ロール                                        | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>user:activity<br>がある    | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| 上記以外                                           | ×                  | ×                    | ×                      | ×            | ×            | ×                        |

## POST /api/\<version>/workflow/activities/\<activity_id>/throw-out

表内の○に合致すれば、操作中のアクティビティの操作を却下することが出来ます。

| 条件/ロール                                        | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>user:activity<br>がある    | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| 上記以外                                           | ×                  | ×                    | ×                      | ×            | ×            | ×                        |

## GET /api/\<version>/records/\<pid>/files/\<filename>/terms

表内の○に合致すれば、指定した制限公開ファイルの利用申請を行う際の利用規約を取得することが出来ます。

| 条件/ロール                                 | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>user:activityがある | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| 上記以外                                    | ×                  | ×                    | ×                      | ×            | ×            | ○                        |

## POST /api/\<version>/records/\<pid>/files/\<filename>/application

表内の○に合致すれば、指定した制限公開ファイルの利用申請を開始し、アクティビティの作成を行うことが出来ます。

| 条件/ロール                                 | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>user:activityがある | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| 上記以外                                    | ×                  | ×                    | ×                      | ×            | ×            | ○ ※1                     |

※1 ゲストアクティビティが作成されます。<br>
　　既に同ファイル、同一メールアドレスに紐づくゲストアクティビティが存在する場合は既存アクティビティを使用します。

## POST /api/\<version>/workflow/activities/\<activity_id>/application

表内の○に合致すれば、制限公開ファイルの利用申請ワークフローにおける申請内容の登録を行うことが出来ます。

| 条件/ロール                                 | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ------------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>user:activityがある | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| 上記以外                                    | ×                  | ×                    | ×                      | ×            | ×            | ○                        |

※ 利用申請ワークフローのみで利用可能で、通常のワークフローアクティビティでは利用出来ません。

## GET /api/\<version>/records/\<pid>/need-restricted-access

表内の○に合致すれば、当該ファイルのコンテンツダウンロードに利用申請が必要かどうか判断することが出来ます。

| 条件/ロール                             | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| --------------------------------------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| トークンのスコープに<br>item:readがある | ○                  | ○                    | ○                      | ○            | ○            | ×                        |
| 上記以外                                | ×                  | ×                    | ×                      | ×            | ×            | ○                        |

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本APIの認可は OAuth2 を基本とし、`require_api_auth(allow_anonymous=…)`（未認証許可可否）、`require_oauth_scopes(<scope>)`（トークン使用時のみスコープ検証）、`roles_required([...])`（未認証かつ guest_token 無しは 401）の組み合わせで判定される。ゲスト（未ログイン）可否は主に `allow_anonymous` と `roles_required` の有無で決まり、公開範囲は検索系では `weko_search_ui.query.get_permission_filter` で絞り込まれる。各エンドポイントの実ハンドラ・スコープは [API仕様（api カテゴリ）](../api/README.md) を参照。

### 実装上の変更（v2.1.0）

- 本カテゴリのエンドポイント自体のデコレータ（`require_api_auth` / `require_oauth_scopes`）は b19e39d8a 以降変更されていない。
- API アプリでは `login_required` 等による未認証応答が、ログイン画面へのリダイレクト（API アプリには `security` blueprint が無いため 500 になっていた）から、401 の JSON（`{"status": 401, "message": "Authentication required."}`）に統一された（`weko_accounts/unauthorized.py` の `install(app, api_only=True)`、`WEKO_ACCOUNTS_UNAUTHORIZED_JSON`（既定 True）。issue62569）。
- `GET /api/<version>/records/<pid>/need-restricted-access` が内部で用いる `weko_records_ui.permissions.check_file_download_permission` では、コミュニティ管理者を管理者扱いする範囲が、当該アイテムが自身の管理するコミュニティ配下のインデックスに所属する場合に限定された（`is_superuser_or_record_comadmin`）。上表のコミュニティ管理者の判定結果は、担当外コミュニティのアイテムでは一般の登録ユーザーと同じになる。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3      | 初版作成                                                 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：API アプリの未認証応答の 401 JSON 統一、ダウンロード可否判定でのコミュニティ管理者の範囲限定を追記 |
