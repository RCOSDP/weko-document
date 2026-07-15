## 未病データベース GakuNin RDMボタン表示

アイテム詳細画面のGakuNin RDM(以下GRDM)ボタンの表示について記述する。

### 用語説明

本書では以下の用語で統一する。

  | 用語 | 説明 |
  | ---- | ---- |
  | フロント | 未病データベースのフロントエンド |
  | WEKO | 未病データベース用のWEKO3リポジトリ（バックエンド） |
  | プロジェクトURL | GRDMのプロジェクトや共有リクエストのURL  |

### 1. RO-CrateからWEKOのアイテムへの変換

プロジェクトURLはRO-Crate内で`ams:projectId`として記述される。
WEKOのJSON-LDマッピング機能( [ADMIN_1_5：JSON-LDマッピング](../admin/ADMIN_1_5.md) )を使用して、`ams:projectId`を未病アイテムタイプのプロジェクトURL(関連情報プロパティ)にマッピングする。

`ams:projectId`を`プロジェクトURL.関連識別子.関連識別子`にマッピングする。(以下、関連識別子とする。)
`プロジェクトURL.関連タイプ`には固定値で後述の`grdm.relationType` の値をマッピングする。(以下、関連タイプとする。)
JSON-LDマッピング機能により、`ams:projectId`が存在する場合のみ関連タイプが登録される。

> WEKO実装（v2.0.2）：JSON-LDマッピング機能は weko-admin の「SWORD API JSON-LDマッピング設定」画面（`SwordAPIJsonldSettingsView`）として提供される。マッピング定義はテーブル `jsonld_mappings`（モデル `ItemTypeJsonldMapping`、API `weko_records.api.JsonldMapping`）に保持され、変換処理は `weko_search_ui.mapper.JsonLdMapper` が担う。固定値のマッピング（例：`"$isVersionOf"`）は先頭 `$` による固定値指定記法で表現される。関連モジュール：weko-admin / weko-records / weko-search-ui。

- RO-Crateの例
  ```json
  "@id": "./",
  "@type": "Dataset",
  "name": "Sample Dataset",
  "description": "This is a sample dataset.",
  "datePublished": "2025-03-01",
  "ams:projectId":{
    "value": "https://rdm.nii.ac.jp/"
  }
  ```

- RO-Crateに対応するマッピング定義の例
  ```json
  "プロジェクトURL": "ams:projectId",
  "プロジェクトURL.関連識別子.関連識別子": "ams:projectId.value",
  "プロジェクトURL.関連タイプ": "$isVersionOf",
  ```

### 2. WEKOのアイテムからRO-Crateへの変換

アイテム取得API (`/api/v1/records/<アイテムID>`)使用時、WEKOのRO-Crateマッピング機能を使用し、関連識別子と関連タイプを以下のキーにマッピングする。

> WEKO実装（v2.0.2）：アイテム取得API `GET /api/v1/records/<id>` は weko-records-ui の `WekoRecordsResource.get_v1`（`rest.py`、`WEKO_RECORDS_UI_REST_ENDPOINTS` の `item_route`）が担当する（invenio-records-rest の `/api/records` とは別系統）。RO-Crate変換は `RoCrateConverter`（`weko_records_ui.utils`）が行い、変換定義はテーブル `rocrate_mapping`（モデル `RocrateMapping`）に保持される。レスポンスは `index` / `rocrate` / `metadata` を含み、`metadata.hasRequestmailAddress`（リクエストメールアドレスの有無）も返す。関連タイプ・関連識別子は jpcoar の `relatedIdentifier`（`relationType`）としてマッピングされる。

- 関連識別子
  - ツリー構造: root > プロジェクトURL > URL > URL
  - RO-Crateのキー: `text`
- 関連タイプ
  - ツリー構造: root > プロジェクトURL > 関連タイプ > 関連タイプ
  - RO-Crateのキー: `text`

### 3. フロントでのGRDMボタン表示

WEKOのアイテム詳細情報取得APIを使用し、RO-Crateから関連識別子と関連タイプを取得する。
関連識別子と関連タイプが以下の2条件を共にみたす場合、関連識別子をプロジェクトURLとして扱う。

- `nginx/ams/weko-frontend/app.config.ts` で設定した `grdm.url` の値が`''`(空文字列)の場合、関連識別子が空でないこと。
  `nginx/ams/weko-frontend/app.config.ts` で設定した `grdm.url` の値が`''`(空文字列)でない場合、関連識別子が `grdm.url` の値から始まること
- 関連タイプが `nginx/ams/weko-frontend/app.config.ts` で設定した `grdm.relationType` の値と一致すること

プロジェクトURLが設定されている場合、ユーザのログイン状態に関わらずアイテム詳細画面にGRDMボタンを表示する。
ユーザがGRDMボタンを押下した場合は、プロジェクトURLを新規ウィンドウで開く。
GRDMボタンを表示している場合、リクエストボタンとその表示領域は非表示とする。

### 更新履歴

| 日付         | GitHubコミットID | 更新内容   |
|--------------|------------------|------------|
| 2025/08/29   |    6ee63da44c8f2e23ac73d6218ee09f23ba5edcb3   | 初版作成   |
| 2026/07/14   |  | 実装(v2.0.2)と突き合わせ。JSON-LDマッピング（SWORD API JSON-LD設定/`JsonLdMapper`）とRO-Crate変換（`RoCrateConverter`/`rocrate_mapping`/`WekoRecordsResource.get_v1`）のバックエンド実装を追記 |
