# ゲストトークンの発行・受付設定

## 1. 概要

- 未ログインユーザ（以下ゲスト）が制限公開ファイルの利用申請・利用報告を行う際に発行するトークン（以下ゲストトークン）について、「発行」と「受付」をそれぞれ設定で有効・無効にできる

- 発行を無効にすると、ゲスト用アクティビティの作成とゲストトークンを含む URL のメール送信を行わない

- 受付を無効にすると、発行済みのゲストトークンを無効として扱い、ゲストトークンによるセッション（以下ゲストセッション）を利用させない

- ログインユーザの利用申請・利用報告は、本設定の影響を受けない

## 2. 用語

| 用語 | 説明 |
| ---- | ---- |
| ゲストトークン | ゲスト用アクティビティごとに発行する文字列。アクティビティ ID・ファイル名・作成日時・メールアドレスから生成し、ゲスト用アクティビティ URL の `token` パラメータとしてメールで通知する |
| ゲスト用アクティビティ | ゲストのメールアドレスで作成するワークフローのアクティビティ。テーブル `workflow_guest_activity` にトークンとともに記録する |
| ゲストセッション | ゲストトークンの検証に成功したときに、セッションに保存する `guest_token`・`guest_email`・`guest_url` の3つの値 |
| 発行 | ゲスト用アクティビティを作成し、ゲストトークンを生成すること |
| 受付 | ゲストトークンを検証し、ゲストセッションを作成・利用すること |

## 3. 設定

| 設定キー | 説明 | 既定値（config.py） | `scripts/instance.cfg` |
| ---- | ---- | ---- | ---- |
| WEKO_WORKFLOW_GUEST_TOKEN_ISSUE_ENABLED | ゲストトークンを発行する | False | True |
| WEKO_WORKFLOW_GUEST_TOKEN_ACCEPT_ENABLED | ゲストトークンを受け付ける | False | True |

- 既定値はいずれも False（無効）とする。ゲスト向けの機能を利用するサーバは `instance.cfg` で True を設定する

- `instance.cfg` に設定キーが無い場合は既定値（無効）となる

- UI アプリと REST API アプリの両方に同じ値を適用する。値の変更はアプリの再起動後に反映する

- 設定値は真偽値として評価する（`bool()`）

## 4. 機能仕様

### 4-1. 発行（WEKO_WORKFLOW_GUEST_TOKEN_ISSUE_ENABLED）

| ID | 対象 | 条件 | 発行が有効のとき | 発行が無効のとき |
| ---- | ---- | ---- | ---- | ---- |
| GT-I-01 | `POST /workflow/activity/init-guest`（アイテム詳細画面のメール入力モーダルからの送信） | ゲストがメールアドレスを送信する | ゲスト用アクティビティを作成し、ゲストトークンを含む URL をメールで送る | HTTP 403 を返す。応答の本文は `This function is not available.`（JSON）。アクティビティの作成とメール送信は行わない |
| GT-I-02 | `POST /api/v1/records/<pid_value>/files/<file_name>/application`（利用申請 API） | 未ログインで `mail` を指定する | ゲスト用アクティビティを作成する | HTTP 403 を返す。アクティビティは作成しない |
| GT-I-03 | 同上 | 未ログインで `mail` の形式が不正 | HTTP 400 | HTTP 400（メールアドレスの検証を発行設定の判定より先に行う） |
| GT-I-04 | 同上 | ログインユーザ | 本設定の影響を受けない | 本設定の影響を受けない |
| GT-I-05 | ワンタイム URL によるファイルのダウンロードで、利用報告のアクティビティを作成する場合（`weko_records_ui.utils.create_usage_report_for_user`） | ゲスト（`extra_info.is_guest` が真） | 利用報告のアクティビティを作成し、リマインダメールを送る | 利用報告のアクティビティを作成しない。ダウンロードは HTTP 403（`Unexpected error occurred.`）となる |
| GT-I-06 | 同上 | ログインユーザ | 本設定の影響を受けない | 本設定の影響を受けない |
| GT-I-07 | 利用報告のリマインダメール（管理画面「利用報告」の `POST /admin/restricted_access/send_mail_reminder` と GT-I-05 の送信） | ゲスト用アクティビティ（`extra_info.is_guest` が真） | 送信する | 送信対象から除外する（エラーにはしない） |
| GT-I-08 | 同上 | ゲスト用以外のアクティビティ | 送信する | 送信する |

- ゲストトークンを生成する関数（`weko_workflow.utils.generate_guest_activity_token_value`）と、ゲスト用アクティビティを作成する関数（`weko_workflow.utils.init_activity_for_guest_user`）は、発行が無効のとき例外 `GuestTokenDisabledError`（HTTP 403）を送出する。上記以外の呼び出し元から呼ばれた場合も、トークンは生成されない

- 発行を無効にしても、発行済みのゲストトークンは受付の設定に従って扱う

### 4-2. 受付（WEKO_WORKFLOW_GUEST_TOKEN_ACCEPT_ENABLED）

