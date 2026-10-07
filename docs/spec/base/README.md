# WEKO3機能仕様書

v2.1.0

| バージョン  | 更新内容                                                                     |
|------------|-----------------------------------------------------------------------------|
| v2.1.0     | - 全カテゴリの機能仕様を release_v2.1.0 の実装と突き合わせて修正し、v2.1.0 で変わった箇所に【v2.1.0】を付けた |
|            | - 主な修正：認可の強化（コミュニティ管理者の管轄限定、グループ権限、ゲストトークンのバケット限定など）、ログイン API の失敗応答の統一とレート制限、エンバーゴを考慮したアクセス権（検索・OAI-PMH・ResourceSync）、プレビュー・IIIF・統計・signposting の権限、ワークスペース（arXiv からの自動入力、出力の No. 列、DOI リンク）、サイトライセンスでのダウンロード、No Group・ロールの判定、アイテムタイプのマッピングの制約、SWORD API・OAI-PMH、Shibboleth の属性の受け付け元の限定 |
|            | - 追加：[API-20: 一括インポートAPI](./api/API_20_bulk_import.md) / [Signposting（FAIR Signposting）](./other/SIGNPOSTING_01.md) / [JSONLDインポート文字列置換](./other/JSONLD_IMPORT_REPLACE.md) / [API連携によるレコード追加機能（researchmap）](./other/RESEARCHMAP_LINKAGE.md) / [未病データベース 拡張メタデータ対応](./ams/AMS_EXTENDED_METADATA.md)、API 共通の認証認可と個別の仕様が無い API の認可一覧 |
|            | - 大容量ファイルのアップロードなど、リリースに含まれない機能を「未リリース」と明記 |
|            | - 見出しのパス引数をコード表記にし、リンク切れ・画像の欠落を修正（HTML 版で切れるアンカーを含む） |
|            |                                                                             |
| v2.0.2 索引 | - 開発者・AI 向けのナビ層を新設：[アーキテクチャ全体像](./ARCHITECTURE.md) / [モジュール索引（逆引き）](./MODULE_INDEX.md) / [開発者ガイド（道しるべ）](./DEV_GUIDE.md) / [横断索引](./CROSS_REFERENCE.md)。既存の機能仕様を束ね、機能↔モジュール↔実装ファイルを辿れるようにした |
| v2.0.2 整備 | - 全カテゴリ（restricted_access / ams / api / access_control / admin / user / other / tool(s)）の機能仕様を実装（tag v2.0.2）と突き合わせ、関連モジュール・エンドポイント・処理概要・設定値・モデル/テーブルを追記し、実装との相違を修正 |
|            |                                                                             |
| v1.0.8     | - [API-2: OAI-PMH ](./api/API_02_OAIPMH.md) のListRecordsの処理内容を追記   |
|            | - [ADMIN-2-4: インポート](./admin/ADMIN_2_4.md) のメッセージ表示仕様を修正  |

