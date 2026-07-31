# Findings: 仕様書 vs 実装 の突き合わせ記録

> 外部/検索由来の内容はここにのみ書く（task_plan.md には書かない）。
> ソースは信頼できるローカルリポジトリ `/home/mhaya/weko`（tag v2.0.2）。

## restricted_access（5並列エージェント調査済み 2026-07-13）

### 調査方式
5並列リサーチエージェントで各仕様の記述を weko ソースと突き合わせ済み。以下は統合編集に使う要点。

---

### RESTRICTED_ACCESS_01.md — アイテムタイプ管理（制限公開）: 全claim CONFIRMED
- 対応アイテムタイプ（日立納品時）: 31001 利用申請 / 31002 二段階利用申請 / 31003 利用報告-Data Usage Report。SQL: `scripts/demo/resticted_access.sql:19-21`。派生: 31004-31008（`scripts/demo/item_type_usage_apply.sql`）。
- config: `weko-workflow/config.py:480-486` `WEKO_WORKFLOW_USAGE_APPLICATION_ITEM_TYPES_LIST=[31001,31002,31004-31008]` / `WEKO_WORKFLOW_USAGE_REPORT_ITEM_TYPES_LIST=[3007,31003]` / `..._ITEM_TITLE='利用申請'/'利用報告'`。
- 制限公開フラグ = `WorkFlow.open_restricted`（table `workflow`, Boolean, **default True**）`weko-workflow/models.py:697`。UI: `admin/workflow_list.html:44,77`（Restricted Access Flag列）。
- アクセス選択肢の内部値: open_access/open_date/open_login/open_no/open_restricted（default open_restricted）。制限公開版ファイルpropは `resticted_access.sql` 内のschema/form（標準の `scripts/demo/properties/files.py` には open_restricted 無し）。
- 提供方法 provide[]{role, workflow}; 利用規約 terms、自由入力=`term_free`（`weko-records-ui/utils.py:1592`, 判定 :1049-1050）。
- アップロード自動設定: filename=`app.js:3015`, format/size=`app.js:3018-3021`, DB格納 `weko-deposit/api.py:1201`。Allow Multiple checked+disabled: `create_itemtype.js:1078-1091`。
- 追記すべき: 目的概要 / 関連モジュール（weko-workflow, weko-records(-ui), weko-itemtypes-ui, weko-items-ui, weko-deposit） / configキー / モデル名 / アクセス内部値マッピング / 処理概要 / 定義SQL所在。
- 軽微: 32行目「データタイプ」の説明文が乱れ（要整形）。

### RESTRICTED_ACCESS_02.md — アイテム詳細(制限公開): 概ねCONFIRMED、EN文言に軽微差異
- `__check_user_permission`: `weko-records-ui/permissions.py:122`（`check_file_download_permission`内ネスト）。管理者ロール = `WEKO_PERMISSION_SUPER_ROLE_USER=['System Administrator','Repository Administrator']` + `WEKO_PERMISSION_ROLE_COMMUNITY=['Community Administrator']`（config.py:38-41）。登録者本人(created_by/owner/weko_shared_ids)も許可(:132,165-168)。
- 警告文言: `weko-admin/config.py:1286-1296` `WEKO_ADMIN_RESTRICTED_ACCESS_ERROR_MESSAGE`（AdminSettings restricted_access.error_msg、**管理画面で編集可**）。JA「このデータは利用できません（権限がないため）。」一致。EN実装「This data is not available for this user」**末尾ピリオド無し**（仕様は有り→修正候補）。
- 「Restricted Access」表示: `body_contents.html:214-219`, `preview_carousel.html:151`, JS分岐 `detail.js:320 is_restricted_access`。
- ファイルURL権限: route `recid_files`+`page_permission_factory`（config.py:127-133）。open_no=:305-319, open_restricted=:320-321→`check_open_restricted_permission`:327-336。Permission requiredテンプレ `config.py:30 WEKO_PERMISSION_REQUIRED_TEMPLATE`。
- モデル: `FileOnetimeDownload`(table `file_onetime_download`) `models.py:374-546` 列: id, approver_id(FK), record_id, file_name, expiration_date, download_limit, download_count, user_mail, is_guest, is_deleted, extra_info(JSON) + created/updated。`FileUrlDownloadLog`(table `file_url_download_log`) `models.py:681-777` 列: id, url_type(Enum SECRET/ONETIME), secret_url_id(FK), onetime_url_id(FK), ip_address(INET), access_status(Enum OPEN_NO/OPEN_DATE/OPEN_RESTRICTED), used_token + created/updated。※仕様未記載列: url_type/secret_url_id/ip_address（シークレットURL共用）。共通処理 `DownloadMixin` :294-371。
- DLエラー文言: `utils.py:2315-2355 validate_url_download`。論理削除「This URL has been deactivated.」:2347、回数超過「The download limit has been exceeded.」:2349、期限超過「The expiration date for download has been exceeded.」:2351。JA訳 messages.po:278-311。※旧実装 `validate_onetime_download_token`(:1297-1327)併存、現行は 2315側。
- DISPLAY_FLAG: `weko-admin/config.py:1298 WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG=False`。ゲート: `fd.py:487-488`, `permissions.py:332,348`, `weko-workflow admin.py:296,384,419 / views.py:1628`。
- 利用報告メール: 初回DLのみ `fd.py:598 process_onetime_file_download`→`check_and_send_usage_report`(utils.py:1196-1223, extra_info['send_usage_report']で1回制御)。ゲスト利用報告リンク期限: `weko-workflow/utils.py:3629-3634` AdminSettings `usage_report_workflow_access.expiration_date_access`(既定500)→`GuestActivity.expiration_date`。
- ルート: recid_files, recid_file_details, recid_guest_onetime_validation(GET)/recid_guest_file_download(POST)（config.py:127-239）。
- 追記すべき: 関連モジュール / 処理概要(実メソッドフロー) / モデルスキーマ / configキー / ルート / 文言が編集可である旨。

### RESTRICTED_ACCESS_03.md — ワークフロー管理(制限公開): 構成はDB管理(コード非強制)
- アクション名 CONFIRMED: `weko-workflow/config.py:285-295` Start/End/Item Registration/Approval。選択可能一覧 `WEKO_WORKFLOW_ACTIONS`(config.py:321-328)。
- フロー構成（利用申請=Start-ItemReg-Approval-End 等）は **コード非依存の運用推奨構成**（FlowDefine/FlowActionはDB登録データ）。仕様に「推奨構成」である旨明記すべき。
- `workflow_flow_action_role` `models.py:586-631`: action_role, action_role_exclude(=Deny), action_user, action_user_exclude(=Deny), specify_property, `action_item_registrant`(Bool default False), action_request_mail。
- action_item_registrant=true→登録者が承認者: 保存時 action_user=None+flag=True（api.py:320-335, `WEKO_WORKFLOW_ITEM_REGISTRANT_ID=-2` config.py:584）。owner展開 api.py:2617-2626, 承認待ちクエリ:2020。承認依頼メール未送信は「意図的スキップ」でなく宛先(-1)解決不能で未送信(utils.py:4277-4283)。
- `admin_settings` restricted_access `settings.edit_mail_templates_enable`（default False, `weko-admin/config.py:1326`）で Specify property / Item registrant / 通知メール設定 表示制御（admin.py:81-82,113-117, flow_detail.html:201,210,225,232）。承認時メール送信もこのフラグでガード(views.py:1672-1683)。
- Specify Property = プロパティ定義に `"approval":true` を持つもの（admin.py:136-153, utils.py:4101-4116, value=-1）。
- 通知メール3種: 承認依頼(Approval Request Notification Email→request_approval[/_for_guest]), 承認却下(Approval Rejection→inform_reject), 承認(Approval Notification→inform_approval)。実装 `process_send_approval_mails`(utils.py:4191-4295)。設定は FlowAction.send_mail_setting(JSON, models.py:570-583)に previous/next 構成。
- open_restricted default True（仕様の「利用報告=チェックしない」と混同注意）。
- 保存メッセージ: アクション保存「Updated flow action successfully」(admin.py:276), フロー保存「Updated flow successfully.」(admin.py:173)。
- 追記すべき: 目的/関連モジュール(weko-workflow, weko-admin) / データモデル(FlowDefine/FlowAction/FlowActionRole/WorkFlow/WorkflowRole) / 処理概要 / configキー(-2/-3/-1, WEKO_WORKFLOW_ACTIONS) / send_mail_setting JSON構造 / 要修正点3件。

### RESTRICTED_ACCESS_04.md — メールテンプレート: 概ねCONFIRMED、デフォルト数7→15に更新要
- ゲート: `admin_settings` restricted_access `edit_mail_templates_enable`(default False, `weko-admin/config.py:1326`)。画面ゲート `weko-admin/ext.py:57`(endpoint mailtemplates 非表示)。
- 画面5項目 Subject/Recipients/CC/BCC/body: `invenio-mail/static/js/mail_template.js`(163/169/173/177/180)。Subject・body必須(js:235, msg「Please input the Mail Subject and Mail Body.」`mail_templates.html:61`)。アドレス登録済み検証 `invenio-mail/admin.py:164-254 get_invalid_emails`(`User.filter_by(email,active=True)`)、エラー「Invalid email addresses (...) detected...」admin.py:182-186。
- `INVENIO_MAIL_ADDITIONAL_RECIPIENTS_ENABLED`: `invenio-mail/config.py:170 =False`。画面表示制御 admin.py:150-154 + mail_template.js:221-290。送信制御 `weko-workflow/utils.py:2669`(無効時subject/bodyのみ, DBは保持し再有効化で復活)。
- 追加宛先検証: 登録済み+active（admin.py:235-254）、カンマ区切り(admin.py:171-176)。送信時自動削除: `weko-workflow/utils.py:2653-2670`(無効ユーザ→MailTemplateUsers.delete_by_user_id)。※宛先は**メール文字列でなくuser_idで永続化**（mail_template_users）。
- デフォルトメール: 実体 `scripts/demo/restricted_mail_template.sql`(table `mail_templates`: id,mail_subject,mail_body,default_mail,genre_id)。**現行は id=1〜15 の15種**（仕様は7種→過小）。③④⑤件名は現行「（ログインユーザー向け）／(for logged in users)」付き（仕様は短縮形＝.tpl版）。固定参照ID: `WEKO_WORKFLOW_USAGE_REPORT_REMINDER_MAIL_TEMPLATE_ID='6'`, `WEKO_WORKFLOW_REQUEST_FOR_REGISTER_USAGE_REPORT='7'`(config.py:453,457)。
- プレースホルダ: 権威定義 `weko-workflow/utils.py:2731-2785 replace_characters replace_list`（仕様7種すべて実在。全集合は多数—[restricted_site_name_ja/en], [url_guest_user], [restricted_activity_id], [restricted_download_link], [usage_report_url], [restricted_expiration_date/_ja/_en], [data_download_date], [restricted_fullname], [restricted_mail_address], [restricted_university_institution], [restricted_research_title], [restricted_data_name], [restricted_application_date], [restricted_usage_activity_id], [file_name], [restricted_download_count/_ja/_en], [secret_url], [terms_of_use_jp/en], [landing_url] 他）。ヘルプ `invenio-mail/config.py:21-166 INVENIO_MAIL_VARIABLE_HELP`（typo: `resricted_download_count`）。
- モデル: admin_settings(AdminSettings models.py:1227), mail_templates(MailTemplates models.py:116), mail_template_users(MailTemplateUsers models.py:252, template_id/user_id/mail_type複合PK), mail_template_genres, MailType enum=recipient/cc/bcc(:241)。
- 利用可能ロール: システム管理者のみ（ext.py endpoint mailtemplates）。
- 追記すべき: 目的/利用可能ロール/関連モジュール(invenio-mail, weko-admin, weko-workflow)/処理概要/configキー/モデル/権威プレースホルダ一覧/デフォルト15種へ更新/無効ユーザ宛先保持挙動。

