# JSON Schema

  - 目的・用途

指定したアイテムタイプの入力フォーム用 JSON Schema（スキーマ定義）を取得する機能を提供する。

  - 利用方法

| **Method** | **HTTP request**                         | **Description** |
| ---------- | ---------------------------------------- | --------------- |
| GET        | **/items/jsonschema/**{ITEMTYPE_ID}      | アイテムタイプのJSON Schemaを取得する |

パスパラメータ

| **GET /items/jsonschema/**{ITEMTYPE_ID} |     |             |
| ---------------------------------------- | --- | ----------- |
| パラメータ                                    | 値   | 説明          |
| ITEMTYPE_ID                             | int | アイテムタイプID（item_type_id）を指定 |

（アクティビティ別スキーマを取得する `GET /items/jsonschema/{ITEMTYPE_ID}/{activity_id}` も存在する）

レスポンス例：

`GET /items/jsonschema/9`

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "",
  "properties": {
    "item_1617186331708": {
      "items": {
        "properties": {
          "subitem_1551255647225": {
            "format": "text",
            "title": "Title",
            "title_i18n": {
              "en": "Title",
              "ja": "タイトル"
            },
            "type": "string"
          },
          "subitem_1551255648112": {
            "currentEnum": [
              "ja",
              "ja-Kana",
              "ja-Latn",
              "en",
              "fr",
              "it",
              "de",
              "es",
              "zh-cn",
              "zh-tw",
              "ru",
              "la",
              "ms",
              "eo",
              "ar",
              "el",
              "ko"
            ],
            "enum": [
              null,
              "ja",
              "ja-Kana",
              "ja-Latn",
              "en",
              "fr",
              "it",
              "de",
              "es",
              "zh-cn",
              "zh-tw",
              "ru",
              "la",
              "ms",
              "eo",
              "ar",
              "el",
              "ko"
            ],
            "format": "select",
            "title": "Language",
            "type": [
              "null",
              "string"
            ]
          }
        },
        "required": [
          "subitem_1551255647225",
          "subitem_1551255648112"
        ],
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Title",
      "type": "array"
    },
    "item_1617186419668": {
      "items": {
        "properties": {
          "creatorAffiliations": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "affiliationNameIdentifiers": {
                  "format": "array",
                  "items": {
                    "format": "object",
                    "properties": {
                      "affiliationNameIdentifier": {
                        "format": "text",
                        "title": "所属機関識別子",
                        "title_i18n": {
                          "en": "Affiliation Name Identifier",
                          "ja": "所属機関識別子"
                        },
                        "type": "string"
                      },
                      "affiliationNameIdentifierScheme": {
                        "currentEnum": [
                          "kakenhi",
                          "ISNI",
                          "Ringgold",
                          "GRID"
                        ],
                        "enum": [
                          null,
                          "kakenhi",
                          "ISNI",
                          "Ringgold",
                          "GRID"
                        ],
                        "format": "select",
                        "title": "所属機関識別子スキーマ",
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "affiliationNameIdentifierURI": {
                        "format": "text",
                        "title": "所属機関識別子URI",
                        "title_i18n": {
                          "en": "Affiliation Name Identifier URI",
                          "ja": "所属機関識別子URI"
                        },
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "title": "所属機関識別子",
                  "type": "array"
                },
                "affiliationNames": {
                  "format": "array",
                  "items": {
                    "format": "object",
                    "properties": {
                      "affiliationName": {
                        "format": "text",
                        "title": "所属機関名",
                        "title_i18n": {
                          "en": "Affiliation Name",
                          "ja": "所属機関名"
                        },
                        "type": "string"
                      },
                      "affiliationNameLang": {
                        "currentEnum": [
                          "ja",
                          "ja-Kana",
                          "ja-Latn",
                          "en",
                          "fr",
                          "it",
                          "de",
                          "es",
                          "zh-cn",
                          "zh-tw",
                          "ru",
                          "la",
                          "ms",
                          "eo",
                          "ar",
                          "el",
                          "ko"
                        ],
                        "enum": [
                          null,
                          "ja",
                          "ja-Kana",
                          "ja-Latn",
                          "en",
                          "fr",
                          "it",
                          "de",
                          "es",
                          "zh-cn",
                          "zh-tw",
                          "ru",
                          "la",
                          "ms",
                          "eo",
                          "ar",
                          "el",
                          "ko"
                        ],
                        "format": "select",
                        "title": "言語",
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": "object"
                  },
                  "title": "所属機関名",
                  "type": "array"
                }
              },
              "type": "object"
            },
            "title": "作成者所属",
            "type": "array"
          },
          "creatorAlternatives": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "creatorAlternative": {
                  "format": "text",
                  "title": "別名",
                  "title_i18n": {
                    "en": "Alternative Name",
                    "ja": "別名"
                  },
                  "type": "string"
                },
                "creatorAlternativeLang": {
                  "currentEnum": [
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "enum": [
                    null,
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "format": "select",
                  "title": "言語",
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "作成者別名",
            "type": "array"
          },
          "creatorMails": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "creatorMail": {
                  "format": "text",
                  "title": "メールアドレス",
                  "title_i18n": {
                    "en": "Email Address",
                    "ja": "メールアドレス"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "作成者メールアドレス",
            "type": "array"
          },
          "creatorNames": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "creatorName": {
                  "format": "text",
                  "title": "姓名",
                  "title_i18n": {
                    "en": "Name",
                    "ja": "姓名"
                  },
                  "type": "string"
                },
                "creatorNameLang": {
                  "currentEnum": [
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "enum": [
                    null,
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "format": "select",
                  "title": "言語",
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "作成者姓名",
            "type": "array"
          },
          "familyNames": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "familyName": {
                  "format": "text",
                  "title": "姓",
                  "title_i18n": {
                    "en": "Family Name",
                    "ja": "姓"
                  },
                  "type": "string"
                },
                "familyNameLang": {
                  "currentEnum": [
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "enum": [
                    null,
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "format": "select",
                  "title": "言語",
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "作成者姓",
            "type": "array"
          },
          "givenNames": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "givenName": {
                  "format": "text",
                  "title": "名",
                  "title_i18n": {
                    "en": "Given Name",
                    "ja": "名"
                  },
                  "type": "string"
                },
                "givenNameLang": {
                  "currentEnum": [
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "enum": [
                    null,
                    "ja",
                    "ja-Kana",
                    "ja-Latn",
                    "en",
                    "fr",
                    "it",
                    "de",
                    "es",
                    "zh-cn",
                    "zh-tw",
                    "ru",
                    "la",
                    "ms",
                    "eo",
                    "ar",
                    "el",
                    "ko"
                  ],
                  "format": "select",
                  "title": "言語",
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "作成者名",
            "type": "array"
          },
          "iscreator": {
            "format": "text",
            "title": "iscreator",
            "title_i18n": {
              "en": "",
              "ja": ""
            },
            "type": "string"
          },
          "nameIdentifiers": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "nameIdentifier": {
                  "format": "text",
                  "title": "作成者識別子",
                  "title_i18n": {
                    "en": "Creator Identifier",
                    "ja": "作成者識別子"
                  },
                  "type": "string"
                },
                "nameIdentifierScheme": {
                  "currentEnum": [],
                  "format": "select",
                  "title": "作成者識別子Scheme",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "nameIdentifierURI": {
                  "format": "text",
                  "title": "作成者識別子URI",
                  "title_i18n": {
                    "en": "Creator Identifier URI",
                    "ja": "作成者識別子URI"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "作成者識別子",
            "type": "array"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Creator",
      "type": "array"
    },
    "item_1617258105262": {
      "properties": {
        "resourcetype": {
          "currentEnum": [
            "conference paper",
            "data paper",
            "departmental bulletin paper",
            "editorial",
            "journal article",
            "newspaper",
            "periodical",
            "review article",
            "software paper",
            "article",
            "book",
            "book part",
            "cartographic material",
            "map",
            "conference object",
            "conference proceedings",
            "conference poster",
            "aggregated data",
            "clinical trial data",
            "compiled data",
            "encoded data",
            "experimental data",
            "genomic data",
            "geospatial data",
            "laboratory notebook",
            "measurement and test data",
            "observational data",
            "recorded data",
            "simulation data",
            "survey data",
            "dataset",
            "interview",
            "image",
            "still image",
            "moving image",
            "video",
            "lecture",
            "patent",
            "internal report",
            "report",
            "research report",
            "technical report",
            "policy report",
            "report part",
            "working paper",
            "data management plan",
            "sound",
            "thesis",
            "bachelor thesis",
            "master thesis",
            "doctoral thesis",
            "interactive resource",
            "learning object",
            "manuscript",
            "musical notation",
            "research proposal",
            "software",
            "technical documentation",
            "workflow",
            "other"
          ],
          "enum": [
            null,
            "conference paper",
            "data paper",
            "departmental bulletin paper",
            "editorial",
            "journal article",
            "newspaper",
            "periodical",
            "review article",
            "software paper",
            "article",
            "book",
            "book part",
            "cartographic material",
            "map",
            "conference object",
            "conference proceedings",
            "conference poster",
            "aggregated data",
            "clinical trial data",
            "compiled data",
            "encoded data",
            "experimental data",
            "genomic data",
            "geospatial data",
            "laboratory notebook",
            "measurement and test data",
            "observational data",
            "recorded data",
            "simulation data",
            "survey data",
            "dataset",
            "interview",
            "image",
            "still image",
            "moving image",
            "video",
            "lecture",
            "patent",
            "internal report",
            "report",
            "research report",
            "technical report",
            "policy report",
            "report part",
            "working paper",
            "data management plan",
            "sound",
            "thesis",
            "bachelor thesis",
            "master thesis",
            "doctoral thesis",
            "interactive resource",
            "learning object",
            "manuscript",
            "musical notation",
            "research proposal",
            "software",
            "technical documentation",
            "workflow",
            "other"
          ],
          "format": "select",
          "title": "資源タイプ",
          "type": [
            "null",
            "string"
          ]
        },
        "resourceuri": {
          "format": "text",
          "title": "資源タイプ識別子",
          "title_i18n": {
            "en": "Resource Type Identifier",
            "ja": "資源タイプ識別子"
          },
          "type": "string"
        }
      },
      "required": [
        "resourcetype",
        "resourceuri"
      ],
      "title": "Resource Type",
      "type": "object"
    },
    "item_1617605131499": {
      "items": {
        "properties": {
          "accessrole": {
            "enum": [
              "open_access",
              "open_date",
              "open_login",
              "open_no"
            ],
            "format": "radios",
            "title": "アクセス",
            "type": [
              "null",
              "string"
            ]
          },
          "date": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "dateType": {
                  "currentEnum": [],
                  "format": "select",
                  "title": "日付タイプ",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "dateValue": {
                  "format": "datetime",
                  "title": "日付",
                  "title_i18n": {
                    "en": "",
                    "ja": ""
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "オープンアクセスの日付",
            "type": "array"
          },
          "displaytype": {
            "currentEnum": [
              "detail",
              "simple",
              "preview"
            ],
            "enum": [
              null,
              "detail",
              "simple",
              "preview"
            ],
            "format": "select",
            "title": "表示形式",
            "type": [
              "null",
              "string"
            ]
          },
          "fileDate": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "fileDateType": {
                  "currentEnum": [
                    "Accepted",
                    "Collected",
                    "Copyrighted",
                    "Created",
                    "Issued",
                    "Submitted",
                    "Updated",
                    "Valid"
                  ],
                  "enum": [
                    null,
                    "Accepted",
                    "Collected",
                    "Copyrighted",
                    "Created",
                    "Issued",
                    "Submitted",
                    "Updated",
                    "Valid"
                  ],
                  "format": "select",
                  "title": "日付タイプ",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "fileDateValue": {
                  "format": "datetime",
                  "title": "日付",
                  "title_i18n": {
                    "en": "Date",
                    "ja": "日付"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "日付",
            "type": "array"
          },
          "filename": {
            "format": "text",
            "title": "表示名",
            "title_i18n": {
              "en": "FileName",
              "ja": "表示名"
            },
            "type": "string"
          },
          "filesize": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "value": {
                  "format": "text",
                  "title": "サイズ",
                  "title_i18n": {
                    "en": "Size",
                    "ja": "サイズ"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "サイズ",
            "type": "array"
          },
          "format": {
            "format": "text",
            "title": "フォーマット",
            "title_i18n": {
              "en": "Format",
              "ja": "フォーマット"
            },
            "type": "string"
          },
          "groups": {
            "currentEnum": [],
            "format": "select",
            "title": "グループ",
            "type": [
              "null",
              "string"
            ]
          },
          "licensefree": {
            "format": "textarea",
            "title": "自由ライセンス",
            "title_i18n": {
              "en": "自由ライセンス",
              "ja": "自由ライセンス"
            },
            "type": "string"
          },
          "licensetype": {
            "currentEnum": [],
            "format": "select",
            "title": "ライセンス",
            "type": [
              "null",
              "string"
            ]
          },
          "url": {
            "format": "object",
            "properties": {
              "label": {
                "format": "text",
                "title": "ラベル",
                "title_i18n": {
                  "en": "Label",
                  "ja": "ラベル"
                },
                "type": "string"
              },
              "objectType": {
                "currentEnum": [
                  "abstract",
                  "summary",
                  "fulltext",
                  "thumbnail",
                  "other"
                ],
                "enum": [
                  null,
                  "abstract",
                  "summary",
                  "fulltext",
                  "thumbnail",
                  "other"
                ],
                "format": "select",
                "title": "オブジェクトタイプ",
                "type": [
                  "null",
                  "string"
                ]
              },
              "url": {
                "format": "text",
                "title": "本文URL",
                "title_i18n": {
                  "en": "Text URL",
                  "ja": "本文URL"
                },
                "type": "string"
              }
            },
            "title": "本文URL",
            "type": "object"
          },
          "version": {
            "format": "text",
            "title": "バージョン情報",
            "title_i18n": {
              "en": "Version Information",
              "ja": "バージョン情報"
            },
            "type": "string"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "File",
      "type": "array"
    },
    "pubdate": {
      "format": "datetime",
      "title": "PubDate",
      "type": "string"
    },
    "system_file": {
      "format": "object",
      "properties": {
        "subitem_systemfile_datetime": {
          "format": "array",
          "items": {
            "format": "object",
            "properties": {
              "subitem_systemfile_datetime_date": {
                "format": "datetime",
                "title": "SYSTEMFILE DateTime Date",
                "type": "string"
              },
              "subitem_systemfile_datetime_type": {
                "enum": [
                  "Accepted",
                  "Available",
                  "Collected",
                  "Copyrighted",
                  "Created",
                  "Issued",
                  "Submitted",
                  "Updated",
                  "Valid"
                ],
                "format": "select",
                "title": "SYSTEMFILE DateTime Type",
                "type": "string"
              }
            },
            "type": "object"
          },
          "title": "SYSTEMFILE DateTime",
          "type": "array"
        },
        "subitem_systemfile_filename": {
          "format": "array",
          "items": {
            "format": "object",
            "properties": {
              "subitem_systemfile_filename_label": {
                "format": "text",
                "title": "SYSTEMFILE Filename Label",
                "type": "string"
              },
              "subitem_systemfile_filename_type": {
                "enum": [
                  "Abstract",
                  "Fulltext",
                  "Summary",
                  "Thumbnail",
                  "Other"
                ],
                "format": "select",
                "title": "SYSTEMFILE Filename Type",
                "type": "string"
              },
              "subitem_systemfile_filename_uri": {
                "format": "text",
                "title": "SYSTEMFILE Filename URI",
                "type": "string"
              }
            },
            "type": "object"
          },
          "title": "SYSTEMFILE Filename",
          "type": "array"
        },
        "subitem_systemfile_mimetype": {
          "format": "text",
          "title": "SYSTEMFILE MimeType",
          "type": "string"
        },
        "subitem_systemfile_size": {
          "format": "text",
          "title": "SYSTEMFILE Size",
          "type": "string"
        },
        "subitem_systemfile_version": {
          "format": "text",
          "title": "SYSTEMFILE Version",
          "type": "string"
        }
      },
      "system_prop": true,
      "title": "File Information",
      "type": "object"
    },
    "system_identifier_doi": {
      "format": "object",
      "properties": {
        "subitem_systemidt_identifier": {
          "format": "text",
          "title": "SYSTEMIDT Identifier",
          "type": "string"
        },
        "subitem_systemidt_identifier_type": {
          "enum": [
            "DOI",
            "HDL",
            "URI"
          ],
          "format": "select",
          "title": "SYSTEMIDT Identifier Type",
          "type": "string"
        }
      },
      "system_prop": true,
      "title": "Persistent Identifier(DOI)",
      "type": "object"
    },
    "system_identifier_hdl": {
      "format": "object",
      "properties": {
        "subitem_systemidt_identifier": {
          "format": "text",
          "title": "SYSTEMIDT Identifier",
          "type": "string"
        },
        "subitem_systemidt_identifier_type": {
          "enum": [
            "DOI",
            "HDL",
            "URI"
          ],
          "format": "select",
          "title": "SYSTEMIDT Identifier Type",
          "type": "string"
        }
      },
      "system_prop": true,
      "title": "Persistent Identifier(HDL)",
      "type": "object"
    },
    "system_identifier_uri": {
      "format": "object",
      "properties": {
        "subitem_systemidt_identifier": {
          "format": "text",
          "title": "SYSTEMIDT Identifier",
          "type": "string"
        },
        "subitem_systemidt_identifier_type": {
          "enum": [
            "DOI",
            "HDL",
            "URI"
          ],
          "format": "select",
          "title": "SYSTEMIDT Identifier Type",
          "type": "string"
        }
      },
      "system_prop": true,
      "title": "Persistent Identifier(URI)",
      "type": "object"
    }
  },
  "required": [
    "pubdate",
    "item_1617186331708",
    "item_1617258105262"
  ],
  "type": "object"
}
```

  - 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 |  |  |  |  |  |  |

  - 機能内容

  - 関連モジュール

  - 関連モジュール

- weko-items-ui（ハンドラ `views.get_json_schema`、Blueprint `weko_items_ui`（`url_prefix='/items'`））
- weko-records（`ItemTypes.get_by_id(item_type_id).schema`＝`ItemType.schema` カラム）
- weko-accounts（`utils.login_required_customize`）

  - 処理概要

1. エンドポイント `GET /items/jsonschema/<int:item_type_id>`（ハンドラ `weko_items_ui.views.get_json_schema`）。権限は `@login_required_customize`（ログイン必須。専用のロールチェックやOAuthスコープは無い。専用のconfig/REST定義も無く通常のFlask blueprintルート）。
2. `ItemTypes.get_by_id(item_type_id)` でアイテムタイプを取得し、その `schema` を JSON で返す。取得失敗時は `abort(400)`、該当なしは `'{}'`。
3. `filemeta` を含む場合はグループ一覧で `enum` を差し替え、`activity_id` 付き（`/jsonschema/<id>/<activity_id>`）ならアクティビティ別スキーマで上書き、除外項目・著者テーブルを反映して返す。

  - 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/11/14 | V0.9.27 | 初版作成 |
| 2024/07/1 | 7733de131da9ad59ab591b2df1c70ddefcfcad98 | v1.0.7対応 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。目的・用途とパラメータ説明の誤り（インデックス検索→アイテムタイプのJSON Schema取得）を修正、レスポンス例パス修正、関連モジュール・ハンドラ・権限・処理概要を追記 |
