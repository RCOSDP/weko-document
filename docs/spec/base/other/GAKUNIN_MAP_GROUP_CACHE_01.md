## mAPグループ連携（グループ情報キャッシュ）

1\. 概要

  - 学認クラウドゲートウェイサービス（以下 mAP）のグループ（mAPグループ）を WEKO3 で利用するための、システム全体の構成と、システム間で受け渡す Redis キャッシュの形式を定める

  - WEKO3 は mAP のグループを作成・変更しない。グループの作成から WEKO3 への反映までは、以下の3つのシステムで分担する

    | システム | リポジトリ | 役割 |
    | ---- | ---- | ---- |
    | JAIRO Cloud Groups Manager | <https://github.com/RCOSDP/jairocloud-groups-manager> | リポジトリ管理者が mAP のグループ・ユーザを作成・管理する Web アプリケーション。キャッシュ更新の手動実行も行える |
    | weko-group-cache-db（`wgcd`） | <https://github.com/RCOSDP/weko-group-cache-db> | 機関ごとに mAP の Groups API からグループ一覧を取得し、Redis にキャッシュする CLI |
    | WEKO3（weko-accounts） | <https://github.com/RCOSDP/weko> | Redis のキャッシュを読み、mAPグループを `accounts_role` に登録する。ログイン時に `isMemberOf` 属性からユーザにロール・mAPグループを付与する |

2\. 全体構成

