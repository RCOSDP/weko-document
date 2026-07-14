### Google Dataset メタデータ出力

#### 目的・用途

本機能は、Google Dataset Search向けのメタデータを出力する機能である。

#### 利用方法

アイテムリストから特定のアイテムを選択することで、アイテム詳細画面を構成する要素、構造化データのheaderのタグの一つとして、Google Dataset meta tagが付与されたアイテムメタデータが表示される。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

#### 機能内容

  - Google Dataset meta tagを利用することで、データ検索に特化したGoogle Dataset Searchにメタデータ を登録することが出来る。

      - meta tagはSchema.orgを利用する。  
        <https://schema.org/>

  - 当該アイテムがOAIPMH出力されること

      - Google Dataset の実装にはGoogle Dataset meta tagが必要である。meta tag はOAI-PMHのXML出力と同じ機能を用いて出力される。

          - そのため、OAI-PMH出力をしなければ、Google Scholar meta tagは出力されない。OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。

  - 当該アイテムのアイテムタイプがJPCOARスキーマにマッピングされていること

  - dc:typeがdatasetであること

  - dc:titleが入力されていること

  - datacite:descriptionが50字以上であること

#### 関連モジュール

  - weko_records_ui

#### 処理概要

1. 設定

Google Dataaset出力をすることのできるリソースタイプ

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L577>

  - 設定キー：  
    「WEKO_RECORDS_UI_GOOGLE_DATASET_RESOURCE_TYPE = [“dataset”]」

Google Dataset descriptionの最小文字数

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L580>

  - 設定キー：  
    「WEKO_RECORDS_UI_GOOGLE_DATASET_DESCRIPTION_MIN = 50」

Google Dataset descriptionの最大文字数

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L582>

  - 設定キー：  
    「WEKO_RECORDS_UI_GOOGLE_DATASET_DESCRIPTION_MAX = 5000」

「WEKO_RECORDS_UI_GOOGLE_DATASET_DISTRIBUTION_BUNDLE」

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L585-L592>

jpcoarマッピングとGoogle Dataset meta tagとの対応:  
別紙「jpcoarスキーマ、schema.org対応表」参照。

2. 実装方法

アイテムリストから特定のアイテムを選択し、アイテム詳細画面を表示する際に、get_google_dataset_metaを使用して、画面を構成する要素として、Google Dataset meta tagをheaderのテンプレートに埋め込む。

  - weko_records_ui.views.default_view_methodからweko_records_ui.utils.get_google_dataset_metaを呼び出して使用する。

  - アイテムの識別子としてoaiが含まれているかを確認する。

      - OAI-PMH出力で使用されるjpcoarマッピングと置き換える形でGoogle Dataset meta tagを付与するため、OAI-PMH出力が出来る状態でなければGoogle Dateset meta tagを出力することは出来ない。

          - 【前提条件】  
            USER3-7「1. OAI-PMHスキーマを管理」及び「2. OAI-PMHスキーマをマッピング」が設定済み

  - リソースタイプがdatasetか確認する。

  - Google Datasetにおけるデータの説明部分であるdescriptionが50字以上か確認する。5000字よりも多い場合、5000字以降は切り捨てて登録する。

  - メタデータに含まれるjpcoarタグの種類に対応するGoogle Dataset meta tagをres_dataリストに追加する。

resリストをgoogle_dataset_metaで受け取り、templating.render_templateを呼び出してアイテムメタデータを作成する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足（訂正）：関数名は `weko_records_ui.utils.get_google_detaset_meta`（ソースの綴りが "detaset"。`get_google_dataset_meta` は存在しない）。出力は dict（`@context`/`@type`:Dataset ...）。config `WEKO_RECORDS_UI_GOOGLE_DATASET_RESOURCE_TYPE`/`_DESCRIPTION_MIN`(50)/`_MAX`(5000)。`WEKO_RECORDS_UI_GOOGLE_DATASET_DISP_FLG` は定義のみで未使用。出力可否は Scholar 用 resource_type config を参照する。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
