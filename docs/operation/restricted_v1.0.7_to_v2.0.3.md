# feature/restricted_v1.0.7 から v2.0.3 へのアップデート方法（docker-compose 版）

制限公開（利用申請）機能を有効にしたまま、`feature/restricted_v1.0.7` で稼働している環境を `v2.0.3` へ
アップデートし、データをマイグレーションする手順である。

> **本手順書の位置づけ**
> 既存手順書 [`v1.0.8b_v2.0.0.md`](./v1.0.8b_v2.0.0.md) が
> **v1.0.8b → v2.0.0（docker-compose 単一環境）** の正規手順である。
> 本書はそれをベースに、以下の 3 つの差分を補ったものである。
>
> 1. **起点が `feature/restricted_v1.0.7`** であること
>    （v1.0.8 / v1.0.8b を経ていないため、v1.0.7a2 / v1.0.7b のパッチが未適用。3-3 参照）
> 2. **終点が v2.0.3** であること
>    （v2.0.0 → v2.0.3 で `postgresql/ddl/61660.sql` と `S3_READONLY_*` が追加。2 章末尾参照）
> 3. **制限公開（利用申請）機能を有効のまま継続**すること
>
> DB / Python / Elasticsearch のマイグレーション本体
> （`W2025-29.sql`、`update_W2025-29.py 30015 500`、`communityIds` マッピング追加、reindex）は
> `v1.0.8b_v2.0.0.md` と同一である。相違点は本書で明示する。
> 本番適用前に必ず「11. NII に確認すべき事項」を確認し、クローン環境でリハーサルを行うこと。

---

## 1. 前提とバージョンパス

| 項目 | 内容 |
| --- | --- |
| 移行元 | `origin/feature/restricted_v1.0.7`（HEAD: `c25353f` 2024-11-15） |
| 移行先 | `v2.0.3`（`d2fdc0e` 2026-07-28） |
| 経由バージョン | v1.0.8 → v1.0.8b → v2.0.0 → v2.0.2 → v2.0.3 |
| 分岐元 | `adddcaf`（`#v1.0.7 merged` 2024-07-22） |
| 変更ファイル数 | 約 2,016 ファイル |

### 据え置きのもの（基盤入れ替えは不要）

- Python 3.6（`python:3.6-slim-buster`）
- Elasticsearch 6.8.23（`elasticsearch/Dockerfile` に変更なし）
- PostgreSQL

### 新規に必要になるもの

| 項目 | 内容 |
| --- | --- |
| `inbox` サービス | COAR Notify LDN Inbox（`inbox/Dockerfile`、`RCOSDP/coar-notify-inbox` の `nii_main` を clone、Python 3.12 / uvicorn 8080） |
| `mongo` サービス | `mongo:7.0.14`（inbox のバックエンド） |
| Tika | `tika/tika-app-2.6.0.jar`（リポジトリに同梱）。`TIKA_JAR_FILE_PATH` を web / worker に設定 |
| イメージ更新 | `pgpool/pgpool:4.2.2`（旧 `bitnami/pgpool`）、`redis:7.4.1`、`rabbitmq:4.0.2` |
| 新規モジュール | `weko-workspace` / `weko-signposting` / `weko-notifications`（egg-info の volume 定義追加） |

### 主要な機能追加（CHANGELOG v2.0.0 より）

学認対応、シークレットURL、OA Assist 連携、研究者用ワークスペース、SWORDv3 でのワークフロー利用、
GakuNin mAP 連携、researchmap 連携、監査ログ（`user_activity_logs`）、JSON-LD マッピング 等。

---

## 2. データマイグレーションの構成

v2.0 系へのマイグレーションは、以下の 2 本に集約されている。

| ファイル | 役割 |
| --- | --- |
| `postgresql/ddl/W2025-29.sql` | DDL + 初期データ。alembic リビジョン 36 本を SQL に変換したもの＋制限公開関連 SQL＋v1.0.8 分。全体が `BEGIN 〜 COMMIT` の単一トランザクションで、`IF NOT EXISTS` / `ON CONFLICT DO NOTHING` により冪等 |
| `scripts/demo/update_W2025-29.py` | データ移行。制限公開アイテムタイプの schema 変換、プロパティ／アイテムタイプ最新化、著者DB（weko id）更新、メタデータ修正、詳細検索条件更新 |

