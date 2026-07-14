## コンフィグ

1. 優先度

invenio.cfg(instance.cfg) > config.py(各モジュール)

2. invenio.cfg

- webコンテナビルド時にinstance.cfgから invenio.cfg([コンフィグ一覧](https://redmine.devops.rcos.nii.ac.jp/attachments/26751/invenio_cfg.xlsx))が生成される。
  - instance.cfg: <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg>

- 各configのパラメータについて、以下のパラメータが「invenio.cfg」にてオーバーライド可能である。

```
TEMPLATES_AUTO_RELOAD
SQLALCHEMY_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS
DB_POOL_CLASS
COLLECT_STORAGE
INDEXER_BULK_REQUEST_TIMEOUT
CACHE_TYPE
CACHE_REDIS_HOST
CACHE_REDIS_URL
ACCOUNTS_SESSION_REDIS_URL
BROKER_URL
CELERY_BROKER_URL
CELERY_RESULT_BACKEND
CELERY_BEAT_SCHEDULE
SEARCH_ELASTIC_HOSTS
SEARCH_INDEX_PREFIX
JSONSCHEMAS_ENDPOINT
JSONSCHEMAS_HOST
OAISERVER_REPOSITORY_NAME
OAISERVER_RECORD_INDEX
OAISERVER_ID_PREFIX
APP_DEFAULT_SECURE_HEADERS
SESSION_COOKIE_DOMAIN
SESSION_COOKIE_SAMESITE
SESSION_COOKIE_SECURE
BABEL_DEFAULT_LOCALE
BABEL_DEFAULT_LANGUAGE
I18N_LANGUAGES
I18N_TRANSLATIONS_PATHS
SECURITY_EMAIL_SENDER
THEME_MATHJAX_CDN
FILES_REST_STORAGE_FACTORY
S3_ACCCESS_KEY_ID
S3_SECRET_ACCESS_KEY
S3_SEND_FILE_DIRECTLY
S3_ENDPOINT_URL
FILES_REST_LOCATION_TYPE_LIST
WEKO_JUPYTERHUB_ENABLE
WEKO_JUPYTERHUB_URL
THEME_SITENAME
THEME_SITEURL
WEKO_RECORDS_UI_LICENSE_ICON_LOCATION
WEKO_RECORDS_UI_LICENSE_ICON_PDF_LOCATION
WEKO_RECORDS_UI_LICENSE_DICT
WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED
WEKO_ACCOUNTS_SHIB_IDP_LOGIN_URL
WEKO_ACCOUNTS_SSO_ATTRIBUTE_MAP
WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED
WEKO_ACCOUNTS_SHIB_DP_LOGIN_DIRECTLY_ENABLED
WEKO_ACCOUNTS_SHIB_INST_LOGIN_DIRECTLY_ENABLED
WEKO_ITEMS_AUTOFILL_TO_BE_USED
WEKO_NOTIFICATIONS
WEKO_NOTIFICATIONS_INBOX_ADDRESS
WEKO_NOTIFICATIONS_INBOX_ENDPOINT
WEKO_NOTIFICATIONS_PUSH_TEMPLATE_PATH
WEKO_SWORDSERVER_DIGEST_VERIFICATION
WEKO_SWORDSERVER_BAGIT_VERIFICATION
WEKO_ITEMTYPES_UI_UPGRADE_VERSION_ENABLED
WEKO_ITEMTYPES_UI_FORCED_IMPORT_ENABLED
WEKO_WORKFLOW_MAIL_TEMPLATE_FOLDER_PATH
WEKO_WORKFLOW_ACCESS_ACTIVITY_URL
WEKO_WORKFLOW_REQUEST_APPROVAL
WEKO_WORKFLOW_REQUEST_FOR_REGISTER_USAGE_REPORT
WEKO_WORKFLOW_MAIL_DEFAULT_LANGUAGE
WEKO_WORKFLOW_USAGE_REPORT_WORKFLOW_NAME
WEKO_RECORDS_UI_SECRET_KEY
WEKO_ITEMS_UI_HIDE_AUTO_FILL_METADATA
WEKO_AUTHORS_EXPORT_TMP_DIR
WEKO_AUTHORS_IMPORT_TMP_DIR
WEKO_RECORDS_UI_OA_GET_TOKEN_URL
WEKO_RECORDS_UI_OA_UPDATE_STATUS_URL
WEKO_RECORDS_UI_OA_GET_OA_POLICIES_URL
```

3. config.py

| モジュール | configuration |
| ---- | ---- |
| invenio-accounts | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-accounts/invenio_accounts/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-accounts/invenio_accounts/config.py) |
| invenio-communities | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-communities/invenio_communities/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-communities/invenio_communities/config.py) |
| invenio-db | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-db/invenio_db/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-db/invenio_db/config.py) |
| invenio-deposit | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-deposit/invenio_deposit/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-deposit/invenio_deposit/config.py) |
| invenio-files-rest | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/config.py) |
| invenio-iiif | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-iiif/invenio_iiif/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-iiif/invenio_iiif/config.py) |
| invenio-indexer | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-indexer/invenio_indexer/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-indexer/invenio_indexer/config.py) |
| invenio-mail | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-mail/invenio_mail/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-mail/invenio_mail/config.py) |
| invenio-oaiharvester | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiharvester/invenio_oaiharvester/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiharvester/invenio_oaiharvester/config.py) |
| invenio-oaiserver | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py) |
| invenio-oauth2server | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oauth2server/invenio_oauth2server/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oauth2server/invenio_oauth2server/config.py) |
| invenio-previewer | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-previewer/invenio_previewer/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-previewer/invenio_previewer/config.py) |
| invenio-queues | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-queues/invenio_queues/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-queues/invenio_queues/config.py) |
| invenio-records | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records/invenio_records/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records/invenio_records/config.py) |
| invenio-records-rest | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records-rest/invenio_records_rest/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records-rest/invenio_records_rest/config.py) |
| invenio-resourcesyncclient | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncclient/invenio_resourcesyncclient/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncclient/invenio_resourcesyncclient/config.py) |
| invenio-resourcesyncserver | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py) |
| invenio-s3 | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-s3/invenio_s3/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-s3/invenio_s3/config.py) |
| invenio-stats | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/config.py) |
| weko-accounts | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py) |
| weko-admin | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py) |
| weko-authors | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py) |
| weko-bulkupdate | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-bulkupdate/weko_bulkupdate/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-bulkupdate/weko_bulkupdate/config.py) |
| weko-deposit | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py) |
| weko-gridlayout | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py) |
| weko-groups | config.py無し |
| weko-handle | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-handle/weko_handle/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-handle/weko_handle/config.py) |
| weko-index-tree | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-index-tree/weko_index_tree/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-index-tree/weko_index_tree/config.py) |
| weko-indextree-journal | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-indextree-journal/weko_indextree_journal/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-indextree-journal/weko_indextree_journal/config.py) |
| weko-items-autofill | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-autofill/weko_items_autofill/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-autofill/weko_items_autofill/config.py) |
| weko-items-ui | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/config.py) |
| weko-itemtypes-ui | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py) |
| weko-logging | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-logging/weko_logging/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-logging/weko_logging/config.py) |
| weko-plugins | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-plugins/weko_plugins/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-plugins/weko_plugins/config.py) |
| weko-records | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records/weko_records/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records/weko_records/config.py) |
| weko-records-ui | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py) |
| weko-redis | config.py無し |
| weko-schema-ui | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-schema-ui/weko_schema_ui/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-schema-ui/weko_schema_ui/config.py) |
| weko-search-ui | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py) |
| weko-sitemap | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py) |
| weko-theme | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/config.py) |
| weko-user-profiles | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py) |
| weko-workflow | [https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py](https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py) |
| weko-notifications | [https://github.com/RCOSDP/weko/blob/main/modules/weko-notifications/weko_notifications/config.py](https://github.com/RCOSDP/weko/blob/main/modules/weko-notifications/weko_notifications/config.py) |
| weko-signposting | [https://github.com/RCOSDP/weko/blob/main/modules/weko-signposting/weko_signposting/config.py](https://github.com/RCOSDP/weko/blob/main/modules/weko-signposting/weko_signposting/config.py) |
| weko-swordserver | [https://github.com/RCOSDP/weko/blob/main/modules/weko-swordserver/weko_swordserver/config.py](https://github.com/RCOSDP/weko/blob/main/modules/weko-swordserver/weko_swordserver/config.py) |
| weko-workspace | [https://github.com/RCOSDP/weko/blob/main/modules/weko-workspace/weko_workspace/config.py](https://github.com/RCOSDP/weko/blob/main/modules/weko-workspace/weko_workspace/config.py) |

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/14 |  | 本文を実装準拠に修正 |

## 実装補足（v2.0.2 実装との突き合わせ）

- S3 のキー名は `S3_SECRET_ACCESS_KEY`（`S3_ACCCESS_KEY_ID` の綴りはソース側もこの綴り）。
- `WEKO_WORKFLOW_APPROVE_DONE` / `WEKO_WORKFLOW_APPROVE_REJECTED` / `WEKO_WORKFLOW_USAGE_REPORT_ACTIVITY_URL` は v2.0.2 に存在しない。
- config は `scripts/instance.cfg`（jinja テンプレート）から生成され、環境変数 `environ()` で上書きされる。GitHub参照リンクは v0.9.22 固定で陳腐化。
