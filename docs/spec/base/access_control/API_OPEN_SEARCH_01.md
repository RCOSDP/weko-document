# OpenSearch

OpenSearchに関するAPIのアクセスコントロールについて記述します。

## 目次

- [GET /api/opensearch/description.xml](#get-apiopensearchdescriptionxml)
- [GET /api/opensearch/search](#get-apiopensearchsearch)

## GET /api/opensearch/description.xml

全てのロールでdescription.xmlを取得することが可能です。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ○            | ○            | ○                        |

## GET /api/opensearch/search

全てのロールでOpenSearchによる検索をすることが可能です。

| ロール   | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| -------- | ------------------ | -------------------- | ---------------------- | ------------ | ------------ | ------------------------ |
| 利用可否 | ○                  | ○                    | ○                      | ○            | ○            | ○                        |

※ OpenSearchによる検索でアイテムが表示されるかどうかは、検索画面の検索結果にアイテムが表示されるかどうかと同一条件です。<br>
　[検索画面](USER_ITEM_SEARCH_01.md#検索画面)を参照ください。

## 実装（アクセス制御の担保）

（2026/07/14 実装 v2.0.2 と突き合わせ）本APIの認可は OAuth2 を基本とし、`require_api_auth(allow_anonymous=…)`（未認証許可可否）、`require_oauth_scopes(<scope>)`（トークン使用時のみスコープ検証）、`roles_required([...])`（未認証かつ guest_token 無しは 401）の組み合わせで判定される。ゲスト（未ログイン）可否は主に `allow_anonymous` と `roles_required` の有無で決まり、公開範囲は検索系では `weko_search_ui.query.get_permission_filter` で絞り込まれる。各エンドポイントの実ハンドラ・スコープは [API仕様（api カテゴリ）](../api/README.md) を参照。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                                 |
| ---------- | ------------------------------------------ | -------------------------------------------------------- |
| 2025/08/29 |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3      | 初版作成                                                 |