`W2025-29.sql` が内包している既存 SQL:

```
alembic 36 リビジョン（invenio-accounts / communities / files-rest / mail /
                       weko-admin / authors / index-tree / indextree-journal /
                       logging / notifications / records / records-ui /
                       swordserver / user-profiles / workflow / workspace）
W2023-23-item-application.sql   （利用申請）
mail_template.sql               （メールテンプレート）
W2023-23-request_mail.sql
W2023-21 workflow_flow_action_role.sql
W2023-21 update_resticted_items.sql
WOA-06-jsonld_mapping.sql
fix_issue_37736.sql / fix_issue_39700.sql
202409_BioResource_ddl.sql
v1.0.8.sql
authors_prefix_settings.sql（一部）
records_metadata の weko_shared_id → weko_shared_ids / owner → owners 変換
restricted_access admin_settings のシークレットURL設定追加
```

`update_W2025-29.py` の実行順（`main()`）:

```
get_update_item_info_W2025_29_sql()        # SQL で更新された ID 一覧をログ出力（再インデックス対象）
updateRestrictedRecords.main(prop_id)      # 制限公開プロパティ／アイテムタイプを v2.0 形式(roles)へ変換
register_properties_only_specified()       # scripts/demo/properties 配下に従いプロパティ更新
renew_all_item_types()                     # 更新プロパティでアイテムタイプ再生成
update_feedback_mail_list_to_db.main()     # 著者DBの weko id 変更＋メタデータ追随
update_itemtype_multiple_main()            # "Multiple" アイテムタイプの修正
fix_issue_47128_newbuild_main()            # harvesting_type=True かつ itemtype_id=12 の修正
fix_metadata_53602_main()                  # プロパティ変更を全アイテムのメタデータへ適用
add_peer_reviewed_to_version_type_property.main()
fix_issue_57372()                          # 詳細検索条件の更新
```

### W2025-29.sql が**カバーしていない**もの（本移行パスでは別途適用が必要）

`feature/restricted_v1.0.7` は 2024-11 時点の枝であり、その後の v1.0.7a2 / v1.0.7b で配られた
パッチが**当たっていない**。以下は適用要否を 3-3 で判定した上で個別に適用する。

| SQL | 内容 | 判定方法 |
| --- | --- | --- |
| `postgresql/update/v1_0_7a2.sql` | `authors_prefix_settings` に e-Rad_Researcher / ROR / ISNI / VIAF / AID / Ringgold、`authors_affiliation_settings` に ROR を追加 | 3-3 (a) |
| `postgresql/update/v1.0.7b.sql` | `authors_prefix_settings` の `e-Rad` → `e-Rad_Researcher` リネーム | 3-3 (a) |
| `postgresql/update/fix_issue45092.sql` | `subitem_record_name` → `subitem_source_title` へ一括置換（item_type / mapping / records_metadata / item_metadata） | 3-3 (b) |
| `postgresql/ddl/61660.sql` | `files_location` に `readonly_access_key` / `readonly_secret_key` を追加 | 3-3 (c)。S3 ロケーション利用時のみ。`ADD COLUMN`（`IF NOT EXISTS` なし）なので存在確認してから実行する |
| `postgresql/ddl/fix_itemtype_issue_45614.sql` | 新規構築機関向けのアイテムタイプ修正 | **移行機関は対象外**。適用しないこと |

### v2.0.0 → v2.0.3 の追加分

`v1.0.8b_v2.0.0.md` は終点が v2.0.0 のため、以下は本書で追加する。

| 対象 | 内容 | 移行での扱い |
| --- | --- | --- |
| `postgresql/ddl/61660.sql` | `files_location` に `readonly_access_key` / `readonly_secret_key` を追加（weko#61752、v2.0.3 で追加） | **S3 ロケーション利用時のみ適用**。`ADD COLUMN`（`IF NOT EXISTS` なし）のため列の存在確認が必須 |
| `S3_READONLY_ACCESS_KEY_ID` / `S3_READONLY_SECRET_ACCESS_KEY` | instance.cfg に追加（既定 `None`） | S3 利用時は値を設定 |
| `scripts/demo/fix_lang_code_column.sql` | `admin_lang_settings.lang_code` の桁拡張と zh → zh_Hans / zh_Hant 変換 | **適用不要**。`W2025-29.sql` の 1520〜1535 行に同内容が内包済み |
| `scripts/demo/restricted_mail_template.sql` | 制限公開のメールテンプレート初期データ（737行） | **適用不要**。`install.sh` / `install3.sh` からのみ参照される新規構築用。移行環境には `W2025-29.sql` の 719〜1456 行が同内容を投入する |

