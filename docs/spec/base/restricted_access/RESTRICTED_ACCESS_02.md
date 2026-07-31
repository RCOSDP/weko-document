# アイテム詳細(制限公開)

- コンテンツのアクセスを「制限公開」とした場合のアイテム詳細画面、ファイル詳細画面の処理
  - アクセスしているユーザーが管理者権限があるかどうかは、「__check_user_permission」のメソッド（`weko-records-ui/weko_records_ui/permissions.py` の `check_file_download_permission` 内）でチェックする。管理者権限ありとして扱われるロールは、`WEKO_PERMISSION_SUPER_ROLE_USER`（`['System Administrator', 'Repository Administrator']`）と `WEKO_PERMISSION_ROLE_COMMUNITY`（`['Community Administrator']`）の合算である（システム管理者・リポジトリ管理者・コミュニティ管理者）。加えてアイテム登録者本人（`created_by` / `owner` / `weko_shared_ids`）も権限ありとして扱われる。
- 管理者権限をもつユーザに対して、アイテム詳細画面、ファイル詳細画面に、ファイルの情報を取得し、ダウンロードできる
- 権限がないユーザに対して、アイテム詳細画面に「アクセス制限」（英「Restricted Access」）と表示する。ファイル情報のリンクは不活性とし、ファイル詳細画面の「Action」にダウンロードボタンのかわりに「申請」ボタンを表示し、コンテンツ登録時に設定した「提供方法：ロール」のロールに一致するユーザーは「申請」ボタンをクリックことで以下の利用申請を実施することができる
  - 「提供方法：ロール」を「非ログインユーザ」とした場合、ログインしていないユーザは「申請」ボタンをクリックことで以下の利用申請を実施することができる
- 制限公開用のコンテンツファイルでの提供方法に一致しないユーザが「申請」ボタンを押下した場合はモーダルで警告メッセージを表示する
  - 警告メッセージ（AdminSettings `restricted_access` の `error_msg`。管理画面で編集可能。既定値は `WEKO_ADMIN_RESTRICTED_ACCESS_ERROR_MESSAGE`）：
    - 日本語：「このデータは利用できません（権限がないため）。」
    - 英語：「This data is not available for this user」（実装の既定値は末尾ピリオドなし）
- コンテンツのアクセスを「制限公開」とした場合のコンテンツファイルのアクセス制御
  - アクセスしているユーザーが管理者権限があるかどうかは、「__check_user_permission」のメソッドでチェックする
    - アクセス権限をもつユーザの場合（管理者・アイテム登録者・代理投稿者）
      - DLのURLを入力：　"Permission required"を表示する
        ※入力するURLは登録者(Contributor)以上がボタンを押下したときのURLとする
      - Informatonボタン押下：　"Permission required"を表示する
      - Informaton画面のURLを入力：　"Permission required"を表示する
    - 権限のないログインユーザの場合（「提供方法：ロール」の設定にかかわらず）
      - DLのURLを入力：　"Permission required"を表示する
        ※入力するURLは登録者(Contributor)以上がボタンを押下したときのURLとする
      - Informatonボタン押下：　"Permission required"を表示する
      - Informaton画面のURLを入力：　"Permission required"を表示する
    - 非ログインユーザの場合（「提供方法：ロール」の設定にかかわらず）
      - DLのURLを入力：　ログイン要求をする
        ※入力するURLは登録者(Contributor)以上がボタンを押下したときのURLとする
      - Informatonボタン押下：ログイン要求をする
      - Informaton画面のURLを入力：ログイン要求をする
- 利用申請①:利用規約への同意
  - 提供方法に一致するユーザーがアイテム詳細画面の「申請」ボタンを押下した際に利用申請設定時に設定されている利用規約をモーダル画面に表示する
    - 利用規約について
      - 利用規約文表示エリア上部に「利用規約」を固定で表示する
      - 「利用規約に同意する」ラベルクリック時もチェックボックスのオンオフができるようにする
      - 「利用規約に同意する」チェックボックスのチェック/非チェックが、「次へ」ボタンが活性/非活性と連動する
