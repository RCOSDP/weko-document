# 利用規約取得API

-   目的・用途

本機能は制限公開ファイルの利用申請を行う際の利用規約を取得するためのAPIである。

-   利用方法

WEKO_RECORDS_UI_RESTRICTED_API が True の状態で API を実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○           | ○           | ○                |

-   機能内容

-   指定されたファイルの利用規約情報を返却する。

> 実装補足（v2.0.2）：エンドポイントは `GET /api/<version>/records/<pid_value>/files/<file_name>/terms`（`WEKO_RECORDS_UI_REST_ENDPOINTS['get_file_terms']`）、ハンドラは `weko_records_ui.rest.GetFileTerms`。認可は `@require_api_auth(True)` ＋ `@require_oauth_scopes(activity_scope.id)`。`WEKO_RECORDS_UI_RESTRICTED_API` が False の場合は403（既定 False）。ETag は `md5([ファイル名]_[利用規約テキスト])` で生成し、`Accept-Language`（`WEKO_RECORDS_UI_API_ACCEPT_LANGUAGES`＝`en`/`ja`）で多言語対応。取得不可時は404（`ContentsNotFoundError`）。関連モジュール：weko-records-ui。

-   利用規約情報には以下の内容を含める。

    -   取得時点の利用規約のテキスト

        -   利用規約が多言語で設定されている場合はリクエスト時に指定された言語のテキストを返却する。（デフォルトは英語(en)）

    -   取得時点のファイル名と利用規約のテキスト内容をハッシュ化したEtag

        -   Etagは本APIのクライアントキャッシュの他、利用申請API
            使用時に確認した規約と差異が無いかをチェックするのに使用する。

-   関連モジュール

-   weko_records_ui.rest.py

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。(flask-limiter)

    -   デフォルトでは同一ホストからのアクセスは１分当たり100回までとする

    -   制限を超える場合429エラー（Too Many Requests）とする

    -   制限公開機能がOFF（WEKO_RECORDS_UI_RESTRICTED_API が False）である場合、403エラー（Forbidden）とする

-   指定されたアイテム/ファイルの情報を取得する

    -   取得できない場合は404エラー

-   利用規約のテキストデータを取得する

    -   「利用規約」の項目自体が存在しない場合は空として扱う

-   レスポンスに必要な情報を生成する。

    -   取得した利用規約のテキストを含める

    -   ファイル名と利用規約テキストからEtagを生成する。

        -   Etagはファイル名と利用規約テキストをアンダースコアで連結した文字列（[ファイル名]_[利用規約テキスト]）をmd5でハッシュ化した値とする。

-   リクエスト

    -   API仕様書を参照

-   レスポンス

    -   API仕様書を参照

-   設定値

      - WEKO_RECORDS_UI_RESTRICTED_API

          - パス: <https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/weko-records-ui/weko_records_ui/config.py>

          - 初期値: False

          - 利用申請APIの有効無効を切り替える。

          - scripts/instance.cfg で定義されている場合は、そちらの設定を優先する。

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/7/14 |初版作成   |
|2025/10/31|APIの利用条件を記載|
|2026/07/14|実装(v2.0.2)と突き合わせ。エンドポイント・ハンドラ(GetFileTerms/FileApplication)・スコープ・configキー・エラーを追記|

# 利用申請開始API

-   目的・用途

本機能は制限公開ファイルの利用申請を開始し、アクティビティを作成するためのAPIである。

-   利用方法

WEKO_RECORDS_UI_RESTRICTED_API が True の状態で API を実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○           | ○           | ○                |

-   機能内容

> 実装補足（v2.0.2）：エンドポイントは `POST /api/<version>/records/<pid_value>/files/<file_name>/application`（`WEKO_RECORDS_UI_REST_ENDPOINTS['file_application']`）、ハンドラは `weko_records_ui.rest.FileApplication`。認可は `@require_api_auth(True)` ＋ `@require_oauth_scopes(activity_scope.id)`。ゲストは `init_activity_for_guest_user`、認証ユーザは `WorkActivity.init_activity` でアクティビティを作成する。レスポンスは `activity_id` / `activity_url` / `item_type_schema`（`ItemType.schema`）、ゲストは `token` を含む。エラー：`terms_token` 不一致は400（`InvalidTokenError`）、ワークフロー未設定は403（`InvalidWorkflowError`）、ゲストのメール不正は400。関連モジュール：weko-records-ui。

-   指定された制限公開ファイルの利用申請ワークフローアクティビティを作成する。

-   作成したアクティビティのIDと利用申請で必要な項目（ItemRegistrationの入力項目）の情報をレスポンスに含めて返却する。またUI上からも作業できるようアクティビティのURLも返す。

-   指定された制限公開ファイルに利用規約が設定されている場合は、規約への同意が必要。

    -   利用規約取得APIで取得されたEtagの値が本APIのリクエストのterms_tokenヘッダーに含まれており、かつそのterms_tokenの内容が一致した場合に同意したものとみなす。

        -   なお、利用規約が多言語で設定されている場合、利用規約取得APIリクエスト時に指定した言語と同じものを本APIリクエスト時に指定しないとtokenが一致しない。

    -   同意がない場合はアクティビティの作成を行わずエラーを返す。

-   利用申請ワークフローが指定されていないロールのユーザーからのリクエストはエラーとする。

-   関連モジュール

-   weko_records_ui.rest.py

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。(flask-limiter)

    -   デフォルトでは同一ホストからのアクセスは１分当たり100回までとする

    -   制限を超える場合429エラー（Too Many Requests）とする

