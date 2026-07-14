# 管理者機能

管理者機能は Flask-Admin ベースの管理画面（`/admin`）から提供される。各画面のロール別アクセス可否は `weko_admin.ext.WekoAdmin.role_has_access` と `WEKO_ADMIN_ACCESS_TABLE`（System Administrator は全許可、Repository/Community Administrator は `WEKO_ADMIN_REPOSITORY_ACCESS_LIST` / `WEKO_ADMIN_COMMUNITY_ACCESS_LIST` に endpoint 名が含まれるか）で判定される（詳細は [アクセスコントロール](../access_control/README.md) 参照）。

## メニューカテゴリ構成

管理画面は以下のカテゴリで構成される（実装の `category` 登録に基づく）。

| カテゴリ | 主な画面（本カテゴリ内ドキュメント） |
| --- | --- |
| Item Types（アイテムタイプ） | メタデータ / マッピング / OAIスキーマ / プロパティ / RO-Crateマッピング / JSON-LDマッピング（ADMIN_1_x） |
| Items（アイテム管理） | 一括更新 / 一括削除 / 一括エクスポート / インポート / RO-Crateインポート（ADMIN_2_x） |
| Index Tree（インデックスツリー） | ツリー編集 / 雑誌情報 / カスタムソート（ADMIN_3_x） |
| Web Design（ウェブデザイン） | ウィジェット / ページレイアウト（ADMIN_4_x） |
| Author Management（著者管理） | 編集 / Affiliation ID / 一括出力 / 一括登録 / 外部著者IDPrefix（ADMIN_5_x） |
| Statistics（統計） | 運用レポート / フィードバックメール / サイトライセンス（ADMIN_6_x） |
| WorkFlow（ワークフロー） | フロー / ワークフロー / ワークスペース設定（ADMIN_7_x） |
| Communities（コミュニティ） | コミュニティ / 注目のコミュニティ / 参加リクエスト（ADMIN_8_x） |
| OAI-PMH | ハーベスト / Identify設定 / Sets（ADMIN_9_x） |
| Resource Sync | Resource List / Change List / Resync（ADMIN_10_x） |
| Records（レコード管理） | 永続識別子 / レコードメタデータ（ADMIN_11_x） |
| Files（ファイル管理） | バケット / ファイルインスタンス / ロケーション / マルチパートオブジェクト / オブジェクトバージョン（ADMIN_12_x） |
| User Management（ユーザー管理） | アクセス（ロール／システムロール／ユーザー）/ 連結アカウント各種 / OAuthアプリ・トークン / ロール / セッションアクティビティ / ユーザー / ユーザープロファイル（ADMIN_13_x） |
| Setting（設定） | アイテム表示・言語・PDFカバーページ・ランキング・検索・ファセット・サイト情報・メール送信・Shibboleth・制限公開・CRIS連携 ほか（ADMIN_14_x） |
| Maintenance（メンテナンス） | Elasticsearchインデックス（ADMIN_15_1） |
| SWORD API | TSV/XML / JSON-LD（ADMIN_16_x） |
| Logs（ログ管理） | エクスポート（ADMIN_17_1） |
| Advanced（アドバンスド） | プロフィール設定編集（ADMIN_18_1） |
