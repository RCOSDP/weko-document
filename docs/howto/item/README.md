# アイテム操作

## 削除アイテムを削除前の状態に戻す

削除アイテムを削除前の状態に戻す手法についてまとめる。
本手法で戻せるのはアイテムのメタデータまでの範囲であり、
アイテムに紐づくコンテンツファイルを戻すことは（バックアップからの復元を除き）本手法の範囲外である。

アイテムを戻す手順は以下である。

1. records_metadataの当該アイテムの削除状態を公開状態に修正する
2. pidstore_pidの当該アイテムに関連するレコードの削除フラグを通常状態に戻す
3. 当該アイテムをelasticsearchへreindexする


### 削除アイテムのPIDを検索する

```
SELECT id,object_uuid,pid_value,pid_type FROM pidstore_pid WHERE object_uuid IN (SELECT object_uuid FROM pidstore_pid WHERE status='D' AND (pid_value='2000002' OR pid_value like '2000002.%'));
```

```
invenio=# SELECT id,object_uuid,pid_value,pid_type FROM pidstore_pid WHERE object_uuid IN (SELECT object_uuid FROM pidstore_pid WHERE status='D' AND (pid_value='2000002' OR pid_value like '2000002.%'));
 id |             object_uuid              |            pid_value             | pid_type 
----+--------------------------------------+----------------------------------+----------
 10 | 0c739e12-d624-4c49-8749-ec0fcdc48155 | 2000002                          | recid
 11 | 0c739e12-d624-4c49-8749-ec0fcdc48155 | 2000002                          | depid
 12 | 0c739e12-d624-4c49-8749-ec0fcdc48155 | parent:2000002                   | parent
 13 | 0c739e12-d624-4c49-8749-ec0fcdc48155 | oai:weko3.example.org:02000002   | oai
 14 | f320964c-8646-400c-b81c-ead87e826964 | 2000002.1                        | recid
 15 | f320964c-8646-400c-b81c-ead87e826964 | 2000002.1                        | depid
 16 | f320964c-8646-400c-b81c-ead87e826964 | oai:weko3.example.org:02000002.1 | oai
 17 | 2609a3f1-d213-453c-80f3-97c6d659b2c1 | 2000002.0                        | recid
 18 | 2609a3f1-d213-453c-80f3-97c6d659b2c1 | 2000002.0                        | depid
 19 | 2609a3f1-d213-453c-80f3-97c6d659b2c1 | oai:weko3.example.org:02000002.0 | oai
(10 rows)
```

### 削除アイテムの公開状態を確認する

```
invenio=# SELECT json->'publish_status' FROM records_metadata WHERE id IN (SELECT object_uuid FROM pidstore_pid WHERE status='D' AND (pid_value='2000002' OR pid_value like '2000002.%'));
 ?column? 
----------
 "-1"
 "-1"
 "-1"
(3 rows)
```

### 削除アイテムの公開状態を公開にする

```
invenio=# UPDATE records_metadata SET json=jsonb_set(json,'{publish_status}','0') WHERE id IN (SELECT object_uuid FROM pidstore_pid WHERE status='D' AND (pid_value='2000002' OR pid_value like '2000002.%'));
UPDATE 3
```

### 削除アイテムのPIDを通常状態に戻す

```
invenio=# UPDATE pidstore_pid SET status='R' WHERE object_uuid IN (SELECT object_uuid FROM pidstore_pid WHERE status='D' AND (pid_value='200
0002' OR pid_value like '2000002.%'));
UPDATE 10
```

### 削除アイテムを検索する

```
curl -XGET 'http://localhost:9200/tenant1-weko-item-v1.0.0/item-v1.0.0/_search_?pretty' -H 'Content-type: application/json' -d '{"query":{"wildcard":{"control_number":"2000002.*"}}}'
```

### 削除アイテムの公開状態を公開にする

```
curl -XPOST 'http://localhost:9200/tenant1-weko-item-v1.0.0/item-v1.0.0/_update_by_query?pretty' -H 'Content-type: application/json' -d '{"query":{"wildcard":{"control_number":"2000002.*"}},"script":{"lang":"painless","source":"ctx._source.publish_status='0'"}}'
```

```
curl -XPOST 'http://localhost:9200/tenant1-weko-item-v1.0.0/item-v1.0.0/_update_by_query?pretty' -H 'Content-type: application/json' -d '{"query":{"term":{"control_number":"2000002"}},"script":{"lang":"painless","source":"ctx._source.publish_status='0'"}}'
```

# アイテム検索

## 日時で検索する

