# 利用統計ログ

## 目的・用途

## 利用方法

## 利用可能なロール

## 機能内容


  - invenio-stats によるログ設定手順は、  
    別紙「Precedure\_of\_implementing\_file-download\_function\_V1.02.xlsx」を参照

  - CELERY SCHEDULE 設定  
    [https://github.com/RCOSDP/weko/blob/develop/scripts/instance.cfghttps://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg\#L70](https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L70)  
    のCELERY\_BEAT\_SCHEDULE に、以下のように追加する

> CELERY\_BEAT\_SCHEDULE = {
> 
> \# Stats
> 
> 'stats-process-events': {
> 
> 'task': 'invenio\_stats.tasks.process\_events',
> 
> 'schedule': timedelta(minutes=1),
> 
> 'args': \[('celery-task', 'item-create', 'top-view', 'record-view', 'file-download', 'file-preview', 'search')\],
> 
> },

  - 各種ログはelasticsearchに格納されており、インデックスを指定して取得することができる
    
      - インデックスについては[その他-4: elasticsearch](#elasticsearch)を参照
    
      - 生データである「events-stats-{ログの種類}」から、統計情報「stats-{ログの種類}」を作成している

  - celery-task ログ
    
      - http://{Elasticsearch:port} /{stats-celery-task のインデックス}/\_search?pretty

> {
> 
> "took" : 6,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 1,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-celery-task-000001",
> 
> "\_type" : "celery-task-day-aggregation",
> 
> "\_id" : "7b2c80be-4058-360f-a247-d228118032d2",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-05-10T00:00:00",
> 
> "unique\_id" : "7b2c80be-4058-360f-a247-d228118032d2",
> 
> "count" : 1,
> 
> "unique\_count" : 1,
> 
> "volume" : 0.0,
> 
> "task\_id" : "21c1fc79-9f16-4f5d-85d6-c556074a5db3",
> 
> "task\_name" : "harvest",
> 
> "task\_state" : "SUCCESS",
> 
> "start\_time" : "2023-05-10T09:36:35",
> 
> "end\_time" : "2023-05-10T00:36:37",
> 
> "total\_records" : 0,
> 
> "repository\_name" : "weko",
> 
> "execution\_time" : "-1 day, 15:00:02.734294"
> 
> }
> 
> }
> 
> \]
> 
> }
> 
> }

  - file-download ログ
    
      - http://{Elasticsearch:port} /{ stats-file-download のインデックス}/\_search?pretty

> {
> 
> "took" : 2,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 32,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-file-download-000001",
> 
> "\_type" : "file-download-day-aggregation",
> 
> "\_id" : "b72c0fab-9215-3a8d-9ba1-bbae7162ea68",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-05-11T00:00:00",
> 
> "unique\_id" : "b72c0fab-9215-3a8d-9ba1-bbae7162ea68",
> 
> "count" : 1,
> 
> "unique\_count" : 1,
> 
> "volume" : 42786.0,
> 
> "country" : null,
> 
> "item\_id" : "4",
> 
> "item\_title" : "テストアイテム壱",
> 
> "file\_key" : "2.2.png",
> 
> "bucket\_id" : "c6202711-3af2-4ca1-943a-a14584b131a9",
> 
> "file\_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
> 
> "root\_file\_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
> 
> "accessrole" : "open\_access",
> 
> "userrole" : "System Administrator",
> 
> "index\_list" : "テストインデックス１",
> 
> "is\_billing\_item" : false,
> 
> "billing\_file\_price" : "",
> 
> "user\_group\_names" : "",
> 
> "site\_license\_name" : "",
> 
> "site\_license\_flag" : false,
> 
> "cur\_user\_id" : 1,
> 
> "hostname" : "None",
> 
> "remote\_addr" : "192.168.56.1"
> 
> }
> 
> },...
> 
> \]
> 
> }
> 
> }

  - file-preview ログ
    
      - http://{Elasticsearch:port} /{ stats- file-preview のインデックス}/\_search?pretty

> {
> 
> "took" : 1,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 1,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-file-preview-000001",
> 
> "\_type" : "file-preview-day-aggregation",
> 
> "\_id" : "d665fc18-c050-3868-ae6f-45daaa06495d",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-07-15T00:00:00",
> 
> "unique\_id" : "d665fc18-c050-3868-ae6f-45daaa06495d",
> 
> "count" : 1,
> 
> "unique\_count" : 1,
> 
> "volume" : 42786.0,
> 
> "country" : null,
> 
> "item\_id" : "4",
> 
> "item\_title" : "テストアイテム壱",
> 
> "file\_key" : "2.2.png",
> 
> "bucket\_id" : "c88e1450-e3d2-4f33-8970-176f9d659410",
> 
> "file\_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
> 
> "root\_file\_id" : "fc178212-279a-49cd-ba8e-2ccbe8bc1a33",
> 
> "accessrole" : "open\_login",
> 
> "userrole" : "System Administrator",
> 
> "index\_list" : "テストインデックス１",
> 
> "is\_billing\_item" : false,
> 
> "billing\_file\_price" : "",
> 
> "user\_group\_names" : "テストグループ",
> 
> "site\_license\_name" : "",
> 
> "site\_license\_flag" : false,
> 
> "cur\_user\_id" : 1,
> 
> "hostname" : "None",
> 
> "remote\_addr" : "192.168.56.1"
> 
> }
> 
> }
> 
> \]
> 
> }
> 
> }

  - item-create ログ
    
      - http://{Elasticsearch:port} /{ stats-item-create のインデックス}/\_search?pretty

