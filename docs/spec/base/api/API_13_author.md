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
|3|著者DB著者編集|PUT   |/api/{version}/authors|author:update|
|4|著者DB著者削除|DELETE|/api/{version}/authors|author:delete|

## 4. スコープと利用可能なロールの関係

- APIを利用できるかどうかをスコープ及びスコープに紐づけられた権限で制御する。

| スコープ | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザ | 一般ユーザ | ゲスト（未ログイン） |
| --- | --- | --- | --- | --- | --- | --- |
|author:search| 〇 | 〇 | ✕ | ✕ | ✕ | ✕ |
|author:create| 〇 | 〇 | ✕ | ✕ | ✕ | ✕ |
|author:update| 〇 | 〇 | ✕ | ✕ | ✕ | ✕ |
|author:delete| 〇 | 〇 | ✕ | ✕ | ✕ | ✕ |


## 5. 著者DB検索

### 5.1. 機能内容

- OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。
- 指定された検索キーで著者DBを検索した結果を返す。
- 検索キーとして著者姓名、著者名、著者姓、著者識別子（外部識別子を含む）を利用できる。
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

    | 項目 | 説明 |
    | --- | --- |
    | version | APIのバージョン |

- クエリパラメータ

    - idtypeは文字列で指定させる（例：weko、orcid）

    | 項目 | 説明 |
    | --- | --- |
    |fullname|著者姓名|
    |firstname|著者名|
    |familyname|著者姓|
    |idtype|著者識別子種別。選択肢は画面と同様|
    |authorid|idtypeに対応した著者識別子|

- ヘッダーパラメータ

    | 項目 | 値 | 必須 | 説明 |
    | --- | --- | --- | --- |
    | Authorization | Bearer <access_token> | - |操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。|


#### レスポンス<!-- omit in toc -->

- レスポンスコード

    | コード | 説明 |
    | --- | --- |
    | 200 | 正常終了 |
    | 400 | リクエストに不備がある |
    | 401 | OAuth2認証失敗 |
    | 403 | 該当ユーザに必要なロールが付与されていない|
    | 500 | 内部のエラー |

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
                ]
            }
        ]
    }
    ```

    **データ構造**

    |項目名|型|説明|
    | --- | --- | --- |
    |authors|object|変更情報を格納する。|

    **emailInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |email|string|著者のメールアドレス|

    **authorIdInfo**

    - idtypeは文字列に変換して返す（例：weko、orcid）

    |項目名|型|説明|
    | --- | --- | --- |
    |idType|string|著者識別子種別。選択肢は画面と同様|
    |authorId|string|著者識別子|
    |authorIdShowFlg|boolean|［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。|

    **authorNameInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |language|string|著者姓名の記述言語。選択肢は画面と同様|
    |firstname|string|著者名|
    |familyName|string|著者姓|
    |nameFormat|string|著者名と著者姓の組み合わせ方|
    |nameShowFlg|boolean|［著者DBから入力］機能で、氏名が自動入力されるかどうか。|

    **identifierInfo**

    - affiliationIdTypeは文字列に変換して返す（例：ISNI、ROR）

    |項目名|型|説明|
    | --- | --- | --- |
    |affiliationIdType|string|所属機関識別子種別。選択肢は画面と同様|
    |affiliationId|string|所属機関識別子|
    |identifierShowFlg|boolean||

    **affiliationNameInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |affiliationName|string|所属機関名|
    |affiliationNameLang|string|所属機関の記述言語。選択肢は画面と同様|
    |affiliationNameShowFlg|boolean||

    **affiliationPeriodInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |periodStart|string|所属開始日。入力形式はyyyy-MM-dd。|
    |periodEnd|string|所属終了日。入力形式はyyyy-MM-dd。|


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

    | 項目 | 説明 |
    | --- | --- |
    | version | APIのバージョン |

- ヘッダーパラメータ

    | 項目 | 値 | 必須 | 説明 |
    | --- | --- | --- | --- |
    | Authorization | Bearer <access_token> | - |操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。|

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
            ]
        }
    }
    ```

    **データ構造**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |author|object|〇|-|変更情報を格納する。|

    **emailInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |email|string|✕|-|著者のメールアドレス|

    **authorIdInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |idType|string|△※|-|著者識別子種別。選択肢は画面と同様（例：weko、orcid）|
    |authorId|string|△※|-|著者識別子|
    |authorIdShowFlg|boolean|✕|true|［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。|

    ※ idTypeとauthorIdの片方のみが送られた場合はエラーにする

    **authorNameInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |language|string|✕※|-|著者姓名の記述言語。選択肢は画面と同様|
    |firstname|string|✕|-|著者名|
    |familyName|string|✕|-|著者姓|
    |nameFormat|string|✕|"familyNmAndNm"※|著者名と著者姓の組み合わせ方|
    |nameShowFlg|boolean|✕|true|［著者DBから入力］機能で、氏名が自動入力されるかどうか。|

    ※ firstnameまたはfamilyNameが指定されたときはlanguageは必須とする
    ※ language、firstname、familyNameが送られてきた場合でnameFormatが指定されていない場合のみデフォルト値を適用する

    **identifierInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |affiliationIdType|string|△※|-|所属機関識別子種別。選択肢は画面と同様（例：ISNI、ROR）|
    |affiliationId|string|△※|-|所属機関識別子|
    |identifierShowFlg|boolean|✕|true||

    ※ affiliationIdTypeとaffiliationIdの片方のみが送られた場合はエラーにする

    **affiliationNameInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |affiliationName|string|△※|-|所属機関名|
    |affiliationNameLang|string|△※|-|所属機関の記述言語。選択肢は画面と同様|
    |affiliationNameShowFlg|boolean|✕|true||

    ※ affiliationNameとaffiliationNameLangの片方のみが送られた場合はエラーにする

    **affiliationPeriodInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |periodStart|string|✕|-|所属開始日。入力形式はyyyy-MM-dd。|
    |periodEnd|string|✕|-|所属終了日。入力形式はyyyy-MM-dd。|

