## celery タスク

  - 定期実行するCeleryタスクはinstance.cfg(invenio.cfg)のCELERY\_BEAT\_SCHEDULE にて定義する。

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
> 
> 'stats-aggregate-events': {
> 
> 'task': 'invenio\_stats.tasks.aggregate\_events',
> 
> 'schedule': timedelta(days=1),
> 
> 'args': \[('celery-task-agg', 'file-download-agg', 'file-preview-agg', 'item-create-agg', 'record-view-agg', 'search-agg', 'top-view-agg')\],
> 
> },
> 
> \# WEKO-indextree-journal-export
> 
> 'indextree-journal-export-journal': {
> 
> 'task': 'weko\_indextree\_journal.tasks.export\_journal\_task',
> 
> 'schedule': timedelta(days=1),
> 
> 'args': \[('p\_path')\],
> 
> },
> 
> 'admin-send-report-emails': {
> 
> 'task': 'weko\_admin.tasks.check\_send\_all\_reports',
> 
> 'schedule': timedelta(days=1, minutes=0, hours=0),
> 
> 'args': \[\],
> 
> },
> 
> 'harvest-check-schedules': {
> 
> 'task': 'invenio\_oaiharvester.tasks.check\_schedules\_and\_run',
> 
> 'schedule': crontab(hour=0, minute=0, day\_of\_week='\*'),
> 
> 'args': \[\],
> 
> },
> 
> 'send-feedback-mail-schedules': {
> 
> 'task': 'weko\_admin.tasks.send\_feedback\_mail',
> 
> 'schedule': crontab(day\_of\_month='1', hour=0, minute=0),
> 
> 'args': \[\],
> 
> },
> 
> 'send\_storage\_alert\_mail': {
> 
> 'task': 'invenio\_files\_rest.tasks.check\_send\_alert\_mail',
> 
> 'schedule': timedelta(days=1, minutes=0, hours=0),
> 
> 'args': \[\],
> 
> },
> 
> 'send\_site\_access\_mail': {
> 
> 'task': 'weko\_admin.tasks.check\_send\_site\_access\_report',
> 
> 'schedule': timedelta(days=1, minutes=0, hours=0),
> 
> 'args': \[\],
> 
> },
> 
> 'remove\_preview\_pdf': {
> 
> 'task': 'invenio\_files\_rest.tasks.check\_file\_storage\_time',
> 
> 'schedule': timedelta(days=0, minutes=0, hours=1),
> 
> 'args': \[\],
> 
> },
> 
> 'update\_sitemap': {
> 
> 'task': 'weko\_sitemap.tasks.update\_sitemap',
> 
> 'schedule': timedelta(days=3, minutes=0, hours=0),
> 
> 'args': \[\],
> 
> },
> 
> 'resync': {
> 
> 'task': 'invenio\_resourcesyncclient.tasks.run\_sync\_auto',
> 
> 'schedule': crontab(hour=0, minute=0),
> 
> },
> 
> \# Execute cancel\_usage\_report\_activities daily at midnight
> 
> 'cancel\_usage\_report\_activities': {
> 
> 'task': 'weko\_workflow.tasks.cancel\_expired\_usage\_report\_activities',
> 
> 'schedule': crontab(minute=0, hour=0),
> 
> },
> 
> 'clean\_temp\_info': {
> 
> 'task': 'weko\_admin.tasks.clean\_temp\_info',
> 
> 'schedule': timedelta(hours=1),
> 
> 'args': \[\],
> 
> },
> 
> }

docker-compose -f docker-compose2.yml exec --user root web celery -A invenio_app.celery call weko_admin.tasks.send_feedback_mail
4f30e29f-f217-4103-8ddf-e7cd1159b36a

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
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>
