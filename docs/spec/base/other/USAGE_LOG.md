# 利用統計ログ

## 目的・用途

本機能は、アイテム閲覧数・ファイルダウンロード数・検索回数・アイテム作成数などの利用統計を、invenio-stats のイベント収集・集計により記録する機能である。収集した統計は運用レポート・ランキング・フィードバックメール・サイトライセンスレポート等で利用される。

## 利用方法

Celery のイベント処理タスク（`invenio_stats.tasks.process_events`）および集計タスク（`aggregate_events`）を `CELERY_BEAT_SCHEDULE` で定期実行するよう設定する（下記「機能内容」参照）。

## 利用可能なロール

統計の収集はシステムが自動で行う（利用者操作を起点にイベントを記録）。収集された統計の閲覧は管理画面の各機能（運用レポート等）の権限に従う。

## 機能内容

- invenio-stats によるログ設定手順は、  
  別紙「Precedure_of_implementing_file-download_function_V1.02.xlsx」を参照

- CELERY SCHEDULE 設定  
  <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L70>
  のCELERY_BEAT_SCHEDULE に、以下のように追加する

```
CELERY_BEAT_SCHEDULE = {
  # Stats
  'stats-process-events': {
    'task': 'invenio_stats.tasks.process_events',
    'schedule': timedelta(minutes=1),
    'args': [('celery-task', 'item-create', 'top-view', 'record-view', 'file-download', 'file-preview', 'search')],
  },
```

