# モジュール索引（逆引きリファレンス）

WEKO3 を構成する各モジュールが「何をするか」と、「そのモジュールを扱う機能仕様はどれか」を
逆引きするための索引である。ある実装モジュールに手を入れる際、影響範囲となる機能仕様を素早く辿れる。

- **順引き（機能 → モジュール）** は各機能仕様の「関連モジュール」節を参照。
- **逆引き（モジュール → 機能）** が本ページ。各機能仕様の「関連モジュール」節を機械集計して生成している。
- モジュール実装は `/home/mhaya/weko/modules/<モジュール名>/` にある。突き合わせ基準は tag `v2.0.2`。
- 利用ライブラリ・パッケージの一覧は [その他 › モジュール、ライブラリ](other/MODULE_01.md) を参照。
- 全体像・レイヤ構造は [アーキテクチャ全体像](ARCHITECTURE.md)、変更作業の入口は [開発者ガイド](DEV_GUIDE.md) を参照。

各モジュールの「主なファイル」は Blueprint／REST／モデル／Celery タスク／設定などの標準的な入口
（`views.py` `rest.py` `api.py` `models.py` `tasks.py` `config.py` `permissions.py` `utils.py`）を示す。

> このページは `spec/tools/generate_module_index.py` で再生成できる（`python3 spec/tools/generate_module_index.py`）。
> 機能仕様の「関連モジュール」節を編集したら、本スクリプトを実行して逆引きを更新すること。
> モジュールの1行説明はスクリプト内の `DESC` を人手で維持する。

> 「関連モジュールに挙げる機能仕様」は当該仕様の「関連モジュール」節で明示されているもの。
> 「本文中で言及する機能仕様」は節外の本文でモジュール名に言及があるもの（参考）。

---

## WEKO 独自モジュール（`weko-*`）

WEKO3 が Invenio3 上に独自実装した機能群。開発の主対象はほぼこの層にある。

### `weko-accounts`

WEKO 独自の認証連携（Shibboleth／セキュリティ設定）を invenio-accounts に付加。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-accounts/`
- このモジュールを「関連モジュール」に挙げる機能仕様（3件）:
    - 管理機能: [Shibboleth](admin/ADMIN_14_19.md)
    - WebAPI: [Index操作API](api/API_05_index_op.md)
    - ユーザ機能: [ログイン](user/USER_8_2.md)
- 本文中で言及する機能仕様: 9件

### `weko-admin`

管理画面全般（各種設定／運用統計レポート／ログ解析／サイト情報／メール等）の中核。

- 主なファイル: `views.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-admin/`
- このモジュールを「関連モジュール」に挙げる機能仕様（35件）:
    - 管理機能: [識別子](admin/ADMIN_14_8.md) / [一括エクスポート](admin/ADMIN_2_3.md) / [サイト情報](admin/ADMIN_14_13.md) / [ランキング表示](admin/ADMIN_14_5.md) / [統計情報表示](admin/ADMIN_14_6.md) / [WebAPIアカウント](admin/ADMIN_14_17.md) / [アイテム一括出力](admin/ADMIN_14_9.md) / [サイトライセンス](admin/ADMIN_6_3.md) / [制限公開(v1.0.7追加)](admin/ADMIN_14_20.md) / [SWORD API JSON-LD](admin/ADMIN_16_2.md) / [エクスポート (基本監査ログ)](admin/ADMIN_17_1.md) / [RO-Crate インポート](admin/ADMIN_2_5.md) / [フィードバックメール](admin/ADMIN_6_2.md) / [SWORD API TSV/XML](admin/ADMIN_16_1.md) / [インポート](admin/ADMIN_2_4.md) / [ログ解析](admin/ADMIN_14_10.md) / [運用レポート](admin/ADMIN_6_1.md) / [サイトライセンス](admin/ADMIN_14_14.md) / [Elasticsearchインデックス](admin/ADMIN_15_1.md) / [プロフィール設定編集機能](admin/ADMIN_18_1.md) / [ファイルプレビュー](admin/ADMIN_14_18.md) / [JSON-LD マッピング](admin/ADMIN_1_5.md) / [言語表示](admin/ADMIN_14_3.md) / [ファセット検索](admin/ADMIN_14_12.md) / [検索設定](admin/ADMIN_14_11.md)
    - WebAPI: [Index操作API](api/API_05_index_op.md) / [アイテム検索用API](api/API_12_item_search_RO-Crate.md)
    - 制限公開: [ワークフロー管理（制限公開）](restricted_access/RESTRICTED_ACCESS_03.md) / [プロフィール表示設定](restricted_access/RESTRICTED_ACCESS_05.md) / [メールテンプレート](restricted_access/RESTRICTED_ACCESS_04.md) / [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md)
    - ユーザ機能: [ワークスペース：アイテム一覧情報取得](user/USER_10_1.md) / [言語切替](user/USER_7_2.md) / [ランキング](user/USER_6_1.md) / [Item Registration：フィードバックメール機能](user/USER_4_8.md)
- 本文中で言及する機能仕様: 41件

### `weko-authors`

著者DB（著者の編集／一括登録・出力／名寄せ／外部著者ID prefix）。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-authors/`
- このモジュールを「関連モジュール」に挙げる機能仕様（5件）:
    - 管理機能: [編集](admin/ADMIN_5_1.md) / [ADMIN-5-1-3:Affiliation ID](admin/ADMIN_5_1_3.md) / [一括出力](admin/ADMIN_5_2.md) / [一括登録](admin/ADMIN_5_3.md) / [外部著者ID Prefix](admin/ADMIN_5_4.md)