### RESTRICTED_ACCESS_05.md — プロフィール表示設定: 実装と重大な乖離 複数
- **CONTRADICTED**: 画面・保存は **weko-admin** 側（`ProfileSettingView admin.py:1437-1449`, メニュー登録 admin.py:2544-2552 カテゴリ Advanced, **メニュー名 "Profile Settings"**（"Item"無し）, 保存API `views.py:866-890 POST /api/admin/profile_settings/save`）。weko-user-profiles は消費側（フォーム生成・autofill）。
- 設定格納: `AdminSettings` name=`profiles_items_settings`(JSON)。デフォルト `weko-user-profiles/config.py:180-202 WEKO_USERPROFILES_DEFAULT_FIELDS_SETTINGS`（項目構造 {order, visible, label_name, format, options}, fullname/university/department/position/item1〜16）。
- 入力方式(format): `USERPROFILES_FORMAT_OPTION_LIST=["text","select","identifier","phonenumber","position(other)"]`(config.py:177)。仕様の3種は不足（実5種）。select時オプション欄 js:53-61。プレースホルダEN「separate option with the | character」js:59 ハードコード。**JA文言はNOT-FOUND（i18n未対応）**。
- **バリデーション/メッセージ 大半 CONTRADICTED/NOT-FOUND**: 実装(js:117-127 handleSave)は label_name未入力 or select時options空要素のみチェック、**エラーは汎用 'Failed to update settings.'（英語のみ、赤アラート）**。項目名チェック無し、ボックス赤表示無し。成功は backend返却 "Settings updated successfully"(views.py:886)。仕様の個別文言（項目名/ラベル名/オプション未記入、「変更が保存されました/Saved successfully.」）は**未実装**。
- autofill連携: `get_user_profile_info`(weko-user-profiles/utils.py:33-89, visible gating :55-83), `get_institute_data`(models.py:236-285)。**ただし `WEKO_USERPROFILES_CUSTOMIZE_ENABLED`(default False, config.py:174)がTrueの時のみ visible制御有効**。デフォルトは全項目出力。
- ロール: 保存API `@roles_required([System Administrator, Repository Administrator])`(views.py:869-870) CONFIRMED。画面indexは標準admin制御。
- 追記/修正すべき: 関連モジュール訂正(weko-admin主, weko-user-profiles消費, weko-workflow/weko-workspace autofill) / メニュー名訂正 / 設定スキーマ / configキー(WEKO_USERPROFILES_CUSTOMIZE_ENABLED等) / format5種 / 処理概要(実ルート/メソッド) / メッセージ実態への修正 or「未実装/将来対応」注記 / autofill前提フラグ。

## ams（2並列調査済み 2026-07-14）

### 前提
AMSは未病データベースの **Nuxtフロント `weko-frontend`（この環境に無い別リポジトリ。`nginx/ams/weko-frontend/`）** が中心。フロント(*.vue/app.config.ts/server)は検証不可。以下はバックエンド `/home/mhaya/weko`(v2.0.2) 側の検証結果。

### AMS_SHIBBOLETH_01
- `weko_accounts.views.shib_sp_login` CONFIRMED。実エンドポイント **`POST /weko/shib/login`**（Blueprint url_prefix=/weko）。`/secure/login.py` は nginx CGI（`nginx/login.py`）で `/weko/shib/login` へ中継。config `WEKO_ACCOUNTS_SHIB_IDP_LOGIN_URL='{}secure/login.py'`。
- ロール付与: `WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS`=True時 `sync_shib_gakunin_map_groups`→`ShibUser.check_in`→`_get_roles_to_add`→`_assign_roles_to_user`。mAPグループ形式は config駆動 `<prefix>_<fqdn>_<role_keyword>_<suffix>`（既定 prefix=jc, role_keyword=ro; `WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT`）。**仕様の `jc_<fqdn>_groups_<groupname>` の "groups" はAMS設定インスタンス**（既定は "ro"）。属性parse=`utils.parse_attributes`, fqdn=`create_fqdn_from_entity_id`。
- ログイン画面エラー文字列（backend実在性）:
  - 「Login is blocked.」CONTRADICTED（実際は `flash("Failed to login.")`+リダイレクト、403直接応答でない。ブロック判定は AdminSettings `blocked_user_settings.blocked_ePPNs`）
  - 「There is no user information.」NOT-FOUND
  - 「Missing SHIB_CACHE_PREFIX!」「Missing Shib-Session-ID!」「Missing SHIB_ATTRs!」PARTIAL（文字列は views.py に存在するが flash+リダイレクトが基本、400直接応答は例外時のみ）。※shib_login側は「Missing SHIB_ATTR!」(単数)
- OAuth認証画面エラー4種（This response type.../The client ID.../The scope.../Access has been denied.）NOT-FOUND＝**フロント生成**。backendは invenio-oauth2server `views/server.py authorize`+oauthlib標準エラー（unsupported_response_type/invalid_client/invalid_scope/access_denied、client不在は404）。
- 関連モジュール(backend): weko-accounts（shib_sp_login/ロール同期）, invenio-oauth2server（OAuth）。参照 other/SHIBBOLETH_01.md, api/API_01_Oauth2.md。

### AMS_GRDM_BUTTON_01
- JSON-LDマッピング CONFIRMED: 実体は weko-admin「SWORD API JSON-LDマッピング設定」(`SwordAPIJsonldSettingsView`)。table `jsonld_mappings`/`jsonld_mappings_version`, model `ItemTypeJsonldMapping`, API `weko_records.api.JsonldMapping`, 変換 `weko_search_ui.mapper.JsonLdMapper`。固定値は `$` 接頭辞記法（`$isVersionOf`）。参照先 admin/ADMIN_1_5.md 実在。
- RO-Crate変換 CONFIRMED: `RoCrateConverter`(weko-records-ui/utils.py), model `RocrateMapping`(table `rocrate_mapping`), endpoint `WekoRecordsResource.get_v1`＝**`GET /api/v1/records/<id>`**（config `item_route`/`WEKO_RECORDS_UI_REST_ENDPOINTS`）。レスポンスに rocrate/metadata/index、`metadata.hasRequestmailAddress` 含む。関連タイプ/識別子は jpcoar relatedIdentifier(relationType)。担当は weko-records-ui（invenio-records-rest の /api/records とは別系統）。

### AMS_ARCHITECTURE_01
- nginx: `nginx/weko-ams.conf` **存在**。`weko-ams-restricted.conf` **NOT-FOUND（v2.0.2未収録）**。
- パス振り分けは専用locationでなく `location / → nuxt`(catch-all)。WEKOへ回る明示location: `/api/v1`, `~/(admin|oauth|tree)`, `/oai`, `/api/records`, `/api/files`, `~/record/[0-9]*/(files|file_preview|preview)/`, `/api/iiif/v2/`, `/ping`, `/static`, `/data`, `/weko/shib`, Shibboleth系。
- `~ /api/v1/(captcha|records/[0-9]*/request-mail)` は **IP allow/deny 制限**（内部NWのみ、フロントserver経由前提）。
- フロントが呼ぶ backend API 実在: リクエストメール=`RequestMail`(`send_request_mail`, weko-records-ui, `/api/v1/records/<id>/request-mail`)※weko-depositでなくweko-records-ui。CAPTCHA画像=`CreateCaptchaImage`(`/api/v1/captcha/image`), 検証=`CaptchaAnswerValidation`(`/api/v1/captcha/validate`)（captcha.py, config `WEKO_RECORDS_UI_CAPTCHA_EXPIRATION_SECONDS=900`/`_TTL_SECONDS=600`）。OAuth2 token=invenio-oauth2server `/oauth/token`。

### ams 統合方針
- 各ファイルに「関連モジュール（バックエンド）」「実装補足（バックエンド）」を追記。
- backend接点の矛盾は実装準拠に修正（実エンドポイント名、restricted.conf不在、mAP形式、request-mailはweko-records-ui、IP制限、catch-all routing、OAuthはoauthlib標準）。
- フロント固有(*.vue/app.config.ts)は別リポジトリのため検証不可＝そのまま残し、フロント仕様である旨を明記。エラー表はフロント表示である旨注記し、backend実文字列と異なる点を修正。

## api（9並列調査 2026-07-14）
各API仕様を weko の REST 実装と突き合わせ。巨大な定義ダンプ(API_11 JSON_Form 7605行, API_10 JSON_Schema)はエンドポイント確認のみ。結果は各エージェントから収集し以下に反映（本セクションは調査後に随時追記）。
- 担当割: (1)Oauth2 (2)OAI-PMH (3)OpenSearch+index_search (4)item_search+RO-Crate (5)workflow+activity_list+approval (6)index_op (7)sword_api (8)JSON_Schema+JSON_Form(軽) (9)author + 制限公開系小API + ENDPOINT/render/README