---

## 3. 事前調査（サービス稼働中に実施可）

### 3-1. 変数の定義

```sh
WEKO_DIR=/path/to/weko                 # 稼働中のリポジトリ
COMPOSE="docker compose -f docker-compose2.yml"
WORK_DIR=/path/to/work                 # 作業ログ・バックアップ置き場
mkdir -p ${WORK_DIR}
cd ${WEKO_DIR}
git rev-parse --abbrev-ref HEAD ; git rev-parse HEAD | tee ${WORK_DIR}/current_revision.txt
```

### 3-2. 制限公開プロパティ ID の特定

`update_W2025-29.py` の引数は**アイテムタイプ ID ではなく `item_type_property.id`**である
（`tools/updateRestrictedRecords.py` の `update_item_type_property()` が `ItemTypeProperty.id` で検索する）。
既定値は 30015（`tools/restricted_upadate.sh` の `RESTRICTED_ACCESS_PROPERTY`）。

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT id, name FROM item_type_property WHERE schema::text LIKE '%termsDescription%' ORDER BY id;"
```

得られた ID を `RESTRICTED_ACCESS_PROPERTY` として控える。複数出た場合は NII に確認すること。

### 3-3. 未適用パッチの判定

```sh
# (a) authors_prefix_settings / authors_affiliation_settings
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT scheme FROM authors_prefix_settings ORDER BY id;"
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT scheme FROM authors_affiliation_settings ORDER BY id;"
#   → 'e-Rad' が残っている        : v1.0.7b.sql を適用
#   → 'ROR' / 'AID' が存在しない  : v1_0_7a2.sql を適用
#     （v1.0.7 の初期データは 5 件、v2.0.3 は 14 件）

# (b) subitem_record_name の残存
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT count(*) FROM item_type WHERE schema::text LIKE '%subitem_record_name%';"
#   → 0 以外なら fix_issue45092.sql を適用

# (c) files_location の readonly キー列
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT column_name FROM information_schema.columns
 WHERE table_name='files_location' AND column_name LIKE 'readonly%';"
#   → 0 行かつ S3 ロケーション利用中なら 61660.sql を適用
```

### 3-4. instance.cfg のカスタマイズ差分抽出

稼働中の設定は `scripts/instance.cfg` を jinja2 で展開した
`/home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg` である。
機関固有のカスタマイズを v2.0.3 の `scripts/instance.cfg` へ手でマージする必要がある。

```sh
cp scripts/instance.cfg ${WORK_DIR}/instance.cfg.restricted_v1.0.7
${COMPOSE} exec web cat /home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg \
  > ${WORK_DIR}/invenio.cfg.current
git show v2.0.3:scripts/instance.cfg > ${WORK_DIR}/instance.cfg.v2.0.3
diff -u ${WORK_DIR}/instance.cfg.restricted_v1.0.7 ${WORK_DIR}/instance.cfg.v2.0.3 \
  > ${WORK_DIR}/instance.cfg.diff ; :
```

#### 特に注意する設定キー

| 変更 | 内容 |
| --- | --- |
| **リネーム** | 設定キー `S3_SECRECT_ACCESS_KEY`（v1.0.7 のタイプミス）→ `S3_SECRET_ACCESS_KEY`。環境変数名は据え置きでよい。詳細は 6-3 参照 |
| 削除 | `WEKO_SITEMAP__ROBOT_TXT` |
| 追加（制限公開） | `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` / `WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS` / `WEKO_RECORDS_UI_RESTRICTED_API` / `WEKO_ITEMS_UI_PROXY_POSTING` / `WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED` / `WEKO_INDEX_TREE_SHOW_MODAL` / `WEKO_USERPROFILES_CUSTOMIZE_ENABLED` / `INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED`（v2.0.3 の既定はいずれも False。**継続利用するので True にする**） |
| 追加（新機能） | `WEKO_NOTIFICATIONS*`（inbox 連携）、`WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_*`、`WEKO_RECORDS_UI_OA_*`、`WEKO_ACCOUNTS_IDP_ENTITY_ID`、`GROUP_INFO_REDIS_DB`、`LINKAGE_MQ_EXCHANGE` / `LINKAGE_MQ_QUEUE`、`SQLALCHEMY_ENGINE_OPTIONS`、`S3_READONLY_ACCESS_KEY_ID` / `S3_READONLY_SECRET_ACCESS_KEY` ほか |

### 3-5. 所要時間の見積り

`update_W2025-29.py` は全アイテムのメタデータを走査するため、件数に比例して時間がかかる。

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c \
"SELECT (SELECT count(*) FROM records_metadata) AS records,
        (SELECT count(*) FROM item_metadata)   AS items,
        (SELECT count(*) FROM item_type)       AS item_types,
        (SELECT count(*) FROM authors)         AS authors;"
```