- 本文中で言及する機能仕様: 7件

### `weko-bulkupdate`

アイテムの一括更新機能。※現状は cookiecutter 雛形のまま実機能を持たない。実際の一括更新は [ADMIN-2-1: 一括更新](admin/ADMIN_2_1.md)（`weko-search-ui` / `weko-index-tree` / `weko-deposit`）が担う。

- 主なファイル: `views.py`, `config.py`
- 実装: `modules/weko-bulkupdate/`
- 本文中で言及する機能仕様: 1件

### `weko-deposit`

アイテム登録の中核。メタデータ整形と Elasticsearch への投入、ファイル情報の DB 格納を担う（invenio-deposit を拡張）。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `tasks.py`, `config.py`, `utils.py`
- 実装: `modules/weko-deposit/`
- このモジュールを「関連モジュール」に挙げる機能仕様（12件）:
    - 管理機能: [編集](admin/ADMIN_5_1.md) / [RO-Crate インポート](admin/ADMIN_2_5.md) / [一括更新](admin/ADMIN_2_1.md)
    - WebAPI: [OAI-PMH 2.0](api/API_02_OAIPMH.md)
    - その他/データ構造: [Form](other/SCHEMA_1_3.md)
    - 制限公開: [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md) / [アイテムタイプ管理（制限公開）](restricted_access/RESTRICTED_ACCESS_01.md)
    - ユーザ機能: [Item Registration](user/USER_4_4.md) / [Item Registration：ファイルアップロード](user/USER_4_5.md) / [Item Registration：インデックス指定](user/USER_4_9.md) / [メタデータ表示](user/USER_3_1.md) / [ワークスペース：簡易アイテム登録機能](user/USER_10_2.md)
- 本文中で言及する機能仕様: 9件

### `weko-gridlayout`

ウェブデザイン管理（ウィジェット／ページレイアウト）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-gridlayout/`
- このモジュールを「関連モジュール」に挙げる機能仕様（3件）:
    - 管理機能: [ウィジェット](admin/ADMIN_4_1.md) / [ページレイアウト](admin/ADMIN_4_2.md)
    - ユーザ機能: [RSS](user/USER_1_5.md)
- 本文中で言及する機能仕様: 2件

### `weko-groups`

ユーザグループの管理（GakuNin mAP 連携によるグループ取込を含む）。

- 主なファイル: `views.py`, `api.py`, `models.py`
- 実装: `modules/weko-groups/`
- 本文中で言及する機能仕様: 3件

### `weko-handle`

CNRI Handle による永続識別子の発行。

- 主なファイル: `views.py`, `api.py`, `config.py`
- 実装: `modules/weko-handle/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - ユーザ機能: [Identifier Grant](user/USER_4_10.md)
- 本文中で言及する機能仕様: 3件

### `weko-index-tree`

インデックスツリー（分類階層）の管理・表示・権限判定。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-index-tree/`
- このモジュールを「関連モジュール」に挙げる機能仕様（9件）:
    - 管理機能: [カスタムソート](admin/ADMIN_3_3.md) / [一括更新](admin/ADMIN_2_1.md) / [インデックスリンク表示](admin/ADMIN_14_2.md)
    - WebAPI: [Index操作API](api/API_05_index_op.md) / [OAI-PMH 2.0](api/API_02_OAIPMH.md)
    - ユーザ機能: [目次形式表示](user/USER_2_2.md) / [インデックス検索](user/USER_1_3.md) / [RSS](user/USER_1_5.md) / [所属コミュニティ情報表示](user/USER_3_10.md)
- 本文中で言及する機能仕様: 9件

### `weko-indextree-journal`

インデックスに紐づく雑誌情報の管理。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`
- 実装: `modules/weko-indextree-journal/`
- このモジュールを「関連モジュール」に挙げる機能仕様（2件）:
    - 管理機能: [雑誌情報](admin/ADMIN_3_2.md)
    - ユーザ機能: [雑誌情報](user/USER_2_3.md)
