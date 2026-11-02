# レコード・デポジットの登録・更新・削除

レコード・デポジットの REST API のうち、登録・更新・削除を行うメソッドのアクセスコントロールについて記述します。

## 1. 概要

- Invenio-Records-REST・Invenio-Deposit の REST エンドポイントのうち、レコードを登録・更新・削除するメソッドの権限を定める

- アイテムの登録・編集は、ワークフロー（アイテム登録画面）、SWORD API、一括インポート等の WEKO の経路で行う。`/api/records` 系のエンドポイントは参照（GET）専用とする

## 2. 対象エンドポイント

| エンドポイント | 定義 | メソッド |
| ---- | ---- | ---- |
| `/api/records/` | `RECORDS_REST_ENDPOINTS['recid']` の `list_route` | GET, POST |
| `/api/records/<pid_value>` | `RECORDS_REST_ENDPOINTS['recid']` の `item_route` | GET, PUT, PATCH, DELETE |
| `/api/opensearch/search` | `RECORDS_REST_ENDPOINTS['opensearch']` の `list_route` | GET, POST |
| `/api/workspace/search` | `RECORDS_REST_ENDPOINTS['worksapce']` の `list_route` | GET, POST |
| `/api/deposits/items` | `DEPOSIT_REST_ENDPOINTS['depid']`（`WEKO_DEPOSIT_REST_ENDPOINTS`）の `list_route` | GET, POST |
| `/api/deposits/items/<pid_value>` | 同上の `item_route` | GET, PUT, PATCH, DELETE |
| `/api/deposits/items/<pid_value>/actions/<action>` | 同上の `actions` ルート（`<action>`＝`edit`・`discard`） | POST |

## 3. 権限

○：利用可、×：利用不可（括弧内は HTTP ステータス）

### 3-1. `/api/records`・`/api/opensearch/search`・`/api/workspace/search` の POST、`/api/records/<pid_value>` の PUT・PATCH・DELETE（ID：RW-R-01）

| ロール | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | ×（403） | ×（403） | ×（403） | ×（403） | ×（403） | ×（401） |

- `create_permission_factory_imp`・`update_permission_factory_imp`・`delete_permission_factory_imp` に `invenio_records_rest.utils:deny_all` を設定する（weko-search-ui の `config.py`）

- GET（検索・参照）の権限は変更しない（[アイテム API](./API_ITEM_01.md)、[OpenSearch API](./API_OPEN_SEARCH_01.md) を参照）

### 3-2. `POST /api/deposits/items`（ID：RW-D-01）

| ロール | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ログイン済み | ○ | ○ | ○ | ○ | ○ | － |
| ゲストセッションあり | － | － | － | － | － | ○ |
| ゲストセッションなし | － | － | － | － | － | ×（401） |

- デコレータ `weko_accounts.utils:login_required_customize` で判定する。ゲストセッションは [ゲストトークンの発行・受付設定](../other/GUEST_TOKEN_01.md) の受付が有効な場合のみ存在する

- GET の権限は変更しない

### 3-3. `PUT`・`PATCH /api/deposits/items/<pid_value>`（ID：RW-D-02）

| 条件 / ロール | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| アイテムの編集権限あり | ○ | ○ | ○ | ○ | ○ | － |
| アイテムの編集権限なし | － | － | ×（403） | ×（403） | ×（403） | ×（401） |
| アイテムが存在しない | ×（404） | ×（404） | ×（404） | ×（404） | ×（404） | ×（401） |

- デコレータ `weko_deposit.rest:require_item_edit_permission` で判定する。編集権限は `weko_items_ui.permissions.edit_permission_factory`（作成者・所有者・共有ユーザー・システム管理者・リポジトリ管理者・当該アイテムのコミュニティのコミュニティ管理者）とする

- バージョン付きの `pid_value`（例：`1.1`）は親の recid で判定する

- GET の権限は変更しない。DELETE は従来どおり `deny_all`

### 3-4. `POST /api/deposits/items/<pid_value>/actions/<action>`（`edit`・`discard`）（ID：RW-D-03）

| 条件 / ロール | システム<br>管理者 | リポジトリ<br>管理者 | コミュニティ<br>管理者 | 登録ユーザー | 一般ユーザー | ゲスト<br>（未ログイン） |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| アイテムの編集権限あり | ○ | ○ | ○ | ○ | ○ | － |
| アイテムの編集権限なし | － | － | ×（403） | ×（403） | ×（403） | ×（401） |
| アイテムが存在しない | ×（404） | ×（404） | ×（404） | ×（404） | ×（404） | ×（401） |

