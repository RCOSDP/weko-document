# researchmap連携機能

## 目的・用途

アイテム登録と同時にアイテムのメタデータをresearchmapの業績として登録する。

## 利用方法



## 利用可能なロール

| ロール   | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:--------:|:--------------:|:----------------:|:------------------:|:------------:|:------------:|:-------------------:|
| 利用可否 | ○              | ○                | ○                  | ○            | ○            |                      |

## 機能内容

データの連携は以下の流れで行われる(項番は図内の番号と対応している)	
    
    1. WEKO上でアイテム登録が完了すると同時に、Signalにデータ連携の予約がされる
    2. 予約キューがRabbitMQにエンキューされる
    3. 2.が完了した段階で連携結果のテーブル（cris_linkage_resultテーブル）のステータスを「実行中」にする
    4. celerybeatが設定されたタイミングでバッチを起動する
    5. キューから得た情報をもとに、データを取得・変換しデータ登録を行う

・キューは、１つのアイテム登録につき１つ存在する。
・データ連携は、一括反映が可能なため、著者はまとめて、アイテムごとに反映する。（10MB制限に留意する）
・WEKOでは１アイテム（＝業績情報）内に複数の著者を抱えているが、researchmapでは１著者に複数の業績情報を抱えている。そのため、１キューあたり、著者数ぶんの連携データを作成する。
・送信対象の著者は、「コントリビュータ」「著者」欄に登録されている、著者DBに登録されている人を対象とする。
・Researchmapに登録されている著者が連携対象。アイテムに登録された著者の中で、著者DBにresearchmapの情報が登録されている場合のみ連携する。
・公開アイテムが連携対象。キューに登録されたアイテムでも、非公開ならば連携は行わない。（コンテンツファイルの公開状態は確認しない）
・連携結果をWEKO内の結果テーブルに書き戻す。（結果が出るまで待機する）
・リトライを行う。

![処理詳細](../media/media/image38.png)


##

|No|ファイルバス|モジュール名|説明|
|---|---|---|---|
|1|weko_admin/admin.py|save_keys|シークレットキーとクライアントキーの保存する|
|2||save_merge_mode|マージモードの変更を保存する|
|3|weko_authors/models.py|get_authorIdInfo|機関名と著者IDから著者情報を取得する|
|4|weko_items_autofill/utils.py|get_researchmap_autofill_item|変換可能なJPCORE MAPPINGをアイテムタイプから取得|
|5|	|get_researchmapid_record_data|researchmapからデータを取得し、JPCOARMAPPING変換可能な形式に整形し、自動入力共通メソッドを呼び出す。|
|6|weko_items_autofill/views.py|get_auto_fill_record_data|Getボタン押下時に呼び出される取得アクション|
|7|weko_items_ui/linkage.py|create_access_token|認証キーの作成する|
|8||creare_jwt|シークレットキーとクライアントキーからJWTを作成する|
|9||retry|指定された回数リトライを行う|
|10|weko_items_ui/models.py|register_linkage_result|連携結果を取得し、DBに保存する|
|11||set_running|連携結果を実行中とする|
|12|weko_items_ui/signals.py|receiver|RabbitMQにキューを入れる|
|13|weko_items_ui/tasks.py|bulk_post_item_to_researchmap|RabbitMQからキューを取得する|
|14||process_researchmap_queue|researchmapに送信に必要な情報を取得し、データを送信する|
|15||get_item|uuidからアイテムを取得する|
|16||is_public|アイテムの公開情報を取得する|
|17||get_authors|著者情報を取得する|
|18||get_merge_mode|マージモードを取得する|
|19||get_achievement_type|業績種別を取得する|
|20||build_achievement|業績種別ごとのJSONを作成する|
|21||build_one_data|著者1人分のデータを作成する|



## 設定値