#### レスポンス<!-- omit in toc -->

- レスポンスコード

    | コード | 説明 |
    | --- | --- |
    | 200 | 正常終了 |
    | 400 | リクエストに不備がある |
    | 401 | OAuth2認証失敗 |
    | 403 | 該当ユーザに必要なロールが付与されていない|
    | 500 | 内部のエラー |

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
            ]
        }
    }
    ```

    **データ構造**

    |項目名|型|説明|
    | --- | --- | --- |
    |authors|object|変更情報を格納する。|

    **emailInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |email|string|著者のメールアドレス|

    **authorIdInfo**

    - idtypeは文字列に変換して返す（例：weko、orcid）

    |項目名|型|説明|
    | --- | --- | --- |
    |idType|string|著者識別子種別。選択肢は画面と同様|
    |authorId|string|著者識別子|
    |authorIdShowFlg|boolean|［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。|

    **authorNameInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |language|string|著者姓名の記述言語。選択肢は画面と同様|
    |firstname|string|著者名|
    |familyName|string|著者姓|
    |nameFormat|string|著者名と著者姓の組み合わせ方|
    |nameShowFlg|boolean|［著者DBから入力］機能で、氏名が自動入力されるかどうか。|

    **identifierInfo**

    - affiliationIdTypeは文字列に変換して返す（例：ISNI、ROR）

    |項目名|型|説明|
    | --- | --- | --- |
    |affiliationIdType|string|所属機関識別子種別。選択肢は画面と同様|
    |affiliationId|string|所属機関識別子|
    |identifierShowFlg|boolean||

    **affiliationNameInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |affiliationName|string|所属機関名|
    |affiliationNameLang|string|所属機関の記述言語。選択肢は画面と同様|
    |affiliationNameShowFlg|boolean||

    **affiliationPeriodInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |periodStart|string|所属開始日。入力形式はyyyy-MM-dd。|
    |periodEnd|string|所属終了日。入力形式はyyyy-MM-dd。|

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
    - `authorIdInfo.idType`が`WEKO`の場合、`authorId`に半角数字以外の文字が含まれている場合または既に存在する値は場合は400エラーにする。入力された値が既に使用されている場合のエラーメッセージは「`The value is already in use as WEKO ID`」とする。
    - `authorIdInfo`について、`idType`と`authorId`の片方のみが送られた場合は400エラーを返す。
    - `authorNameInfo`について、`firstname`または`familyName`が指定されたとき、`language`が指定されていなければ400エラーを返す。
    - `identifierInfo`について、`affiliationIdType`と`affiliationId`の片方のみが送られた場合は400エラーを返す。
    - `affiliationNameInfo`について、`affiliationName`と`affiliationNameLang`の片方のみが送られた場合は400エラーを返す。
    - `affiliationPeriodInfo`について、以下の場合400エラーを返す。
      - yyyy-MM-ddの入力形式を満たさない場合
      - 所属開始日（`periodStart`）が所属終了日（`periodEnd`）より後の日付の場合

6. 著者情報を登録する
    - `authorIdInfo.idType`が`WEKO`の`authorIdInfo.authorId`が指定されていない場合、既存のWEKOIDの最大値+1の数字を`authorIdInfo.authorId`として登録する。
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

PUT /api/{version}/authors

**スコープ**

- author:update

#### リクエスト<!-- omit in toc -->

- パスパラメータ

    | 項目 | 説明 |
    | --- | --- |
    | version | APIのバージョン |

- ヘッダーパラメータ

    | 項目 | 値 | 必須 | 説明 |
    | --- | --- | --- | --- |
    | Authorization | Bearer <access_token> | 〇 |操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。|

- リクエストボディ

    **サンプル**

    ```json
    {
        "force_change": false,
        "id": "e2fc714c-6fcb-469c-993e-28a67c6fbcf5",
        "pk_id": "1",
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
            ]
        }
    }
    ```

    **データ構造**

    ※ idとpk_idはどちらか、または両方を指定する。両方を指定した際、著者が一致しなければエラーとする。

    |項目名|型|必須|説明|
    | --- | --- | --- | --- |
    |force_change|boolean|✕|著者名の変更をアイテムに反映するかどうか|
    |id|string|〇※|ElasticSearchのuuid|
    |pk_id|string|〇※|authorsテーブルのid|
    |author|object|〇|変更情報を格納する。<br>空の辞書はエラーとする。|

    **emailInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |email|string|✕|-|著者のメールアドレス|

    **authorIdInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |idType|string|〇※|-|著者識別子種別。選択肢は画面と同様（例：weko、orcid）|
    |authorId|string|〇※|-|著者識別子|
    |authorIdShowFlg|boolean|✕|true|［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。|

    ※ idTypeとauthorIdの片方のみが送られた場合はエラーにする
    ※ WEKO IDは必須

    **authorNameInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |language|string|△※|-|著者姓名の記述言語。選択肢は画面と同様|
    |firstname|string|△※|-|著者名|
    |familyName|string|△※|-|著者姓|
    |nameFormat|string|✕|"familyNmAndNm"※|著者名と著者姓の組み合わせ方|
    |nameShowFlg|boolean|✕|true|［著者DBから入力］機能で、氏名が自動入力されるかどうか。|

    ※ firstnameまたはfamilyNameが指定されたときはlanguageは必須とする
    ※ language、firstname、familyNameが送られてきた場合でnameFormatが指定されていない場合のみデフォルト値を適用する

    **identifierInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |affiliationIdType|string|△※|-|所属機関識別子種別。選択肢は画面と同様（例：ISNI、ROR）|
    |affiliationId|string|△※|-|所属機関識別子|
    |identifierShowFlg|boolean|✕|true||

    ※ affiliationIdTypeとaffiliationIdの片方のみが送られた場合はエラーにする

    **affiliationNameInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |affiliationName|string|△※|-|所属機関名|
    |affiliationNameLang|string|△※|-|所属機関の記述言語。選択肢は画面と同様|
    |affiliationNameShowFlg|boolean|✕|true||

    ※ affiliationNameとaffiliationNameLangの片方のみが送られた場合はエラーにする

    **affiliationPeriodInfo**

    |項目名|型|必須|デフォルト値|説明|
    | --- | --- | --- | --- | --- |
    |periodStart|string|✕|-|所属開始日。入力形式はyyyy-MM-dd。|
    |periodEnd|string|✕|-|所属終了日。入力形式はyyyy-MM-dd。|

#### レスポンス<!-- omit in toc -->

- レスポンスコード

    | コード | 説明 |
    | --- | --- |
    | 200 | 正常終了 |
    | 400 | リクエストに不備がある |
    | 401 | OAuth2認証失敗 |
    | 403 | 該当ユーザに必要なロールが付与されていない |
    | 404 | 指定された著者が存在しない |
    | 500 | 内部のエラー |


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
            ]
        }
    }
    ```

    **データ構造**

    |項目名|型|説明|
    | --- | --- | --- |
    |authors|object|変更情報を格納する。|

    **emailInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |email|string|著者のメールアドレス|

    **authorIdInfo**

    - idtypeは文字列に変換して返す（例：weko、orcid）

    |項目名|型|説明|
    | --- | --- | --- |
    |idType|string|著者識別子種別。選択肢は画面と同様|
    |authorId|string|著者識別子|
    |authorIdShowFlg|boolean|［著者DBから入力］機能で、外部著者IDを自動入力するかどうか。|

    **authorNameInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |language|string|著者姓名の記述言語。選択肢は画面と同様|
    |firstname|string|著者名|
    |familyName|string|著者姓|
    |nameFormat|string|著者名と著者姓の組み合わせ方|
    |nameShowFlg|boolean|［著者DBから入力］機能で、氏名が自動入力されるかどうか。|

    **identifierInfo**

    - affiliationIdTypeは文字列に変換して返す（例：ISNI、ROR）

    |項目名|型|説明|
    | --- | --- | --- |
    |affiliationIdType|string|所属機関識別子種別。選択肢は画面と同様|
    |affiliationId|string|所属機関識別子|
    |identifierShowFlg|boolean||

    **affiliationNameInfo**

    |項目名|型|説明|
    | --- | --- | --- |
    |affiliationName|string|所属機関名|
    |affiliationNameLang|string|所属機関の記述言語。選択肢は画面と同様|
    |affiliationNameShowFlg|boolean||

    **"affiliationPeriodInfo"**

    |項目名|型|説明|
    | --- | --- | --- |
    |periodStart|string|所属開始日。入力形式はyyyy-MM-dd。|
    |periodEnd|string|所属終了日。入力形式はyyyy-MM-dd。|


