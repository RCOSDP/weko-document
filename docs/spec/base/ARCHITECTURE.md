# アーキテクチャ全体像

WEKO3 の全体構成と、機能仕様書を読む前提となる「どこで何が動くか」を示す。
個々の機能の詳細は各機能仕様に、モジュール単位の逆引きは [モジュール索引](MODULE_INDEX.md) に、
変更作業の入口は [開発者ガイド](DEV_GUIDE.md) に譲る。

## WEKO3 とは

WEKO3 は研究成果（コンテンツファイル）と、その説明情報であるメタデータを一緒に保存し、
表示・検索・配布するためのリポジトリソフトウェアである。外部システム連携のための API を備える。
コード用リポジトリ（Git 等）とは異なり、ウェブデータベースアプリケーションに近い。

## 技術スタック

出典: リポジトリ直下 `AGENTS.md`、`docker-compose*.yml`、`Dockerfile`。

| 層 | 採用技術 |
| --- | --- |
| バックエンドフレームワーク | Invenio 3（Flask 1.0.4 ベース、Python 3.6） |
| フロントエンド | React / AngularJS / jQuery（画面ごとに混在。別リポジトリ管理のものもある） |
| データベース | PostgreSQL 12.x（クラスタ用に Pgpool-II 4.2.2） |
| 検索エンジン | Elasticsearch 6.8.23 |
| キャッシュ／セッション | Redis 7.4.1 |
| メッセージキュー | RabbitMQ 4.0.2（Celery のブローカ） |
| 非同期タスク | Celery |
| Web サーバ | nginx 1.20.1 |
| 認証（学認） | shibboleth-sp |
| 永続識別子 | CNRI Handle Server |

環境変数は `docker-compose2.yml` で管理し、サーバ固有設定は `scripts/instance.cfg` に置く（機密はコード直書きしない）。
S3 互換ストレージ利用時、v2.1.0 からクライアントへのダウンロード用に読み取り専用アクセスキー（`S3_READONLY_ACCESS_KEY_ID` / `S3_READONLY_SECRET_ACCESS_KEY`、既定 `None`）を設定できる（#61752）。

## プロセス構成（実行時）

`docker-compose*.yml` で以下のサービスが起動する。役割の分離を押さえると障害切り分けや変更範囲の見極めが早い。

- **web（UI アプリ）**: 画面表示用の Flask アプリ。`scripts/entrypoint_web.sh`。
- **api（REST API アプリ）**: WebAPI 用の Flask アプリ。UI アプリとは別インスタンス（後述の entry_points 参照）。
- **worker（Celery）**: 非同期タスク実行。`scripts/entrypoint_worker.sh`。インデックス更新・メール送信・統計集計・インポート等の重い処理を担う。
- **postgresql / pgpool**: メタデータ・各種状態の永続化。
- **elasticsearch**: 検索・ファセット・統計イベントの格納。
- **redis**: セッション・キャッシュ・一部の一時状態。
  【v2.1.0】v2.1.0 では（502 エラー対策。v2.0.3／v2.0.4 のリリースには含まれない）、高頻度に呼ばれる設定・集計の取得結果を invenio-cache（`CACHE_TYPE = 'redis'`）に短 TTL でキャッシュする（後述「キャッシュ」）。
- **rabbitmq**: Celery のメッセージブローカ。
- **nginx**: リバースプロキシ（`https://127.0.0.1/`）。設定は `nginx/weko.conf`（AMS 用は `weko-ams.conf` / `weko-ams-restricted.conf`）。
  【v2.1.0】v2.1.0 では `listen 443 ssl;`（非推奨の `ssl on` を廃止）、gzip は `gzip_http_version 1.0`（前段プロキシの HTTP/1.0 転送にも効かせる）とし、`gzip_types` から `application/octet-stream`（バイナリのダウンロード）と `text/html`（既定で圧縮対象）を外した。
  【v2.1.0】また `location = /weko/shib/login` を設け、POST は real_ip で書き換える前の接続元（`$realip_remote_addr`）がループバック（`127.0.0.1` / `::1`）の場合のみ許可し（それ以外は 403）、その接続元を `REMOTE_ADDR` として WEKO に渡す（Shibboleth SP 属性の受け付け元限定。詳細は [Shibboleth対応](other/SHIBBOLETH_01.md)）。
- **handle**（任意）: CNRI Handle サーバ連携時。

> UI アプリと API アプリが分かれている点は重要。ある機能が「画面から動くのか API から動くのか」で、
> 変更対象の Blueprint／設定が変わる。

## Invenio3 のモジュール機構（各機能がどう組み込まれるか）

