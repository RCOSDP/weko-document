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
