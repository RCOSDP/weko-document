# RO-Crate インポート

## 目的・用途
本機能は、管理者として、RO-Crate+BagItファイルをインポートし、データを登録する機能である。

## 利用方法
管理者は 【Administration > アイテム管理（Items） > RO-Crate インポート（RO-Crate Import）】を開き、アイテム登録用のRO-Crate+BagItファイルを登録する。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       〇       |        〇        |         〇         |      ×      |      ×      |        ×          |

※コミュニティ管理者は、自身の管理下にあるコミュニティに関連付けられたインデックスへのインポートのみ可能

## 機能内容

- RO-Crate+BagItファイルをインポートし、アイテムを登録する。
- RO-Crate+BagItファイルに含まれる`ro-crate-metadata.json`ファイルを読み込み、アイテムのメタデータへマッピングする。
- WEB APIを利用してDOIによるメタデータ補完を提供する。

## 画面仕様

## RO-Crate+BagItファイルの構成
RO-Crate+BagItファイルは、以下の構成である必要がある。

```plaintext
./ (bagit root)
 ├── bagit.txt
 ├── bag-info.txt
 ├── data/
 │    └── <Files>
 ├── ro-crate-metadata.json
 ├── manifest-sha256.txt
 └── tagmanifest-sha256.txt
```

| ファイル or ディレクトリ | 必須 | 詳細                                                                          |
| :----------------------- | :--: | :---------------------------------------------------------------------------- |
| bagit.txt                |  ◯  | BagItファイルの宣言                                                           |
| bag-info.txt             |      | Bagに関するメタデータを含むファイル                                           |
| data/                    |  ◯  | ペイロードディレクトリ。 配下のファイルはマニフェストの妥当性により担保される |
| ro-crate-metadata.json   |  ◯  | アイテムのメタデータがJSON-LD形式で記述されたファイル                         |
| manifst-sha256.txt       |  ◯  | data/内の各ファイルのSHA-256チェックサムをまとめたマニフェストファイル        |
| tagmanifst-sha256.txt    |      | data/外の各ファイルのSHA-256チェックサムをまとめたマニフェストファイル        |

## メタデータ記述
アイテムのメタデータは、`ro-crate-metadata.json`ファイルにJSON-LD形式で記述される。  
`@graph`には、アイテムのメタデータを記述するエンティティが配列で格納される。  
`@id`は、エンティティの識別子を示し、リンクトデータとしての参照先を示す。  
すべてのメタデータは、ルートデータセット（`@id: ./`）に記述される。

```jsonc
// ro-crate-metadata.json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Sample Dataset",
      "description": "This is a sample dataset.",
      "datePublished": "2025-03-01",
      "creator": [ {"@id": "_:creator"} ],
      "hasPart": [ {"@id": "data/sample.txt"} ]
    },
    {
      "@id": "_:creator",
      "@type": "Person",
      "name": "John Doe"
    },
    {
      "@id": "data/sample.txt",
      "@type": "File",
      "name": "sample.txt"
    }
  ]
}
```

## カスタム語彙
RO-Crate+BagItファイルに含まれる`ro-crate-metadata.json`ファイルには、システム向け情報が含まれている。  
RO-Crateには、アイテムのメタデータを記述するための語彙が定義されているが、WEKO3のシステム向け情報は表現することができない。  
そのため、カスタム語彙を定義して記述されているため、インポート処理においては、これらを解析し、システム向け情報を取得する。

### 使用語彙
TSV形式のメタデータ項目とシステム向け語彙について、定義したカスタム語彙を以下に示す。  
カスタム語彙はプレフィックスとして、`wk:`が付与されている。  
インポート時に必須である項目は、インデックスIDと公開ステータスである。

| 使用語彙                                   | 対応するTSV項目名    | バリュータイプ     | デフォルト値 | 親エンティティタイプ | 説明                     |
| ------------------------------------------ | -------------------- | ------------------ | ------------ | -------------------- | ------------------------ |
| identifier                                 | ID                   | 整数値             | -            | Dataset              | アイテムID               |
| uri                                        | URI                  | URL                | -            | Dataset              | アイテムのURI            |
| wk:index                                   | .IndexID             | 配列               | -            | Dataset              | インデックスID           |
| wk:publishStatus                           | .PUBLISH_STATUS      | 文字列             | -            | Dataset              | 公開ステータス           |
| wk:feedbackMail                            | .FEEDBACK_MAIL       | 文字列             | -            | Dataset              | フィードバックメール     |
| wk:requestMail                             | .REQUEST_MAIL        | 文字列             | -            | Dataset              | リクエストメール         |
| wk:grant.@id                               | .CNRI                | URL                | -            | Dataset              | CNRI                     |
| wk:grant.@id                               | .DOI                 | URL                | -            | Dataset              | DOI                      |
| wk:grant<br>.jpcoar:identifierRegistration | .DOI_RA              | URL                | -            | Dataset              | DOI_RA                   |
| wk:editMode                                | Keep/Upgrade Version | 文字列             | -            | Dataset              | Keep/Upgrade Version     |
| wk:itemLinks.identifier                    | -                    | 整数値 or 文字列   | -            | File                 | アイテムリンク先識別子   |
| wk:itemLinks.value                         | -                    | 文字列             | -            | File                 | アイテムリンクタイプ     |
| wk:textExtraction                          | -                    | 真偽値             | true         | File                 | 全文検索用本文抽出フラグ |
| wk:saveAsIs                                | -                    | 真偽値             | false        | Dataset              | 登録用ファイル保存フラグ |
| wk:isSplited                               | -                    | 真偽値             | false        | File                 | アイテム分割フラグ       |