WEKO3 の機能は `modules/` 配下の Python パッケージ（Invenio 拡張）として実装され、
各モジュールの `setup.py` の **`entry_points`** を通じて Flask アプリへ登録される。
新機能の追加・既存機能の変更は、まず該当モジュールの entry_points から入口をたどるのが定石。

主な entry_points グループ（例は `modules/weko-workflow/setup.py`）:

| entry_points グループ | 役割 | 典型的な実装ファイル |
| --- | --- | --- |
| `invenio_base.apps` | UI アプリへ拡張（Blueprint 等）を登録 | `<pkg>/__init__.py`（拡張クラス）、`views.py` |
| `invenio_base.api_apps` | REST API アプリへ拡張を登録 | `ext.py`、`rest.py` |
| `invenio_admin.views` | Flask-Admin の管理ビューを登録 | `admin.py` |
| `invenio_celery.tasks` | Celery タスクを登録 | `tasks.py` |
| `invenio_db.models` | SQLAlchemy モデルを登録 | `models.py` |
| `invenio_db.alembic` | DB マイグレーション（Alembic）を登録 | `alembic/` |
| `invenio_assets.bundles` | フロントエンドの JS/CSS バンドル（Webpack） | `bundles.py`、`static/`、`templates/` |
| `invenio_i18n.translations` | 翻訳メッセージ | `translations/` |
| `invenio_oauth2server.scopes` | WebAPI の OAuth2 スコープ | `scopes.py` |
| `flask.commands` | CLI コマンド | `cli.py` |

設定値（config）は各モジュールの `config.py` に定義され、アプリ起動時に集約される。
サーバ個別の上書きは `scripts/instance.cfg`。config キーの横断索引は [横断索引](CROSS_REFERENCE.md) 参照。

## モジュールのレイヤ構造

- **Invenio 基盤（`invenio-*`）**: レコード格納・ファイル・検索・OAI・OAuth・統計などの土台。上流 inveniosoftware 由来（WEKO3 内で改変あり）。
- **WEKO 独自（`weko-*`）**: WEKO3 固有の機能（アイテムタイプ、ワークフロー、制限公開、著者DB、ウェブデザイン等）。開発の主対象。

代表的な中核モジュール（詳細は [モジュール索引](MODULE_INDEX.md)）:

- `weko-records` / `invenio-records`: メタデータ（レコード）モデルと API。
- `weko-deposit`: アイテム登録の中核。メタデータ整形と Elasticsearch 投入、ファイル情報の DB 格納。
- `weko-search-ui`: 検索結果表示・ファセット・インポート／一括処理。
- `weko-records-ui`: アイテム詳細表示・ファイル配信・アクセス制御。
- `weko-workflow`: 登録・利用申請等のワークフロー。
- `weko-admin`: 管理画面全般。
- `weko-index-tree`: インデックスツリー（分類階層）。
- `invenio-files-rest` / `invenio-s3`: ファイル実体の格納と配信。
- `invenio-indexer` / `invenio-stats`: ES インデクシングと利用統計。

## データの流れ

### アイテム登録 → 公開までの流れ

1. **登録 UI**（`weko-items-ui`）でメタデータ入力・ファイルアップロード。フロントは React/AngularJS。
2. **ワークフロー**（`weko-workflow`）でアクティビティとして進行（メタデータ入力→ファイル→インデックス指定→Identifier付与→承認→完了）。制限公開・利用申請もここが起点。
3. **deposit**（`weko-deposit` / `invenio-deposit`）がレコードを保存し、ファイルは `invenio-files-rest`（必要に応じ `invenio-s3`）へ格納。
4. **インデクシング**（`invenio-indexer`）でレコードを Elasticsearch に投入（多くは Celery 経由の非同期）。
5. **公開・表示**（`weko-records-ui` / `weko-theme`）でアイテム詳細を表示。ファイル配信時に **アクセス制御**（公開範囲・ログイン要否・制限公開・利用申請）を判定。

### 検索・配布

- **検索**（`weko-search-ui` / `invenio-records-rest`）は Elasticsearch に対して実行。ファセット・インデックス検索・全文検索。
- **メタデータ出力**（`weko-schema-ui`）が OAI/JPCOAR 等のスキーマへマッピングして出力。
- **外部提供**: OAI-PMH（`invenio-oaiserver`）、ResourceSync（`invenio-resourcesyncserver`）、SWORD 受入（`weko-swordserver`）、Signposting（`weko-signposting`）、OpenSearch など。WebAPI の一覧は [WebAPI](api/README.md)。

### 認証・権限

- 認証は `invenio-accounts` ＋ `weko-accounts`（Shibboleth 連携）。WebAPI は `invenio-oauth2server`（OAuth2 トークン／スコープ）。
- 権限判定はロール（システム管理者／リポジトリ管理者／コミュニティ管理者／登録ユーザー／一般ユーザー／ゲスト）ベース。
  画面・API ごとの可否は [アクセスコントロール](access_control/README.md) にまとまっている。