### 反映すべき要点（api 全21ファイル、調査済）
- API_01 Oauth2: authorizeは`/oauth/authorize`(GET/POST両対応), tokenは`/oauth/token`。handler=invenio_oauth2server.views.server.authorize/access_token。grant_type=authorization_code/client_credentials/refresh_token, response_type=code/token。scope機構=各module scopes.py+entrypoint。scope一覧(現行): user:email, deposit:write/actions, index:create/read/update/delete, item:read/create/update/delete, ranking:read, author:search/create/update/delete, oa_status:update, user:activity, file:read。config: OAUTH2_PROVIDER_TOKEN_EXPIRES_IN=3600, OAUTH2SERVER_ALLOWED_GRANT_TYPES/RESPONSE_TYPES。関連モジュールにscope提供7モジュール追加。weko-accountsはOAuth実装含まず。err: client不在404, 未ログイン302。
- API_02 OAI-PMH: /oai(GET/POST) blueprint invenio_oaiserver, dispatch views/server.py:response→response.py各verb。6 verb確認。metadataFormatは固定でなくDB(WekoSchema)から get_oai_metadata_formats(weko-schema-ui)が動的生成(コード既定oai_dc/marc21のみ)。set=index(weko-index-tree)。resumptionToken=ES scroll, OAISERVER_PAGE_SIZE=100。実ES対象は INDEXER_DEFAULT_INDEX(OAISERVER_RECORD_INDEXは未使用)。noSetHierarchyは実装で未発行。エラーHTTP422。関連: invenio-oaiserver/weko-schema-ui/weko-index-tree/weko-deposit。見出し表記ListRecord→ListRecords。
- API_03 OpenSearch: GET /api/opensearch/search + /api/opensearch/description.xml。handler invenio_records_rest.views.RecordsListResource.get + weko_search_ui.views.opensearch_description。factory weko_search_ui.query.opensearch_factory。**wid=作成者識別子(creator.nameIdentifier)であってアイテムIDではない(要修正)**。Iid→iid(path/index)。q(主検索語)未記載→追加。size(=list_view_num,既定10)/page(=page_no,既定1)。権限フィルタ get_permission_filter。config: WEKO_SEARCH_KEYWORDS_DICT, WEKO_OPENSEARCH_SYSTEM_SHORTNAME/_DESCRIPTION/_IMAGE_URL。
- API_08 index_search: ほぼ空。GET /api/index/(末尾slash), handler weko_search_ui.rest.IndexSearchResource.get, factory item_path_search_factory(別名weko_search_factory)。q=index_id。resp JSON(hits+aggregations)。権限 get_permission_filter。表ヘッダの/api/opensearch/search誤記→/api/index/。関連: weko-search-ui, weko-index-tree(Indexes), weko-records(json_v1_search)。/api/v1/records(IndexSearchResourceAPI)は別APIで混同注意。
- API_07 item_search: スタブ(関連/機能/処理概要空)。GET /api/records/ handler invenio_records_rest.views.RecordsListResource.get, factory weko_search_ui.query.es_search_factory(recid)/opensearch_factory。serializer json_v1_search/opensearch_v1_search。record_class weko_records.api.WekoRecord。WEKO_SEARCH_TYPE_DICT{FULL_TEXT:0,KEYWORD:1,INDEX:2}, WEKO_SEARCH_MAX_RESULT=10000。権限 get_permission_filter。RO-Crate形式でない(API_12と別物)。
- API_12 RO-Crate: 3 API。§1 GET /api/v1/records handler **weko_search_ui.rest.IndexSearchResourceAPI.get_v1**(invenio_records_rest.views.pyでない・要修正), factory weko_search_factory, RO-Crate変換 RoCrateConverter/RocrateMapping(記載欠落), OAuth @require_api_auth(allow_anonymous)+item_read_scope, RocrateMappingありのITのみ対象。§2 GET /api/v1/records/<id> handler **weko_records_ui.rest.WekoRecordsResource.get_v1**(GetIndexは誤り・要修正), RoCrateConverter, metadata.hasRequestmailAddress(RequestMailList)。§3 POST /api/v1/records/list handler weko_search_ui.rest.IndexSearchResultList.post_v1, size10000固定, TSV生成 result_download_ui。config WEKO_SEARCH_REST_ENDPOINTS, WEKO_RECORDS_UI_CITES_REST_ENDPOINTS, WEKO_ADMIN_FACET_SEARCH_SETTING_BUCKET_SIZE=1000。§1ソートID降順記述は実装control_number昇順付与と不一致(要確認)。
- API_04 workflow: POST/GET/DELETE /api/depositactivity[/<activity_id>] handler weko_workflow.views.ActivityActionResource(blueprint weko_activity_rest url_prefix=/depositactivity)。scope user:activity(activity_scope)+require_api_auth。POST params item_type_id+file。応答 activityId/email/status。err InvalidInputRESTError=405, ActivityBaseRESTError=400, ActivityNotFoundRESTError=404, DeleteActivityFailedRESTError=404。logging_errorはINFO。ロール表はコード非担保(scope+authのみ)。config WEKO_WORKFLOW_GAKUNINRDM_DATA/PREFIX。
- API_16 activity_list: GET /api/<version>/workflow/activities handler weko_workflow.rest.GetActivities.get_v1。scope user:activity。ETag/If-None-Match→304。Accept-Language(en/ja)。params status(既定todo,値todo/wait/all)/limit(20)/page(1)/pretty(false)。check_role(WEKO_PERMISSION_ROLE_USER)。resp total/condition/activities[created,updated,activity_id,item_name,workflow_type,action,status,user]。err InvalidParameterValueError=400/PermissionError=403/VersionNotFoundRESTError=400。config WEKO_WORKFLOW_REST_ENDPOINTS, _TODO_TAB/WAIT_TAB/ALL_TAB, _API_ACCEPT_LANGUAGES, _API_LIMIT_RATE_DEFAULT。
- API_17 approval: POST /api/<version>/workflow/activities/<id>/approve (ApproveActivity), .../throw-out (ThrowOutActivity), handler post_v1。承認=next_action, 却下=previous_action(req=0)。get_activity_display_info, action_endpoint!='approval'→StatusNotApproveError(400), check_authority_action!=0→PermissionError(403)。応答 next_action{id,endpoint}+action_info{action_id,action_date,action_user,action_status,action_comment}(history action_id==4)。却下も同create_approve_response流用。scope user:activity。404の明示処理なし。ロール表コード非担保。
- API_05 index_op: (1)レガシー POST /api/indextree/create handler weko_index_tree.views.create_index, scope index:create。**「update戻り値None/NoneType iterable」はv2.0.2で誤り(updateはindex返す)→削除・修正**。id=UNIX時間×1000, 既定index_name"New Index"/public_state=False/harvest_public_state=True。(2)管理API IndexManagementAPI(rest.py): GET /api/<v>/tree, GET /tree/<id>, POST /tree/index, PUT /tree/index/<id>, DELETE /tree/index/<id>。scope index:read/create/update/delete。書込は@roles_required(System/Repo/Community Admin)。GET allow_anonymous。DELETE 204だが**body={"status":204}(空でない)**。POST201/PUT200。schema IndexCreate/UpdateRequestSchema。version!=v1→VersionNotFoundRESTError(400)。Content-Type json必須, index_id=0のPUT/DELETE不可。config WEKO_INDEX_TREE_REST_ENDPOINTS。誤記:L285"tru"→true, curl public_state重複。
- API_06 SWORD: 実装=weko-swordserver(invenio-sword無し)。5経路 GET/POST /sword/service-document, GET/PUT/DELETE /sword/deposit/<recid> handler weko_swordserver.views(get_service_document/post_service_document/get_status_document/put_object/delete_object)。認証Bearer/OAuth。scope deposit:write/actions,item:create/update/delete,user:activity(Workflow時)。**conf修正: ACCEPT_PACKAGING=[SimpleZip,SWORDBagIt](["*"]でない), ACCEPT_ARCHIVE_FORMAT=['application/zip','multipart/form-data'], DEPOSIT_ROLE_ENABLE=4ロール(System/Repo/Community Admin+Contributor)**。DELETE成功ヘッダは**Location**(Linkでない)。BAGIT_VERIFICATION config追記。ErrorType enum(errors.py)。POST Direct201/Workflow202。関連追加: weko-items-ui,weko-admin,weko-accounts,weko-logging,weko-notifications,invenio-files-rest,invenio-oaiserver。
- API_10 JSON_Schema: GET /items/jsonschema/<int:item_type_id>[/<activity_id>] handler weko_items_ui.views.get_json_schema(blueprint weko_items_ui url_prefix=/items)。**目的「インデックスID検索」は誤り(index APIのコピペ)→アイテムタイプのJSON Schema返却に修正**。param=item_type_id(インデックスIDでない)。resp例パス/api/index/?q=9も誤り。権限@login_required_customize。data ItemTypes.get_by_id(id).schema。専用config/RESTなし。
- API_11 JSON_Form: GET /items/schemaform/<int:item_type_id>[/<activity_id>] handler get_schema_form。**同様に目的・param説明が誤り→修正**。data ItemType.form。権限@login_required_customize。関連 weko-items-ui(+weko-records,weko-accounts,weko-groups)。
- API_13 author: GET/POST /api/<v>/authors, PUT/DELETE /api/<v>/authors/<identifier> handler weko_authors.rest.AuthorDBManagementAPI。scope author:search/create/update/delete。@roles_required(System/Repo/Community)。**未記載: GET /api/<v>/authors/count(Authors→count_authors)**。検索/登録はES {prefix}-authors。削除は論理削除(is_deleted)。idType='1'(WEKO)のauthorIdInfoは除去。config WEKO_AUTHORS_REST_ENDPOINTS, WEKO_AUTHORS_ES_INDEX_NAME。レート100/min(429)。
- API_14 acquiring_application: 利用規約取得 GET /api/<v>/records/<pid>/files/<file>/terms handler weko_records_ui.rest.GetFileTerms。利用申請開始 POST .../application handler FileApplication。scope activity_scope, @require_api_auth(True)。WEKO_RECORDS_UI_RESTRICTED_API=False時403(既定False)。Etag=md5(filename_terms)。多言語 WEKO_RECORDS_UI_API_ACCEPT_LANGUAGES=['en','ja']。resp activity_id/activity_url/item_type_schema(ゲストtoken)。err ContentsNotFoundError=404,InvalidTokenError=400,InvalidWorkflowError=403。config WEKO_RECORDS_UI_REST_ENDPOINTS。
- API_15 application_decision: GET /api/<v>/records/<pid>/need-restricted-access handler weko_records_ui.rest.NeedRestrictedAccess.get_v1(記載漏れ)。scope item_read_scope, @require_api_auth(True)。処理 get_file_info_list+check_file_download_permission+check_content_clickable。resp 各file{need_restricted_access,filename}。WF未完了404。
- API_18 CAPTCHA: GET /api/v1/captcha/image handler CreateCaptchaImage(create_captcha_image), POST /api/v1/captcha/validate handler CaptchaAnswerValidation(validate_captcha_answer)(rest.py記載漏れ)。key=sha1(datetime+salt), token=sha256(64桁)。Redis expire=WEKO_RECORDS_UI_CAPTCHA_EXPIRATION_SECONDS(900), ttl=min(,_TTL_SECONDS=600)。不一致400+key削除。CACHE_REDIS_DB。
- API_19 request_mail: POST /api/v1/records/<pid>/request-mail handler weko_records_ui.rest.RequestMail.post_v1→api.send_request_mail(記載漏れ)。**処理順は実装:①token照合(401)→②送信先取得(404)→③送信元必須→④email検証(400) (仕様の順序は逆・要修正)**。**送信元は「Cc」でなく別途通知メール(recipients=[msg_sender])・要修正**。必須body from/subject/message/key/authorization_token。key/tokenはCAPTCHA発行。OAuthデコレータ無し(未ログイン可)。config WEKO_RECORDS_UI_REQUEST_MESSAGE/_NOTIFICATION_MESSAGE。
- API_ENDPOINT_01: UIアプリ/APIアプリ2構成。実APIベース/api, version segment(v1)→/api/v1/...。各module *_REST_ENDPOINTS。
- API_09 render: /admin/itemtypes/<item_type_id>/render handler weko_itemtypes_ui.admin.render_itemtype(Flask-Adminビュー、RESTでない)。GET。関連 weko-itemtypes-ui。

## access_control（5並列調査 2026-07-14）

### 共通：管理画面のアクセス担保機構（全ADMIN_*に追記）
- `weko_admin/ext.py: WekoAdmin.role_has_access`（`@app.before_request` の `is_accessible_to_role` が全Flask-Adminビューの is_accessible/is_visible を上書き）。
- `weko_admin/config.py: WEKO_ADMIN_ACCESS_TABLE`（System=全許可バイパス / Repository=`WEKO_ADMIN_REPOSITORY_ACCESS_LIST` / Community=`WEKO_ADMIN_COMMUNITY_ACCESS_LIST`。repositoryリストはcommunityリストを+=）。判定キーはビューのendpoint名（ModelViewはクラス名小文字）。ロール無し(登録/一般)・ゲストは全画面×。
- CRUD（can_create/can_edit/can_delete + get_query絞り込み）は画面アクセスとは別レイヤ。コミュニティ絞り込みは `Community.get_repositories_by_user` / `WEKO_PERMISSION_SUPER_ROLE_USER`(=System+Repository)。

### ADMIN_* 検証結果（矛盾のみ抜粋、他は整合）
- ADMIN_ITEM_TYPE: 整合。OAIスキーマ実体=weko-schema-ui(`schemasettings`)、JSON-LDマッピング=weko-admin(`jsonld-mapping`)、プロパティ=System専用。
- ADMIN_ITEM: 整合。一括更新=weko-records-ui admin、他(削除/export/import/rocrate/custom_sort)=weko-search-ui admin。
- ADMIN_INDEXTREE: 整合。雑誌情報=weko-indextree-journal、カスタムソート=weko-search-ui。
- ADMIN_WEB_DESIGN: 整合。`WidgetSettingView.get_query`でsuper以外はコミュニティ絞り込み。
- ADMIN_AUTHOR: 整合（authors/export/import すべてcommunityリスト）。
- ADMIN_STATISTICS/WORKFLOW/COMMUNITY: 整合。WORKFLOW: 利用申請フラグ=System専用(`WorkFlowSettingView...is_display_restricted_access_checkbox`, `FlowSettingView._check_auth`)。COMMUNITY作成: `can_create` min(role_ids)<=2(=System/Repo)。
- ADMIN_OAI_PMH: 上位整合。**矛盾**: harvestの一覧/編集/削除の判別条件ラベル「作成者ロール：コミュニティ管理者」は実際は「対象インデックスが管理対象コミュニティに属するか」(`HarvestSettingView.get_query/_index_filter`)。
- ADMIN_RESOURCE_SYNC: 整合。**訂正**: Resyncは invenio-resourcesyncclient(`AdminResyncClient`)、Resource/Change Listは invenio-resourcesyncserver。
- ADMIN_SWORD_API: 上位整合(swordapi/swordapi/jsonld=repoリスト→System/Repo)。**要検証(PLAUSIBLE)**: JSON-LD設定の「自身が作成したレコード以外Repo×」「非自作アプリ非表示」はコードに作成者フィルタ無し(`get_query`/`create_view`)→実際は全件見える可能性。
- ADMIN_FILES: **矛盾**: Location「作成・削除」Repo×→実際は`LocationModelView.can_create/can_edit/can_delete`がSystem+Repo許可(Repo○, editも可)。bucket/fileinstance/multipart/objectversion=System専用は整合。
- ADMIN_RECORDS: 整合(System専用、RecordMetadataは削除可)。
- ADMIN_USER: **矛盾2件**: (1)sessionactivityはrepositoryリストにあり→Repo○(仕様×は誤り)。(2)ユーザーの編集/削除/(非)活性化はSystem専用(`_admin_roles=[System]`)で、Repo/Commは閲覧のみ(仕様のRepo○/Comm○は編集/削除では誤り)。user閲覧のコミュニティ絞り込みは`UserView.get_query`。
- ADMIN_SETTING: 全22画面整合。制限公開は`WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS`(既定True)でも制御。mail/webapiaccount/filepreview=System専用。
- ADMIN_LOGS: 整合(`logs/export` repoリスト→System/Repo)。
- ADMIN_MAINTENANCE: 整合(`reindex_es`非リスト→System専用)。
- ADMIN_ADVANCED: **矛盾**: profile_settingsは`role_has_access`の特別分岐で`WEKO_USERPROFILES_CUSTOMIZE_ENABLED`(既定False)を返す→Offで全員×(System含む)、Onでロールを持つ全認証ユーザー○(Repo/Comm/Contributor/General区別なし)。

