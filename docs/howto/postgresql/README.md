

# ERROR:  database "wekotest" is being accessed by other users

```
invenio=# drop database wekotest;
ERROR:  database "wekotest" is being accessed by other users
DETAIL:  There are 10 other sessions using the database.
```

```
invenio=# SELECT                 
    pg_terminate_backend(pg_stat_activity.pid)
FROM
    pg_stat_activity
WHERE
    pg_stat_activity.datname = 'wekotest'               
AND pid <> pg_backend_pid();
 pg_terminate_backend 
----------------------
(0 rows)
```

```
invenio=# drop database wekotest;
DROP DATABASE
invenio=# 
```