---

## 4. リハーサル（必須）

本番と同じデータを持つクローン環境で 5〜8 章を通しで実施し、以下を記録する。

- `W2025-29.sql` の実行時間とエラー有無
- `update_W2025-29.py` の実行時間（`batch_size` の調整要否）
- 再インデックスの所要時間
- 動作確認チェックリスト（9 章）の結果

本番のメンテナンス時間はここで得た実測値をもとに決めること。

---

## 5. バックアップ

```sh
cd ${WEKO_DIR}

# DB 全体（必須）
${COMPOSE} exec -T postgresql pg_dump -U invenio -d invenio -Fc \
  > ${WORK_DIR}/invenio_$(date +%Y%m%d%H%M).dump

# 設定
cp scripts/instance.cfg ${WORK_DIR}/
${COMPOSE} exec web cat /home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg \
  > ${WORK_DIR}/invenio.cfg.bak

# コンテンツファイル（ローカル volume の場合）／S3 の場合はバケットのバージョニング状況を確認
docker volume ls
```

Elasticsearch は DB から再構築できるためバックアップ必須ではないが、
統計インデックス（`*-stats-*`, `*-events-stats-*`）は再構築できないので**削除しないこと**（8 章参照）。

---

## 6. サービス停止とコードの更新

### 6-1. サービス停止

```sh
cd ${WEKO_DIR}
${COMPOSE} down
```

（公開環境ではメンテナンス画面へ切り替えてから停止すること）

### 6-2. コード取得

```sh
git fetch origin --tags
git stash            # ローカル変更がある場合
git checkout v2.0.3 -B v2.0.3
git log -1 --format='%H %ci %s'      # d2fdc0e... 2026-07-28 を確認
```

### 6-3. instance.cfg のマージ

3-4 の差分をもとに `scripts/instance.cfg` へ機関固有設定を反映し、
制限公開関連フラグを True にする。`tools/restricted_upadate.sh` の前半がそのまま使えるが、
同スクリプトは後半で SQL 適用とコンテナ再起動まで行うため、**フラグ設定部分だけを流用**する。
（本手順書に付属の `tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh` の `step_config` が同等の処理を行う）

```
WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG = True
WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS    = True
WEKO_RECORDS_UI_RESTRICTED_API            = True
WEKO_ITEMS_UI_PROXY_POSTING               = True
WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED   = True
WEKO_INDEX_TREE_SHOW_MODAL                = True
WEKO_USERPROFILES_CUSTOMIZE_ENABLED       = True
INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED = True
```

#### S3 を利用している場合

設定**キー名**が `S3_SECRECT_ACCESS_KEY`（v1.0.7 のタイプミス）から `S3_SECRET_ACCESS_KEY` に変わった。
環境変数名は据え置きでよく、`v1.0.8b_v2.0.0.md` 5.4 のとおり次のように書ける。

```python
S3_SECRET_ACCESS_KEY = '{{ environ("S3_SECRECT_ACCESS_KEY") }}'

FILES_REST_LOCATION_TYPE_LIST = [
    ('s3', 'S3 Path'),
    ('s3_vh', 'S3 Virtural Host')
]
```

v2.0.3 では加えて readonly キーが必要（weko#61752）。

```python
S3_READONLY_ACCESS_KEY_ID = ...
S3_READONLY_SECRET_ACCESS_KEY = ...
```

#### その他 v2.0.3 の instance.cfg で追加されている項目