### 7.3. 処理概要

1. ユーザー認証する
    - リクエストに **`Authorization`** ヘッダーがある場合は、記載されたアクセストークンを使用しユーザーを認証する。認証に失敗した場合は401エラーを返す。

2. スコープを確認する
    - 必要なスコープがついていなければ403エラーを返す。

3. ユーザーの権限を確認する
    - スコープに設定されている権限が満たせていなければ403エラーを返す。

4. リクエストを確認する
    - 必須の項目が送られていない場合は400エラーにする。
    - idとpk_idの両方が指定されていない場合は400エラーとする。
    - authorが空だった場合は、400エラーとなりエラーメッセージ「author can not be null.」が返却される。
    - 送られてきた値の型が定義と異なる場合は400エラーを返す。
    - `authorIdInfo.idtype`が`WEKO`の項目が存在しない場合は400エラーを返す。

5. 指定された著者を確認する
    - idとpk_idでそれぞれ著者情報を検索する。
    - 指定された著者情報が存在しない場合は404エラーを返す。
    - 両方が指定された際、著者が一致しなければ400エラーを返す。エラーメッセージは「`Parameters 'id' and 'pk_id' refer to different users.`」とする。

6. 著者情報を確認する
    - `authorIdInfo.idType`、`authorNameInfo.language`、`affiliationInfo.identifierInfo.affiliationIdType`、`affiliationInfo.affiliationNameInfo.affiliationNameLang`の値が選択肢に無い値の場合、400エラーを返す。
    - `authorIdInfo.idType`が`WEKO`の場合、`authorId`に半角数字以外の文字が含まれている場合または既に存在する値は場合は400エラーにする。入力された値が既に使用されている場合のエラーメッセージは「`The value is already in use as WEKO ID`」とする。
    - `authorIdInfo`について、`idType`と`authorId`の片方のみが送られた場合は400エラーを返す。
    - `authorNameInfo`について、`firstname`または`familyName`が指定されたとき、`language`が指定されていなければ400エラーを返す。
    - `identifierInfo`について、`affiliationIdType`と`affiliationId`の片方のみが送られた場合は400エラーを返す。
    - `affiliationNameInfo`について、`affiliationName`と`affiliationNameLang`の片方のみが送られた場合は400エラーを返す。
    - `affiliationPeriodInfo`について、以下の場合400エラーを返す。
      - yyyy-MM-ddの入力形式を満たさない場合
      - 所属開始日（`periodStart`）が所属終了日（`periodEnd`）より後の日付の場合