> {
> 
> "took" : 3,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 42,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-item-create-000001",
> 
> "\_type" : "item-create-day-aggregation",
> 
> "\_id" : "item\_create\_11",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-06-09T00:00:00",
> 
> "unique\_id" : "item\_create\_11",
> 
> "count" : 1,
> 
> "unique\_count" : 1,
> 
> "country" : null,
> 
> "hostname" : "None",
> 
> "cur\_user\_id" : 1,
> 
> "remote\_addr" : "192.168.56.1",
> 
> "pid\_type" : "recid",
> 
> "pid\_value" : "11",
> 
> "record\_name" : ""
> 
> }
> 
> },...
> 
> \]
> 
> }
> 
> }

  - record-view ログ
    
      - http://{Elasticsearch:port} /{ stats-record-view のインデックス}/\_search?pretty

> {
> 
> "took" : 3,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 185,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-record-view-000001",
> 
> "\_type" : "record-view-day-aggregation",
> 
> "\_id" : "8eefc281-f477-3639-9475-1d2b2621d33f",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-06-09T00:00:00",
> 
> "unique\_id" : "8eefc281-f477-3639-9475-1d2b2621d33f",
> 
> "count" : 2,
> 
> "unique\_count" : 1,
> 
> "country" : null,
> 
> "hostname" : "None",
> 
> "remote\_addr" : "192.168.56.1",
> 
> "record\_id" : "9b4bb507-3a6a-4eeb-8f82-300c2b0a6302",
> 
> "record\_name" : "テストアイテム03",
> 
> "record\_index\_names" : "テストインデックス１",
> 
> "pid\_type" : "recid",
> 
> "pid\_value" : "3",
> 
> "cur\_user\_id" : "1",
> 
> "site\_license\_name" : "",
> 
> "site\_license\_flag" : false
> 
> }
> 
> },...
> 
> \]
> 
> }
> 
> }

  - search ログ
    
      - http://{Elasticsearch:port} /{ stats-search のインデックス}/\_search?pretty

> {
> 
> "took" : 2,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 11,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-search-000001",
> 
> "\_type" : "search-day-aggregation",
> 
> "\_id" : "1ef1be2d-9261-3182-91b6-a878ac568e83",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-07-07T00:00:00",
> 
> "unique\_id" : "1ef1be2d-9261-3182-91b6-a878ac568e83",
> 
> "count" : 1,
> 
> "unique\_count" : 1,
> 
> "country" : null,
> 
> "referrer" : "https://192.168.56.103/",
> 
> "search\_key" : "0718",
> 
> "search\_type" : "0",
> 
> "site\_license\_name" : "",
> 
> "site\_license\_flag" : false
> 
> }
> 
> },...
> 
> \]
> 
> }
> 
> }

  - top-view ログ
    
      - http://{Elasticsearch:port} /{ stats-top-view のインデックス}/\_search?pretty

> {
> 
> "took" : 1,
> 
> "timed\_out" : false,
> 
> "\_shards" : {
> 
> "total" : 5,
> 
> "successful" : 5,
> 
> "skipped" : 0,
> 
> "failed" : 0
> 
> },
> 
> "hits" : {
> 
> "total" : 562,
> 
> "max\_score" : 1.0,
> 
> "hits" : \[
> 
> {
> 
> "\_index" : "tenant1-stats-top-view-000001",
> 
> "\_type" : "top-view-day-aggregation",
> 
> "\_id" : "3569afb4-53bd-3ef6-823d-e864be85faee",
> 
> "\_score" : 1.0,
> 
> "\_source" : {
> 
> "timestamp" : "2023-05-09T00:00:00",
> 
> "unique\_id" : "3569afb4-53bd-3ef6-823d-e864be85faee",
> 
> "count" : 10,
> 
> "unique\_count" : 1,
> 
> "country" : null,
> 
> "hostname" : "None",
> 
> "remote\_addr" : "192.168.56.1",
> 
> "site\_license\_name" : "",
> 
> "site\_license\_flag" : false
> 
> }
> 
> },...
> 
> \]
> 
> }
> 
> }


### アイテム作成数

- アイテム個別登録時のアイテム作成イベントを記録
- 一括登録時のアイテム作成イベントを記録
- ハーベスト時のアイテム作成イベントを記録


## 関連モジュール

- invenio-oaiharvester
- invenio-stats
- weko-search-ui
- weko-workflow


  - > 更新履歴

<table>
<thead>
<tr class="header">
<th>日付</th>
<th>GitHubコミットID</th>
<th>更新内容</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>