機関固有の instance.cfg を使っている場合、v2.0.3 の `scripts/instance.cfg` から以下を取り込む
（`v1.0.8b_v2.0.0.md` 5.1〜5.8 と同じ）。

- `CELERY_RESULT_BACKEND` を `CELERY_RESULT_BACKEND_DB_NO` から組み立てる形に変更
- Celery task `remove_author_tmp_file`（著者一時ファイルの定期削除、1時間毎）
- `WEKO_AUTHORS_EXPORT_TMP_DIR` / `WEKO_AUTHORS_IMPORT_TMP_DIR`（v2.0.3 の既定値は `'authors_export'` / `'authors_import'`）
- `WEKO_DEPOSIT_ITEM_UPDATE_TASK_TTL` / `_RETRY_COUNT` / `_RETRY_COUNTDOWN` / `_RETRY_BACKOFF_RATE`
- `WEKO_SEARCH_UI_FACET_LANG_DISP_FLG` / `DISPLAY_LOGIN` / `WEKO_RECORDS_UI_LANG_DISP_FLG` / `WEKO_THEME_FETCH_SEARCH_FLG`
- `GROUP_INFO_REDIS_DB` / `LINKAGE_MQ_EXCHANGE` / `LINKAGE_MQ_QUEUE` / `SQLALCHEMY_ENGINE_OPTIONS`
- 任意機能（researchmap 連携 / OA Assist / GakuNin RDM / Notification / SWORD / Redis Sentinel / Shibboleth）は
  利用するものだけ採用する

### 6-3b. weko.conf（Shibboleth 利用時のみ）

`v1.0.8b_v2.0.0.md` 6 章のとおり、Shibboleth の session 変数名が変わっている。
**認証環境に依存するため、一律に適用しないこと。**

```diff
-shib_request_set $shib_shib_session_id $upstream_http_variable_shib_session_id;
-fastcgi_param Shib-Session-ID $shib_shib_session_id;
+shib_request_set $shib_session_id $upstream_http_variable_shib_session_id;
+fastcgi_param Shib-Session-ID $shib_session_id;
```

JAIRO Cloud では `eppn` として渡す属性を `eppn` から `persistent-id` へ変更している。
Shibboleth を使っていない docker 環境では不要。

### 6-3c. uwsgi.ini

大容量ファイルのアップロードを行う場合、アップロード中に `harakiri` が発動しないよう無効化する
（`v1.0.8b_v2.0.0.md` 7 章）。

```ini
# harakiri = 300
```

### 6-4. イメージのビルド

```sh
DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 ${COMPOSE} build --no-cache --force-rm
```

`inbox` は GitHub から `RCOSDP/coar-notify-inbox` を clone するため、ビルドホストから
GitHub へ到達できることを事前に確認する。

### 6-5. postgresql のみ起動

```sh
${COMPOSE} up -d postgresql
${COMPOSE} exec postgresql pg_isready -U invenio
```

---

## 7. DB マイグレーション

### 7-1. 未適用パッチの適用（3-3 で「要」と判定したもののみ）

```sh
for f in postgresql/update/v1_0_7a2.sql postgresql/update/v1.0.7b.sql postgresql/update/fix_issue45092.sql ; do
  docker cp "$f" $(${COMPOSE} ps -q postgresql):/tmp/$(basename "$f")
  ${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/$(basename "$f")
done
```

S3 利用かつ `readonly_access_key` 列が無い場合のみ:

```sh
docker cp postgresql/ddl/61660.sql $(${COMPOSE} ps -q postgresql):/tmp/61660.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 -f /tmp/61660.sql
```

### 7-2. W2025-29.sql の適用

単一トランザクションのため、途中で失敗すれば全体がロールバックされる。
`RAISE NOTICE` を残すためログを必ず保存すること。

```sh
docker cp postgresql/ddl/W2025-29.sql $(${COMPOSE} ps -q postgresql):/tmp/W2025-29.sql
${COMPOSE} exec -T postgresql psql -U invenio -d invenio -v ON_ERROR_STOP=1 \
  -f /tmp/W2025-29.sql 2>&1 | tee ${WORK_DIR}/W2025-29.log

grep -iE 'error|fatal|rollback' ${WORK_DIR}/W2025-29.log
tail -3 ${WORK_DIR}/W2025-29.log   # 'End execution: Migration W2025-29.sql' と COMMIT を確認
```