### API_* 検証結果
- 共通: `require_api_auth(allow_anonymous)`, `require_oauth_scopes`(トークン使用時のみ), `roles_required`(未認証+guest_token無しは401)。
- API_ITEM: **矛盾**: `GET /api/records/`(非version)は item:read を強制しない(invenio recid list_route, permission/ESフィルタのみ)。`PUT /api/records/`は対応ハンドラ無し(recid PUT=deny_all;実編集は/deposits/redirect/<pid>)。他(v1 records等)は整合(item:read, allow_anonymous)。
- API_FILE: 全整合(ranking:read, file:read)。
- API_INDEX: 整合。guest×/○の差は`roles_required`有無由来(tree=roles_required→guest×, tree/index=GetIndex→guest○)。
- API_ACTIVITY: 整合(user:activity, allow_anonymous=False→guest×)。
- API_OPEN_SEARCH: 整合(description.xml/searchとも公開・スコープ無し)。
- API_AUTHOR: **矛盾**: 4スコープendpointの`roles_required`はCommunity Adminを含むが仕様はコミュニティ×。count=公開(スコープ無し)。
- API_REQUEST_MAIL: ファイル本体は正しい(captcha image/validate, request-mail、いずれもauthデコレータ無し・body検証)。**README TOCが誤り**(author endpointを列挙)。
- API_LOGIN: 整合(login/logout, デコレータ無し)。
- API_OA_STATUS: 整合。raw `@oauth2.require_oauth()`(トークン必須)+oa_status:update。
- API_SWORD_API: 整合(service-doc/status=require_oauth のみ; POST/PUT/DELETE=deposit:write/actions+item:create/update/delete+roles_required(WEKO_SWORDSERVER_DEPOSIT_ROLE_ENABLE), workflow時 user:activity)。
- API_RESTRICTED_ACCESS: 整合。`GET /workflow/activities`の一般ユーザー×は内部フィルタ(デコレータはauth+user:activityのみ)。

### USER_* 検証結果（過小強制/矛盾が集中）
- 前提: `check_created_id`(created_by/owner/weko_shared_ids)はロール非依存→「作成者:自分/一般×」はコード強制でなく実務前提。
- USER_ITEM_DETAIL: **過小強制/矛盾多数**: (1)公開ステータス変更`edit_permission_factory`はflg='Edit'未使用でpage_permission_factory等価→公開アイテム閲覧可な非ownerも通過。(2)リクエストメール`RequestMail.post_v1`は権限/公開チェック皆無。(3)編集`prepare_edit_item`は`get_user_roles(is_super_role=True)`で任意のコミュニティ管理者が任意アイテム編集可。(4)閲覧/削除もcomadminが自コミュニティ配下の非公開・他者アイテムを操作可(`has_comadmin_permission`)。(5)OAI owner行は匿名ハーベストで裏付け不可。エクスポート/OtherFormats=page_permission_factory準拠。
- USER_FILES_DETAIL: DL/プレビュー/情報=`check_file_download_permission`(accessrole分岐、owner+super+comadminバイパス)で整合。シークレットURL編集=`has_permission_to_manage_secret_url`(owner/shared/System+Repoのみ、comadmin除外)で整合。**過小強制**: `replace_file`/`copy_bucket`は`@login_required`も権限factoryも無し(ゲスト含め誰でも可)。
- USER_ITEM_SEARCH: 整合(`get_permission_filter`+`search_permission`("search-access")、`check_index_permissions`)。`check_permission_user`は実質no-op。
- USER_ITEM_RANKING: 整合。ranking=`@login_required`無し(ゲスト可)、`RankingSettings.is_show`でON/OFF、`get_permission_record`。検索とは根拠機構が異なる(check_created_id, search-access非依存)。
- USER_ITEM_EXPORT: 整合。`export_settings.allow_item_exporting`無効で全ロール403(仕様未記載→追記)。open_restrictedファイルはDL権限あっても除外。
- USER_WORKSPACE: 概ね整合(自作/proxyのみ, adminバイパス無し)。item_registrationの登録先候補は閲覧権限4条件と同一(一般×の専用機構無し)。
- USER_WORKFLOW_ACTIVITY: 大部分整合。Approvalの代理投稿者行はコード裏付け無し(承認はproxy無視、フロー割当依存)。投稿インデックス条件はcheck_roles(全一致)で仕様(1個以上)より厳格。
- USER_ACCOUNT_SETTING: **矛盾**: Groups作成=任意ログインユーザー、編集/削除=グループ単位所有(`Group.can_edit`→GroupAdmin)。仕様の「sys/repo/comadminのみ」と矛盾(登録/一般も可)。Sessions=`_has_admin_access`でadmin限定(仕様整合)。メール通知はconfirmed_at必須。
- USER_COMMUNITY_SUBREPOSITORY: 整合(list/view/content_policyとも`@login_required`無し・公開)。

### README doc-bug（要修正）
- L170: `ADMIN_ADVANCED_ADMIN_01.md` はリンク切れ→正: `ADMIN_ADVANCED_01.md`。
- L211-215: リクエストメールのTOCがauthor endpointを列挙(コピペ誤り)→正: captcha image/validate + records/<pid>/request-mail。
- L226: `DELETE /sword/deposit/` アンカー切れ(→`<recid>`)。

### 統合方針（access_control）
- 全ADMIN_*に「実装（アクセス制御の担保）」注記（role_has_access+ACCESS_TABLE+当該view/endpoint）を追記。明確な矛盾セル(Location, sessionactivity, user編集/削除, profile_settings, OAI harvestラベル, resyncモジュール)は実装準拠に修正。SWORD JSON-LDは要検証注記。
- API_*は認可機構(scope/roles/factory)を追記、API_ITEM(records/ PUT/scope)・API_AUTHOR(community)を修正/注記。
- USER_*は権限担保メカニズムを追記し、過小強制(公開切替/replace_file/copy_bucket/request-mail等)は「バックエンド未強制・UI依存」を明記。
- READMEのdoc-bug3件を修正。

## admin（Wave1 6群調査済 2026-07-14。item-mgmt(2_x)/indextree+webdesign(3_x,4_x)は別途）

### ADMIN_1_x（アイテムタイプ）weko-itemtypes-ui 他
- 1_1 メタデータ: view `ItemTypeMetaDataView`(endpoint itemtypesregister)。**修正**: 登録成功文言=`'Successfuly registered Item type.'`(コードのtypoママ), import成功=`'The item type imported successfully.'`, import失敗=`'Failed to import the item type.'`。強制インポートに「The property name already exists.」チェックは無く、未登録prop→`ValueError('Unregistered properties detected.')`、重複はupdated時刻比較でスキップ(duplicated_props)。model: ItemType/ItemTypeName/ItemTypeMapping/ItemTypeProperty(weko_records.models)。export=4JSON zip(ItemType_export.zip)。config多数(WEKO_ITEMTYPES_UI_*)確認済。
- 1_2 マッピング: view `ItemTypeMappingView`(itemtypesmapping)。整合。table item_type_mapping(+_version, __versioned__)。default schema jpcoar_mapping。meta_systemキー群追記可。
- 1_3 OAIスキーマ: view `OAISchemaSettingView`(schemasettings, weko-schema-ui)。**目的空欄→要記入**。処理概要が「config.pyに定義」だけで不十分→実処理: list/add/delete + REST `SchemaFilesResource.post`(/api/schemas/) + `SchemaConverter` + `WekoSchema.create`, table `oaiserver_schema`。root_name必須/name→_mapping付与/重複400。config: WEKO_SCHEMA_UI_ADMIN_LIST/UPLOAD, WEKO_SCHEMA_*_SCHEMA_NAME。
- 1_4 プロパティ: view `ItemTypePropertiesView`(itemtypesproperties)。整合。table item_type_property。保存成功「Saved property successfully.」失敗「Failed to save property.」。system_prop/billing_file_prop非表示。
- 1_5 JSON-LDマッピング: **関連モジュール誤り**→画面実体は **weko-admin `JsonldMappingView`(endpoint jsonld-mapping, category Item Types)**。weko_records(model `ItemTypeJsonldMapping`=table `jsonld_mappings`, `JsonldMapping` API), weko_search_ui(`JsonLdMapper`検証)。**table名typo `jsond_mapping`→`jsonld_mappings`、`is_delete`→`is_deleted`**。RO-Crate Mappingとは別物。template jsonld_mapping_settings.html。論理削除・__versioned__。編集制限(_is_editable承認待ち, SWORD利用でitemtype変更不可)。

### ADMIN_5_x（著者DB）weko-authors
- 横断: **target値は `author_db`/`id_prefix`/`affiliation_id` に統一**(仕様の authors/authors_prefix/... や Author/ID_Prefix/... は誤り)。著者ID採番はDBシーケンス `authors_id_seq`(max+1でない)。統合タスクは `weko_deposit.tasks.update_items_by_authorInfo`。列名 is_delete→`is_deleted`。ESインデックス `WEKO_AUTHORS_ES_INDEX_NAME`({prefix}-authors)。
- 5_1 編集: view `AuthorManagementView`+ views.py(/authors/search,add,edit,delete,gather,search_edit)。初期表示はES検索(DB直読でない)。中間table author_community_relations。言語mapにzh-cn含む。
- 5_1_3 Affiliation ID: views(/authors/search_affiliation,edit_affiliation,delete_affiliation/<id>,add_affiliation)。table authors_affiliation_settings + author_affiliation_community_relations。**config修正**: WEKO_AUTHORS_LIST_SCHEME_AFFILIATION=['ISNI','GRID','Ringgold','kakenhi','ROR','Other'](ROR追加), WEKO_AUTHORS_AFFILIATION_IDENTIFIER_ITEM_OTHER=5。
- 5_2 一括出力: view `ExportView`+Celery `tasks.export_all`。**修正**: target=author_db/id_prefix/affiliation_id。DL単一ルート `/download/Creator_export_all`(対象別URLは無い)。定数名 WEKO_AUTHORS_ID_PREFIX_EXPORT_FILE_NAME/WEKO_AUTHORS_AFFILIATION_EXPORT_FILE_NAME。Affiliation TSVヘッダ(json_idパス)が実mapping(affiliationInfo/identifierInfo/affiliationIdType/affiliationNameLang/periodStart/periodEnd)と広範に不一致。
- 5_3 一括登録: view `ImportView`。**修正**: isTarget=author_db/id_prefix/affiliation_id。redis `author_import_cache` にgroup_task保存。強制変更モードあり。periodStart/periodEnd。
- 5_4 外部著者ID Prefix: views(/authors/search_prefix,edit_prefix,delete_prefix/<id>,add_prefix)。table authors_prefix_settings + author_prefix_community_relations。**config修正**: WEKO_AUTHORS_LIST_SCHEME に e-Rad_Researcher/researchmap 追加(全13), WEKO_AUTHORS_INDEX_ITEM_OTHER=12。WEKO(idType=1)は編集不可。

