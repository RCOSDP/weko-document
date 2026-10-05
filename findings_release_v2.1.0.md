# findings release_v2.1.0（ドキュメント × 実装突合 2026-10-05）

実装 RCOSDP/weko `origin/release_v2.1.0`（508030789, 2026-09-30）と、weko-document develop_v2.1.0 のマニュアル・機能仕様書・ガイドを突き合わせた結果。
前回（2026-07-17）突合地点 b19e39d8a から 317 コミット（主に認可・権限強化 issue62569 / PR #1918〜#1932、グループ・ウィジェット権限、mAP map conditions #1891、v2.0.3/v2.0.4 取り込み、nginx）。

## 対象と反映範囲
| 対象 | 反映 |
|---|---|
| docs/manuals/ADMIN/base/README.md | 全章突合・修正。新設：RO-Crateのマッピングを設定する／WEKO独自のプロパティ（wk:）について／インポート時のメタデータ文字列置換について／RO-Crateインポートする／一括インポートAPIを利用する／File Instanceを削除する／アクティビティ一覧の表示を設定する。目次・版数(v2.1.0)・改定履歴更新 |
| docs/manuals/USER/base/README.md | 全章突合・修正。「大容量のファイルをアップロードする」を未リリース機能である旨に修正、ワークスペース見出し階層修正。版数・改定履歴更新 |
| docs/manuals/GUIDE/base/manual/*.md | 4ファイル突合・修正（GakuNin RDM連携、OAアシスト、論文・研究データ登録） |
| docs/manuals_en/USER, ADMIN | 日本語版の修正内容を英語版へ反映（USER は Workspace 章を新設） |
| docs/spec/base/** | api / access_control / restricted_access / admin / ams / user / other / tools / base直下を b19e39d8a 以後の差分＋7/31他者追記分で突合。API_20 重複を `API_20_bulk_import.md` に統合 |
| docs/operation/v2.0.4_v2.1.0.md | 新規（v2.0.4→v2.1.0 アップデート手順。実装差分から作成・実機未検証、【要確認】付き） |
| 対象外 | docs/manuals/未病USER（派生版）、docs/build（ビルド成果物） |

## 実装側の要確認事項（ドキュメントでは解決できないもの）

### 重大（取りまとめ役がソースで確認済み）
1. **nginx イメージから login.py が消えている（Shibboleth ログイン不可）**：標準は `login.py`（v2.0.0 以降、`7e536799c` で login.php から変換。login.php 運用は終了）。ところが release の `nginx/Dockerfile` は fcgiwrap・python3-pip・`pip3 install requests`・login.py の配置が無く、login.php を配置している。`weko.conf` の `/secure/`・`supervisord.conf`・`WEKO_ACCOUNTS_SHIB_IDP_LOGIN_URL`（`secure/login.py`）は login.py 前提のままなので、既定構成で Shibboleth ログインが動かない。
   - 原因：develop_v2.1.0 のビルドエラー対応コミット `d6d92a5bd`（2026-07-17 "fix build error"）と `3de23b2dd`（2026-07-20 "fix build error"）が、`nginx/Dockerfile` を v2.0.4 の `nginx/Dockerfile.arm64` と同一内容で上書きした。`7e536799c` の login.py 化は `nginx/Dockerfile` だけに適用され、`Dockerfile.arm64` は login.php のまま残っていたため、上書きで login.py 化が失われた。`d6d92a5bd` の変更は直後の `b19e39d8a`（"fix"）でいったん戻されたが、`3de23b2dd` で再び入り、`fc73edb50` を経て release に至る。
   - 対処：PR #1936（https://github.com/RCOSDP/weko/pull/1936、develop_v2.1.0 向け）で修正。`nginx/Dockerfile`・`Dockerfile.arm64` に fcgiwrap・python3-requests・`ADD ./login.py`＋`chmod 755` を戻し、PHP（php-fpm・php-curl・supervisord の php-fpm・`.php` 用 location・login.php／index.php／phpinfo.php）を削除。アップデート手順書 6.4 は PR #1936 取り込み後の内容で記載済み。
   - 関連（arm64）：`nginx/supervisord.conf` が shibauthorizer／shibresponder を `/usr/lib/x86_64-linux-gnu/shibboleth/` から起動するため、arm64 ではこの2つが FATAL になり Shibboleth ログイン不可（2021年からの既存不具合）。同じ PR #1936 で、ビルド時に `uname -m` でパスを書き換えるよう修正（aarch64 で RUNNING と IdP への 302 を確認）。
2. **ウィジェット埋め込み画像**：facd5abf7 で `weko_gridlayout.views.uploaded_file`（`GET /widget/uploaded/...`）に管理者ロール必須の `roles_required` が付いた。ウィジェット本文に埋め込まれる画像URLはこのルートのため、ゲスト・一般ユーザに画像が表示されない（401/403）恐れ。

### 権限強化に伴う副作用の疑い（コード上の確認のみ）
- コミュニティ管理者：サイトライセンス画面でリポジトリ切替時 403（`get_site_license_send_mail_settings` が Sys/Repo 限定）、フィードバックメール画面で 403（`feedback_mail.js` が `get_send_mail_history` を repo_id なしで呼ぶ）、Root Index のウィジェット保存不可。
- `/get_uri` が login＋編集権限必須 → ゲスト・一般閲覧者の URL 型ファイルリンクがダウンロード回数に計上されない。
- Contributor ロールを持たない代理投稿者が validate 系 API で 403 の恐れ。General ロールが `/workflow/` を直接開ける恐れ。
- 未対応で残る認可不足：`RequestMail.post_v1` に認可なし、`prepare_edit_item` で任意のコミュニティ管理者が任意アイテムを編集可。

### DB・アップデート
- 全モジュールの Alembic 履歴が新ベースラインに再編されたが、既存 DB の `alembic_version` の扱いが未定義。invenio-oaiharvester / resourcesyncclient / resourcesyncserver / weko-schema-ui は alembic ディレクトリ無しで entry point が残存。
- `W2025-61a.sql`（全インデックスに No Group(-89) 付与）は必須。未適用だとグループ未設定インデックスが管理者以外から見えない。
- 存在しないアイテムタイプを指す item_type_mapping 行があると FK 追加（W2025-16.sql）が失敗するが解消ツールなし。モデル定義の GIN インデックスは SQL/Alembic とも作成処理なし。`postgresql/ddl/sp72-createindex.sql` は旧 btree のまま（7/17 から継続）。
- CHANGELOG / CHANGELOG_ja に v2.1.0 エントリなし、v2.1.0 タグ未作成。

### 機能の不具合疑い
- SWORD：ワークフロー登録で承認アクション無し即完了(201)でも state=inWorkflow／`GET /sword/deposit/<recid>` は承認待ちでも常に ingested／ワークフロー登録応答のファイルURLホストのみ `INVENIO_WEB_HOST_NAME` から組立／POST が Location ヘッダ未返却。
- 一括インポートAPI POST：`list_record` 空かつ error 無しで `summary_result={}` の KeyError → 500。許可ロールはモジュール読込時固定で instance.cfg 上書き不可。
- インポート置換ルール：置換結果をインデックス除去後のキー（`metadata[path_key]`）へ書込み、繰り返し項目で反映されない恐れ。非文字列値で例外。
- TSV `.RESEAECHMAP_LINKAGE`：空欄以外なら "false" でも連携（列名綴りも誤り）。
- File Instance 削除：実体 `os.remove` 後に DB 削除 → RESTRICT で失敗すると実体のみ消失。S3 はレコードのみ削除。
- Location：`get_count_query` と `get_query` の不整合（リポジトリ管理者の件数表示）。S3 Path で endpoint_url 空だと `on_model_change` 例外。Type ラベル「S3 Virtural Host」綴り誤り（JS も同綴りで判定）。
- `ItemTypes.create` が harvesting_type を引き継がず、ハーベスト用アイテムタイプのバージョンアップで標準化する恐れ。
- コミュニティ編集の Group 欄が `allow_blank=False` かつ選択肢が mAP グループのみ → mAP 未設定環境で保存不能の恐れ。
- `create_facet_search_query` の当日日付が Redis 保存時点で固定（FIX_ACCESSRIGHTS 用集計）。
- AMS `login.vue` がエラー文言を英語文字列で照合（日本語ロケールで不一致の恐れ）。
- mAP：既定設定で `jc_<fqdn>_groups_*` が画面ではグループ欄に出る一方、判定ではロール扱い。
- `_adjust_shib_admin_DB` の呼出し元なし。`weko_admin/admin.py` の `__all__` カンマ抜け。

### 文言・翻訳
- ja：「フィードバックメースステータス」（誤記）、「Item type cannot be updated becase import is in progress.」（綴り・ja 訳なし）、一括出力画面の多数ラベル未翻訳、weko-admin「The following items is required…」ja 訳なし。msgid「Relation Titie」。en：workspace `oa_policy_label` / `oa_policy_export` 訳空。WorkspaceExport.js の 0 件時文言「(出力に失敗しました」括弧未閉。

## 画像（スクリーンショット）差し替え要
- ADMIN：image4（管理メニュー）、image88（インポート結果タブ）、image189（著者言語）、image199/200/204（Scheme選択肢）、image259、image326/327、storage000〜002（ロケーション・S3キー）、image330（Multipart）、image365/366（ユーザ Roles/Groups）、image370（著者表示）、image406（サイト情報）、image418（Shibboleth）、image457/458/460（SWORD 設定）、image480（CRIS）、image493（JSON-LD 編集不可）。新設節（RO-Crate マッピング／インポート、一括インポートAPI、File Instance 削除、アクティビティ一覧表示設定）は画像なし。
- USER：image134（自動入力 ID 選択）、image266（一括出力）、image307/309（ワークスペース出力）、image312〜314（簡易登録 arXiv）、image316（アカウントメニュー）。
- GUIDE：images/grdm/app_setting_1.png、image-65.png。
- EN USER：図 7-1（Export Format）。

## ドキュメント側の要確認
- USER「大容量のファイルをアップロードする」：旧記述の専用画面（アップロードID・［転記］・ヒストリー）は release_v2.1.0 にも git 履歴にも存在しない。リリースが見送られた機能であるため（2026-10-05 確認）、節は残して「未リリースの機能」と明記した。
- GUIDE：GakuNin RDM 直接登録の「公開状態」と OA アシストの「非公開状態」の違いは連携元の送信値（wk:publishStatus）依存。「1GB 超は送信不可」は GakuNin RDM 側の制約と思われる。
- MODULE_INDEX.md は生成スクリプトで再生成済みだが、今回の手修正を含むため再実行すると手修正が消える。
