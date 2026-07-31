# その他

特定の画面・APIに紐づかない横断的な仕様（基盤・連携・ログ・スキーマ等）をまとめる。

| ドキュメント | 内容 |
| --- | --- |
| [CELERY](./CELERY_01.md) | Celery タスク / ビートスケジュール |
| [CONFIG](./CONFIG_01.md) | コンフィグ（`instance.cfg` と上書き） |
| [ID体系](./ID_01.md) | ID の体系・採番 |
| [モジュール](./MODULE_01.md) | モジュール／ライブラリ構成 |
| [DB](./DB_01.md) | DB（テーブル定義書へのポインタ、invenio-db + Alembic） |
| [ログ](./LOG.md) | ログ方針 |
| [セッション管理](./SESSION_01.md) | セッション（Redis） |
| [登録完了・承認通知（INBOX/LDN）](./INBOX_01.md) | COAR Notify / weko-notifications |
| [ワークフロー連携](./WORKFLOW_01.md) | GakuNinRDM 連携（depositactivity API） |
| [OAアシスト ステータス連携](./OA-ASSIST_STATUS_LINKING.md) | 外部システムへの公開ステータス連携 |
| [解析基盤連携](./KAISEKI_01.md) | オンライン分析（Binder 誘導） |
| [Shibboleth対応](./SHIBBOLETH_01.md) | 学認／Shibboleth ログイン・ロール付与 |
| [elasticsearch](./OTHER_elasticsearch.md) | 検索基盤（ES 6.8）・インデックス |
| [利用統計ログ](./USAGE_LOG.md) | invenio-stats のイベント／集計 |
| [基本監査ログ](./USER_ACTIVITY_LOG.md) | weko-logging の操作ログ |
| [Render](./SCHEMA_1_1.md) / [Schema](./SCHEMA_1_2.md) / [Form](./SCHEMA_1_3.md) | アイテムタイプの render / schema / form 定義のサンプルダンプ |
