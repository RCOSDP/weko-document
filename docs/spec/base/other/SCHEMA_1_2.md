# Schema

## 目的・用途



## 利用方法

## 機能内容

/items/jsonschema/{item type id}

## 構造

```
{
  "type": "object",
  "$schema": "http://json-schema.org/draft-04/schema#",
  "required": ["pubdate"]
  "properties": {
    "pubdate": {
      "type": "string",
      "title": "PubDate",
      "format": "datetime"
    },                                                        
  },
  "description": ""
}
```

## 関連モジュール


## 更新履歴


| 日付  | GitHubコミットID | 更新内容 |
| ------------- | ------------- | ------------- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