### wk:index：インデックスID

アイテムの登録先インデックスIDを配列で指定する。ルートデータセット直下に記述する。

```json
{
  "@id": "./",
  "wk:index": ["1623632832836"]
}
```

### wk:publishStatus：公開ステータス

アイテムの公開ステータスを指定する。ルートデータセット直下に記述する。  
公開ステータスは、`public`または`private`を指定する。

```json
{
  "@id": "./",
  "wk:publishStatus": "public"
}
```

### wk:feedbackMail：フィードバックメール

アイテムに紐づけるフィードバックメールアドレスを指定する。ルートデータセット直下に記述する。

```json
{
  "@id": "./",
  "wk:feedbackMail": ["wekosoftware@nii.ac.jp"]
}
```

### wk:grant：識別子付与（CNRI、DOI）

アイテムに識別子を付与するための情報を指定する。ルートデータセット直下に記述する。  
識別子変更モードでなければ、識別子は自動採番によって付与されるため、指定する必要はない。  
識別子の種類を`jpcoar:identifier`で`HDL`または`DOI`で指定し、識別子は`plefix/suffix`の形式で`@id`に指定する。  
DOI発行機関を指定する場合は、`jpcoar:identifierRegistration`で指定する。

```json
{
  "@id": "./",
  "wk:grant": [
    {"@id": "1234/5678"},
    {"@id": "10.1234/5678"}
  ],
},
{
  "@id": "1234/5678",
  "@type": "Property ",
  "jpcoar:identifier": "HDL"
},
{
  "@id": "10.1234/5678",
  "@type": "Property ",
  "jpcoar:identifier": "DOI",
  "jpcoar:identifierRegistration": "DataCite"
}
```

### wk:editMode：

アイテムの編集時のモードを指定する。ルートデータセット直下に記述する。  
`Keep`または`Upgrade Version`を指定する。


```json
{
  "@id": "./",
  "wk:editMode": "Keep"
}
```

### wk:requestMail：リクエストメール

ワークフロー使用時にアクティビティに紐づけるリクエストメールアドレスを指定する。ルートデータセット直下に記述する。

```json
{
  "@id": "./",
  "wk:requestMail": ["wekosoftware@nii.ac.jp"]
}
```

### wk:itemLinks：アイテムリンク

アイテムにリンクを設定する。`wk:itemLinks`は、`identifier`と`value`の2つのプロパティを持つ。  
`identifier`はアイテムリンク先のアイテムIDを指定し、`value`はアイテムリンクのリレーションタイプを指定する。
ルートデータセット直下に記述する。

```json
{
  "@id": "./",
  "wk:itemLinks": [
    {"@id": "_:itemLink"}
  ]
},
{
  "@id": "_:itemLink",
  "@type": "PropertyValue",
  "value": "isSupplementedBy",
  "identifier": "https://example.repo.nii.ac.jp/records/123456789"
},
```

### wk:textExtraction：全文検索用本文抽出フラグ

WEKO3では、アイテムの全文検索を行うために、アイテム登録時にファイルの本文を抽出し、Elasticsearchに登録する。  
本文抽出を行わない場合は、ファイルのメタデータとして`wk:textExtraction`を`false`に設定する。デフォルト値は`true`である。

```json
{
  "@id": "data/sample.txt",
  "neme": "sample.txt",
  "wk:textExtraction": false
}
```

### wk:saveAsIs：登録用ファイル保存フラグ<span id="saveAsIs">

RO-Crate+BagItファイルをインポート時するとき、デフォルトではZIPファイルを展開し、dataディレクトリ内のファイルを登録する。  
ファイルを展開せずにZIPファイルをそのまま登録する場合は、`wk:saveAsIs`を`true`に設定する。デフォルト値は`false`である。  
ルートデータセット直下に記述する。

