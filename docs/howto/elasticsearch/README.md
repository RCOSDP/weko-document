
# 新しいマッピングでreindexする

## エイリアスを確認する

```
curl -X GET "http://elasticsearch:9200/_cat/aliases/tenant1-weko"
```

```
tenant1-weko tenant1-weko-item-v1.0.0 - - -
```

## マッピングを指定してインデックスを作成する

```
curl -s -X PUT "http://elasticsearch:9200/testindex" -d@"item-v1.0.0.json" -H 'Content-type: application/json'
```

```
{"acknowledged":true,"shards_acknowledged":true,"index":"tmpindex"}
```

## 作成したインデックスに既存のインデックスからreindexする

```
curl -s -X POST "http://elasticsearch:9200/_reindex?pretty" -d '{"source":{"index":"tenant1-weko-item-v1.0.0"},"dest":{"index":"tmpindex"}}' -H 'Content-type: application/json'
```

```
{
  "took" : 24,
  "timed_out" : false,
  "total" : 6,
  "updated" : 6,
  "created" : 0,
  "deleted" : 0,
  "batches" : 1,
  "version_conflicts" : 0,
  "noops" : 0,
  "retries" : {
    "bulk" : 0,
    "search" : 0
  },
  "throttled_millis" : 0,
  "requests_per_second" : -1.0,
  "throttled_until_millis" : 0,
  "failures" : [ ]
}
```

## エイリアスに一時的に追加する

```
curl -X POST 'http://elasticsearch:9200/_aliases?pretty' -d '{"actions": [{"add": {"index": "tmpindex","alias": "tenant1-weko"}}]}' -H 'Content-type: application/json'
```

```
{
  "acknowledged" : true
}
```

```
curl -X GET 'http://elasticsearch:9200/_cat/aliases/tenant1-weko'
```

```
tenant1-weko tmpindex                 - - -
tenant1-weko tenant1-weko-item-v1.0.0 - - -
```

## 旧インデックスを削除する

```
curl -X DELETE 'http://elasticsearch:9200/tenant1-weko-item-v1.0.0?pretty'
```

```
{
  "acknowledged" : true
}
```

## 新しいマッピングを指定してインデックスを作成する

```
curl -s -X PUT "http://elasticsearch:9200/tenant1-weko-item-v1.0.0" -d@"item-v1.0.0.json" -H 'Content-type: application/json'
```

```
{"acknowledged":true,"shards_acknowledged":true,"index":"tenant1-weko-item-v1.0.0"}
```

## 一時インデックスの内容をreindexする

```
curl -s -X POST "http://elasticsearch:9200/_reindex?pretty" -d '{"source":{"index":"tmpindex"},"dest":{"index":"tenant1-weko-item-v1.0.0"}}' -H 'Content-type: application/json'
```

```
{
  "took" : 316,
  "timed_out" : false,
  "total" : 6,
  "updated" : 0,
  "created" : 6,
  "deleted" : 0,
  "batches" : 1,
  "version_conflicts" : 0,
  "noops" : 0,
  "retries" : {
    "bulk" : 0,
    "search" : 0
  },
  "throttled_millis" : 0,
  "requests_per_second" : -1.0,
  "throttled_until_millis" : 0,
  "failures" : [ ]
}
```


## エイリアスに移行先インデックスを追加する

```
curl -X POST 'http://elasticsearch:9200/_aliases?pretty' -d '{"actions": [{"add": {"index": "tenant1-weko-item-v1.0.0","alias": "tenant1-weko"}}]}' -H 'Content-type: application/json'
```

```
{
  "acknowledged" : true
}
```

```
curl -X GET 'http://elasticsearch:9200/_cat/aliases/tenant1-weko'
```

```
tenant1-weko tmpindex                 - - -
tenant1-weko tenant1-weko-item-v1.0.0 - - -
```

## 一時インデックスを削除する


```
curl -X DELETE 'http://elasticsearch:9200/tmpindex'
```

```
{"acknowledged":true}
```



```
$ diff -u item-v1.0.0.json modules/weko-schema-ui/weko_schema_ui/mappings/v6/weko/item-v1.0.0.json
--- item-v1.0.0.json    2025-01-12 09:15:34.103889864 +0900
+++ modules/weko-schema-ui/weko_schema_ui/mappings/v6/weko/item-v1.0.0.json     2024-09-25 07:39:45.748205280 +0900
@@ -81,7 +81,7 @@
           "fields": {
             "tree": {
               "type": "text",
-              "fielddata": false,
+              "fielddata": true,
               "analyzer": "paths"
             }
           }
@@ -98,7 +98,7 @@
               "ignore_above": 256
             }
           },
-          "fielddata": false,
+          "fielddata": true,
           "copy_to": [
             "search_other"
           ]
@@ -1096,12 +1096,12 @@
         },
         "weko_creator_id": {
           "type": "text",
-          "fielddata": false,
+          "fielddata": true,
           "index": true
         },
         "weko_id": {
           "type": "text",
-          "fielddata": false,
+          "fielddata": true,
           "index": true
         },
         "search_title": {
@@ -1178,8 +1178,8 @@
             "match": "^weko_id$",
             "mapping": {
               "type": "text",
-              "fielddata": false,
-              "index": true,
+              "fielddata": true,
+              "index": false,
               "copy_to": "weko_id"
             }
           }
@@ -1189,8 +1189,7 @@
             "match_mapping_type": "string",
             "mapping": {
               "type": "text",
-              "index": true,
-              "fielddata": true,
+              "index": false,
               "copy_to": "search_string",
               "fields": {
                 "raw": {
@@ -1206,7 +1205,7 @@
             "match_mapping_type": "date",
             "mapping": {
               "type": "text",
-              "index": true,
+              "index": false,
               "copy_to": "search_string",
               "fields": {
                 "raw": {
```