- 利用申請②：利用規約画面での「次へ」ボタンを押下した際の挙動
  - 「非ログインユーザ」で設定される場合、メールアドレスが入力できるモーダル画面が表示される
    - 受信したメール文のリンクをクリックするとワークフローに定義されているアクション画面（アイテム登録画面など）に遷移する
    - リンクはランダムなURLとトークン値から構成し、両者が一致した場合に利用登録ワークフローへのリンクとして機能する
  - 「提供方法：ロール」で設定される場合、指定されたワークフローの画面に遷移する
- 利用申請③：ワークフロー終了後の挙動
  - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True かつアイテム詳細画面の「申請」ボタンから起動したワークフローが「作業済み(Done)」となった際にダウンロード用のURL(以下、ワンタイムURL)をメールで通知する。リンクの有効期限とダウンロード回数は【Administration > Setting > Restricted Access画面】での「コンテンツファイルのダウンロード」(Content File Download)エリアで設定される
  - ワンタイムURLへアクセスした際、その時点でまだ有効なURLであればダウンロードが開始する
    - 以下のケースでは正しいURLであってもダウンロードできず、エラーメッセージが表示される
      - 有効期限を超過した場合
        - 日本語：「ダウンロード有効期限を超過しています。」
        - 英語：「 The expiration date for download has been exceeded. 」
      - ダウンロード回数を超過した場合
        - 日本語：「ダウンロード上限回数を超過しています。」
        - 英語：「 The download limit has been exceeded. 」
      - アイテム登録者または管理者により論理削除が行われた場合
        - 日本語：「このURLは削除されました。」
        - 英語：「 This URL has been deactivated. 」
      - 上記の他、以下のケースでもダウンロードが許可されない
        - 登録時は制限公開ファイルだったが、途中でその他の公開設定に変更された場合
        - 該当アイテムを含むインデックスが非公開に変更された場合
        - ファイルあるいはアイテムが削除された場合
        - システムのアップデートによりURL情報を保存するデータベースに変更が生じた場合
        - WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が False の場合
  - ワンタイムURLが使用されたとき、ファイルダウンロードに関するログ情報を保存する。ログ情報はダウンロードURL利用記録テーブル(file_url_download_log)に格納される
    - テーブルfile_url_download_logは以下の情報を保持する(ワンタイムURLが使用された場合)
      - ダウンロード日時
      - ワンタイムURLのID
      - ダウンロードされたファイルの公開設定
      - 使用されたトークン
    - ワンタイムURLのIDはテーブルfile_onetime_downloadのIDカラムを外部キーとしているため、テーブルを結合することでさらに以下の情報を確認できる
      - 利用申請者のメールアドレス
      - 利用申請を承認したユーザー
      - ダウンロードされたファイル
- 利用申請④：データダウンロード後の挙動
  - 利用申請が承認された制限公開コンテンツファイルを最初にダウンロードした際(=各ワンタイムURLの初回利用時)に、利用申請を行ったユーザーに向けて「利用報告の登録のお願い」メールを送信する。メールには利用報告ワークフローアクティビティの登録URLリンクが掲載されており、URLリンクから遷移する登録画面から利用報告を登録できる。
    - ゲストユーザーの利用報告WFに対して、リンクの有効期限は【Administration > Setting > Restricted Access画面】での「利用報告ワークフローへのアクセス」(Usage Report Workflow Access)エリアで設定できる

## 関連モジュール

- weko-records-ui（アクセス判定 `permissions.py`、ファイルダウンロード処理 `fd.py`、モデル `models.py`、共通処理 `utils.py`、ルート定義 `config.py`）
- weko-workflow（利用申請ワークフロー・ゲストアクティビティ `GuestActivity`、利用報告ワークフロー自動生成、`DISPLAY_FLAG` 連動）
- weko-admin（Restricted Access 設定、警告文言／`DISPLAY_FLAG` の既定値、AdminSettings `restricted_access`）
- 補助：invenio-files-rest（`ObjectVersion`）、weko-deposit（`WekoRecord`）、invenio-mail

## 処理概要

- 表示／ダウンロード権限判定
  - `page_permission_factory` → `file_permission_factory` → `check_file_download_permission` →（内部）`__check_user_permission` / `check_open_restricted_permission` → `check_permission_period`
  - アクセス設定ごとの分岐：`open_no`（`permissions.py`）、`open_restricted`（`check_open_restricted_permission`。`WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` が False なら不許可）
  - Permission required 画面テンプレート：`WEKO_PERMISSION_REQUIRED_TEMPLATE = 'weko_workflow/permission_required.html'`
