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