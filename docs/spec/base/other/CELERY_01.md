## celery タスク

- 定期実行するCeleryタスクはinstance.cfg(invenio.cfg)のCELERY_BEAT_SCHEDULE にて定義する。

```python
CELERY_BEAT_SCHEDULE = {
    # Stats
    'stats-process-events': {
        'task': 'invenio_stats.tasks.process_events',
        'schedule': timedelta(minutes=1),
        'args': [('celery-task', 'item-create', 'top-view', 'record-view', 'file-download', 'file-preview', 'search')],
    },
    'stats-aggregate-events': {
        'task': 'invenio_stats.tasks.aggregate_events',
        'schedule': crontab(hour=WEKO_AGGREGATE_EVENT_HOUR, minute=WEKO_AGGREGATE_EVENT_MINUTE),
        'args': [('celery-task-agg', 'file-download-agg', 'file-preview-agg', 'item-create-agg', 'record-view-agg', 'search-agg', 'top-view-agg')],
    },
    # WEKO-indextree-journal-export
    'indextree-journal-export-journal': {
        'task': 'weko_indextree_journal.tasks.export_journal_task',
        'schedule': timedelta(days=1),
        'args': [('p_path')],
    },
    'admin-send-report-emails': {
        'task': 'weko_admin.tasks.check_send_all_reports',
        'schedule': timedelta(days=1, minutes=0, hours=0),
        'args': [],
    },
    'harvest-check-schedules': {
        'task': 'invenio_oaiharvester.tasks.check_schedules_and_run',
        'schedule': crontab(hour=0, minute=0, day_of_week='*'),
        'args': [],
    },
    'send-feedback-mail-schedules': {
        'task': 'weko_admin.tasks.send_feedback_mail',
        'schedule': crontab(day_of_month='1', hour=0, minute=0),
        'args': [],
    },
    'send_storage_alert_mail': {
        'task': 'invenio_files_rest.tasks.check_send_alert_mail',
        'schedule': timedelta(days=1, minutes=0, hours=0),
        'args': [],
    },
    'send_site_access_mail': {
        'task': 'weko_admin.tasks.check_send_site_access_report',
        'schedule': timedelta(days=1, minutes=0, hours=0),
        'args': [],
    },
    'remove_preview_pdf': {
        'task': 'invenio_files_rest.tasks.check_file_storage_time',
        'schedule': timedelta(days=0, minutes=0, hours=1),
        'args': [],
    },
    'remove_author_tmp_file': {
        'task': 'weko_authors.tasks.check_tmp_file_time_for_author',
        'schedule': timedelta(days=0, minutes=0, hours=1),
        'args': [],
    },
    'update_sitemap': {
        'task': 'weko_sitemap.tasks.update_sitemap',
        'schedule': timedelta(days=3, minutes=0, hours=0),
        'args': [],
    },
    'resync': {
        'task': 'invenio_resourcesyncclient.tasks.run_sync_auto',
        'schedule': crontab(hour=0, minute=0),
    },
    # Execute cancel_usage_report_activities daily at midnight
    'cancel_usage_report_activities': {
        'task': 'weko_workflow.tasks.cancel_expired_usage_report_activities',
        'schedule': crontab(minute=0, hour=0),
    },
    'clean_temp_info': {
        'task': 'weko_admin.tasks.clean_temp_info',
        'schedule': timedelta(hours=1),
        'args': [],
    },
    'bulk_post_item_to_researchmap': {
        'task': 'weko_items_ui.tasks.bulk_post_item_to_researchmap',
        'schedule': crontab(hour=0, minute=0),
        'args': [],
    },
}
```

```
docker-compose -f docker-compose2.yml exec --user root web celery -A invenio_app.celery call weko_admin.tasks.send_feedback_mail
4f30e29f-f217-4103-8ddf-e7cd1159b36a
```

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |

## 実装補足（v2.0.2 実装との突き合わせ）

- `CELERY_BEAT_SCHEDULE` の定義は `scripts/instance.cfg`（jinja テンプレート、`environ()` で invenio.cfg を生成）にあり、各タスクは対応モジュールの `tasks.py` に実在する（`invenio_stats.tasks.process_events`/`aggregate_events`、`weko_indextree_journal.tasks.export_journal_task`、`weko_admin.tasks.*`、`invenio_oaiharvester.tasks.check_schedules_and_run`、`invenio_files_rest.tasks.check_send_alert_mail`/`check_file_storage_time`、`weko_authors.tasks.check_tmp_file_time_for_author`、`weko_sitemap.tasks.update_sitemap`、`invenio_resourcesyncclient.tasks.run_sync_auto`、`weko_workflow.tasks.cancel_expired_usage_report_activities`、`weko_items_ui.tasks.bulk_post_item_to_researchmap`）。
- 補足：`weko_logging.tasks.delete_log`（ログ削除）は実装済みだが beat スケジュールではコメントアウトされ**無効**（定期実行されない）。