- 本文中で言及する機能仕様: 2件

### `weko-items-autofill`

メタデータ自動補完（CrossRef／CiNii 等、外部IDからの取得）。

- 主なファイル: `views.py`, `api.py`, `config.py`, `permissions.py`, `utils.py`
- 実装: `modules/weko-items-autofill/`
- このモジュールを「関連モジュール」に挙げる機能仕様（4件）:
    - 管理機能: [RO-Crate インポート](admin/ADMIN_2_5.md) / [インポート](admin/ADMIN_2_4.md)
    - ユーザ機能: [ワークスペース：メタデータ自動補完機能](user/USER_10_3.md) / [Item Registration：メタデータ入力](user/USER_4_6.md)
- 本文中で言及する機能仕様: 2件

### `weko-items-ui`

アイテム登録・編集 UI およびエクスポート／インポートの UI。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `utils.py`
- 実装: `modules/weko-items-ui/`
- このモジュールを「関連モジュール」に挙げる機能仕様（21件）:
    - 管理機能: [ランキング表示](admin/ADMIN_14_5.md) / [CRIS連携](admin/ADMIN_14_23.md)
    - その他/データ構造: [Schema](other/SCHEMA_1_2.md) / [Form](other/SCHEMA_1_3.md)
    - 制限公開: [アイテムタイプ管理（制限公開）](restricted_access/RESTRICTED_ACCESS_01.md)
    - ユーザ機能: [Item Registration](user/USER_4_4.md) / [目次形式表示](user/USER_2_2.md) / [ランキング](user/USER_6_1.md) / [Item Registration：コンテンツ未登録時の制限公開機能](user/USER_4_16.md) / [アイテム一括出力](user/USER_2_4.md) / [一覧形式表示](user/USER_2_1.md) / [Item Registration：インデックス指定](user/USER_4_9.md) / [Item Registration：リクエストメール機能](user/USER_4_17.md) / [ワークスペース：メタデータ自動補完機能](user/USER_10_3.md) / [RSS](user/USER_1_5.md) / [USER-1-1: 簡易検索（全文検索・キーワード検索）](user/USER_1_1.md) / [詳細検索](user/USER_1_2.md) / [ワークスペース：簡易アイテム登録機能](user/USER_10_2.md) / [Item Registration：代理投稿](user/USER_4_7.md) / [ファセット検索](user/USER_1_4.md) / [Item Registration：メタデータ入力](user/USER_4_6.md)
- 本文中で言及する機能仕様: 19件

### `weko-itemtypes-ui`

アイテムタイプ・メタデータ・マッピング・プロパティ定義の UI。

- 主なファイル: `views.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-itemtypes-ui/`
- このモジュールを「関連モジュール」に挙げる機能仕様（8件）:
    - 管理機能: [プロパティ](admin/ADMIN_1_4.md) / [マッピング](admin/ADMIN_1_2.md) / [メタデータ](admin/ADMIN_1_1.md)
    - WebAPI: [Render](api/API_09_render.md)
    - その他/データ構造: [Render](other/SCHEMA_1_1.md)
    - 制限公開: [アイテムタイプ管理（制限公開）](restricted_access/RESTRICTED_ACCESS_01.md)
    - ツール: [Render](tools/TOOL_01.md)
    - ユーザ機能: [メタデータ表示](user/USER_3_1.md)
- 本文中で言及する機能仕様: 3件

### `weko-logging`

ロギング（ファイル／DB）の基盤。

- 主なファイル: `views.py`, `models.py`, `tasks.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-logging/`
- このモジュールを「関連モジュール」に挙げる機能仕様（2件）:
    - 管理機能: [エクスポート (基本監査ログ)](admin/ADMIN_17_1.md)
    - その他/データ構造: [基本監査ログ](other/USER_ACTIVITY_LOG.md)
- 本文中で言及する機能仕様: 6件

### `weko-notifications`

COAR Notify 準拠のプッシュ通知（inbox）機能。

