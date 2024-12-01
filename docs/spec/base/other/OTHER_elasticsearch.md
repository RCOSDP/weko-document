# elasticsearch



indices

> $ docker-compose exec elasticsearch curl -s http://localhost:9200/\_cat/indices?h=i|sort
> 
> \~snip\~
> 
> tenant1-authors-author-v1.0.0
> 
> tenant1-deposits-deposit-v1.0.0
> 
> tenant1-events-stats-celery-task-000001
> 
> tenant1-events-stats-file-download-000001
> 
> tenant1-events-stats-file-preview-000001
> 
> tenant1-events-stats-item-create-000001
> 
> tenant1-events-stats-record-view-000001
> 
> tenant1-events-stats-search-000001
> 
> tenant1-events-stats-top-view-000001
> 
> tenant1-marc21-authority-ad-v1.0.0
> 
> tenant1-marc21-bibliographic-bd-v1.0.0
> 
> tenant1-marc21-holdings-hd-v1.0.0
> 
> tenant1-stats-bookmarks
> 
> tenant1-stats-celery-task-000001
> 
> tenant1-stats-file-download-000001
> 
> tenant1-stats-file-preview-000001
> 
> tenant1-stats-item-create-000001
> 
> tenant1-stats-record-view-000001
> 
> tenant1-stats-search-000001
> 
> tenant1-stats-top-view-000001
> 
> tenant1-weko-item-v1.0.0

template

> docker-compose exec elasticsearch curl -s http://localhost:9200/\_cat/templates?h=n,t|grep tenant1|sort
> 
> \~snip\~
> 
> tenant1-aggregations-aggr\_celery\_task/v6-aggr-celery-task-v1 \[tenant1-stats-celery-task-\*\]
> 
> tenant1-aggregations-aggr\_file\_download/v6-aggr-file-download-v1 \[tenant1-stats-file-download-\*\]
> 
> tenant1-aggregations-aggr\_file\_preview/v6-aggr-file-preview-v1 \[tenant1-stats-file-preview-\*\]
> 
> tenant1-aggregations-aggr\_item\_create/v6-aggr-item-create-v1 \[tenant1-stats-item-create-\*\]
> 
> tenant1-aggregations-aggr\_record\_view/v6-aggr-record-view-v1 \[tenant1-stats-record-view-\*\]
> 
> tenant1-aggregations-aggr\_search/v6-aggr-search-v1 \[tenant1-stats-search-\*\]
> 
> tenant1-aggregations-aggr\_top\_view/v6-aggr-top-view-v1 \[tenant1-stats-top-view-\*\]
> 
> tenant1-celery\_task/v6-celery-task-v1 \[tenant1-events-stats-celery-task-\*\]
> 
> tenant1-file\_download/v6-file-download-v1 \[tenant1-events-stats-file-download-\*\]
> 
> tenant1-file\_preview/v6-file-preview-v1 \[tenant1-events-stats-file-preview-\*\]
> 
> tenant1-item\_create/v6-item-create-v1 \[tenant1-events-stats-item-create-\*\]
> 
> tenant1-record\_view/v6-record-view-v1 \[tenant1-events-stats-record-view-\*\]
> 
> tenant1-search/v6-search-v1 \[tenant1-events-stats-search-\*\]
> 
> tenant1-top\_view/v6-top-view-v1 \[tenant1-events-stats-top-view-\*\]

  - マッピング
    
      - item（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-schema-ui/weko\_schema\_ui/mappings/v6/weko/item-v1.0.0.json）
    
      - author（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko\_authors/mappings/v6/authors/author-v1.0.0.json）
    
      - file-download（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats//contrib/file\_download/v6/file-download-v1.json）
    
      - file-preview（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/file\_preview/v6/file-preview-v1.json）
    
      - item-create（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/item\_create/v6/item-create-v1.json）
    
      - record-view（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/ invenio\_stats /contrib/record\_view/v6/record-view-v1.json）
    
      - search（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/search/v6/search-v1.json）
    
      - top-view（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/top\_view/v6/top-view-v1.json）
    
      - celery-task（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/celery\_task/v6/celery-task-v1.json）
    
      - aggr-file-download（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/aggregations/aggr\_file\_download/v6/aggr-file-download-v1.json）
    
      - aggr-file-preview（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/aggregations/aggr\_file\_preview/v6/aggr-file-preview-v1.json）
    
      - aggr-item-create（<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/contrib/aggregations/aggr_item_create/v6/aggr-item-create-v1.json>）
    
      - aggr-record-view（<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio_stats/contrib/aggregations/aggr_record_view/v6/aggr-record-view-v1.json>）
    
      - aggr-search（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/aggregations/aggr\_search/v6/aggr-search-v1.json）
    
      - aggr-top-view（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/aggregations/aggr\_top\_view/v6/aggr-top-view-v1.json）
    
      - aggr-celery-task（https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-stats/invenio\_stats/contrib/aggregations/aggr\_celery\_task/v6/aggr-celery-task-v1.json）

Invenio index コマンドによる再インデクシング

  - > reindexの処理概要


  ```
  Usage: invenio index reindex [OPTIONS]

  Reindex all records.

  :param pid_type: Pid type.

Options:
  --yes-i-know
  -t, --pid-type TEXT  [required]
  --include-delete
  --skip-exists
  --size INTEGER
  --help 
  ```