### ADMIN_6_x/7_x（統計/ワークフロー）weko-admin, weko-workflow
- 6_1 運用レポート: view `ReportView`(report)。未記載メソッド: get_file_stats_output(/stats_file_output DLzip+mail), set_email_schedule, get_email_address, get_user_report_data。受信メール model `StatisticsEmail`(table stats_email_address)。スケジュールは AdminSettings `report_email_schedule_settings`(repo単位dict)。
- 6_2 フィードバックメール: view `FeedbackMailView`(feedbackmail)。API views.py(update/get_feedback_mail, get_send_mail_history, get_failed_mail, resend_failed_mail)。task `send_feedback_mail`(crontab 毎月1日0:00, key send-feedback-mail-schedules)。**修正**: `WEKO_SEARCH_MAX_FEEDBACK_MAIL=10000`(仕様100は誤り)。table feedback_email_setting(account_author NOT NULL/root_url列あり), feedback_mail_history/failed, feedback_mail_list(weko-records)。
- 6_3 サイトライセンス: view `SiteLicenseSendMailSettingsView`(sitelicensesendmail)。手動送信 views `manual_send_site_license_mail`(POST /api/admin/sitelicensesendmail/send/<start>/<end>)。**修正**: 保存は AdminSettings `site_license_mail_settings` の repo_idキーnested dict。get設定=/api/admin/get_site_license_send_mail_settings。table sitelicense_info。
- 7_1 フロー: view `FlowSettingView`(flowsetting)。整合。index/flow_detail/new_flow/del_flow/upt_flow_action。「Updated flow action successfully」。ITEM_REGISTRANT_ID=-2/REQUEST_MAIL_ID=-3。削除ガード「Cannot be deleted because flow is used.」。_check_auth(open_restricted→System)。WEKO_WORKFLOW_ACTIONS(6種)/DELETION_ACTIONS(Start/End/Approval)。OA Policy Confirmation(id6)は現行選択不可。
- 7_2 ワークフロー: view `WorkFlowSettingView`(workflowsetting)。**修正**: `WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS` 初期値=**True**(仕様Falseは誤り)。新規flows_id=uuid4。削除「Cannot be deleted because workflow is used.」。成功文言はJS付与。WorkflowRole保存。
- 7_3 ワークスペース設定: view `WorkSpaceWorkFlowSettingView`(workspaceworkflowsetting)。保存 AdminSettings `workspace_workflow_settings`(item_type_id/work_flow_id/workFlow_select_flg)。「WorkSpace WorkFlow Setting was updated.」。registrationRadio '1'=直接登録。

### ADMIN_8_x/9_x（コミュニティ/OAI-PMH）invenio-communities, invenio-oaiharvester, invenio-oaiserver
- 8_1 コミュニティ: `CommunityModelView`(table communities_community)。COMMUNITIES_LIMITED_ROLE_ACCESS_PERMIT=2。**修正**: バリデーションは create/edit両方で走る(create限定でない)。メソッドは `validate_community_id`/`_validate_input_id`(validate_input_idは存在せず)。id_userは作成時のみ設定(編集で書換なし)。CNRIハンドル登録・Catalog(jsonschema/schemaform, item_type_property id=1057)追記可。潜在バグ: COMMUNITY_ID_TOO_LONG未定義→100字超でKeyError。
- 8_2 注目のコミュニティ: `FeaturedCommunityModelView`(table communities_featured_community)。can_create/edit/delete=True。get_query絞り込み無し(権限はfactory依存)。
- 8_3 参加リクエスト: `InclusionRequestModelView`(table `communities_community_record`)。can_create/edit=False, can_delete=True。column_list(id_community,id_record,expires_at,id_user)。本文「確認中」→埋める。
- 9_1 ハーベスト: `HarvestSettingView`(harvestsettings, table harvest_settings + harvest_logs)。**修正**: ボタンはRun/Resume/Pause/Clear(「Suspected」誤記→Pause=Suspended)。Resumeは`run`再利用(専用resume無し)。作成タブは既定create_view(edit_viewでない)。repository_name unique/max20。中断=celery revoke。OAIHARVESTER_NUMBER_OF_HISTORIES=20。
- 9_2 Identify設定: `IdentifyModelView`(table oaiserver_identify)。1件のみ(can_create条件)。can_delete=False/can_view_details=False。
- 9_3 Sets: `OAISetModelView`(table oaiserver_set)。**修正**: **can_delete=False(削除不可)**→目的の「削除」修正。edit_formで`del form.spec`(spec編集不可)。「oaiserver」→`oaiserver_set`。get_query絞り込み無し(権限factory依存)。

### ADMIN_10_x/11_x（Resource Sync/Records）
- 10_1 Resource List: `AdminResourceListView`(resource_list, invenio-resourcesyncserver)。整合。table resourcelist_indexes。get_list_resourceはuser絞り込み(全件は管理者のみ)。
- 10_2 Change List: `AdminChangeListView`(change_list)。**修正**: 一覧route=/get_all(get_list)。create/updateはHandler.save()(create/updateメソッド無し)。table changelist_indexes。
- 10_3 Resync: `AdminResyncClient`(resync, **invenio-resourcesyncCLIENT**)。**修正**: create_resync(重複チェック無し)。Sync=run_sync, Import=run_import, ON/OFF=toggle_auto。task resync_sync。table resync_indexes/resync_logs。INVENIO_RESYNC_SAVE_PATH=/tmp/resync/。
- 11_1 永続識別子: invenio-pidstore(**未vendored**、upstream依存)。table pidstore_pid, ModelView。pid_type使用実在(oai/depid/recid/parent/actid/doi/hdl/hvstid)。ソース照合不可の旨。
- 11_2 レコードメタデータ: `RecordMetadataModelView`(table records_metadata, record_adminview)。can_create/edit=False, can_delete=True。**修正**: soft_delete/restoreは **weko_records_ui.utils** 由来(weko_recordsでない)。**v0.9.22の「必ずエラー」記述は古い→v2.0.2で実装済み**(soft_delete/restore動作、is_lockedハンドリング)。status=hybrid property(recid pid照会)。

### ADMIN_12_x（ファイル）invenio-files-rest/admin.py
- 12_1 バケット: `BucketModelView`(table files_bucket)。can_create/edit=True,can_delete=False。作成はLocationフィールド無しで失敗(既知)。config FILES_REST_STORAGE_CLASS_LIST/DEFAULT_STORAGE_CLASS='S'。
- 12_2 ファイルインスタンス: `FileInstanceModelView`(table files_files)。全can_*=False(閲覧のみ)。@action verify_checksum→`verify_checksum.delay`「Fixity check(s) sent to queue.」。objectsフィルタはrelationship展開。
- 12_3 ロケーション: `LocationModelView`(table files_location)。**can_create/edit/delete=System+Repository両方**(access_controlの矛盾はこれで確定=Repo○)。repo管理者はdefault=Falseに限定(get_query)。**修正**: 「https://で始まる」検証はS3 Virtual Host型のみ。s3_signature_versionは作成時Noneにされる(選択値破棄)。config FILES_REST_LOCATION_TYPE_LIST/_S3_PATH_VALUE/_S3_VIRTUAL_HOST_VALUE。role env INVENIO_ROLE_SYSTEM/REPOSITORY。
- 12_4 マルチパートオブジェクト: `MultipartObjectModelView`(table files_multipartobject)。全can_*=False。**注意**: Repo○のロール表はコード裏付け無し(can_*/get_query無し、admin factory依存)→要検証注記。
- 12_5 オブジェクトバージョン: `ObjectModelView`(table files_object)。全can_*=False(閲覧のみ)。

### ADMIN_2_x（アイテム管理）
- 2_1 一括更新: view `ItemManagementBulkUpdate`(**weko-records-ui.admin**, endpoint items/bulk/update)。**weko-bulkupdateはスタブで使用しない**。実装=weko-records-ui(view)+weko-search-ui(検索)+weko-deposit(REST更新: /api/deposits/redirect→items→publish)。template `WEKO_THEME_ADMIN_ITEM_MANAGEMENT_TEMPLATE`(management_type='update')。WEKO_RECORDS_UI_LICENSE_DICTは実体list。新バージョン作成あり(edit_mode='upgrade')。table item_metadata(+_version __versioned__)。
- 2_2 一括削除: view `ItemManagementBulkDelete`(weko-search-ui, items/bulk/delete, **GET/PUT**。削除はPUT)。`/check`エンドポイントで確認ダイアログ・DOI/編集中除外(get_doi_items_in_index+get_editing_items_in_index)。削除=`delete_records`(utils)→`soft_delete`(weko-records-ui.utils)。publish_status=`PublishStatus.DELETE.value`="-1"(**weko-schema-ui**のenum、JSON内文字列)、全版PID status=DELETED。再帰はview側(recursively param)。複数index所属はunlink。副作用: FeedbackMailList/RequestMailList削除, bucket削除, ES更新, ITEM_BULK_DELETEログ。
- 2_3 一括エクスポート: view `ItemBulkExport`(weko-search-ui, index/export_all/cancel_export/download/check_export_status)。**修正**: `WEKO_SEARCH_UI_BULK_EXPORT_EXPIRED_TIME=1440`(仕様7は誤り。7は`WEKO_SEARCH_UI_EXPORT_FILE_RETENTION_DAYS`)。WEKO_SEARCH_UI_*はweko-search-ui/config(weko_adminでない。WEKO_ADMIN_CACHE_PREFIXのみweko-admin)。`get_last_item_id`=views.py, `get_itemtypes`=**weko-itemtypes-ui/views.py**。task `export_all_task`/`write_files_task`。DLは`/download`(FileInstance.get_by_uri, export-all.zip, メタのみ)。session lifetime≥86400ゲート。状態はRedis per-user。
- 2_4 インポート: view `ItemImportView`(weko-search-ui, items/import, SPA, template weko_search_ui/admin/import.html)。**修正メソッド名**: `check_tsv_import_items`(check_import_itemsでない), `import_item`(import_itemsでない), `make_stats_file`(make_stats_tsvでない)。重複チェックは weko-items-ui `check_duplicate`/`is_duplicate_item`(DOI→Title→ResourceType→Author, publish_status='0'非版のみ)。メタデータ補完は weko-items-autofill `fetch_metadata_by_doi`(CrossRef/DataCite/CiNii/JaLC/医中誌)。関連module追加: weko-deposit/weko-items-ui/weko-workflow/weko-index-tree/weko-authors/invenio-pidstore。BULK_IMPORT config family無し。file形式は WEKO_ADMIN_OUTPUT_FORMAT。
- 2_5 RO-Crateインポート: view `ItemRocrateImportView`(weko-search-ui, items/rocrate_import, template rocrate_import.html, /all_mappings)。**修正**: table `jsonld_mappings`(単数jsonld_mappingは誤り, +_version), model `ItemTypeJsonldMapping`(weko-records), API `JsonldMapping`, 管理UI `SwordAPIJsonldSettingsView`(weko-admin, swordapi/jsonld)。wk:キーは`JsonLdMapper`(weko-search-ui/mapper.py)でパース(ハードコード。exportにtypo wk:metadaAutoFill)。ro-crate/sword.json両対応(@contextで判定)。wk:textExtraction→ES抽出skip。check=`check_jsonld_import_items`。関連module追加: weko-records/weko-admin/weko-items-autofill/weko-swordserver。config WEKO_ITEM_ADMIN_ROCRATE_IMPORT_TEMPLATE等。

### ADMIN_3_x/4_x（インデックスツリー/ウェブデザイン）
- 3_1 ツリー編集: admin `IndexEditSettingView.index`(AJAX→REST `IndexTreeActionResource.get`→`Indexes.get_index_tree`)。追加/編集/削除=`IndexActionResource.post/put/delete`→`Indexes.create/update`, `perform_delete_index`(論理削除 is_deleted)。移動=`IndexTreeActionResource.put`→`Indexes.move`。キャッシュ`save_index_trees_to_redis`。**修正**: 再帰フラグ番号誤り→正=#10 recursive_public_state/#18 recursive_coverpage_check/#21 biblio_flag/#23 recursive_browsing_role/#25 recursive_browsing_group/#27 recursive_contribute_role/#29 recursive_contribute_group(#8/#16に再帰なし,#29欠落)。カラム名 recursive_coverpage_state→`recursive_coverpage_check`。欠落列 is_deleted/owner_user_id/cnri/index_url/harvest_spec。config `WEKO_INDEXTREE_GAKUNIN_GROUP_DEFAULT_*_PERMISSION`は**weko-accounts/config.py**。関連module追加 weko_accounts/weko_handle/weko_workflow/weko_logging。
- 3_2 雑誌情報: admin `IndexJournalSettingView`(indexjournal, weko-indextree-journal, table journal)。REST `JournalActionResource.post/put/delete`→`Journals.create/update/delete`。**修正**: 関連モジュールに weko-index-tree/weko-records 追加。updateは**index_idベース検索**。schemaは`/admin/indexjournal/jsonschema`でfetch。欠落列 is_output/title_url/title_id/owner_user_id/first_author/date_monograph_*/monograph_*/deleted等。model `Journal_export_processing`。required差異(date_first_issue_online非必須)。
- 3_3 カスタムソート: admin `ItemManagementCustomSort`(items/custom_sort, weko-search-ui)+`ItemManagementBulkSearch`。保存 POST /admin/items/custom_sort/save→`save_sort`→`Indexes.set_item_sort_custom`(weko-index-tree)。**修正**: 「None変換」→非数値/≤0は除外。`get_custom_sort`は`SearchSetting`(weko_search_ui/api.py。query.pyでない)。保存時ES同期は無効(コメントアウト、クエリ時にDB列適用)。ロールガード無し(admin factory依存)。table列 `Index.item_custom_sort`(JSONB)。template `WEKO_THEME_ADMIN_ITEM_MANAGEMENT_TEMPLATE`(weko-theme)。
- 4_1 ウィジェット: admin `WidgetSettingView`(widgetitem, weko-gridlayout)。index_view/details_view/edit_view/create_view。ロック `WidgetItemServices.get_locked_widget_info`(session key locked_widget_key_{}, WEKO_ADMIN_DEFAULT_LIFETIME分で失効)。編集保存=`WidgetItemServices.update_by_id`。削除=論理削除(is_deleted), `is_used_in_widget_design`チェック。**修正**: ウィジェット種別は**DB駆動**(table widget_type, `WidgetType.get_all_widget_types`, CLI insert_widget_type_to_db)でコード定数でない。一覧はリポジトリ権限スコープ(get_query, super-roleのみ全件)。関連module追加 invenio-communities/weko-admin/weko-index-tree/weko-items-ui/weko-theme。config WEKO_GRIDLAYOUT_WIDGET_DEFAULT_COLOR='#4169E1'等。
- 4_2 ページレイアウト: admin `WidgetDesign.index`(widgetdesign)。**修正**: レイアウト保存クラス名誤り→`WidgetDesignServices.update_widget_design_setting`(WidgetDesignPageServicesでない)。ページ保存は中間`WidgetDesignPageServices.add_or_update_page`→`WidgetDesignPage.create_or_update`。model WidgetDesignSetting/WidgetDesignPage/WidgetDesignPageMultiLangData。