7. 著者情報を変更する
    - `authorIdInfo.idType`、`affiliationInfo.identifierInfo.affiliationIdType`は与えられた値で検索しIDを引っ張ってくる。
    - DBとElasticsearchの著者情報を置きかえる。
    - エラーが発生した場合は、ロールバックして500エラーを返す。

8. 著者情報の更新をアイテムのメタデータに反映する
    - pk_idでauthor_linkを検索し、著者名以外の著者情報の変更をアイテムのメタデータに反映する。
    - `force_change`がTrueの場合は、著者名の変更もアイテムのメタデータに反映する。
    - WEKO IDに変更がある場合、"weko_link"のweko_idを更新する。

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

DELETE /api/{version}/authors

**スコープ**

- author:delete

#### リクエスト<!-- omit in toc -->


- パスパラメータ

    | 項目 | 説明 |
    | --- | --- |
    | version | APIのバージョン |

- ヘッダーパラメータ

    | 項目 | 値 | 必須 | 説明 |
    | --- | --- | --- | --- |
    | Authorization | Bearer <access_token> | 〇 |操作するWEKOユーザーのOAuth認証情報。アクセストークンを用いる。|

- リクエストボディ

    **サンプル**

    ```json
    {
        "id": "e2fc714c-6fcb-469c-993e-28a67c6fbcf5",
        "pk_id": "1"
    }
    ```

    **データ構造**

    ※ idとpk_idはどちらか、または両方を指定する。両方を指定した際、著者が一致しなければエラーとする。

    |項目名|型|必須|説明|
    | --- | --- | --- | --- |
    |id|string|〇※|ElasticSearchのuuid|
    |pk_id|string|〇※|authorsテーブルのid|


