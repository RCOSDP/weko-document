# メンテナンス手法

## インデックスを削除する

インデックスを削除する場合、アイテムの所属を外していく必要がある。本稿では手動でインデックスの削除を行う手法をまとめる。

### インデックスに所属していないアイテムを探す

インデックスに所属していないアイテムは削除されるが、ごみデータとして残っている可能性を考慮する。
以下クエリでインデックスに所属していないアイテムの一覧を取得する。

```
SELECT id,json->'path' FROM records_metadata WHERE jsonb_array_length((json->'path')::jsonb)=0;
```

### インデックスを削除する

1733503900136 の子インデックス一覧を取得する。 

```
with recursive child (depth, id, parent,index_name) as (
		select 0, index.id, index.parent,index.index_name from index where index.id = '1733503900136'
	union all
		select
			child.depth + 1,
			index.id,
			index.parent,
            index.index_name
		from index, child
		where index.parent = child.id)
select depth, id,index_name from child order by depth;
```

```
 depth |      id       | index_name 
-------+---------------+------------
     0 | 1733503900136 | LV1
     1 | 1733503930431 | LV2
     2 | 1733503950790 | LV3
(3 rows)
```

1733503900136 とその子インデックスを削除する。

```
DELETE FROM index WHERE id IN (
with recursive child (depth, id, parent,index_name) as (
		select 0, index.id, index.parent,index.index_name from index where index.id = '1733503900136'
	union all
		select
			child.depth + 1,
			index.id,
			index.parent,
            index.index_name
		from index, child
		where index.parent = child.id)
select id from child order by depth);
```

### アイテムのインデックス情報を削除する(PostgreSQL)

#### アイテムのインデックス情報を削除する

```
UPDATE records_metadata SET json=jsonb_set(json,'{path}',(json->'path')::jsonb - '1733503900136')::jsonb WHERE json->'path' ? '1733503900136';
```

```
UPDATE records_metadata SET json=jsonb_set(json,'{path}',(json->'path')::jsonb - '1733503930431')::jsonb WHERE json->'path' ? '1733503930431';
```

```
UPDATE records_metadata SET json=jsonb_set(json,'{path}',(json->'path')::jsonb - '1733503950790')::jsonb WHERE json->'path' ? '1733503950790';
```

#### アイテムのOAI-SET情報を削除する

```
UPDATE records_metadata SET json=jsonb_set(json,'{_oai,sets}',(json->'_oai'->'sets')::jsonb - '1733503900136')::jsonb WHERE json->'_oai'->'sets' ? '1733503900136';
```

```
UPDATE records_metadata SET json=jsonb_set(json,'{_oai,sets}',(json->'_oai'->'sets')::jsonb - '1733503930431')::jsonb WHERE json->'_oai'->'sets' ? '1733503930431';
```

```
UPDATE records_metadata SET json=jsonb_set(json,'{_oai,sets}',(json->'_oai'->'sets')::jsonb - '1733503950790')::jsonb WHERE json->'_oai'->'sets' ? '1733503950790';
```

#### インデックスに紐づくOAI-SET情報を削除する

```
DELETE FROM oaiserver_set WHERE id='1733503900136';
```

```
DELETE FROM oaiserver_set WHERE id='1733503930431';
```

```
DELETE FROM oaiserver_set WHERE id='1733503950790';
```

### アイテムの所属情報を削除する(Elasticsearch)


```
curl http://localhost:9200/tenant1-weko/_update_by_query?pretty -H 'Content-type: application/json' -d '{"query":{"terms":{"path":["1733503900136"]}},"script":{"lang":"painless","source":"if(ctx._source.path!=null){ctx._source.path.removeIf(item -> item.toString().contains(params.pattern));}if(ctx._source._oai!=null){if(ctx._source._oai.sets!=null){ctx._source._oai.sets.removeIf(item -> item.toString().contains(params.pattern));}}if(ctx._source._item_metadata!=null){if(ctx._source._item_metadata.path!=null){ctx._source._item_metadata.path.removeIf(item -> item.toString().contains(params.pattern));}}if(ctx._source._item_metadata!=null){if(ctx._source._item_metadata._oai!=null){if(ctx._source._item_metadata._oai.sets!=null){ctx._source._item_metadata._oai.sets.removeIf(item -> item.toString().contains(params.pattern));}}}","params":{"pattern":"1733503900136"}}}'
```


```
curl http://localhost:9200/tenant1-weko/_update_by_query?pretty -H 'Content-type: application/json' -d '{"query":{"terms":{"path":["1733503930431"]}},"script":{"lang":"painless","source":"if(ctx._source.path!=null){ctx._source.path.removeIf(item -> item.toString().contains(params.pattern));}if(ctx._source._oai!=null){if(ctx._source._oai.sets!=null){ctx._source._oai.sets.removeIf(item -> item.toString().contains(params.pattern));}}if(ctx._source._item_metadata!=null){if(ctx._source._item_metadata.path!=null){ctx._source._item_metadata.path.removeIf(item -> item.toString().contains(params.pattern));}}if(ctx._source._item_metadata!=null){if(ctx._source._item_metadata._oai!=null){if(ctx._source._item_metadata._oai.sets!=null){ctx._source._item_metadata._oai.sets.removeIf(item -> item.toString().contains(params.pattern));}}}","params":{"pattern":"1733503930431"}}}'
```


```
curl http://localhost:9200/tenant1-weko/_update_by_query?pretty -H 'Content-type: application/json' -d '{"query":{"terms":{"path":["1733503950790"]}},"script":{"lang":"painless","source":"if(ctx._source.path!=null){ctx._source.path.removeIf(item -> item.toString().contains(params.pattern));}if(ctx._source._oai!=null){if(ctx._source._oai.sets!=null){ctx._source._oai.sets.removeIf(item -> item.toString().contains(params.pattern));}}if(ctx._source._item_metadata!=null){if(ctx._source._item_metadata.path!=null){ctx._source._item_metadata.path.removeIf(item -> item.toString().contains(params.pattern));}}if(ctx._source._item_metadata!=null){if(ctx._source._item_metadata._oai!=null){if(ctx._source._item_metadata._oai.sets!=null){ctx._source._item_metadata._oai.sets.removeIf(item -> item.toString().contains(params.pattern));}}}","params":{"pattern":"1733503950790"}}}'
```

```
curl -XDELETE 'http://localhost:9200/tenant1-weko-item-v1.0.0/item-v1.0.0/oaiset-1733503900136:1733503930431:1733503950790'
```

```
curl -XDELETE 'http://localhost:9200/tenant1-weko-item-v1.0.0/item-v1.0.0/oaiset-1733503900136:1733503930431'
```

```
curl -XDELETE 'http://localhost:9200/tenant1-weko-item-v1.0.0/item-v1.0.0/oaiset-1733503900136'
```

### インデックスのキャッシュを削除する

```
redis-cli -n 0
```

```
del index_tree_view_<FQDN>_ja
del index_tree_view_<FQDN>_en
del cache::index_tree_jsonja
del cache::index_tree_jsonen
```

### インデックスに所属していないアイテムを探す

```
SELECT id,json->'path' FROM records_metadata WHERE jsonb_array_length((json->'path')::jsonb)=0;
```


## 削除アイテムを戻す


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