### ADMIN_13_x（ユーザー管理）Wave2
- 13_1 アクセス_ロール: `invenio_access.admin.ActionRolesView`(model ActionRoles, table access_actionsroles)。Action選択肢は登録済アクション由来。
- 13_2 アクセス_システムロール: `ActionSystemRolesView`(table access_actionssystemroles)。**修正**: フィールドは `role`でなく`role_name`。
- 13_3 アクセス_ユーザー: `ActionUsersView`(table access_actionsusers)。Emailは`user.email`リレーション。
- 13_4 連結アカウント識別子: **修正**: 実体は`invenio_oauthclient.admin.UserIdentityView`(model UserIdentity, table `oauthclient_useridentity`, can_create=False)。invenio_accounts/accounts_useridentityは誤り。
- 13_5 連結アカウントトークン: `invenio_oauthclient.admin.RemoteTokenView`(table oauthclient_remotetoken)。
- 13_6 連結アカウント: **修正**: 目的の対象テーブルは`oauthclient_remoteaccount`(RemoteAccountView, oauthclient_remotetokenは誤り)。
- 13_7 OAuthアプリトークン: `invenio_oauth2server.admin.TokenView`(table oauth2server_token, can_create=False)。**修正**: 処理概要の`invenio_files_rest.admin.TokenView`はコピペ誤り→invenio_oauth2server.admin。
- 13_8 OAuthアプリ: `invenio_oauth2server.admin.ClientView`(table oauth2server_client, can_create=False)。**修正**: 同様に`invenio_files_rest.admin.ClientView`誤り→invenio_oauth2server.admin。
- 13_9 ロール: `invenio_accounts.admin.RoleView`(table accounts_role)。**修正**: 処理概要「access_actionssystemrolesに保存」→`accounts_role`。after_model_change で ACCOUNTS_WORKFLOW_ROLE_HIDE_FILTER 時 workflow_userrole 追加。
- 13_10 セッションアクティビティ: `SessionActivityView`(table accounts_user_session_activity, can_create/edit/view_details=False)。現在セッションは削除不可。
- 13_11 ユーザー: `invenio_accounts.admin.UserView`(table accounts_user)。編集/削除/(非)活性化は`_admin_roles=[System]`でSystem専用。get_queryは`WEKO_PERMISSION_SUPER_ROLE_USER`(System+Repository)で全件、それ以外はコミュニティ絞り込み。**追記**: フォームにGroupsフィールド(role dropdownは_groups_除外)。
- 13_12 ユーザープロファイル: `weko_user_profiles.admin.UserProfileView`(table userprofiles_userprofile)。can_edit/delete=System専用(property)。表示列は`WEKO_USERPROFILES_FORM_COLUMN`で実行時フィルタ。edit_viewでposition→role再割当(get_role_by_position)。

### ADMIN_14_x（設定）Wave2
- 14_1 アイテム表示: `weko_records_ui.admin.ItemSettingView`。AdminSettings `items_display_settings`(items_display_email/item_display_open_date)。config EMAIL_DISPLAY_FLG等。
- 14_2 インデックスリンク表示: `weko_index_tree.admin.IndexLinkSettingView`。model IndexStyle(index_style, index_link_enabled)。「IndexLink flag was updated.」
- 14_3 言語表示: 画面`weko_admin.admin.LanguageSettingView`+API views get_lang_list/save_lang_list。model AdminLangSettings(admin_lang_settings)。
- 14_4 PDFカバーページ: 画面`PdfCoverPageSettingView.index`(GET)。**保存主体は`weko_records_ui.views.set_pdfcoverpage_header`(POST /admin/pdfcoverpage)**。model PDFCoverPageSettings(pdfcoverpage_set id=1)。
- 14_5 ランキング表示: `weko_admin.admin.RankingSettingsView.index`(POST)。model RankingSettings(ranking_settings)。**修正**: Deleteは`RankingSettings.delete`を呼ばない(クライアント側で入力破棄・再表示、DB削除なし)。
- 14_6 統計情報表示: `StatsSettingsView.index`。AdminSettings `display_stats_settings`(サブキー display_stats。「カラム」でなくレコード名)。
- 14_7 画面背景色: `StyleSettingView.index`。**修正**: 保存はPUTでなく**POST**。_variables.scss($body-bg)書換。権限 update-style-action。関連module weko_admin追記。
- 14_8 識別子: `IdentifierSettingView`(ModelView, can_delete=False)。model Identifier(doi_identifier)。全角チェック。
- 14_9 アイテム一括出力: `ItemExportSettingsView`。AdminSettings `item_export_settings`(allow_item_exporting/enable_contents_exporting)。最大件数は`weko_items_ui.config.WEKO_ITEMS_UI_DEFAULT_MAX_EXPORT_NUM=100`(+_PER_ROLE)。
- 14_10 ログ解析: `LogAnalysisSettings.index`。table loganalysis_restricted_ip_address/loganalysis_restricted_crawler_list。判定 api.is_restricted_user/_is_crawler(CRAWLER_REDIS_DB)。
- 14_11 検索設定: `SearchSettingsView.index`。model SearchManagement(search_management)。**修正**: Search Author Settingは search_management でなく AdminSettings `items_display_settings`(items_search_author)。既定は config ITEM_SEARCH_FLG。IndexツリーWidth/HeightはIndexStyle。
- 14_12 ファセット検索: `FacetSearchSettingView`(ModelView)。model FacetSearchSetting(facet_search_setting, is_open/aggregations列)。save/remove_facet_search→`store_facet_search_query_in_redis`。**修正**: 選択削除は`weko_gridlayout...action_delete`でなくFacetSearchSettingView自身のaction_delete。
- 14_13 サイト情報: `SiteInfoView.index`+views update_site_info/get_site_info。model SiteInfo(site_info)。**修正**: トラッキングIDは admin_setting でなく`site_info.google_tracking_id_user`列。AddThis列は非推奨(未使用)。OGP画像はupdate_ogp_image(/api/admin/ogp_image)。roles_required(System,Repo)。
- 14_14 サイトライセンス: `SiteLicenseSettingsView.index`。`weko_records.api.SiteLicense.update`。**追記**: IP範囲は別table`sitelicense_ip_address`(SiteLicenseIpAddress)。除外アイテムタイプは item_type_name.has_site_license。サブリポ対応(get_records)。
- 14_15 サイトマップ: 画面`weko_sitemap.admin.SitemapSettingView`。Run(POST /update_sitemap)→Celery `weko_sitemap.tasks.update_sitemap`。状態は get_task_status。config WEKO_SITEMAP_*。
- 14_16 メール送信: `invenio_mail.admin.MailSettingView`(**綴りMailSettingVIewは誤り**)。model MailConfig(mail_config)。「ドメイン」列は`mail_local_hostname`。メッセージ確認済。
- 14_17 WebAPIアカウント: `weko_admin.admin.WebApiAccount`+views get_curr_api_cert/save_api_cert_data。model ApiCertificate(api_certificate, PK api_code)。**修正**: 関数名`validate_certification`(calidate_certificationは誤り)。接続確認はcrf(CrossRef)のみ、oaaは確認なし。保存は utils.save_api_certification。入力タイプ取得 get_api_cert_type。
- 14_18 ファイルプレビュー: `FilePreviewSettingsView`。AdminSettings `convert_pdf_settings`。config FILES_REST_DEFAULT_PDF_SAVE_PATH(=tempfile.gettempdir())/FILES_REST_DEFAULT_PDF_TTL=3600。cleanup task check_file_storage_time。
- 14_19 Shibboleth: `weko_accounts.admin.ShibSettingView`+views._adjust_shib_admin_DB。**修正**: 有効/無効は config だけでなく AdminSettings `shib_login_enable`(shib_flg)に永続化。AdminSettings default_role_settings/attribute_mapping/blocked_user_settings。CLI weko-admin admin_settings mapping_update。
- 14_20 制限公開: `RestrictedAccessSettingView`(restricted_access)。save `views.save_restricted_access`→`utils.update_restricted_access`。AdminSettings `restricted_access`(item_application/preview_workflow_approval_enable/edit_mail_templates_enable/display_request_form/password_enable/secret_URL_file_download/content_file_download/usage_report_workflow_access/terms_and_conditions/error_msg)。**追記**: 画面/メニュー表示は`WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS`(既定True, ext.py)、セクション表示は`WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG`(既定False)。無期限=WEKO_ADMIN_RESTRICTED_ACCESS_MAX_INTEGER=9999999。edit_mail_templates_enable=False保存でreset_flow_action_roles_restricted_access。
- 14_21 その他: `weko_records_ui.admin.InstitutionNameSettingView`。model InstitutionName(institution_name)。get_google_scholar_metaで使用。仕様は正確。
- 14_22 メールテンプレート編集: **修正**: `WEKO_ADMIN_USE_MAIL_TEMPLATE_EDIT`は既定False かつ**未参照(デッド)**。実ゲートは AdminSettings restricted_access `edit_mail_templates_enable`(ext.pyでendpoint mailtemplates非表示)。画面は`invenio_mail.admin.MailTemplatesView`(mailtemplates, index/save_mail_template/delete_mail_template)。model MailTemplates/MailTemplateUsers/MailConfig。関連module=invenio-mail。処理概要/関連モジュール空欄→要記入。
- 14_23 CRIS連携: 設定画面は**weko-admin `CrisLinkageSettingView`(cris_linkage)**(仕様のweko-items-uiのみは不足)。AdminSettings `researchmap_linkage_settings`(researchmap_cidkey_contents/pkey_contents/merge_mode)。save_keys/save_merge_mode。task `weko_items_ui.tasks.bulk_post_item_to_researchmap`。config WEKO_ITEMS_UI_CRIS_LINKAGE_RESEARCHMAP_*(weko-items-ui)。merge_modes=WEKO_ADMIN_SETTINGS_RESEARCHMAP_MERGE_MODES。

