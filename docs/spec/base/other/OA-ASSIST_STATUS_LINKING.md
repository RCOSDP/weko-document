## OAアシスト機能ステータス連携

- 目的・用途

WEKOに本文ファイルや根拠データが登録された際に、OAアシスト機能に対して、当該登録に対して本文登録等があったステータスを連携する。

- 機能内容

以降、「アイテム」はWEKO内のアイテム、「論文」はOAアシスト機能内の論文を指すものとする。

OAアシスト機能から登録されたアイテムに対して特定の操作が行われた場合に、OAアシスト機能に連携する。

本機能の画面は存在しない。

- メソッド

```python
def call_external_system(old_record=None, new_record=None,
                          old_item_reference_list=None, new_item_reference_list=None)
```

- パラメータ

  - old_record
    - 更新前のアイテムのWekoRecords
  - new_record
    - 更新後のアイテムのWekoRecords
  - old_item_reference_list
    - 更新前のItemReferenceのリスト
  - new_item_reference_list
    - 更新後のItemReferenceのリスト

old_recordとnew_recordのうち、old_recordのみ受け取った場合はアイテムの削除、new_recordのみ受け取った場合はアイテムの新規作成、両方を受け取った場合はアイテムの更新が行われたとものとする。

old_item_reference_listとnew_item_reference_listのうち、片方がNoneの場合は空のリストとして扱う。

- 処理概要

1. アイテムに対する以下の操作が成功した場合、この機能を呼び出す。

対象となる操作

- アイテムの登録、更新、削除
- アイテムの公開ステータスの変更
- アイテムに対するファイルの登録、更新、削除
- アイテム間連携の登録、変更、削除
- DOIの付与、取り下げ

アイテムやファイルの登録、更新、削除、DOIの付与、取り下げが行われたことは、以下の操作が行われたことで判定する。

- ワークフロー(新規作成、更新)でend_actionまで進行

  weko_workflow.utilsのhandle_finish_workflow()でsession.commit()に成功した場合

- アイテム詳細画面からの最新バージョン削除

  weko_records_ui.utilsのdelete_version()で最新のバージョンを削除し、publish()が成功した場合

- アイテム詳細画面からのアイテム削除

  weko_records_ui.views内のsoft_delete()でsession.commit()に成功した場合

- アイテム詳細画面からの公開ステータスの変更

  weko_records_ui.views内のpublish()でsession.commit()に成功した場合

- TSV形式インポート

  weko_search_ui.utilsのimport_items_to_system()でsession.commit()が成功した場合

- Admin画面のアイテム管理からのアイテム一括更新

  weko_deposit.rest.ItemResourceのput()でsession.commit()が成功した場合

- Admin画面のアイテム管理からのアイテム一括削除

  weko_search_ui.admin.ItemManagementBulkDeleteのindex()でsession.commit()が成功した場合

アイテム間連携が更新されたことは、以下の操作が行われたことで判定する。

- ワークフロー(新規作成、更新) でend_actionまで進行

  weko_workflow.utilsのhandle_finish_workflow()でupdate_item_link()によってitem_referenceテーブルのレコードが更新された場合

- アイテム詳細画面からの最新バージョン削除

  weko_records_ui.utilsのdelete_version()でupdate_item_link()にitem_referenceテーブルのレコードが更新された場合

  連携先判定処理を呼び出し、更新前のアイテム(アイテム更新、削除の場合)、更新後のアイテム(アイテム新規作成、更新の場合)を引数として渡す。

  アイテム間連携が更新されている場合は、更新前後のアイテム間連携のリストも追加で渡す。

  連携先判定処理の結果がOAアシスト機能である場合、以降の処理を実行する。

  連携先判定処理の結果がそれ以外の場合や、エラーが起きた場合は処理を終了する。

2. アイテムのIDを使用し、WEKO内のOAステータスから論文のIDを取得する。

3. アイテムの登録元のOAアシスト機能のトークンを取得する。

   1. DBのapi_certificateテーブルからレコードを取得し、アイテムの登録元のOAアシスト機能で発行されたclient_idとclient_secretを取得する。
   2. OAアシスト機能の/oauth/tokenにclient_idとclient_secretを使用してPOSTメソッドでリクエストを送信し、レスポンスからトークンを取得する。

   APIのURLはconfigファイルから取得する。取得したURLが空の場合はリクエストを送信しない。

   API呼び出しに失敗した場合はリトライする。リトライ回数はconfigファイルから取得する。

   DBから必要な情報を取得できなかった場合、OAアシスト機能からトークンを取得できなかった場合は処理を終了する。

