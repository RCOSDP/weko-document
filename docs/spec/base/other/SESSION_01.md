# セッション管理

- invenioモジュールを利用しており、サーバ側のセッション管理、セッションアクティビティの追跡が可能。詳細なドキュメントは[invenio-accounts](https://github.com/inveniosoftware/invenio-accounts#invenio-accounts) で入手可能。
- 一括登録画面のセッション維持期間のみカスタマイズ可能。設定WEKO_ADMIN_IMPORT_PAGE_LIFETIMEに秒数を設定する（デフォルトは12時間）。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2023/11/11 | V0.9.27 | V0.9.27追加機能 |

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足：通常セッションの有効期限は `PERMANENT_SESSION_LIFETIME`（既定 1日）、インポート画面は `WEKO_ADMIN_IMPORT_PAGE_LIFETIME`（既定 43200秒＝12時間）。サーバ側セッションは Redis（`ACCOUNTS_SESSION_REDIS_URL`、DB=1）に保存される。