### 7-3. 適用結果の確認

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -c "
SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename IN
 ('mail_templates','mail_template_genres','mail_template_users','jsonld_mappings',
  'oa_status','user_activity_logs','notifications_user_settings','sword_clients',
  'workspace_default_conditions','workspace_status_management',
  'author_community_relations','file_onetime_download','file_secret_download')
ORDER BY tablename;"

# records_metadata の変換確認（weko_shared_ids / owners になっていること）
${COMPOSE} exec postgresql psql -U invenio -d invenio -c "
SELECT count(*) FROM records_metadata WHERE json ? 'weko_shared_id';"   -- 0 件であること
${COMPOSE} exec postgresql psql -U invenio -d invenio -c "
SELECT count(*) FROM records_metadata WHERE json ? 'owners';"           -- 全件

# 監査ログのパーティション（2026-01〜2027-12 が作られる）
${COMPOSE} exec postgresql psql -U invenio -d invenio -c "
SELECT tablename FROM pg_tables WHERE tablename LIKE 'user_activity_logs_%' ORDER BY 1;"
```

> **alembic について**
> `W2025-29.sql` は alembic リビジョンを SQL 化したもので、`alembic_version` テーブルは更新されない。
> WEKO の運用手順は `invenio db create` / 生 SQL ベースであり `invenio alembic upgrade` は使わないため
> 実害はないが、次回以降 alembic を使う予定がある場合は NII に確認すること。

---

## 8. データマイグレーションと再インデックス

### 8-1. 全サービス起動

```sh
${COMPOSE} up -d
${COMPOSE} ps
${COMPOSE} logs --tail=100 web
```

新規サービス（`inbox` / `mongo`）が Up になっていることを確認する。

### 8-2. update_W2025-29.py の実行

```sh
RESTRICTED_ACCESS_PROPERTY=30015    # 3-2 で特定した値
BATCH_SIZE=500                      # 既定値。メモリ不足時は小さくする
# ※ `v1.0.8b_v2.0.0.md` 12章、および JAIRO Cloud の migration_py.sh も
#    `invenio shell scripts/demo/update_W2025-29.py 30015 500` を使用している

${COMPOSE} exec -T web invenio shell scripts/demo/update_W2025-29.py \
  ${RESTRICTED_ACCESS_PROPERTY} ${BATCH_SIZE} 2>&1 | tee ${WORK_DIR}/update_W2025-29.log

grep -iE 'error|traceback|rollback|not found' ${WORK_DIR}/update_W2025-29.log
grep 'All updates completed successfully' ${WORK_DIR}/update_W2025-29.log
```

> **注意**
> `main()` は例外を握りつぶして `db.session.rollback()` するだけで異常終了しない。
> 終了コードではなく**必ずログで判定**すること。
> `All updates completed successfully.` が出ていなければ失敗である。
> 各ステップの所要時間も `show_exec_time` によりログに出る。

### 8-3. Elasticsearch マッピングの更新

ES 6.8 では既存インデックスへの**フィールド追加のみ**可能。v2.0 での変更は次の 2 点。

| インデックス | 変更 | 対応 |
| --- | --- | --- |
| `<prefix>-weko-item-v1.0.0` | `request_mail_list` の**削除** | 既存マッピングに残っていても無害。対応不要 |
| `<prefix>-authors-author-v1.0.0` | `communityIds`（keyword）の**追加** | マッピングを追加してから著者を再インデックス |

対象インデックスを確認する。

```sh
${COMPOSE} exec -T elasticsearch curl -s "localhost:9200/_cat/indices?v"
```

`<prefix>-authors-author-v1.0.0` の形式のものが対象である
（`<prefix>` は `SEARCH_INDEX_PREFIX`。docker-compose の既定は `tenant1`。
`WEKO_AUTHORS_ES_INDEX_NAME = "{SEARCH_INDEX_PREFIX}-authors"` はエイリアス名）。

```sh
AUTHORS_INDEX=$(${COMPOSE} exec -T elasticsearch \
  curl -s "localhost:9200/_cat/indices/*authors*?h=index" | tr -d '\r' | grep -v '^$' | head -1)
echo "${AUTHORS_INDEX}"