4. 取得したトークンと論文のIDを使用してOAアシスト機能の論文ステータス更新API(/api/articles/{論文のID}/status)にPUTメソッドでリクエストを送信し、OAアシスト機能にステータス更新を連携する。

   以下の情報をリクエストボディでJSON形式としてOAアシスト機能に連携する。

   - 操作アクション
     - 作成: created
     - 更新: updated
     - 削除: deleted
   - アイテム情報
     - 公開ステータス
       - 公開: 0
       - 非公開: 1
       - 削除: -1
     - 公開日(YYYY-MM-DD形式)
   - ファイルの公開状態ごとのファイル数
     - 公開 + エンバーゴ(公開日以降): public
     - エンバーゴ(公開日より前): embargo
     - 非公開: private
     - 制限公開: restricted

   APIのURLはconfigファイルから取得する。取得したURLが空の場合はリクエストを送信しない。

   API呼び出しに失敗した場合はリトライする。リトライ回数はconfigファイルから取得する。

5. APIの呼び出しを行った場合、API実行のログを出力する。

   基本監査ログ機能を呼び出し、以下の情報を記録する。

   - 現在時刻 (基本監査ログ機能により自動で記録される)
   - 操作を行ったユーザーのID (基本監査ログ機能により自動で記録される)
   - アイテムのID
   - 操作アクション
   - 連携した外部システム名
   - 外部システムのAPI呼び出しの成否

- 設定値

  weko_records_ui/config.pyに記述する。

  - EXTERNAL_SYSTEM
    - 外部システム名を定義するEnum型
  - WEKO_RECORDS_UI_OA_GET_TOKEN_URL
    - OAアシスト機能のトークン取得APIのURL
  - WEKO_RECORDS_UI_OA_UPDATE_STATUS_URL
    - OAアシスト機能の論文ステータス更新APIのURL
  - WEKO_RECORDS_UI_OA_API_RETRY_COUNT
    - OAアシスト機能のAPIの呼び出しが失敗した際にリトライする最大回数
    - デフォルトでは3回とする
  - WEKO_RECORDS_UI_OA_API_CODE
    - api_certificateテーブルにおけるOAアシスト機能のAPIコード

  WEKO_RECORDS_UI_OA_GET_TOKEN_URL、WEKO_RECORDS_UI_OA_UPDATE_STATUS_URLについてはinstance.cfgにも記述する。

## 連携先判定処理

- 目的・用途

WEKO内のアイテムと、アイテムに対して行われた操作から、変更を連携する必要がある外部システムを判定する。

- メソッド

```python
def select_call_external_system_list(old_record=None, new_record=None,
                                      old_item_reference_list=None, new_item_reference_list=None)
```

- パラメータ

call_external_systemと同じ

- 戻り値

変更を通知する必要があるEXTERNAL_SYSTEMのリスト

通知する必要がない場合は空のリストを返す

- 処理概要

1. アイテムのIDから、アイテムの登録元のシステムを判定する。

   OAステータスから論文のIDが取得できればOAアシスト機能が登録元と判定する。

2. アイテムの登録元システムがOAアシストの場合

   引数を比較し、どのような操作が行われたか判定する。

   以下の操作の場合、OAアシスト機能に連携が必要と判定する。

   アイテムの削除、公開日や公開ステータス変更、ファイルの登録、削除、公開状況の変更

- 更新履歴

| 日付 | 更新内容 |
| ---- | ---- |
| 2025/3/21 | 初版作成 |

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足（訂正）：`weko_records_ui.external.call_external_system(old_record, new_record, old_item_reference_list, new_item_reference_list, request_info=None)`（第5引数 `request_info` は監査ログ用）。
- **公開ステータス値（重要な訂正）**：外部連携で送る `publish_status` は実装 `OAPublishStatus` に基づき **DRAFT=0（非公開）/ PUBLISHED=1（公開）/ DELETED=-1（削除）**。旧記述の「公開:0 / 非公開:1」は**公開・非公開が逆**（削除=-1 のみ一致）。
- 受信側（登録元からの状態受信）は weko-records の REST `OaStatusCallback`（route `/<version>/oa_status/callback`、スコープ `oa_status:update`、model `OaStatus`）で、article_id↔weko_item_pid の対応を upsert する。
- config `WEKO_RECORDS_UI_OA_GET_TOKEN_URL` / `_UPDATE_STATUS_URL` / `_API_RETRY_COUNT`(3) / `_API_CODE`(`"oaa"`)。監査ログは operation `ITEM_EXTERNAL_LINK`。呼び出し元は workflow(handle_finish_workflow)/records-ui(publish/soft_delete/delete_version)/search-ui(import)/deposit(ItemResource.put)/bulk-delete。
