## コンフィグ

1.優先度

invenio.cfg(instans.cfg) \> config.py(各モジュール)

2.invenio.cfg

  - webコンテナビルド時にinstance.cfgから invenio.cfg([コンフィグ一覧](https://redmine.devops.rcos.nii.ac.jp/attachments/26751/invenio_cfg.xlsx) )が生成される。
    
      - instance.cfg: <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg>

  - 各configのパラメータについて、以下のパラメータが「invenio.cfg」にてオーバーライド可能である。

> TEMPLATES\_AUTO\_RELOAD
> 
> SQLALCHEMY\_DATABASE\_URI
> 
> SQLALCHEMY\_TRACK\_MODIFICATIONS
> 
> DB\_POOL\_CLASS
> 
> COLLECT\_STORAGE
> 
> INDEXER\_BULK\_REQUEST\_TIMEOUT
> 
> CACHE\_TYPE
> 
> CACHE\_REDIS\_HOST
> 
> CACHE\_REDIS\_URL
> 
> ACCOUNTS\_SESSION\_REDIS\_URL
> 
> BROKER\_URL
> 
> CELERY\_BROKER\_URL
> 
> CELERY\_RESULT\_BACKEND
> 
> CELERY\_BEAT\_SCHEDULE
> 
> SEARCH\_ELASTIC\_HOSTS
> 
> SEARCH\_INDEX\_PREFIX
> 
> JSONSCHEMAS\_ENDPOINT
> 
> JSONSCHEMAS\_HOST
> 
> OAISERVER\_REPOSITORY\_NAME
> 
> OAISERVER\_RECORD\_INDEX
> 
> OAISERVER\_ID\_PREFIX
> 
> APP\_DEFAULT\_SECURE\_HEADERS
> 
> SESSION\_COOKIE\_DOMAIN
> 
> SESSION\_COOKIE\_SAMESITE
> 
> SESSION\_COOKIE\_SECURE
> 
> BABEL\_DEFAULT\_LOCALE
> 
> BABEL\_DEFAULT\_LANGUAGE
> 
> I18N\_LANGUAGES
> 
> I18N\_TRANSLATIONS\_PATHS
> 
> SECURITY\_EMAIL\_SENDER
> 
> THEME\_MATHJAX\_CDN
> 
> FILES\_REST\_STORAGE\_FACTORY
> 
> S3\_ACCCESS\_KEY\_ID
> 
> S3\_SECRECT\_ACCESS\_KEY
> 
> S3\_SEND\_FILE\_DIRECTLY
> 
> S3\_ENDPOINT\_URL
> 
> FILES\_REST\_LOCATION\_TYPE\_LIST
> 
> WEKO\_JUPYTERHUB\_ENABLE
> 
> WEKO\_JUPYTERHUB\_URL
> 
> THEME\_SITENAME
> 
> THEME\_SITEURL
> 
> WEKO\_RECORDS\_UI\_LICENSE\_ICON\_LOCATION
> 
> WEKO\_RECORDS\_UI\_LICENSE\_ICON\_PDF\_LOCATION
> 
> WEKO\_RECORDS\_UI\_LICENSE\_DICT
> 
> WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED
> 
> WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_URL
> 
> WEKO\_ACCOUNTS\_SSO\_ATTRIBUTE\_MAP
> 
> WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_ENABLED
> 
> WEKO\_ACCOUNTS\_SHIB\_DP\_LOGIN\_DIRECTLY\_ENABLED
> 
> WEKO\_ACCOUNTS\_SHIB\_INST\_LOGIN\_DIRECTLY\_ENABLED
> 
> WEKO\_ITEMTYPES\_UI\_UPGRADE\_VERSION\_ENABLED
> 
> WEKO\_WORKFLOW\_MAIL\_TEMPLATE\_FOLDER\_PATH
> 
> WEKO\_WORKFLOW\_ACCESS\_ACTIVITY\_URL
> 
> WEKO\_WORKFLOW\_USAGE\_REPORT\_ACTIVITY\_URL
> 
> WEKO\_WORKFLOW\_APPROVE\_DONE
> 
> WEKO\_WORKFLOW\_APPROVE\_REJECTED
> 
> WEKO\_WORKFLOW\_REQUEST\_APPROVAL
> 
> WEKO\_WORKFLOW\_REQUEST\_FOR\_REGISTER\_USAGE\_REPORT
> 
> WEKO\_WORKFLOW\_USAGE\_REPORT\_WORKFLOW\_NAME
> 
> WEKO\_RECORDS\_UI\_SECRET\_KEY
> 
> WEKO\_ITEMS\_UI\_HIDE\_AUTO\_FILL\_METADATA

3.config.py

<table>
<thead>
<tr class="header">
<th><blockquote>
<p>モジュール</p>
</blockquote></th>
<th>configuration</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>invenio-accounts</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-accounts/invenio_accounts/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-accounts/invenio_accounts/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-communities</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-communities/invenio_communities/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-communities/invenio_communities/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-db</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-db/invenio_db/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-db/invenio_db/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-deposit</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-deposit/invenio_deposit/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-deposit/invenio_deposit/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-files-rest</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-iiif</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-iiif/invenio_iiif/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-iiif/invenio_iiif/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-indexer</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-indexer/invenio_indexer/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-indexer/invenio_indexer/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-mail</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-mail/invenio_mail/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-mail/invenio_mail/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-oaiharvester</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiharvester/invenio_oaiharvester/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiharvester/invenio_oaiharvester/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-oaiserver</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oaiserver/invenio_oaiserver/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-oauth2server</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oauth2server/invenio_oauth2server/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-oauth2server/invenio_oauth2server/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-previewer</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-previewer/invenio_previewer/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-previewer/invenio_previewer/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-queues</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-queues/invenio_queues/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-queues/invenio_queues/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-records</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records/invenio_records/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records/invenio_records/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-records-rest</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records-rest/invenio_records_rest/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-records-rest/invenio_records_rest/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-resourcesyncclient</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncclient/invenio_resourcesyncclient/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncclient/invenio_resourcesyncclient/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-resourcesyncserver</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-resourcesyncserver/invenio_resourcesyncserver/config.py</a></td>
</tr>
<tr class="even">
<td>invenio-s3</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-s3/invenio_s3/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-s3/invenio_s3/config.py</a></td>
</tr>
<tr class="odd">
<td>invenio-stats</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/config.py</a></td>
</tr>
<tr class="even">
<td>weko-accounts</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-admin</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py</a></td>
</tr>
<tr class="even">
<td>weko-authors</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-bulkupdate</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-bulkupdate/weko_bulkupdate/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-bulkupdate/weko_bulkupdate/config.py</a></td>
</tr>
<tr class="even">
<td>weko-deposit</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-gridlayout</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-gridlayout/weko_gridlayout/config.py</a></td>
</tr>
<tr class="even">
<td>weko-groups</td>
<td>config.py無し</td>
</tr>
<tr class="odd">
<td>weko-handle</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-handle/weko_handle/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-handle/weko_handle/config.py</a></td>
</tr>
<tr class="even">
<td>weko-index-tree</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-index-tree/weko_index_tree/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-index-tree/weko_index_tree/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-indextree-journal</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-indextree-journal/weko_indextree_journal/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-indextree-journal/weko_indextree_journal/config.py</a></td>
</tr>
<tr class="even">
<td>weko-items-autofill</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-autofill/weko_items_autofill/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-autofill/weko_items_autofill/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-items-ui</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/config.py</a></td>
</tr>
<tr class="even">
<td>weko-itemtypes-ui</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-itemtypes-ui/weko_itemtypes_ui/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-logging</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-logging/weko_logging/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-logging/weko_logging/config.py</a></td>
</tr>
<tr class="even">
<td>weko-plugins</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-plugins/weko_plugins/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-plugins/weko_plugins/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-records</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records/weko_records/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records/weko_records/config.py</a></td>
</tr>
<tr class="even">
<td>weko-records-ui</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-redis</td>
<td>config.py無し</td>
</tr>
<tr class="even">
<td>weko-schema-ui</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-schema-ui/weko_schema_ui/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-schema-ui/weko_schema_ui/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-search-ui</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-search-ui/weko_search_ui/config.py</a></td>
</tr>
<tr class="even">
<td>weko-sitemap</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-sitemap/weko_sitemap/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-theme</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/config.py</a></td>
</tr>
<tr class="even">
<td>weko-user-profiles</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py</a></td>
</tr>
<tr class="odd">
<td>weko-workflow</td>
<td><a href="https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py">https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py</a></td>
</tr>
</tbody>
</table>

  - > 更新履歴

<table>
<thead>
<tr class="header">
<th>日付</th>
<th>GitHubコミットID</th>
<th>更新内容</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>