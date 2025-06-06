# PostgreSQLクエリ集

## 2024/9/21時点で最新のアイテムタイプのIDをバージョンを検索する

```
SELECT id,MAX(version_id) FROM item_type_version WHERE updated < '2024/9/21' GROUP BY id ORDER BY id;
```

## 2024/9/9時点で最新のアイテムタイプのプロパティの属性値のオプションを検索する

```
SELECT current_database() as db,updated,id,version_id,jsonb_path_query(render,'$.table_row_map.form[*].items.key') as key,jsonb_path_query(render,'$.table_row_map.form[*].items.isHide') AS isHide, jsonb_path_query(render,'$.table_row_map.form[*].items.isShowList') AS isShowList,jsonb_path_query(render,'$.table_row_map.form[*].items.isNonDisplay') AS isNonDisplay,jsonb_path_query(render,'$.table_row_map.form[*].items.isSpecifyNewline') AS isSpeficyNewline,jsonb_path_query(render,'$.table_row_map.form[*].items.required') AS required FROM item_type_version WHERE id IN (SELECT id FROM item_type_version WHERE updated < '2024/9/9' GROUP BY id ORDER BY id) and version_id IN (SELECT MAX(version_id) FROM item_type_version WHERE updated < '2024/9/9' GROUP BY id ORDER BY id);  
```

```
cat repositories.txt | cut -d' ' -f1 | while read line; do db=$(echo $line | tr .- _); kubectl exec -n weko3pg weko-postgresql-2 -- psql -U invenio ${db} -t -c "SELECT current_database() as db,updated,id,version_id,jsonb_path_query(render,'$.table_row_map.form[*].items.key') as key,jsonb_path_query(render,'$.table_row_map.form[*].items.isHide') AS isHide, jsonb_path_query(render,'$.table_row_map.form[*].items.isShowList') AS isShowList,jsonb_path_query(render,'$.table_row_map.form[*].items.isNonDisplay') AS isNonDisplay,jsonb_path_query(render,'$.table_row_map.form[*].items.isSpecifyNewline') AS isSpeficyNewline,jsonb_path_query(render,'$.table_row_map.form[*].items.required') AS required FROM item_type_version WHERE id IN (SELECT id FROM item_type_version WHERE updated < '2024/9/9' GROUP BY id ORDER BY id) and version_id IN (SELECT MAX(version_id) FROM item_type_version WHERE updated < '2024/9/9' GROUP BY id ORDER BY id);";done > tmp
```

## 2024/9/9時点で最新のアイテムタイプのプロパティのオプション（hidden）を検索する

```
SELECT updated,id,version_id,jsonb_path_query(render,'$.meta_list.keyvalue()')->'key',jsonb_path_query(render,'$.meta_list.**.hidden') as key FROM item_type_version WHERE id IN (SELECT id FROM item_type_version WHERE updated < '2024/9/21' GROUP BY id ORDER BY id) and version_id IN (SELECT MAX(version_id) FROM item_type_version WHERE updated < '2024/9/21' GROUP BY id ORDER BY id);  
```