# 著者DB機能API<!-- omit in toc -->

## 目次<!-- omit in toc -->

- [1. 目的](#1-目的)
- [2. 要求仕様](#2-要求仕様)
- [3. エンドポイント一覧](#3-エンドポイント一覧)
- [4. スコープと利用可能なロールの関係](#4-スコープと利用可能なロールの関係)
- [5. 著者DB検索](#5-著者db検索)
  - [5.1. 機能内容](#51-機能内容)
  - [5.2. API仕様](#52-api仕様)
  - [5.3. 処理概要](#53-処理概要)
- [6. 著者DB著者登録](#6-著者db著者登録)
  - [6.1. 機能内容](#61-機能内容)
  - [6.2. API仕様](#62-api仕様)
  - [6.3. 処理概要](#63-処理概要)
- [7. 著者DB著者変更](#7-著者db著者変更)
  - [7.1. 機能内容](#71-機能内容)
  - [7.2. API仕様](#72-api仕様)
  - [7.3. 処理概要](#73-処理概要)
- [8. 著者DB著者削除](#8-著者db著者削除)
  - [8.1. 機能内容](#81-機能内容)
  - [8.2. API仕様](#82-api仕様)
  - [8.3. 処理概要](#83-処理概要)
- [9. 更新履歴](#9-更新履歴)

## 1. 目的

著者DBをAPIで操作できるようにする。

## 2. 要求仕様

- 著者DBを検索、登録、更新、削除するためのAPIを整備する。
- 検索APIでは、検索キーとして、著者姓名、著者名、著者姓、著者識別子を利用できるようにする。
- 検索結果には著者DBの各項目を含める。
- 検索、登録、更新、削除のAPIでそれぞれ固有のスコープを必須とする。
- サービス用アカウントによるサーバ間OAuth2を利用する。

## 3. エンドポイント一覧

| 項番 | 概要 | HTTP Method | エンドポイント | スコープ |
| --- | --- | --- | --- |--- |
|1|著者DB著者検索|GET   |/api/{version}/authors|author:search|
|2|著者DB著者追加|POST  |/api/{version}/authors|author:create|
|3|著者DB著者編集|PUT   |/api/{version}/authors/{identifier}|author:update|
|4|著者DB著者削除|DELETE|/api/{version}/authors/{identifier}|author:delete|
|5|著者DB件数取得|GET   |/api/{version}/authors/count|author:search|

- 実ハンドラは `weko_authors.rest.AuthorDBManagementAPI`（検索/追加/編集/削除）および `weko_authors.rest.Authors`（件数取得 `count_authors`）。Blueprint生成は `rest.create_blueprint`、REST定義は `config.WEKO_AUTHORS_REST_ENDPOINTS`。`{identifier}` は整数IDまたはUUIDを受理する。

## 4. スコープと利用可能なロールの関係

- APIを利用できるかどうかをスコープ及びスコープに紐づけられた権限で制御する。

| スコープ | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザ | 一般ユーザ | ゲスト（未ログイン） |
| --- | --- | --- | --- | --- | --- | --- |
|author:search| 〇 | 〇 | 〇 | ✕ | ✕ | ✕ |
|author:create| 〇 | 〇 | 〇 | ✕ | ✕ | ✕ |
|author:update| 〇 | 〇 | 〇 | ✕ | ✕ | ✕ |
|author:delete| 〇 | 〇 | 〇 | ✕ | ✕ | ✕ |


## 5. 著者DB検索

### 5.1. 機能内容

- OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。
- 指定された検索キーで著者DBを検索した結果を返す。
- 検索キーとして著者姓名、著者名、著者姓、著者識別子（外部識別子を含む）、コミュニティIDを利用できる。
- スコープとロールによるアクセス制御を行う。
- 著者識別子種別と属機関識別子種別はidではなくschemeの値でリクエスト、レスポンスをする

### 5.2. API仕様

**関連モジュール**

- weko_authors.rest.py
- weko_authors.scopes.py
- weko_authors.config.py

**エンドポイント**

GET /api/{version}/authors

**スコープ**

- author:search

#### リクエスト<!-- omit in toc -->

- パスパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>version</td>
    <td>APIのバージョン</td>
    </tr>
    </tbody>
    </table>

- クエリパラメータ

    - idtypeは文字列で指定させる（例：weko、orcid）

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>fullname</td>
    <td>著者姓名</td>
    </tr>
    <tr>
    <td>firstname</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>familyname</td>
    <td>著者姓</td>
    </tr>
    <tr>
    <td>idtype</td>
    <td>著者識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>authorid</td>
    <td>idtypeに対応した著者識別子</td>
    </tr>
    <tr>
    <td>communityid</td>
    <td>著者を管理するコミュニティのID</td>
    </tr>
    </tbody>
    </table>

- ヘッダーパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>値</th>
    <th>必須</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Authorization</td>
    <td>Bearer &lt;access_token&gt;</td>
    <td>-</td>
    <td>操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。</td>
    </tr>
    </tbody>
    </table>


#### レスポンス<!-- omit in toc -->

- レスポンスコード

    <table>
    <thead>
    <tr>
    <th>コード</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>200</td>
    <td>正常終了</td>
    </tr>
    <tr>
    <td>400</td>
    <td>リクエストに不備がある</td>
    </tr>
    <tr>
    <td>401</td>
    <td>OAuth2認証失敗</td>
    </tr>
    <tr>
    <td>403</td>
    <td>該当ユーザに必要なロールが付与されていない</td>
    </tr>
    <tr>
    <td>500</td>
    <td>内部のエラー</td>
    </tr>
    </tbody>
    </table>

- レスポンスボディ

    **サンプル**

    ```json
    {
        "authors": [
            {
                "emailInfo": [
                    {
                        "email": "sample@xxx.co.jp"
                    }
                ],
                "authorIdInfo": [
                    {
                        "idType": "ORCID",
                        "authorId":"https://orcid.org/##",
                        "authorIdShowFlg": "true"
                    }
                ],
                "authorNameInfo": [
                    {
                        "language": "en",
                        "firstName": "John",
                        "familyName": "Doe",
                        "nameFormat": "familyNmAndNm",
                        "nameShowFlg": "true"
                    }
                ],
                "affiliationInfo": [
                    {
                        "identifierInfo": [
                            {
                                "affiliationId": "https://ror.org/##",
                                "affiliationIdType": "ROR",
                                "identifierShowFlg": "true"
                            }
                        ],
                        "affiliationNameInfo": [
                            {
                                "affiliationName": "NII",
                                "affiliationNameLang": "en",
                                "affiliationNameShowFlg": "true"
                            }
                        ],
                        "affiliationPeriodInfo": [
                            {
                                "periodStart": "2025-01-27",
                                "periodEnd": "2025-03-21"
                            }
                        ]
                    }
                ],
                "communityIds": ["community1"]
            }
        ]
    }
    ```

    **データ構造**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>authors</td>
    <td>object</td>
    <td>変更情報を格納する。</td>
    </tr>
    </tbody>
    </table>

    **emailInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>email</td>
    <td>string</td>
    <td>著者のメールアドレス</td>
    </tr>
    </tbody>
    </table>

    **authorIdInfo**

    - idtypeは文字列に変換して返す（例：weko、orcid）

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>idType</td>
    <td>string</td>
    <td>著者識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>authorId</td>
    <td>string</td>
    <td>著者識別子</td>
    </tr>
    <tr>
    <td>authorIdShowFlg</td>
    <td>boolean</td>
    <td>［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。</td>
    </tr>
    </tbody>
    </table>

    **authorNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>language</td>
    <td>string</td>
    <td>著者姓名の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>firstname</td>
    <td>string</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>familyName</td>
    <td>string</td>
    <td>著者姓</td>
    </tr>
    <tr>
    <td>nameFormat</td>
    <td>string</td>
    <td>著者名と著者姓の組み合わせ方</td>
    </tr>
    <tr>
    <td>nameShowFlg</td>
    <td>boolean</td>
    <td>［著者DBから入力］機能で、氏名が自動入力されるかどうか。</td>
    </tr>
    </tbody>
    </table>

    **identifierInfo**

    - affiliationIdTypeは文字列に変換して返す（例：ISNI、ROR）

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationIdType</td>
    <td>string</td>
    <td>所属機関識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationId</td>
    <td>string</td>
    <td>所属機関識別子</td>
    </tr>
    <tr>
    <td>identifierShowFlg</td>
    <td>boolean</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    **affiliationNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationName</td>
    <td>string</td>
    <td>所属機関名</td>
    </tr>
    <tr>
    <td>affiliationNameLang</td>
    <td>string</td>
    <td>所属機関の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationNameShowFlg</td>
    <td>boolean</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    **affiliationPeriodInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>periodStart</td>
    <td>string</td>
    <td>所属開始日。入力形式はyyyy-MM-dd。</td>
    </tr>
    <tr>
    <td>periodEnd</td>
    <td>string</td>
    <td>所属終了日。入力形式はyyyy-MM-dd。</td>
    </tr>
    </tbody>
    </table>

    **communityIds**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>communityIds[n]</td>
    <td>string</td>
    <td>著者を管理するコミュニティのID</td>
    </tr>
    </tbody>
    </table>


### 5.3. 処理概要

1. ユーザー認証する
    - リクエストに **`Authorization`** ヘッダーがある場合は、記載されたアクセストークンを使用しユーザーを認証する。認証に失敗した場合は401エラーを返す。

2. スコープを確認する
    - 必要なスコープがついていなければ403エラーを返す。

3. ユーザーの権限を確認する
    - スコープに設定されている権限が満たせていなければ403エラーを返す。

4. クエリパラメータから検索項目を取得する
    - `idtype`と`authorid`の片方のみが指定された場合は400エラーを返す。エラーメッセージは「`Both 'idtype' and 'authorid' must be specified together or omitted.`」とする。
    - `idtype`で指定された識別子種別でauthors_prefix_settingsテーブルのschemeカラムを検索し、一致するもののIDを取得する。

5. 著者情報を検索する
    - Elasticsearchに対して取得したパラメータでAND検索する。
    - DBとのやりとりでエラーが発生した場合は、ロールバックして500エラーを返す。

6. 検索結果を返す
    - 検索結果の`idtype`はauthors_prefix_settingsテーブルのidからschemeの値に変換する。
    - 検索結果の`affiliationIdType`はauthors_prefix_settingsテーブルのidからschemeの値に変換する。
    - 検索結果を整形してjson形式にエンコードしたものをレスポンスボディに入れ、ステータスコード200を返す。
    - 検索結果が空の場合もステータスコード200を返す。


## 6. 著者DB著者登録

### 6.1. 機能内容

- OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。
- 渡された内容で著者を登録する。
- スコープとロールによるアクセス制御を行う。
- 著者識別子種別と属機関識別子種別はidではなくschemeの値でリクエスト、レスポンスをする

### 6.2. API仕様

**関連モジュール**

- weko_authors.rest.py
- weko_authors.scopes.py
- weko_authors.config.py

**エンドポイント**

POST /api/{version}/authors

**スコープ**

- author:create

#### リクエスト<!-- omit in toc -->

- パスパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>version</td>
    <td>APIのバージョン</td>
    </tr>
    </tbody>
    </table>

- ヘッダーパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>値</th>
    <th>必須</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Authorization</td>
    <td>Bearer &lt;access_token&gt;</td>
    <td>-</td>
    <td>操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。</td>
    </tr>
    </tbody>
    </table>

- リクエストボディ

    **サンプル**

    ```json
    {
        "author": {
            "emailInfo": [
                {
                    "email": "sample@xxx.co.jp"
                }
            ],
            "authorIdInfo": [
                {
                    "idType": "ORCID",
                    "authorId":"https://orcid.org/##",
                    "authorIdShowFlg": "true"
                }
            ],
            "authorNameInfo": [
                {
                    "language": "en",
                    "firstName": "John",
                    "familyName": "Doe",
                    "nameFormat": "familyNmAndNm",
                    "nameShowFlg": "true"
                }
            ],
            "affiliationInfo": [
                {
                    "identifierInfo": [
                        {
                            "affiliationId": "https://ror.org/##",
                            "affiliationIdType": "ROR",
                            "identifierShowFlg": "true"
                        }
                    ],
                    "affiliationNameInfo": [
                        {
                            "affiliationName": "NII",
                            "affiliationNameLang": "en",
                            "affiliationNameShowFlg": "true"
                        }
                    ],
                    "affiliationPeriodInfo": [
                        {
                            "periodStart": "2025-01-27",
                            "periodEnd": "2025-03-21"
                        }
                    ]
                }
            ],
            "communityIds": ["community1"]
        }
    }
    ```

    **データ構造**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>author</td>
    <td>object</td>
    <td>〇</td>
    <td>-</td>
    <td>変更情報を格納する。</td>
    </tr>
    </tbody>
    </table>

    **emailInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>email</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>著者のメールアドレス</td>
    </tr>
    </tbody>
    </table>

    **authorIdInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>idType</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者識別子種別。選択肢は画面と同様（例：weko、orcid）</td>
    </tr>
    <tr>
    <td>authorId</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者識別子</td>
    </tr>
    <tr>
    <td>authorIdShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td>［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。</td>
    </tr>
    </tbody>
    </table>

    ※ idTypeとauthorIdの片方のみが送られた場合はエラーにする

    **authorNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>language</td>
    <td>string</td>
    <td>✕※</td>
    <td>-</td>
    <td>著者姓名の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>firstname</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>familyName</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>著者姓</td>
    </tr>
    <tr>
    <td>nameFormat</td>
    <td>string</td>
    <td>✕</td>
    <td>"familyNmAndNm"※</td>
    <td>著者名と著者姓の組み合わせ方</td>
    </tr>
    <tr>
    <td>nameShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td>［著者DBから入力］機能で、氏名が自動入力されるかどうか。</td>
    </tr>
    </tbody>
    </table>

    ※ firstnameまたはfamilyNameが指定されたときはlanguageは必須とする

    ※ language、firstname、familyNameが送られてきた場合でnameFormatが指定されていない場合のみデフォルト値を適用する

    **identifierInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationIdType</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関識別子種別。選択肢は画面と同様（例：ISNI、ROR）</td>
    </tr>
    <tr>
    <td>affiliationId</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関識別子</td>
    </tr>
    <tr>
    <td>identifierShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    ※ affiliationIdTypeとaffiliationIdの片方のみが送られた場合はエラーにする

    **affiliationNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationName</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関名</td>
    </tr>
    <tr>
    <td>affiliationNameLang</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationNameShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    ※ affiliationNameとaffiliationNameLangの片方のみが送られた場合はエラーにする

    **affiliationPeriodInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>periodStart</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>所属開始日。入力形式はyyyy-MM-dd。</td>
    </tr>
    <tr>
    <td>periodEnd</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>所属終了日。入力形式はyyyy-MM-dd。</td>
    </tr>
    </tbody>
    </table>

    **communityIds**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>communityIds[n]</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者を管理するコミュニティのID</td>
    </tr>
    </tbody>
    </table>

    ※ コミュニティ管理者の場合は管理対象のコミュニティが指定されていない場合はエラーにする

#### レスポンス<!-- omit in toc -->

- レスポンスコード

    <table>
    <thead>
    <tr>
    <th>コード</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>200</td>
    <td>正常終了</td>
    </tr>
    <tr>
    <td>400</td>
    <td>リクエストに不備がある</td>
    </tr>
    <tr>
    <td>401</td>
    <td>OAuth2認証失敗</td>
    </tr>
    <tr>
    <td>403</td>
    <td>該当ユーザに必要なロールが付与されていない</td>
    </tr>
    <tr>
    <td>500</td>
    <td>内部のエラー</td>
    </tr>
    </tbody>
    </table>

- レスポンスボディ

    **サンプル**

    ```json
    {
        "message": "Author successfully registered.",
        "author":{
            "emailInfo": [
                {
                    "email": "sample@xxx.co.jp"
                }
            ],
            "authorIdInfo": [
                {
                    "idType": "ORCID",
                    "authorId":"https://orcid.org/##",
                    "authorIdShowFlg": "true"
                }
            ],
            "authorNameInfo": [
                {
                    "language": "en",
                    "firstName": "John",
                    "familyName": "Doe",
                    "nameFormat": "familyNmAndNm",
                    "nameShowFlg": "true"
                }
            ],
            "affiliationInfo": [
                {
                    "identifierInfo": [
                        {
                            "affiliationId": "https://ror.org/##",
                            "affiliationIdType": "ROR",
                            "identifierShowFlg": "true"
                        }
                    ],
                    "affiliationNameInfo": [
                        {
                            "affiliationName": "NII",
                            "affiliationNameLang": "en",
                            "affiliationNameShowFlg": "true"
                        }
                    ],
                    "affiliationPeriodInfo": [
                        {
                            "periodStart": "2025-01-27",
                            "periodEnd": "2025-03-21"
                        }
                    ]
                }
            ],
            "communityIds": ["community1"]
        }
    }
    ```

    **データ構造**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>authors</td>
    <td>object</td>
    <td>変更情報を格納する。</td>
    </tr>
    </tbody>
    </table>

    **emailInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>email</td>
    <td>string</td>
    <td>著者のメールアドレス</td>
    </tr>
    </tbody>
    </table>

    **authorIdInfo**

    - idtypeは文字列に変換して返す（例：weko、orcid）

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>idType</td>
    <td>string</td>
    <td>著者識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>authorId</td>
    <td>string</td>
    <td>著者識別子</td>
    </tr>
    <tr>
    <td>authorIdShowFlg</td>
    <td>boolean</td>
    <td>［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。</td>
    </tr>
    </tbody>
    </table>

    **authorNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>language</td>
    <td>string</td>
    <td>著者姓名の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>firstName</td>
    <td>string</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>familyName</td>
    <td>string</td>
    <td>著者姓</td>
    </tr>
    <tr>
    <td>nameFormat</td>
    <td>string</td>
    <td>著者名と著者姓の組み合わせ方</td>
    </tr>
    <tr>
    <td>nameShowFlg</td>
    <td>boolean</td>
    <td>［著者DBから入力］機能で、氏名が自動入力されるかどうか。</td>
    </tr>
    </tbody>
    </table>

    **identifierInfo**

    - affiliationIdTypeは文字列に変換して返す（例：ISNI、ROR）

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationIdType</td>
    <td>string</td>
    <td>所属機関識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationId</td>
    <td>string</td>
    <td>所属機関識別子</td>
    </tr>
    <tr>
    <td>identifierShowFlg</td>
    <td>boolean</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    **affiliationNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationName</td>
    <td>string</td>
    <td>所属機関名</td>
    </tr>
    <tr>
    <td>affiliationNameLang</td>
    <td>string</td>
    <td>所属機関の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationNameShowFlg</td>
    <td>boolean</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    **affiliationPeriodInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>periodStart</td>
    <td>string</td>
    <td>所属開始日。入力形式はyyyy-MM-dd。</td>
    </tr>
    <tr>
    <td>periodEnd</td>
    <td>string</td>
    <td>所属終了日。入力形式はyyyy-MM-dd。</td>
    </tr>
    </tbody>
    </table>

    **communityIds**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>communityIds[n]</td>
    <td>string</td>
    <td>著者を管理するコミュニティのID</td>
    </tr>
    </tbody>
    </table>

### 6.3. 処理概要

1. ユーザー認証する
    - リクエストに **`Authorization`** ヘッダーがある場合は、記載されたアクセストークンを使用しユーザーを認証する。認証に失敗した場合は401エラーを返す。

2. スコープを確認する
    - 必要なスコープがついていなければ403エラーを返す。

3. ユーザーの権限を確認する
    - スコープに設定されている権限が満たせていなければ403エラーを返す。

4. リクエストを確認する
    - 必須の項目が送られていない場合は400エラーにする。
    - リクエストボディが無かった場合は400エラーにする。
    - authorが空だった場合は、400エラーとなりエラーメッセージ「author can not be null.」が返却される。
    - 送られてきた値の型が定義と異なる場合は400エラーを返す。

5. 著者情報を確認する
    - `authorIdInfo.idType`、`authorNameInfo.language`、`affiliationInfo.identifierInfo.affiliationIdType`、`affiliationInfo.affiliationNameInfo.affiliationNameLang`の値が選択肢に無い値の場合、400エラーを返す。
    - `authorIdInfo`について、`idType`と`authorId`の片方のみが送られた場合は400エラーを返す。
    - `authorNameInfo`について、`firstName`または`familyName`が指定されたとき、`language`が指定されていなければ400エラーを返す。
    - `identifierInfo`について、`affiliationIdType`と`affiliationId`の片方のみが送られた場合は400エラーを返す。
    - `affiliationNameInfo`について、`affiliationName`と`affiliationNameLang`の片方のみが送られた場合は400エラーを返す。
    - `affiliationPeriodInfo`について、以下の場合400エラーを返す。
      - yyyy-MM-ddの入力形式を満たさない場合
      - 所属開始日（`periodStart`）が所属終了日（`periodEnd`）より後の日付の場合
   - `communityIds`について、以下の場合400エラーを返す。
     - 許可されていない記号や制御文字を使用されている場合
     - DBに存在しないコミュニティIDを指定した場合
     - コミュニティ管理者権限のユーザーで管理対象のコミュニティが一つも含まれていない場合
   - コミュニティ管理者で、いかの場合403エラーを返す。
     - 管理対象外コミュニティのIDを指定した場合

6. 著者情報を登録する
    - リクエストに含まれる`idType`が`WEKO`（`'1'`）の`authorIdInfo`は除去し、WEKO IDは既存のWEKO IDの最大値+1を新規に採番して登録する。
    - `authorIdInfo.idType`、`affiliationInfo.identifierInfo.affiliationIdType`は与えられた値で検索しIDを引っ張ってくる。
    - DBとElasticsearchに著者情報を登録する。
    - エラーが発生した場合は、ロールバックして500エラーを返す。

7. レスポンスを返す
    - 登録した著者情報をjson形式にエンコードしたものをレスポンスボディに入れ、レスポンスコード200を返す。
    - `idtype`と`affiliationIdType`はidではなくschemeの文字列に変換して返す。


## 7. 著者DB著者変更

### 7.1. 機能内容

- OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。
- 指定された著者の情報を送られてきた情報で置き変える。
- スコープとロールによるアクセス制御を行う。
- 著者識別子種別と属機関識別子種別はidではなくschemeの値でリクエスト、レスポンスをする

### 7.2. API仕様

**関連モジュール**

- weko_authors.rest.py
- weko_authors.scopes.py
- weko_authors.config.py

**エンドポイント**

PUT /api/{version}/authors/{identifier}

**スコープ**

- author:update

#### リクエスト<!-- omit in toc -->

- パスパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>version</td>
    <td>APIのバージョン</td>
    </tr>
    <tr>
    <td>identifier</td>
    <td>更新対象の著者を一意に識別する値。<br>authorsテーブルのIDまたはElasticSearchのUUID のいずれかを指定する。</td>
    </tr>
    </tbody>
    </table>

- ヘッダーパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>値</th>
    <th>必須</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Authorization</td>
    <td>Bearer &lt;access_token&gt;</td>
    <td>〇</td>
    <td>操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。</td>
    </tr>
    </tbody>
    </table>

- リクエストボディ

    **サンプル**

    ```json
    {
        "force_change": false,
        "author": {
            "emailInfo": [
                {
                    "email": "sample@xxx.co.jp"
                }
            ],
            "authorIdInfo": [
                {
                    "idType": "WEKO",
                    "authorId":"111",
                    "authorIdShowFlg": "true"
                },
                {
                    "idType": "ORCID",
                    "authorId":"https://orcid.org/##",
                    "authorIdShowFlg": "true"
                }
            ],
            "authorNameInfo": [
                {
                    "language": "en",
                    "firstName": "John",
                    "familyName": "Doe",
                    "nameFormat": "familyNmAndNm",
                    "nameShowFlg": "true"
                }
            ],
            "affiliationInfo": [
                {
                    "identifierInfo": [
                        {
                            "affiliationId": "https://ror.org/##",
                            "affiliationIdType": "ROR",
                            "identifierShowFlg": "true"
                        }
                    ],
                    "affiliationNameInfo": [
                        {
                            "affiliationName": "NII",
                            "affiliationNameLang": "en",
                            "affiliationNameShowFlg": "true"
                        }
                    ],
                    "affiliationPeriodInfo": [
                        {
                            "periodStart": "2025-01-27",
                            "periodEnd": "2025-03-21"
                        }
                    ]
                }
            ],
            "communityIds": ["community1"]
        }
    }
    ```

    **データ構造**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>force_change</td>
    <td>boolean</td>
    <td>✕</td>
    <td>著者名の変更をアイテムに反映するかどうか</td>
    </tr>
    <tr>
    <td>author</td>
    <td>object</td>
    <td>〇</td>
    <td>変更情報を格納する。<br>空の辞書はエラーとする。</td>
    </tr>
    </tbody>
    </table>

    **emailInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>email</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>著者のメールアドレス</td>
    </tr>
    </tbody>
    </table>

    **authorIdInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>idType</td>
    <td>string</td>
    <td>〇※</td>
    <td>-</td>
    <td>著者識別子種別。選択肢は画面と同様（例：weko、orcid）</td>
    </tr>
    <tr>
    <td>authorId</td>
    <td>string</td>
    <td>〇※</td>
    <td>-</td>
    <td>著者識別子</td>
    </tr>
    <tr>
    <td>authorIdShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td>［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。</td>
    </tr>
    </tbody>
    </table>

    ※ idTypeとauthorIdの片方のみが送られた場合はエラーにする

    **authorNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>language</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者姓名の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>firstName</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>familyName</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者姓</td>
    </tr>
    <tr>
    <td>nameFormat</td>
    <td>string</td>
    <td>✕</td>
    <td>"familyNmAndNm"※</td>
    <td>著者名と著者姓の組み合わせ方</td>
    </tr>
    <tr>
    <td>nameShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td>［著者DBから入力］機能で、氏名が自動入力されるかどうか。</td>
    </tr>
    </tbody>
    </table>

    ※ firstNameまたはfamilyNameが指定されたときはlanguageは必須とする

    ※ language、firstname、familyNameが送られてきた場合でnameFormatが指定されていない場合のみデフォルト値を適用する

    **identifierInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationIdType</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関識別子種別。選択肢は画面と同様（例：ISNI、ROR）</td>
    </tr>
    <tr>
    <td>affiliationId</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関識別子</td>
    </tr>
    <tr>
    <td>identifierShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    ※ affiliationIdTypeとaffiliationIdの片方のみが送られた場合はエラーにする

    **affiliationNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationName</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関名</td>
    </tr>
    <tr>
    <td>affiliationNameLang</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>所属機関の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationNameShowFlg</td>
    <td>boolean</td>
    <td>✕</td>
    <td>true</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    ※ affiliationNameとaffiliationNameLangの片方のみが送られた場合はエラーにする

    **affiliationPeriodInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>periodStart</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>所属開始日。入力形式はyyyy-MM-dd。</td>
    </tr>
    <tr>
    <td>periodEnd</td>
    <td>string</td>
    <td>✕</td>
    <td>-</td>
    <td>所属終了日。入力形式はyyyy-MM-dd。</td>
    </tr>
    </tbody>
    </table>

    **communityIds**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>必須</th>
    <th>デフォルト値</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>communityIds[n]</td>
    <td>string</td>
    <td>△※</td>
    <td>-</td>
    <td>著者を管理するコミュニティのID</td>
    </tr>
    </tbody>
    </table>

    ※ コミュニティ管理者の場合は管理対象のコミュニティが指定されていない場合エラーにする。

#### レスポンス<!-- omit in toc -->

- レスポンスコード

    <table>
    <thead>
    <tr>
    <th>コード</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>200</td>
    <td>正常終了</td>
    </tr>
    <tr>
    <td>400</td>
    <td>リクエストに不備がある</td>
    </tr>
    <tr>
    <td>401</td>
    <td>OAuth2認証失敗</td>
    </tr>
    <tr>
    <td>403</td>
    <td>該当ユーザに必要なロールが付与されていない</td>
    </tr>
    <tr>
    <td>404</td>
    <td>指定された著者が存在しない</td>
    </tr>
    <tr>
    <td>500</td>
    <td>内部のエラー</td>
    </tr>
    </tbody>
    </table>


- レスポンスボディ

    **サンプル**

    ```json
    {
        "message": "Author successfully updated.",
        "author":{
            "emailInfo": [
                {
                    "email": "sample@xxx.co.jp"
                }
            ],
            "authorIdInfo": [
                {
                    "idType": "ORCID",
                    "authorId":"https://orcid.org/##",
                    "authorIdShowFlg": "true"
                }
            ],
            "authorNameInfo": [
                {
                    "language": "en",
                    "firstName": "John",
                    "familyName": "Doe",
                    "nameFormat": "familyNmAndNm",
                    "nameShowFlg": "true"
                }
            ],
            "affiliationInfo": [
                {
                    "identifierInfo": [
                        {
                            "affiliationId": "https://ror.org/##",
                            "affiliationIdType": "ROR",
                            "identifierShowFlg": "true"
                        }
                    ],
                    "affiliationNameInfo": [
                        {
                            "affiliationName": "NII",
                            "affiliationNameLang": "en",
                            "affiliationNameShowFlg": "true"
                        }
                    ],
                    "affiliationPeriodInfo": [
                        {
                            "periodStart": "2025-01-27",
                            "periodEnd": "2025-03-21"
                        }
                    ]
                }
            ],
            "communityIds": ["community1"]
        }
    }
    ```

    **データ構造**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>authors</td>
    <td>object</td>
    <td>変更情報を格納する。</td>
    </tr>
    </tbody>
    </table>

    **emailInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>email</td>
    <td>string</td>
    <td>著者のメールアドレス</td>
    </tr>
    </tbody>
    </table>

    **authorIdInfo**

    - idtypeは文字列に変換して返す（例：weko、orcid）

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>idType</td>
    <td>string</td>
    <td>著者識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>authorId</td>
    <td>string</td>
    <td>著者識別子</td>
    </tr>
    <tr>
    <td>authorIdShowFlg</td>
    <td>boolean</td>
    <td>［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。</td>
    </tr>
    </tbody>
    </table>

    **authorNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>language</td>
    <td>string</td>
    <td>著者姓名の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>firstName</td>
    <td>string</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>familyName</td>
    <td>string</td>
    <td>著者姓</td>
    </tr>
    <tr>
    <td>nameFormat</td>
    <td>string</td>
    <td>著者名と著者姓の組み合わせ方</td>
    </tr>
    <tr>
    <td>nameShowFlg</td>
    <td>boolean</td>
    <td>［著者DBから入力］機能で、氏名が自動入力されるかどうか。</td>
    </tr>
    </tbody>
    </table>

    **identifierInfo**

    - affiliationIdTypeは文字列に変換して返す（例：ISNI、ROR）

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationIdType</td>
    <td>string</td>
    <td>所属機関識別子種別。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationId</td>
    <td>string</td>
    <td>所属機関識別子</td>
    </tr>
    <tr>
    <td>identifierShowFlg</td>
    <td>boolean</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    **affiliationNameInfo**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>affiliationName</td>
    <td>string</td>
    <td>所属機関名</td>
    </tr>
    <tr>
    <td>affiliationNameLang</td>
    <td>string</td>
    <td>所属機関の記述言語。選択肢は画面と同様</td>
    </tr>
    <tr>
    <td>affiliationNameShowFlg</td>
    <td>boolean</td>
    <td></td>
    </tr>
    </tbody>
    </table>

    **"affiliationPeriodInfo"**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>periodStart</td>
    <td>string</td>
    <td>所属開始日。入力形式はyyyy-MM-dd。</td>
    </tr>
    <tr>
    <td>periodEnd</td>
    <td>string</td>
    <td>所属終了日。入力形式はyyyy-MM-dd。</td>
    </tr>
    </tbody>
    </table>

    **communityIds**

    <table>
    <thead>
    <tr>
    <th>項目名</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>communityIds[n]</td>
    <td>string</td>
    <td>著者を管理するコミュニティのID</td>
    </tr>
    </tbody>
    </table>


### 7.3. 処理概要

1. ユーザー認証する
    - リクエストに **`Authorization`** ヘッダーがある場合は、記載されたアクセストークンを使用しユーザーを認証する。認証に失敗した場合は401エラーを返す。

2. スコープを確認する
    - 必要なスコープがついていなければ403エラーを返す。

3. ユーザーの権限を確認する
    - スコープに設定されている権限が満たせていなければ403エラーを返す。

4. リクエストを確認する
    - `identifier`が整数値でもUUIDでもない場合は400エラーにする。
    - 必須の項目が送られていない場合は400エラーにする。
    - authorが空だった場合は、400エラーとなりエラーメッセージ「author can not be null.」が返却される。
    - 送られてきた値の型が定義と異なる場合は400エラーを返す。
    - `authorIdInfo.idtype`が`WEKO`の項目が存在しない場合は400エラーを返す。

5. 指定された著者を確認する
    - `identifier`で著者情報を検索する。
    - 指定された著者情報が存在しない場合は404エラーを返す。

6. 著者情報を確認する
    - `authorIdInfo.idType`、`authorNameInfo.language`、`affiliationInfo.identifierInfo.affiliationIdType`、`affiliationInfo.affiliationNameInfo.affiliationNameLang`の値が選択肢に無い値の場合、400エラーを返す。
    - `authorIdInfo`について、`idType`と`authorId`の片方のみが送られた場合は400エラーを返す。
    - `authorNameInfo`について、`firstName`または`familyName`が指定されたとき、`language`が指定されていなければ400エラーを返す。
    - `identifierInfo`について、`affiliationIdType`と`affiliationId`の片方のみが送られた場合は400エラーを返す。
    - `affiliationNameInfo`について、`affiliationName`と`affiliationNameLang`の片方のみが送られた場合は400エラーを返す。
    - `affiliationPeriodInfo`について、以下の場合400エラーを返す。
      - yyyy-MM-ddの入力形式を満たさない場合
      - 所属開始日（`periodStart`）が所属終了日（`periodEnd`）より後の日付の場合
    - `communityIds`について、以下の場合400エラーを返す。
      - 許可されていない記号や制御文字が含まれる場合
      - DBに存在しないコミュニティIDが指定された場合
      - コミュニティ管理者権限のユーザーが、指定したIDの中に管理対象コミュニティを一つも含まない場合
   - コミュニティ管理者で、以下の場合403エラーを返す。
      - 管理対象外コミュニティのIDを新たに指定した場合
      - 変更前の著者に紐づいていた管理対象外コミュニティIDを指定しない場合
      - 管理対象コミュニティに紐づかない著者を変更対象に指定した場合

7. 著者情報を変更する
    - `authorIdInfo.idType`、`affiliationInfo.identifierInfo.affiliationIdType`は与えられた値で検索しIDを引っ張ってくる。
    - DBとElasticsearchの著者情報を置きかえる。
    - エラーが発生した場合は、ロールバックして500エラーを返す。

8. 著者情報の更新をアイテムのメタデータに反映する
    - pk_idでauthor_linkを検索し、著者名以外の著者情報の変更をアイテムのメタデータに反映する。
    - `force_change`がTrueの場合は、著者名の変更もアイテムのメタデータに反映する。

9.  レスポンスを返す
    - 変更した著者情報の内容をjson形式にエンコードしたものをレスポンスボディに入れ、レスポンスコード200を返す。
    - `idtype`と`affiliationIdType`はidではなくschemeの文字列に変換して返す。


## 8. 著者DB著者削除

### 8.1. 機能内容

- OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。
- 指定された著者情報を削除する。
- スコープとロールによるアクセス制御を行う。

### 8.2. API仕様

**関連モジュール**

- weko_authors.rest.py
- weko_authors.scopes.py
- weko_authors.config.py

**エンドポイント**

DELETE /api/{version}/authors/{identifier}

**スコープ**

- author:delete

#### リクエスト<!-- omit in toc -->


- パスパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>version</td>
    <td>APIのバージョン</td>
    </tr>
    <tr>
    <td>identifier</td>
    <td>削除対象の著者を一意に識別する値。<br>authorsテーブルのIDまたはElasticSearchのUUID のいずれかを指定する。</td>
    </tr>
    </tbody>
    </table>

- ヘッダーパラメータ

    <table>
    <thead>
    <tr>
    <th>項目</th>
    <th>値</th>
    <th>必須</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Authorization</td>
    <td>Bearer &lt;access_token&gt;</td>
    <td>〇</td>
    <td>操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。</td>
    </tr>
    </tbody>
    </table>


#### レスポンス<!-- omit in toc -->

- レスポンスコード

    <table>
    <thead>
    <tr>
    <th>コード</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>200</td>
    <td>正常終了</td>
    </tr>
    <tr>
    <td>400</td>
    <td>リクエストに不備がある</td>
    </tr>
    <tr>
    <td>401</td>
    <td>OAuth2認証失敗</td>
    </tr>
    <tr>
    <td>403</td>
    <td>該当ユーザに必要なロールが付与されていない</td>
    </tr>
    <tr>
    <td>404</td>
    <td>指定された著者が存在しない</td>
    </tr>
    <tr>
    <td>500</td>
    <td>内部のエラー</td>
    </tr>
    </tbody>
    </table>


### 8.3. 処理概要

1. ユーザー認証する
    - リクエストに **`Authorization`** ヘッダーがある場合は、記載されたアクセストークンを使用しユーザーを認証する。認証に失敗した場合は401エラーを返す。

2. スコープを確認する
    - 必要なスコープがついていなければ403エラーを返す。

3. ユーザーの権限を確認する
    - スコープに設定されている権限が満たせていなければ403エラーを返す。

4. リクエストの確認
    - `identifier`が整数値でもUUIDでもない場合は400エラーにする。

5. パラメータの確認
    - `identifier`で著者情報を検索する。
    - 指定された著者情報が存在しない場合は404エラーを返す。
    - コミュニティ管理者の場合、削除対象の著者は管理対象コミュニティに関連付けられている必要がある。該当しない場合は403エラーを返す。

6. 著者を削除する
    - DBとElasticsearchの著者情報の`is_deleted`をTrueに書き変える。
    - エラーが発生した場合は、ロールバックして500エラーを返す。


## 実装補足（v2.0.2）

- 関連モジュール：weko-authors（`rest.py`：`AuthorDBManagementAPI` / `Authors`、`scopes.py`、`config.py`：`WEKO_AUTHORS_REST_ENDPOINTS` / `WEKO_AUTHORS_ES_INDEX_NAME`、`schema.py`：`AuthorCreateRequestSchema` / `AuthorUpdateRequestSchema`、`api.py`：`WekoAuthors.create` / `update`、`utils.py`：`validate_community_ids` / `check_delete_author` / `get_author_prefix_obj`、`models.py`：`Authors` / `AuthorsPrefixSettings` / `AuthorsAffiliationSettings`）
- 各メソッドは `@roles_required([WEKO_ADMIN_PERMISSION_ROLE_SYSTEM, _REPO, _COMMUNITY])`。検索・登録は Elasticsearch の `{prefix}-authors`（`WEKO_AUTHORS_ES_INDEX_NAME`）インデックスを使用する。
- 削除は論理削除（`is_deleted=True`。DB・ES 双方を更新）。
- 検索の `idtype` は scheme 文字列で受け取りDBでID変換し、レスポンスでID→schemeへ逆変換する。`idtype` と `authorid` は両方指定または両方省略が必要。
- POST時、`idType='1'`（WEKO）の `authorIdInfo` は除去される。
- レート制限は 1分あたり 100回（超過時 429）。

## 9. 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
|2025/2/17||初版作成|
|2025/5/30||REST対応|
| 2025/11/27|-|WEKO ID対応|
| 2026/07/14|-|実装(v2.0.2)と突き合わせ。未記載の件数取得API(/authors/count)追加、関連モジュール・ESインデックス・論理削除・configキーを追記|
| 2026/07/14||本文を実装準拠に修正|