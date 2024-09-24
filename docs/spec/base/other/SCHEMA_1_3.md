# Form

## 目的・用途

他のウェブアプリがweko3のリソースにアクセスできるようAPI利用を承認することを目的としている。

## 利用方法

API-8-5の機能を用いて、OAuthアプリケーション、またはトークンを登録する。その後、設定された値を利用してAPI接続の設定を行う。

## 機能内容

/items/schemaform/{item type id}

## 関連モジュール

- Invenio_oaiserver

#### 構造


| # | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
|   | [ |   |   |   |   |   |
|   |   | { |   |   |   |   |
|   |   | "add": "New", |   |   |   |   |
|   |   | "items": [|   |   |   |   |
|   |   |   | {  |   |   |   |
|   |   |   |   | "isHide": true,  |   |   |
|   |   |   |   | "isNonDisplay": false,  |   |   |
|   |   |   |   | "isShowList": false,  |   |   |
|   |   |   |   | "isSpecifyNewline": false,  |   |   |
|   |   |   |   | "required": false, |   |   |
|   |   |   |   | "key": "item_1617186331708[].subitem_title", |   |   |
|   |   |   |   | "title": "Title", |   |   |
|   |   |   |   | "title_i18n": {"en": "Title","ja": "タイトル"}, |   |   |
|   |   |   |   | "title_i18n_temp": {"en": "Title","ja": "タイトル"}, |   |   |
|   |   |   |   | "type": "text"|   |   |
|   |   |   | },  |   |   |   |
|   |   |   | {  |   |   |   |
|   |   |   |   | "isHide": true,  |   |   |
|   |   |   |   | "isNonDisplay": false,  |   |   |
|   |   |   |   | "isShowList": false,  |   |   |
|   |   |   |   | "isSpecifyNewline": false,  |   |   |
|   |   |   |   | "required": false, |   |   |
|   |   |   |   | "key": "item_1617186331708[].subitem_title_language", |   |   |
|   |   |   |   | "title": "Language", |   |   |
|   |   |   |   | "titleMap": [{"name": "ja","value": "ja"},{"name": "ja-Kana","value": "ja-Kana"},{"name": "ja-Latn","value": "ja-Latn"},{"name": "en","value": "en"}], |   |   |
|   |   |   |   | "title_i18n": {"en": "Language","ja": "言語"}, |   |   |
|   |   |   |   | "title_i18n_temp": {"en": "Language","ja": "言語"}, |   |   |
|   |   |   |   | "type": "select"|   |   |
|   |   |   | }  |   |   |   |
|   |   |  ], |   |   |   |   |
|   |   |  "key": "item_1617186331708", |   |   |   |   |
|   |   |  "style": {"add": "btn-success"}, |   |   |   |   |
|   |   |  "title": "Title", |   |   |   |   |
|   |   |  "title_i18n": {"en": "Title","ja": "タイトル"} |   |   |   |   |
|   |   | }, |   |   |   |   |
|   |   | ... |   |   |   |   |
|   | ] |   |   |   |   |   |



