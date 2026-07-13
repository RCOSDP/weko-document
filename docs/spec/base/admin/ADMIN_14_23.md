# CRIS連携

## 目的・用途

researchmapからの流用入力およびメタデータ登録のための設定を行う。

- researchmap連携のためのAPIキーの設定
- researchmap連携時のマージモードの設定

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

## 利用方法

[トップページ>利用者の方へ>各種資料>申請書類](https://researchmap.jp/public/other-document/application)からresearchmap.V2利用申請書【API】申請の申請し、APIキーを取得する。

試験時は、トライアルサイト用のAPIキーを用いる。

[トップページ>利用者の方へ>機関の方向け>トライアルサイトご利用案内](https://researchmap.jp/public/about/rmap2/function/v2_trial)からトライアルサイト用のAPI申請を行う。

トライアルサイトはIPアドレスによる接続制限がある。

### 連携条件

連携の必須項目は以下の通りである。

- タイトル
- タイトルの言語
- researchmap情報を登録した作成者
- 日付、Issued
- 資源タイプ

### APIキーの設定

取得したAPIキーを読み込み、保存する。

### マージモードの設定

デフォルトでは、類似データマージ（類似データ優先）が選択されている。

マージモードは以下から選択可能である。

|マージモード|説明|
|---|---|
|類似データマージ（類似データ優先）|追加・更新を行おうとしている会員の業績リスト中に類似ドキュメントがあった場合、類似ドキュメントを優先させ、入力データ（または、入力データを指定ドキュメントとマージしたもの）をマージする。|
|類似データマージ（入力データ優先）|追加・更新を行おうとしている会員の業績リスト中に類似ドキュメントがあった場合、入力データ（または、入力データを指定ドキュメントとマージしたもの）を優先させ、類似ドキュメントをマージする。|
|追加（類似データがあればエラー）|指定ドキュメントがない場合、新規登録。追加・更新を行おうとしている会員の業績リスト中に類似ドキュメントがあればエラーとなる。|
|追加（入力データ強制）|類似ドキュメントがあった場合でも、別業績として扱い強制的に新規登録を行う。ただし、類似ドキュメントが機関以外（本人相当）によって登録／更新されている場合は、追加することができない。|

### スケジュール処理

researchmapへの連携はCelery beatによるスケジュール処理により実行される。
デフォルトでは毎日0時0分に実行される。

```
CELERY_BEAT_SCHEDULE = {
~snip~
    'bulk_post_item_to_researchmap': {
        'task': 'weko_items_ui.tasks.bulk_post_item_to_researchmap',
        # 'schedule': crontab(minute='*/1'),
        'schedule': crontab(hour=0, minute=0),
        'args': [],
    },
~snip~
}
```

手動で実行する場合は以下コマンドでスケジュール処理を手動実行することができる。

```
celery -A invenio_app.celery call weko_items_ui.tasks.bulk_post_item_to_researchmap
```

## 設定値

|設定値|説明|デフォルト値|
|---|---|---|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_BASE_URL||"https://api-trial.researchmap.jp"|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_HOST||"api-trial.researchmap.jp:443"|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_RETRY_MAX||5|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_MERGE_MODE_DEFAULT||'similar_merge_similar_data'|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_MAPPINGS||[{ 'type' : 'lang' , "rm_name" : 'paper_title', "jpcoar_name" : 'dc:title' , "weko_name" :"title"},{ 'type' : 'lang' , "rm_name" : 'book_title', "jpcoar_name" : 'dc:title' , "weko_name" :"title"},{ 'type' : 'lang' , "rm_name" : 'presentation_title', "jpcoar_name" : 'dc:title' , "weko_name" :"title"},{ 'type' : 'lang' , "rm_name" : 'work_title', "jpcoar_name" : 'dc:title' , "weko_name" :"title"},{ 'type' : 'lang' , "rm_name" : 'other_title', "jpcoar_name" : 'dc:title' , "weko_name" :"title"},{'type' : 'lang' , "rm_name" : 'description', "jpcoar_name" : 'datacite:description' , "weko_name" :"description"},{'type' : 'lang' , "rm_name" : 'publisher',   "jpcoar_name" : 'dc:publisher' , "weko_name" :"publisher"},{'type' : 'lang' , "rm_name" : 'publication_name',   "jpcoar_name" : 'jpcoar:sourceTitle' , "weko_name" :"sourceTitle"},{'type' : 'lang' , "rm_name" : 'event',   "jpcoar_name" : 'jpcoar:conference' , "weko_name" :"conference" , "child_node" : "conferenceName"},{'type' : 'lang' , "rm_name" : 'promoter',   "jpcoar_name" : 'jpcoar:conference' , "weko_name" :"conference", "child_node" : "conferenceSponsor"},{'type' : 'lang' , "rm_name" : 'location',   "jpcoar_name" : 'jpcoar:conference' , "weko_name" :"conference", "child_node" : "conferencePlace"},{'type' : 'simple' , "rm_name" : 'address_country',   "jpcoar_name" : 'jpcoar:conference' , "weko_name" :"conference", "child_node" : "conferenceCountry"},{'type' : 'authors'    ,  "rm_name" : 'authors'     , "jpcoar_name" : 'jpcoar:creator'  ,"weko_name": 'creator'},{'type' : 'authors'    ,  "rm_name" : 'creators'     , "jpcoar_name" : 'jpcoar:creator'  ,"weko_name": 'creator'},{'type' : 'authors'    ,  "rm_name" : 'originators'     , "jpcoar_name" : 'jpcoar:creator'  ,"weko_name": 'creator'},{'type' : 'authors'    ,  "rm_name" : 'presenters'     , "jpcoar_name" : 'jpcoar:creator'  ,"weko_name": 'creator'},{'type' : 'identifiers',  "rm_name" : "identifiers" , "jpcoar_name" : 'jpcoar:relation' ,"weko_name": 'relation'},{'type' : 'simple_value', "rm_name" : 'publication_date',  "jpcoar_name" :  'datacite:date' , "weko_name" : "date"},{'type' : 'simple' ,"rm_name" : 'total_page',   "jpcoar_name" : 'jpcoar:numPages', "weko_name" : "numPages"},{'type' : 'simple', "rm_name" : 'volume', "jpcoar_name" :  'jpcoar:volume' , "weko_name" : "volume"},{'type' : 'simple', "rm_name" : 'number', "jpcoar_name" :  'jpcoar:issue' , "weko_name" : "issue"},{'type' : 'simple', "rm_name" : 'starting_page', "jpcoar_name" : 'jpcoar:pageStart' , "weko_name" : "pageStart"},{'type' : 'simple', "rm_name" : 'ending_page', "jpcoar_name" :   'jpcoar:pageEnd' ,   "weko_name" : "pageEnd"},{'type' : 'simple', "rm_name" : 'languages', "jpcoar_name" :  'dc:language' , "weko_name" : "language"},{'type' :  'type', "rm_name" : 'published_paper_type'     , "jpcoar_name" :  'dc:type'     , "weko_name" : "type" ,'achievement_type' : 'published_papers'},{'type' :  'type', "rm_name" : 'misc_type'     , "jpcoar_name" :  'dc:type'     , "weko_name" : "type" , 'achievement_type' : 'misc'},{'type' :  'type', "rm_name" : 'book_type'     , "jpcoar_name" :  'dc:type'     , "weko_name" : "type" , 'achievement_type' : 'books_etc'},{'type' :  'type', "rm_name" : 'presentation_type'     , "jpcoar_name" :  'dc:type'     , "weko_name" : "type",'achievement_type' : 'presentations'},{'type' :  'type', "rm_name" : 'work_type'     , "jpcoar_name" :  'dc:type'     , "weko_name" : "type", 'achievement_type' : 'works'},{'type' :  'type', "rm_name" : 'dataset_type'     , "jpcoar_name" :  'dc:type'     , "weko_name" : "type" ,'achievement_type' : 'others'}]|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_TYPE_MAPPINGS||[{'achievement_type' : 'published_papers','detail_type_name':'','JPCOAR_resource_type':'article'},{'achievement_type' : 'published_papers','detail_type_name':'scientific_journal','JPCOAR_resource_type':'journal article'},{'achievement_type' : 'published_papers','detail_type_name':'international_conference_proceedings','JPCOAR_resource_type':'conference paper'},{'achievement_type' : 'published_papers','detail_type_name':'research_institution','JPCOAR_resource_type':'departmental bulletin paper'},{'achievement_type' : 'published_papers','detail_type_name':'symposium','JPCOAR_resource_type':'conference paper'},{'achievement_type' : 'published_papers','detail_type_name':'research_society','JPCOAR_resource_type':'article'},{'achievement_type' : 'published_papers','detail_type_name':'in_book','JPCOAR_resource_type':'article'},{'achievement_type' : 'published_papers','detail_type_name':'master_thesis','JPCOAR_resource_type':'master thesis'},{'achievement_type' : 'published_papers','detail_type_name':'others','JPCOAR_resource_type':'article'},{'achievement_type' : 'published_papers','detail_type_name':'doctoral_thesis','JPCOAR_resource_type':'doctoral thesis'},{'achievement_type' : 'misc','detail_type_name':'','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'report_scientific_journal','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'report_research_institution','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'summary_international_conference','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'summary_national_conference','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'technical_report','JPCOAR_resource_type':'technical report'},{'achievement_type' : 'misc','detail_type_name':'introduction_scientific_journal','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'introduction_international_proceedings','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'introduction_research_institution','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'introduction_commerce_magazine','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'introduction_other','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'lecture_materials','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'book_review','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'meeting_report','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'misc','detail_type_name':'others','JPCOAR_resource_type':'learning object'},{'achievement_type' : 'books_etc','detail_type_name':'','JPCOAR_resource_type':'book'},{'achievement_type' : 'books_etc','detail_type_name':'scholarly_book','JPCOAR_resource_type':'book'},{'achievement_type' : 'books_etc','detail_type_name':'dictionary_or_encycropedia','JPCOAR_resource_type':'book'},{'achievement_type' : 'books_etc','detail_type_name':'textbook','JPCOAR_resource_type':'book'},{'achievement_type' : 'books_etc','detail_type_name':'report','JPCOAR_resource_type':'report'},{'achievement_type' : 'books_etc','detail_type_name':'general_book','JPCOAR_resource_type':'book'},{'achievement_type' : 'books_etc','detail_type_name':'musical_material','JPCOAR_resource_type':'musical notation'},{'achievement_type' : 'books_etc','detail_type_name':'film_or_video','JPCOAR_resource_type':'video'},{'achievement_type' : 'books_etc','detail_type_name':'image_material','JPCOAR_resource_type':'image'},{'achievement_type' : 'books_etc','detail_type_name':'phonetic_material','JPCOAR_resource_type':'sound'},{'achievement_type' : 'books_etc','detail_type_name':'map','JPCOAR_resource_type':'map'},{'achievement_type' : 'books_etc','detail_type_name':'others','JPCOAR_resource_type':'book'},{'achievement_type' : 'presentations','detail_type_name':'','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'oral_presentation','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'invited_oral_presentation','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'keynote_oral_presentation','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'poster_presentation','JPCOAR_resource_type':'conference poster'},{'achievement_type' : 'presentations','detail_type_name':'public_symposium','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'nominated_symposium','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'public_discourse','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'media_report','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'presentations','detail_type_name':'others','JPCOAR_resource_type':'conference presentation'},{'achievement_type' : 'works','detail_type_name':'','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'works','detail_type_name':'artistic_activity','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'works','detail_type_name':'architectural_works','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'works','detail_type_name':'software','JPCOAR_resource_type':'software'},{'achievement_type' : 'works','detail_type_name':'database','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'works','detail_type_name':'web_service','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'works','detail_type_name':'educational_materials','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'works','detail_type_name':'others','JPCOAR_resource_type':'interactive resource'},{'achievement_type' : 'others','detail_type_name':'','JPCOAR_resource_type':'other'},{'achievement_type' : 'others','detail_type_name':'preprint','JPCOAR_resource_type':'other'},{'achievement_type' : 'others','detail_type_name':'published','JPCOAR_resource_type':'other'},{'achievement_type' : 'others','detail_type_name':'experimental','JPCOAR_resource_type':'other'},{'achievement_type' : 'others','detail_type_name':'summary','JPCOAR_resource_type':'other'},{'achievement_type' : 'others','detail_type_name':'others','JPCOAR_resource_type':'other'}]|
|LINKAGE_MQ_EXCHANGE||Exchange('cris_researchmap_linkage', type='direct')|
|LINKAGE_MQ_QUEUE||Queue("cris_researchmap_linkage", exchange=LINKAGE_MQ_EXCHANGE, routing_key="cris_researchmap_linkage",queue_arguments={"x-queue-type":"quorum"})|

## 関連モジュール

- weko-items-ui

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2026/01/24 | ccd8e5ad8b88f4d102fe543ab1e60f9833af6659 | 初版作成 |