-   制限公開機能がOFF（WEKO_RECORDS_UI_RESTRICTED_API が False）である場合、403エラー（Forbidden）とする

-   ゲストユーザーの場合、リクエストに含まれるメールアドレスを確認する

    -   メールアドレスがない、またはメールアドレスの形式不正の場合は400エラー

-   指定されたアイテム/ファイルの情報を取得する

    -   取得できない場合は404エラー

-   ユーザーロールに該当する利用申請ワークフロー情報を取得する

    -   ワークフローが設定されていない場合は403エラー

    -   設定されたワークフロー情報の取得に失敗した場合は404エラー

-   利用規約をチェックする

    -   利用規約が設定されていない、または利用規約テキストが空である場合はチェックを行わない。

    -   利用規約が設定されテキスト内容が空でない場合は、リクエストヘッダーに含まれるterms_tokenの内容を検証する。

        -   terms_tokenが一致しない場合400エラー

-   ユーザーのロールに応じたワークフローアクティビティを作成する

    -   ゲストユーザーの場合はGuestActivityを作成する
        （init_activity_for_guest_user）

        -   既に同ファイル・同メールアドレスに紐づくゲストアクティビティが存在した場合、新たにアクティビティは作成されず、既存アクティビティを使用する。

    -   認証済みユーザーの場合は通常のActivityのみを作成する（init_activity）

-   レスポンスに必要な情報を生成する。

    -   作成したアクティビティのIDを含める

    -   ワークフローに紐づくアイテムタイプのスキーマJSON(ItemType.schema)を含める

    -   UI上でアクティビティへアクセスするためのURLを含める

    -   ゲストユーザーの場合アクティビティへのアクセスに必要なtokenを含める

        -   このtokenはアクティビティへアクセスするためのURLに含まれているものと同一

-   リクエスト

    -   API仕様書を参照

-   レスポンス

    -   API仕様書を参照

-   設定値

      - WEKO_RECORDS_UI_RESTRICTED_API

          - パス: <https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/weko-records-ui/weko_records_ui/config.py>

          - 初期値: False

          - 利用申請APIの有効無効を切り替える。

          - scripts/instance.cfg で定義されている場合は、そちらの設定を優先する。

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/7/14 |初版作成   |
|2025/10/31|APIの利用条件を記載|
|2026/07/14|実装(v2.0.2)と突き合わせ。エンドポイント・ハンドラ(GetFileTerms/FileApplication)・スコープ・configキー・エラーを追記|

# 利用申請API

-   目的・用途

本機能は制限公開ファイルの利用申請のワークフローにおける申請内容の登録（item Registration）を行うためのAPIである。

-   利用方法

WEKO_RECORDS_UI_RESTRICTED_API が True の状態で API を実行する。

-   利用可能なロール

| ロール             | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:------------------:|:-------------:|:---------------:|:------------------:|:-----------:|:-----------:|:----------------:|
| 利用可否           | ○             | ○               | ○                  | ○           | ○           | ○                |

-   機能内容

-   指定された利用申請ワークフローアクティビティのItem Registrationの処理を行う。

    -   ItemRegistrationの各入力項目に対する入力情報はリクエスト内に含まれるJSONで受け取り、depositを行う。

    -   depositされたアイテムのpublish_stateの値は1（private）とする。

    -   アイテムはリクエストで指定されたインデックスIDにリンクし、インデックスIDは複数指定可能とする。

-   本利用申請ワークフローのアクティビティの場合のみ利用可能とし、通常のワークフローアクティビティでは使用できない。

-   関連モジュール

-   weko_workflow.rest.py

-   処理概要

-   OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。

-   サーバー負荷軽減のためリクエストのアクセス制限機能をかける。(flask-limiter)

    -   デフォルトでは同一ホストからのアクセスは１分当たり100回までとする

    -   制限を超える場合429エラー（Too Many Requests）とする

-   制限公開機能がOFF（WEKO_RECORDS_UI_RESTRICTED_API が False）である場合、403エラー（Forbidden）とする

-   ゲストユーザーの場合、リクエストに含まれるtokenを確認する

    -   tokenに紐づくゲストアクティビティが存在しない場合は404エラー

-   指定されたアクティビティの情報を取得する

    -   取得できない場合は404エラー

    -   ユーザーにアクション実行権限がなければ403エラー

-   ItemRegistrationの各項目の入力内容を確認し、depositを実行する

    -   必須項目に値がない場合は400エラー

    -   アイテム登録に使用するワークフローで登録先インデックスが指定されている場合はそちらにリンクさせ、そうでない場合はリクエストで指定されたインデックスにリンクさせる。

    -   格納後は次のフローアクションに移行する。（次アクションがApproveである場合かつ承認依頼通知メールが送信する設定になっている場合はメールを送信する）

-   レスポンスに必要な情報を生成する。

    -   Item Registrationの情報を取得する

    -   workflow_activity.temp_dataに保存された申請内容を取得する。

-   リクエスト

    -   API仕様書を参照

-   レスポンス

    -   API仕様書を参照

-   設定値

      - WEKO_RECORDS_UI_RESTRICTED_API

          - パス: <https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/weko-records-ui/weko_records_ui/config.py>

          - 初期値: False

          - 利用申請APIの有効無効を切り替える。

          - scripts/instance.cfg で定義されている場合は、そちらの設定を優先する。

-   更新履歴

| 日付      | 更新内容 |
|----------|----------|
|2023/7/14 |初版作成   |
|2025/10/31|APIの利用条件を記載|
|2026/07/14|実装(v2.0.2)と突き合わせ。エンドポイント・ハンドラ(GetFileTerms/FileApplication)・スコープ・configキー・エラーを追記|
