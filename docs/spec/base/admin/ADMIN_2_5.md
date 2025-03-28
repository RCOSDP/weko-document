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
アイテムとして登録するファイルは、`data/`ディレクトリに格納される。  
参照：[Adding RO-Crate to Bagit](https://www.researchobject.org/ro-crate/specification/1.1/appendix/implementation-notes.html)  


```plaintext
./ (bagit root)
 ├── bagit.txt
 ├── bag-info.txt
 ├── data/
 │    ├── ro-crate-metadata.json
 │    └── <Files>
 ├── manifest-sha256.txt
 └── tagmanifest-sha256.txt
```

| ファイル or ディレクトリ | 必須 | 詳細                                                                          |
| :----------------------- | :--: | :---------------------------------------------------------------------------- |
| bagit.txt                |  ※  | BagItファイルの宣言                                                           |
| bag-info.txt             |      | Bagに関するメタデータを含むファイル                                           |
| data/                    |  ※  | ペイロードディレクトリ。 配下のファイルはマニフェストの妥当性により担保される |
| ro-crate-metadata.json   |  ◯  | アイテムのメタデータがJSON-LD形式で記述されたファイル                         |
| manifst-sha256.txt       |  ※  | data/内の各ファイルのSHA-256チェックサムをまとめたマニフェストファイル        |
| tagmanifst-sha256.txt    |      | data/外の各ファイルのSHA-256チェックサムをまとめたタグマニフェストファイル    |

ただし、この機能からのインポート時には、`data/` ディレクトリ以外は無視する。  
※ この機能からインポートする際には必須でないが、SWORD APIを利用してアイテムを登録する際にはファイルの検証のため必須になるファイル。


## メタデータ記述
アイテムのメタデータは、`ro-crate-metadata.json`ファイルにJSON-LD形式で記述される。  
`@graph`には、アイテムのメタデータを記述するエンティティが配列で格納される。  
`@id`は、エンティティの識別子を示し、リンクトデータとしての参照先を示す。  
すべてのメタデータは、ルートデータセット（`{"@id": "./"}`）に記述され、
ここにリンクトデータとしての参照先が指定されていないエンティティは、インポート時にすべて無視される。  
また、ルートデータセットを指定するエンティティ（`{"@id": "ro0crate-metadata.json"}`）が必須である。

```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      }
    },
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

また、アイテムの含まれるすべてのファイルのメタデータは、`hasPart`プロパティを使用して指定する。  
ここでは、すべてのファイルを`data/`ディレクトリ以下の相対パスで表現する。  
[アイテム分離](#wkissplitedアイテム分割フラグ)の場合を除き、ルートデータセット以外のエンティティに`hasPart`プロパティにファイルを指定しても無視される。

```json
{
  "@id": "./",
  "hasPart": [
    {"@id": "data/sample.txt"},
    {"@id": "data/img/sample.jpg"}
  ]
},
{
    "@id": "data/sample.txt",
    "@type": "File",
    "name": "sample.txt",
    "contentSize": "1024 KB" ,
    "fileFormat": "text/plain"
},
{
    "@id": "data/img/sample.jpg",
    "@type": "File",
    "name": "sample.jpg",
    "contentSize": "2048 MB" ,
    "fileFormat": "image/jpeg"
}
```

## カスタム語彙
RO-Crate+BagItファイルに含まれる`ro-crate-metadata.json`ファイルには、システム向け情報が含まれている。  
RO-Crateには、アイテムのメタデータを記述するための語彙が定義されているが、WEKO3のシステム向け情報は表現することができない。  
そのため、カスタム語彙を定義して記述されているため、インポート処理においては、これらを解析し、システム向け情報を取得する。

### 使用語彙
TSV形式のメタデータ項目とシステム向け語彙について、定義したカスタム語彙を以下に示す。  
カスタム語彙はプレフィックスとして、`wk:`が付与されている。  
新規登録としてインポートする際に必須である項目は、インデックスIDと公開ステータスである。  
更新登録としてインポートする際に追加で必須になる項目は、アイテムIDとURIである。  
一部の語彙は、この機能では使用せず、SWORD APIを利用してアイテムを登録する際に使用することを前提としている。

| 使用語彙                                   | 対応するTSV項目名    | バリュータイプ     | デフォルト値 | 新規 | 更新 | 説明                                     |
| ------------------------------------------ | -------------------- | ------------------ | ------------ | :--: | :--: | ---------------------------------------- |
| identifier                                 | ID                   | 整数値             | -            | ×   | 〇   | アイテムID                               |
| uri                                        | URI                  | URL                | -            | ×   | 〇   | アイテムのURI                            |
| wk:index                                   | .IndexID             | 配列               | -            | 〇   | 〇   | インデックスID                           |
| wk:publishStatus                           | .PUBLISH_STATUS      | 文字列             | -            | 〇   | 〇   | 公開ステータス                           |
| wk:feedbackMail                            | .FEEDBACK_MAIL       | 文字列             | -            |      |      | フィードバックメール                     |
| wk:requestMail                             | .REQUEST_MAIL        | 文字列             | -            |      |      | リクエストメール                         |
| wk:grant.@id                               | .CNRI                | URL                | -            |      |      | CNRI                                     |
| wk:grant.@id                               | .DOI                 | URL                | -            |      |      | DOI                                      |
| wk:grant<br>.jpcoar:identifierRegistration | .DOI_RA              | URL                | -            |      |      | DOI_RA                                   |
| wk:editMode                                | Keep/Upgrade Version | 文字列             | -            |      | 〇   | Keep/Upgrade Version                     |
| wk:itemLinks.identifier                    | -                    | 整数値 or 文字列   | -            |      |      | アイテムリンク先識別子（SWORD経由のみ）  |
| wk:itemLinks.value                         | -                    | 文字列             | -            |      |      | アイテムリンクタイプ （SWORD経由のみ）   |
| wk:textExtraction                          | -                    | 真偽値             | true         |      |      | 全文検索用本文抽出フラグ                 |
| wk:saveAsIs                                | -                    | 真偽値             | false        |      |      | 登録用ファイル保存フラグ                 |
| wk:isSplited                               | -                    | 真偽値             | false        |      |      | アイテム分割フラグ （SWORD経由のみ）     |
| wk:metadataAutoFill                        | -                    | 真偽値             | false        |      |      | メタデータ自動補完フラグ                 |
| wk:metadataReplace                         | -                    | 真偽値             | false        |      |      | メタデータのみ置換フラグ（SWORD経由のみ）|

※ 登録用ファイル保存フラグとアイテム分割フラグが両方`true`の場合、アイテム分割フラグが優先され、ファイルは展開されて保存される。

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
`Keep`または`Upgrade`を指定する。


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
SWORD APIを利用時、ワークフローを経由してアイテムを登録する際に使用することを前提としている。

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

WEKO3では、アイテム登録時に本文ファイルのテキストを抽出し、アイテムの全文検索に利用している。  
本文抽出を行わない場合は、ファイルのメタデータとして`wk:textExtraction`を`false`に設定する。デフォルト値は`true`である。

```json
{
  "@id": "data/sample.txt",
  "@type": "File",
  "neme": "sample.txt",
  "wk:textExtraction": false
},
{
  "@id": "/data/result.csv",
  "@type": "File",
  "name": "result.csv",
  "wk:textExtraction": true
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
例外的にアイテムを複数に分割し、ワークフローを経由して登録する場合は、`wk:isSplited`を`true`に設定する。デフォルト値は`false`である。ルートデータセット直下に記述する。  
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

### wk:metadataAutoFill：メタデータ自動補完フラグ

アイテムのメタデータを自動補完するかどうかを指定する。ルートデータセット直下に記述する。  
"jpcoar:relation"プロパティで関連情報として`cite_as`にDOIを指定すると、そのDOIを利用してメタデータを補完する。  
このとき、`relationType`プロパティに`isVersionOf`を指定する必要がある。  
関係情報が複数記述されるとき、はじめて`relationType`プロパティに`isVersionOf`を指定したものが対象となる。  
自動補完機能については、[メタデータ補完機能](#メタデータ補完機能)を参照。

```json
{
  "@id": "./",
  "jpcoar:relation": [{ "@id": "_:Relation1" }, { "@id": "_:Relation2" }],
  "wk:metadataAutoFill": true
},
{
  "@id": "_:Relation1",
  "relationType": "isVersionOf",
  "cite-as": "https://doi.org/10.34477/0002000074"
}
```

### wk:metadataReplace：メタデータのみ置換フラグ

SWORD APIを利用してアイテムを登録する際に、メタデータのみを置換するかどうかを指定する。ルートデータセット直下に記述する。  
暫定的に使用するフラグであり、将来的には廃止される予定である。

```json
{
  "@id": "./",
  "wk:metadataReplace": true
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

## 本文抽出選択機能

WEKO3では、アイテムの全文検索に使用するのために本文ファイルのテキストを抽出し、Elasticsearchに登録する。  
本文ファイルをあえて全文検索対象から外したいというユースケースに対応するため、RO-Crateに含まれるメタデータ情報をもとに、全文検索機能の要不要を指定できる機能を提供する。  
[全文検索用本文抽出フラグ](#wktextextraction全文検索用本文抽出フラグ)を使用して、本文抽出を行わないファイルを指定する。  



## 関連モジュール

- weko_search_ui：インポート処理およびマッピング処理を実行する

## 関連テーブル

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                        |
| ---------- | ------------------------------------------ | ----------------------------------------------- |
| 2024/03/07 |                                            | 初版作成                                        |
