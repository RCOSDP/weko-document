# Signposting（FAIR Signposting）

## 目的・用途

アイテム詳細ページに対し、機械可読な関連リソースへのリンクを HTTP レスポンスの `Link` ヘッダで提示する
（[FAIR Signposting](https://signposting.org/) 準拠）。人間向けの HTML とは別に、機械エージェント（クローラ・
テキストマイニング・リポジトリ間連携）が、当該アイテムの永続識別子（DOI）や各種メタデータ表現（JSON／BibTeX／
OAI-PMH の XML）へプログラムから到達できるようにすることを目的とする。

## 機能内容

アイテム詳細 URL（`/records/<recid>`）への **HEAD リクエスト**に対して、`Link` ヘッダに以下の typed link を付与して返す。

| rel | type | リンク先 | 付与条件 |
| --- | --- | --- | --- |
| `cite-as` | （なし） | 当該アイテムに紐づく登録済み DOI の permalink | アイテムに登録済み（REGISTERED）の DOI が存在する場合のみ |
| `describedby` | `application/json` | `{THEME_SITEURL}/records/<recid>/export/json` | 常時 |
| `describedby` | `application/x-bibtex` | `{THEME_SITEURL}/records/<recid>/export/bibtex` | 常時 |
| `describedby` | `application/xml`（`formats` にスキーマ namespace 付き） | `{THEME_SITEURL}/oai?verb=GetRecord&metadataPrefix=<fmt>&identifier=<oai_id>` | `OAISERVER_METADATA_FORMATS` に定義された各メタデータ形式ごとに 1 本 |

- ホスト部は config `THEME_SITEURL` を用いる。
- OAI 形式のリンクにはレコードの OAI 識別子（`record['_oai']['id']`）を用いるため、アイテムが OAI 識別子を持つことが前提。
- `cite-as` の DOI は、レコードの親（recid の `object_uuid`）に紐づく `pid_type='doi'` かつ `status=REGISTERED` の
  PID のうち、作成日時が最新のものを採用する。

## 利用可能なロール

- 【v2.1.0】アイテム詳細画面と同じ閲覧権限を持つ利用者（v2.1.0 以降）。`recid_signposting` に詳細表示 `recid` と同じ `permission_factory_imp='weko_records_ui.permissions:page_permission_factory'` が設定されており、閲覧できないアイテム（非公開・公開日前・閲覧不可インデックスのみに所属 等）への HEAD リクエストには `Link` ヘッダを返さない。未ログインの場合はログイン画面（`RECORDS_UI_LOGIN_ENDPOINT`）へのリダイレクト、ログイン済みで権限がない場合は 403 となる（invenio-records-ui の `record_view` の挙動）。公開アイテムおよび管理者は従来どおり応答を得られる。

## 関連モジュール

- weko-signposting（`Link` ヘッダ生成の本体。`weko_signposting/api.py` の `requested_signposting` / `get_record_doi`）
- weko-records-ui（`RECORDS_UI_ENDPOINTS` の `recid_signposting` で本機能を配線。`/export/json`・`/export/bibtex` の出力先も担当）
- invenio-pidstore（recid → object_uuid → DOI の PID 解決）
- invenio-oaiserver（`OAISERVER_METADATA_FORMATS` に定義された OAI メタデータ形式）

## 処理概要

1. 【v2.1.0】`weko-records-ui` の `RECORDS_UI_ENDPOINTS` に `recid_signposting`（`route='/records/<pid_value>'`,
   `methods=['HEAD']`, `view_imp='weko_signposting.api.requested_signposting'`,
   `permission_factory_imp='weko_records_ui.permissions:page_permission_factory'`）が定義される。
   PID 解決後、view 呼び出し前に `page_permission_factory(record).can()` で閲覧権限を確認する（v2.1.0 で追加）。
   同一ルートで GET を処理する `recid`（詳細表示）エンドポイントより**前に**配置され、HEAD メソッドを先取りする。
2. HEAD リクエストを受けると `requested_signposting(pid, record, ...)` が呼ばれ、`THEME_SITEURL` を基点に
   `record['recid']` から `record_link` を組み立てる。
3. `get_record_doi(recid)` が recid の `object_uuid` を取得し、その uuid に紐づく登録済み DOI（`pid_type='doi'`,
   `PIDStatus.REGISTERED`）を作成日時降順で 1 件取得する。存在すれば `rel="cite-as"` を先頭に追加する。
4. `rel="describedby"` の JSON／BibTeX リンク（`/export/json`, `/export/bibtex`）を追加する。
5. `OAISERVER_METADATA_FORMATS` の各形式について、`GetRecord` の OAI-PMH URL（`metadataPrefix`＝形式名、
   `identifier`＝`record['_oai']['id']`）を `rel="describedby"; type="application/xml"; formats="<namespace>"` として追加する。
6. 生成した全リンクを `, ` 連結で `Link` ヘッダに設定し、空のボディで `Response` を返す。

## エラー処理

- `get_record_doi` 内で `PIDDoesNotExistError`／`SQLAlchemyError` が発生した場合はログ出力し `None` を返す。
  この場合 `cite-as`（DOI）は付与されず、`describedby` 系リンクのみが返る（詳細表示自体は妨げない）。

## 関連ファイル

- `modules/weko-signposting/weko_signposting/api.py`（`requested_signposting`, `get_record_doi`）
- `modules/weko-records-ui/weko_records_ui/config.py`（`RECORDS_UI_ENDPOINTS` の `recid_signposting`）

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2026/07/15 | | 新規作成。実装（weko-signposting / weko-records-ui、tag v2.0.2）に基づき FAIR Signposting の応答仕様を整備 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：signposting 応答に詳細画面と同じ閲覧権限（`page_permission_factory`）を適用する点を反映 |
