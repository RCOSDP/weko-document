# 削除レコードの復帰方法

削除レコードの各種識別子のステータスを確認する。

WEKO ID : 1 の場合。

```
SELECT id,pid_type,pid_value,status,object_uuid FROM pidstore_pid WHERE object_uuid IN (SELECT
 object_uuid FROM pidstore_pid WHERE pid_value = 'parent:1' or pid_value like '1.%');
```

削除ステータスを元に戻す。

```
UPDATE pidstore_pid SET status='R' WHERE object_uuid IN (SELECT object_uuid FROM pidstore_pid
WHERE pid_value = 'parent:96584' OR pid_value LIKE '96584.%');
```

以上。