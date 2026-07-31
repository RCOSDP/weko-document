# findings v2.1.0（v2.0.2 → develop_v2.1.0 差分反映）

実装リポジトリ `/home/mhaya/weko`（branch `develop_v2.1.0` = `v2.0.2-427-gb19e39d8a`）の tag `v2.0.2` からの差分を機能仕様書へ反映するための調査結果。テーマ別詳細は scratchpad の以下に保存（本セッション）:
`find_A_embargo.md` / `find_B_import.md` / `find_D_workspace.md` / `find_E_itemtype_db.md` / `find_F_perms_misc.md`

## 変更テーマ概要
- **A. エンバーゴ機能の刷新**（新設config `WEKO_SEARCH_FIX_ACCESSRIGHTS` 既定False でゲート）: accessRightsの実効値をファイルの `accessrole`・公開日・現在日から判定し、検索/ファセット/OAI-PMH/ResourceSyncの出し分けに反映。中核 `weko_records/utils.py` `check_embargo_rights`/`update_embargo_rights`、`weko_search_ui/query.py` `__get_accessrights_query`、`invenio_oaiserver/query.py` `range_query`、`invenio_records/api.py` `Record.updated`。
- **B. 一括インポートAPI（新規）**: `weko-items-ui` に OAuth2保護のREST API `POST /api/items/import-task`・`GET /api/items/import-task/get_bulk_import_task_status/<task_id>`。新scope `item:bulkprocess`、新config 3種、限定ロール（System/Repository Administrator）。
- **C. JSON-LDインポート改修**: 置換ルール（`WEKO_SEARCH_UI_IMPORT_REPLACE_RULES`/`_RULE_MAP`）、カスタム語彙 `wk:researchmapLinkage`（SWORD→ワークフロー→`cris_linkage.researchmap`）、SWORDエラー応答へのwarnings併記。
- **D. AMSワークスペース/GRDM/OAuth/SWORD Links**: arXivメタデータ自動補完、export headerサーバ定義化＋先頭「No.」列、DOIリンク導出をrelation(isVersionOf)ベースへ、SWORDステータス`links`にファイルリンク(fileSetFile)・state `inWorkflow`追加、AMSログイン経路、OAuth invalid_scope応答。
- **E. item_type_mapping制約 & マッピング保存刷新**: `ItemTypeMapping.item_type_id` に一意制約＋FK(ON DELETE CASCADE)、`mapping` にGIN、`Mapping.create`→`create_or_update`（1タイプ1行upsert）。
- **G. AMSロール/ロールグループ/インデックス権限**: No Group(-89)既定、インデックス閲覧/投稿が「ロール AND グループ」判定・GakuNin mAPロール除外、コミュニティOwner表示名変換。
- **F. ファイルDL権限**: `open_login`/`open_restricted` にサイトライセンス・フォールバック、サイトライセンス利用者はopen_restrictedのワンタイムDLをスキップ。
- **H. その他fix（仕様影響あり）**: ロケーション権限（作成/編集/削除=システム管理者のみ、リポジトリ管理者はデフォルトも閲覧可 #60332）、ファイルインスタンス削除可能化(#60919)、JPCOAR nameIdentifierScheme置換の不具合修正(#58215)。
- **DBベースライン刷新(#61275)**: 全モジュールのAlembic履歴を新規ベースライン(no-op, down_revision=None)へ再編（論理スキーマ不変）。

## 更新対象 機能仕様書（カテゴリ＝コミット単位）

### api（7）
| ファイル | 反映内容 | テーマ |
|---|---|---|
| api/README.md | API-20 一括インポートAPI を一覧に追加 | B |
| api/API_20_bulk_import.md（新規） | 一括インポートAPI仕様全体 | B |
| api/API_01_Oauth2.md | weko-items-ui スコープに `item:bulkprocess` 追加、invalid_scope時 `/oauth/errors` リダイレクト・errors()の400応答 | B/D |
| api/API_06_sword_api.md | `wk:researchmapLinkage`連携・checkエラー時warnings併記、`links`にファイルリンク(fileSetFile)・複数登録時Activityリンク、state `inWorkflow`、conf `WEKO_SWORDSERVER_FILE_SET_FILE` | C/D |
| api/API_07_item_search.md | `accessrights`パラメータとエンバーゴ考慮出し分け | A |
| api/API_03_OpenSearch.md | `accessrights`パラメータ（`opensearch_factory`経由） | A |
| api/API_02_OAIPMH.md | from/until のエンバーゴ考慮・datestamp繰り上げ | A |

### access_control（3、任意1）
| ファイル | 反映内容 | テーマ |
|---|---|---|
| access_control/USER_ITEM_SEARCH_01.md | エンバーゴ考慮のaccessRightsファセット/絞り込み | A |
| access_control/ADMIN_OAI_PMH_01.md | ハーベスト応答のエンバーゴ考慮 | A |
| access_control/ADMIN_RESOURCE_SYNC_01.md | ChangeListのエンバーゴ考慮 | A |
| access_control/ADMIN_RECORDS_01.md（任意） | レコード取得時のaccessRights動的補正 | A |

### admin（9）
| ファイル | 反映内容 | テーマ |
|---|---|---|
| admin/ADMIN_1_1.md | item_type_mapping の FK(CASCADE)/一意制約 | E |
| admin/ADMIN_1_2.md | `Mapping.create_or_update`（upsert・1タイプ1行）、制約/GIN | E |
| admin/ADMIN_1_5.md | インポート時メタデータ置換ルール | C |
| admin/ADMIN_2_4.md（任意） | テンプレート列 `.bulk_doi`/`.BULK_DOI` | B |
| admin/ADMIN_2_5.md | カスタム語彙 `wk:researchmapLinkage` | C |
| admin/ADMIN_3_1.md | No Group(-89)既定、閲覧/投稿の「ロール AND グループ」判定・mAP除外 | G |
| admin/ADMIN_8_1.md | Owner表示名変換・OwnerプルダウンからのmAPロール除外 | G |
| admin/ADMIN_12_2.md | ファイルインスタンス削除可能化（delete_model） | H |
| admin/ADMIN_12_3.md | ロケーション権限（作成/編集/削除=システム管理者のみ、リポジトリ管理者は閲覧可） | H |

### user（5）
| ファイル | 反映内容 | テーマ |
|---|---|---|
| user/USER_1_3.md | インデックスツリー閲覧判定ロジック補足 | G |
| user/USER_3_2.md | サイトライセンス利用者のopen_login/open_restricted DL・ワンタイム省略 | F |
| user/USER_10_1.md | export headerサーバ定義化＋「No.」列、DOIリンクをrelation(isVersionOf)ベースへ | D |
| user/USER_10_2.md | 簡易登録に arXiv MetaData ラジオ＋endpoint | D |
| user/USER_10_3.md | arXivメタデータ自動補完ソース追加 | D |

### other（4、うちSCHEMAは要確認）／ams（1）
| ファイル | 反映内容 | テーマ |
|---|---|---|
| other/DB_01.md | item_type_mapping制約/GIN/旧btree削除、Alembicベースライン刷新(#61275) | E/G |
| other/SHIBBOLETH_01.md | 各shibビューの ams_login 分岐を補足 | D |
| other/SCHEMA_1_2.md / SCHEMA_1_3.md | JPCOAR nameIdentifierScheme置換の実装準拠（要確認） | H |
| ams/AMS_SHIBBOLETH_01.md | AMSログイン経路（next=ams、失敗時 `/ams/login?error=`、config `WEKO_ACCOUNTS_SHIB_AMS_LOGIN_URL`） | D |

## 仕様書更新不要（主なもの）
- weko-notifications / weko-user-profiles / weko-workspace migration = Alembicベースライン刷新のみ（スキーマ・機能不変）
- weko-authors = Alembicベースライン＋翻訳のみ（機能・スキーマ不変）
- 多言語コンパイル #60737、テスト追加/修正、フォーマット整形
- GRDMボタンのリンク遷移実装＝フロント(detail.vue)のみ（バックエンド変更なし）
- delete_versionのインデックス引き継ぎ / CrossRef autofill relation_type ＝軽微な内部補完（任意）

## 実装側の要注意（報告事項）
- `postgresql/ddl/sp72-createindex.sql` が未修正で item_type_mapping の旧btree 2本＋GIN を作る記述のまま。新規構築時とマイグレーション後（W2025-16.sql適用後＝btree削除・GIN）で最終状態が食い違う懸念。