|設定値名|説明|ファイルパス|デフォルト値|
|---|---|---|---|
|WEKO_ADMIN_SETTINGS_RESEARCHMAP_LINKAGE_SETTINGS|admin_settingsテーブルのreseachmap関連のデータが入るカラム名	|weko_admin/config.py|researchmap_linkage_settings|
|WEKO_ADMIN_SETTINGS_RESEARCHMAP_MERGE_MODES|管理画面で選択できるマージモードの種類|weko_admin/config.py|\[('similar_merge_similar_data','similar merge(similar data priority)'),('similar_merge_input_data','similar merge(input data priority)'),('merge','merge'),('force','force')\]|
|WEKO_ADMIN_CRIS_LINKAGE_SETTINGS_TEMPLATE|CRIS連携用HTMLのパス|weko_admin/config.py|weko_admin/admin/cris_linkage_setting.html|
|WEKO_ITEMS_AUTOFILL_RESEARCHMAP_REQUIRED_ITEM|流用入力機能で自動入力可能なJPCOARマッピングの項目一覧|weko_items_autofill/config.py|\["title","creator","contributor","subject","description","publisher","date","language","type","version","identifier","relation","sourceIdentifier","sourceTitle","volume","issue","numPages","pageStart","pageEnd","conference"\]|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_BASE_URL|researchmapのURL|scripts/instance.cfg|https://api.researchmap.jp|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_HOST|researchmapのhostURL|scripts/instance.cfg|api.researchmap.jp:443|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_RETRY_MAX|リトライ回数の上限|weko_items_ui/config.py|5|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_MERGE_MODE_DEFAULT|マージモードの初期設定値|weko_items_ui/config.py|similar_merge_similar_data|
|WEKO_ITEMS_UI_DEFAULT_LANG|言語未選択の際に、設定される言語|weko_items_ui/config.py|ja|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_MAPPINGS|researchmapとJPCOARの対応表|weko_items_ui/config.py|\[{ 'type'	:	'lang' ,	'rm_name'	:	'paper_title' ,	'jpcoar_name' 	:	'dc:title' ,	'weko_name'	:	'title'	},{ 'type'	:	'lang' ,	'rm_name'	:	'description' ,	'jpcoar_name' 	:	'datacite:description' ,	'weko_name'	:	'description'	},{ 'type'	:	'lang' ,	'rm_name'	:	'publisher' ,	'jpcoar_name' 	:	'dc:publisher' ,	'weko_name'	:	'publisher'	},{ 'type'	:	'lang' ,	'rm_name'	:	'publication_name' ,	'jpcoar_name' 	:	'jpcoar:sourceTitle' ,	'weko_name'	:	'sourceTitle'	},{ 'type'	:	'authors' ,	'rm_name'	:	'authors' ,	'jpcoar_name' 	:	'jpcoar:creator' ,	'weko_name'	:	'creator'	},{ 'type'	:	'identifiers' ,	'rm_name'	:	'identifiers' ,	'jpcoar_name' 	:	'jpcoar:relation' ,	'weko_name'	:	'relation'	},{ 'type'	:	'simple_value' ,	'rm_name'	:	'publication_date' ,	'jpcoar_name' 	:	'datacite:date' ,	'weko_name'	:	'date'	},{ 'type'	:	'simple' ,	'rm_name'	:	'volume' ,	'jpcoar_name' 	:	'jpcoar:volume' ,	'weko_name'	:	'volume'	},{ 'type'	:	'simple' ,	'rm_name'	:	'number' ,	'jpcoar_name' 	:	'jpcoar:issue' ,	'weko_name'	:	'issue'	},{ 'type'	:	'simple' ,	'rm_name'	:	'starting_page' ,	'jpcoar_name' 	:	'jpcoar:pageStart' ,	'weko_name'	:	'pageStart'	},{ 'type'	:	'simple' ,	'rm_name'	:	'ending_page' ,	'jpcoar_name' 	:	'jpcoar:pageEnd' ,	'weko_name'	:	'pageEnd'	},{ 'type'	:	'simple' ,	'rm_name'	:	'language' ,	'jpcoar_name' 	:	'dc:language' ,	'weko_name'	:	'language'	},{ 'type'	:	'type' ,	'rm_name'	:	'published_paper_type' ,	'jpcoar_name' 	:	'dc:type' ,	'weko_name'	:	'type'	},{ 'type'	:	'type' ,	'rm_name'	:	'misc_type' ,	'jpcoar_name' 	:	'dc:type' ,	'weko_name'	:	'type'	},{ 'type'	:	'type' ,	'rm_name'	:	'book_type' ,	'jpcoar_name' 	:	'dc:type' ,	'weko_name'	:	'type'	},{ 'type'	:	'type' ,	'rm_name'	:	'presentation_type' ,	'jpcoar_name' 	:	'dc:type' ,	'weko_name'	:	'type'	},{ 'type'	:	'type' ,	'rm_name'	:	'work_type' ,	'jpcoar_name' 	:	'dc:type' ,	'weko_name'	:	'type'	},{ 'type'	:	'type' ,	'rm_name'	:	'dataset_type' ,	'jpcoar_name' 	:	'dc:type' ,	'weko_name'	:	'type'	} \]|
|WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_TYPE_MAPPINGS|researchmapのtypeとJPCOARの資源タイプの対応表|weko_items_ui/config.py|\[{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	' ' ,	'JPCOAR_resource_type'	:	'article'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'scientific_journal' ,	'JPCOAR_resource_type'	:	'journal article'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'international_conference_proceedings' ,	'JPCOAR_resource_type'	:	'conference paper'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'research_institution' ,	'JPCOAR_resource_type'	:	'departmental bulletin paper'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'symposium' ,	'JPCOAR_resource_type'	:	'conference paper'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	' research_society' ,	'JPCOAR_resource_type'	:	'article'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'in_book' ,	'JPCOAR_resource_type'	:	'article'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'master_thesis',	'JPCOAR_resource_type'	:	'master thesis'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'others' ,	'JPCOAR_resource_type'	:	'article'	},{ 'achievement_type'	:	'published_papers' ,	'detail_type_name'	:	'doctoral_thesis' ,	'JPCOAR_resource_type'	:	'doctoral thesis'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	' ' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'report_scientific_journal' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'report_research_institution' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'summary_international_conference' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'summary_national_conference' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'technical_report' ,	'JPCOAR_resource_type'	:	'technical report'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'introduction_scientific_journal' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'introduction_international_proceedings' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'introduction_commerce_magazine' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'introduction_other' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'lecture_materials' ,	'JPCOAR_resource_type'	:	'learning object'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'book_review' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'meeting_report' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'misc' ,	'detail_type_name'	:	'others' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	' ' ,	'JPCOAR_resource_type'	:	'book'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'scholarly_book' ,	'JPCOAR_resource_type'	:	'book'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'dictionary_or_encycropedia' ,	'JPCOAR_resource_type'	:	'book'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'textbook' ,	'JPCOAR_resource_type'	:	'book'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'report' ,	'JPCOAR_resource_type'	:	'report'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'general_book' ,	'JPCOAR_resource_type'	:	'book'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'musical_material' ,	'JPCOAR_resource_type'	:	'musical notation'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'film_or_video' ,	'JPCOAR_resource_type'	:	'video'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'image_material' ,	'JPCOAR_resource_type'	:	'image'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'phonetic_material' ,	'JPCOAR_resource_type'	:	'sound'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'map' ,	'JPCOAR_resource_type'	:	'map'	},{ 'achievement_type'	:	'book_etc' ,	'detail_type_name'	:	'others' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	' ' ,	'JPCOAR_resource_type'	:	'conference presentation'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'oral_presentation' ,	'JPCOAR_resource_type'	:	'conference presentation'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'invited_oral_presentation' ,	'JPCOAR_resource_type'	:	'conference presentation'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'keynote_oral_presentation' ,	'JPCOAR_resource_type'	:	'conference presentation'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'poster_presentation' ,	'JPCOAR_resource_type'	:	'conference poster'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'public_symposium' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'nominated_symposium' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'public_discourse' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'media_report' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'presentations' ,	'detail_type_name'	:	'others' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	' ' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'artistic_activity' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'architecural_works' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'software' ,	'JPCOAR_resource_type'	:	'software'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'database' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'web_service' ,	'JPCOAR_resource_type'	:	'interactive resource'	}{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'educational_materials' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'works' ,	'detail_type_name'	:	'others' ,	'JPCOAR_resource_type'	:	'other'	},{ 'achievement_type'	:	'others' ,	'detail_type_name'	:	'works' ,	'JPCOAR_resource_type'	:	,'other'	}\]|
|LINKAGE_MQ_EXCHANGE|RabbitMQのExchangeの設定値|scripts/instance.cfg|Exchange('cris_researchmap_linkage', type='direct')|
|LINKAGE_MQ_QUEUE|RabbitMQのQueueの設定値|scripts/instance.cfg|Queue("cris_researchmap_linkage", exchange=LINKAGE_MQ_EXCHANGE, routing_key="cris_researchmap_linkage",queue_arguments={"x-queue-type":"quorum"})|
|CELERY_BEAT_SCHEDULE|バッチを起動するタイミングについての設定値|scripts/instance.cfg|bulk_post_item_to_researchmap': {'task': 'weko_items_ui.tasks.bulk_post_item_to_researchmap','schedule': crontab(days=1, hour=0, minute=0),'args': [],  }|



## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足（訂正）：JWT生成関数は `create_jwt`（`weko_items_ui.linkage`。`creare_jwt` は誤植）。BASE_URL/HOST の既定は `https://api-trial.researchmap.jp` / `api-trial.researchmap.jp:443`（本番 `api.researchmap.jp` ではない）。連携結果モデルは `CRISLinkageResult`（table `cris_linkage_result`）。連携タスクの beat は `crontab(hour=0, minute=0)`。config は `WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_*`（weko-items-ui）。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|---|---|---|
|||初版作成|