### ADMIN_15/16/17/18 + README Wave2
- 15_1 ESインデックス: `ReindexElasticSearchView`(reindex_es, superuser_access限定)。/reindex(is_db_to_es param)/is_reindex_running。Celery task reindex→utils.elasticsearch_reindex。AdminSettings elastic_reindex_settings(has_errored)。
- 16_1 SWORD API TSV/XML: `SwordAPISettingsView`(swordapi)。AdminSettings `sword_api_setting`(active/registration_type/workflow/duplicate_check)。重複チェック表示は WEKO_ITEMS_UI_ENABLE_DUPLICATE_CHECK。
- 16_2 SWORD API JSON-LD: `SwordAPIJsonldSettingsView`(ModelView, swordapi/jsonld)。model **SwordClientModel(table `sword_clients`複数形。sword_clientは誤り)**。WebAPI優先は WEKO_ITEMS_AUTOFILL_API_LIST。
- 17_1 エクスポート(監査ログ): `weko_logging.admin.ExportLogAdminView`(logs/export)。/export/check_export_status/cancel_export/download(export_log.zip)。task export_all_user_activity_logs。**修正**: get_export_status→`UserActivityLogUtils.get_export_task_status`。関連module weko_search_ui(check_celery_is_run)、weko_admin依存は要確認。
- 18_1 プロフィール設定編集: `weko_admin.admin.ProfileSettingView`(Advanced, Profile Settings)+API send_profile_settings_save(/api/admin/profile_settings/save, roles_required System/Repo)。AdminSettings `profiles_items_settings`。format `USERPROFILES_FORMAT_OPTION_LIST`(text/select/identifier/phonenumber/position(other))。**修正**: 初期値誤り(item1=position(other)[otherPosition誤], item2=phonenumber[identifier誤], position options=WEKO_USERPROFILES_POSITION_LIST[1:], item13-16 visible=False[True誤], university label「大学・機関名」)。メニュー自体が`WEKO_USERPROFILES_CUSTOMIZE_ENABLED`(既定False, ext.py)でゲート。関連module weko-user-profiles追記。RESTRICTED_ACCESS_05と重複。
- README: 1行のみ→管理画面(/admin)のメニューカテゴリ概要を記入。

### admin 共通
- 更新履歴のGitHub参照が軒並み v0.9.22 / feature/weko の古い行を指す(値は概ね現行一致)。
- ロール表の「コミュニティ/サブリポ管理者○」はModelView側get_query実装が無いものが多く、権限はadmin factory(role_has_access/WEKO_ADMIN_ACCESS_TABLE)依存(access_control参照)。
- 統合方針: 各fileに実view/endpoint/method・configキー・table名を追記、明確な矛盾(文言/config値/メソッド名/モジュール帰属/v0.9.22古記述)を実装準拠に修正。行番号は載せない。

## user（8並列調査 2026-07-14）要点（矛盾中心）
- 1_1 簡易検索: view `weko_search_ui.views.search`(route /search/index)。factory `query.default_search_factory`(=es_search_factory)。`sort_meta_data_by_options`は**async**(weko_records.utils)。権限`get_permission_filter`。
- 1_2 詳細検索: `default_search_factory._get_detail_keywords_query`。キー対応は`WEKO_SEARCH_KEYWORDS_DICT`。exact_title_match分岐あり。
- 1_3 インデックス検索: `weko_theme.views.index`→`get_weko_contents`→`get_index_link_list`。REST `IndexTreeActionResource.get`(rest.getは略記)。factory `item_path_search_factory`。`get_journal_info`はweko_search_ui.utils。
- 1_4 ファセット検索: **矛盾**: aggは`RECORDS_REST_FACETS`(空dict)でなく、customized`default_facets_factory`→`weko_admin.utils.get_facet_search_query`→Redis(FacetSearchSetting)。7デフォルトはDB seed。BUCKET_SIZE=1000。
- 1_5 RSS: `/api/rss.xml`(weko_index_tree.views.get_rss_data)/`/rss/records`(weko_gridlayout)。builder`weko_gridlayout.utils.build_rss_xml`。**矛盾**: count>100は100でなく既定20にリセット。RSS1.0。config WEKO_INDEX_TREE_RSS_*。
- 2_1 一覧形式: `Index.display_format`は'1'一覧/'2'目次の2値。defaults=`SearchManagement`+`WEKO_ADMIN_MANAGEMENT_OPTIONS`(searchメソッドは無し→SearchSetting.get_results_setting)。`sort_meta_data_by_options`はweko_records.utils。改行はrenderの`crtf`。関連module追加weko_records/weko_admin/weko_theme。
- 2_2 目次形式: `weko_search_ui.rest.get`→`get_heading_info`(subitem_heading_banner_headline/headline/language)。ページキーは`pageStart`/`pageEnd`(camelCase)。**矛盾**: 表示形式は2種(list/contents)でJournalは別機能。
- 2_3 雑誌情報: `get_journal_info`(weko_search_ui.utils)。table journal(is_output)。KBART出力task `export_journal_task`(weko-indextree-journal)。**矛盾**: ファイル名prefixは`OAISERVER_REPOSITORY_NAME`(WEKO固定でない)。is_outputはKBART出力をフィルタしない(画面表示のみ)。beatはinstance.cfg。
- 2_4 一括出力: `weko_items_ui.views.export`(/items/export)。**矛盾**: ファイル名`recid_{record_id}.zip`(recod_は誤植)。`WEKO_ITEMS_UI_EXPORT_MAX_FILE_SIZE`/JS`getExportItemsMetadata`は存在せず。NFKD/MarkupSafe/&EMPTY&はTSVで無効(escape_newlineのみ)。RO-Crate mapper=`JsonLdMapper`(weko_search_ui.mapper)、`JsonldMapping`はweko_records.api(table jsonld_mappings)。管理設定AdminSettings`item_export_settings`。上限WEKO_ITEMS_UI_DEFAULT_MAX_EXPORT_NUM=100(+_PER_ROLE)。bibtex検証`/items/validate_bibtext_export`。
- 3_1 メタデータ表示: `weko_records_ui.views.default_view_method`。**矛盾**: 関連モジュール`weko_detail`は存在しない(weko_records_ui+weko_deposit)。`WEKO_DEPOSIT_SYS_CREATOR_KEY`にcreator_type/creator_name_type追加済。config WEKO_RECORDS_UI_DEFAULT_MAX_WIDTH_THUMBNAIL=100。
- 3_2 コンテンツファイル管理: `permissions.check_file_download_permission`(内部__check_user_permission)。**矛盾**: 定数`MAX_DOWNLOAD_SIZE_AT_ONE_TIME`/`DOWNLOAD_SIZE_IN_ONE_PART`は存在せず(実体はWEKO_RECORDS_UI_S3_TRANSFER_MULTIPART_THRESHOLD/CHUNKSIZE=S3転送用)。DISPLAY_FLAGはweko_admin、FILE_SISE_PREVIEW_LIMITはweko_items_ui(format別dict)。models file_onetime_download/file_secret_download/file_url_download_log。
- 3_2_1 ファイル管理機能: `api.get_file_place_info`/`replace_file_bucket`/`copy_bucket_to_s3`。routes views `/get_file_place`/`/replace_file`/`/get_bucket_list`/`/copy_bucket`。
- 3_3 バージョン管理: `default_view_method`のPIDVersioning(active_versions/all_versions)。draft除外。
- 3_4 引用情報: `CiteprocSerializer`+`RecordSchemaCSLJSON`。既定style`aapg-bulletin`。render filter`weko_records_ui.views.citation`。
- 3_5 統計情報: `record_viewed`送出。`QueryRecordViewCount`/`QueryFileStatsCount`。file_downloadedはget_uriとsend_object 2箇所。
- 3_6 共有: **重大矛盾**: AddThis/mendeley/citeulike/+は現行share.htmlに無い→Facebook/Twitter(X)/Printのみ(native SDK)。addthis_widget.jsは孤立。要書き換え。
- 3_7 エクスポート: `weko_records_ui.views.export`(/records/<pid>/export/<format>)。`SchemaTree(record,schema_name)`。OAI error `get_error_code_msg`等。BIBTEX`WekoBibTexSerializer`。
- 3_8 Google Scholar: `weko_records_ui.utils.get_google_scholar_meta`(target_map一致)。追加meta多数(citation_doi/issn/pdf_url/dissertation_institution等)。config WEKO_RECORDS_UI_GOOGLE_SCHOLAR_OUTPUT_RESOURCE_TYPE。
- 3_9 Google Dataset: **矛盾**: 関数名`get_google_detaset_meta`(typo。get_google_dataset_metaでない)。出力はdict。`WEKO_RECORDS_UI_GOOGLE_DATASET_DISP_FLG`はデッド(未使用)。gate はScholar resource_type config。
- 3_10 所属コミュニティ: `default_view_method`→`GetCommunity.get_community_by_root_node_id`(weko_workflow)→Community(invenio_communities, table communities_community)。関連module追加。record.naviループ。
- 3_11 リクエスト機能: **矛盾**: config`DISPLAY_REQUEST_FORM`は存在せず→AdminSettings`restricted_access.display_request_form`。送信元はCcでなく別通知メール。table request_mail_list(weko_records)。REST RequestMail/CreateCaptchaImage/CaptchaAnswerValidation。config WEKO_RECORDS_UI_CAPTCHA_*/REQUEST_MESSAGE/NOTIFICATION_MESSAGE。
- 3_12 メールアドレス入力: `fd.file_download_onetime`→`process_onetime_file_download`→`_download_file`。**矛盾**: メールはクエリでなくPOST body(mail_address/input_password)。password gateは`restricted_access.password_enable`。model FileOnetimeDownload。
- 3_13 アイテム利用申請: table `item_application`(weko_records)。`api.get_item_provide_list`。gate AdminSettings`restricted_access.item_application`(item_application_enable/application_item_types)。**矛盾**: 処理概要「リクエスト送信先」は誤り(item_application)。
- 4_1 アクティビティ一覧: `WorkActivity.get_activity_list`/`filter_conditions`。download/clear_activitylog。DELETE_ACTIVITY_LOG_ENABLE(instance.cfg)。get_server_date=/api/admin/get_server_date。
- 4_2 ワークフロー一覧: `get_new_activity_id`(A-{}-{})。lock/unlock_activity(redis workflow_userlock_activity_/workflow_locked_activity_)。new_activity→WorkFlow.get_workflow_list/get_workflows_by_roles。
- 4_3 ワークフロー: 「Workflow setting does not exist.」(weko_items_ui.views)。
- 4_4 Item Registration親: 概要。関連module空欄→weko_workflow/weko_items_ui/weko_deposit。
- 4_5 ファイルアップロード: **矛盾**: `FILES_REST_USE_MULTIPART_UPLOAD`/`FILES_REST_RESUME_CHUNK_SIZE`は存在せず→実体`FILES_REST_MULTIPART_CHUNKSIZE_MIN(5MiB)/MAX(5GiB)/MAX_PARTS(10000)/EXPIRES(4日)`。WEKO_DEPOSIT_FILESIZE_LIMIT=2MB。
- 4_6 メタデータ入力: WEKO_ITEMS_UI_SAVE_FREQUENCY=600000ms(10分)。autofill list=WEKO_ITEMS_AUTOFILL_API_LIST(5種)。重複`is_duplicate_record`(weko_items_ui.utils, view /330)。TO_BE_USED既定[]、instance.cfgで6種。
- 4_7 代理投稿: WEKO_ITEMS_UI_PROXY_POSTING=False。`get_search_data`/`validate_user_info`(views)。`check_authority_action`(weko_workflow)。autocomplete/get_autofill_dataはJS(app.js)。
- 4_8 フィードバックメール: table feedback_email_setting/history/failed(weko_admin)、**feedback_mail_listはweko-records**。task send_feedback_mail。config WEKO_ADMIN_NUMBER_OF_SEND_MAIL_HISTORY=20/FAILED_MAIL=10, WEKO_SEARCH_MAX_FEEDBACK_MAIL=10000。
- 4_9 インデックス指定: `get_pid_and_record`(weko_workflow.utils)。`iframe_items_index`/`update_index_tree_for_record`(weko_items_ui)。`WekoDeposit.commit`。エラーはJS(main.bundle.js)。※weko-workspace登録経路も存在。
- 4_10 Identifier Grant: action_id 7 endpoint identifier_grant。DOI検証`check_doi_validation_not_pass`等。IDENTIFIER_GRANT_LIST/SUFFIX_METHOD/WEKO_SERVER_CNRI_HOST_LINK/DOI_VALIDATION_INFO*。**矛盾/追記**: `doi_identifier`テーブルはweko-admin(Identifier)。実DOI付与`saving_doi_pidstore`(Approval時)。CNRIは`register_hdl`→`Handle.register_handle`。IdentifierHandleはweko_workflow.utils。
- 4_11 Item Link: action_id 5 item_link。`ItemLink.get_item_link_info`(weko_records.api)。table item_reference。**矛盾**: src_item_pid/dst_item_pidは`String(255)`(整数でない、複合PK)。
- 4_12 OA Policy Confirmation: action_id 6 oa_policy。**config定義のみでWEKO_WORKFLOW_ACTIONSに含まれず、views.pyに処理分岐無し(非対応)**。残存はcli seedとWEKO_WORKFLOW_OAPOLICY_SEARCHのみ。
- 4_13 Approval: action_id 4 approval。`next_action`/`saving_doi_pidstore`/`end_activity`(weko_workflow.api)。FeedbackMailList/RequestMailList/ItemApplication.update_by_list_item_id(weko-records)。
- 4_14 メールアドレス入力: `fd.file_download_onetime`/`_download_file`。permissions.check_file_download_permission/check_open_restricted_permission。「Could not download file.」「Please input email address.」。
- 4_15 End画面: action_id 2 end_action。`end_activity`。
- 4_16 Item Registration:コンテンツ未登録制限公開: weko_items_ui(no_file_approval.js, iframe/item_edit.html is_no_content_item_application)。API /workflow/get_item_application/<id>。model ItemApplication(weko_records)。**矛盾**: 「Request Email Addresses do not exist.」はソースに存在せず(要文言確認)。
- 4_17 Item Registration:リクエストメール: weko_items_ui(request_maillist.js, edit.html)。display_request_form(AdminSettings restricted_access,既定False)。table request_mail_list(weko_records)。「Duplicate Email Addresses.」「Invalid email format.」実在。「Request Email Addresses do not exist.」不在(要確認)。
- 5_1 コミュニティ: `invenio_communities.views.ui.community_list`(route /c/list/)/view(/c/<id>/)。?view=weko未使用。sort['title','ranking']。**矛盾**: カタログ2項目めはcontributors(寄与者)で提供機関でない。thumb 256x256。
- 5_2 コンテンツポリシー: `content_policy`(/c/<id>/content_policy/, @pass_community)。table communities_community.content_policy。
- 6_1 ランキング: `weko_items_ui.views.ranking`(/items/ranking)。**矛盾**: `invenio_stats.utils`(util誤)。ランキングは**リクエスト毎にESからライブ算出**(日次バッチ集計でない)。RankingSettings(ranking_settings)。config WEKO_ITEMS_UI_RANKING_*。範囲1-30/1-3650/1-100はUIのみ。
- 7_1 ファイルアップロード: **矛盾**: weko-items-uiに大容量uploadタブは無い。multipartはinvenio-files-rest(ObjectResource multipart_*)、UIはdeposit form(ng-file-upload)。/items/uploadはメタデータImport。config FILES_REST_MULTIPART_*。task merge_multipartobject。
- 7_2 言語切替: **矛盾**: route`/lang/<lang_code>`でなく`/accounts/settings/lang/<lang_code>`(weko_admin.views.custom_set_lang)。無効はGET404/POST400。model AdminLangSettings。default設定はset_default_language。
- 9_1 Cookie: config`ENABLE_COOKIE_CONSENT`(既定False, weko_theme)。Klaro v0.7.16。**矛盾**: 対象サービスはAddThisでなくFacebook/X(+GA必須)。
- 11_1 researchmap連携: **矛盾**: `create_jwt`(creare_jwt誤)。BASE_URL/HOST既定は`api-trial.researchmap.jp`(api.researchmapでない)。beat crontab(hour=0,minute=0)。model CRISLinkageResult(cris_linkage_result)。
- 8_1 サインアップ: **帰属矛盾**: 画面/文言はFlask-Security(SECURITY_MSG_*)由来でinvenio_accountsでない。登録view=flask_security.views.register(/signup/)。send_security_email celeryはACCOUNTS_USE_CELERY依存。6文字最小はFlask-Securityハードコード。
- 8_2 ログイン: view=flask_security.views.login(/login/)。SessionActivity(accounts_user_session_activity)。**矛盾**: organization_nameはinvenio_accounts側(綴り`orgniazation_name`)でweko_accountsでない。文言はFlask-Security。config WEKO_ACCOUNTS_SHIB_*(INST/DP別キー実在)。weko_accounts実view(index/shib_login/shib_sp_login等)。
- 8_3 パスワードリセット: view=flask_security.views.forgot_password(/lost-password/)/reset_password(/reset/<token>)。文言8種Flask-Security。
- 8_4 プロフィール設定: `weko_user_profiles.forms.ProfileForm`+`views.profile`(/account/settings/profile/)。**訂正**: `handle_profile_form`/`handle_verification_form`はutils(viewsでない)。カラム25項目一致。Username=displayname。validate_usernameフォーマットは未強制(デッド)。S3系は`WEKO_RECORDS_UI_USER_STORAGE_MODIFICATION_ENABLED`時のみ。
- 8_5 API設定: blueprint invenio_oauth2server_settings(/account/settings/applications)。**訂正**: `client_secret`(clien_secret誤), `Confidential`(Confidencial誤)。personal/authorized振り分けに`Token.is_internal==False`条件あり。スコープ一覧不完全(index/item/author/file/oa_status/ranking 追加)。削除はPOST+delete field(HTTP DELETEでない)。
- 10_1 ワークスペース:アイテム一覧: **矛盾**: 関連モジュールに`weko_workspace`筆頭欠落。`get_workspace_itemlist`(/workspace/)。ES index`{prefix}-weko`(-weko-item誤)。status table複合PK(user_id,recid)。TSVはクライアントJS(WorkspaceExport.js)`itemlist_export_YYYYMMDDhhmmss.tsv`。OaStatus(weko_records)。
- 10_2 簡易アイテム登録: weko_workspace(item_register /workspace/item_registration, item_register_save /workspace/workflow_registration)。DB/ES保存はweko_search_ui(import_items_to_activity/system)。CrossRefのみweko_items_ui経由。医中誌ラジオはUI未実装。
- 10_3 メタデータ自動補完: weko_workspace.api(CiNiiURL/JALCURL/DATACITEURL/JamasURL)+weko_items_autofill(CrossRefOpenURL)。CrossRef api_certificate依存(weko_admin.models.ApiCertificate, code"crf")。URLはconfigキー(WEKO_WORKSPACE_*_API_URL)。
- README: 1行→機能グループ1_x〜11_x概要を記入。
- user共通: 更新履歴のGitHub参照はv0.9.22で陳腐化。関連モジュール欠落頻出(weko-records/weko-workflow/invenio-communities/weko-workspace)。認証系はFlask-Security由来。