- 主なファイル: `views.py`, `models.py`, `config.py`, `utils.py`
- 実装: `modules/weko-notifications/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - その他/データ構造: [登録完了・承認通知機能](other/INBOX_01.md)
- 本文中で言及する機能仕様: 3件

### `weko-plugins`

プラグイン機構（flask_plugins）。

- 主なファイル: `views.py`, `config.py`, `admin.py`
- 実装: `modules/weko-plugins/`
- 本文中で言及する機能仕様: 1件

### `weko-records`

レコード（メタデータ）とアイテムタイプ／マッピングのモデル・API 中核（invenio-records を拡張）。

- 主なファイル: `rest.py`, `api.py`, `models.py`, `config.py`, `utils.py`
- 実装: `modules/weko-records/`
- このモジュールを「関連モジュール」に挙げる機能仕様（39件）:
    - 管理機能: [一括削除](admin/ADMIN_2_2.md) / [統計情報表示](admin/ADMIN_14_6.md) / [レコードメタデータ](admin/ADMIN_11_2.md) / [アイテム表示](admin/ADMIN_14_1.md) / [RO-Crate インポート](admin/ADMIN_2_5.md) / [その他](admin/ADMIN_14_21.md) / [フィードバックメール](admin/ADMIN_6_2.md) / [一括更新](admin/ADMIN_2_1.md) / [JSON-LD マッピング](admin/ADMIN_1_5.md) / [PDFカバーページ表示](admin/ADMIN_14_4.md)
    - WebAPI: [SWORD API](api/API_06_sword_api.md) / [アイテム検索用API](api/API_12_item_search_RO-Crate.md) / [OAI-PMH 2.0](api/API_02_OAIPMH.md)
    - その他/データ構造: [Schema](other/SCHEMA_1_2.md) / [Render](other/SCHEMA_1_1.md) / [Form](other/SCHEMA_1_3.md) / [Signposting（FAIR Signposting）](other/SIGNPOSTING_01.md)
    - 制限公開: [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md) / [アイテムタイプ管理（制限公開）](restricted_access/RESTRICTED_ACCESS_01.md)
    - ツール: [Render](tools/TOOL_01.md)
    - ユーザ機能: [ワークスペース：アイテム一覧情報取得](user/USER_10_1.md) / [目次形式表示](user/USER_2_2.md) / [Google Scholar メタデータ出力](user/USER_3_8.md) / [共有](user/USER_3_6.md) / [一覧形式表示](user/USER_2_1.md) / [Item Registration：ファイルアップロード](user/USER_4_5.md) / [Item Registration：フィードバックメール機能](user/USER_4_8.md) / [Item Link](user/USER_4_11.md) / [統計情報表示](user/USER_3_5.md) / [メタデータ表示](user/USER_3_1.md) / [RSS](user/USER_1_5.md) / [アイテムバージョン管理](user/USER_3_3.md) / [Google Dataset メタデータ出力](user/USER_3_9.md) / [USER-1-1: 簡易検索（全文検索・キーワード検索）](user/USER_1_1.md) / [引用情報表示](user/USER_3_4.md) / [所属コミュニティ情報表示](user/USER_3_10.md) / [コンテンツファイル管理](user/USER_3_2.md) / [アイテム利用申請機能](user/USER_3_13.md) / [リクエスト機能](user/USER_3_11.md)
- 本文中で言及する機能仕様: 39件

### `weko-records-ui`

アイテム詳細表示・ファイル配信・アクセス制御・利用申請入口・引用／統計表示。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-records-ui/`
- このモジュールを「関連モジュール」に挙げる機能仕様（26件）:
    - 管理機能: [一括削除](admin/ADMIN_2_2.md) / [統計情報表示](admin/ADMIN_14_6.md) / [レコードメタデータ](admin/ADMIN_11_2.md) / [アイテム表示](admin/ADMIN_14_1.md) / [その他](admin/ADMIN_14_21.md) / [一括更新](admin/ADMIN_2_1.md) / [PDFカバーページ表示](admin/ADMIN_14_4.md)
    - WebAPI: [SWORD API](api/API_06_sword_api.md) / [アイテム検索用API](api/API_12_item_search_RO-Crate.md)
    - その他/データ構造: [Signposting（FAIR Signposting）](other/SIGNPOSTING_01.md)
    - 制限公開: [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md) / [アイテムタイプ管理（制限公開）](restricted_access/RESTRICTED_ACCESS_01.md)
    - ユーザ機能: [目次形式表示](user/USER_2_2.md) / [Google Scholar メタデータ出力](user/USER_3_8.md) / [共有](user/USER_3_6.md) / [一覧形式表示](user/USER_2_1.md) / [Item Registration：ファイルアップロード](user/USER_4_5.md) / [統計情報表示](user/USER_3_5.md) / [メタデータ表示](user/USER_3_1.md) / [アイテムバージョン管理](user/USER_3_3.md) / [Google Dataset メタデータ出力](user/USER_3_9.md) / [引用情報表示](user/USER_3_4.md) / [所属コミュニティ情報表示](user/USER_3_10.md) / [コンテンツファイル管理](user/USER_3_2.md) / [アイテム利用申請機能](user/USER_3_13.md) / [リクエスト機能](user/USER_3_11.md)