```json
{
  "@id": "./",
  "wk:saveAsIs": true
}
```

### wk:isSplited：アイテム分割フラグ<span id="isSplited">

WEKO3においてRO-Crateは、SWORD APIを利用してアイテムを登録する際に使用することを前提としている。  
原則として、RO-Crate+BagItファイルに含まれるアイテムは、1つのアイテムとして登録される。  
例外的にアイテムを複数に分割して登録する場合は、`wk:isSplited`を`true`に設定する。デフォルト値は`false`である。ルートデータセット直下に記述する。  
分割するとき、`hasPart`プロパティを使用して、個別のアイテムを指定する。  
メタデータは個別のアイテムをルートデータセットとみなして記述する。

以下の例は、論文アイテムとその論拠データアイテムに分割して登録する場合の例である。  
アイテムはアイテムは`{"@id": "_:item1"}`と`{"@id": "_:item2"}`の2つに独立した状態で分割されるため、メタデータはそれぞれのアイテムに記述する。
また、相互のアイテムは`wk:itemLinks`プロパティを使用してアイテムリンクを設定する。

```json
{
  "@id": "./",
  "hasPart": [
    {"@id": "_:item1"},
    {"@id": "_:item2"}
  ],
  "wk:isSplited": true
},
{
  "@id": "_:item1",
  "datePublished": "2025-03-01",
  "wk:itemLinks": [{"@id": "_:itemLink1"}]
},
{
  "@id": "_:item2",
  "datePublished": "2025-03-01",
  "wk:itemLinks": [{"@id": "_:itemLink2"}]
},
{
  "@id": "_:itemLink1",
  "@type": "PropertyValue",
  "value": "isSupplementedBy",
  "identifier": "_:item2"
},
{
  "@id": "_:itemLink2",
  "@type": "PropertyValue",
  "value": "isSupplementTo",
  "identifier": "_:item1"
}
```

## マッピング機能
RO-Crate+BagItファイルに含まれる`ro-crate-metadata.json`ファイルを読み込み、あらかじめ設定されたマッピング定義に基づいてJSON-LD形式で記述されたメタデータをアイテムタイプへマッピングする。

### 語句

- **JSON-LD形式のメタデータ**：  
  JSON-LD（JavaScript Object Notation for Linked Data）で記述されたアイテムのメタデータ。  
  インポート対象のRO-Crate+BagItファイルに含まれる`ro-crate-metadata.json`ファイルの内容がこれに該当する。
- **マッピング定義**：  
  JSON-LD形式で記述されたメタデータをアイテムタイプへマッピングするための定義。  
  マッピング定義は、[ADMIN_1_5：JSON-LD マッピング](ADMIN_1_5.md)でユーザーによって定義される。

### 処理概要

- JSON-LD形式のメタデータの読み込み
- マッピング定義の読み込み
- カスタム語彙で指定されたシステム向け情報の取得
- マッピング処理の実行

### マッピング定義
マッピング定義は以下のようなJSON形式で記述される。

```jsonc
{
  "Title": "dc:title",
  "Title.タイトル": "dc:title.value",
  "Title.言語": "dc:title.language",
  "メタデータ登録日.日付": "dateCreated",
  "メタデータ登録日.日付タイプ": "$Created",
  "Creator": "creator",
  "Creator.作成者姓名.姓名": "creator.name",
}
```

| アイテムタイプのプロパティのパス | JSON-LDのメタデータのパス | 説明                                                                  |
| -------------------------------- | ------------------------- | --------------------------------------------------------------------- |
| Title                            | dc:title                  | アイテムタイプの "Title" に対応するメタデータのパス                   |
| Title.タイトル                   | dc:title.value            | アイテムタイプの "Title.タイトル" に対応するメタデータのパス          |
| Title.言語                       | dc:title.language         | アイテムタイプの "Title.言語" に対応するメタデータのパス              |
| メタデータ登録日.日付            | dateCreated               | アイテムタイプの "メタデータ登録日.日付" に対応するメタデータのパス   |
| メタデータ登録日.日付タイプ      | $Created                  | アイテムタイプの "メタデータ登録日.日付タイプ" に対応する固定値       |
| Creator                          | creator                   | アイテムタイプの "Creator" に対応するメタデータのパス                 |
| Creator.作成者姓名.姓名          | creator.name              | アイテムタイプの "Creator.作成者姓名.姓名" に対応するメタデータのパス |


## メタデータ補完機能

## 関連モジュール

- weko_search_ui：インポート処理およびマッピング処理を実行する

## 関連テーブル

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                        |
| ---------- | ------------------------------------------ | ----------------------------------------------- |
| 2024/03/07 |                                            | 初版作成                                        |