```
curl -s "http://elasticsearch:9200/tenant1-weko/_search?pretty" -H "Content-type: application/json" -d '{"query": {"bool": {"must": [{"match": {"relation_version_is_last": "true"}}, {"bool": {"must": [{"terms": {"publish_status": ["0", "1"]}}, {"terms": {"path": ["1623632832836"]}}]}}]}}, "post_filter": {"bool": {"must": [{"terms": {"path": ["1623632832836"]}}, {"bool": {"should": [{"bool": {"must": [{"terms": {"publish_status": ["0", "1"]}}, {"match": {"weko_creator_id": "1"}}]}}, {"bool": {"must": [{"terms": {"publish_status": ["0", "1"]}}, {"match": {"weko_shared_id": "1"}}]}}, {"bool": {"must": [{"terms": {"publish_status": ["0", "1"]}}]}}]}}]}}, "aggs": {"path": {"terms": {"field": "path", "include": "1623632832836", "size": "1"}, "aggs": {"date_range": {"filter": {"match": {"publish_status": "0"}}, "aggs": {"available": {"range": {"field": "publish_date", "ranges": [{"from": "now+1d/d"}, {"to": "now+1d/d"}]}}}}, "no_available": {"filter": {"bool": {"must_not": [{"match": {"publish_status": "0"}}]}}}, "Data Language": {"terms": {"field": "language", "size": 1000}}, "Access": {"terms": {"field": "accessRights", "size": 1000}}, "Location": {"terms": {"field": "geoLocation.geoLocationPlace", "size": 1000}}, "Temporal": {"terms": {"field": "temporal", "size": 1000}}, "Topic": {"terms": {"field": "subject.value", "size": 1000}}, "Distributor": {"filter": {"bool": {"must": [{"term": {"contributor.@attributes.contributorType": "Distributor"}}]}}, "aggs": {"Distributor": {"terms": {"field": "contributor.contributorName", "size": 1000}}}}, "Data Type": {"filter": {"bool": {"must": [{"term": {"description.descriptionType": "Other"}}]}}, "aggs": {"Data Type": {"terms": {"field": "description.value", "size": 1000}}}}}}}, "sort": [{"_script": {"type": "number", "script": "Float.parseFloat(doc[\"control_number\"].value)", "order": "asc"}}], "from": 0, "size": 20, "_source": {"excludes": ["content"]}}'
```

```
curl -s "http://elasticsearch:9200/tenant1-weko/_search?pretty" -H "Content-type: application/json" -d '{"query": {"bool": {"must": [{"match": {"relation_version_is_last": "true"}}, {"bool": {"must": [{"terms": {"publish_status": ["0", "1"]}}, {"terms": {"path": []}}]}}]}}, "post_filter": {"bool": {"must": [{"terms": {"publish_status": ["0"]}}, {"range": {"publish_date": {"lte": "now/d", "time_zone": "Asia/Tokyo"}}}, {"terms": {"path": []}}, {"bool": {"must": [{"terms": {"publish_status": ["0"]}}, {"match": {"relation_version_is_last": "true"}}]}}]}}, "aggs": {"path": {"terms": {"field": "path", "size": "1"}, "aggs": {"date_range": {"filter": {"match": {"publish_status": "0"}}, "aggs": {"available": {"range": {"field": "publish_date", "ranges": [{"from": "now+1d/d"}, {"to": "now+1d/d"}]}}}}, "no_available": {"filter": {"bool": {"must_not": [{"match": {"publish_status": "0"}}]}}}, "Data Language": {"filter": {"bool": {"must": [{"term": {"publish_status": "0"}}]}}, "aggs": {"Data Language": {"terms": {"field": "language", "size": 1000}}}}, "Access": {"filter": {"bool": {"must": [{"term": {"publish_status": "0"}}]}}, "aggs": {"Access": {"terms": {"field": "accessRights", "size": 1000}}}}, "Location": {"filter": {"bool": {"must": [{"term": {"publish_status": "0"}}]}}, "aggs": {"Location": {"terms": {"field": "geoLocation.geoLocationPlace", "size": 1000}}}}, "Temporal": {"filter": {"bool": {"must": [{"term": {"publish_status": "0"}}]}}, "aggs": {"Temporal": {"terms": {"field": "temporal", "size": 1000}}}}, "Topic": {"filter": {"bool": {"must": [{"term": {"publish_status": "0"}}]}}, "aggs": {"Topic": {"terms": {"field": "subject.value", "size": 1000}}}}, "Distributor": {"filter": {"bool": {"must": [{"term": {"contributor.@attributes.contributorType": "Distributor"}}, {"term": {"publish_status": "0"}}]}}, "aggs": {"Distributor": {"terms": {"field": "contributor.contributorName", "size": 1000}}}}, "Data Type": {"filter": {"bool": {"must": [{"term": {"description.descriptionType": "Other"}}, {"term": {"publish_status": "0"}}]}}, "aggs": {"Data Type": {"terms": {"field": "description.value", "size": 1000}}}}}}}, "sort": [{"_script": {"type": "number", "script": "Float.parseFloat(doc[\"control_number\"].value)", "order": "asc"}}], "from": 0, "size": 20, "_source": {"excludes": ["content"]}}'
```

```
{
  "source": {
    "index": SRC_INDEX,
    "query": {
      "bool": {
        "should": [
          {
            "range": {
              "created_at": {
                "gte": TIMESTAMP # Reindex開始時のタイムスタンプ
              }
            }
          },
          {
            "range": {
              "updated_at": {
                "gte": TIMESTAMP　　# Reindex開始時のタイムスタンプ
              }
            }
          }
        ]
      }
    }
  },
  "dest": {
    "index": DEST_INDEX
  }
}
```