| ID | 対象 | 条件 | 受付が有効のとき | 受付が無効のとき |
| ---- | ---- | ---- | ---- | ---- |
| GT-A-01 | `GET /workflow/activity/guest-user/<file_name>?token=...`、`GET /workflow/activity/guest-user/recid/<record_id>?token=...` | 有効なゲストトークン | ゲスト用アクティビティ画面を表示し、ゲストセッションを作成する | エラー画面（`Token is invalid`）を表示する。ゲストセッションは作成しない |
| GT-A-02 | `POST /api/v1/workflow/activities/<activity_id>/application`（利用申請アクティビティの実行 API） | 未ログインで有効なゲストトークンを指定する | アクティビティを実行する | HTTP 400（`Invalid token.`） |
| GT-A-03 | UI アプリ・REST API アプリへのすべてのリクエスト | ゲストセッションを持つ | セッションを変更しない | リクエストの処理前に、セッションから `guest_token`・`guest_email`・`guest_url` を削除する |
| GT-A-04 | ゲストセッションを前提とする機能（`weko_accounts.utils.login_required_customize`・`roles_required` を付けた画面・API、Invenio-Files-REST のゲスト向けファイル操作） | GT-A-03 でゲストセッションを削除した | ゲストとして処理する | 未ログインとして扱う（API は HTTP 401、画面はログイン画面へ遷移する） |
| GT-A-05 | トークンの検証（`weko_workflow.utils.validate_guest_activity_token`） | 任意のトークン | トークンを検証する | 常に無効（`(False, None, None)`）を返す |

- 受付を無効にした時点で、利用中のゲストセッションは次のリクエストから利用できなくなる

### 4-3. 設定の組み合わせ

| 発行 | 受付 | ゲストの利用 |
| ---- | ---- | ---- |
| 有効 | 有効 | ゲストトークンの発行・受付ともに行う（`scripts/instance.cfg` の設定） |
| 有効 | 無効 | ゲスト用アクティビティを作成しメールを送るが、URL を開いてもトークンは無効となる。運用上は推奨しない |
| 無効 | 有効 | 新規の発行は行わず、発行済みのゲストトークンは有効期限まで利用できる。ゲスト向け機能を段階的に停止する場合に用いる |
| 無効 | 無効 | ゲスト向けの機能を利用できない（既定値） |

## 5. 画面

- アイテム詳細画面のゲスト向けメール入力モーダル・申請ボタンは、設定に関わらず表示する。発行が無効のときに送信すると、GT-I-01 のとおり失敗する

## 6. 関連モジュール

- weko-workflow（`config.py`：設定キー、`utils.py`：`is_guest_token_issue_enabled`・`is_guest_token_accept_enabled`・`guest_token_issue_required`・`clear_guest_session`、`errors.py`：`GuestTokenDisabledError`、`views.py`：`init_activity_guest`・`render_guest_workflow`、`rest.py`：`FileApplicationActivity`、`ext.py`：`before_request` の登録）

- weko-records-ui（`rest.py`：`FileApplication.post_v1`、`utils.py`：`create_usage_report_for_user`）

- weko-admin（`utils.py`：`UsageReport.send_reminder_mail`）

- 関連する機能仕様：[USER-4-14](../user/USER_4_14.md)、[制限公開](../restricted_access/README.md)、[ワークフロー・アクティビティの権限](../access_control/USER_WORKFLOW_ACTIVITY_01.md)

## 7. テスト観点

各 ID について、発行・受付の設定（有効・無効）と、利用者（ゲスト・ログインユーザ）を組み合わせて確認する。

| 観点 | 確認内容 | 対応 ID・節 |
| ---- | ---- | ---- |
| 既定値 | `instance.cfg` に設定が無いとき、発行・受付ともに無効となる | 3 |
| 設定の上書き | `instance.cfg` の True が既定値より優先される（UI アプリ・REST API アプリの両方） | 3 |
| 発行の停止 | 無効時、各入口で 403 となり、アクティビティ・トークン・メールが作られない | GT-I-01, 02, 05 |
| 入力検証の順序 | 不正なメールアドレスは発行設定に関わらず 400 | GT-I-03 |
| ログインユーザへの影響 | 発行・受付が無効でもログインユーザの利用申請・利用報告は従来どおり | GT-I-04, 06, 08 |
| リマインダの除外 | 無効時、ゲスト用アクティビティだけが除外され、ほかは送信される | GT-I-07, 08 |
| 受付の停止 | 無効時、有効なトークンでもゲスト用アクティビティ画面・API を利用できない | GT-A-01, 02, 05 |
| 既存セッション | 無効に切り替えた後、既存のゲストセッションが次のリクエストで削除され、ゲスト前提の画面・API が未ログイン扱いになる | GT-A-03, 04 |
| 有効時の回帰 | 発行・受付とも有効のとき、ゲストの利用申請から利用報告まで従来どおり完了する | 4-1, 4-2 |
| 組み合わせ | 4-3 の4通りで期待どおりに動作する | 4-3 |

## 8. 更新履歴

| 日付 | 更新内容 |
| ---- | ---- |
| （リリース日） | 新規作成（<リリース版>） |
