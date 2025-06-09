# 基本監査ログ

## 目的・用途

セルフアーカイブにより、リポジトリを操作するユーザが多くなり、作業ミスによるトラブルの発生も増加すると考えられる。

リポジトリ操作に関するログを記録し、リポジトリ管理者以上がリポジトリ操作に関するログを取得できるようにする。

## 関連モジュール

  - weko\_logging

## ログ取得機能マスタ定義

  - パス: <https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-logging/weko_logging/config.py#L96-L324>

  - 設定キー：WEKO\_LOGGING\_USER\_ACTIVITY\_DB\_SETTING

  - どのような操作が行われた場合に、基本監査ログを出力するか定義したマスタ。

  - 基本監査ログが出力された際に、どのような操作によって出力したか併せて保存。

  - 出力したログの操作分類毎に機能IDが設定される。

      - 現状設定されている機能IDについては、[機能ID](#機能ID) 参照

  - 機能に対する具体的な操作を処理IDとして設定する。

      - 現状設定されている処理IDについては、[処理ID](#処理ID) 参照

      - 具体的なイメージについては[マスタイメージ](#マスタイメージ) を参照


### マスタイメージ
```
WEKO_LOGGING_OPERATION_MASTER = {
    "ITEM": {
        "id": 11
        "label": "アイテム操作"
        "operation": {
            "ITEM_CREATE": {
              "id": 1,
              "label": "アイテム登録",
              "target": "item",
            },
            "ITEM_UPDATE": {
                "id": 2,
                "label": "アイテム編集",
                "target": "item"
            }
        }
    }
}
```


### 機能ID

| 機能ID | キー        | 機能             |
| -----: | :--------- | :--------------- |
| 01     | GENERAL    | 一般              |
| 10     | ITEM\_TYPE | アイテムタイプ操作 |
| 11     | ITEM       | アイテム操作       |
| 12     | FILE       | ファイル操作       |
| 20     | WORKFLOW   | ワークフロー操作   |
| 21     | INDEX      | インデックス操作   |
| 22     | AUTHOR\_DB | 著者DB            |

### 処理ID

**01：一般**

| 処理ID | キー        | 処理       | 操作対象 |
| -----: | :--------- | :-------- | :------- |
| 1      | LOGIN      | ログイン   | ユーザー |
| 2      | LOGOUT     | ログアウト | ユーザー |

**10：アイテムタイプ操作**

| 処理ID | キー                     | 処理                         | 操作対象       |
| -----: | :------------------------   | :------------------------- | :------------- |
| 1      | ITEM\_TYPE\_CREATE          | アイテムタイプ作成           | アイテムタイプ |
| 2      | ITEM\_TYPE\_UPDATE          | アイテムタイプ編集           | アイテムタイプ |
| 3      | ITEM\_TYPE\_DELETE          | アイテムタイプ削除           | アイテムタイプ |
| 4      | ITEM\_TYPE\_MAPPING\_CREATE | アイテムタイプマッピング作成 | アイテムタイプ |
| 5      | ITEM\_TYPE\_MAPPING\_UPDATE | アイテムタイプマッピング編集 | アイテムタイプ |
| 6      | ITEM\_TYPE\_MAPPING\_DELETE | アイテムタイプマッピング削除 | アイテムタイプ |

**11：アイテム操作**

| 処理ID | キー                | 処理                                                       | 操作対象 |
| -----: | :-------------------- | :--------------------------------------------------------- | :------- |
| 1      | ITEM\_CREATE          | アイテム登録                                              | アイテム |
| 2      | ITEM\_UPDATE          | アイテム更新                                              | アイテム |
| 3      | ITEM\_DELETE          | アイテム削除                                              | アイテム |
| 4      | ITEM\_DELETE\_REQUEST | アイテム削除申請                                            | アイテム |
| 5      | ITEM\_IMPORT          | アイテムインポート                                          | -       |
| 6      | ITEM\_BULK\_CREATE    | アイテム一括登録                                            | -       |
| 7      | ITEM\_BULK\_DELETE    | アイテム一括削除                                            | -       |
| 8      | ITEM\_CREATE\_LINK    | アイテム間連携登録                                          | アイテム |
| 9      | ITEM\_UPDATE\_LINK    | アイテム間連携変更                                          | アイテム |
| 10     | ITEM\_DELETE\_LINK    | アイテム間連携削除                                          | アイテム |
| 11     | ITEM\_ASSIGN\_DOI     | DOI付与                                                   | アイテム |
| 12     | ITEM\_WITHDRAW\_DOI   | DOI取り下げ                                                | アイテム |
| 13     | ITEM\_PUBLISH         | アイテム公開                                               | アイテム |
| 14     | ITEM\_UNPUBLISH       | アイテム非公開                                             | アイテム |
| 15     | ITEM\_EXTERNAL\_LINK  | 外部へのアイテム情報連携<br>（ステータス連携（OAアシスト）等） | アイテム |

**12：ファイル操作**

| 処理ID | キー                | 処理                 | 操作対象 |
| -----: | :------------------ | :------------------ | :------- |
| 1      | FILE\_CREATE        | ファイル登録         | ファイル |
| 2      | FILE\_UPDATE        | ファイル変更         | ファイル |
| 3      | FILE\_DELETE        | ファイル削除         | ファイル |
| 4      | FILE\_REQUEST\_MAIL | リクエストメール     | ファイル |
| 5      | FILE\_DOWNLOAD      | ファイルダウンロード  | ファイル |

**20：ワークフロー操作**

| 処理ID | キー             | 処理             | 操作対象     |
| -----: | :--------------- | :-------------- | :---------- |
| 1      | WORKFLOW\_CREATE | ワークフロー登録 | ワークフロー |
| 2      | WORKFLOW\_UPDATE | ワークフロー変更 | ワークフロー |
| 3      | WORKFLOW\_DELETE | ワークフロー削除 | ワークフロー |

**21：インデックス操作**

| 処理ID | キー         | 処理             | 操作対象     |
| -----: | :------------ | :-------------- | :---------- |
| 1      | INDEX\_CREATE | インデックス登録 | インデックス |
| 2      | INDEX\_UPDATE | インデックス変更 | インデックス |
| 3      | INDEX\_DELETE | インデックス削除 | インデックス |

**22：著者DB**

| 処理ID | キー           | 処理         | 操作対象 |
| -----: | :------------- | :---------- | :------ |
| 1      | AUTHOR\_CREATE | 著者情報登録 | 著者     |
| 2      | AUTHOR\_UPDATE | 著者情報変更 | 著者     |
| 3      | AUTHOR\_DELETE | 著者情報削除 | 著者     |

**操作対象一覧**

| No. | 操作対象       | target     | 操作対象ID       |
| --: | -------------- | ---------- | ---------------- |
| 1   | ユーザー       | user       | ユーザーID       |
| 2   | アイテムタイプ  | itemtype   | アイテムタイプID |
| 3   | アイテム       | item       | アイテムID       |
| 4   | ファイル       | file       | ファイルID       |
| 5   | メタデータ      | metadata  | メタデータID     |
| 6   | インデックス    | index     | インデックスID   |
| 7   | ワークフロー    | workflow  | ワークフローID   |
| 8   | 著者           | author    | 著者ID           |

## 監査ログ出力

### 機能内容

  - ログをDBと標準出力に出力する
  - マスタに記述されている機能は画面からの操作でもAPIからの操作でもログを取る
  - 一連の処理の中で複数の機能を利用している場合は複数のログが出る
      - 例えばアイテム変更の際、ファイルがふたつ登録されたときはファイル変更のログがふたつ出力され、メタデータ変更のログも出力される。

### 設定値

  - DBへ出力するログレベル、およびDBのレコードの有効期限の設定

      - パス: <https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-logging/weko_logging/config.py#L82-L88>

      - 設定キー：WEKO\_LOGGING\_USER\_ACTIVITY\_DB\_SETTING

      - 現在の設定値：

> WEKO\_LOGGING\_USER\_ACTIVITY\_DB\_SETTING = {
> 
>   "log\_level": "ERROR",
> 
>   "delete": {
> 
>    "when": "months",
> 
>    "interval": 3
> 
>   }
> 
> }

  - 標準出力するログの設定

      - パス: <https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-logging/weko_logging/config.py#L91-L93>


      - 設定キー：WEKO\_LOGGING\_USER\_ACTIVITY\_DB\_SETTING

      - 現在の設定値：

> WEKO\_LOGGING\_USER\_ACTIVITY\_STREAM\_SETTING = {
> 
>   "log\_level": "ERROR"
> 
> }

### テーブル定義

  - テーブル名：user\_activity\_logs

      - json、remarks以外の項目はjsonの中に同じ項目を入れる

| 項目名         | カラム名        | データ型                       | Not Null | デフォルト | 説明                                        |
| -------------- | --------------- | ------------------------------ | -------- | ---------- | ------------------------------------------- |
| 識別子         | id              | integer                        | Yes(PK)  | -          | 連番。                                      |
| 日時           | date            | timestamp(6) without time zone | Yes      | -          | ログを出力する日時                          |
| ユーザーID     | user\_id         | integer                        |          | null       | 操作を行ったユーザーのID                    |
| コミュニティID | community\_id | text                           | Yes      | -          | コミュニティ（サブリポジトリ）のID |
| ロググループID     | log\_group\_id       | integer                        |          | null       | リクエスト毎に付けられる一連の処理のID   |
| ログ           | json            | jsonb                          |          | -          | ログ。中身はjson項目定義参照                |
| 備考           | remarks         |                                |      | null       |

### json項目定義

  - 定義はjsonschemaとしてconfig.pyに追加する
  - jsonの中で、テーブルのカラムにするものもある
  - ログレベルは、機能IDと処理IDで規定された処理が成功した場合はINFO、なんらかの異常で処理が完了できなかった場合はERRORにする

| 項目名         | 物理名              | カラム参照 | 型　　　 | デフォルト | 説明                                 |
| :------------ | :------------------ | :-------: | :------ | :-------- | :----------------------------------- |
| 識別子         | id                  | 〇        | integer | -         | レコードのID                          |
| ログレベル     | log\_level           |          | string  | -         | ERROR, INFOのいずれか                 |
| 日時           | date                | 〇        | string  | -         | ログを出力する日時                     |
| ユーザーID     | user\_id            | 〇        | integer | null      | 操作を行ったユーザーのID               |
| eppn          | eppn                 |          | string  | null      | 操作を行ったユーザーのeppnのID          |
| IPアドレス     | ip\_address         |           | string  | null      | 操作が行われた環境のIPアドレス          |
| クライアントID | client\_id           |           | string  | null      | クライアントID                        |
| コミュニティID | community\_id        | 〇        | string  | -          | コミュニティ（サブリポジトリ）のID     |
| 操作元         | source              |           | string  | null       | リクエストされたWEKOのAPIのURL        |
| ロググループID  | log\_group\_id      |           | integer | null       | リクエスト毎に付けられる一連の処理のID |
| 機能ID         | operation\_type\_id |           | integer | -          | 各処理の大項目。マスタを参照する。     |
| 処理ID         | operation\_id       |           | integer | -          | 各処理に対するID。マスタを参照する。   |
| 対象           | target              |           | string  | null       | 操作の対象                           |
| 対象キー       | target\_key         |           | string  | null       | 操作対象のID                         |

サンプル
```json
{
    "id": 5,
    "log_level": "ERROR",
    "date":"2025/02/21 7:38:19.201",
    "user_id": 1,
    "eppn": null,
    "ip_address":"192.168.56.1",
    "client_id":"Z6DWfNWrrGwEYvh5Dcf81SSkrH6BiqIja17Cu2Hs",
    "community_id": "ccp",
    "source": "/sword/service-document",
    "log_group_id": 2,
    "operation_type_id": 10,
    "operation_id": 2,
    "target":"item",
    "target_key":"2000001"
}
```


### 処理概要

- メソッドの引数から機能ID、処理ID、対象キー、備考を受け取る
- flaskパッケージのrequestやcurrent\_userから値を取得する
    - requestから取得するもの：source、ip\_address、client\_id
    - current\_userから取得するもの：user\_id
- DBと標準出力にログを出力する
    - DBに書き込むときのフォーマット標準出力のフォーマットの定義は別にする
    - 日時はDBと標準出力で同じにする

## 監査ログ削除

### 機能内容

- 基本監査ログのDB保持期間を設定し、その期間を超えたログを削除する

### 処理概要

- [設定値](#設定値) の WEKO\_LOGGING\_USER\_ACTIVITY\_SETTINGにある 「delete」キーの情報から設定期間を読み込む
    - 設定できる期間は任意の日、週、月、年とする
- 設定期間を超えたログをDBから物理削除する
  - バッチは一日に一回の間隔で回す


## 更新履歴

| 日付       | GitHubコミットID | 更新内容 |
| ---------- | ---------------- | -------- |
| 2025/06/06 | d4285ebc75428677dc8c314171a631c6bbb1bfee | 初版作成 |