${COMPOSE} exec -T elasticsearch curl -XPUT \
  "localhost:9200/${AUTHORS_INDEX}/_mapping/author-v1.0.0?pretty" \
  -H "Content-Type: application/json" \
  -d '{"properties":{"communityIds":{"type":"keyword"}}}'

# 確認
${COMPOSE} exec -T elasticsearch curl -s \
  "localhost:9200/${AUTHORS_INDEX}/_mapping?pretty" | grep -A2 communityIds
```

### 8-4. dynamic mapping timeout の変更

再インデックス時に dynamic mapping がタイムアウトしないよう 600 秒に延ばす
（`v1.0.8b_v2.0.0.md` 14 章）。

```sh
${COMPOSE} exec -T elasticsearch curl -XPUT localhost:9200/_cluster/settings \
  -H "Content-Type: application/json" \
  -d '{"persistent": {"indices.mapping.dynamic_timeout": "600s"}}'

${COMPOSE} exec -T elasticsearch curl -s "localhost:9200/_cluster/settings?pretty"
```

### 8-5. 再インデックス

`W2025-29.sql` と `update_W2025-29.py` は `records_metadata` / `item_metadata` を直接更新するため、
**全件の再インデックスが必須**である（`update_W2025-29.py` 自身は ES 更新を行わず、
対象 ID を `[FIX] records_metadata:<id>` としてログに出すだけである）。

```sh
# 再インデックス対象の登録
${COMPOSE} exec -T web invenio index reindex --pid-type recid --yes-i-know 2>&1 \
  | tee ${WORK_DIR}/reindex.log

# インデックス処理の実行
${COMPOSE} exec -T web invenio index run --raise-on-error False --chunk-size 50 2>&1 \
  | tee -a ${WORK_DIR}/reindex.log

# 著者DB
${COMPOSE} exec -T web invenio authors reindex --yes-i-know 2>&1 \
  | tee ${WORK_DIR}/reindex_authors.log
```

`--raise-on-error False` で個別アイテムのエラーがあっても処理を継続し、
`--chunk-size 50`（既定 500）で ES / RabbitMQ の負荷を抑える。

> 統計インデックス（`*-stats-*` / `*-events-stats-*`）は再構築できないため、
> `invenio index destroy` は**実行しないこと**。

処理中の負荷確認:

```sh
${COMPOSE} ps
${COMPOSE} exec -T elasticsearch curl -s "localhost:9200/_cluster/health?pretty"
```

件数照合:

```sh
${COMPOSE} exec postgresql psql -U invenio -d invenio -qtAX -c \
 "SELECT count(*) FROM pidstore_pid WHERE pid_type='recid' AND status='R';"
${COMPOSE} exec -T elasticsearch curl -s "localhost:9200/_cat/indices?v"
```

### 8-6. 静的リソースの再生成

```sh
${COMPOSE} exec -T web invenio assets build
${COMPOSE} exec -T web invenio collect -v
${COMPOSE} exec -T web bash -c \
  "jinja2 /code/scripts/instance.cfg > /home/invenio/.virtualenvs/invenio/var/instance/invenio.cfg"
${COMPOSE} restart web worker
```

---

## 9. 動作確認チェックリスト

`v1.0.8b_v2.0.0.md` 17 章の項目に、制限公開まわりを追加したもの。

- [ ] トップページが表示され、HTTP 500 / 502 が発生しない
- [ ] 管理者でログインできる／一般ユーザーでログインできる
- [ ] Shibboleth 利用時: ログインでき、`eppn` / `persistent-id` のマッピングが正しい
- [ ] トップページ／検索が表示される（検索結果件数に不自然な差異がない）
- [ ] アイテム詳細画面が表示され、ファイルがダウンロードできる
- [ ] **制限公開アイテムの利用申請フォームが表示され、申請できる**
- [ ] **ワークフローに制限公開の承認アクションが表示される**
- [ ] Administration > 制限公開（利用申請）設定が表示される
- [ ] シークレットURL の発行・ダウンロード（v2.0 新機能。`max_secret_download_limit` = 10、`max_secret_expiration_date` = 30 が既定で入る）
- [ ] アイテム登録・編集・承認が通る
- [ ] 著者DB の検索・編集（`communityIds` 追加後の再インデックス結果）
- [ ] OAI-PMH の応答
- [ ] メール送信（`mail_templates` / `mail_template_users` の To/CC/BCC）
- [ ] 統計（`*-stats-*` が残っていること）
- [ ] `${COMPOSE} logs web worker` にエラーが出ていない

---

## 10. 切り戻し

```sh
cd ${WEKO_DIR}
${COMPOSE} down

