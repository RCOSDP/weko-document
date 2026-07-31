# AMS

未病データベース（AMS）は、未病データベース専用の WEKO3 リポジトリ（バックエンド）と、その上で動作する Nuxt 製フロントエンド（`weko-frontend`）から構成されるシステムである。

> 注：フロントエンド（`weko-frontend` / `nginx/ams/weko-frontend/`）は WEKO バックエンド（`/home/mhaya/weko`）とは**別リポジトリ**で管理される。本カテゴリの各仕様書のうち、フロントのページ（`*.vue`）・設定（`app.config.ts`）・サーバーサイドAPI（`weko-frontend/server`）はそのフロントリポジトリ側の定義であり、本書ではフロントが利用する WEKO バックエンド側の接点を中心に実装（v2.0.2）と突き合わせている。

## 本カテゴリの構成

| ドキュメント | 内容 |
| --- | --- |
| [未病データベースとWEKOの構成](./AMS_ARCHITECTURE_01.md) | フロントのパス／API、フロントとWEKOの共存（nginx振り分け）、バックエンド実API |
| [未病フロント アクセスコントロール](./AMS_ACCESS_CONTROLL.md) | 画面・操作ごとのロール別アクセス可否 |
| [GakuNin RDMボタン表示](./AMS_GRDM_BUTTON_01.md) | RO-Crate ↔ WEKOアイテム変換、JSON-LDマッピング、GRDMボタン表示条件 |
| [Shibboleth対応](./AMS_SHIBBOLETH_01.md) | Shibbolethログイン・ロール付与・OAuth認証・エラー |

## 関連モジュール（WEKOバックエンド）

- weko-accounts（Shibbolethログイン・mAPグループによるロール付与）
- weko-records-ui（アイテム取得API `/api/v1/records/<id>`、RO-Crate変換、リクエストメール・CAPTCHA API）
- weko-records / weko-search-ui（JSON-LDマッピング定義・変換）
- weko-admin（SWORD API JSON-LDマッピング設定）
- invenio-oauth2server（OAuth2 トークン発行 `/oauth/token`）
- invenio-oaiserver（OAI-PMH `/oai`）
