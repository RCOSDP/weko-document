# インデックス操作

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




