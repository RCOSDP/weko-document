# インデックス検索用API

  - 目的・用途

インデックスIDを指定して、そのインデックスに属するアイテムを検索する機能を提供する。

  - 利用方法

| **Method** | **HTTP request**   | **Description** |
| ---------- | ------------------ | --------------- |
| GET        | **/api/index/**    | インデックス配下のアイテムを検索する |

クエリパラメータ

| **GET /api/index/** |    |     |             |
| ------------------------------ | -- | --- | ----------- |
| パラメータ | 必須 | 値 | 説明 |
| q | - | int | インデックスID（path）を指定する。未指定時はルート（"0"）扱い |
| page | - | int | ページ番号（既定1） |
| size | - | int | 1ページの件数（既定20） |
| is_search | - | - | 検索モード指定 |
| c | - | str | コミュニティID |

レスポンス例：

JSON形式。検索ヒット（`hits`）に加え、`aggregations` にインデックスツリー（path）ごとの集計（name / comment / 公開件数 / 非公開件数 / RSSステータス / サムネイル画像情報等）を含む。

  - 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | 〇 | 〇 | 〇 | 〇 | 〇 | 〇 |

（公開範囲は権限フィルタにより自動的に絞り込まれる。下記「処理概要」参照）

  - 機能内容

- 指定したインデックス（`q`＝インデックスID/path）に属するアイテムをElasticsearch/OpenSearchで検索し、結果とインデックスツリーの集計を返す。
- ログイン状態・ロールに応じて閲覧可能なアイテムのみを返す（オープンアクセス／非公開の出し分け）。

  - 関連モジュール

- weko-search-ui（`rest.py` の `IndexSearchResource`、検索ファクトリ `query.item_path_search_factory`（別名 `weko_search_factory`）、権限フィルタ `query.get_permission_filter`、REST定義 `config.WEKO_SEARCH_REST_ENDPOINTS`）
- weko-index-tree（`Indexes`：path・公開判定・ツリー集計）
- weko-records（検索レスポンスシリアライザ `serializers.json_v1_search`）
- invenio-search（`RecordsSearch`：ES実行）

  - 処理概要

1. エンドポイント `GET /api/index/`（Blueprint `weko_search_rest`、APIアプリの `/api` 配下にマウント）。ハンドラは `weko_search_ui.rest.IndexSearchResource.get`。
2. 検索ファクトリ `item_path_search_factory` が `q`（インデックスID/path）を条件にESクエリを構築する。
3. `get_permission_filter` により公開範囲を絞り込む（非管理者は `publish_status=public` かつ `publish_date <= now`、管理者は非公開も可、ログインユーザは自身が作成者／共有のアイテムも可視）。
4. レスポンスは JSON（`hits` ＋ `aggregations`）。

> 補足：同一Blueprintに `GET /api/v1/records`（`IndexSearchResourceAPI`）が存在するが、これはメタデータ検索用の別APIであり、本インデックス検索とは異なる（混同注意）。

  - 主要設定値

`WEKO_SEARCH_REST_ENDPOINTS`、`SEARCH_UI_SEARCH_INDEX`、`RECORDS_REST_SORT_OPTIONS`、`WEKO_SEARCH_TYPE_DICT`

  - 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/11/14 | V0.9.27 | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。エンドポイント`/api/index/`・ハンドラ・検索ファクトリ・権限フィルタ・レスポンス（hits+aggregations）・関連モジュール・処理概要を追記。クエリ表ヘッダの`/api/opensearch/search`誤記を修正 |