- 各種ログはelasticsearchに格納されており、インデックスを指定して取得することができる

  - インデックスについては[その他-4: elasticsearch](#elasticsearch)を参照

  - 生データである「events-stats-{ログの種類}」から、統計情報「stats-{ログの種類}」を作成している

- celery-task ログ

  - http://{Elasticsearch:port} /{stats-celery-task のインデックス}/_search?pretty

```
{
  "took" : 6,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-celery-task-000001",
        "_type" : "celery-task-day-aggregation",
        "_id" : "7b2c80be-4058-360f-a247-d228118032d2",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-05-10T00:00:00",
          "unique_id" : "7b2c80be-4058-360f-a247-d228118032d2",
          "count" : 1,
          "unique_count" : 1,
          "volume" : 0.0,
          "task_id" : "21c1fc79-9f16-4f5d-85d6-c556074a5db3",
          "task_name" : "harvest",
          "task_state" : "SUCCESS",
          "start_time" : "2023-05-10T09:36:35",
          "end_time" : "2023-05-10T00:36:37",
          "total_records" : 0,
          "repository_name" : "weko",
          "execution_time" : "-1 day, 15:00:02.734294"
        }
      }
    ]
  }
}
```

- file-download ログ

  - http://{Elasticsearch:port} /{ stats-file-download のインデックス}/_search?pretty

```
{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 32,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-file-download-000001",
        "_type" : "file-download-day-aggregation",
        "_id" : "b72c0fab-9215-3a8d-9ba1-bbae7162ea68",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-05-11T00:00:00",
          "unique_id" : "b72c0fab-9215-3a8d-9ba1-bbae7162ea68",
          "count" : 1,
          "unique_count" : 1,
          "volume" : 42786.0,
          "country" : null,
          "item_id" : "4",
          "item_title" : "テストアイテム壱",
          "file_key" : "2.2.png",
          "bucket_id" : "c6202711-3af2-4ca1-943a-a14584b131a9",
          "file_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
          "root_file_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
          "accessrole" : "open_access",
          "userrole" : "System Administrator",
          "index_list" : "テストインデックス１",
          "is_billing_item" : false,
          "billing_file_price" : "",
          "user_group_names" : "",
          "site_license_name" : "",
          "site_license_flag" : false,
          "cur_user_id" : 1,
          "hostname" : "None",
          "remote_addr" : "192.168.56.1"
        }
      },...
    ]
  }
}
```

- file-preview ログ

  - http://{Elasticsearch:port} /{ stats- file-preview のインデックス}/_search?pretty

```
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-file-preview-000001",
        "_type" : "file-preview-day-aggregation",
        "_id" : "d665fc18-c050-3868-ae6f-45daaa06495d",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-07-15T00:00:00",
          "unique_id" : "d665fc18-c050-3868-ae6f-45daaa06495d",
          "count" : 1,
          "unique_count" : 1,
          "volume" : 42786.0,
          "country" : null,
          "item_id" : "4",
          "item_title" : "テストアイテム壱",
          "file_key" : "2.2.png",
          "bucket_id" : "c88e1450-e3d2-4f33-8970-176f9d659410",
          "file_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
          "root_file_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
          "accessrole" : "open_login",
          "userrole" : "System Administrator",
          "index_list" : "テストインデックス１",
          "is_billing_item" : false,
          "billing_file_price" : "",
          "user_group_names" : "テストグループ",
          "site_license_name" : "",
          "site_license_flag" : false,
          "cur_user_id" : 1,
          "hostname" : "None",
          "remote_addr" : "192.168.56.1"
        }
      }
    ]
  }
}
```

- item-create ログ

  - http://{Elasticsearch:port} /{ stats-item-create のインデックス}/_search?pretty

```
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 42,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-item-create-000001",
        "_type" : "item-create-day-aggregation",
        "_id" : "item_create_11",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-06-09T00:00:00",
          "unique_id" : "item_create_11",
          "count" : 1,
          "unique_count" : 1,
          "country" : null,
          "hostname" : "None",
          "cur_user_id" : 1,
          "remote_addr" : "192.168.56.1",
          "pid_type" : "recid",
          "pid_value" : "11",
          "record_name" : ""
        }
      },...
    ]
  }
}
```

- record-view ログ

  - http://{Elasticsearch:port} /{ stats-record-view のインデックス}/_search?pretty

```
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 185,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-record-view-000001",
        "_type" : "record-view-day-aggregation",
        "_id" : "8eefc281-f477-3639-9475-1d2b2621d33f",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-06-09T00:00:00",
          "unique_id" : "8eefc281-f477-3639-9475-1d2b2621d33f",
          "count" : 2,
          "unique_count" : 1,
          "country" : null,
          "hostname" : "None",
          "remote_addr" : "192.168.56.1",
          "record_id" : "9b4bb507-3a6a-4eeb-8f82-300c2b0a6302",
          "record_name" : "テストアイテム03",
          "record_index_names" : "テストインデックス１",
          "pid_type" : "recid",
          "pid_value" : "3",
          "cur_user_id" : "1",
          "site_license_name" : "",
          "site_license_flag" : false
        }
      },...
    ]
  }
}
```

- search ログ

  - http://{Elasticsearch:port} /{ stats-search のインデックス}/_search?pretty

```
{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 11,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-search-000001",
        "_type" : "search-day-aggregation",
        "_id" : "1ef1be2d-9261-3182-91b6-a878ac568e83",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-07-07T00:00:00",
          "unique_id" : "1ef1be2d-9261-3182-91b6-a878ac568e83",
          "count" : 1,
          "unique_count" : 1,
          "country" : null,
          "referrer" : "https://192.168.56.103/",
          "search_key" : "0718",
          "search_type" : "0",
          "site_license_name" : "",
          "site_license_flag" : false
        }
      },...
    ]
  }
}
```

- top-view ログ

  - http://{Elasticsearch:port} /{ stats-top-view のインデックス}/_search?pretty

```
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 562,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tenant1-stats-top-view-000001",
        "_type" : "top-view-day-aggregation",
        "_id" : "3569afb4-53bd-3ef6-823d-e864be85faee",
        "_score" : 1.0,
        "_source" : {
          "timestamp" : "2023-05-09T00:00:00",
          "unique_id" : "3569afb4-53bd-3ef6-823d-e864be85faee",
          "count" : 10,
          "unique_count" : 1,
          "country" : null,
          "hostname" : "None",
          "remote_addr" : "192.168.56.1",
          "site_license_name" : "",
          "site_license_flag" : false
        }
      },...
    ]
  }
}
```

### アイテム作成数

- アイテム個別登録時のアイテム作成イベントを記録
- 一括登録時のアイテム作成イベントを記録
- ハーベスト時のアイテム作成イベントを記録

## 関連モジュール

- invenio-oaiharvester
- invenio-stats
- weko-search-ui
- weko-workflow

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2024/07/1 | 7733de131da9ad59ab591b2df1c70ddefcfcad98 | v1.0.7対応 |

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足：利用統計ログは `invenio_stats.tasks.process_events`（生イベント処理）と `aggregate_events`（集計）で処理される。イベント種別は `invenio_stats.contrib.registrations` に登録（celery-task / file-download / file-preview / item-create / record-view / search / top-view）。インデックス名は `SEARCH_INDEX_PREFIX` に依存。関連モジュール：invenio-stats / weko-search-ui / weko-workflow / invenio-oaiharvester。