- ワンタイムURLによるダウンロード（GET：検証）
  - route `recid_guest_onetime_validation` → `fd` のトークン検証 → `validate_onetime_token`（`DISPLAY_FLAG` チェック → `validate_url_download` → ゲストなら `validate_onetime_guest`）→ `process_onetime_file_download` → `check_and_send_usage_report` / ダウンロードログ保存 / `DownloadMixin.increment_download_count`
- ゲストの確定ダウンロード（POST）
  - route `recid_guest_file_download` → メール／パスワード照合 → `process_onetime_file_download`
- ダウンロード可否の検証（`validate_url_download`、`weko-records-ui/weko_records_ui/utils.py`）
  - 論理削除：「This URL has been deactivated.」（`is_deleted` が True）
  - ダウンロード回数超過：「The download limit has been exceeded.」（`download_count >= download_limit`）
  - 有効期限超過：「The expiration date for download has been exceeded.」
  - 上記の他、公開設定変更・ファイル／アイテム削除・`DISPLAY_FLAG` が False の場合も不許可
  - ※旧実装 `validate_onetime_download_token` が併存するが、現行のワンタイムDL経路は `validate_url_download` 側

## モデル / テーブルスキーマ

- `FileOnetimeDownload`（テーブル `file_onetime_download`、`weko-records-ui/weko_records_ui/models.py`）
  - `id` / `approver_id`（FK accounts_user＝承認者） / `record_id` / `file_name`（ファイル） / `expiration_date` / `download_limit` / `download_count` / `user_mail`（利用申請者メールアドレス） / `is_guest` / `is_deleted`（論理削除） / `extra_info`（JSON。`send_usage_report` 等） / `created` / `updated`
- `FileUrlDownloadLog`（テーブル `file_url_download_log`、同 `models.py`）
  - `id` / `url_type`（Enum SECRET/ONETIME） / `secret_url_id`（FK） / `onetime_url_id`（FK `file_onetime_download.id`） / `ip_address`（INET） / `access_status`（Enum OPEN_NO/OPEN_DATE/OPEN_RESTRICTED＝ダウンロードされたファイルの公開設定） / `used_token`（使用されたトークン） / `created`（ダウンロード日時） / `updated`
  - ※本テーブルはシークレットURLと共用のため、仕様本文に未記載の `url_type` / `secret_url_id` / `ip_address` 列を持つ
  - ダウンロード回数加算・論理削除・有効URL取得の共通処理は `DownloadMixin` に集約

## 主要設定値（config / AdminSettings）

| キー | 既定値 | 用途 |
| --- | --- | --- |
| `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` | False | 制限公開機能の表示制御。False時はワンタイムDLを不許可（403） |
| `WEKO_ADMIN_RESTRICTED_ACCESS_ERROR_MESSAGE` | （JA/EN文言） | 権限不一致時の警告メッセージ既定値（AdminSettingsで編集可） |
| `WEKO_PERMISSION_SUPER_ROLE_USER` | `['System Administrator','Repository Administrator']` | 管理者権限ロール |
| `WEKO_PERMISSION_ROLE_COMMUNITY` | `['Community Administrator']` | コミュニティ管理者ロール |
| `WEKO_PERMISSION_REQUIRED_TEMPLATE` | `'weko_workflow/permission_required.html'` | Permission required 画面 |
| AdminSettings `restricted_access.usage_report_workflow_access.expiration_date_access` | 500 | ゲスト利用報告ワークフローリンクの有効期限（日） |

## 主要ルート（RECORDS_UI_ENDPOINTS）

- `recid_files` `/record/<pid_value>/files/<path:filename>`（通常DL・権限判定）
- `recid_file_details` `/records/<pid_value>/file_details/<path:filename>`
- `recid_guest_onetime_validation`（GET）/ `recid_guest_file_download`（POST）`/record/<pid_value>/file/onetime/<filename>`
- `recid_copy_onetime_url` / `delete_onetime_url` `/records/<pid_value>/onetime/<filename>/<onetime_url_id>`

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | コンフィグ値による条件を記載 |
| 2026/07/13 |  | 実装(v2.0.2)と突き合わせ、関連モジュール・処理概要（実メソッドフロー）・モデル/テーブルスキーマ・設定値・ルートを追記。管理者ロール定数・警告文言の編集可能性・EN既定文言を明記 |