## other（4並列調査 2026-07-14）要点
- CELERY_01: instance.cfg CELERY_BEAT_SCHEDULEと一致(15タスク実在)。delete_log(weko_logging)は実装済だがbeatでコメントアウト(無効)。
- CONFIG_01: **修正**: `S3_SECRECT_ACCESS_KEY`→`S3_SECRET_ACCESS_KEY`。存在しないキー削除: WEKO_WORKFLOW_APPROVE_DONE/APPROVE_REJECTED/USAGE_REPORT_ACTIVITY_URL。リンクv0.9.22陳腐化。weko-groups/weko-redisはconfig.py無し(一致)。
- ID_01: **修正**: 利用申請アイテムタイプIDは31001-31008(`WEKO_WORKFLOW_USAGE_APPLICATION_ITEM_TYPES_LIST`。31005-08欠落、31003は利用申請でなく利用報告)。
- MODULE_01: リンクv0.9.22陳腐化。新規module(weko-redis/swordserver/workspace/signposting/notifications/invenio-iiif)反映要。
- DB_01: 外部SharePointリンクのみ。invenio-db+Alembic言及推奨。
- LOG.md: 方針doc。config WEKO_LOGGING_FS_LOGFILE/FS_LEVEL(ERROR)/FS_BACKUPCOUNT(31)/Sentry追記可。delete_log無効。
- SESSION_01: WEKO_ADMIN_IMPORT_PAGE_LIFETIME=43200(12h)一致。PERMANENT_SESSION_LIFETIME=1日、ACCOUNTS_SESSION_REDIS(DB1)追記。
- INBOX_01: weko-notifications(Notification/NotificationClient)。config WEKO_NOTIFICATIONS。model NotificationsUserSettings。**軽微矛盾**: TentativeAccept/UndoはEnum未実装。削除系通知メソッドは実装済だがシナリオ表未記載。COAR_NOTIFY_*/WEKO_NOTIFICATIONS_INBOX_*キー追記。
- WORKFLOW_01(連携): **修正**: エンドポイントは小文字`/depositactivity`(ActivityActionResource)。scope user:activity。config WEKO_WORKFLOW_GAKUNINRDM_DATA(workflow_id=-1,item_type_id=15)/GAKUNINRDM_PREFIX。
- OA-ASSIST: `call_external_system`(weko-records-ui/external.py, 第5引数request_info追加)。**重大矛盾**: publish_status値が逆(実装OAPublishStatus DRAFT=0/PUBLISHED=1/DELETED=-1→公開=1・非公開=0。仕様の公開0/非公開1は逆)。受信側oa_status_callback(weko-records rest, scope oa_status:update, model OaStatus)欠落。config WEKO_RECORDS_UI_OA_*。監査ログ operation ITEM_EXTERNAL_LINK。
- KAISEKI_01: **修正**: invenio-statsでなくweko-records-uiのオンライン分析ボタン(Binder誘導)。config WEKO_RECORDS_UI_DISPLAY_ONLINE_ANALYSIS_FLG(既定False)/ONLINE_ANALYSIS_URL。オープンアクセス限定表示。仕様ほぼ空→大幅追記。
- SHIBBOLETH_01: エンドポイント`POST /weko/shib/login`(shib_sp_login)。table shibboleth_user/shibboleth_userrole。**修正**: `gakunin_check_in`メソッドは非存在(check_in内インライン)。`WEKO_ACCOUNTS_SHIB_ROLE_RELATION`実値={管理者:System Administrator,図書館員:Repository Administrator,教員:Contributor,教官:Contributor}(仕様のコメントアウト旧版と不一致)。`WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT`実値 role_keyword="ro"/role_mapping{radm/cadm/cont}(仕様rolesは誤り)。IDP_ENTITY_ID実値は空文字。organizationName判定(get_organization_from_api, WEKO_ACCOUNTS_GAKUNIN_ROLE等)追記。ブロックユーザ(blocked_ePPNs)。
- OTHER_elasticsearch: ES 6.8.23。index prefix SEARCH_INDEX_PREFIX。7イベント。INDEXER_MAX_BODY_SIZE=62914560。**修正**: reindex新オプション--item-type-id/-f。
- USAGE_LOG: `invenio_stats.tasks.process_events`/`aggregate_events`。7イベント一致。目的/利用方法/ロール節が空欄→記入。
- USER_ACTIVITY_LOG: `weko_logging.UserActivityLogger`。table user_activity_logs。**修正多数**: JSONカラム名は`json`でなく`log`(NOT NULL)。community_idはString(100)/nullable/FK(text/NotNullは誤り)。DB設定 log_level実値INFO(ERRORは誤り)、delete when=years interval=10(months/3は誤り)。STREAM設定 log_level INFO。マスタは`WEKO_LOGGING_OPERATION_MASTER`。複合PK(id,date)でdateパーティション。削除設定キーは`WEKO_LOGGING_USER_ACTIVITY_DB_SETTING`(USER_ACTIVITY_SETTINGは誤り)。
- SCHEMA_1_1(Render)/1_2(Schema)/1_3(Form): ItemTypeの render/schema/form カラムのダンプ(デフォルトアイテムタイプ id16)。**修正**: 1_2/1_3のヘッダ「関連モジュール: Invenio_oaiserver」＋OAuth boilerplateはコピペ誤り→schema=weko-items-ui `get_json_schema`(/items/jsonschema/<id>), form=weko-items-ui `get_schema_form`(/items/schemaform/<id>), render=weko-itemtypes-ui `render_itemtype`。格納は weko_records.models.ItemType.{schema,form,render}。
- RADME.md: README.mdのtypo重複ファイル(両方「その他」1行)。要確認(削除候補)。

## 統合方針（このカテゴリ）
- CONFIRMED箇所: 関連モジュール/処理概要/configキー/モデル・テーブルスキーマ/ルートを追記して拡充。
- CONTRADICTED箇所: 実装に合わせて修正しつつ、乖離が重要なものは「実装上の注記」を添える（特にRA_05、RA_04のデフォルト15種、RA_02のEN文言）。
- 原仕様の「意図・要件」記述は残し、実装挙動との差は注記で明示（消さない）。