- 本文中で言及する機能仕様: 26件

### `weko-redis`

Redis 接続ヘルパ。

- 実装: `modules/weko-redis/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - 管理機能: [ログ解析](admin/ADMIN_14_10.md)
- 本文中で言及する機能仕様: 3件

### `weko-schema-ui`

メタデータスキーマ（OAI／JPCOAR 等）とマッピングによる出力生成。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-schema-ui/`
- このモジュールを「関連モジュール」に挙げる機能仕様（6件）:
    - 管理機能: [OAIスキーマ](admin/ADMIN_1_3.md)
    - WebAPI: [OAI-PMH 2.0](api/API_02_OAIPMH.md)
    - ユーザ機能: [エクスポート](user/USER_3_7.md) / [RSS](user/USER_1_5.md) / [詳細検索](user/USER_1_2.md) / [ファセット検索](user/USER_1_4.md)
- 本文中で言及する機能仕様: 4件

### `weko-search-ui`

検索結果表示・ファセット・インポート／一括処理・検索設定。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-search-ui/`
- このモジュールを「関連モジュール」に挙げる機能仕様（22件）:
    - 管理機能: [一括エクスポート](admin/ADMIN_2_3.md) / [一括削除](admin/ADMIN_2_2.md) / [カスタムソート](admin/ADMIN_3_3.md) / [エクスポート (基本監査ログ)](admin/ADMIN_17_1.md) / [RO-Crate インポート](admin/ADMIN_2_5.md) / [フィードバックメール](admin/ADMIN_6_2.md) / [インポート](admin/ADMIN_2_4.md) / [一括更新](admin/ADMIN_2_1.md) / [JSON-LD マッピング](admin/ADMIN_1_5.md)
    - WebAPI: [SWORD API](api/API_06_sword_api.md) / [アイテム検索用API](api/API_12_item_search_RO-Crate.md)
    - その他/データ構造: [利用統計ログ](other/USAGE_LOG.md)
    - ユーザ機能: [ワークスペース：アイテム一覧情報取得](user/USER_10_1.md) / [目次形式表示](user/USER_2_2.md) / [一覧形式表示](user/USER_2_1.md) / [インデックス検索](user/USER_1_3.md) / [Item Link](user/USER_4_11.md) / [RSS](user/USER_1_5.md) / [USER-1-1: 簡易検索（全文検索・キーワード検索）](user/USER_1_1.md) / [詳細検索](user/USER_1_2.md) / [雑誌情報](user/USER_2_3.md) / [ファセット検索](user/USER_1_4.md)
- 本文中で言及する機能仕様: 32件

### `weko-signposting`

FAIR Signposting（アイテム詳細への HTTP Link ヘッダ付与。rel=cite-as／describedby）。

- 主なファイル: `views.py`, `api.py`, `config.py`
- 実装: `modules/weko-signposting/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - その他/データ構造: [Signposting（FAIR Signposting）](other/SIGNPOSTING_01.md)
- 本文中で言及する機能仕様: 2件

### `weko-sitemap`

sitemap.xml の生成。