#### レスポンス<!-- omit in toc -->

- レスポンスコード

    | コード | 説明 |
    | --- | --- |
    | 200 | 正常終了 |
    | 400 | リクエストに不備がある |
    | 401 | OAuth2認証失敗 |
    | 403 | 該当ユーザに必要なロールが付与されていない |
    | 404 | 指定された著者が存在しない |
    | 500 | 内部のエラー |


### 8.3. 処理概要

1. ユーザー認証する
    - リクエストに **`Authorization`** ヘッダーがある場合は、記載されたアクセストークンを使用しユーザーを認証する。認証に失敗した場合は401エラーを返す。

2. スコープを確認する
    - 必要なスコープがついていなければ403エラーを返す。

3. ユーザーの権限を確認する
    - スコープに設定されている権限が満たせていなければ403エラーを返す。

4. リクエストの確認
    - 必須の項目が送られていない場合は400エラーにする。
    - idとpk_idの両方が指定されていない場合は400エラーとする。
    - authorが空だった場合は、400エラーとなりエラーメッセージ「`author can not be null.`」が返却される。

5. パラメータの確認
    - idとpk_idでそれぞれ著者情報を検索する。
    - 指定された著者情報が存在しない場合は404エラーを返す。
    - 両方が指定された際、著者が一致しなければ400エラーを返す。エラーメッセージは「`Parameters 'id' and 'pk_id' refer to different users.`」とする。

6. 著者を削除する
    - DBとElasticsearchの著者情報の`is_deleted`をTrueに書き変える。
    - エラーが発生した場合は、ロールバックして500エラーを返す。


## 9. 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
|2025/2/17||初版作成|