```
curl "http://localhost:9200/tenant1-weko/_search?pretty" -H "Content-type: application/json" -d '{"query":{"range":{"_created":{"lt":"2025-01-11T02:33"}}},"_source":["_id","_created","_updated"]}'
```

```
{
  "took" : 5,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "39878b48-6ef1-4a80-a765-a523566d190b",
        "_score" : 1.0,
        "_source" : {
          "_created" : "2025-01-11T02:22:49.506234+00:00",
          "_updated" : "2025-01-11T02:23:57.229649+00:00"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "ab279ae4-a9c8-447d-b5ba-1b9086a86536",
        "_score" : 1.0,
        "_source" : {
          "_created" : "2025-01-11T02:23:54.577204+00:00",
          "_updated" : "2025-01-11T02:23:56.488937+00:00"
        }
      }
    ]
  }
}
```

## タイムゾーンを指定した日時で検索する


```
$ docker-compose -f docker-compose2.yml exec elasticsearch curl "http://localhost:9200/tenant1-weko/_search?pretty" -H "Content-type: application/json" -d '{"query":{"range":{"_created":{"lt":"2025-10-11T02:23:54","time_zone":"+09:00"}}},"_source":["_id","_created","_updated"]}'
{
  "took" : 8,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 4,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "39878b48-6ef1-4a80-a765-a523566d190b",
        "_score" : 1.0,
        "_source" : {
          "_created" : "2025-01-11T02:22:49.506234+00:00",
          "_updated" : "2025-01-11T02:23:57.229649+00:00"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "4ca215dc-3928-4b9a-8613-0a71955f1b37",
        "_score" : 1.0,
        "_source" : {
          "_created" : "2025-01-11T02:35:02.657664+00:00",
          "_updated" : "2025-01-11T02:36:37.396831+00:00"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "dbef5c39-c822-421d-8cfe-feaf2a67488e",
        "_score" : 1.0,
        "_source" : {
          "_created" : "2025-01-11T02:36:35.390837+00:00",
          "_updated" : "2025-01-11T02:36:37.009785+00:00"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "ab279ae4-a9c8-447d-b5ba-1b9086a86536",
        "_score" : 1.0,
        "_source" : {
          "_created" : "2025-01-11T02:23:54.577204+00:00",
          "_updated" : "2025-01-11T02:23:56.488937+00:00"
        }
      }
    ]
  }
}
```

## 年月で検索する

```
curl "http://localhost:9200/tenant1-weko/_search?pretty" -H "Content-type: application/json" -d '{"query":{"range":{"publish_date":{"gte":"2025-01"}}},"_source":["_id","publish_date"]}'
```

```
{
  "took" : 7,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 4,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "39878b48-6ef1-4a80-a765-a523566d190b",
        "_score" : 1.0,
        "_source" : {
          "publish_date" : "2025-01-11"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "4ca215dc-3928-4b9a-8613-0a71955f1b37",
        "_score" : 1.0,
        "_source" : {
          "publish_date" : "2025-01-11"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "dbef5c39-c822-421d-8cfe-feaf2a67488e",
        "_score" : 1.0,
        "_source" : {
          "publish_date" : "2025-01-11"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "ab279ae4-a9c8-447d-b5ba-1b9086a86536",
        "_score" : 1.0,
        "_source" : {
          "publish_date" : "2025-01-11"
        }
      }
    ]
  }
}
```

## Created and 日付 で検索する

```
curl "http://localhost:9200/tenant1-weko/_search?pretty" -H "Content-type: application/json" -d '{"query":{"nested":{"path":"date","query":{"bool":{"must":[{"term":{"date.dateType":{"value":"Created"}}},{"range":{"date.value":{"gte":"2025"}}}]}}}},"_source":["_id","date","control_number"]}'
```

```
{
  "took" : 8,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 1.1053605,
    "hits" : [
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "4ca215dc-3928-4b9a-8613-0a71955f1b37",
        "_score" : 1.1053605,
        "_source" : {
          "date" : [
            {
              "dateType" : "Created",
              "value" : "2025-02-20"
            }
          ],
          "control_number" : "2000002"
        }
      },
      {
        "_index" : "tenant1-weko-item-v1.0.0",
        "_type" : "item-v1.0.0",
        "_id" : "dbef5c39-c822-421d-8cfe-feaf2a67488e",
        "_score" : 1.1053605,
        "_source" : {
          "date" : [
            {
              "dateType" : "Created",
              "value" : "2025-02-20"
            }
          ],
          "control_number" : "2000002.1"
        }
      }
    ]
  }
}
```