- 主なファイル: `views.py`, `tasks.py`, `config.py`, `admin.py`
- 実装: `modules/weko-sitemap/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - 管理機能: [サイトマップ](admin/ADMIN_14_15.md)
- 本文中で言及する機能仕様: 2件

### `weko-swordserver`

SWORD（v3）によるアイテム受入 API。

- 主なファイル: `views.py`, `api.py`, `models.py`, `config.py`, `utils.py`
- 実装: `modules/weko-swordserver/`
- このモジュールを「関連モジュール」に挙げる機能仕様（5件）:
    - 管理機能: [SWORD API JSON-LD](admin/ADMIN_16_2.md) / [RO-Crate インポート](admin/ADMIN_2_5.md) / [SWORD API TSV/XML](admin/ADMIN_16_1.md)
    - WebAPI: [SWORD API](api/API_06_sword_api.md)
    - その他/データ構造: [登録完了・承認通知機能](other/INBOX_01.md)
- 本文中で言及する機能仕様: 3件

### `weko-theme`

サイトのテーマ・トップページ・共通レイアウト。

- 主なファイル: `views.py`, `config.py`, `utils.py`
- 実装: `modules/weko-theme/`
- このモジュールを「関連モジュール」に挙げる機能仕様（10件）:
    - 管理機能: [画面背景色](admin/ADMIN_14_7.md) / [カスタムソート](admin/ADMIN_3_3.md)
    - ユーザ機能: [インデックス検索](user/USER_1_3.md) / [Cookie使用確認画面表示](user/USER_9_1.md) / [RSS](user/USER_1_5.md) / [USER-1-1: 簡易検索（全文検索・キーワード検索）](user/USER_1_1.md) / [詳細検索](user/USER_1_2.md) / [コンテンツポリシー](user/USER_5_2.md) / [ファセット検索](user/USER_1_4.md) / [コミュニティ](user/USER_5_1.md)
- 本文中で言及する機能仕様: 5件

### `weko-user-profiles`

ユーザプロファイル（表示名／所属等）の管理。

- 主なファイル: `views.py`, `api.py`, `models.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-user-profiles/`
- このモジュールを「関連モジュール」に挙げる機能仕様（4件）:
    - 管理機能: [ユーザープロファイル](admin/ADMIN_13_12.md)
    - 制限公開: [プロフィール表示設定](restricted_access/RESTRICTED_ACCESS_05.md)
    - ユーザ機能: [ワークスペース：アイテム一覧情報取得](user/USER_10_1.md) / [ユーザープロファイル設定](user/USER_8_4.md)
- 本文中で言及する機能仕様: 2件

### `weko-workflow`

登録・利用申請等のワークフロー（アクティビティ／フロー／承認／Identifier付与／フィードバックメール）の中核。

- 主なファイル: `views.py`, `rest.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/weko-workflow/`
- このモジュールを「関連モジュール」に挙げる機能仕様（27件）:
    - 管理機能: [ワークフロー](admin/ADMIN_7_2.md) / [ワークスペース設定](admin/ADMIN_7_3.md) / [SWORD API JSON-LD](admin/ADMIN_16_2.md) / [フロー](admin/ADMIN_7_1.md)
    - WebAPI: [SWORD API](api/API_06_sword_api.md)
    - その他/データ構造: [利用統計ログ](other/USAGE_LOG.md) / [登録完了・承認通知機能](other/INBOX_01.md)
    - 制限公開: [ワークフロー管理（制限公開）](restricted_access/RESTRICTED_ACCESS_03.md) / [プロフィール表示設定](restricted_access/RESTRICTED_ACCESS_05.md) / [メールテンプレート](restricted_access/RESTRICTED_ACCESS_04.md) / [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md) / [アイテムタイプ管理（制限公開）](restricted_access/RESTRICTED_ACCESS_01.md)
    - ユーザ機能: [Item Registration](user/USER_4_4.md) / [ワークフロー](user/USER_4_3.md) / [OA Policy Confirmation（現在非対応）](user/USER_4_12.md) / [Item Registration：ファイルアップロード](user/USER_4_5.md) / [Item Registration：フィードバックメール機能](user/USER_4_8.md) / [Item Registration：インデックス指定](user/USER_4_9.md) / [Item Link](user/USER_4_11.md) / [ワークフロー一覧表示](user/USER_4_2.md) / [Identifier Grant](user/USER_4_10.md) / [Approval](user/USER_4_13.md) / [所属コミュニティ情報表示](user/USER_3_10.md) / [ワークスペース：簡易アイテム登録機能](user/USER_10_2.md) / [Item Registration：代理投稿](user/USER_4_7.md) / [アイテム利用申請機能](user/USER_3_13.md) / [Item Registration：メタデータ入力](user/USER_4_6.md)
- 本文中で言及する機能仕様: 16件

### `weko-workspace`

ワークスペース（簡易アイテム登録／一覧取得／メタデータ自動補完）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `config.py`, `utils.py`
- 実装: `modules/weko-workspace/`
- このモジュールを「関連モジュール」に挙げる機能仕様（3件）:
    - 制限公開: [プロフィール表示設定](restricted_access/RESTRICTED_ACCESS_05.md)
    - ユーザ機能: [ワークスペース：アイテム一覧情報取得](user/USER_10_1.md) / [ワークスペース：メタデータ自動補完機能](user/USER_10_3.md)
- 本文中で言及する機能仕様: 4件

---

## Invenio 基盤モジュール（`invenio-*`）

WEKO3 が土台とする Invenio3 のモジュール群。フレームワークの挙動を変える際に参照する。
これらは上流（inveniosoftware）由来だが、WEKO3 リポジトリ内で改変されているものもある。

### `invenio-accounts`

ユーザ管理・認証の基盤（ログイン／セッション／ロール）。Flask-Security/Flask-Login ベース。

- 主なファイル: `models.py`, `tasks.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-accounts/`
- このモジュールを「関連モジュール」に挙げる機能仕様（6件）:
    - 管理機能: [セッションアクティビティ](admin/ADMIN_13_10.md) / [ロール](admin/ADMIN_13_9.md) / [ユーザー](admin/ADMIN_13_11.md)
    - ユーザ機能: [パスワードリセット](user/USER_8_3.md) / [ログイン](user/USER_8_2.md) / [サインアップ](user/USER_8_1.md)
- 本文中で言及する機能仕様: 3件

### `invenio-communities`

コミュニティ（サブリポジトリ）機能の基盤。

- 主なファイル: `models.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-communities/`
- このモジュールを「関連モジュール」に挙げる機能仕様（6件）:
    - 管理機能: [コミュニティ](admin/ADMIN_8_1.md) / [注目のコミュニティ](admin/ADMIN_8_2.md) / [参加リクエスト](admin/ADMIN_8_3.md)
    - ユーザ機能: [所属コミュニティ情報表示](user/USER_3_10.md) / [コンテンツポリシー](user/USER_5_2.md) / [コミュニティ](user/USER_5_1.md)
- 本文中で言及する機能仕様: 2件

### `invenio-db`

SQLAlchemy によるDB接続・マイグレーション管理の基盤。

- 主なファイル: `config.py`, `utils.py`
- 実装: `modules/invenio-db/`
- 本文中で言及する機能仕様: 2件

### `invenio-deposit`

レコードの deposit（登録）とファイルアップロードの REST 基盤。

- 主なファイル: `api.py`, `config.py`, `permissions.py`, `utils.py`
- 実装: `modules/invenio-deposit/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - WebAPI: [SWORD API](api/API_06_sword_api.md)
- 本文中で言及する機能仕様: 2件

