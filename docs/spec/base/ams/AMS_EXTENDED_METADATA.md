# 未病データベース 拡張メタデータ対応

## 概要

JSON-LDマッピング機能を使用したアイテム登録・更新で拡張メタデータのファイルを受け取った場合、ファイルの内容をテキストエリアに登録する。

### 用語説明

| 用語 | 説明 |
| ---- | ---- |
|拡張メタデータ|通常のメタデータに加えて、ファイルやデータの内容そのものを含めて保存・管理するための追加情報|
|SWORD API|学術リポジトリなどにコンテンツを自動的に登録・更新するための標準的なプロトコル|

## 変更対象箇所
JSON-LDマッピング機能を使用してアイテムを登録・更新する以下の処理
- SWORD API (直接登録)
- SWORD API (ワークフロー登録)
- RO-Crateインポート

## 処理内容

### 拡張メタデータファイルの判定

拡張メタデータ判定用のwkコンテキスト(`wk:extendedMetadata`)を追加する。  
`"hasPart"`で定義されたファイルの`"wk:extendedMetadata"`が`true`の場合、拡張メタデータファイルとして扱う。

上記の判定に従って拡張メタデータとして判定するファイルの例:

```json
{
    "hasPart": [
        {
            "@id": "data/metadata.txt"
        }
    ]
},
{
    "@id": "data/metadata.txt",
    "wk:extendedMetadata": true,
    "name": "metadata.txt",
}
```

### 拡張メタデータファイルからJSON-LDへの変換

ファイルが拡張メタデータであると判定した場合、ファイルの内容を以下のJSON形式に変換する。

```json
{
    "extended_metadata": {
        "<ファイル名1>": "<ファイル1の内容>",
        "<ファイル名2>": "<ファイル2の内容>"
    }
}
```
- ファイル名とファイルの内容をkey-valueとして保存する
- 拡張メタデータファイルの`@id`は`hasPart`から削除する
- 拡張メタデータはファイルとして送られてくるため、もとのJSON-LD内に`extended_metadata`のキーがあっても無視する
- 既存の本文抽出機能と同様に`WEKO_DEPOSIT_FILESIZE_LIMIT`の値(デフォルト: 2MB)を上限として読み込む
- 既存の機能と同様、本文抽出の対象は`mimetype`が`WEKO_MIMETYPE_WHITELIST_FOR_ES`であるものとする


#### `WEKO_MIMETYPE_WHITELIST_FOR_ES` のデフォルト値

- `text/plain`
- `text/csv`
- `text/html`
- `text/tab-separated-values`
- `text/xml`
- `application/x-tex`
- `application/x-latex`
- `application/msword`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.ms-excel`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.oasis.opendocument.spreadsheet`
- `application/vnd.ms-powerpoint`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.oasis.opendocument.presentation`
- `application/pdf`

### JSON-LDからプロパティへのマッピング

- アイテムタイプに拡張メタデータ用のテキストエリアプロパティをhide属性で追加する
- hide属性に設定することにより、権限のないユーザーはアイテムエクスポート時に拡張メタデータをエクスポートできない
- `extended_metadata`から作成したアイテムタイプへのマッピングを定義することにより、拡張メタデータが保存される

#### 作成したアイテムタイプへのマッピング定義の例

ここでは`拡張メタデータ`という名前のテキストエリアプロパティを作成したものとする。

```json
{
    "拡張メタデータ": "extended_metadata",
    "拡張メタデータ.値": "extended_metadata.value"
}
```

### アイテム更新時

既存の更新処理同様、拡張メタデータ含めて更新前のメタデータを更新後のメタデータで全て上書きする。  
SWORD APIやRO-Crateインポートによる更新で拡張メタデータのファイルが送られてこなかった場合、テキストエリアプロパティ内の拡張メタデータは削除される。

## 処理概要

### 拡張メタデータのファイルからメタデータへの変換
- JSON-LDの`hasPart`から、`wk:extendedMetadata`が`true`に設定されているものを確認する
- `wk:extendedMetadata`が`true`であるファイルの`@id`は`hasPart`から削除する
- `wk:extendedMetadata`が`true`であるファイルに対し、後述の本文抽出処理を適用し、本文を抽出する
- もとのメタデータの入った辞書のキー`extended_metadata`に `{ファイル名: 本文}`という辞書形式で拡張メタデータを保存する

### 本文抽出処理

- 指定したファイルがフォルダ内に存在するか確認し、存在しない場合は`FileNotFoundError`を発生させる
- PDFファイルが壊れていたり、サポートされていない形式であることにより、読み込みや解析に失敗した場合は、`PdfiumError`を発生させる
- ファイル名からMIMETYPEを判定する
- MIMETYPEが設定値の`WEKO_MIMETYPE_WHITELIST_FOR_ES`にない場合、空文字列を返して終了する
- MIMETYPEが設定値の`WEKO_MIMETYPE_WHITELIST_FOR_ES`にある場合
    - MIMETYPEが設定値の`WEKO_DEPOSIT_TEXTMIMETYPE_WHITELIST_FOR_ES` にある場合はファイルの内容をそのまま抽出する
    - MIMETYPEが`application/pdf`の場合は既存の関数の`extract_text_from_pdf`を呼び出し本文を抽出する
    - MIMETYPEがそれ以外の場合は既存の関数の`extract_text_with_tika`を呼び出し本文を抽出する
    - 上記の3パターンとも、設定値の`WEKO_DEPOSIT_FILESIZE_LIMIT`を上限として読み込む
- 抽出した本文を返して終了する


## 更新履歴

|日付|更新内容|
| --- | --- |
| 10/14 | 初版 |
| 10/21 | 10/20の定例で決まった内容を反映 <br> ( 拡張メタデータのファイル名を保存する <br> 拡張メタデータのマッピング先を`Extra`とは別に定義する <br> 抽出の対象とするmimetype ) |