```
[
  {
    "format": "yyyy-MM-dd",
    "key": "pubdate",
    "required": true,
    "templateUrl": "/static/templates/weko_deposit/datepicker.html",
    "title": "PubDate",
    "title_i18n": {
      "en": "PubDate",
      "ja": "公開日"
    },
    "type": "template"
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": true,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186331708[].subitem_title",
        "required": false,
        "title": "Title",
        "title_i18n": {
          "en": "Title",
          "ja": "タイトル"
        },
        "title_i18n_temp": {
          "en": "Title",
          "ja": "タイトル"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186331708[].subitem_title_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186331708",
    "style": {
      "add": "btn-success"
    },
    "title": "Title",
    "title_i18n": {
      "en": "Title",
      "ja": "タイトル"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186385884[].subitem_alternative_title",
        "required": false,
        "title": "Alternative Title",
        "title_i18n": {
          "en": "Alternative Title",
          "ja": "その他のタイトル"
        },
        "title_i18n_temp": {
          "en": "Alternative Title",
          "ja": "その他のタイトル"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186385884[].subitem_alternative_title_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186385884",
    "style": {
      "add": "btn-success"
    },
    "title": "Alternative Title",
    "title_i18n": {
      "en": "Alternative Title",
      "ja": "その他のタイトル"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186419668[].creatorType",
        "required": false,
        "title": "Creator Type",
        "title_i18n": {
          "en": "Creator Type",
          "ja": "作成者タイプ"
        },
        "title_i18n_temp": {
          "en": "Creator Type",
          "ja": "作成者タイプ"
        },
        "type": "text"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": true,
        "isSpecifyNewline": true,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": true,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].nameIdentifiers[].nameIdentifierScheme",
            "required": false,
            "title": "Creator Name Identifier Scheme",
            "titleMap": [],
            "title_i18n": {
              "en": "Creator Name Identifier Scheme",
              "ja": "作成者識別子Scheme"
            },
            "title_i18n_temp": {
              "en": "Creator Name Identifier Scheme",
              "ja": "作成者識別子Scheme"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": true,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].nameIdentifiers[].nameIdentifierURI",
            "required": false,
            "title": "Creator Name Identifier URI",
            "title_i18n": {
              "en": "Creator Name Identifier URI",
              "ja": "作成者識別子URI"
            },
            "title_i18n_temp": {
              "en": "Creator Name Identifier URI",
              "ja": "作成者識別子URI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": true,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].nameIdentifiers[].nameIdentifier",
            "required": false,
            "title": "Creator Name Identifier",
            "title_i18n": {
              "en": "Creator Name Identifier",
              "ja": "作成者識別子"
            },
            "title_i18n_temp": {
              "en": "Creator Name Identifier",
              "ja": "作成者識別子"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186419668[].nameIdentifiers",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Creator Name Identifier",
        "title_i18n": {
          "en": "Creator Name Identifier",
          "ja": "作成者識別子"
        },
        "title_i18n_temp": {
          "en": "Creator Name Identifier",
          "ja": "作成者識別子"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": true,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": true,
            "isShowList": false,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].creatorNames[].creatorName",
            "required": false,
            "title": "Name",
            "title_i18n": {
              "en": "Name",
              "ja": "姓名"
            },
            "title_i18n_temp": {
              "en": "Name",
              "ja": "姓名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].creatorNames[].creatorNameLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].creatorNames[].creatorNameType",
            "required": false,
            "title": "Name Type",
            "titleMap": [
              {
                "name": "Personal",
                "value": "Personal"
              },
              {
                "name": "Organizational",
                "value": "Organizational"
              }
            ],
            "title_i18n": {
              "en": "Name Type",
              "ja": "名前タイプ"
            },
            "title_i18n_temp": {
              "en": "Name Type",
              "ja": "名前タイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186419668[].creatorNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Creator Name",
        "title_i18n": {
          "en": "Creator Name",
          "ja": "作成者姓名"
        },
        "title_i18n_temp": {
          "en": "Creator Name",
          "ja": "作成者姓名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": true,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": true,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186419668[].familyNames[].familyName",
            "required": true,
            "title": "Family Name",
            "title_i18n": {
              "en": "Family Name",
              "ja": "姓"
            },
            "title_i18n_temp": {
              "en": "Family Name",
              "ja": "姓"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": true,
            "isShowList": false,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].familyNames[].familyNameLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186419668[].familyNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Creator Family Name",
        "title_i18n": {
          "en": "Creator Family Name",
          "ja": "作成者姓"
        },
        "title_i18n_temp": {
          "en": "Creator Family Name",
          "ja": "作成者姓"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": true,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": true,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].givenNames[].givenName",
            "required": false,
            "title": "Given Name",
            "title_i18n": {
              "en": "Given Name",
              "ja": "名"
            },
            "title_i18n_temp": {
              "en": "Given Name",
              "ja": "名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].givenNames[].givenNameLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186419668[].givenNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Creator Given Name",
        "title_i18n": {
          "en": "Creator Given Name",
          "ja": "作成者名"
        },
        "title_i18n_temp": {
          "en": "Creator Given Name",
          "ja": "作成者名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": true,
            "isNonDisplay": false,
            "isShowList": true,
            "isSpecifyNewline": false,
            "key": "item_1617186419668[].creatorAlternatives[].creatorAlternative",
            "required": false,
            "title": "Alternative Name",
            "title_i18n": {
              "en": "Alternative Name",
              "ja": "別名"
            },
            "title_i18n_temp": {
              "en": "Alternative Name",
              "ja": "別名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": true,
            "isShowList": true,
            "isSpecifyNewline": true,
            "key": "item_1617186419668[].creatorAlternatives[].creatorAlternativeLang",
            "required": true,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186419668[].creatorAlternatives",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Creator Alternative Name",
        "title_i18n": {
          "en": "Creator Alternative Name",
          "ja": "作成者別名"
        },
        "title_i18n_temp": {
          "en": "Creator Alternative Name",
          "ja": "作成者別名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": true,
        "isShowList": true,
        "isSpecifyNewline": false,
        "items": [
          {
            "add": "New",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "items": [
              {
                "isHide": false,
                "isNonDisplay": true,
                "isShowList": true,
                "isSpecifyNewline": true,
                "key": "item_1617186419668[].creatorAffiliations[].affiliationNameIdentifiers[].affiliationNameIdentifier",
                "required": true,
                "title": "Affiliation Name Identifier",
                "title_i18n": {
                  "en": "Affiliation Name Identifier",
                  "ja": "所属機関識別子"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name Identifier",
                  "ja": "所属機関識別子"
                },
                "type": "text"
              },
              {
                "isHide": true,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617186419668[].creatorAffiliations[].affiliationNameIdentifiers[].affiliationNameIdentifierScheme",
                "required": false,
                "title": "Affiliation Name Identifier Scheme",
                "titleMap": [
                  {
                    "name": "kakenhi",
                    "value": "kakenhi"
                  },
                  {
                    "name": "ISNI",
                    "value": "ISNI"
                  },
                  {
                    "name": "Ringgold",
                    "value": "Ringgold"
                  },
                  {
                    "name": "GRID",
                    "value": "GRID"
                  }
                ],
                "title_i18n": {
                  "en": "Affiliation Name Identifier Scheme",
                  "ja": "所属機関識別子Scheme"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name Identifier Scheme",
                  "ja": "所属機関識別子Scheme"
                },
                "type": "select"
              },
              {
                "isHide": false,
                "isNonDisplay": true,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617186419668[].creatorAffiliations[].affiliationNameIdentifiers[].affiliationNameIdentifierURI",
                "required": false,
                "title": "Affiliation Name Identifier URI",
                "title_i18n": {
                  "en": "Affiliation Name Identifier URI",
                  "ja": "所属機関識別子URI"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name Identifier URI",
                  "ja": "所属機関識別子URI"
                },
                "type": "text"
              }
            ],
            "key": "item_1617186419668[].creatorAffiliations[].affiliationNameIdentifiers",
            "required": false,
            "style": {
              "add": "btn-success"
            },
            "title": "Affiliation Name Identifiers",
            "title_i18n": {
              "en": "Affiliation Name Identifiers",
              "ja": "所属機関識別子"
            },
            "title_i18n_temp": {
              "en": "Affiliation Name Identifiers",
              "ja": "所属機関識別子"
            }
          },
          {
            "add": "New",
            "isHide": true,
            "isNonDisplay": true,
            "isShowList": false,
            "isSpecifyNewline": false,
            "items": [
              {
                "isHide": true,
                "isNonDisplay": true,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617186419668[].creatorAffiliations[].affiliationNames[].affiliationName",
                "required": true,
                "title": "Affiliation Name",
                "title_i18n": {
                  "en": "Affiliation Name",
                  "ja": "所属機関名"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name",
                  "ja": "所属機関名"
                },
                "type": "text"
              },
              {
                "isHide": true,
                "isNonDisplay": true,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617186419668[].creatorAffiliations[].affiliationNames[].affiliationNameLang",
                "required": true,
                "title": "Language",
                "titleMap": [
                  {
                    "name": "ja",
                    "value": "ja"
                  },
                  {
                    "name": "ja-Kana",
                    "value": "ja-Kana"
                  },
                  {
                    "name": "ja-Latn",
                    "value": "ja-Latn"
                  },
                  {
                    "name": "en",
                    "value": "en"
                  },
                  {
                    "name": "fr",
                    "value": "fr"
                  },
                  {
                    "name": "it",
                    "value": "it"
                  },
                  {
                    "name": "de",
                    "value": "de"
                  },
                  {
                    "name": "es",
                    "value": "es"
                  },
                  {
                    "name": "zh-cn",
                    "value": "zh-cn"
                  },
                  {
                    "name": "zh-tw",
                    "value": "zh-tw"
                  },
                  {
                    "name": "ru",
                    "value": "ru"
                  },
                  {
                    "name": "la",
                    "value": "la"
                  },
                  {
                    "name": "ms",
                    "value": "ms"
                  },
                  {
                    "name": "eo",
                    "value": "eo"
                  },
                  {
                    "name": "ar",
                    "value": "ar"
                  },
                  {
                    "name": "el",
                    "value": "el"
                  },
                  {
                    "name": "ko",
                    "value": "ko"
                  }
                ],
                "title_i18n": {
                  "en": "Language",
                  "ja": "言語"
                },
                "title_i18n_temp": {
                  "en": "Language",
                  "ja": "言語"
                },
                "type": "select"
              }
            ],
            "key": "item_1617186419668[].creatorAffiliations[].affiliationNames",
            "required": true,
            "style": {
              "add": "btn-success"
            },
            "title": "Affiliation Names",
            "title_i18n": {
              "en": "Affiliation Names",
              "ja": "所属機関名"
            },
            "title_i18n_temp": {
              "en": "Affiliation Names",
              "ja": "所属機関名"
            }
          }
        ],
        "key": "item_1617186419668[].creatorAffiliations",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Affiliation",
        "title_i18n": {
          "en": "Affiliation",
          "ja": "作成者所属"
        },
        "title_i18n_temp": {
          "en": "Affiliation",
          "ja": "作成者所属"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": true,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186419668[].creatorMails[].creatorMail",
            "required": false,
            "title": "Email Address",
            "title_i18n": {
              "en": "Email Address",
              "ja": "メールアドレス"
            },
            "title_i18n_temp": {
              "en": "Email Address",
              "ja": "メールアドレス"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186419668[].creatorMails",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Creator Email Address",
        "title_i18n": {
          "en": "Creator Email Address",
          "ja": "作成者メールアドレス"
        },
        "title_i18n_temp": {
          "en": "Creator Email Address",
          "ja": "作成者メールアドレス"
        }
      },
      {
        "icon": "glyphicon glyphicon-search",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186419668[].authorInputButton",
        "onClick": "searchAuthor('item_1617186419668', true, form)",
        "required": false,
        "style": "btn-default pull-right m-top-5",
        "title": "Enter from DB",
        "title_i18n": {
          "en": "Enter from DB",
          "ja": "著者DBから入力"
        },
        "title_i18n_temp": {
          "en": "Enter from DB",
          "ja": "著者DBから入力"
        },
        "type": "button"
      }
    ],
    "key": "item_1617186419668",
    "style": {
      "add": "btn-success"
    },
    "title": "Creator",
    "title_i18n": {
      "en": "Creator",
      "ja": "作成者"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617349709064[].contributorType",
        "required": false,
        "title": "Contributor Type",
        "titleMap": [
          {
            "name": "ContactPerson",
            "value": "ContactPerson"
          },
          {
            "name": "DataCollector",
            "value": "DataCollector"
          },
          {
            "name": "DataCurator",
            "value": "DataCurator"
          },
          {
            "name": "DataManager",
            "value": "DataManager"
          },
          {
            "name": "Distributor",
            "value": "Distributor"
          },
          {
            "name": "Editor",
            "value": "Editor"
          },
          {
            "name": "HostingInstitution",
            "value": "HostingInstitution"
          },
          {
            "name": "Producer",
            "value": "Producer"
          },
          {
            "name": "ProjectLeader",
            "value": "ProjectLeader"
          },
          {
            "name": "ProjectManager",
            "value": "ProjectManager"
          },
          {
            "name": "ProjectMember",
            "value": "ProjectMember"
          },
          {
            "name": "RelatedPerson",
            "value": "RelatedPerson"
          },
          {
            "name": "Researcher",
            "value": "Researcher"
          },
          {
            "name": "ResearchGroup",
            "value": "ResearchGroup"
          },
          {
            "name": "Sponsor",
            "value": "Sponsor"
          },
          {
            "name": "Supervisor",
            "value": "Supervisor"
          },
          {
            "name": "WorkPackageLeader",
            "value": "WorkPackageLeader"
          },
          {
            "name": "Other",
            "value": "Other"
          }
        ],
        "title_i18n": {
          "en": "Contributor Type",
          "ja": "寄与者タイプ"
        },
        "title_i18n_temp": {
          "en": "Contributor Type",
          "ja": "寄与者タイプ"
        },
        "type": "select"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].nameIdentifiers[].nameIdentifierScheme",
            "required": false,
            "title": "Contributor Name Identifier Scheme",
            "titleMap": [],
            "title_i18n": {
              "en": "Contributor Name Identifier Scheme",
              "ja": "寄与者識別子Scheme"
            },
            "title_i18n_temp": {
              "en": "Contributor Name Identifier Scheme",
              "ja": "寄与者識別子Scheme"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].nameIdentifiers[].nameIdentifierURI",
            "required": false,
            "title": "Contributor Name Identifier URI",
            "title_i18n": {
              "en": "Contributor Name Identifier URI",
              "ja": "寄与者識別子URI"
            },
            "title_i18n_temp": {
              "en": "Contributor Name Identifier URI",
              "ja": "寄与者識別子URI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].nameIdentifiers[].nameIdentifier",
            "required": false,
            "title": "Contributor Name Identifier",
            "title_i18n": {
              "en": "Contributor Name Identifier",
              "ja": "寄与者識別子"
            },
            "title_i18n_temp": {
              "en": "Contributor Name Identifier",
              "ja": "寄与者識別子"
            },
            "type": "text"
          }
        ],
        "key": "item_1617349709064[].nameIdentifiers",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Contributor Name Identifier",
        "title_i18n": {
          "en": "Contributor Name Identifier",
          "ja": "寄与者識別子"
        },
        "title_i18n_temp": {
          "en": "Contributor Name Identifier",
          "ja": "寄与者識別子"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].contributorNames[].contributorName",
            "required": false,
            "title": "Name",
            "title_i18n": {
              "en": "Name",
              "ja": "姓名"
            },
            "title_i18n_temp": {
              "en": "Name",
              "ja": "姓名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].contributorNames[].lang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].contributorNames[].nameType",
            "required": false,
            "title": "Name Type",
            "titleMap": [
              {
                "name": "Personal",
                "value": "Personal"
              },
              {
                "name": "Organizational",
                "value": "Organizational"
              }
            ],
            "title_i18n": {
              "en": "Name Type",
              "ja": "名前タイプ"
            },
            "title_i18n_temp": {
              "en": "Name Type",
              "ja": "名前タイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1617349709064[].contributorNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Contributor Name",
        "title_i18n": {
          "en": "Contributor Name",
          "ja": "寄与者姓名"
        },
        "title_i18n_temp": {
          "en": "Contributor Name",
          "ja": "寄与者姓名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].familyNames[].familyNameLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].familyNames[].familyName",
            "required": false,
            "title": "Family Name",
            "title_i18n": {
              "en": "Family Name",
              "ja": "姓"
            },
            "title_i18n_temp": {
              "en": "Family Name",
              "ja": "姓"
            },
            "type": "text"
          }
        ],
        "key": "item_1617349709064[].familyNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Contributor Family Name",
        "title_i18n": {
          "en": "Contributor Family Name",
          "ja": "寄与者姓"
        },
        "title_i18n_temp": {
          "en": "Contributor Family Name",
          "ja": "寄与者姓"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].givenNames[].givenName",
            "required": false,
            "title": "Given Name",
            "title_i18n": {
              "en": "Given Name",
              "ja": "名"
            },
            "title_i18n_temp": {
              "en": "Given Name",
              "ja": "名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].givenNames[].givenNameLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617349709064[].givenNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Contributor Given Name",
        "title_i18n": {
          "en": "Contributor Given Name",
          "ja": "寄与者名"
        },
        "title_i18n_temp": {
          "en": "Contributor Given Name",
          "ja": "寄与者名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].contributorAlternatives[].contributorAlternativeLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].contributorAlternatives[].contributorAlternative",
            "required": false,
            "title": "Alternative Name",
            "title_i18n": {
              "en": "Alternative Name",
              "ja": "別名"
            },
            "title_i18n_temp": {
              "en": "Alternative Name",
              "ja": "別名"
            },
            "type": "text"
          }
        ],
        "key": "item_1617349709064[].contributorAlternatives",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Contributor Alternative Name",
        "title_i18n": {
          "en": "Contributor Alternative Name",
          "ja": "寄与者別名"
        },
        "title_i18n_temp": {
          "en": "Contributor Alternative Name",
          "ja": "寄与者別名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "add": "New",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "items": [
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNameIdentifiers[].contributorAffiliationNameIdentifier",
                "required": false,
                "title": "Affiliation Name Identifier",
                "title_i18n": {
                  "en": "Affiliation Name Identifier",
                  "ja": "所属機関識別子"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name Identifier",
                  "ja": "所属機関識別子"
                },
                "type": "text"
              },
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNameIdentifiers[].contributorAffiliationScheme",
                "required": false,
                "title": "Affiliation Name Identifier Scheme",
                "titleMap": [
                  {
                    "name": "kakenhi",
                    "value": "kakenhi"
                  },
                  {
                    "name": "ISNI",
                    "value": "ISNI"
                  },
                  {
                    "name": "Ringgold",
                    "value": "Ringgold"
                  },
                  {
                    "name": "GRID",
                    "value": "GRID"
                  }
                ],
                "title_i18n": {
                  "en": "Affiliation Name Identifier Scheme",
                  "ja": "所属機関識別子Scheme"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name Identifier Scheme",
                  "ja": "所属機関識別子Scheme"
                },
                "type": "select"
              },
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNameIdentifiers[].contributorAffiliationURI",
                "required": false,
                "title": "Affiliation Name Identifier URI",
                "title_i18n": {
                  "en": "Affiliation Name Identifier URI",
                  "ja": "所属機関識別子URI"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name Identifier URI",
                  "ja": "所属機関識別子URI"
                },
                "type": "text"
              }
            ],
            "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNameIdentifiers",
            "required": false,
            "style": {
              "add": "btn-success"
            },
            "title": "Affiliation Name Identifiers",
            "title_i18n": {
              "en": "Affiliation Name Identifiers",
              "ja": "所属機関識別子"
            },
            "title_i18n_temp": {
              "en": "Affiliation Name Identifiers",
              "ja": "所属機関識別子"
            }
          },
          {
            "add": "New",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "items": [
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNames[].contributorAffiliationName",
                "required": false,
                "title": "Affiliation Name",
                "title_i18n": {
                  "en": "Affiliation Name",
                  "ja": "所属機関名"
                },
                "title_i18n_temp": {
                  "en": "Affiliation Name",
                  "ja": "所属機関名"
                },
                "type": "text"
              },
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNames[].contributorAffiliationNameLang",
                "required": false,
                "title": "Language",
                "titleMap": [
                  {
                    "name": "ja",
                    "value": "ja"
                  },
                  {
                    "name": "ja-Kana",
                    "value": "ja-Kana"
                  },
                  {
                    "name": "ja-Latn",
                    "value": "ja-Latn"
                  },
                  {
                    "name": "en",
                    "value": "en"
                  },
                  {
                    "name": "fr",
                    "value": "fr"
                  },
                  {
                    "name": "it",
                    "value": "it"
                  },
                  {
                    "name": "de",
                    "value": "de"
                  },
                  {
                    "name": "es",
                    "value": "es"
                  },
                  {
                    "name": "zh-cn",
                    "value": "zh-cn"
                  },
                  {
                    "name": "zh-tw",
                    "value": "zh-tw"
                  },
                  {
                    "name": "ru",
                    "value": "ru"
                  },
                  {
                    "name": "la",
                    "value": "la"
                  },
                  {
                    "name": "ms",
                    "value": "ms"
                  },
                  {
                    "name": "eo",
                    "value": "eo"
                  },
                  {
                    "name": "ar",
                    "value": "ar"
                  },
                  {
                    "name": "el",
                    "value": "el"
                  },
                  {
                    "name": "ko",
                    "value": "ko"
                  }
                ],
                "title_i18n": {
                  "en": "Language",
                  "ja": "言語"
                },
                "title_i18n_temp": {
                  "en": "Language",
                  "ja": "言語"
                },
                "type": "select"
              }
            ],
            "key": "item_1617349709064[].contributorAffiliations[].contributorAffiliationNames",
            "required": false,
            "style": {
              "add": "btn-success"
            },
            "title": "Affiliation Names",
            "title_i18n": {
              "en": "Affiliation Names",
              "ja": "所属機関名"
            },
            "title_i18n_temp": {
              "en": "Affiliation Names",
              "ja": "所属機関名"
            }
          }
        ],
        "key": "item_1617349709064[].contributorAffiliations",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Affiliation",
        "title_i18n": {
          "en": "Affiliation",
          "ja": "寄与者所属"
        },
        "title_i18n_temp": {
          "en": "Affiliation",
          "ja": "寄与者所属"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617349709064[].contributorMails[].contributorMail",
            "required": false,
            "title": "Email Address",
            "title_i18n": {
              "en": "Email Address",
              "ja": "メールアドレス"
            },
            "title_i18n_temp": {
              "en": "Email Address",
              "ja": "メールアドレス"
            },
            "type": "text"
          }
        ],
        "key": "item_1617349709064[].contributorMails",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Contributor Email Address",
        "title_i18n": {
          "en": "Contributor Email Address",
          "ja": "寄与者メールアドレス"
        },
        "title_i18n_temp": {
          "en": "Contributor Email Address",
          "ja": "寄与者メールアドレス"
        }
      },
      {
        "icon": "glyphicon glyphicon-search",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617349709064[].authorInputButton",
        "onClick": "searchAuthor('item_1617349709064[]', true, form)",
        "required": false,
        "style": "btn-default pull-right m-top-5",
        "title": "Enter from DB",
        "title_i18n": {
          "en": "Enter from DB",
          "ja": "著者DBから入力"
        },
        "title_i18n_temp": {
          "en": "Enter from DB",
          "ja": "著者DBから入力"
        },
        "type": "button"
      }
    ],
    "key": "item_1617349709064",
    "style": {
      "add": "btn-success"
    },
    "title": "Contributor",
    "title_i18n": {
      "en": "Contributor",
      "ja": "寄与者"
    }
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186476635.subitem_access_right",
        "onChange": "changedAccessRights(this, modelValue)",
        "required": false,
        "title": "Access Rights",
        "titleMap": [
          {
            "name": "embargoed access",
            "value": "embargoed access"
          },
          {
            "name": "metadata only access",
            "value": "metadata only access"
          },
          {
            "name": "open access",
            "value": "open access"
          },
          {
            "name": "restricted access",
            "value": "restricted access"
          }
        ],
        "title_i18n": {
          "en": "Access Rights",
          "ja": "アクセス権"
        },
        "title_i18n_temp": {
          "en": "Access Rights",
          "ja": "アクセス権"
        },
        "type": "select"
      },
      {
        "fieldHtmlClass": "txt-access-rights-uri",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186476635.subitem_access_right_uri",
        "readonly": true,
        "required": false,
        "title": "Access Rights URI",
        "title_i18n": {
          "en": "Access Rights URI",
          "ja": "アクセス権URI"
        },
        "title_i18n_temp": {
          "en": "Access Rights URI",
          "ja": "アクセス権URI"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186476635",
    "title": "Access Rights",
    "title_i18n": {
      "en": "Access Rights",
      "ja": "アクセス権"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617351524846.subitem_apc",
        "required": false,
        "title": "APC",
        "titleMap": [
          {
            "name": "Paid",
            "value": "Paid"
          },
          {
            "name": "Partially waived",
            "value": "Partially waived"
          },
          {
            "name": "Fully waived",
            "value": "Fully waived"
          },
          {
            "name": "Not charged",
            "value": "Not charged"
          },
          {
            "name": "Not required",
            "value": "Not required"
          },
          {
            "name": "Unknown",
            "value": "Unknown"
          }
        ],
        "title_i18n": {
          "en": "APC",
          "ja": "APC"
        },
        "title_i18n_temp": {
          "en": "APC",
          "ja": "APC"
        },
        "type": "select"
      }
    ],
    "key": "item_1617351524846",
    "title": "APC",
    "title_i18n": {
      "en": "APC",
      "ja": "APC"
    },
    "type": "fieldset"
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186499011[].subitem_rights_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186499011[].subitem_rights_resource",
        "required": false,
        "title": "Rights Resource",
        "title_i18n": {
          "en": "Rights Resource",
          "ja": "権利情報Resource"
        },
        "title_i18n_temp": {
          "en": "Rights Resource",
          "ja": "権利情報Resource"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186499011[].subitem_rights",
        "required": false,
        "title": "Rights",
        "title_i18n": {
          "en": "Rights",
          "ja": "権利情報"
        },
        "title_i18n_temp": {
          "en": "Rights",
          "ja": "権利情報"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186499011",
    "style": {
      "add": "btn-success"
    },
    "title": "Rights",
    "title_i18n": {
      "en": "Rights",
      "ja": "権利情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617610673286[].nameIdentifiers[].nameIdentifierScheme",
            "required": false,
            "title": "Right Holder Name Identifier Scheme",
            "titleMap": [],
            "title_i18n": {
              "en": "Right Holder Name Identifier Scheme",
              "ja": "権利者識別子Scheme"
            },
            "title_i18n_temp": {
              "en": "Right Holder Name Identifier Scheme",
              "ja": "権利者識別子Scheme"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617610673286[].nameIdentifiers[].nameIdentifierURI",
            "required": false,
            "title": "Right Holder Name Identifier URI",
            "title_i18n": {
              "en": "Right Holder Name Identifier URI",
              "ja": "権利者識別子URI"
            },
            "title_i18n_temp": {
              "en": "Right Holder Name Identifier URI",
              "ja": "権利者識別子URI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617610673286[].nameIdentifiers[].nameIdentifier",
            "required": false,
            "title": "Right Holder Name Identifier",
            "title_i18n": {
              "en": "Right Holder Name Identifier",
              "ja": "権利者識別子"
            },
            "title_i18n_temp": {
              "en": "Right Holder Name Identifier",
              "ja": "権利者識別子"
            },
            "type": "text"
          }
        ],
        "key": "item_1617610673286[].nameIdentifiers",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Right Holder Identifier",
        "title_i18n": {
          "en": "Right Holder Identifier",
          "ja": "権利者識別子"
        },
        "title_i18n_temp": {
          "en": "Right Holder Identifier",
          "ja": "権利者識別子"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617610673286[].rightHolderNames[].rightHolderName",
            "required": false,
            "title": "Right Holder Name",
            "title_i18n": {
              "en": "Right Holder Name",
              "ja": "権利者名"
            },
            "title_i18n_temp": {
              "en": "Right Holder Name",
              "ja": "権利者名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617610673286[].rightHolderNames[].rightHolderLanguage",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617610673286[].rightHolderNames",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Right Holder Name",
        "title_i18n": {
          "en": "Right Holder Name",
          "ja": "権利者名"
        },
        "title_i18n_temp": {
          "en": "Right Holder Name",
          "ja": "権利者名"
        }
      }
    ],
    "key": "item_1617610673286",
    "style": {
      "add": "btn-success"
    },
    "title": "Right Holder",
    "title_i18n": {
      "en": "Right Holder",
      "ja": "権利者情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186609386[].subitem_subject_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186609386[].subitem_subject_scheme",
        "required": false,
        "title": "Subject Scheme",
        "titleMap": [
          {
            "name": "BSH",
            "value": "BSH"
          },
          {
            "name": "DDC",
            "value": "DDC"
          },
          {
            "name": "e-Rad_field",
            "value": "e-Rad_field"
          },
          {
            "name": "JEL",
            "value": "JEL"
          },
          {
            "name": "LCC",
            "value": "LCC"
          },
          {
            "name": "LCSH",
            "value": "LCSH"
          },
          {
            "name": "MeSH",
            "value": "MeSH"
          },
          {
            "name": "NDC",
            "value": "NDC"
          },
          {
            "name": "NDLC",
            "value": "NDLC"
          },
          {
            "name": "NDLSH",
            "value": "NDLSH"
          },
          {
            "name": "SciVal",
            "value": "SciVal"
          },
          {
            "name": "UDC",
            "value": "UDC"
          },
          {
            "name": "Other",
            "value": "Other"
          }
        ],
        "title_i18n": {
          "en": "Subject Scheme",
          "ja": "主題Scheme"
        },
        "title_i18n_temp": {
          "en": "Subject Scheme",
          "ja": "主題Scheme"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186609386[].subitem_subject_uri",
        "required": false,
        "title": "Subject URI",
        "title_i18n": {
          "en": "Subject URI",
          "ja": "主題URI"
        },
        "title_i18n_temp": {
          "en": "Subject URI",
          "ja": "主題URI"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186609386[].subitem_subject",
        "required": false,
        "title": "Subject",
        "title_i18n": {
          "en": "Subject",
          "ja": "主題"
        },
        "title_i18n_temp": {
          "en": "Subject",
          "ja": "主題"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186609386",
    "style": {
      "add": "btn-success"
    },
    "title": "Subject",
    "title_i18n": {
      "en": "Subject",
      "ja": "主題"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186626617[].subitem_description_type",
        "required": false,
        "title": "Description Type",
        "titleMap": [
          {
            "name": "Abstract",
            "value": "Abstract"
          },
          {
            "name": "Methods",
            "value": "Methods"
          },
          {
            "name": "TableOfContents",
            "value": "TableOfContents"
          },
          {
            "name": "TechnicalInfo",
            "value": "TechnicalInfo"
          },
          {
            "name": "Other",
            "value": "Other"
          }
        ],
        "title_i18n": {
          "en": "Description Type",
          "ja": "内容記述タイプ"
        },
        "title_i18n_temp": {
          "en": "Description Type",
          "ja": "内容記述タイプ"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186626617[].subitem_description",
        "required": false,
        "title": "Description",
        "title_i18n": {
          "en": "Description",
          "ja": "内容記述"
        },
        "title_i18n_temp": {
          "en": "Description",
          "ja": "内容記述"
        },
        "type": "textarea"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186626617[].subitem_description_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186626617",
    "style": {
      "add": "btn-success"
    },
    "title": "Description",
    "title_i18n": {
      "en": "Description",
      "ja": "内容記述"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186643794[].subitem_publisher",
        "required": false,
        "title": "Publisher",
        "title_i18n": {
          "en": "Publisher",
          "ja": "出版者"
        },
        "title_i18n_temp": {
          "en": "Publisher",
          "ja": "出版者"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186643794[].subitem_publisher_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186643794",
    "style": {
      "add": "btn-success"
    },
    "title": "Publisher",
    "title_i18n": {
      "en": "Publisher",
      "ja": "出版者"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "format": "yyyy-MM-dd",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186660861[].subitem_date_issued_datetime",
        "required": false,
        "templateUrl": "/static/templates/weko_deposit/datepicker_multi_format.html",
        "title": "Date",
        "title_i18n": {
          "en": "Date",
          "ja": "日付"
        },
        "title_i18n_temp": {
          "en": "Date",
          "ja": "日付"
        },
        "type": "template"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186660861[].subitem_date_issued_type",
        "required": false,
        "title": "Date Type",
        "titleMap": [
          {
            "name": "Accepted",
            "value": "Accepted"
          },
          {
            "name": "Available",
            "value": "Available"
          },
          {
            "name": "Collected",
            "value": "Collected"
          },
          {
            "name": "Copyrighted",
            "value": "Copyrighted"
          },
          {
            "name": "Created",
            "value": "Created"
          },
          {
            "name": "Issued",
            "value": "Issued"
          },
          {
            "name": "Submitted",
            "value": "Submitted"
          },
          {
            "name": "Updated",
            "value": "Updated"
          },
          {
            "name": "Valid",
            "value": "Valid"
          }
        ],
        "title_i18n": {
          "en": "Date Type",
          "ja": "日付タイプ"
        },
        "title_i18n_temp": {
          "en": "Date Type",
          "ja": "日付タイプ"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186660861",
    "style": {
      "add": "btn-success"
    },
    "title": "Date",
    "title_i18n": {
      "en": "Date",
      "ja": "日付"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186702042[].subitem_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "jpn",
            "value": "jpn"
          },
          {
            "name": "eng",
            "value": "eng"
          },
          {
            "name": "aar",
            "value": "aar"
          },
          {
            "name": "abk",
            "value": "abk"
          },
          {
            "name": "afr",
            "value": "afr"
          },
          {
            "name": "aka",
            "value": "aka"
          },
          {
            "name": "amh",
            "value": "amh"
          },
          {
            "name": "ara",
            "value": "ara"
          },
          {
            "name": "arg",
            "value": "arg"
          },
          {
            "name": "asm",
            "value": "asm"
          },
          {
            "name": "ava",
            "value": "ava"
          },
          {
            "name": "ave",
            "value": "ave"
          },
          {
            "name": "aym",
            "value": "aym"
          },
          {
            "name": "aze",
            "value": "aze"
          },
          {
            "name": "bak",
            "value": "bak"
          },
          {
            "name": "bam",
            "value": "bam"
          },
          {
            "name": "bel",
            "value": "bel"
          },
          {
            "name": "ben",
            "value": "ben"
          },
          {
            "name": "bis",
            "value": "bis"
          },
          {
            "name": "bod",
            "value": "bod"
          },
          {
            "name": "bos",
            "value": "bos"
          },
          {
            "name": "bre",
            "value": "bre"
          },
          {
            "name": "bul",
            "value": "bul"
          },
          {
            "name": "cat",
            "value": "cat"
          },
          {
            "name": "ces",
            "value": "ces"
          },
          {
            "name": "cha",
            "value": "cha"
          },
          {
            "name": "che",
            "value": "che"
          },
          {
            "name": "chu",
            "value": "chu"
          },
          {
            "name": "chv",
            "value": "chv"
          },
          {
            "name": "cor",
            "value": "cor"
          },
          {
            "name": "cos",
            "value": "cos"
          },
          {
            "name": "cre",
            "value": "cre"
          },
          {
            "name": "cym",
            "value": "cym"
          },
          {
            "name": "dan",
            "value": "dan"
          },
          {
            "name": "deu",
            "value": "deu"
          },
          {
            "name": "div",
            "value": "div"
          },
          {
            "name": "dzo",
            "value": "dzo"
          },
          {
            "name": "ell",
            "value": "ell"
          },
          {
            "name": "epo",
            "value": "epo"
          },
          {
            "name": "est",
            "value": "est"
          },
          {
            "name": "eus",
            "value": "eus"
          },
          {
            "name": "ewe",
            "value": "ewe"
          },
          {
            "name": "fao",
            "value": "fao"
          },
          {
            "name": "fas",
            "value": "fas"
          },
          {
            "name": "fij",
            "value": "fij"
          },
          {
            "name": "fin",
            "value": "fin"
          },
          {
            "name": "fra",
            "value": "fra"
          },
          {
            "name": "fry",
            "value": "fry"
          },
          {
            "name": "ful",
            "value": "ful"
          },
          {
            "name": "gla",
            "value": "gla"
          },
          {
            "name": "gle",
            "value": "gle"
          },
          {
            "name": "glg",
            "value": "glg"
          },
          {
            "name": "glv",
            "value": "glv"
          },
          {
            "name": "grn",
            "value": "grn"
          },
          {
            "name": "guj",
            "value": "guj"
          },
          {
            "name": "hat",
            "value": "hat"
          },
          {
            "name": "hau",
            "value": "hau"
          },
          {
            "name": "heb",
            "value": "heb"
          },
          {
            "name": "her",
            "value": "her"
          },
          {
            "name": "hin",
            "value": "hin"
          },
          {
            "name": "hmo",
            "value": "hmo"
          },
          {
            "name": "hrv",
            "value": "hrv"
          },
          {
            "name": "hun",
            "value": "hun"
          },
          {
            "name": "hye",
            "value": "hye"
          },
          {
            "name": "ibo",
            "value": "ibo"
          },
          {
            "name": "ido",
            "value": "ido"
          },
          {
            "name": "iii",
            "value": "iii"
          },
          {
            "name": "iku",
            "value": "iku"
          },
          {
            "name": "ile",
            "value": "ile"
          },
          {
            "name": "ina",
            "value": "ina"
          },
          {
            "name": "ind",
            "value": "ind"
          },
          {
            "name": "ipk",
            "value": "ipk"
          },
          {
            "name": "isl",
            "value": "isl"
          },
          {
            "name": "ita",
            "value": "ita"
          },
          {
            "name": "jav",
            "value": "jav"
          },
          {
            "name": "kal",
            "value": "kal"
          },
          {
            "name": "kan",
            "value": "kan"
          },
          {
            "name": "kas",
            "value": "kas"
          },
          {
            "name": "kat",
            "value": "kat"
          },
          {
            "name": "kau",
            "value": "kau"
          },
          {
            "name": "kaz",
            "value": "kaz"
          },
          {
            "name": "khm",
            "value": "khm"
          },
          {
            "name": "kik",
            "value": "kik"
          },
          {
            "name": "kin",
            "value": "kin"
          },
          {
            "name": "kir",
            "value": "kir"
          },
          {
            "name": "kom",
            "value": "kom"
          },
          {
            "name": "kon",
            "value": "kon"
          },
          {
            "name": "kor",
            "value": "kor"
          },
          {
            "name": "kua",
            "value": "kua"
          },
          {
            "name": "kur",
            "value": "kur"
          },
          {
            "name": "lao",
            "value": "lao"
          },
          {
            "name": "lat",
            "value": "lat"
          },
          {
            "name": "lav",
            "value": "lav"
          },
          {
            "name": "lim",
            "value": "lim"
          },
          {
            "name": "lin",
            "value": "lin"
          },
          {
            "name": "lit",
            "value": "lit"
          },
          {
            "name": "ltz",
            "value": "ltz"
          },
          {
            "name": "lub",
            "value": "lub"
          },
          {
            "name": "lug",
            "value": "lug"
          },
          {
            "name": "mah",
            "value": "mah"
          },
          {
            "name": "mal",
            "value": "mal"
          },
          {
            "name": "mar",
            "value": "mar"
          },
          {
            "name": "mkd",
            "value": "mkd"
          },
          {
            "name": "mlg",
            "value": "mlg"
          },
          {
            "name": "mlt",
            "value": "mlt"
          },
          {
            "name": "mon",
            "value": "mon"
          },
          {
            "name": "mri",
            "value": "mri"
          },
          {
            "name": "msa",
            "value": "msa"
          },
          {
            "name": "mya",
            "value": "mya"
          },
          {
            "name": "nau",
            "value": "nau"
          },
          {
            "name": "nav",
            "value": "nav"
          },
          {
            "name": "nbl",
            "value": "nbl"
          },
          {
            "name": "nde",
            "value": "nde"
          },
          {
            "name": "ndo",
            "value": "ndo"
          },
          {
            "name": "nep",
            "value": "nep"
          },
          {
            "name": "nld",
            "value": "nld"
          },
          {
            "name": "nno",
            "value": "nno"
          },
          {
            "name": "nob",
            "value": "nob"
          },
          {
            "name": "nor",
            "value": "nor"
          },
          {
            "name": "nya",
            "value": "nya"
          },
          {
            "name": "oci",
            "value": "oci"
          },
          {
            "name": "oji",
            "value": "oji"
          },
          {
            "name": "ori",
            "value": "ori"
          },
          {
            "name": "orm",
            "value": "orm"
          },
          {
            "name": "oss",
            "value": "oss"
          },
          {
            "name": "pan",
            "value": "pan"
          },
          {
            "name": "pli",
            "value": "pli"
          },
          {
            "name": "pol",
            "value": "pol"
          },
          {
            "name": "por",
            "value": "por"
          },
          {
            "name": "pus",
            "value": "pus"
          },
          {
            "name": "que",
            "value": "que"
          },
          {
            "name": "roh",
            "value": "roh"
          },
          {
            "name": "ron",
            "value": "ron"
          },
          {
            "name": "run",
            "value": "run"
          },
          {
            "name": "rus",
            "value": "rus"
          },
          {
            "name": "sag",
            "value": "sag"
          },
          {
            "name": "san",
            "value": "san"
          },
          {
            "name": "sin",
            "value": "sin"
          },
          {
            "name": "slk",
            "value": "slk"
          },
          {
            "name": "slv",
            "value": "slv"
          },
          {
            "name": "sme",
            "value": "sme"
          },
          {
            "name": "smo",
            "value": "smo"
          },
          {
            "name": "sna",
            "value": "sna"
          },
          {
            "name": "snd",
            "value": "snd"
          },
          {
            "name": "som",
            "value": "som"
          },
          {
            "name": "sot",
            "value": "sot"
          },
          {
            "name": "spa",
            "value": "spa"
          },
          {
            "name": "sqi",
            "value": "sqi"
          },
          {
            "name": "srd",
            "value": "srd"
          },
          {
            "name": "srp",
            "value": "srp"
          },
          {
            "name": "ssw",
            "value": "ssw"
          },
          {
            "name": "sun",
            "value": "sun"
          },
          {
            "name": "swa",
            "value": "swa"
          },
          {
            "name": "swe",
            "value": "swe"
          },
          {
            "name": "tah",
            "value": "tah"
          },
          {
            "name": "tam",
            "value": "tam"
          },
          {
            "name": "tat",
            "value": "tat"
          },
          {
            "name": "tel",
            "value": "tel"
          },
          {
            "name": "tgk",
            "value": "tgk"
          },
          {
            "name": "tgl",
            "value": "tgl"
          },
          {
            "name": "tha",
            "value": "tha"
          },
          {
            "name": "tir",
            "value": "tir"
          },
          {
            "name": "ton",
            "value": "ton"
          },
          {
            "name": "tsn",
            "value": "tsn"
          },
          {
            "name": "tso",
            "value": "tso"
          },
          {
            "name": "tuk",
            "value": "tuk"
          },
          {
            "name": "tur",
            "value": "tur"
          },
          {
            "name": "twi",
            "value": "twi"
          },
          {
            "name": "uig",
            "value": "uig"
          },
          {
            "name": "ukr",
            "value": "ukr"
          },
          {
            "name": "urd",
            "value": "urd"
          },
          {
            "name": "uzb",
            "value": "uzb"
          },
          {
            "name": "ven",
            "value": "ven"
          },
          {
            "name": "vie",
            "value": "vie"
          },
          {
            "name": "vol",
            "value": "vol"
          },
          {
            "name": "wln",
            "value": "wln"
          },
          {
            "name": "wol",
            "value": "wol"
          },
          {
            "name": "xho",
            "value": "xho"
          },
          {
            "name": "yid",
            "value": "yid"
          },
          {
            "name": "yor",
            "value": "yor"
          },
          {
            "name": "zha",
            "value": "zha"
          },
          {
            "name": "zho",
            "value": "zho"
          },
          {
            "name": "zul",
            "value": "zul"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186702042",
    "style": {
      "add": "btn-success"
    }
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617258105262.resourceuri",
        "readonly": true,
        "required": false,
        "title": "Resource Type Identifier",
        "title_i18n": {
          "en": "Resource Type Identifier",
          "ja": "資源タイプ識別子"
        },
        "title_i18n_temp": {
          "en": "Resource Type Identifier",
          "ja": "資源タイプ識別子"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617258105262.resourcetype",
        "onChange": "resourceTypeSelect()",
        "required": false,
        "title": "Resource Type",
        "titleMap": [
          {
            "name": "conference paper",
            "value": "conference paper"
          },
          {
            "name": "data paper",
            "value": "data paper"
          },
          {
            "name": "departmental bulletin paper",
            "value": "departmental bulletin paper"
          },
          {
            "name": "editorial",
            "value": "editorial"
          },
          {
            "name": "journal",
            "value": "journal"
          },
          {
            "name": "journal article",
            "value": "journal article"
          },
          {
            "name": "newspaper",
            "value": "newspaper"
          },
          {
            "name": "review article",
            "value": "review article"
          },
          {
            "name": "other periodical",
            "value": "other periodical"
          },
          {
            "name": "software paper",
            "value": "software paper"
          },
          {
            "name": "article",
            "value": "article"
          },
          {
            "name": "book",
            "value": "book"
          },
          {
            "name": "book part",
            "value": "book part"
          },
          {
            "name": "cartographic material",
            "value": "cartographic material"
          },
          {
            "name": "map",
            "value": "map"
          },
          {
            "name": "conference output",
            "value": "conference output"
          },
          {
            "name": "conference presentation",
            "value": "conference presentation"
          },
          {
            "name": "conference proceedings",
            "value": "conference proceedings"
          },
          {
            "name": "conference poster",
            "value": "conference poster"
          },
          {
            "name": "aggregated data",
            "value": "aggregated data"
          },
          {
            "name": "clinical trial data",
            "value": "clinical trial data"
          },
          {
            "name": "compiled data",
            "value": "compiled data"
          },
          {
            "name": "dataset",
            "value": "dataset"
          },
          {
            "name": "encoded data",
            "value": "encoded data"
          },
          {
            "name": "experimental data",
            "value": "experimental data"
          },
          {
            "name": "genomic data",
            "value": "genomic data"
          },
          {
            "name": "geospatial data",
            "value": "geospatial data"
          },
          {
            "name": "laboratory notebook",
            "value": "laboratory notebook"
          },
          {
            "name": "measurement and test data",
            "value": "measurement and test data"
          },
          {
            "name": "observational data",
            "value": "observational data"
          },
          {
            "name": "recorded data",
            "value": "recorded data"
          },
          {
            "name": "simulation data",
            "value": "simulation data"
          },
          {
            "name": "survey data",
            "value": "survey data"
          },
          {
            "name": "image",
            "value": "image"
          },
          {
            "name": "still image",
            "value": "still image"
          },
          {
            "name": "moving image",
            "value": "moving image"
          },
          {
            "name": "video",
            "value": "video"
          },
          {
            "name": "lecture",
            "value": "lecture"
          },
          {
            "name": "design patent",
            "value": "design patent"
          },
          {
            "name": "patent",
            "value": "patent"
          },
          {
            "name": "PCT application",
            "value": "PCT application"
          },
          {
            "name": "plant patent",
            "value": "plant patent"
          },
          {
            "name": "plant variety protection",
            "value": "plant variety protection"
          },
          {
            "name": "software patent",
            "value": "software patent"
          },
          {
            "name": "trademark",
            "value": "trademark"
          },
          {
            "name": "utility model",
            "value": "utility model"
          },
          {
            "name": "report",
            "value": "report"
          },
          {
            "name": "research report",
            "value": "research report"
          },
          {
            "name": "technical report",
            "value": "technical report"
          },
          {
            "name": "policy report",
            "value": "policy report"
          },
          {
            "name": "working paper",
            "value": "working paper"
          },
          {
            "name": "data management plan",
            "value": "data management plan"
          },
          {
            "name": "sound",
            "value": "sound"
          },
          {
            "name": "thesis",
            "value": "thesis"
          },
          {
            "name": "bachelor thesis",
            "value": "bachelor thesis"
          },
          {
            "name": "master thesis",
            "value": "master thesis"
          },
          {
            "name": "doctoral thesis",
            "value": "doctoral thesis"
          },
          {
            "name": "commentary",
            "value": "commentary"
          },
          {
            "name": "design",
            "value": "design"
          },
          {
            "name": "industrial design",
            "value": "industrial design"
          },
          {
            "name": "interactive resource",
            "value": "interactive resource"
          },
          {
            "name": "layout design",
            "value": "layout design"
          },
          {
            "name": "learning object",
            "value": "learning object"
          },
          {
            "name": "manuscript",
            "value": "manuscript"
          },
          {
            "name": "musical notation",
            "value": "musical notation"
          },
          {
            "name": "peer review",
            "value": "peer review"
          },
          {
            "name": "research proposal",
            "value": "research proposal"
          },
          {
            "name": "research protocol",
            "value": "research protocol"
          },
          {
            "name": "software",
            "value": "software"
          },
          {
            "name": "source code",
            "value": "source code"
          },
          {
            "name": "technical documentation",
            "value": "technical documentation"
          },
          {
            "name": "transcription",
            "value": "transcription"
          },
          {
            "name": "workflow",
            "value": "workflow"
          },
          {
            "name": "other",
            "value": "other"
          }
        ],
        "title_i18n": {
          "en": "Resource Type",
          "ja": "資源タイプ "
        },
        "title_i18n_temp": {
          "en": "Resource Type",
          "ja": "資源タイプ "
        },
        "type": "select"
      }
    ],
    "key": "item_1617258105262",
    "title": "Resource Type",
    "title_i18n": {
      "en": "Resource Type",
      "ja": "資源タイプ"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617349808926.subitem_version",
        "required": false,
        "title": "Version",
        "title_i18n": {
          "en": "Version",
          "ja": "バージョン情報"
        },
        "title_i18n_temp": {
          "en": "Version",
          "ja": "バージョン情報"
        },
        "type": "text"
      }
    ],
    "key": "item_1617349808926",
    "title": "Version",
    "title_i18n": {
      "en": "Version",
      "ja": "バージョン情報"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617265215918.subitem_version_type",
        "onChange": "changedVersionType(this, modelValue)",
        "required": false,
        "title": "Version Type",
        "titleMap": [
          {
            "name": "AO",
            "value": "AO"
          },
          {
            "name": "SMUR",
            "value": "SMUR"
          },
          {
            "name": "AM",
            "value": "AM"
          },
          {
            "name": "P",
            "value": "P"
          },
          {
            "name": "VoR",
            "value": "VoR"
          },
          {
            "name": "CVoR",
            "value": "CVoR"
          },
          {
            "name": "EVoR",
            "value": "EVoR"
          },
          {
            "name": "NA",
            "value": "NA"
          }
        ],
        "title_i18n": {
          "en": "Version Type",
          "ja": "出版タイプ"
        },
        "title_i18n_temp": {
          "en": "Version Type",
          "ja": "出版タイプ"
        },
        "type": "select"
      },
      {
        "fieldHtmlClass": "txt-version-resource",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617265215918.subitem_version_resource",
        "readonly": true,
        "required": false,
        "title": "Version Type Resource",
        "title_i18n": {
          "en": "Version Type Resource",
          "ja": "出版タイプResource"
        },
        "title_i18n_temp": {
          "en": "Version Type Resource",
          "ja": "出版タイプResource"
        },
        "type": "text"
      }
    ],
    "key": "item_1617265215918",
    "title": "Version Type",
    "title_i18n": {
      "en": "Version Type",
      "ja": "出版タイプ"
    },
    "type": "fieldset"
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186783814[].subitem_identifier_uri",
        "required": false,
        "title": "Identifier",
        "title_i18n": {
          "en": "Identifier",
          "ja": "識別子"
        },
        "title_i18n_temp": {
          "en": "Identifier",
          "ja": "識別子"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186783814[].subitem_identifier_type",
        "required": false,
        "title": "Identifier Type",
        "titleMap": [
          {
            "name": "DOI",
            "value": "DOI"
          },
          {
            "name": "HDL",
            "value": "HDL"
          },
          {
            "name": "URI",
            "value": "URI"
          }
        ],
        "title_i18n": {
          "en": "Identifier Type",
          "ja": "識別子タイプ"
        },
        "title_i18n_temp": {
          "en": "Identifier Type",
          "ja": "識別子タイプ"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186783814",
    "style": {
      "add": "btn-success"
    },
    "title": "Identifier",
    "title_i18n": {
      "en": "Identifier",
      "ja": "識別子"
    }
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186819068.subitem_identifier_reg_text",
        "readonly": true,
        "required": false,
        "title": "Identifier Registration",
        "title_i18n": {
          "en": "Identifier Registration",
          "ja": "ID登録"
        },
        "title_i18n_temp": {
          "en": "Identifier Registration",
          "ja": "ID登録"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186819068.subitem_identifier_reg_type",
        "readonly": true,
        "required": false,
        "title": "Identifier Registration Type",
        "titleMap": [
          {
            "name": "JaLC",
            "value": "JaLC"
          },
          {
            "name": "Crossref",
            "value": "Crossref"
          },
          {
            "name": "DataCite",
            "value": "DataCite"
          },
          {
            "name": "PMID【現在不使用】",
            "value": "PMID【現在不使用】"
          }
        ],
        "title_i18n": {
          "en": "Identifier Registration Type",
          "ja": "ID登録タイプ"
        },
        "title_i18n_temp": {
          "en": "Identifier Registration Type",
          "ja": "ID登録タイプ"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186819068",
    "title": "Identifier Registration",
    "title_i18n": {
      "en": "Identifier Registration",
      "ja": "ID登録"
    },
    "type": "fieldset"
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617353299429[].subitem_relation_type",
        "required": false,
        "title": "Relation Type",
        "titleMap": [
          {
            "name": "isVersionOf",
            "value": "isVersionOf"
          },
          {
            "name": "hasVersion",
            "value": "hasVersion"
          },
          {
            "name": "isPartOf",
            "value": "isPartOf"
          },
          {
            "name": "hasPart",
            "value": "hasPart"
          },
          {
            "name": "isReferencedBy",
            "value": "isReferencedBy"
          },
          {
            "name": "references",
            "value": "references"
          },
          {
            "name": "isFormatOf",
            "value": "isFormatOf"
          },
          {
            "name": "hasFormat",
            "value": "hasFormat"
          },
          {
            "name": "isReplacedBy",
            "value": "isReplacedBy"
          },
          {
            "name": "replaces",
            "value": "replaces"
          },
          {
            "name": "isRequiredBy",
            "value": "isRequiredBy"
          },
          {
            "name": "requires",
            "value": "requires"
          },
          {
            "name": "isSupplementedBy",
            "value": "isSupplementedBy"
          },
          {
            "name": "isSupplementTo",
            "value": "isSupplementTo"
          },
          {
            "name": "isIdenticalTo",
            "value": "isIdenticalTo"
          },
          {
            "name": "isDerivedFrom",
            "value": "isDerivedFrom"
          },
          {
            "name": "isSourceOf",
            "value": "isSourceOf"
          },
          {
            "name": "isCitedBy",
            "value": "isCitedBy"
          },
          {
            "name": "Cites",
            "value": "Cites"
          },
          {
            "name": "inSeries",
            "value": "inSeries"
          }
        ],
        "title_i18n": {
          "en": "Relation Type",
          "ja": "関連タイプ"
        },
        "title_i18n_temp": {
          "en": "Relation Type",
          "ja": "関連タイプ"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617353299429[].subitem_relation_type_id.subitem_relation_type_select",
            "required": false,
            "title": "Identifier Type",
            "titleMap": [
              {
                "name": "ARK",
                "value": "ARK"
              },
              {
                "name": "arXiv",
                "value": "arXiv"
              },
              {
                "name": "DOI",
                "value": "DOI"
              },
              {
                "name": "HDL",
                "value": "HDL"
              },
              {
                "name": "ICHUSHI",
                "value": "ICHUSHI"
              },
              {
                "name": "ISBN",
                "value": "ISBN"
              },
              {
                "name": "J-GLOBAL",
                "value": "J-GLOBAL"
              },
              {
                "name": "Local",
                "value": "Local"
              },
              {
                "name": "PISSN",
                "value": "PISSN"
              },
              {
                "name": "EISSN",
                "value": "EISSN"
              },
              {
                "name": "ISSN【非推奨】",
                "value": "ISSN"
              },
              {
                "name": "NAID【非推奨】",
                "value": "NAID"
              },
              {
                "name": "NCID",
                "value": "NCID"
              },
              {
                "name": "PMID【現在不使用】",
                "value": "PMID"
              },
              {
                "name": "PURL",
                "value": "PURL"
              },
              {
                "name": "SCOPUS",
                "value": "SCOPUS"
              },
              {
                "name": "URI",
                "value": "URI"
              },
              {
                "name": "WOS",
                "value": "WOS"
              },
              {
                "name": "CRID",
                "value": "CRID"
              }
            ],
            "title_i18n": {
              "en": "Identifier Type",
              "ja": "識別子タイプ"
            },
            "title_i18n_temp": {
              "en": "Identifier Type",
              "ja": "識別子タイプ"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617353299429[].subitem_relation_type_id.subitem_relation_type_id_text",
            "required": false,
            "title": "Related Identifier",
            "title_i18n": {
              "en": "Related Identifier",
              "ja": "関連識別子"
            },
            "title_i18n_temp": {
              "en": "Related Identifier",
              "ja": "関連識別子"
            },
            "type": "text"
          }
        ],
        "key": "item_1617353299429[].subitem_relation_type_id",
        "required": false,
        "title": "Related Identifier",
        "title_i18n": {
          "en": "Related Identifier",
          "ja": "関連識別子"
        },
        "title_i18n_temp": {
          "en": "Related Identifier",
          "ja": "関連識別子"
        },
        "type": "fieldset"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617353299429[].subitem_relation_name[].subitem_relation_name_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617353299429[].subitem_relation_name[].subitem_relation_name_text",
            "required": false,
            "title": "Related Title",
            "title_i18n": {
              "en": "Related Title",
              "ja": "関連名称"
            },
            "title_i18n_temp": {
              "en": "Related Title",
              "ja": "関連名称"
            },
            "type": "text"
          }
        ],
        "key": "item_1617353299429[].subitem_relation_name",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Related Title",
        "title_i18n": {
          "en": "Related Title",
          "ja": "関連名称"
        },
        "title_i18n_temp": {
          "en": "Related Title",
          "ja": "関連名称"
        }
      }
    ],
    "key": "item_1617353299429",
    "style": {
      "add": "btn-success"
    },
    "title": "Relation",
    "title_i18n": {
      "en": "Relation",
      "ja": "関連情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186859717[].subitem_temporal_text",
        "required": false,
        "title": "Temporal",
        "title_i18n": {
          "en": "Temporal",
          "ja": "時間的範囲"
        },
        "title_i18n_temp": {
          "en": "Temporal",
          "ja": "時間的範囲"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186859717[].subitem_temporal_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186859717",
    "style": {
      "add": "btn-success"
    },
    "title": "Temporal",
    "title_i18n": {
      "en": "Temporal",
      "ja": "時間的範囲"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_point.subitem_point_longitude",
            "required": false,
            "title": "Point Longitude",
            "title_i18n": {
              "en": "Point Longitude",
              "ja": "経度"
            },
            "title_i18n_temp": {
              "en": "Point Longitude",
              "ja": "経度"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_point.subitem_point_latitude",
            "required": false,
            "title": "Point Latitude",
            "title_i18n": {
              "en": "Point Latitude",
              "ja": "緯度"
            },
            "title_i18n_temp": {
              "en": "Point Latitude",
              "ja": "緯度"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186882738[].subitem_geolocation_point",
        "required": false,
        "title": "Geo Location Point",
        "title_i18n": {
          "en": "Geo Location Point",
          "ja": "位置情報（点）"
        },
        "title_i18n_temp": {
          "en": "Geo Location Point",
          "ja": "位置情報（点）"
        },
        "type": "fieldset"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_box.subitem_west_longitude",
            "required": false,
            "title": "West Bound Longitude",
            "title_i18n": {
              "en": "West Bound Longitude",
              "ja": "西部経度"
            },
            "title_i18n_temp": {
              "en": "West Bound Longitude",
              "ja": "西部経度"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_box.subitem_east_longitude",
            "required": false,
            "title": "East Bound Longitude",
            "title_i18n": {
              "en": "East Bound Longitude",
              "ja": "東部経度"
            },
            "title_i18n_temp": {
              "en": "East Bound Longitude",
              "ja": "東部経度"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_box.subitem_south_latitude",
            "required": false,
            "title": "South Bound Latitude",
            "title_i18n": {
              "en": "South Bound Latitude",
              "ja": "南部緯度"
            },
            "title_i18n_temp": {
              "en": "South Bound Latitude",
              "ja": "南部緯度"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_box.subitem_north_latitude",
            "required": false,
            "title": "North Bound Latitude",
            "title_i18n": {
              "en": "North Bound Latitude",
              "ja": "北部緯度"
            },
            "title_i18n_temp": {
              "en": "North Bound Latitude",
              "ja": "北部緯度"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186882738[].subitem_geolocation_box",
        "required": false,
        "title": "Geo Location Box",
        "title_i18n": {
          "en": "Geo Location Box",
          "ja": "位置情報（空間）"
        },
        "title_i18n_temp": {
          "en": "Geo Location Box",
          "ja": "位置情報（空間）"
        },
        "type": "fieldset"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186882738[].subitem_geolocation_place[].subitem_geolocation_place_text",
            "required": false,
            "title": "Geo Location Place",
            "title_i18n": {
              "en": "Geo Location Place",
              "ja": "位置情報（自由記述）"
            },
            "title_i18n_temp": {
              "en": "Geo Location Place",
              "ja": "位置情報（自由記述）"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186882738[].subitem_geolocation_place",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Geo Location Place",
        "title_i18n": {
          "en": "Geo Location Place",
          "ja": "位置情報（自由記述）"
        },
        "title_i18n_temp": {
          "en": "Geo Location Place",
          "ja": "位置情報（自由記述）"
        }
      }
    ],
    "key": "item_1617186882738",
    "style": {
      "add": "btn-success"
    },
    "title": "Geo Location",
    "title_i18n": {
      "en": "Geo Location",
      "ja": "位置情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funder_identifiers.subitem_funder_identifier_type",
            "required": false,
            "title": "Funder Identifier Type",
            "titleMap": [
              {
                "name": "Crossref Funder",
                "value": "Crossref Funder"
              },
              {
                "name": "e-Rad_funder",
                "value": "e-Rad_funder"
              },
              {
                "name": "GRID【非推奨】",
                "value": "GRID"
              },
              {
                "name": "ISNI",
                "value": "ISNI"
              },
              {
                "name": "ROR",
                "value": "ROR"
              },
              {
                "name": "Other",
                "value": "Other"
              }
            ],
            "title_i18n": {
              "en": "Funder Identifier Type",
              "ja": "助成機関識別子タイプ"
            },
            "title_i18n_temp": {
              "en": "Funder Identifier Type",
              "ja": "助成機関識別子タイプ"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funder_identifiers.subitem_funder_identifier_type_uri",
            "required": false,
            "title": "Funder Identifier Type URI",
            "title_i18n": {
              "en": "Funder Identifier Type URI",
              "ja": "助成機関識別子タイプURI"
            },
            "title_i18n_temp": {
              "en": "Funder Identifier Type URI",
              "ja": "助成機関識別子タイプURI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funder_identifiers.subitem_funder_identifier",
            "required": false,
            "title": "Funder Identifier",
            "title_i18n": {
              "en": "Funder Identifier",
              "ja": "助成機関識別子"
            },
            "title_i18n_temp": {
              "en": "Funder Identifier",
              "ja": "助成機関識別子"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186901218[].subitem_funder_identifiers",
        "required": false,
        "title": "Funder Identifier",
        "title_i18n": {
          "en": "Funder Identifier",
          "ja": "助成機関識別子"
        },
        "title_i18n_temp": {
          "en": "Funder Identifier",
          "ja": "助成機関識別子"
        },
        "type": "fieldset"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funder_names[].subitem_funder_name",
            "required": false,
            "title": "Funder Name",
            "title_i18n": {
              "en": "Funder Name",
              "ja": "助成機関名"
            },
            "title_i18n_temp": {
              "en": "Funder Name",
              "ja": "助成機関名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funder_names[].subitem_funder_name_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186901218[].subitem_funder_names",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Funder Name",
        "title_i18n": {
          "en": "Funder Name",
          "ja": "助成機関名"
        },
        "title_i18n_temp": {
          "en": "Funder Name",
          "ja": "助成機関名"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funding_stream_identifiers.subitem_funding_stream_identifier_type",
            "required": false,
            "title": "Funding Stream Identifier Type",
            "titleMap": [
              {
                "name": "Crossref Funder",
                "value": "Crossref Funder"
              },
              {
                "name": "JGN_fundingStream",
                "value": "JGN_fundingStream"
              }
            ],
            "title_i18n": {
              "en": "Funding Stream Identifier Type",
              "ja": "プログラム情報識別子タイプ"
            },
            "title_i18n_temp": {
              "en": "Funding Stream Identifier Type",
              "ja": "プログラム情報識別子タイプ"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funding_stream_identifiers.subitem_funding_stream_identifier_type_uri",
            "required": false,
            "title": "Funding Stream Identifier Type URI",
            "title_i18n": {
              "en": "Funding Stream Identifier Type URI",
              "ja": "プログラム情報識別子タイプURI"
            },
            "title_i18n_temp": {
              "en": "Funding Stream Identifier Type URI",
              "ja": "プログラム情報識別子タイプURI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funding_stream_identifiers.subitem_funding_stream_identifier",
            "required": false,
            "title": "Funding Stream Identifier",
            "title_i18n": {
              "en": "Funding Stream Identifier",
              "ja": "研究課題番号タイプ"
            },
            "title_i18n_temp": {
              "en": "Funding Stream Identifier",
              "ja": "研究課題番号タイプ"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186901218[].subitem_funding_stream_identifiers",
        "required": false,
        "title": "Funding Stream Identifiers",
        "title_i18n": {
          "en": "Funding Stream Identifiers",
          "ja": "プログラム情報識別子"
        },
        "title_i18n_temp": {
          "en": "Funding Stream Identifiers",
          "ja": "プログラム情報識別子"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funding_streams[].subitem_funding_stream_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_funding_streams.subitem_funding_stream",
            "required": false,
            "title": "Funding Stream",
            "title_i18n": {
              "en": "Funding Stream",
              "ja": "プログラム情報"
            },
            "title_i18n_temp": {
              "en": "Funding Stream",
              "ja": "プログラム情報"
            },
            "type": "text"
          }
        ],
        "key": "item_1617186901218[].subitem_funding_streams",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Funding Streams",
        "title_i18n": {
          "en": "Funding Streams",
          "ja": "プログラム情報"
        },
        "title_i18n_temp": {
          "en": "Funding Streams",
          "ja": "プログラム情報"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_award_numbers.subitem_award_uri",
            "required": false,
            "title": "Award Number URI",
            "title_i18n": {
              "en": "Award Number URI",
              "ja": "研究課題番号URI"
            },
            "title_i18n_temp": {
              "en": "Award Number URI",
              "ja": "研究課題番号URI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_award_numbers.subitem_award_number",
            "required": false,
            "title": "Award Number",
            "title_i18n": {
              "en": "Award Number",
              "ja": "研究課題番号"
            },
            "title_i18n_temp": {
              "en": "Award Number",
              "ja": "研究課題番号"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_award_numbers.subitem_award_number_type",
            "required": false,
            "title": "Award Number Type",
            "titleMap": [
              {
                "name": "JGN",
                "value": "JGN"
              }
            ],
            "title_i18n": {
              "en": "Award Number Type",
              "ja": "研究課題番号タイプ"
            },
            "title_i18n_temp": {
              "en": "Award Number Type",
              "ja": "研究課題番号タイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186901218[].subitem_award_numbers",
        "required": false,
        "title": "Award Number",
        "title_i18n": {
          "en": "Award Number",
          "ja": "研究課題番号"
        },
        "title_i18n_temp": {
          "en": "Award Number",
          "ja": "研究課題番号"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_award_titles[].subitem_award_title",
            "required": false,
            "title": "Award Title",
            "title_i18n": {
              "en": "Award Title",
              "ja": "研究課題名"
            },
            "title_i18n_temp": {
              "en": "Award Title",
              "ja": "研究課題名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617186901218[].subitem_award_titles[].subitem_award_title_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617186901218[].subitem_award_titles",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Award Title",
        "title_i18n": {
          "en": "Award Title",
          "ja": "研究課題名"
        },
        "title_i18n_temp": {
          "en": "Award Title",
          "ja": "研究課題名"
        }
      }
    ],
    "key": "item_1617186901218",
    "style": {
      "add": "btn-success"
    },
    "title": "Funder",
    "title_i18n": {
      "en": "Funder",
      "ja": "助成情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186920753[].subitem_source_identifier_type",
        "required": false,
        "title": "Source Identifier Type",
        "titleMap": [
          {
            "name": "PISSN",
            "value": "PISSN"
          },
          {
            "name": "EISSN",
            "value": "EISSN"
          },
          {
            "name": "ISSN",
            "value": "ISSN"
          },
          {
            "name": "NCID",
            "value": "NCID"
          }
        ],
        "title_i18n": {
          "en": "Source Identifier Type",
          "ja": "収録物識別子タイプ"
        },
        "title_i18n_temp": {
          "en": "Source Identifier Type",
          "ja": "収録物識別子タイプ"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186920753[].subitem_source_identifier",
        "required": false,
        "title": "Source Identifier",
        "title_i18n": {
          "en": "Source Identifier",
          "ja": "収録物識別子"
        },
        "title_i18n_temp": {
          "en": "Source Identifier",
          "ja": "収録物識別子"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186920753",
    "style": {
      "add": "btn-success"
    },
    "title": "Source Identifier",
    "title_i18n": {
      "en": "Source Identifier",
      "ja": "収録物識別子"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186941041[].subitem_source_title",
        "required": false,
        "title": "Source Title",
        "title_i18n": {
          "en": "Source Title",
          "ja": "収録物名"
        },
        "title_i18n_temp": {
          "en": "Source Title",
          "ja": "収録物名"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186941041[].subitem_source_title_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617186941041",
    "style": {
      "add": "btn-success"
    },
    "title": "Source Title",
    "title_i18n": {
      "en": "Source Title",
      "ja": "収録物名"
    }
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186959569.subitem_volume",
        "required": false,
        "title": "Volume",
        "title_i18n": {
          "en": "Volume",
          "ja": "巻"
        },
        "title_i18n_temp": {
          "en": "Volume",
          "ja": "巻"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186959569",
    "title": "Volume",
    "title_i18n": {
      "en": "Volume",
      "ja": "巻"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186981471.subitem_issue",
        "required": false,
        "title": "Issue",
        "title_i18n": {
          "en": "Issue",
          "ja": "号"
        },
        "title_i18n_temp": {
          "en": "Issue",
          "ja": "号"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186981471",
    "title": "Issue",
    "title_i18n": {
      "en": "Issue",
      "ja": "号"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617186994930.subitem_number_of_pages",
        "required": false,
        "title": "Number of Pages",
        "title_i18n": {
          "en": "Number of Pages",
          "ja": "ページ数"
        },
        "title_i18n_temp": {
          "en": "Number of Pages",
          "ja": "ページ数"
        },
        "type": "text"
      }
    ],
    "key": "item_1617186994930",
    "title": "Number of Pages",
    "title_i18n": {
      "en": "Number of Pages",
      "ja": "ページ数"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187024783.subitem_start_page",
        "required": false,
        "title": "Start Page",
        "title_i18n": {
          "en": "Start Page",
          "ja": "開始ページ"
        },
        "title_i18n_temp": {
          "en": "Start Page",
          "ja": "開始ページ"
        },
        "type": "text"
      }
    ],
    "key": "item_1617187024783",
    "title": "Start Page",
    "title_i18n": {
      "en": "Start Page",
      "ja": "開始ページ"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187045071.subitem_end_page",
        "required": false,
        "title": "End Page",
        "title_i18n": {
          "en": "End Page",
          "ja": "終了ページ"
        },
        "title_i18n_temp": {
          "en": "End Page",
          "ja": "終了ページ"
        },
        "type": "text"
      }
    ],
    "key": "item_1617187045071",
    "title": "End Page",
    "title_i18n": {
      "en": "End Page",
      "ja": "終了ページ"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187056579.bibliographic_titles[].bibliographic_title",
            "required": false,
            "title": "Title",
            "title_i18n": {
              "en": "Title",
              "ja": "タイトル"
            },
            "title_i18n_temp": {
              "en": "Title",
              "ja": "タイトル"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187056579.bibliographic_titles[].bibliographic_titleLang",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187056579.bibliographic_titles",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Journal Title",
        "title_i18n": {
          "en": "Journal Title",
          "ja": "雑誌名"
        },
        "title_i18n_temp": {
          "en": "Journal Title",
          "ja": "雑誌名"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187056579.bibliographicVolumeNumber",
        "required": false,
        "title": "Volume Number",
        "title_i18n": {
          "en": "Volume Number",
          "ja": "巻"
        },
        "title_i18n_temp": {
          "en": "Volume Number",
          "ja": "巻"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187056579.bibliographicIssueNumber",
        "required": false,
        "title": "Issue Number",
        "title_i18n": {
          "en": "Issue Number",
          "ja": "号"
        },
        "title_i18n_temp": {
          "en": "Issue Number",
          "ja": "号"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187056579.bibliographicPageStart",
        "required": false,
        "title": "Page Start",
        "title_i18n": {
          "en": "Page Start",
          "ja": "開始ページ"
        },
        "title_i18n_temp": {
          "en": "Page Start",
          "ja": "開始ページ"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187056579.bibliographicPageEnd",
        "required": false,
        "title": "Page End",
        "title_i18n": {
          "en": "Page End",
          "ja": "終了ページ"
        },
        "title_i18n_temp": {
          "en": "Page End",
          "ja": "終了ページ"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187056579.bibliographicNumberOfPages",
        "required": false,
        "title": "Number of Page",
        "title_i18n": {
          "en": "Number of Page",
          "ja": "ページ数"
        },
        "title_i18n_temp": {
          "en": "Number of Page",
          "ja": "ページ数"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "format": "yyyy-MM-dd",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187056579.bibliographicIssueDates.bibliographicIssueDate",
            "required": false,
            "templateUrl": "/static/templates/weko_deposit/datepicker_multi_format.html",
            "title": "Date",
            "title_i18n": {
              "en": "Date",
              "ja": "日付"
            },
            "title_i18n_temp": {
              "en": "Date",
              "ja": "日付"
            },
            "type": "template"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187056579.bibliographicIssueDates.bibliographicIssueDateType",
            "required": false,
            "title": "Date Type",
            "titleMap": [
              {
                "name": "",
                "value": ""
              },
              {
                "name": "Issued",
                "value": "Issued"
              }
            ],
            "title_i18n": {
              "en": "Date Type",
              "ja": "日付タイプ"
            },
            "title_i18n_temp": {
              "en": "Date Type",
              "ja": "日付タイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187056579.bibliographicIssueDates",
        "required": false,
        "title": "Issue Date",
        "title_i18n": {
          "en": "Issue Date",
          "ja": "発行日"
        },
        "title_i18n_temp": {
          "en": "Issue Date",
          "ja": "発行日"
        },
        "type": "fieldset"
      }
    ],
    "key": "item_1617187056579",
    "title": "Bibliographic Information",
    "title_i18n": {
      "en": "Bibliographic Information",
      "ja": "書誌情報"
    },
    "type": "fieldset"
  },
  {
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187087799.subitem_dissertationnumber",
        "required": false,
        "title": "Dissertation Number",
        "title_i18n": {
          "en": "Dissertation Number",
          "ja": "学位授与番号"
        },
        "title_i18n_temp": {
          "en": "Dissertation Number",
          "ja": "学位授与番号"
        },
        "type": "text"
      }
    ],
    "key": "item_1617187087799",
    "title": "Dissertation Number",
    "title_i18n": {
      "en": "Dissertation Number",
      "ja": "学位授与番号"
    },
    "type": "fieldset"
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187112279[].subitem_degreename_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187112279[].subitem_degreename",
        "required": false,
        "title": "Degree Name",
        "title_i18n": {
          "en": "Degree Name",
          "ja": "学位名"
        },
        "title_i18n_temp": {
          "en": "Degree Name",
          "ja": "学位名"
        },
        "type": "text"
      }
    ],
    "key": "item_1617187112279",
    "style": {
      "add": "btn-success"
    },
    "title": "Degree Name",
    "title_i18n": {
      "en": "Degree Name",
      "ja": "学位名"
    }
  },
  {
    "items": [
      {
        "format": "yyyy-MM-dd",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187136212.subitem_dategranted",
        "required": false,
        "templateUrl": "/static/templates/weko_deposit/datepicker_multi_format.html",
        "title": "Date Granted",
        "title_i18n": {
          "en": "Date Granted",
          "ja": "学位授与年月日"
        },
        "title_i18n_temp": {
          "en": "Date Granted",
          "ja": "学位授与年月日"
        },
        "type": "template"
      }
    ],
    "key": "item_1617187136212",
    "title": "Date Granted",
    "title_i18n": {
      "en": "Date Granted",
      "ja": "学位授与年月日"
    },
    "type": "fieldset"
  },
  {
    "add": "New",
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617944105607[].subitem_degreegrantor_identifier[].subitem_degreegrantor_identifier_scheme",
            "required": false,
            "title": "Degree Grantor Name Identifier Scheme",
            "titleMap": [
              {
                "name": "kakenhi",
                "value": "kakenhi"
              }
            ],
            "title_i18n": {
              "en": "Degree Grantor Name Identifier Scheme",
              "ja": "学位授与機関識別子Scheme"
            },
            "title_i18n_temp": {
              "en": "Degree Grantor Name Identifier Scheme",
              "ja": "学位授与機関識別子Scheme"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617944105607[].subitem_degreegrantor_identifier[].subitem_degreegrantor_identifier_name",
            "required": false,
            "title": "Degree Grantor Name Identifier",
            "title_i18n": {
              "en": "Degree Grantor Name Identifier",
              "ja": "学位授与機関識別子"
            },
            "title_i18n_temp": {
              "en": "Degree Grantor Name Identifier",
              "ja": "学位授与機関識別子"
            },
            "type": "text"
          }
        ],
        "key": "item_1617944105607[].subitem_degreegrantor_identifier",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Degree Grantor Name Identifier",
        "title_i18n": {
          "en": "Degree Grantor Name Identifier",
          "ja": "学位授与機関識別子"
        },
        "title_i18n_temp": {
          "en": "Degree Grantor Name Identifier",
          "ja": "学位授与機関識別子"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617944105607[].subitem_degreegrantor[].subitem_degreegrantor_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617944105607[].subitem_degreegrantor[].subitem_degreegrantor_name",
            "required": false,
            "title": "Degree Grantor Name",
            "title_i18n": {
              "en": "Degree Grantor Name",
              "ja": "学位授与機関名"
            },
            "title_i18n_temp": {
              "en": "Degree Grantor Name",
              "ja": "学位授与機関名"
            },
            "type": "text"
          }
        ],
        "key": "item_1617944105607[].subitem_degreegrantor",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Degree Grantor Name",
        "title_i18n": {
          "en": "Degree Grantor Name",
          "ja": "学位授与機関名"
        },
        "title_i18n_temp": {
          "en": "Degree Grantor Name",
          "ja": "学位授与機関名"
        }
      }
    ],
    "key": "item_1617944105607",
    "style": {
      "add": "btn-success"
    },
    "title": "Degree Grantor",
    "title_i18n": {
      "en": "Degree Grantor",
      "ja": "学位授与機関"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_names[].subitem_conference_name",
            "required": false,
            "title": "Conference Name",
            "title_i18n": {
              "en": "Conference Name",
              "ja": "会議名"
            },
            "title_i18n_temp": {
              "en": "Conference Name",
              "ja": "会議名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_names[].subitem_conference_name_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187187528[].subitem_conference_names",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Conference Name",
        "title_i18n": {
          "en": "Conference Name",
          "ja": "会議名"
        },
        "title_i18n_temp": {
          "en": "Conference Name",
          "ja": "会議名"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187187528[].subitem_conference_sequence",
        "required": false,
        "title": "Conference Sequence",
        "title_i18n": {
          "en": "Conference Sequence",
          "ja": "回次"
        },
        "title_i18n_temp": {
          "en": "Conference Sequence",
          "ja": "回次"
        },
        "type": "text"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_sponsors[].subitem_conference_sponsor",
            "required": false,
            "title": "Conference Sponsor",
            "title_i18n": {
              "en": "Conference Sponsor",
              "ja": "主催機関"
            },
            "title_i18n_temp": {
              "en": "Conference Sponsor",
              "ja": "主催機関"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_sponsors[].subitem_conference_sponsor_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187187528[].subitem_conference_sponsors",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Conference Sponsor",
        "title_i18n": {
          "en": "Conference Sponsor",
          "ja": "主催機関"
        },
        "title_i18n_temp": {
          "en": "Conference Sponsor",
          "ja": "主催機関"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_start_year",
            "required": false,
            "title": "Start Year",
            "title_i18n": {
              "en": "Start Year",
              "ja": "開始年"
            },
            "title_i18n_temp": {
              "en": "Start Year",
              "ja": "開始年"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_start_month",
            "required": false,
            "title": "Start Month",
            "title_i18n": {
              "en": "Start Month",
              "ja": "開始月"
            },
            "title_i18n_temp": {
              "en": "Start Month",
              "ja": "開始月"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_start_day",
            "required": false,
            "title": "Start Day",
            "title_i18n": {
              "en": "Start Day",
              "ja": "開始日"
            },
            "title_i18n_temp": {
              "en": "Start Day",
              "ja": "開始日"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_end_year",
            "required": false,
            "title": "End Year",
            "title_i18n": {
              "en": "End Year",
              "ja": "終了年"
            },
            "title_i18n_temp": {
              "en": "End Year",
              "ja": "終了年"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_end_month",
            "required": false,
            "title": "End Month",
            "title_i18n": {
              "en": "End Month",
              "ja": "終了月"
            },
            "title_i18n_temp": {
              "en": "End Month",
              "ja": "終了月"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_end_day",
            "required": false,
            "title": "End Day",
            "title_i18n": {
              "en": "End Day",
              "ja": "終了日"
            },
            "title_i18n_temp": {
              "en": "End Day",
              "ja": "終了日"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_period",
            "required": false,
            "title": "Conference Date",
            "title_i18n": {
              "en": "Conference Date",
              "ja": "開催期間"
            },
            "title_i18n_temp": {
              "en": "Conference Date",
              "ja": "開催期間"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_date.subitem_conference_date_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187187528[].subitem_conference_date",
        "required": false,
        "title": "Conference Date",
        "title_i18n": {
          "en": "Conference Date",
          "ja": "開催期間"
        },
        "title_i18n_temp": {
          "en": "Conference Date",
          "ja": "開催期間"
        },
        "type": "fieldset"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_venues[].subitem_conference_venue",
            "required": false,
            "title": "Conference Venue",
            "title_i18n": {
              "en": "Conference Venue",
              "ja": "開催会場"
            },
            "title_i18n_temp": {
              "en": "Conference Venue",
              "ja": "開催会場"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_venues[].subitem_conference_venue_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187187528[].subitem_conference_venues",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Conference Venue",
        "title_i18n": {
          "en": "Conference Venue",
          "ja": "開催会場"
        },
        "title_i18n_temp": {
          "en": "Conference Venue",
          "ja": "開催会場"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_places[].subitem_conference_place",
            "required": false,
            "title": "Conference Place",
            "title_i18n": {
              "en": "Conference Place",
              "ja": "開催地"
            },
            "title_i18n_temp": {
              "en": "Conference Place",
              "ja": "開催地"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617187187528[].subitem_conference_places[].subitem_conference_place_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1617187187528[].subitem_conference_places",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Conference Place",
        "title_i18n": {
          "en": "Conference Place",
          "ja": "開催地"
        },
        "title_i18n_temp": {
          "en": "Conference Place",
          "ja": "開催地"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617187187528[].subitem_conference_country",
        "required": false,
        "title": "Conference Country",
        "titleMap": [
          {
            "name": "JPN",
            "value": "JPN"
          },
          {
            "name": "ABW",
            "value": "ABW"
          },
          {
            "name": "AFG",
            "value": "AFG"
          },
          {
            "name": "AGO",
            "value": "AGO"
          },
          {
            "name": "AIA",
            "value": "AIA"
          },
          {
            "name": "ALA",
            "value": "ALA"
          },
          {
            "name": "ALB",
            "value": "ALB"
          },
          {
            "name": "AND",
            "value": "AND"
          },
          {
            "name": "ARE",
            "value": "ARE"
          },
          {
            "name": "ARG",
            "value": "ARG"
          },
          {
            "name": "ARM",
            "value": "ARM"
          },
          {
            "name": "ASM",
            "value": "ASM"
          },
          {
            "name": "ATA",
            "value": "ATA"
          },
          {
            "name": "ATF",
            "value": "ATF"
          },
          {
            "name": "ATG",
            "value": "ATG"
          },
          {
            "name": "AUS",
            "value": "AUS"
          },
          {
            "name": "AUT",
            "value": "AUT"
          },
          {
            "name": "AZE",
            "value": "AZE"
          },
          {
            "name": "BDI",
            "value": "BDI"
          },
          {
            "name": "BEL",
            "value": "BEL"
          },
          {
            "name": "BEN",
            "value": "BEN"
          },
          {
            "name": "BES",
            "value": "BES"
          },
          {
            "name": "BFA",
            "value": "BFA"
          },
          {
            "name": "BGD",
            "value": "BGD"
          },
          {
            "name": "BGR",
            "value": "BGR"
          },
          {
            "name": "BHR",
            "value": "BHR"
          },
          {
            "name": "BHS",
            "value": "BHS"
          },
          {
            "name": "BIH",
            "value": "BIH"
          },
          {
            "name": "BLM",
            "value": "BLM"
          },
          {
            "name": "BLR",
            "value": "BLR"
          },
          {
            "name": "BLZ",
            "value": "BLZ"
          },
          {
            "name": "BMU",
            "value": "BMU"
          },
          {
            "name": "BOL",
            "value": "BOL"
          },
          {
            "name": "BRA",
            "value": "BRA"
          },
          {
            "name": "BRB",
            "value": "BRB"
          },
          {
            "name": "BRN",
            "value": "BRN"
          },
          {
            "name": "BTN",
            "value": "BTN"
          },
          {
            "name": "BVT",
            "value": "BVT"
          },
          {
            "name": "BWA",
            "value": "BWA"
          },
          {
            "name": "CAF",
            "value": "CAF"
          },
          {
            "name": "CAN",
            "value": "CAN"
          },
          {
            "name": "CCK",
            "value": "CCK"
          },
          {
            "name": "CHE",
            "value": "CHE"
          },
          {
            "name": "CHL",
            "value": "CHL"
          },
          {
            "name": "CHN",
            "value": "CHN"
          },
          {
            "name": "CIV",
            "value": "CIV"
          },
          {
            "name": "CMR",
            "value": "CMR"
          },
          {
            "name": "COD",
            "value": "COD"
          },
          {
            "name": "COG",
            "value": "COG"
          },
          {
            "name": "COK",
            "value": "COK"
          },
          {
            "name": "COL",
            "value": "COL"
          },
          {
            "name": "COM",
            "value": "COM"
          },
          {
            "name": "CPV",
            "value": "CPV"
          },
          {
            "name": "CRI",
            "value": "CRI"
          },
          {
            "name": "CUB",
            "value": "CUB"
          },
          {
            "name": "CUW",
            "value": "CUW"
          },
          {
            "name": "CXR",
            "value": "CXR"
          },
          {
            "name": "CYM",
            "value": "CYM"
          },
          {
            "name": "CYP",
            "value": "CYP"
          },
          {
            "name": "CZE",
            "value": "CZE"
          },
          {
            "name": "DEU",
            "value": "DEU"
          },
          {
            "name": "DJI",
            "value": "DJI"
          },
          {
            "name": "DMA",
            "value": "DMA"
          },
          {
            "name": "DNK",
            "value": "DNK"
          },
          {
            "name": "DOM",
            "value": "DOM"
          },
          {
            "name": "DZA",
            "value": "DZA"
          },
          {
            "name": "ECU",
            "value": "ECU"
          },
          {
            "name": "EGY",
            "value": "EGY"
          },
          {
            "name": "ERI",
            "value": "ERI"
          },
          {
            "name": "ESH",
            "value": "ESH"
          },
          {
            "name": "ESP",
            "value": "ESP"
          },
          {
            "name": "EST",
            "value": "EST"
          },
          {
            "name": "ETH",
            "value": "ETH"
          },
          {
            "name": "FIN",
            "value": "FIN"
          },
          {
            "name": "FJI",
            "value": "FJI"
          },
          {
            "name": "FLK",
            "value": "FLK"
          },
          {
            "name": "FRA",
            "value": "FRA"
          },
          {
            "name": "FRO",
            "value": "FRO"
          },
          {
            "name": "FSM",
            "value": "FSM"
          },
          {
            "name": "GAB",
            "value": "GAB"
          },
          {
            "name": "GBR",
            "value": "GBR"
          },
          {
            "name": "GEO",
            "value": "GEO"
          },
          {
            "name": "GGY",
            "value": "GGY"
          },
          {
            "name": "GHA",
            "value": "GHA"
          },
          {
            "name": "GIB",
            "value": "GIB"
          },
          {
            "name": "GIN",
            "value": "GIN"
          },
          {
            "name": "GLP",
            "value": "GLP"
          },
          {
            "name": "GMB",
            "value": "GMB"
          },
          {
            "name": "GNB",
            "value": "GNB"
          },
          {
            "name": "GNQ",
            "value": "GNQ"
          },
          {
            "name": "GRC",
            "value": "GRC"
          },
          {
            "name": "GRD",
            "value": "GRD"
          },
          {
            "name": "GRL",
            "value": "GRL"
          },
          {
            "name": "GTM",
            "value": "GTM"
          },
          {
            "name": "GUF",
            "value": "GUF"
          },
          {
            "name": "GUM",
            "value": "GUM"
          },
          {
            "name": "GUY",
            "value": "GUY"
          },
          {
            "name": "HKG",
            "value": "HKG"
          },
          {
            "name": "HMD",
            "value": "HMD"
          },
          {
            "name": "HND",
            "value": "HND"
          },
          {
            "name": "HRV",
            "value": "HRV"
          },
          {
            "name": "HTI",
            "value": "HTI"
          },
          {
            "name": "HUN",
            "value": "HUN"
          },
          {
            "name": "IDN",
            "value": "IDN"
          },
          {
            "name": "IMN",
            "value": "IMN"
          },
          {
            "name": "IND",
            "value": "IND"
          },
          {
            "name": "IOT",
            "value": "IOT"
          },
          {
            "name": "IRL",
            "value": "IRL"
          },
          {
            "name": "IRN",
            "value": "IRN"
          },
          {
            "name": "IRQ",
            "value": "IRQ"
          },
          {
            "name": "ISL",
            "value": "ISL"
          },
          {
            "name": "ISR",
            "value": "ISR"
          },
          {
            "name": "ITA",
            "value": "ITA"
          },
          {
            "name": "JAM",
            "value": "JAM"
          },
          {
            "name": "JEY",
            "value": "JEY"
          },
          {
            "name": "JOR",
            "value": "JOR"
          },
          {
            "name": "KAZ",
            "value": "KAZ"
          },
          {
            "name": "KEN",
            "value": "KEN"
          },
          {
            "name": "KGZ",
            "value": "KGZ"
          },
          {
            "name": "KHM",
            "value": "KHM"
          },
          {
            "name": "KIR",
            "value": "KIR"
          },
          {
            "name": "KNA",
            "value": "KNA"
          },
          {
            "name": "KOR",
            "value": "KOR"
          },
          {
            "name": "KWT",
            "value": "KWT"
          },
          {
            "name": "LAO",
            "value": "LAO"
          },
          {
            "name": "LBN",
            "value": "LBN"
          },
          {
            "name": "LBR",
            "value": "LBR"
          },
          {
            "name": "LBY",
            "value": "LBY"
          },
          {
            "name": "LCA",
            "value": "LCA"
          },
          {
            "name": "LIE",
            "value": "LIE"
          },
          {
            "name": "LKA",
            "value": "LKA"
          },
          {
            "name": "LSO",
            "value": "LSO"
          },
          {
            "name": "LTU",
            "value": "LTU"
          },
          {
            "name": "LUX",
            "value": "LUX"
          },
          {
            "name": "LVA",
            "value": "LVA"
          },
          {
            "name": "MAC",
            "value": "MAC"
          },
          {
            "name": "MAF",
            "value": "MAF"
          },
          {
            "name": "MAR",
            "value": "MAR"
          },
          {
            "name": "MCO",
            "value": "MCO"
          },
          {
            "name": "MDA",
            "value": "MDA"
          },
          {
            "name": "MDG",
            "value": "MDG"
          },
          {
            "name": "MDV",
            "value": "MDV"
          },
          {
            "name": "MEX",
            "value": "MEX"
          },
          {
            "name": "MHL",
            "value": "MHL"
          },
          {
            "name": "MKD",
            "value": "MKD"
          },
          {
            "name": "MLI",
            "value": "MLI"
          },
          {
            "name": "MLT",
            "value": "MLT"
          },
          {
            "name": "MMR",
            "value": "MMR"
          },
          {
            "name": "MNE",
            "value": "MNE"
          },
          {
            "name": "MNG",
            "value": "MNG"
          },
          {
            "name": "MNP",
            "value": "MNP"
          },
          {
            "name": "MOZ",
            "value": "MOZ"
          },
          {
            "name": "MRT",
            "value": "MRT"
          },
          {
            "name": "MSR",
            "value": "MSR"
          },
          {
            "name": "MTQ",
            "value": "MTQ"
          },
          {
            "name": "MUS",
            "value": "MUS"
          },
          {
            "name": "MWI",
            "value": "MWI"
          },
          {
            "name": "MYS",
            "value": "MYS"
          },
          {
            "name": "MYT",
            "value": "MYT"
          },
          {
            "name": "NAM",
            "value": "NAM"
          },
          {
            "name": "NCL",
            "value": "NCL"
          },
          {
            "name": "NER",
            "value": "NER"
          },
          {
            "name": "NFK",
            "value": "NFK"
          },
          {
            "name": "NGA",
            "value": "NGA"
          },
          {
            "name": "NIC",
            "value": "NIC"
          },
          {
            "name": "NIU",
            "value": "NIU"
          },
          {
            "name": "NLD",
            "value": "NLD"
          },
          {
            "name": "NOR",
            "value": "NOR"
          },
          {
            "name": "NPL",
            "value": "NPL"
          },
          {
            "name": "NRU",
            "value": "NRU"
          },
          {
            "name": "NZL",
            "value": "NZL"
          },
          {
            "name": "OMN",
            "value": "OMN"
          },
          {
            "name": "PAK",
            "value": "PAK"
          },
          {
            "name": "PAN",
            "value": "PAN"
          },
          {
            "name": "PCN",
            "value": "PCN"
          },
          {
            "name": "PER",
            "value": "PER"
          },
          {
            "name": "PHL",
            "value": "PHL"
          },
          {
            "name": "PLW",
            "value": "PLW"
          },
          {
            "name": "PNG",
            "value": "PNG"
          },
          {
            "name": "POL",
            "value": "POL"
          },
          {
            "name": "PRI",
            "value": "PRI"
          },
          {
            "name": "PRK",
            "value": "PRK"
          },
          {
            "name": "PRT",
            "value": "PRT"
          },
          {
            "name": "PRY",
            "value": "PRY"
          },
          {
            "name": "PSE",
            "value": "PSE"
          },
          {
            "name": "PYF",
            "value": "PYF"
          },
          {
            "name": "QAT",
            "value": "QAT"
          },
          {
            "name": "REU",
            "value": "REU"
          },
          {
            "name": "ROU",
            "value": "ROU"
          },
          {
            "name": "RUS",
            "value": "RUS"
          },
          {
            "name": "RWA",
            "value": "RWA"
          },
          {
            "name": "SAU",
            "value": "SAU"
          },
          {
            "name": "SDN",
            "value": "SDN"
          },
          {
            "name": "SEN",
            "value": "SEN"
          },
          {
            "name": "SGP",
            "value": "SGP"
          },
          {
            "name": "SGS",
            "value": "SGS"
          },
          {
            "name": "SHN",
            "value": "SHN"
          },
          {
            "name": "SJM",
            "value": "SJM"
          },
          {
            "name": "SLB",
            "value": "SLB"
          },
          {
            "name": "SLE",
            "value": "SLE"
          },
          {
            "name": "SLV",
            "value": "SLV"
          },
          {
            "name": "SMR",
            "value": "SMR"
          },
          {
            "name": "SOM",
            "value": "SOM"
          },
          {
            "name": "SPM",
            "value": "SPM"
          },
          {
            "name": "SRB",
            "value": "SRB"
          },
          {
            "name": "SSD",
            "value": "SSD"
          },
          {
            "name": "STP",
            "value": "STP"
          },
          {
            "name": "SUR",
            "value": "SUR"
          },
          {
            "name": "SVK",
            "value": "SVK"
          },
          {
            "name": "SVN",
            "value": "SVN"
          },
          {
            "name": "SWE",
            "value": "SWE"
          },
          {
            "name": "SWZ",
            "value": "SWZ"
          },
          {
            "name": "SXM",
            "value": "SXM"
          },
          {
            "name": "SYC",
            "value": "SYC"
          },
          {
            "name": "SYR",
            "value": "SYR"
          },
          {
            "name": "TCA",
            "value": "TCA"
          },
          {
            "name": "TCD",
            "value": "TCD"
          },
          {
            "name": "TGO",
            "value": "TGO"
          },
          {
            "name": "THA",
            "value": "THA"
          },
          {
            "name": "TJK",
            "value": "TJK"
          },
          {
            "name": "TKL",
            "value": "TKL"
          },
          {
            "name": "TKM",
            "value": "TKM"
          },
          {
            "name": "TLS",
            "value": "TLS"
          },
          {
            "name": "TON",
            "value": "TON"
          },
          {
            "name": "TTO",
            "value": "TTO"
          },
          {
            "name": "TUN",
            "value": "TUN"
          },
          {
            "name": "TUR",
            "value": "TUR"
          },
          {
            "name": "TUV",
            "value": "TUV"
          },
          {
            "name": "TWN",
            "value": "TWN"
          },
          {
            "name": "TZA",
            "value": "TZA"
          },
          {
            "name": "UGA",
            "value": "UGA"
          },
          {
            "name": "UKR",
            "value": "UKR"
          },
          {
            "name": "UMI",
            "value": "UMI"
          },
          {
            "name": "URY",
            "value": "URY"
          },
          {
            "name": "USA",
            "value": "USA"
          },
          {
            "name": "UZB",
            "value": "UZB"
          },
          {
            "name": "VAT",
            "value": "VAT"
          },
          {
            "name": "VCT",
            "value": "VCT"
          },
          {
            "name": "VEN",
            "value": "VEN"
          },
          {
            "name": "VGB",
            "value": "VGB"
          },
          {
            "name": "VIR",
            "value": "VIR"
          },
          {
            "name": "VNM",
            "value": "VNM"
          },
          {
            "name": "VUT",
            "value": "VUT"
          },
          {
            "name": "WLF",
            "value": "WLF"
          },
          {
            "name": "WSM",
            "value": "WSM"
          },
          {
            "name": "YEM",
            "value": "YEM"
          },
          {
            "name": "ZAF",
            "value": "ZAF"
          },
          {
            "name": "ZMB",
            "value": "ZMB"
          },
          {
            "name": "ZWE",
            "value": "ZWE"
          }
        ],
        "title_i18n": {
          "en": "Conference Country",
          "ja": "開催国"
        },
        "title_i18n_temp": {
          "en": "Conference Country",
          "ja": "開催国"
        },
        "type": "select"
      }
    ],
    "key": "item_1617187187528",
    "style": {
      "add": "btn-success"
    },
    "title": "Conference",
    "title_i18n": {
      "en": "Conference",
      "ja": "会議記述"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].filename",
        "onChange": "fileNameSelect(this, form, modelValue)",
        "required": false,
        "templateUrl": "/static/templates/weko_deposit/datalist.html",
        "title": "FileName",
        "titleMap": [],
        "title_i18n": {
          "en": "FileName",
          "ja": "ファイル名"
        },
        "title_i18n_temp": {
          "en": "FileName",
          "ja": "ファイル名"
        },
        "type": "template",
        "useDataList": true
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "fieldHtmlClass": "file-text-url",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617605131499[].url.url",
            "readonly": false,
            "required": false,
            "title": "URL",
            "title_i18n": {
              "en": "URL",
              "ja": "本文URL"
            },
            "title_i18n_temp": {
              "en": "URL",
              "ja": "本文URL"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617605131499[].url.label",
            "required": false,
            "title": "Label",
            "title_i18n": {
              "en": "Label",
              "ja": "ラベル"
            },
            "title_i18n_temp": {
              "en": "Label",
              "ja": "ラベル"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617605131499[].url.objectType",
            "required": false,
            "title": "Object Type",
            "titleMap": [
              {
                "name": "abstract",
                "value": "abstract"
              },
              {
                "name": "dataset",
                "value": "dataset"
              },
              {
                "name": "fulltext",
                "value": "fulltext"
              },
              {
                "name": "iiif",
                "value": "iiif"
              },
              {
                "name": "software",
                "value": "software"
              },
              {
                "name": "summary",
                "value": "summary"
              },
              {
                "name": "thumbnail",
                "value": "thumbnail"
              },
              {
                "name": "other",
                "value": "other"
              }
            ],
            "title_i18n": {
              "en": "Object Type",
              "ja": "オブジェクトタイプ"
            },
            "title_i18n_temp": {
              "en": "Object Type",
              "ja": "オブジェクトタイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1617605131499[].url",
        "required": false,
        "title": "Text URL",
        "title_i18n": {
          "en": "Text URL",
          "ja": "本文URL"
        },
        "title_i18n_temp": {
          "en": "Text URL",
          "ja": "本文URL"
        },
        "type": "fieldset"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].format",
        "required": false,
        "title": "Format",
        "title_i18n": {
          "en": "Format",
          "ja": "フォーマット"
        },
        "title_i18n_temp": {
          "en": "Format",
          "ja": "フォーマット"
        },
        "type": "text"
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617605131499[].filesize[].value",
            "required": false,
            "title": "Size",
            "title_i18n": {
              "en": "Size",
              "ja": "サイズ"
            },
            "title_i18n_temp": {
              "en": "Size",
              "ja": "サイズ"
            },
            "type": "text"
          }
        ],
        "key": "item_1617605131499[].filesize",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Size",
        "title_i18n": {
          "en": "Size",
          "ja": "サイズ"
        },
        "title_i18n_temp": {
          "en": "Size",
          "ja": "サイズ"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617605131499[].fileDate[].fileDateType",
            "required": false,
            "title": "Date Type",
            "titleMap": [
              {
                "name": "Accepted",
                "value": "Accepted"
              },
              {
                "name": "Available",
                "value": "Available"
              },
              {
                "name": "Collected",
                "value": "Collected"
              },
              {
                "name": "Copyrighted",
                "value": "Copyrighted"
              },
              {
                "name": "Created",
                "value": "Created"
              },
              {
                "name": "Issued",
                "value": "Issued"
              },
              {
                "name": "Submitted",
                "value": "Submitted"
              },
              {
                "name": "Updated",
                "value": "Updated"
              },
              {
                "name": "Valid",
                "value": "Valid"
              }
            ],
            "title_i18n": {
              "en": "Date Type",
              "ja": "日付タイプ"
            },
            "title_i18n_temp": {
              "en": "Date Type",
              "ja": "日付タイプ"
            },
            "type": "select"
          },
          {
            "format": "yyyy-MM-dd",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1617605131499[].fileDate[].fileDateValue",
            "required": false,
            "templateUrl": "/static/templates/weko_deposit/datepicker_multi_format.html",
            "title": "Date",
            "title_i18n": {
              "en": "Date",
              "ja": "日付"
            },
            "title_i18n_temp": {
              "en": "Date",
              "ja": "日付"
            },
            "type": "template"
          }
        ],
        "key": "item_1617605131499[].fileDate",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Date",
        "title_i18n": {
          "en": "Date",
          "ja": "日付"
        },
        "title_i18n_temp": {
          "en": "Date",
          "ja": "日付"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].version",
        "required": false,
        "title": "Version",
        "title_i18n": {
          "en": "Version",
          "ja": "バージョン情報"
        },
        "title_i18n_temp": {
          "en": "Version",
          "ja": "バージョン情報"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].displaytype",
        "required": false,
        "title": "Preview",
        "titleMap": [
          {
            "name": "Detail",
            "name_i18n": {
              "en": "Detail",
              "ja": "詳細表示"
            },
            "value": "detail"
          },
          {
            "name": "Simple",
            "name_i18n": {
              "en": "Simple",
              "ja": "簡易表示"
            },
            "value": "simple"
          },
          {
            "name": "Preview",
            "name_i18n": {
              "en": "Preview",
              "ja": "プレビュー"
            },
            "value": "preview"
          }
        ],
        "title_i18n": {
          "en": "Preview",
          "ja": "表示形式"
        },
        "title_i18n_temp": {
          "en": "Preview",
          "ja": "表示形式"
        },
        "type": "select"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].licensetype",
        "required": false,
        "title": "License",
        "titleMap": [],
        "title_i18n": {
          "en": "License",
          "ja": "ライセンス"
        },
        "title_i18n_temp": {
          "en": "License",
          "ja": "ライセンス"
        },
        "type": "select"
      },
      {
        "condition": "model.item_1617605131499[arrayIndex].licensetype == 'license_free'",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].licensefree",
        "notitle": true,
        "required": false,
        "title_i18n_temp": {
          "en": "",
          "ja": ""
        },
        "type": "textarea"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].accessrole",
        "onChange": "accessRoleChange()",
        "required": false,
        "title": "Access",
        "titleMap": [
          {
            "name": "Open Access",
            "name_i18n": {
              "en": "Open Access",
              "ja": "オープンアクセス"
            },
            "value": "open_access"
          },
          {
            "name": "Input Open Access Date",
            "name_i18n": {
              "en": "Input Open Access Date",
              "ja": "オープンアクセス日を指定する"
            },
            "value": "open_date"
          },
          {
            "name": "Registered User Only",
            "name_i18n": {
              "en": "Registered User Only",
              "ja": "ログインユーザのみ"
            },
            "value": "open_login"
          },
          {
            "name": "Do not Publish",
            "name_i18n": {
              "en": "Do not Publish",
              "ja": "公開しない"
            },
            "value": "open_no"
          }
        ],
        "title_i18n": {
          "en": "Access",
          "ja": "アクセス"
        },
        "title_i18n_temp": {
          "en": "Access",
          "ja": "アクセス"
        },
        "type": "radios"
      },
      {
        "condition": "model.item_1617605131499[arrayIndex].accessrole == 'open_date'",
        "format": "yyyy-MM-dd",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].date[0].dateValue",
        "required": false,
        "templateUrl": "/static/templates/weko_deposit/datepicker.html",
        "title": "Opendate",
        "title_i18n": {
          "en": "Opendate",
          "ja": "公開日"
        },
        "title_i18n_temp": {
          "en": "Opendate",
          "ja": "公開日"
        },
        "type": "template"
      },
      {
        "condition": "model.item_1617605131499[arrayIndex].accessrole == 'open_login'",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617605131499[].groups",
        "required": false,
        "title": "Group",
        "titleMap": [],
        "title_i18n": {
          "en": "Group",
          "ja": "グループ"
        },
        "title_i18n_temp": {
          "en": "Group",
          "ja": "グループ"
        },
        "type": "select"
      }
    ],
    "key": "item_1617605131499",
    "style": {
      "add": "btn-success"
    },
    "title": "File Information",
    "title_i18n": {
      "en": "File Information",
      "ja": "ファイル情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617620223087[].subitem_heading_banner_headline",
        "required": false,
        "title": "Heading",
        "title_i18n": {
          "en": "Heading",
          "ja": "大見出し"
        },
        "title_i18n_temp": {
          "en": "Heading",
          "ja": "大見出し"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617620223087[].subitem_heading_headline",
        "required": false,
        "title": "Subheading",
        "title_i18n": {
          "en": "Subheading",
          "ja": "小見出し"
        },
        "title_i18n_temp": {
          "en": "Subheading",
          "ja": "小見出し"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1617620223087[].subitem_heading_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1617620223087",
    "style": {
      "add": "btn-success"
    },
    "title": "Heading",
    "title_i18n": {
      "en": "Heading",
      "ja": "見出し"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591601[].holding_agent_names[].holding_agent_name",
            "required": false,
            "title": "Holding Agent Name",
            "title_i18n": {
              "en": "Holding Agent Name",
              "ja": "所蔵機関名"
            },
            "title_i18n_temp": {
              "en": "Holding Agent Name",
              "ja": "所蔵機関名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591601[].holding_agent_names[].holding_agent_names_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591601[].holding_agent_names",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Holding Agent",
        "title_i18n": {
          "en": "Holding Agent",
          "ja": "所蔵機関"
        },
        "title_i18n_temp": {
          "en": "Holding Agent",
          "ja": "所蔵機関"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591601[].holding_agent_name_identifier.holding_agent_name_idenfitier_value",
            "required": false,
            "title": "Holding Agent Name Identifier",
            "title_i18n": {
              "en": "Holding Agent Name Identifier",
              "ja": "所蔵機関識別子"
            },
            "title_i18n_temp": {
              "en": "Holding Agent Name Identifier",
              "ja": "所蔵機関識別子"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591601[].holding_agent_name_identifier.holding_agent_name_identifier_scheme",
            "required": false,
            "title": "Holding Agent Name Identifier Schema",
            "titleMap": [
              {
                "name": "kakenhi【非推奨】",
                "value": "kakenhi"
              },
              {
                "name": "ISNI",
                "value": "ISNI"
              },
              {
                "name": "Ringgold",
                "value": "Ringgold"
              },
              {
                "name": "GRID【非推奨】",
                "value": "GRID"
              },
              {
                "name": "ROR",
                "value": "ROR"
              },
              {
                "name": "FANO",
                "value": "FANO"
              },
              {
                "name": "ISIL",
                "value": "ISIL"
              },
              {
                "name": "MARC",
                "value": "MARC"
              },
              {
                "name": "OCLC",
                "value": "OCLC"
              }
            ],
            "title_i18n": {
              "en": "Holding Agent Name Identifier Schema",
              "ja": "所蔵機関識別子スキーマ"
            },
            "title_i18n_temp": {
              "en": "Holding Agent Name Identifier Schema",
              "ja": "所蔵機関識別子スキーマ"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591601[].holding_agent_name_identifier.holding_agent_name_identifier_uri",
            "required": false,
            "title": "Holding Agent Name Identifier URI",
            "title_i18n": {
              "en": "Holding Agent Name Identifier URI",
              "ja": "所蔵機関識別子URI"
            },
            "title_i18n_temp": {
              "en": "Holding Agent Name Identifier URI",
              "ja": "所蔵機関識別子URI"
            },
            "type": "text"
          }
        ],
        "key": "item_1698591601[].holding_agent_name_identifier",
        "required": false,
        "title": "Holding Agent Name Identifier",
        "title_i18n": {
          "en": "Holding Agent Name Identifier",
          "ja": "所蔵機関識別子"
        },
        "title_i18n_temp": {
          "en": "Holding Agent Name Identifier",
          "ja": "所蔵機関識別子"
        }
      }
    ],
    "key": "item_1698591601",
    "style": {
      "add": "btn-success"
    },
    "title": "Holding Agent",
    "title_i18n": {
      "en": "Holding Agent",
      "ja": "所蔵機関"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591602[].subitem_dcterms_date",
        "required": false,
        "title": "Date Literal",
        "title_i18n": {
          "en": "Date Literal",
          "ja": "日付（リテラル）"
        },
        "title_i18n_temp": {
          "en": "Date Literal",
          "ja": "日付（リテラル）"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591602[].subitem_dcterms_date_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591602",
    "style": {
      "add": "btn-success"
    },
    "title": "Date(Literal)",
    "title_i18n": {
      "en": "Date(Literal)",
      "ja": "日付（リテラル）"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591603[].jpcoar_dataset_series",
        "required": false,
        "title": "Dataset Series",
        "titleMap": [
          {
            "name": "True",
            "value": "True"
          },
          {
            "name": "False",
            "value": "False"
          }
        ],
        "title_i18n": {
          "en": "Dataset Series",
          "ja": "データセットシリーズ"
        },
        "title_i18n_temp": {
          "en": "Dataset Series",
          "ja": "データセットシリーズ"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591603",
    "style": {
      "add": "btn-success"
    },
    "title": "Dataset Series",
    "title_i18n": {
      "en": "Dataset Series",
      "ja": "データセットシリーズ"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591604[].publisher_names[].publisher_name",
            "required": false,
            "title": "Publisher Name",
            "title_i18n": {
              "en": "Publisher Name",
              "ja": "出版者名"
            },
            "title_i18n_temp": {
              "en": "Publisher Name",
              "ja": "出版者名"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591604[].publisher_names[].publisher_name_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591604[].publisher_names",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Publisher Name",
        "title_i18n": {
          "en": "Publisher Name",
          "ja": "出版者名"
        },
        "title_i18n_temp": {
          "en": "Publisher Name",
          "ja": "出版者名"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591604[].publisher_descriptions[].publisher_description",
            "required": false,
            "title": "Publisher Description",
            "title_i18n": {
              "en": "Publisher Description",
              "ja": "出版者注記"
            },
            "title_i18n_temp": {
              "en": "Publisher Description",
              "ja": "出版者注記"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591604[].publisher_descriptions[].publisher_description_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591604[].publisher_descriptions",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Publisher Description",
        "title_i18n": {
          "en": "Publisher Description",
          "ja": "出版者注記"
        },
        "title_i18n_temp": {
          "en": "Publisher Description",
          "ja": "出版者注記"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591604[].publisher_locations[].publisher_location",
            "required": false,
            "title": "Publication Place",
            "title_i18n": {
              "en": "Publication Place",
              "ja": "出版地"
            },
            "title_i18n_temp": {
              "en": "Publication Place",
              "ja": "出版地"
            },
            "type": "text"
          }
        ],
        "key": "item_1698591604[].publisher_locations",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Publication Place",
        "title_i18n": {
          "en": "Publication Place",
          "ja": "出版地"
        },
        "title_i18n_temp": {
          "en": "Publication Place",
          "ja": "出版地"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591604[].publication_places[].publication_place",
            "required": false,
            "title": "Publication Place (Country code)",
            "title_i18n": {
              "en": "Publication Place (Country code)",
              "ja": "出版地（国名コード）"
            },
            "title_i18n_temp": {
              "en": "Publication Place (Country code)",
              "ja": "出版地（国名コード）"
            },
            "type": "text"
          }
        ],
        "key": "item_1698591604[].publication_places",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Publication Place (Country code)",
        "title_i18n": {
          "en": "Publication Place (Country code)",
          "ja": "出版地（国名コード）"
        },
        "title_i18n_temp": {
          "en": "Publication Place (Country code)",
          "ja": "出版地（国名コード）"
        }
      }
    ],
    "key": "item_1698591604",
    "style": {
      "add": "btn-success"
    },
    "title": "Publisher Information",
    "title_i18n": {
      "en": "Publisher Information",
      "ja": "出版者情報"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591605[].dcterms_extent",
        "required": false,
        "title": "Extent",
        "title_i18n": {
          "en": "Extent",
          "ja": "大きさ"
        },
        "title_i18n_temp": {
          "en": "Extent",
          "ja": "大きさ"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591605[].dcterms_extent_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591605",
    "style": {
      "add": "btn-success"
    },
    "title": "Extent",
    "title_i18n": {
      "en": "Extent",
      "ja": "大きさ"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_contributors[].contributor_type",
            "required": false,
            "title": "Hosting Institution Type",
            "titleMap": [
              {
                "name": "HostingInstitution",
                "value": "HostingInstitution"
              }
            ],
            "title_i18n": {
              "en": "Hosting Institution Type",
              "ja": "提供機関タイプ"
            },
            "title_i18n_temp": {
              "en": "Hosting Institution Type",
              "ja": "提供機関タイプ"
            },
            "type": "select"
          },
          {
            "add": "New",
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "items": [
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1698591606[].catalog_contributors[].contributor_names[].contributor_name",
                "required": false,
                "title": "Hosting Institution Name",
                "title_i18n": {
                  "en": "Hosting Institution Name",
                  "ja": "提供機関名"
                },
                "title_i18n_temp": {
                  "en": "Hosting Institution Name",
                  "ja": "提供機関名"
                },
                "type": "text"
              },
              {
                "isHide": false,
                "isNonDisplay": false,
                "isShowList": false,
                "isSpecifyNewline": false,
                "key": "item_1698591606[].catalog_contributors[].contributor_names[].contributor_name_language",
                "required": false,
                "title": "Language",
                "titleMap": [
                  {
                    "name": "ja",
                    "value": "ja"
                  },
                  {
                    "name": "ja-Kana",
                    "value": "ja-Kana"
                  },
                  {
                    "name": "ja-Latn",
                    "value": "ja-Latn"
                  },
                  {
                    "name": "en",
                    "value": "en"
                  },
                  {
                    "name": "fr",
                    "value": "fr"
                  },
                  {
                    "name": "it",
                    "value": "it"
                  },
                  {
                    "name": "de",
                    "value": "de"
                  },
                  {
                    "name": "es",
                    "value": "es"
                  },
                  {
                    "name": "zh-cn",
                    "value": "zh-cn"
                  },
                  {
                    "name": "zh-tw",
                    "value": "zh-tw"
                  },
                  {
                    "name": "ru",
                    "value": "ru"
                  },
                  {
                    "name": "la",
                    "value": "la"
                  },
                  {
                    "name": "ms",
                    "value": "ms"
                  },
                  {
                    "name": "eo",
                    "value": "eo"
                  },
                  {
                    "name": "ar",
                    "value": "ar"
                  },
                  {
                    "name": "el",
                    "value": "el"
                  },
                  {
                    "name": "ko",
                    "value": "ko"
                  }
                ],
                "title_i18n": {
                  "en": "Language",
                  "ja": "言語"
                },
                "title_i18n_temp": {
                  "en": "Language",
                  "ja": "言語"
                },
                "type": "select"
              }
            ],
            "key": "item_1698591606[].catalog_contributors[].contributor_names",
            "required": false,
            "style": {
              "add": "btn-success"
            },
            "title": "Hosting Institution Name",
            "title_i18n": {
              "en": "Hosting Institution Name",
              "ja": "提供機関名"
            },
            "title_i18n_temp": {
              "en": "Hosting Institution Name",
              "ja": "提供機関名"
            }
          }
        ],
        "key": "item_1698591606[].catalog_contributors",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Hosting Institution",
        "title_i18n": {
          "en": "Hosting Institution",
          "ja": "提供機関"
        },
        "title_i18n_temp": {
          "en": "Hosting Institution",
          "ja": "提供機関"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_identifiers[].catalog_identifier",
            "required": false,
            "title": "Identifier",
            "title_i18n": {
              "en": "Identifier",
              "ja": "識別子"
            },
            "title_i18n_temp": {
              "en": "Identifier",
              "ja": "識別子"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_identifiers[].catalog_identifier_type",
            "required": false,
            "title": "Identifier Type",
            "titleMap": [
              {
                "name": "DOI",
                "value": "DOI"
              },
              {
                "name": "HDL",
                "value": "HDL"
              },
              {
                "name": "URI",
                "value": "URI"
              }
            ],
            "title_i18n": {
              "en": "Identifier Type",
              "ja": "識別子タイプ"
            },
            "title_i18n_temp": {
              "en": "Identifier Type",
              "ja": "識別子タイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591606[].catalog_identifiers",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Identifier",
        "title_i18n": {
          "en": "Identifier",
          "ja": "識別子"
        },
        "title_i18n_temp": {
          "en": "Identifier",
          "ja": "識別子"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_titles[].catalog_title",
            "required": false,
            "title": "Title",
            "title_i18n": {
              "en": "Title",
              "ja": "タイトル"
            },
            "title_i18n_temp": {
              "en": "Title",
              "ja": "タイトル"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_titles[].catalog_title_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591606[].catalog_titles",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Title",
        "title_i18n": {
          "en": "Title",
          "ja": "タイトル"
        },
        "title_i18n_temp": {
          "en": "Title",
          "ja": "タイトル"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_descriptions[].catalog_description",
            "required": false,
            "title": "Description",
            "title_i18n": {
              "en": "Description",
              "ja": "内容記述"
            },
            "title_i18n_temp": {
              "en": "Description",
              "ja": "内容記述"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_descriptions[].catalog_description_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_descriptions[].catalog_description_type",
            "required": false,
            "title": "Description Type",
            "titleMap": [
              {
                "name": "Abstract",
                "value": "Abstract"
              },
              {
                "name": "Methods",
                "value": "Methods"
              },
              {
                "name": "TableOfContents",
                "value": "TableOfContents"
              },
              {
                "name": "TechnicalInfo",
                "value": "TechnicalInfo"
              },
              {
                "name": "Other",
                "value": "Other"
              }
            ],
            "title_i18n": {
              "en": "Description Type",
              "ja": "内容記述タイプ"
            },
            "title_i18n_temp": {
              "en": "Description Type",
              "ja": "内容記述タイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591606[].catalog_descriptions",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Description",
        "title_i18n": {
          "en": "Description",
          "ja": "内容記述"
        },
        "title_i18n_temp": {
          "en": "Description",
          "ja": "内容記述"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_subjects[].catalog_subject",
            "required": false,
            "title": "Subject",
            "title_i18n": {
              "en": "Subject",
              "ja": "主題"
            },
            "title_i18n_temp": {
              "en": "Subject",
              "ja": "主題"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_subjects[].catalog_subject_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_subjects[].catalog_subject_uri",
            "required": false,
            "title": "Subject URI",
            "title_i18n": {
              "en": "Subject URI",
              "ja": "主題URI"
            },
            "title_i18n_temp": {
              "en": "Subject URI",
              "ja": "主題URI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_subjects[].catalog_subject_scheme",
            "required": false,
            "title": "Subject Scheme",
            "titleMap": [
              {
                "name": "BSH",
                "value": "BSH"
              },
              {
                "name": "DDC",
                "value": "DDC"
              },
              {
                "name": "e-Rad",
                "value": "e-Rad"
              },
              {
                "name": "LCC",
                "value": "LCC"
              },
              {
                "name": "LCSH",
                "value": "LCSH"
              },
              {
                "name": "",
                "value": ""
              },
              {
                "name": "MeSH",
                "value": "MeSH"
              },
              {
                "name": "NDC",
                "value": "NDC"
              },
              {
                "name": "NDLC",
                "value": "NDLC"
              },
              {
                "name": "NDLSH",
                "value": "NDLSH"
              },
              {
                "name": "SciVal",
                "value": "SciVal"
              },
              {
                "name": "UDC",
                "value": "UDC"
              },
              {
                "name": "Other",
                "value": "Other"
              }
            ],
            "title_i18n": {
              "en": "Subject Scheme",
              "ja": "主題スキーマ"
            },
            "title_i18n_temp": {
              "en": "Subject Scheme",
              "ja": "主題スキーマ"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591606[].catalog_subjects",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Subject",
        "title_i18n": {
          "en": "Subject",
          "ja": "主題"
        },
        "title_i18n_temp": {
          "en": "Subject",
          "ja": "主題"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_licenses[].catalog_license",
            "required": false,
            "title": "License",
            "title_i18n": {
              "en": "License",
              "ja": "ライセンス"
            },
            "title_i18n_temp": {
              "en": "License",
              "ja": "ライセンス"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_license.catalog_license_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_license.catalog_license_type",
            "required": false,
            "title": "License Type",
            "titleMap": [
              {
                "name": "file",
                "value": "file"
              },
              {
                "name": "metadata",
                "value": "metadata"
              },
              {
                "name": "thumbnail",
                "value": "thumbnail"
              }
            ],
            "title_i18n": {
              "en": "License Type",
              "ja": "ライセンスタイプ"
            },
            "title_i18n_temp": {
              "en": "License Type",
              "ja": "ライセンスタイプ"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_license.catalog_license_rdf_resource",
            "required": false,
            "title": "RDF Resource",
            "title_i18n": {
              "en": "RDF Resource",
              "ja": "RDFリソース"
            },
            "title_i18n_temp": {
              "en": "RDF Resource",
              "ja": "RDFリソース"
            },
            "type": "text"
          }
        ],
        "key": "item_1698591606[].catalog_licenses",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "License",
        "title_i18n": {
          "en": "License",
          "ja": "ライセンス"
        },
        "title_i18n_temp": {
          "en": "License",
          "ja": "ライセンス"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_rights[].catalog_right",
            "required": false,
            "title": "Access Rights",
            "title_i18n": {
              "en": "Access Rights",
              "ja": "アクセス権"
            },
            "title_i18n_temp": {
              "en": "Access Rights",
              "ja": "アクセス権"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_rights[].catalog_right_language",
            "required": false,
            "title": "Language",
            "titleMap": [
              {
                "name": "ja",
                "value": "ja"
              },
              {
                "name": "ja-Kana",
                "value": "ja-Kana"
              },
              {
                "name": "ja-Latn",
                "value": "ja-Latn"
              },
              {
                "name": "en",
                "value": "en"
              },
              {
                "name": "fr",
                "value": "fr"
              },
              {
                "name": "it",
                "value": "it"
              },
              {
                "name": "de",
                "value": "de"
              },
              {
                "name": "es",
                "value": "es"
              },
              {
                "name": "zh-cn",
                "value": "zh-cn"
              },
              {
                "name": "zh-tw",
                "value": "zh-tw"
              },
              {
                "name": "ru",
                "value": "ru"
              },
              {
                "name": "la",
                "value": "la"
              },
              {
                "name": "ms",
                "value": "ms"
              },
              {
                "name": "eo",
                "value": "eo"
              },
              {
                "name": "ar",
                "value": "ar"
              },
              {
                "name": "el",
                "value": "el"
              },
              {
                "name": "ko",
                "value": "ko"
              }
            ],
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "title_i18n_temp": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_rights[].catalog_right_rdf_resource",
            "required": false,
            "title": "RDF Resource",
            "title_i18n": {
              "en": "RDF Resource",
              "ja": "RDFリソース"
            },
            "title_i18n_temp": {
              "en": "RDF Resource",
              "ja": "RDFリソース"
            },
            "type": "text"
          }
        ],
        "key": "item_1698591606[].catalog_rights",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Access Rights",
        "title_i18n": {
          "en": "Access Rights",
          "ja": "アクセス権"
        },
        "title_i18n_temp": {
          "en": "Access Rights",
          "ja": "アクセス権"
        }
      },
      {
        "add": "New",
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_access_rights[].catalog_access_right_access_rights",
            "required": false,
            "title": "Access Rights",
            "titleMap": [
              {
                "name": "embargoed access",
                "value": "embargoed access"
              },
              {
                "name": "metadata only access",
                "value": "metadata only access"
              },
              {
                "name": "restricted access",
                "value": "restricted access"
              },
              {
                "name": "open access",
                "value": "open access"
              }
            ],
            "title_i18n": {
              "en": "Access Rights",
              "ja": "アクセス権"
            },
            "title_i18n_temp": {
              "en": "Access Rights",
              "ja": "アクセス権"
            },
            "type": "select"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_access_rights[].catalog_access_right_rdf_resource",
            "required": false,
            "title": "RDF Resource",
            "title_i18n": {
              "en": "RDF Resource",
              "ja": "RDFリソース"
            },
            "title_i18n_temp": {
              "en": "RDF Resource",
              "ja": "RDFリソース"
            },
            "type": "text"
          }
        ],
        "key": "item_1698591606[].catalog_access_rights",
        "required": false,
        "style": {
          "add": "btn-success"
        },
        "title": "Access Rights",
        "title_i18n": {
          "en": "Access Rights",
          "ja": "アクセス権"
        },
        "title_i18n_temp": {
          "en": "Access Rights",
          "ja": "アクセス権"
        }
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "items": [
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_file.catalog_file_uri",
            "required": false,
            "title": "Thumbnail URI",
            "title_i18n": {
              "en": "Thumbnail URI",
              "ja": "代表画像URI"
            },
            "title_i18n_temp": {
              "en": "Thumbnail URI",
              "ja": "代表画像URI"
            },
            "type": "text"
          },
          {
            "isHide": false,
            "isNonDisplay": false,
            "isShowList": false,
            "isSpecifyNewline": false,
            "key": "item_1698591606[].catalog_file.catalog_file_object_type",
            "required": false,
            "title": "Object Type",
            "titleMap": [
              {
                "name": "thumbnail",
                "value": "thumbnail"
              }
            ],
            "title_i18n": {
              "en": "Object Type",
              "ja": "オブジェクトタイプ"
            },
            "title_i18n_temp": {
              "en": "Object Type",
              "ja": "オブジェクトタイプ"
            },
            "type": "select"
          }
        ],
        "key": "item_1698591606[].catalog_file",
        "required": false,
        "title": "Thumbnail",
        "title_i18n": {
          "en": "Thumbnail",
          "ja": "代表画像"
        },
        "title_i18n_temp": {
          "en": "Thumbnail",
          "ja": "代表画像"
        },
        "type": "fieldset"
      }
    ],
    "key": "item_1698591606",
    "style": {
      "add": "btn-success"
    },
    "title": "Catalog",
    "title_i18n": {
      "en": "Catalog",
      "ja": "カタログ"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591607[].original_language",
        "required": false,
        "title": "Original Language",
        "title_i18n": {
          "en": "Original Language",
          "ja": "原文の言語"
        },
        "title_i18n_temp": {
          "en": "Original Language",
          "ja": "原文の言語"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591607[].original_language_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591607",
    "style": {
      "add": "btn-success"
    },
    "title": "Original Language",
    "title_i18n": {
      "en": "Original Language",
      "ja": "原文の言語"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591608[].volume_title",
        "required": false,
        "title": "Edition",
        "title_i18n_temp": {
          "en": "",
          "ja": ""
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591608[].volume_title_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591608",
    "style": {
      "add": "btn-success"
    },
    "title": "Volume Title",
    "title_i18n": {
      "en": "Volume Title",
      "ja": "部編名"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591609[].edition",
        "required": false,
        "title": "Edition",
        "title_i18n": {
          "en": "Edition",
          "ja": "版"
        },
        "title_i18n_temp": {
          "en": "Edition",
          "ja": "版"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591609[].edition_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591609",
    "style": {
      "add": "btn-success"
    },
    "title": "Edition",
    "title_i18n": {
      "en": "Edition",
      "ja": "版"
    }
  },
  {
    "add": "New",
    "items": [
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591610[].jpcoar_format",
        "required": false,
        "title": "Physical Format",
        "title_i18n": {
          "en": "Physical Format",
          "ja": "物理的形態"
        },
        "title_i18n_temp": {
          "en": "Physical Format",
          "ja": "物理的形態"
        },
        "type": "text"
      },
      {
        "isHide": false,
        "isNonDisplay": false,
        "isShowList": false,
        "isSpecifyNewline": false,
        "key": "item_1698591610[].json_format_language",
        "required": false,
        "title": "Language",
        "titleMap": [
          {
            "name": "ja",
            "value": "ja"
          },
          {
            "name": "ja-Kana",
            "value": "ja-Kana"
          },
          {
            "name": "ja-Latn",
            "value": "ja-Latn"
          },
          {
            "name": "en",
            "value": "en"
          },
          {
            "name": "fr",
            "value": "fr"
          },
          {
            "name": "it",
            "value": "it"
          },
          {
            "name": "de",
            "value": "de"
          },
          {
            "name": "es",
            "value": "es"
          },
          {
            "name": "zh-cn",
            "value": "zh-cn"
          },
          {
            "name": "zh-tw",
            "value": "zh-tw"
          },
          {
            "name": "ru",
            "value": "ru"
          },
          {
            "name": "la",
            "value": "la"
          },
          {
            "name": "ms",
            "value": "ms"
          },
          {
            "name": "eo",
            "value": "eo"
          },
          {
            "name": "ar",
            "value": "ar"
          },
          {
            "name": "el",
            "value": "el"
          },
          {
            "name": "ko",
            "value": "ko"
          }
        ],
        "title_i18n": {
          "en": "Language",
          "ja": "言語"
        },
        "title_i18n_temp": {
          "en": "Language",
          "ja": "言語"
        },
        "type": "select"
      }
    ],
    "key": "item_1698591610",
    "style": {
      "add": "btn-success"
    },
    "title": "Physical Format",
    "title_i18n": {
      "en": "Physical Format",
      "ja": "物理的形態"
    }
  },
  {
    "items": [
      {
        "key": "item_1727008761239.interim",
        "title": "abc",
        "titleMap": [
          {
            "name": "a",
            "value": "a"
          },
          {
            "name": "b",
            "value": "b"
          },
          {
            "name": "c",
            "value": "c"
          },
          {
            "name": "d",
            "value": "d"
          }
        ],
        "title_i18n": {
          "en": "",
          "ja": ""
        },
        "type": "select"
      }
    ],
    "key": "item_1727008761239",
    "title": "abc",
    "title_i18n": {
      "en": "",
      "ja": ""
    },
    "type": "fieldset"
  },
  {
    "condition": 1,
    "items": [
      {
        "key": "parentkey.subitem_systemidt_identifier",
        "title": "SYSTEMIDT Identifier",
        "type": "text"
      },
      {
        "key": "parentkey.subitem_systemidt_identifier_type",
        "title": "SYSTEMIDT Identifier Type",
        "titleMap": [
          {
            "name": "DOI",
            "value": "DOI"
          },
          {
            "name": "HDL",
            "value": "HDL"
          },
          {
            "name": "URI",
            "value": "URI"
          }
        ],
        "type": "select"
      }
    ],
    "key": "system_identifier_doi",
    "title": "Persistent Identifier(DOI)",
    "title_i18n": {
      "en": "Persistent Identifier(DOI)",
      "ja": "永続識別子（DOI）"
    },
    "type": "fieldset"
  },
  {
    "condition": 1,
    "items": [
      {
        "key": "parentkey.subitem_systemidt_identifier",
        "title": "SYSTEMIDT Identifier",
        "type": "text"
      },
      {
        "key": "parentkey.subitem_systemidt_identifier_type",
        "title": "SYSTEMIDT Identifier Type",
        "titleMap": [
          {
            "name": "DOI",
            "value": "DOI"
          },
          {
            "name": "HDL",
            "value": "HDL"
          },
          {
            "name": "URI",
            "value": "URI"
          }
        ],
        "type": "select"
      }
    ],
    "key": "system_identifier_hdl",
    "title": "Persistent Identifier(HDL)",
    "title_i18n": {
      "en": "Persistent Identifier(HDL)",
      "ja": "永続識別子（HDL）"
    },
    "type": "fieldset"
  },
  {
    "condition": 1,
    "items": [
      {
        "key": "parentkey.subitem_systemidt_identifier",
        "title": "SYSTEMIDT Identifier",
        "type": "text"
      },
      {
        "key": "parentkey.subitem_systemidt_identifier_type",
        "title": "SYSTEMIDT Identifier Type",
        "titleMap": [
          {
            "name": "DOI",
            "value": "DOI"
          },
          {
            "name": "HDL",
            "value": "HDL"
          },
          {
            "name": "URI",
            "value": "URI"
          }
        ],
        "type": "select"
      }
    ],
    "key": "system_identifier_uri",
    "title": "Persistent Identifier(URI)",
    "title_i18n": {
      "en": "Persistent Identifier(URI)",
      "ja": "永続識別子（URI）"
    },
    "type": "fieldset"
  },
  {
    "condition": 1,
    "items": [
      {
        "add": "New",
        "items": [
          {
            "key": "parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_label",
            "title": "SYSTEMFILE Filename Label",
            "type": "text"
          },
          {
            "key": "parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_type",
            "title": "SYSTEMFILE Filename Type",
            "titleMap": [
              {
                "name": "Abstract",
                "value": "Abstract"
              },
              {
                "name": "Fulltext",
                "value": "Fulltext"
              },
              {
                "name": "Summary",
                "value": "Summary"
              },
              {
                "name": "Thumbnail",
                "value": "Thumbnail"
              },
              {
                "name": "Other",
                "value": "Other"
              }
            ],
            "type": "select"
          },
          {
            "key": "parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_uri",
            "title": "SYSTEMFILE Filename URI",
            "type": "text"
          }
        ],
        "key": "parentkey.subitem_systemfile_filename",
        "style": {
          "add": "btn-success"
        },
        "title": "SYSTEMFILE Filename"
      },
      {
        "key": "parentkey.subitem_systemfile_mimetype",
        "title": "SYSTEMFILE MimeType",
        "type": "text"
      },
      {
        "key": "parentkey.subitem_systemfile_size",
        "title": "SYSTEMFILE Size",
        "type": "text"
      },
      {
        "add": "New",
        "items": [
          {
            "format": "yyyy-MM-dd",
            "key": "parentkey.subitem_systemfile_datetime[].subitem_systemfile_datetime_date",
            "templateUrl": "/static/templates/weko_deposit/datepicker.html",
            "title": "SYSTEMFILE DateTime Date",
            "type": "template"
          },
          {
            "key": "parentkey.subitem_systemfile_datetime[].subitem_systemfile_datetime_type",
            "title": "SYSTEMFILE DateTime Type",
            "titleMap": [
              {
                "name": "Accepted",
                "value": "Accepted"
              },
              {
                "name": "Available",
                "value": "Available"
              },
              {
                "name": "Collected",
                "value": "Collected"
              },
              {
                "name": "Copyrighted",
                "value": "Copyrighted"
              },
              {
                "name": "Created",
                "value": "Created"
              },
              {
                "name": "Issued",
                "value": "Issued"
              },
              {
                "name": "Submitted",
                "value": "Submitted"
              },
              {
                "name": "Updated",
                "value": "Updated"
              },
              {
                "name": "Valid",
                "value": "Valid"
              }
            ],
            "type": "select"
          }
        ],
        "key": "parentkey.subitem_systemfile_datetime",
        "style": {
          "add": "btn-success"
        },
        "title": "SYSTEMFILE DateTime"
      },
      {
        "key": "parentkey.subitem_systemfile_version",
        "title": "SYSTEMFILE Version",
        "type": "text"
      }
    ],
    "key": "system_file",
    "title": "File Information",
    "title_i18n": {
      "en": "File Information",
      "ja": "ファイル情報"
    },
    "type": "fieldset"
  }
]
```

#### 更新履歴

<table>
<thead>
<tr class="header">
<th>日付</th>
<th>GitHubコミットID</th>
<th>更新内容</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>