> 実装補足（v2.1.0）：
> - 未認証時の応答は `weko_accounts.unauthorized` が制御する（`WEKO_ACCOUNTS_UNAUTHORIZED_JSON`、既定 `True`）。API アプリ（`/api`）は常に 401 JSON を返し（従来は `security.login` を解決できず 500）、UI アプリは API/AJAX 呼び出しとみなすリクエストにのみ 401 JSON を返す。通常の画面遷移と iframe 等の埋め込み内の遷移（`Sec-Fetch-Dest` が document / iframe / frame / embed / object）はログイン画面へ遷移する。
> - 【v2.1.0】認可が未設定だった API への `login_required`／権限チェックの追加（issue62569 ほか）、IIIF・signposting・統計・プレビュー・サイトマップ・ResourceSync 等の閲覧権限判定の統一が行われた。個別の可否は各機能仕様・[アクセスコントロール](access_control/README.md) を参照。
> - 【v2.1.0】ログイン API（`/api/<version>/login`）は失敗応答を1種類に揃え、ログイン API にだけレート制限（`WEKO_API_LIMIT_RATE_DEFAULT`）をかける（/api 配下の他経路には制限をかけない）。
> - 【v2.1.0】Shibboleth SP の属性は SP のログインスクリプト（`nginx/login.py`）がループバック宛てに POST したものだけを受け付ける（`WEKO_ACCOUNTS_SHIB_SP_ALLOWED_ADDRS`、既定 `['127.0.0.1', '::1']`。nginx 側の制限と二重）。

### キャッシュ（v2.1.0）

【v2.1.0】502 エラー対策（v2.1.0 で導入。v2.0.3／v2.0.4 のリリースには含まれない）として、ページ描画ごとに繰り返されていた DB／ES 参照を invenio-cache（Redis）で短 TTL キャッシュする。cache 拡張が未設定の環境ではキャッシュせず従来どおり都度取得する。

| 対象 | キャッシュ単位・無効化 | TTL 設定（既定） |
| --- | --- | --- |
| `weko_admin.utils.get_search_setting()` | 1キー。検索設定の更新・作成時に `delete_search_setting_cache()` で削除 | `WEKO_ADMIN_SETTINGS_CACHE_TTL`（300 秒） |
| `AdminSettings.get()`（weko-admin） | 設定名ごと。update/delete 時に削除 | `WEKO_ADMIN_SETTINGS_CACHE_TTL`（300 秒） |
| `get_ranking()`（weko-items-ui、トップページのランキング） | 設定・日付・利用者（ゲストは共通、ログインユーザーは個別）ごと | `WEKO_ITEMS_UI_RANKING_CACHE_TTL`（300 秒） |
| `get_search_detail_keyword()`（weko-search-ui、詳細検索条件） | 言語・利用者の閲覧可能インデックス等ごと | `WEKO_SEARCH_DETAIL_KEYWORD_CACHE_TTL`（300 秒） |
| アイテム詳細の Google Scholar／Dataset 用 JPCOAR XML（weko-records-ui） | OAI ID＋レコードのリビジョンごと（編集で即無効） | `WEKO_RECORDS_UI_GOOGLE_XML_CACHE_TTL`（300 秒） |

このほか、ウィジェットデザイン（weko-gridlayout）、アイテム詳細のインデックス参照、`sort_meta_data_by_options` のアイテムタイプ取得はリクエスト内でのメモ化のみ（Redis は使わない）。いずれの TTL も 0 で有効期限なし。

## 開発環境

- Docker を利用。クローン後 `install.sh` で環境構築。構築後 `https://127.0.0.1/` にアクセス。
- テストは `python manage.py test` または `pytest`。詳細と落とし穴は [開発者ガイド](DEV_GUIDE.md)。

## 更新履歴

| 日付 | 更新内容 |
| --- | --- |
| 2026/07/15 | 新規作成。技術スタック・プロセス構成・Invenio entry_points 機構・データフローを実装（tag v2.0.2）と `AGENTS.md`／`docker-compose` を基に整理 |
| 2026/10/05 | release_v2.1.0突合（508030789）：nginx 設定（listen ssl、gzip、/weko/shib/login の接続元制限）、未認証応答 401 統一・ログイン API レート制限・SP 属性受け付け元限定、502 対策キャッシュ（Redis 短 TTL）、S3 読み取り専用アクセスキーを追記。モジュール構成（49 ディレクトリ）に変化なしを確認 |
| 2026/10/05 | v2.1.0タグ付けに伴う記述訂正：502 エラー対策のキャッシュは v2.1.0 で導入（v2.0.3／v2.0.4 には含まれない）と訂正 |