- `actions` ルート（編集開始＝`edit`・破棄＝`discard`）の POST にも、RW-D-02 と同じデコレータ `weko_deposit.rest:require_item_edit_permission` を適用する。判定内容（`edit_permission_factory`・バージョン付き pid の親 recid 判定）は RW-D-02 と同じ

## 4. 判定の順序

- RW-D-01・RW-D-02・RW-D-03 のデコレータは、Invenio-Records-REST の権限ファクトリより先に実行する。デコレータで拒否した場合、ビューの処理（レコードの作成・更新・編集開始・破棄）は行わない

- デコレータは対象のメソッドにのみ適用する（POST：`list_route`・`actions` ルート、PUT・PATCH：`item_route`）。同じルートの GET 等には適用しない

- 判定を権限ファクトリ（`*_permission_factory_imp`）ではなくデコレータで行うのは、次の理由による（`weko_deposit.rest:require_item_edit_permission` の実装による）

  - 対象ビューは `ContentNegotiatedMethodView` で、ビュー本体が例外補足（`try`）に包まれている。ビュー内部で `abort` すると、その例外が本体側の補足に取り込まれて想定と異なる応答になる。判定をビューの外側（デコレータ）に置くことでこれを避ける

  - 未ログインの扱いを `@login_required` に任せると、UI アプリの文脈ではログイン画面への 302 応答が返り、その応答が `make_response(*result)` に渡されて `(pid, record)` として展開されるため型が合わなくなる。デコレータ内で 401 を送出することで、未ログインを 401、編集権限なしを 403 と明確に分ける

## 5. 設定

- `DEPOSIT_REST_ENDPOINTS` の各エンドポイントに、次のオプションを指定できる（invenio-deposit の `views/rest.py` `create_blueprint`）

  | オプション | 適用先 | 値 |
  | ---- | ---- | ---- |
  | `create_decorators` | `list_route` の POST | デコレータ、またはそのインポート文字列のリスト |
  | `update_decorators` | `item_route` の PUT・PATCH | 同上 |
  | `action_decorators` | `actions` ルートの POST | 同上 |

- リストの先頭のデコレータが最も外側（最初に実行）となる

## 6. 関連モジュール

- invenio-deposit（`views/rest.py`：`create_blueprint`・`decorate_view`）

- weko-deposit（`config.py`：`DEPOSIT_REST_ENDPOINTS`、`rest.py`：`require_item_edit_permission`）

- weko-search-ui（`config.py`：`RECORDS_REST_ENDPOINTS`）

- weko-accounts（`utils.py`：`login_required_customize`）

## 7. テスト観点

| 観点 | 確認内容 | 対応 ID・節 |
| ---- | ---- | ---- |
| 登録・更新・削除の拒否 | 各エンドポイント・メソッドについて、未ログインは 401、ログインユーザ（システム管理者を含む）は 403 となり、レコードが変更されない | RW-R-01 |
| 参照の回帰 | `/api/records` 等の GET（検索・詳細）が従来どおり利用できる | RW-R-01 |
| デポジット登録 | 未ログインかつゲストセッションなしは 401、ログイン済み・ゲストセッションありは登録できる | RW-D-01 |
| デポジット更新 | PUT・PATCH それぞれについて、未ログイン 401、編集権限なし 403、存在しない 404、編集権限ありは更新できる | RW-D-02 |
| デポジットのアクション | `actions`（`edit`・`discard`）の POST について、未ログイン 401、編集権限なし 403、存在しない 404、編集権限ありは実行できる | RW-D-03 |
| バージョン付き pid | `<recid>.<version>` の PUT・PATCH・`actions` POST を親の recid の編集権限で判定する | RW-D-02・RW-D-03 |
| メソッドの限定 | デコレータが GET 等の対象外メソッドに影響しない | 4 |
| 既存経路の回帰 | アイテム登録画面・アイテム編集・SWORD API・一括インポートによる登録・編集が従来どおり完了する | 1 |
| オプション | `create_decorators`・`update_decorators` 未指定のエンドポイントは従来どおり動作する。指定順に適用される | 5 |

## 8. 更新履歴

| 日付 | 更新内容 |
| ---- | ---- |
| （リリース日） | 新規作成（<リリース版>） |
| 2026/11/02 | `actions` ルート（`edit`・`discard`）の POST と `action_decorators` オプションを追記（RW-D-03）。権限ファクトリではなくデコレータで判定する理由（ビュー本体の例外補足・`make_response` の展開と 401/403 の分離）を §4 に追記 |
