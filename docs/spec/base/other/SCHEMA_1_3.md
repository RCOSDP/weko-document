# Form

## 目的・用途



## 利用方法

## 機能内容


## 構造

```
[
    {                                                                                                       
        "key": "pubdate",
        "type": "template",
        "title":"PubDate",
        "format": "yyyy-MM-dd",
        "required": true,
        "title_i18n": {"en": "PubDate","ja": "公開日"},
        "templateUrl": "/static/templates/weko_deposit/datepicker.html"
    },
    {
        "add": "New",
        "key": "item_30002_title0",
        "items": [
            {
                "key": "item_30002_title0[].subitem_title",
                "type": "text",
                "title": "タイトル",
                "isHide": false,
                "required": false,
                "isShowList": false,
                "title_i18n": {"en": "Title","ja": "タイトル"},
                "isNonDisplay": false,
                "isSpecifyNewline": false
            },
            {
                "key": "item_30002_title0[].subitem_title_language",
                "type": "select",
                "title": "言語",
                "isHide": false,
                "required": false,
                "titleMap": [
                    {"name": "ja","value": "ja"},
                    {"name": "ja-Kana","value": "ja-Kana"},
                    {"name": "ja-Latn","value": "ja-Latn"},
                    {"name": "en","value": "en"},
                ],
                "isShowList": false,
                "title_i18n": {"en": "Language","ja": "言語"},
                "isNonDisplay": false,
                "isSpecifyNewline": false
            }
        ],
        "style": {"add": "btn-success"},
        "title": "Title",
        "title_i18n": {"en": "Title","ja": "タイトル"}
    },
    {
        "key": "item_30002_dataset_series42",
        "type": "fieldset",
        "items": [
            {
                "key": "item_30002_dataset_series42.jpcoar_dataset_series",
                "type": "select",
                "title": "Dataset Series",
                "isHide": false,
                "required": false,
                "titleMap": [
                    {"name": "True","value": "True"},
                    {"name": "False","value": "False"}
                ],
                "isShowList": false,
                "title_i18n": {"en": "Dataset Series","ja": "データセットシリーズ"},
                "isNonDisplay": false,
                "title_i18n_temp": {"en": "Dataset Series","ja": "データセットシリーズ"},
                "isSpecifyNewline": false
            }
        ],
        "title": "データセットシリーズ",
        "title_i18n": {"en": "","ja": "データセットシリーズ"}
    }

]
```

## 関連モジュール


## 更新履歴


| 日付  | GitHubコミットID | 更新内容 |
| ------------- | ------------- | ------------- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