git checkout feature/restricted_v1.0.7
cp ${WORK_DIR}/instance.cfg scripts/instance.cfg

DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 ${COMPOSE} build --no-cache --force-rm
${COMPOSE} up -d postgresql

# DB リストア
docker cp ${WORK_DIR}/invenio_YYYYMMDDHHMM.dump $(${COMPOSE} ps -q postgresql):/tmp/restore.dump
${COMPOSE} exec -T postgresql pg_restore -U invenio -d invenio --clean --if-exists /tmp/restore.dump

${COMPOSE} up -d
${COMPOSE} exec -T web invenio index reindex -t recid --yes-i-know
${COMPOSE} exec -T web invenio index run
```

`W2025-29.sql` 適用**前**に切り戻す場合は git のブランチ戻しと再ビルドのみでよい。
`update_W2025-29.py` を流した後はメタデータが書き換わっているため、**必ず DB リストアが必要**である。

---

## 11. NII に確認すべき事項

`v1.0.8b_v2.0.0.md` により、マイグレーション本体（W2025-29.sql / update_W2025-29.py 30015 500 /
communityIds マッピング / reindex）と引数の妥当性は確認済みである。
残る未確認事項は、**起点が `feature/restricted_v1.0.7` であること**に起因するもののみ。

1. **3-3 で判定した v1.0.7a2 / v1.0.7b / fix_issue45092 の適用要否と適用順序**
   （`v1.0.8b_v2.0.0.md` は起点が v1.0.8b のため、これらは既に当たっている前提。
   本移行では未適用の可能性が高く、`W2025-29.sql` の**前**に適用してよいかを確認する）
2. **制限公開機能を有効のまま移行する場合の追加手順の有無**
   （`restricted_access_enable_accessRequestFunc.md` は v2.0 系で新たに有効化する機関向け。
   その検証ツール `tools/verify_restricted_records.py` / `tools/verify_restricted_update.sh` は
   v2.0.3 に未収録で `fix/restricted_update_202606` 等のブランチにのみ存在する。
   本移行でも移行後の検証に使うべきか）
3. **`inbox` / `mongo` を本番構成に含めるか**（`weko-k8s` には未収録）
4. `alembic_version` を stamp する運用があるか
   （`W2025-29.sql` は alembic リビジョンを SQL 化したもので `alembic_version` を更新しない）

---

## アップデート処理の流れ

```text
事前調査(3章) ─ 未適用パッチの判定 / instance.cfg 差分 / 制限公開プロパティID
    ↓
リハーサル(4章)
    ↓
バックアップ(5章)
    ↓
WEKO 停止 → v2.0.3 チェックアウト(6-1,6-2)
    ↓
instance.cfg / weko.conf / uwsgi.ini 更新(6-3)  ← 制限公開フラグ True
    ↓
イメージビルド(6-4) → postgresql のみ起動(6-5)
    ↓
未適用パッチ SQL(7-1)  ← 本移行に固有
    ↓
W2025-29.sql(7-2) → 確認(7-3)
    ↓
WEKO 起動(8-1)
    ↓
update_W2025-29.py 30015 500 (8-2)
    ↓
ES mapping communityIds 追加(8-3)
    ↓
dynamic mapping timeout 600s(8-4)
    ↓
reindex(8-5)
    ↓
assets build / collect(8-6)
    ↓
動作確認(9章)
```

---

## 付録: 実行スクリプト

`weko` リポジトリ直下に配置して使う。

```
tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh
```

```sh
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh check     # 3章  事前調査（更新なし）
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh backup    # 5章  DB/設定のバックアップ
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh config    # 6-3  制限公開フラグの設定
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh build     # 6-4,6-5 ビルド + postgresql 起動
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh migrate   # 7章  未適用パッチ + W2025-29.sql
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh data      # 8-1,8-2 起動 + update_W2025-29.py
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh reindex   # 8-3〜8-5 mapping + timeout + reindex
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh assets    # 8-6  assets build / collect
./tools/upgrade_restricted_v1.0.7_to_v2.0.3.sh verify    # 7-3 / 9章の機械的確認
```