### `invenio-files-rest`

ファイルのアップロード／ダウンロード REST（バケット／オブジェクト／ロケーション。S3類似API）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-files-rest/`
- このモジュールを「関連モジュール」に挙げる機能仕様（11件）:
    - 管理機能: [オブジェクトバージョン](admin/ADMIN_12_5.md) / [一括エクスポート](admin/ADMIN_2_3.md) / [マルチパートオブジェクト](admin/ADMIN_12_4.md) / [バケット](admin/ADMIN_12_1.md) / [ファイルインスタンス](admin/ADMIN_12_2.md) / [エクスポート (基本監査ログ)](admin/ADMIN_17_1.md) / [ロケーション](admin/ADMIN_12_3.md) / [ファイルプレビュー](admin/ADMIN_14_18.md)
    - 制限公開: [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md)
    - ユーザ機能: [ファイルアップロード](user/USER_7_1.md) / [統計情報表示](user/USER_3_5.md)
- 本文中で言及する機能仕様: 6件

### `invenio-iiif`

IIIF 画像 API（画像プレビュー／変換）。

- 主なファイル: `views.py`, `tasks.py`, `config.py`, `utils.py`
- 実装: `modules/invenio-iiif/`
- 本文中で言及する機能仕様: 2件

### `invenio-indexer`

レコードの Elasticsearch インデクシング基盤。

- 主なファイル: `api.py`, `tasks.py`, `config.py`, `utils.py`
- 実装: `modules/invenio-indexer/`
- 本文中で言及する機能仕様: 1件

### `invenio-mail`

メール送信の基盤（Flask-Mail ラッパ）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `admin.py`
- 実装: `modules/invenio-mail/`
- このモジュールを「関連モジュール」に挙げる機能仕様（4件）:
    - 管理機能: [サイトライセンス](admin/ADMIN_6_3.md) / [メール送信](admin/ADMIN_14_16.md)
    - 制限公開: [メールテンプレート](restricted_access/RESTRICTED_ACCESS_04.md) / [アイテム詳細(制限公開)](restricted_access/RESTRICTED_ACCESS_02.md)
- 本文中で言及する機能仕様: 2件

### `invenio-oaiharvester`

OAI-PMH ハーベスト（他リポジトリからのメタデータ収集）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-oaiharvester/`
- このモジュールを「関連モジュール」に挙げる機能仕様（2件）:
    - 管理機能: [ハーベスト](admin/ADMIN_9_1.md)
    - その他/データ構造: [利用統計ログ](other/USAGE_LOG.md)
- 本文中で言及する機能仕様: 2件

### `invenio-oaiserver`

OAI-PMH サーバ（メタデータの外部提供）。

- 主なファイル: `api.py`, `models.py`, `tasks.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-oaiserver/`
- このモジュールを「関連モジュール」に挙げる機能仕様（3件）:
    - WebAPI: [OAI-PMH 2.0](api/API_02_OAIPMH.md)
    - その他/データ構造: [Signposting（FAIR Signposting）](other/SIGNPOSTING_01.md)
    - ユーザ機能: [エクスポート](user/USER_3_7.md)
- 本文中で言及する機能仕様: 6件

### `invenio-oauth2server`

OAuth2 サーバ（WebAPI のトークン／スコープ管理）。