invenio index reindex -t recid --yes-i-know

  - select \* from pidstore\_pid where object\_type='rec' and status='R' and pid\_type='recid';
    
      - の、条件にあたるアイテム分のbulk indexing タスクがqueue に登録されます。
    
      - 親情報はpid\_type='parent' のためこの対象になりません。

  - invenio index run --skip-errors
    
      - queueに登録されたタスクが実行されます。
    
      - 既にアイテムのデータがあれば上書き、無ければ新規登録。
    
      - エラーが発生しても他のタスクは処理を続けます。エラーだったものは上書き/新規登録されません。




<!-- end list -->

  - > 使い方

1\) インデックス削除

$ docker-compose exec web invenio index destroy --yes-i-know

2\) インデックス初期化

$ docker-compose exec web invenio index init

3\) インデックスキュー初期化

$ docker-compose exec web invenio index queue init

4\) パイプライン設定　v.1.0.4より不要となりました。

$ curl -XPUT 'http://localhost:29202/\_ingest/pipeline/item-file-pipeline' -H 'Content-Type: application/json' -d '{

"description" : "Index contents of each file.",

"processors" : \[

{

"foreach": {

"field": "content",

"processor": {

"attachment": {

"indexed\_chars" : -1,

"target\_field": "\_ingest.\_value.attachment",

"field": "\_ingest.\_value.file",

"properties": \[

"content"

\]

}

}

}

}

\]

}'

5\) 再インデクシング

$ docker-compose exec web invenio index reindex -t recid --yes-i-know

6\) インデックス登録

$ docker-compose exec web invenio index run --skip-errors


| TH | TH | TH |
| ---- | ---- | ---- |
| Usage: invenio index reindex [OPTIONS] || |
| Reindex all records. | | |
| :param pid_type: Pid type. | | |
| Options: | | |
|  | -t, --pid-type TEXT  [required]  | |
|  | --include-delete  | 削除済みアイテムをreindexする |
|  | --skip-exists  | |
|  | --size INTEGER | |
|  | --help  | |


reindex時、ボディサイズがINDEXER\_MAX\_BODY\_SIZEを超える場合は、BASE64 fileを削除(v1.0.7では意味のない処理)。

```
INDEXER_MAX_BODY_SIZE = 62914560
```

## クエリ例

### root_file_idの値がない(null,"")ドキュメントを検索

```
curl "http://localhost:9200/tenant1-stats-file-download/_search?pretty" -d '{"query":{"bool":{"should":[{"bool":{"must_not":{"exists":{"field":"root_file_id"}}}},{"term":{"root_file_id":""}}]}},"_source":["_id","file_id","root_file_id","bucket_id","file_key"]}' -H 'Content-type: application/json'
```

curl "http://localhost:9200/tenant1-events-stats-file-download/_search?pretty" -d '{"query":{"bool":{"should":[{"bool":{"must_not":{"exists":{"field":"root_file_id"}}}},{"term":{"root_file_id":""}}]}},"_source":["_id","file_id","root_file_id","bucket_id","file_key"]}' -H 'Content-type: application/json'


curl "http://localhost:9200/grips_repo_nii_ac_jp-stats-file-download/_search?pretty" -d '{"query":{"bool":{"should":[{"bool":{"must_not":{"exists":{"field":"root_file_id"}}}},{"term":{"root_file_id":""}}]}},"_source":["_id","file_id","root_file_id","bucket_id","file_key"]}' -H 'Content-type: application/json'

curl "http://localhost:9200/grips_repo_nii_ac_jp-events-stats-file-download/_search?pretty" -d '{"query":{"bool":{"should":[{"bool":{"must_not":{"exists":{"field":"root_file_id"}}}},{"term":{"root_file_id":""}}]}},"_source":["_id","file_id","root_file_id","bucket_id","file_key"]}' -H 'Content-type: application/json'

# curl "http://localhost:9200/grips_repo_nii_ac_jp-events-stats-file-download/_search?pretty" -d '{"query":{"bool":{"must_not":{"exists":{"field":"root_file_id"}}}},"size":0}' -H 'Content-type: appli
cation/json'



curl 'http://localhost:9200/grips_repo_nii_ac_jp-events-stats-file-download-000001/stats-file-download/2021-10-01T10:00:00-6406d627e650ab25cd2bc0b46b07e866d5f09887?pretty'


curl 'http://localhost:9200/grips_repo_nii_ac_jp-stats-file-download-000001/file-download-day-aggregation/420494d5-6a5d-328d-b553-2dd7f3398952?pretty'

curl 'http://localhost:9200/grips_repo_nii_ac_jp-events-stats-file-download-000001/stats-file-download/2021-10-01T10:00:00-6406d627e650ab25cd2bc0b46b07e866d5f09887'



 curl -X POST 'http://localhost:9200/_snapshot/grips/snapshot_all/_restore?wait_for_completion=true' -H 'Content-Type: application/json' -d '{"indices": "grips_repo_nii_ac_jp*","ignore_unavailable": true,"include_global_state": true}'

 curl -X DELETE http://localhost:9200/grips_repo*


###

```
curl "http://localhost:9200/tenant1-events-stats-file-download-000001/stats-file-download/2024-05-02T15:40:30-9262f1675b96f8481cc7c924d4c88a4ebf816649/_update" -d '{"doc":{"file_id":"","root_file_id":""}}' -H 'Content-type: application/json' -X POST
```


## 更新履歴

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
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>