```
 [リポジトリ管理者]
       │ (1) グループ・ユーザの作成/編集
       ▼
 ┌─────────────────────────────┐   (1') mAP API           ┌──────────────────────┐
 │ JAIRO Cloud Groups Manager  │ ───────────────────────▶ │                      │
 └─────────────────────────────┘                          │  学認クラウド        │
       │ (2') キャッシュ更新の手動実行                    │  ゲートウェイ (mAP)  │
       │      (Celery 経由で wgcd を呼ぶ)                 │                      │
       ▼                                                  │                      │
 ┌─────────────────────────────┐   (2) GET Groups API     │                      │
 │ weko-group-cache-db (wgcd)  │ ───────────────────────▶ │                      │
 │  定期実行 / 手動実行        │   機関ごとの TLS         │                      │
 └─────────────────────────────┘   クライアント証明書     └──────────────────────┘
       │ (3) HSET <repository_id>_gakunin_groups                    │
       ▼                                                            │ isMemberOf 属性
 ┌─────────────────────────────┐                                    │ (Shibboleth 経由)
 │ Redis  (DB: GROUP_INFO_REDIS_DB, 既定 4)                         │
 └─────────────────────────────┘                                    │
       │ (4) HGETALL                                                ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ WEKO3 (weko-accounts)                                                │
 │  (4) sync_shib_gakunin_map_groups: mAPグループを登録/削除            │
 │  (5) ShibUser.check_in: isMemberOf からログインユーザにロールを付与  │
 └──────────────────────────────────────────────────────────────────────┘
```

  - (1) リポジトリ管理者が Groups Manager でグループを作成する。Groups Manager は mAP API にグループを登録する

  - (2) `wgcd` が機関ごとに mAP の Groups API（`<MAP_GROUPS_API_ENDPOINT><SPコネクタID>`）を呼び、SP コネクタに紐づくグループ ID の一覧を取得する

    - SP コネクタ ID は `jc_<repository_id>` とする（`repository_id` は「3. Redis キャッシュの形式」を参照）

    - 認証には機関ごとの TLS クライアント証明書・鍵を用いる

    - (2') Groups Manager の画面から同じ処理を実行することもできる。この場合 Groups Manager は Celery タスクから `weko_group_cache_db.groups.fetch_all()` を呼ぶ

  - (3) `wgcd` が取得したグループ ID の一覧を Redis に書き込む

  - (4) WEKO3 は以下の契機で Redis からグループ ID の一覧を読み、`accounts_role` に登録された mAPグループを同期する（`weko_accounts.api.sync_shib_gakunin_map_groups`）

    - Shibboleth ログイン時（`weko_accounts.views.shib_sp_login`）

    - インデックスツリー管理画面の表示時（`weko_index_tree.admin`）

  - (5) Shibboleth ログイン時に、`isMemberOf` 属性に含まれる mAPグループに応じて、ユーザにロール・mAPグループを付与する（詳細は [Shibboleth対応](./SHIBBOLETH_01.md) を参照）

  - (2)〜(4) はいずれも `WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS = True` のときのみ WEKO3 側で利用される

3\. Redis キャッシュの形式

  - 本節は `wgcd`（書き込み側）と WEKO3（読み込み側）の間の取り決めである。いずれかを変更する場合は、もう一方も合わせて変更すること

  - 格納先

    - Redis の DB 番号は WEKO3 の `GROUP_INFO_REDIS_DB`（既定 4）と、`wgcd` の Redis 接続設定とで一致させる

  - キー

    - `<repository_id><suffix>` とする

    - `repository_id` はリポジトリ（SP）の FQDN の "." と "-" を "_" に置き換えた値とする

      - 例：`xxx.repo.nii.ac.jp` → `xxx_repo_nii_ac_jp`

    - `suffix` は `_gakunin_groups` とする

      - 例：`xxx_repo_nii_ac_jp_gakunin_groups`

    - キーの生成元

      | | 生成元 | 設定 |
      | ---- | ---- | ---- |
      | wgcd | FQDN リスト（`-l`）または機関情報 TOML（`-f`）に記載したリポジトリの FQDN | `CACHE_KEY_SUFFIX`（既定 `_gakunin_groups`） |
      | WEKO3 | `WEKO_ACCOUNTS_IDP_ENTITY_ID` の URL のホスト部（ポート番号を除く） | `WEKO_ACCOUNTS_GAKUNIN_GROUP_SUFFIX`（既定 `_gakunin_groups`） |

    - **`WEKO_ACCOUNTS_IDP_ENTITY_ID` には、リポジトリの Shibboleth SP のエンティティ ID を設定すること。** 設定名に反して IdP のエンティティ ID ではない。IdP のエンティティ ID を設定するとキーが一致せず、WEKO3 はキャッシュが存在しないものとして、エラーを出さずにロールの同期を行わない

  - 型と値

    - ハッシュ型とし、以下のフィールドを持つ

      | フィールド | 値 | 例 |
      | ---- | ---- | ---- |
      | `groups` | グループ ID をカンマ区切りで連結した文字列。グループ ID は mAP の Groups API が返す `id` の最後の "/" 以降 | `jc_roles_sysadm,jc_xxx_repo_nii_ac_jp_ro_radm,jc_xxx_repo_nii_ac_jp_gr_lab1` |
      | `updated_at` | キャッシュを作成した日時（UTC、ISO 8601、秒精度） | `2025-11-14T04:27:28+00:00` |

    - WEKO3 が参照するのは `groups` のみである。`updated_at` は Groups Manager の画面表示に用いる

  - 有効期限

    - `wgcd` は書き込みのたびに `CACHE_TTL`（既定 86400 秒）の有効期限を設定する。`CACHE_TTL` が負の場合は有効期限を設定しない

    - 有効期限が切れてキーが消えると、WEKO3 は mAPグループの同期を行わない。登録済みの mAPグループは削除されず、新しく作成されたグループが反映されなくなる。このため `wgcd` は `CACHE_TTL` より短い間隔で定期実行する必要がある

  - グループ ID の命名規則

    - Groups Manager は以下の命名規則でグループを作成する（Groups Manager の `[groups.id_patterns]` 設定）。WEKO3 はこの規則を `WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT` で解釈する

      | 種別（Groups Manager） | 仕様書での名称 | グループ ID | WEKO3 での扱い |
      | ---- | ---- | ---- | ---- |
      | システム管理者 | mAPロールグループ | `jc_roles_sysadm` | `sysadm_group`。ログイン時に `WEKO_ADMIN_PERMISSION_ROLE_SYSTEM` のロールを付与する |
      | リポジトリ管理者 | mAPロールグループ | `jc_<repository_id>_ro_radm` | ログイン時に Repository Administrator を付与する |
      | コミュニティ管理者 | mAPロールグループ | `jc_<repository_id>_ro_cadm` | ログイン時に Community Administrator を付与する |
      | コントリビュータ | mAPロールグループ | `jc_<repository_id>_ro_cont` | ログイン時に Contributor を付与する |
      | 一般ユーザ | mAPロールグループ | `jc_<repository_id>_ro_user` | `role_mapping` に定義がないため、WEKO3 の既定ロールには対応づけない |
      | ユーザー定義グループ | mAPユーザー定義グループ | `jc_<repository_id>_gr_<任意のID>` | インデックスの閲覧・投稿権限の設定に用いる |

  - WEKO3 での同期処理

    - `groups` に含まれ、`accounts_role` に存在しないグループ ID は、グループ ID を名前として `accounts_role` に登録する。あわせてインデックスツリーの閲覧・投稿権限の初期値を設定する（`WEKO_INDEXTREE_GAKUNIN_GROUP_DEFAULT_BROWSING_PERMISSION` / `WEKO_INDEXTREE_GAKUNIN_GROUP_DEFAULT_CONTRIBUTE_PERMISSION`）

    - `accounts_role` のレコードのうち、`groups` に含まれず、かつ名前が `jc_roles_sysadm` であるか `jc_<repository_id>_` で始まるもの（mAPグループ）は削除する

    - 上記以外のレコード（ロール）は変更しない

  - 用語（mAPロールグループ、mAPユーザー定義グループ、mAPグループ）は[用語集](../GLOSSARY.md#ロールとグループ)の定義に従う

4\. 関連設定

  - WEKO3（`instance.cfg`）

    | 設定キー | 説明 | 既定値 |
    | ---- | ---- | ---- |
    | WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS | mAPグループ連携を有効にする | False |
    | WEKO_ACCOUNTS_IDP_ENTITY_ID | リポジトリの Shibboleth SP のエンティティ ID。キャッシュのキーの生成元 | "" |
    | WEKO_ACCOUNTS_GAKUNIN_GROUP_SUFFIX | キャッシュのキーの suffix | "_gakunin_groups" |
    | WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT | グループ ID の命名規則と、ロールとの対応 | 「3. Redis キャッシュの形式」を参照 |
    | GROUP_INFO_REDIS_DB | キャッシュを格納する Redis の DB 番号 | 4 |

  - weko-group-cache-db（`config.toml`）

    | 設定キー | 説明 | 既定値 |
    | ---- | ---- | ---- |
    | map_groups_api_endpoint | mAP の Groups API のエンドポイント | — |
    | sp_connector_id_prefix | SP コネクタ ID の接頭辞 | "jc_" |
    | cache_key_suffix | キャッシュのキーの suffix。WEKO3 の WEKO_ACCOUNTS_GAKUNIN_GROUP_SUFFIX と一致させる | "_gakunin_groups" |
    | cache_ttl | キャッシュの有効期限（秒） | 86400 |
    | redis_type / redis_host / redis_port / redis_db_index | 書き込み先の Redis。redis_db_index は WEKO3 の GROUP_INFO_REDIS_DB と一致させる | redis_db_index: 4 |

    - `redis_type` に指定できる値は、1.0.0rc4 では `redis` / `sentinel`、1.0.0rc6 以降では `RedisCache` / `RedisSentinelCache` である

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2026/10/25 |  | 初版作成 |