- 主なファイル: `models.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-oauth2server/`
- このモジュールを「関連モジュール」に挙げる機能仕様（3件）:
    - 管理機能: [OAuthアプリケーション](admin/ADMIN_13_8.md) / [OAuthアプリケーショントークン](admin/ADMIN_13_7.md)
    - WebAPI: [SWORD API](api/API_06_sword_api.md)
- 本文中で言及する機能仕様: 7件

### `invenio-previewer`

ファイルプレビューの基盤。

- 主なファイル: `views.py`, `api.py`, `config.py`, `utils.py`
- 実装: `modules/invenio-previewer/`
- 本文中で言及する機能仕様: 2件

### `invenio-queues`

メッセージキュー（イベント）管理の基盤。

- 主なファイル: `config.py`, `utils.py`
- 実装: `modules/invenio-queues/`
- 本文中で言及する機能仕様: 1件

### `invenio-records`

メタデータ（レコード）格納の中核基盤。

- 主なファイル: `views.py`, `api.py`, `models.py`, `config.py`, `admin.py`
- 実装: `modules/invenio-records/`
- このモジュールを「関連モジュール」に挙げる機能仕様（6件）:
    - 管理機能: [レコードメタデータ](admin/ADMIN_11_2.md)
    - ユーザ機能: [一覧形式表示](user/USER_2_1.md) / [メタデータ表示](user/USER_3_1.md) / [エクスポート](user/USER_3_7.md) / [引用情報表示](user/USER_3_4.md) / [ファセット検索](user/USER_1_4.md)
- 本文中で言及する機能仕様: 9件

### `invenio-records-rest`

レコードの REST API 基盤。

- 主なファイル: `views.py`, `config.py`, `utils.py`
- 実装: `modules/invenio-records-rest/`
- このモジュールを「関連モジュール」に挙げる機能仕様（3件）:
    - ユーザ機能: [一覧形式表示](user/USER_2_1.md) / [引用情報表示](user/USER_3_4.md) / [ファセット検索](user/USER_1_4.md)
- 本文中で言及する機能仕様: 7件

### `invenio-resourcesyncclient`

ResourceSync クライアント（Resync による外部リソース取り込み）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `tasks.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-resourcesyncclient/`
- このモジュールを「関連モジュール」に挙げる機能仕様（1件）:
    - 管理機能: [Resync](admin/ADMIN_10_3.md)
- 本文中で言及する機能仕様: 3件

### `invenio-resourcesyncserver`

ResourceSync サーバ（Resource List／Change List の公開）。

- 主なファイル: `views.py`, `api.py`, `models.py`, `config.py`, `admin.py`, `utils.py`
- 実装: `modules/invenio-resourcesyncserver/`
- このモジュールを「関連モジュール」に挙げる機能仕様（2件）:
    - 管理機能: [Resource List](admin/ADMIN_10_1.md) / [Change List](admin/ADMIN_10_2.md)
- 本文中で言及する機能仕様: 2件

### `invenio-s3`

S3 互換オブジェクトストレージ対応。

- 主なファイル: `config.py`
- 実装: `modules/invenio-s3/`
- 本文中で言及する機能仕様: 1件

### `invenio-stats`

利用統計の収集・集計基盤（ES の events／aggregations）。

- 主なファイル: `views.py`, `models.py`, `tasks.py`, `config.py`, `permissions.py`, `utils.py`
- 実装: `modules/invenio-stats/`
- このモジュールを「関連モジュール」に挙げる機能仕様（10件）:
    - 管理機能: [ランキング表示](admin/ADMIN_14_5.md) / [統計情報表示](admin/ADMIN_14_6.md) / [サイトライセンス](admin/ADMIN_6_3.md) / [フィードバックメール](admin/ADMIN_6_2.md) / [ログ解析](admin/ADMIN_14_10.md) / [運用レポート](admin/ADMIN_6_1.md)
    - その他/データ構造: [利用統計ログ](other/USAGE_LOG.md)
    - ユーザ機能: [ワークスペース：アイテム一覧情報取得](user/USER_10_1.md) / [ランキング](user/USER_6_1.md) / [統計情報表示](user/USER_3_5.md)
- 本文中で言及する機能仕様: 5件

---

## モジュール以外のディレクトリ

`modules/` 直下だが Python モジュールではないもの。

- `resources/`: Python モジュールではない。CNRI Handle サーバ用の証明書・鍵・認証情報を格納。
- `cookiecutter-weko-module/`: 新規 weko モジュールを生成するためのテンプレート（スキャフォールド）。

---

## 更新履歴

| 日付 | 更新内容 |
| --- | --- |
| 2026/07/15 | 新規作成。49 ディレクトリ（実モジュール47＋非モジュール2）について、説明と機能仕様の逆引きを整備（tag v2.0.2 で突き合わせ） |
