# Schema

## 目的・用途

他のウェブアプリがweko3のリソースにアクセスできるようAPI利用を承認することを目的としている。

## 利用方法

API-8-5の機能を用いて、OAuthアプリケーション、またはトークンを登録する。その後、設定された値を利用してAPI接続の設定を行う。

## 機能内容

/items/jsonschema/{item type id}

## 関連モジュール

<!-- end list -->

  - > Invenio\_oaiserver

<!-- end list -->


##

| # | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
|   | { |   |   |   |   |   |
|   | "$schema": "http://json-schema.org/draft-04/schema#", |   |   |   |   |   |
|   | "description": "", |   |   |   |   |   |
|   | "properties": { |   |   |   |   |   |
|   | , |   |   |   |   |   |
|   | "required": [|   |   |   |   |   |
|   | "pubdate",|   |   |   |   |   |
|   | "item_1617186331708",|   |   |   |   |   |
|   | "item_1617258105262"|   |   |   |   |   |
|   | ],|   |   |   |   |   |
|   | "type": "object"|   |   |   |   |   |
|   | } |   |   |   |   |   |


UPDATE item_type SET schema=jsonb_set(schema,'{properties,item_1727013688876}','{"type": "object", "format": "object",
 "properties": {"subitem_select_item": {"items": {"enum": [null,"a","b","c"], "type": ["null","string"], "title": "値", "format"
: "select", "editAble": true}}, "subitem_select_language": {"enum": [null, "ja", "ja-Kana", "ja-Latn", "en", "fr", "it", "de", "
es", "zh-cn", "zh-tw", "ru", "la", "ms", "eo", "ar", "el", "ko"], "type": ["null", "string"], "title": "言語", "format": "select
", "editAble": true}}}') WHERE id=16;


```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "",
  "properties": {
    "item_1617186331708": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_title": {
            "format": "text",
            "title": "タイトル",
            "title_i18n": {
              "en": "Title",
              "ja": "タイトル"
            },
            "type": "string"
          },
          "subitem_title_language": {
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
            "editAble": true,
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": [
              "null",
              "string"
            ]
          }
        },
        "required": [
          "subitem_title",
          "subitem_title_language"
        ],
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Title",
      "type": "array"
    },
    "item_1617186385884": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_alternative_title": {
            "format": "text",
            "title": "その他のタイトル",
            "title_i18n": {
              "en": "Alternative Title",
              "ja": "その他のタイトル"
            },
            "type": "string"
          },
          "subitem_alternative_title_language": {
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
            "editAble": true,
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Alternative Title",
      "type": "array"
    },
    "item_1617186419668": {
      "items": {
        "format": "object",
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
                        "enum": [null, "kakenhi",
                          "ISNI",
                          "Ringgold",
                          "GRID"
                        ],
                        "format": "select",
                        "title": "所属機関識別子Scheme",
                        "title_i18n": {
                          "en": "Affiliation Name Identifier Scheme",
                          "ja": "所属機関識別子Scheme"
                        },
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
                        "editAble": true,
                        "enum": [null, "ja",
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
                        "title_i18n": {
                          "en": "Language",
                          "ja": "言語"
                        },
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
                  "editAble": true,
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
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
                  "editAble": true,
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "creatorNameType": {
                  "currentEnum": [
                    "Personal",
                    "Organizational"
                  ],
                  "enum": [null, "Personal",
                    "Organizational"
                  ],
                  "format": "select",
                  "title": "名前タイプ",
                  "title_i18n": {
                    "en": "Name Type",
                    "ja": "名前タイプ"
                  },
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
          "creatorType": {
            "format": "text",
            "title": "作成者タイプ",
            "title_i18n": {
              "en": "Creator Type",
              "ja": "作成者タイプ"
            },
            "type": "string"
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
                  "editAble": true,
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
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
                  "editAble": true,
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
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
                    "en": "Creator Name Identifier",
                    "ja": "作成者識別子"
                  },
                  "type": "string"
                },
                "nameIdentifierScheme": {
                  "currentEnum": [],
                  "format": "select",
                  "title": "作成者識別子Scheme",
                  "title_i18n": {
                    "en": "IdentifierScheme",
                    "ja": "作成者識別子Scheme"
                  },
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "nameIdentifierURI": {
                  "format": "text",
                  "title": "作成者識別子URI",
                  "title_i18n": {
                    "en": "Creator Name Identifier URI",
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
        "system_prop": true,
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Creator",
      "type": "array"
    },
    "item_1617186476635": {
      "format": "object",
      "properties": {
        "subitem_access_right": {
          "currentEnum": [
            "embargoed access",
            "metadata only access",
            "open access",
            "restricted access"
          ],
          "enum": [null, "embargoed access",
            "metadata only access",
            "open access",
            "restricted access"
          ],
          "format": "select",
          "title": "アクセス権",
          "title_i18n": {
            "en": "Access Rights",
            "ja": "アクセス権"
          },
          "type": [
            "null",
            "string"
          ]
        },
        "subitem_access_right_uri": {
          "format": "text",
          "title": "アクセス権URI",
          "title_i18n": {
            "en": "Access Rights URI",
            "ja": "アクセス権URI"
          },
          "type": "string"
        }
      },
      "system_prop": true,
      "title": "アクセス権",
      "type": "object"
    },
    "item_1617186499011": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_rights": {
            "format": "text",
            "title": "権利情報",
            "type": "string"
          },
          "subitem_rights_language": {
            "editAble": true,
            "enum": [null, "ja",
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
          },
          "subitem_rights_resource": {
            "format": "text",
            "title": "権利情報Resource",
            "type": "string"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Rights",
      "type": "array"
    },
    "item_1617186609386": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_subject": {
            "format": "text",
            "title": "主題",
            "title_i18n": {
              "en": "Subject",
              "ja": "主題"
            },
            "type": "string"
          },
          "subitem_subject_language": {
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
            "editAble": true,
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": [
              "null",
              "string"
            ]
          },
          "subitem_subject_scheme": {
            "currentEnum": [
              "BSH",
              "DDC",
              "e-Rad_field",
              "JEL",
              "LCC",
              "LCSH",
              "MeSH",
              "NDC",
              "NDLC",
              "NDLSH",
              "SciVal",
              "UDC",
              "Other"
            ],
            "enum": [null, "BSH",
              "DDC",
              "e-Rad_field",
              "JEL",
              "LCC",
              "LCSH",
              "MeSH",
              "NDC",
              "NDLC",
              "NDLSH",
              "SciVal",
              "UDC",
              "Other"
            ],
            "format": "select",
            "title": "主題Scheme",
            "title_i18n": {
              "en": "Subject Scheme",
              "ja": "主題Scheme"
            },
            "type": [
              "null",
              "string"
            ]
          },
          "subitem_subject_uri": {
            "format": "text",
            "title": "主題URI",
            "title_i18n": {
              "en": "Subject URI",
              "ja": "主題URI"
            },
            "type": "string"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Subject",
      "type": "array"
    },
    "item_1617186626617": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_description": {
            "format": "textarea",
            "title": "内容記述",
            "type": "string"
          },
          "subitem_description_language": {
            "editAble": true,
            "enum": [null, "ja",
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
          },
          "subitem_description_type": {
            "enum": [null, "Abstract",
              "Methods",
              "TableOfContents",
              "TechnicalInfo",
              "Other"
            ],
            "format": "select",
            "title": "内容記述タイプ",
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Description",
      "type": "array"
    },
    "item_1617186643794": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_publisher": {
            "format": "text",
            "title": "出版者",
            "title_i18n": {
              "en": "Publisher",
              "ja": "出版者"
            },
            "type": "string"
          },
          "subitem_publisher_language": {
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
            "editAble": true,
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Publisher",
      "type": "array"
    },
    "item_1617186660861": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_date_issued_datetime": {
            "format": "datetime",
            "title": "日付",
            "type": "string"
          },
          "subitem_date_issued_type": {
            "currentEnum": [null, "Accepted",
              "Available",
              "Collected",
              "Copyrighted",
              "Created",
              "Issued",
              "Submitted",
              "Updated",
              "Valid"
            ],
            "enum": [null, "Accepted",
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
            "title": "日付タイプ",
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Date",
      "type": "array"
    },
    "item_1617186702042": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_language": {
            "editAble": true,
            "enum": [null, "jpn",
              "eng",
              "aar",
              "abk",
              "afr",
              "aka",
              "amh",
              "ara",
              "arg",
              "asm",
              "ava",
              "ave",
              "aym",
              "aze",
              "bak",
              "bam",
              "bel",
              "ben",
              "bis",
              "bod",
              "bos",
              "bre",
              "bul",
              "cat",
              "ces",
              "cha",
              "che",
              "chu",
              "chv",
              "cor",
              "cos",
              "cre",
              "cym",
              "dan",
              "deu",
              "div",
              "dzo",
              "ell",
              "epo",
              "est",
              "eus",
              "ewe",
              "fao",
              "fas",
              "fij",
              "fin",
              "fra",
              "fry",
              "ful",
              "gla",
              "gle",
              "glg",
              "glv",
              "grn",
              "guj",
              "hat",
              "hau",
              "heb",
              "her",
              "hin",
              "hmo",
              "hrv",
              "hun",
              "hye",
              "ibo",
              "ido",
              "iii",
              "iku",
              "ile",
              "ina",
              "ind",
              "ipk",
              "isl",
              "ita",
              "jav",
              "kal",
              "kan",
              "kas",
              "kat",
              "kau",
              "kaz",
              "khm",
              "kik",
              "kin",
              "kir",
              "kom",
              "kon",
              "kor",
              "kua",
              "kur",
              "lao",
              "lat",
              "lav",
              "lim",
              "lin",
              "lit",
              "ltz",
              "lub",
              "lug",
              "mah",
              "mal",
              "mar",
              "mkd",
              "mlg",
              "mlt",
              "mon",
              "mri",
              "msa",
              "mya",
              "nau",
              "nav",
              "nbl",
              "nde",
              "ndo",
              "nep",
              "nld",
              "nno",
              "nob",
              "nor",
              "nya",
              "oci",
              "oji",
              "ori",
              "orm",
              "oss",
              "pan",
              "pli",
              "pol",
              "por",
              "pus",
              "que",
              "roh",
              "ron",
              "run",
              "rus",
              "sag",
              "san",
              "sin",
              "slk",
              "slv",
              "sme",
              "smo",
              "sna",
              "snd",
              "som",
              "sot",
              "spa",
              "sqi",
              "srd",
              "srp",
              "ssw",
              "sun",
              "swa",
              "swe",
              "tah",
              "tam",
              "tat",
              "tel",
              "tgk",
              "tgl",
              "tha",
              "tir",
              "ton",
              "tsn",
              "tso",
              "tuk",
              "tur",
              "twi",
              "uig",
              "ukr",
              "urd",
              "uzb",
              "ven",
              "vie",
              "vol",
              "wln",
              "wol",
              "xho",
              "yid",
              "yor",
              "zha",
              "zho",
              "zul"
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
      "maxItems": 9999,
      "minItems": 1,
      "title": "Language",
      "type": "array"
    },
    "item_1617186783814": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_identifier_type": {
            "enum": [null, "DOI",
              "HDL",
              "URI"
            ],
            "format": "select",
            "title": "識別子タイプ",
            "type": [
              "null",
              "string"
            ]
          },
          "subitem_identifier_uri": {
            "format": "text",
            "title": "識別子",
            "type": "string"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Identifier",
      "type": "array"
    },
    "item_1617186819068": {
      "format": "object",
      "properties": {
        "subitem_identifier_reg_text": {
          "format": "text",
          "title": "ID登録",
          "title_i18n": {
            "en": "Identifier Registration",
            "ja": "ID登録"
          },
          "type": "string"
        },
        "subitem_identifier_reg_type": {
          "currentEnum": [
            "JaLC",
            "Crossref",
            "DataCite",
            "PMID【現在不使用】"
          ],
          "enum": [null, "JaLC",
            "Crossref",
            "DataCite",
            "PMID【現在不使用】"
          ],
          "format": "select",
          "title": "ID登録タイプ",
          "title_i18n": {
            "en": "Identifier Registration Type",
            "ja": "ID登録タイプ"
          },
          "type": [
            "null",
            "string"
          ]
        }
      },
      "title": "identifier_registration",
      "type": "object"
    },
    "item_1617186859717": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_temporal_language": {
            "editAble": true,
            "enum": [null, "ja",
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
          },
          "subitem_temporal_text": {
            "format": "text",
            "title": "時間的範囲",
            "type": "string"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Temporal",
      "type": "array"
    },
    "item_1617186882738": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_geolocation_box": {
            "format": "object",
            "properties": {
              "subitem_east_longitude": {
                "format": "text",
                "title": "東部経度",
                "type": "string"
              },
              "subitem_north_latitude": {
                "format": "text",
                "title": "北部緯度",
                "type": "string"
              },
              "subitem_south_latitude": {
                "format": "text",
                "title": "南部緯度",
                "type": "string"
              },
              "subitem_west_longitude": {
                "format": "text",
                "title": "西部経度",
                "type": "string"
              }
            },
            "title": "位置情報（空間）",
            "type": "object"
          },
          "subitem_geolocation_place": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_geolocation_place_text": {
                  "format": "text",
                  "title": "位置情報（自由記述）",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "位置情報（自由記述）",
            "type": "array"
          },
          "subitem_geolocation_point": {
            "format": "object",
            "properties": {
              "subitem_point_latitude": {
                "format": "text",
                "title": "緯度",
                "type": "string"
              },
              "subitem_point_longitude": {
                "format": "text",
                "title": "経度",
                "type": "string"
              }
            },
            "title": "位置情報（点）",
            "type": "object"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Geo Location",
      "type": "array"
    },
    "item_1617186901218": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_award_numbers": {
            "format": "object",
            "properties": {
              "subitem_award_number": {
                "format": "text",
                "title": "研究課題番号",
                "type": "string"
              },
              "subitem_award_number_type": {
                "enum": [null, "JGN"
                ],
                "format": "select",
                "title": "研究課題番号タイプ",
                "type": [
                  "null",
                  "string"
                ]
              },
              "subitem_award_uri": {
                "format": "text",
                "title": "研究課題番号URI",
                "type": "string"
              }
            },
            "title": "研究課題番号",
            "type": "object"
          },
          "subitem_award_titles": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_award_title": {
                  "format": "text",
                  "title": "研究課題名",
                  "type": "string"
                },
                "subitem_award_title_language": {
                  "enum": [null, "ja",
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
            "title": "研究課題名",
            "type": "array"
          },
          "subitem_funder_identifiers": {
            "format": "object",
            "properties": {
              "subitem_funder_identifier": {
                "format": "text",
                "title": "助成機関識別子",
                "type": "string"
              },
              "subitem_funder_identifier_type": {
                "enum": [null, "Crossref Funder",
                  "e-Rad_funder",
                  "GRID",
                  "ISNI",
                  "ROR",
                  "Other"
                ],
                "format": "select",
                "title": "識別子タイプ",
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "title": "助成機関識別子",
            "type": "object"
          },
          "subitem_funder_names": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_funder_name": {
                  "format": "text",
                  "title": "助成機関名",
                  "type": "string"
                },
                "subitem_funder_name_language": {
                  "enum": [null, "ja",
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
            "title": "助成機関名",
            "type": "array"
          },
          "subitem_funding_stream_identifiers": {
            "format": "object",
            "properties": {
              "subitem_funding_stream_identifier": {
                "format": "text",
                "title": "プログラム情報識別子",
                "type": "string"
              },
              "subitem_funding_stream_identifier_type": {
                "enum": [
                  "Crossref Funder",
                  "JGN_fundingStream"
                ],
                "format": "select",
                "title": "プログラム情報識別子タイプ",
                "type": [
                  "null",
                  "string"
                ]
              },
              "subitem_funding_stream_identifier_type_uri": {
                "format": "text",
                "title": "プログラム情報識別子タイプURI",
                "type": "string"
              }
            },
            "title": "プログラム情報識別子",
            "type": "object"
          },
          "subitem_funding_streams": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_funding_stream": {
                  "format": "text",
                  "title": "プログラム情報",
                  "type": "string"
                },
                "subitem_funding_stream_language": {
                  "enum": [null, "ja",
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
            "title": "プログラム情報",
            "type": "array"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Funding Reference",
      "type": "array"
    },
    "item_1617186920753": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_source_identifier": {
            "format": "text",
            "title": "収録物識別子",
            "type": "string"
          },
          "subitem_source_identifier_type": {
            "enum": [null, "PISSN",
              "EISSN",
              "ISSN",
              "NCID"
            ],
            "format": "select",
            "title": "収録物識別子タイプ",
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Source Identifier",
      "type": "array"
    },
    "item_1617186941041": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_source_title": {
            "format": "text",
            "title": "収録物名",
            "type": "string"
          },
          "subitem_source_title_language": {
            "editAble": true,
            "enum": [null, "ja",
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
      "maxItems": 9999,
      "minItems": 1,
      "title": "Source Title",
      "type": "array"
    },
    "item_1617186959569": {
      "format": "object",
      "properties": {
        "subitem_volume": {
          "format": "text",
          "title": "巻",
          "title_i18n": {
            "en": "Volume",
            "ja": "巻"
          },
          "type": "string"
        }
      },
      "title": "巻",
      "type": "object"
    },
    "item_1617186981471": {
      "format": "object",
      "properties": {
        "subitem_issue": {
          "format": "text",
          "title": "号",
          "title_i18n": {
            "en": "Issue",
            "ja": "号"
          },
          "type": "string"
        }
      },
      "title": "号",
      "type": "object"
    },
    "item_1617186994930": {
      "format": "object",
      "properties": {
        "subitem_number_of_pages": {
          "format": "text",
          "title": "ページ数",
          "title_i18n": {
            "en": "Number of Pages",
            "ja": "ページ数"
          },
          "type": "string"
        }
      },
      "title": "ページ数",
      "type": "object"
    },
    "item_1617187024783": {
      "format": "object",
      "properties": {
        "subitem_start_page": {
          "format": "text",
          "title": "開始ページ",
          "title_i18n": {
            "en": "Start Page",
            "ja": "開始ページ"
          },
          "type": "string"
        }
      },
      "title": "開始ページ",
      "type": "object"
    },
    "item_1617187045071": {
      "format": "object",
      "properties": {
        "subitem_end_page": {
          "format": "text",
          "title": "終了ページ",
          "title_i18n": {
            "en": "End Page",
            "ja": "終了ページ"
          },
          "type": "string"
        }
      },
      "title": "終了ページ",
      "type": "object"
    },
    "item_1617187056579": {
      "format": "object",
      "properties": {
        "bibliographicIssueDates": {
          "format": "object",
          "properties": {
            "bibliographicIssueDate": {
              "format": "datetime",
              "title": "日付",
              "type": "string"
            },
            "bibliographicIssueDateType": {
              "currentEnum": [null, "",
                "Issued"
              ],
              "enum": [null, "",
                "Issued"
              ],
              "format": "select",
              "title": "日付タイプ",
              "type": [
                "null",
                "string"
              ]
            }
          },
          "title": "発行日",
          "type": "object"
        },
        "bibliographicIssueNumber": {
          "format": "text",
          "title": "号",
          "type": "string"
        },
        "bibliographicNumberOfPages": {
          "format": "text",
          "title": "ページ数",
          "type": "string"
        },
        "bibliographicPageEnd": {
          "format": "text",
          "title": "終了ページ",
          "type": "string"
        },
        "bibliographicPageStart": {
          "format": "text",
          "title": "開始ページ",
          "type": "string"
        },
        "bibliographicVolumeNumber": {
          "format": "text",
          "title": "巻",
          "type": "string"
        },
        "bibliographic_titles": {
          "format": "array",
          "items": {
            "format": "object",
            "properties": {
              "bibliographic_title": {
                "format": "text",
                "title": "タイトル",
                "type": "string"
              },
              "bibliographic_titleLang": {
                "editAble": true,
                "enum": [null, "ja",
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
          "title": "雑誌名",
          "type": "array"
        }
      },
      "system_prop": true,
      "title": "bibliographic_information",
      "type": "object"
    },
    "item_1617187087799": {
      "format": "object",
      "properties": {
        "subitem_dissertationnumber": {
          "format": "text",
          "title": "学位授与番号",
          "title_i18n": {
            "en": "Dissertation Number",
            "ja": "学位授与番号"
          },
          "type": "string"
        }
      },
      "title": "dissertation_number",
      "type": "object"
    },
    "item_1617187112279": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_degreename": {
            "format": "text",
            "title": "学位名",
            "type": "string"
          },
          "subitem_degreename_language": {
            "editAble": true,
            "enum": [null, "ja",
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
        "title": "学位名",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Degree Name",
      "type": "array"
    },
    "item_1617187136212": {
      "format": "object",
      "properties": {
        "subitem_dategranted": {
          "format": "datetime",
          "title": "学位授与年月日",
          "title_i18n": {
            "en": "Date Granted",
            "ja": "学位授与年月日"
          },
          "type": "string"
        }
      },
      "title": "学位授与年月日",
      "type": "object"
    },
    "item_1617187187528": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_conference_country": {
            "enum": [null, "JPN",
              "ABW",
              "AFG",
              "AGO",
              "AIA",
              "ALA",
              "ALB",
              "AND",
              "ARE",
              "ARG",
              "ARM",
              "ASM",
              "ATA",
              "ATF",
              "ATG",
              "AUS",
              "AUT",
              "AZE",
              "BDI",
              "BEL",
              "BEN",
              "BES",
              "BFA",
              "BGD",
              "BGR",
              "BHR",
              "BHS",
              "BIH",
              "BLM",
              "BLR",
              "BLZ",
              "BMU",
              "BOL",
              "BRA",
              "BRB",
              "BRN",
              "BTN",
              "BVT",
              "BWA",
              "CAF",
              "CAN",
              "CCK",
              "CHE",
              "CHL",
              "CHN",
              "CIV",
              "CMR",
              "COD",
              "COG",
              "COK",
              "COL",
              "COM",
              "CPV",
              "CRI",
              "CUB",
              "CUW",
              "CXR",
              "CYM",
              "CYP",
              "CZE",
              "DEU",
              "DJI",
              "DMA",
              "DNK",
              "DOM",
              "DZA",
              "ECU",
              "EGY",
              "ERI",
              "ESH",
              "ESP",
              "EST",
              "ETH",
              "FIN",
              "FJI",
              "FLK",
              "FRA",
              "FRO",
              "FSM",
              "GAB",
              "GBR",
              "GEO",
              "GGY",
              "GHA",
              "GIB",
              "GIN",
              "GLP",
              "GMB",
              "GNB",
              "GNQ",
              "GRC",
              "GRD",
              "GRL",
              "GTM",
              "GUF",
              "GUM",
              "GUY",
              "HKG",
              "HMD",
              "HND",
              "HRV",
              "HTI",
              "HUN",
              "IDN",
              "IMN",
              "IND",
              "IOT",
              "IRL",
              "IRN",
              "IRQ",
              "ISL",
              "ISR",
              "ITA",
              "JAM",
              "JEY",
              "JOR",
              "KAZ",
              "KEN",
              "KGZ",
              "KHM",
              "KIR",
              "KNA",
              "KOR",
              "KWT",
              "LAO",
              "LBN",
              "LBR",
              "LBY",
              "LCA",
              "LIE",
              "LKA",
              "LSO",
              "LTU",
              "LUX",
              "LVA",
              "MAC",
              "MAF",
              "MAR",
              "MCO",
              "MDA",
              "MDG",
              "MDV",
              "MEX",
              "MHL",
              "MKD",
              "MLI",
              "MLT",
              "MMR",
              "MNE",
              "MNG",
              "MNP",
              "MOZ",
              "MRT",
              "MSR",
              "MTQ",
              "MUS",
              "MWI",
              "MYS",
              "MYT",
              "NAM",
              "NCL",
              "NER",
              "NFK",
              "NGA",
              "NIC",
              "NIU",
              "NLD",
              "NOR",
              "NPL",
              "NRU",
              "NZL",
              "OMN",
              "PAK",
              "PAN",
              "PCN",
              "PER",
              "PHL",
              "PLW",
              "PNG",
              "POL",
              "PRI",
              "PRK",
              "PRT",
              "PRY",
              "PSE",
              "PYF",
              "QAT",
              "REU",
              "ROU",
              "RUS",
              "RWA",
              "SAU",
              "SDN",
              "SEN",
              "SGP",
              "SGS",
              "SHN",
              "SJM",
              "SLB",
              "SLE",
              "SLV",
              "SMR",
              "SOM",
              "SPM",
              "SRB",
              "SSD",
              "STP",
              "SUR",
              "SVK",
              "SVN",
              "SWE",
              "SWZ",
              "SXM",
              "SYC",
              "SYR",
              "TCA",
              "TCD",
              "TGO",
              "THA",
              "TJK",
              "TKL",
              "TKM",
              "TLS",
              "TON",
              "TTO",
              "TUN",
              "TUR",
              "TUV",
              "TWN",
              "TZA",
              "UGA",
              "UKR",
              "UMI",
              "URY",
              "USA",
              "UZB",
              "VAT",
              "VCT",
              "VEN",
              "VGB",
              "VIR",
              "VNM",
              "VUT",
              "WLF",
              "WSM",
              "YEM",
              "ZAF",
              "ZMB",
              "ZWE"
            ],
            "format": "select",
            "title": "開催国",
            "type": [
              "null",
              "string"
            ]
          },
          "subitem_conference_date": {
            "format": "object",
            "properties": {
              "subitem_conference_date_language": {
                "enum": [null, "ja",
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
              },
              "subitem_conference_end_day": {
                "format": "text",
                "title": "終了日",
                "type": "string"
              },
              "subitem_conference_end_month": {
                "format": "text",
                "title": "終了月",
                "type": "string"
              },
              "subitem_conference_end_year": {
                "format": "text",
                "title": "終了年",
                "type": "string"
              },
              "subitem_conference_period": {
                "format": "text",
                "title": "開催期間",
                "type": "string"
              },
              "subitem_conference_start_day": {
                "format": "text",
                "title": "開始日",
                "type": "string"
              },
              "subitem_conference_start_month": {
                "format": "text",
                "title": "開始月",
                "type": "string"
              },
              "subitem_conference_start_year": {
                "format": "text",
                "title": "開始年",
                "type": "string"
              }
            },
            "title": "開催期間",
            "type": "object"
          },
          "subitem_conference_names": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_conference_name": {
                  "format": "text",
                  "title": "会議名",
                  "type": "string"
                },
                "subitem_conference_name_language": {
                  "enum": [null, "ja",
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
            "title": "会議名",
            "type": "array"
          },
          "subitem_conference_places": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_conference_place": {
                  "format": "text",
                  "title": "開催地",
                  "type": "string"
                },
                "subitem_conference_place_language": {
                  "enum": [null, "ja",
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
            "title": "開催地",
            "type": "array"
          },
          "subitem_conference_sequence": {
            "format": "text",
            "title": "回次",
            "type": "string"
          },
          "subitem_conference_sponsors": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_conference_sponsor": {
                  "format": "text",
                  "title": "主催機関",
                  "type": "string"
                },
                "subitem_conference_sponsor_language": {
                  "enum": [null, "ja",
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
            "title": "主催機関",
            "type": "array"
          },
          "subitem_conference_venues": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_conference_venue": {
                  "format": "text",
                  "title": "開催会場",
                  "type": "string"
                },
                "subitem_conference_venue_language": {
                  "enum": [null, "ja",
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
            "title": "開催会場",
            "type": "array"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Conference",
      "type": "array"
    },
    "item_1617258105262": {
      "format": "object",
      "properties": {
        "resourcetype": {
          "currentEnum": [
            "conference paper",
            "data paper",
            "departmental bulletin paper",
            "editorial",
            "journal",
            "journal article",
            "newspaper",
            "review article",
            "other periodical",
            "software paper",
            "article",
            "book",
            "book part",
            "cartographic material",
            "map",
            "conference output",
            "conference presentation",
            "conference proceedings",
            "conference poster",
            "aggregated data",
            "clinical trial data",
            "compiled data",
            "dataset",
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
            "image",
            "still image",
            "moving image",
            "video",
            "lecture",
            "design patent",
            "patent",
            "PCT application",
            "plant patent",
            "plant variety protection",
            "software patent",
            "trademark",
            "utility model",
            "report",
            "research report",
            "technical report",
            "policy report",
            "working paper",
            "data management plan",
            "sound",
            "thesis",
            "bachelor thesis",
            "master thesis",
            "doctoral thesis",
            "commentary",
            "design",
            "industrial design",
            "interactive resource",
            "layout design",
            "learning object",
            "manuscript",
            "musical notation",
            "peer review",
            "research proposal",
            "research protocol",
            "software",
            "source code",
            "technical documentation",
            "transcription",
            "workflow",
            "other"
          ],
          "enum": [null, "conference paper",
            "data paper",
            "departmental bulletin paper",
            "editorial",
            "journal",
            "journal article",
            "newspaper",
            "review article",
            "other periodical",
            "software paper",
            "article",
            "book",
            "book part",
            "cartographic material",
            "map",
            "conference output",
            "conference presentation",
            "conference proceedings",
            "conference poster",
            "aggregated data",
            "clinical trial data",
            "compiled data",
            "dataset",
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
            "image",
            "still image",
            "moving image",
            "video",
            "lecture",
            "design patent",
            "patent",
            "PCT application",
            "plant patent",
            "plant variety protection",
            "software patent",
            "trademark",
            "utility model",
            "report",
            "research report",
            "technical report",
            "policy report",
            "working paper",
            "data management plan",
            "sound",
            "thesis",
            "bachelor thesis",
            "master thesis",
            "doctoral thesis",
            "commentary",
            "design",
            "industrial design",
            "interactive resource",
            "layout design",
            "learning object",
            "manuscript",
            "musical notation",
            "peer review",
            "research proposal",
            "research protocol",
            "software",
            "source code",
            "technical documentation",
            "transcription",
            "workflow",
            "other"
          ],
          "format": "select",
          "title": "資源タイプ",
          "title_i18n": {
            "en": "Resource Type",
            "ja": "資源タイプ "
          },
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
        "resourceuri",
        "resourcetype"
      ],
      "system_prop": true,
      "type": "object"
    },
    "item_1617265215918": {
      "format": "object",
      "properties": {
        "subitem_version_resource": {
          "format": "text",
          "title": "出版タイプResource",
          "title_i18n": {
            "en": "Version Type Resource",
            "ja": "出版タイプResource"
          },
          "type": "string"
        },
        "subitem_version_type": {
          "currentEnum": [
            "AO",
            "SMUR",
            "AM",
            "P",
            "VoR",
            "CVoR",
            "EVoR",
            "NA"
          ],
          "enum": [null, "AO",
            "SMUR",
            "AM",
            "P",
            "VoR",
            "CVoR",
            "EVoR",
            "NA"
          ],
          "format": "select",
          "title": "出版タイプ",
          "title_i18n": {
            "en": "Version Type",
            "ja": "出版タイプ"
          },
          "type": [
            "null",
            "string"
          ]
        }
      },
      "system_prop": true,
      "title": "出版タイプ",
      "type": "object"
    },
    "item_1617349709064": {
      "items": {
        "format": "object",
        "properties": {
          "contributorAffiliations": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "contributorAffiliationNameIdentifiers": {
                  "format": "array",
                  "items": {
                    "format": "object",
                    "properties": {
                      "contributorAffiliationNameIdentifier": {
                        "format": "text",
                        "title": "所属機関識別子",
                        "type": "string"
                      },
                      "contributorAffiliationScheme": {
                        "enum": [null, "kakenhi",
                          "ISNI",
                          "Ringgold",
                          "GRID"
                        ],
                        "format": "select",
                        "title": "所属機関識別子Scheme",
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "contributorAffiliationURI": {
                        "format": "text",
                        "title": "所属機関識別子URI",
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "title": "所属機関識別子",
                  "type": "array"
                },
                "contributorAffiliationNames": {
                  "format": "array",
                  "items": {
                    "format": "object",
                    "properties": {
                      "contributorAffiliationName": {
                        "format": "text",
                        "title": "所属機関名",
                        "type": "string"
                      },
                      "contributorAffiliationNameLang": {
                        "editAble": true,
                        "enum": [null, "ja",
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
            "title": "寄与者所属",
            "type": "array"
          },
          "contributorAlternatives": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "contributorAlternative": {
                  "format": "text",
                  "title": "別名",
                  "type": "string"
                },
                "contributorAlternativeLang": {
                  "editAble": true,
                  "enum": [null, "ja",
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
            "title": "寄与者別名",
            "type": "array"
          },
          "contributorMails": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "contributorMail": {
                  "format": "text",
                  "title": "メールアドレス",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "寄与者メールアドレス",
            "type": "array"
          },
          "contributorNames": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "contributorName": {
                  "format": "text",
                  "title": "姓名",
                  "type": "string"
                },
                "lang": {
                  "editAble": true,
                  "enum": [null, "ja",
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
                },
                "nameType": {
                  "editAble": false,
                  "enum": [null, "Personal",
                    "Organizational"
                  ],
                  "format": "select",
                  "title": "名前タイプ",
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "寄与者姓名",
            "type": "array"
          },
          "contributorType": {
            "enum": [null, "ContactPerson",
              "DataCollector",
              "DataCurator",
              "DataManager",
              "Distributor",
              "Editor",
              "HostingInstitution",
              "Producer",
              "ProjectLeader",
              "ProjectManager",
              "ProjectMember",
              "RelatedPerson",
              "Researcher",
              "ResearchGroup",
              "Sponsor",
              "Supervisor",
              "WorkPackageLeader",
              "Other"
            ],
            "format": "select",
            "title": "寄与者タイプ",
            "type": [
              "null",
              "string"
            ]
          },
          "familyNames": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "familyName": {
                  "format": "text",
                  "title": "姓",
                  "type": "string"
                },
                "familyNameLang": {
                  "editAble": true,
                  "enum": [null, "ja",
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
            "title": "寄与者姓",
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
                  "type": "string"
                },
                "givenNameLang": {
                  "editAble": true,
                  "enum": [null, "ja",
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
            "title": "寄与者名",
            "type": "array"
          },
          "nameIdentifiers": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "nameIdentifier": {
                  "format": "text",
                  "title": "寄与者識別子",
                  "type": "string"
                },
                "nameIdentifierScheme": {
                  "format": "select",
                  "title": "寄与者識別子Scheme",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "nameIdentifierURI": {
                  "format": "text",
                  "title": "寄与者識別子URI",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "寄与者識別子",
            "type": "array"
          }
        },
        "system_prop": true,
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Contributor",
      "type": "array"
    },
    "item_1617349808926": {
      "format": "object",
      "properties": {
        "subitem_version": {
          "format": "text",
          "title": "バージョン情報",
          "title_i18n": {
            "en": "Version",
            "ja": "バージョン情報"
          },
          "type": "string"
        }
      },
      "title": "バージョン情報",
      "type": "object"
    },
    "item_1617351524846": {
      "format": "object",
      "properties": {
        "subitem_apc": {
          "currentEnum": [
            "Paid",
            "Partially waived",
            "Fully waived",
            "Not charged",
            "Not required",
            "Unknown"
          ],
          "enum": [null, "Paid",
            "Partially waived",
            "Fully waived",
            "Not charged",
            "Not required",
            "Unknown"
          ],
          "format": "select",
          "title": "APC",
          "title_i18n": {
            "en": "APC",
            "ja": "APC"
          },
          "type": [
            "null",
            "string"
          ]
        }
      },
      "title": "APC",
      "type": "object"
    },
    "item_1617353299429": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_relation_name": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_relation_name_language": {
                  "editAble": true,
                  "enum": [null, "ja",
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
                },
                "subitem_relation_name_text": {
                  "format": "text",
                  "title": "関連名称",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "関連名称",
            "type": "array"
          },
          "subitem_relation_type": {
            "currentEnum": [null, "isVersionOf",
              "hasVersion",
              "isPartOf",
              "hasPart",
              "isReferencedBy",
              "references",
              "isFormatOf",
              "hasFormat",
              "isReplacedBy",
              "replaces",
              "isRequiredBy",
              "requires",
              "isSupplementedBy",
              "isSupplementTo",
              "isIdenticalTo",
              "isDerivedFrom",
              "isSourceOf",
              "isCitedBy",
              "Cites",
              "inSeries"
            ],
            "enum": [null, "isVersionOf",
              "hasVersion",
              "isPartOf",
              "hasPart",
              "isReferencedBy",
              "references",
              "isFormatOf",
              "hasFormat",
              "isReplacedBy",
              "replaces",
              "isRequiredBy",
              "requires",
              "isSupplementedBy",
              "isSupplementTo",
              "isIdenticalTo",
              "isDerivedFrom",
              "isSourceOf",
              "isCitedBy",
              "Cites",
              "inSeries"
            ],
            "format": "select",
            "title": "関連タイプ",
            "type": [
              "null",
              "string"
            ]
          },
          "subitem_relation_type_id": {
            "format": "object",
            "properties": {
              "subitem_relation_type_id_text": {
                "format": "text",
                "title": "関連識別子",
                "type": "string"
              },
              "subitem_relation_type_select": {
                "currentEnum": [null, "ARK",
                  "arXiv",
                  "DOI",
                  "HDL",
                  "ICHUSHI",
                  "ISBN",
                  "J-GLOBAL",
                  "Local",
                  "PISSN",
                  "EISSN",
                  "ISSN",
                  "NAID",
                  "NCID",
                  "PMID",
                  "PURL",
                  "SCOPUS",
                  "URI",
                  "WOS",
                  "CRID"
                ],
                "enum": [null, "ARK",
                  "arXiv",
                  "DOI",
                  "HDL",
                  "ICHUSHI",
                  "ISBN",
                  "J-GLOBAL",
                  "Local",
                  "PISSN",
                  "EISSN",
                  "ISSN【非推奨】",
                  "NAID",
                  "NCID",
                  "PMID",
                  "PURL",
                  "SCOPUS",
                  "URI",
                  "WOS",
                  "CRID"
                ],
                "format": "select",
                "title": "識別子タイプ",
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "title": "関連識別子",
            "type": "object"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Relation",
      "type": "array"
    },
    "item_1617605131499": {
      "items": {
        "format": "object",
        "properties": {
          "accessrole": {
            "enum": [null, "open_access",
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
                  "enum": [null, "Available"
                  ],
                  "format": "select",
                  "title": "タイプ",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "dateValue": {
                  "format": "datetime",
                  "title": "公開日",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "公開日",
            "type": "array"
          },
          "displaytype": {
            "enum": [null, "detail",
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
                  "enum": [null, "Accepted",
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
                  "title": "日付タイプ",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "fileDateValue": {
                  "format": "datetime",
                  "title": "日付",
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
            "title": "ファイル名",
            "type": [
              "null",
              "string"
            ]
          },
          "filesize": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "value": {
                  "format": "text",
                  "title": "サイズ",
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
            "type": "string"
          },
          "groups": {
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
            "type": "string"
          },
          "licensetype": {
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
                "type": "string"
              },
              "objectType": {
                "enum": [null, "abstract",
                  "dataset",
                  "fulltext",
                  "iiif",
                  "software",
                  "summary",
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
                "type": "string"
              }
            },
            "title": "本文URL",
            "type": "object"
          },
          "version": {
            "format": "text",
            "title": "バージョン情報",
            "type": "string"
          }
        },
        "system_prop": true,
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "File",
      "type": "array"
    },
    "item_1617610673286": {
      "items": {
        "format": "object",
        "properties": {
          "nameIdentifiers": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "nameIdentifier": {
                  "format": "text",
                  "title": "権利者識別子",
                  "type": "string"
                },
                "nameIdentifierScheme": {
                  "format": "select",
                  "title": "権利者識別子Scheme",
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "nameIdentifierURI": {
                  "format": "text",
                  "title": "権利者識別子URI",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "権利者識別子",
            "type": "array"
          },
          "rightHolderNames": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "rightHolderLanguage": {
                  "editAble": true,
                  "enum": [null, "ja",
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
                },
                "rightHolderName": {
                  "format": "text",
                  "title": "権利者名",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "権利者名",
            "type": "array"
          }
        },
        "system_prop": true,
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Rights Holder",
      "type": "array"
    },
    "item_1617620223087": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_heading_banner_headline": {
            "format": "text",
            "title": "大見出し",
            "type": "string"
          },
          "subitem_heading_headline": {
            "format": "text",
            "title": "小見出し",
            "type": "string"
          },
          "subitem_heading_language": {
            "editAble": true,
            "enum": [null, "ja",
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
        "system_prop": true,
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Heading",
      "type": "array"
    },
    "item_1617944105607": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_degreegrantor": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_degreegrantor_language": {
                  "editAble": true,
                  "enum": [null, "ja",
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
                },
                "subitem_degreegrantor_name": {
                  "format": "text",
                  "title": "学位授与機関名",
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "学位授与機関名",
            "type": "array"
          },
          "subitem_degreegrantor_identifier": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "subitem_degreegrantor_identifier_name": {
                  "format": "text",
                  "title": "学位授与機関識別子",
                  "type": "string"
                },
                "subitem_degreegrantor_identifier_scheme": {
                  "enum": [null, "kakenhi"
                  ],
                  "format": "select",
                  "title": "学位授与機関識別子Scheme",
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "学位授与機関識別子",
            "type": "array"
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "Degree Grantor",
      "type": "array"
    },
    "item_1698591601": {
      "items": {
        "format": "object",
        "properties": {
          "holding_agent_name_identifier": {
            "format": "object",
            "properties": {
              "holding_agent_name_idenfitier_scheme": {
                "currentEnum": [null, "kakenhi",
                  "ISNI",
                  "Ringgold",
                  "GRID",
                  "ROR",
                  "FANO",
                  "ISIL",
                  "MARC",
                  "OCLC"
                ],
                "enum": [null, "kakenhi",
                  "ISNI",
                  "Ringgold",
                  "GRID",
                  "ROR",
                  "FANO",
                  "ISIL",
                  "MARC",
                  "OCLC"
                ],
                "format": "select",
                "title": "所蔵機関識別子スキーマ",
                "title_i18n": {
                  "en": "Holding Agent Name Identifier Schema",
                  "ja": "所蔵機関識別子スキーマ"
                },
                "type": "string"
              },
              "holding_agent_name_idenfitier_uri": {
                "format": "text",
                "title": "所蔵機関識別子URI",
                "title_i18n": {
                  "en": "Holding Agent Name Identifier URI",
                  "ja": "所蔵機関識別子URI"
                },
                "type": "string"
              },
              "holding_agent_name_idenfitier_value": {
                "format": "text",
                "title": "所蔵機関識別子",
                "title_i18n": {
                  "en": "Holding Agent Name Identifier",
                  "ja": "所蔵機関識別子"
                },
                "type": "string"
              }
            },
            "title": "所蔵機関識別子",
            "type": "object"
          },
          "holding_agent_names": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "holding_agent_name": {
                  "format": "text",
                  "title": "所蔵機関名",
                  "title_i18n": {
                    "en": "Holding Agent Name",
                    "ja": "所蔵機関名"
                  },
                  "type": "string"
                },
                "holding_agent_name_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "所蔵機関名",
            "type": "array"
          }
        },
        "title": "holding_agent_name",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "所蔵機関",
      "type": "array"
    },
    "item_1698591602": {
      "items": {
        "format": "object",
        "properties": {
          "subitem_dcterms_date": {
            "format": "text",
            "title": "日付（リテラル）",
            "title_i18n": {
              "en": "Date Literal",
              "ja": "日付（リテラル）"
            },
            "type": "string"
          },
          "subitem_dcterms_date_language": {
            "editAble": true,
            "enum": [null, "ja",
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
        "system_prop": false,
        "title": "dcterms_date",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "日付（リテラル）",
      "type": "array"
    },
    "item_1698591603": {
      "items": {
        "format": "object",
        "properties": {
          "jpcoar_dataset_series": {
            "enum": [null, "True",
              "False"
            ],
            "format": "select",
            "title": "Dataset Series",
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "データセットシリーズ",
      "type": "array"
    },
    "item_1698591604": {
      "items": {
        "format": "object",
        "properties": {
          "publication_places": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "publication_place": {
                  "format": "text",
                  "title": "出版地（国名コード）",
                  "title_i18n": {
                    "en": "Publication Place (Country code)",
                    "ja": "出版地（国名コード）"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "出版地（国名コード）",
            "type": "array"
          },
          "publisher_descriptions": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "publisher_description": {
                  "format": "text",
                  "title": "出版者注記",
                  "title_i18n": {
                    "en": "Publisher Description",
                    "ja": "出版者注記"
                  },
                  "type": "string"
                },
                "publisher_description_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "出版者注記",
            "type": "array"
          },
          "publisher_locations": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "publisher_location": {
                  "format": "text",
                  "title": "出版地",
                  "title_i18n": {
                    "en": "Publication Place",
                    "ja": "出版地"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "出版地",
            "type": "array"
          },
          "publisher_names": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "publisher_name": {
                  "format": "text",
                  "title": "出版者名",
                  "title_i18n": {
                    "en": "Publisher Name",
                    "ja": "出版者名"
                  },
                  "type": "string"
                },
                "publisher_name_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "出版者名",
            "type": "array"
          }
        },
        "title": "publisher_information",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "出版者情報",
      "type": "array"
    },
    "item_1698591605": {
      "items": {
        "format": "object",
        "properties": {
          "dcterms_extent": {
            "format": "text",
            "title": "Extent",
            "title_i18n": {
              "en": "Extent",
              "ja": "大きさ"
            },
            "type": "string"
          },
          "dcterms_extent_language": {
            "currentEnum": [null, "ja",
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
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "string"
          }
        },
        "title": "dcterms_extent",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "大きさ",
      "type": "array"
    },
    "item_1698591606": {
      "items": {
        "format": "object",
        "properties": {
          "catalog_access_rights": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_access_right": {
                  "currentEnum": [
                    "embargoed access",
                    "metadata only access",
                    "restricted access",
                    "open access"
                  ],
                  "enum": [
                    "embargoed access",
                    "metadata only access",
                    "restricted access",
                    "open access"
                  ],
                  "format": "select",
                  "title": "Access Rights",
                  "title_i18n": {
                    "en": "Access Rights",
                    "ja": "アクセス権"
                  },
                  "type": "string"
                },
                "catalog_access_right_rdf_resource": {
                  "format": "text",
                  "title": "RDF Resource",
                  "title_i18n": {
                    "en": "RDF Resource",
                    "ja": "RDFリソース"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "Access Rights",
            "type": "array"
          },
          "catalog_contributors": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "contributor_names": {
                  "format": "array",
                  "items": {
                    "format": "object",
                    "properties": {
                      "contributor_name": {
                        "format": "text",
                        "title": "Hosting Institution Name",
                        "title_i18n": {
                          "en": "Hosting Institution Name",
                          "ja": "提供機関名"
                        },
                        "type": "string"
                      },
                      "contributor_name_language": {
                        "currentEnum": [null, "ja",
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
                        "enum": [null, "ja",
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
                        "title_i18n": {
                          "en": "Language",
                          "ja": "言語"
                        },
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": "object"
                  },
                  "title": "Hosting Institution Name",
                  "type": "array"
                },
                "contributor_type": {
                  "currentEnum": [
                    "HostingInstitution"
                  ],
                  "enum": [
                    "HostingInstitution"
                  ],
                  "format": "select",
                  "title": "Hosting Institution Type",
                  "title_i18n": {
                    "en": "Hosting Institution Type",
                    "ja": "提供機関タイプ"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "Hosting Institution",
            "type": "array"
          },
          "catalog_descriptions": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_description": {
                  "format": "text",
                  "title": "Description",
                  "title_i18n": {
                    "en": "Description",
                    "ja": "内容記述"
                  },
                  "type": "string"
                },
                "catalog_description_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                },
                "catalog_description_type": {
                  "currentEnum": [
                    "Abstract",
                    "Methods",
                    "TableOfContents",
                    "TechnicalInfo",
                    "Other"
                  ],
                  "enum": [
                    "Abstract",
                    "Methods",
                    "TableOfContents",
                    "TechnicalInfo",
                    "Other"
                  ],
                  "format": "select",
                  "title": "Description Type",
                  "title_i18n": {
                    "en": "Description Type",
                    "ja": "内容記述タイプ"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "Description",
            "type": "array"
          },
          "catalog_file": {
            "format": "object",
            "properties": {
              "catalog_file_object_type": {
                "currentEnum": [
                  "thumbnail"
                ],
                "enum": [
                  "thumbnail"
                ],
                "format": "select",
                "title": "Object Type",
                "title_i18n": {
                  "en": "Object Type",
                  "ja": "オブジェクトタイプ"
                },
                "type": "string"
              },
              "catalog_file_uri": {
                "format": "text",
                "title": "Thumbnail URI",
                "title_i18n": {
                  "en": "Thumbnail URI",
                  "ja": "代表画像URI"
                },
                "type": "string"
              }
            },
            "title": "Thumbnail",
            "type": "object"
          },
          "catalog_identifiers": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_identifier": {
                  "format": "text",
                  "title": "Identifier",
                  "title_i18n": {
                    "en": "Identifier",
                    "ja": "識別子"
                  },
                  "type": "string"
                },
                "catalog_identifier_type": {
                  "currentEnum": [
                    "DOI",
                    "HDL",
                    "URI"
                  ],
                  "enum": [
                    "DOI",
                    "HDL",
                    "URI"
                  ],
                  "format": "select",
                  "title": "Identifier Type",
                  "title_i18n": {
                    "en": "Identifier Type",
                    "ja": "識別子タイプ"
                  },
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": "object"
            },
            "title": "Identifier",
            "type": "array"
          },
          "catalog_licenses": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_license": {
                  "format": "text",
                  "title": "License",
                  "title_i18n": {
                    "en": "License",
                    "ja": "ライセンス"
                  },
                  "type": "string"
                },
                "catalog_license_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                },
                "catalog_license_rdf_resource": {
                  "format": "text",
                  "title": "RDF Resource",
                  "title_i18n": {
                    "en": "RDF Resource",
                    "ja": "RDFリソース"
                  },
                  "type": "string"
                },
                "catalog_license_type": {
                  "currentEnum": [
                    "file",
                    "metadata",
                    "thumbnail"
                  ],
                  "enum": [
                    "file",
                    "metadata",
                    "thumbnail"
                  ],
                  "format": "select",
                  "title": "License Type",
                  "title_i18n": {
                    "en": "License Type",
                    "ja": "ライセンスタイプ"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "License",
            "type": "array"
          },
          "catalog_rights": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_right_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                },
                "catalog_right_rdf_resource": {
                  "format": "text",
                  "title": "RDF Resource",
                  "title_i18n": {
                    "en": "RDF Resource",
                    "ja": "RDFリソース"
                  },
                  "type": "string"
                },
                "catalog_rights_right": {
                  "format": "text",
                  "title": "Rights",
                  "title_i18n": {
                    "en": "Rights",
                    "ja": "権利情報"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "Rights",
            "type": "array"
          },
          "catalog_subjects": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_subject": {
                  "format": "text",
                  "title": "Subject",
                  "title_i18n": {
                    "en": "Subject",
                    "ja": "主題"
                  },
                  "type": "string"
                },
                "catalog_subject_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                },
                "catalog_subject_scheme": {
                  "currentEnum": [
                    "BSH",
                    "DDC",
                    "e-Rad",
                    "LCC",
                    "LCSH",
                    "MeSH",
                    "NDC",
                    "NDLC",
                    "NDLSH",
                    "SciVal",
                    "UDC",
                    "Other"
                  ],
                  "enum": [
                    "BSH",
                    "DDC",
                    "e-Rad",
                    "LCC",
                    "LCSH",
                    "MeSH",
                    "NDC",
                    "NDLC",
                    "NDLSH",
                    "SciVal",
                    "UDC",
                    "Other"
                  ],
                  "format": "select",
                  "title": "Subject Scheme",
                  "title_i18n": {
                    "en": "Subject Scheme",
                    "ja": "主題スキーマ"
                  },
                  "type": "string"
                },
                "catalog_subject_uri": {
                  "format": "text",
                  "title": "Subject URI",
                  "title_i18n": {
                    "en": "Subject URI",
                    "ja": "主題URI"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "Subject",
            "type": "array"
          },
          "catalog_titles": {
            "format": "array",
            "items": {
              "format": "object",
              "properties": {
                "catalog_title": {
                  "format": "text",
                  "title": "Title",
                  "title_i18n": {
                    "en": "Title",
                    "ja": "タイトル"
                  },
                  "type": "string"
                },
                "catalog_title_language": {
                  "currentEnum": [null, "ja",
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
                  "enum": [null, "ja",
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
                  "title_i18n": {
                    "en": "Language",
                    "ja": "言語"
                  },
                  "type": "string"
                }
              },
              "type": "object"
            },
            "title": "Title",
            "type": "array"
          }
        },
        "title": "catalog",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "カタログ",
      "type": "array"
    },
    "item_1698591607": {
      "items": {
        "format": "object",
        "properties": {
          "original_language": {
            "format": "text",
            "title": "Original Language",
            "title_i18n": {
              "en": "Volume Title",
              "ja": "原文の言語"
            },
            "type": "string"
          },
          "original_language_language": {
            "currentEnum": [null, "ja",
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
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "string"
          }
        },
        "title": "original_language",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "原文の言語",
      "type": "array"
    },
    "item_1698591608": {
      "items": {
        "format": "object",
        "properties": {
          "volume_title": {
            "format": "text",
            "title": "部編名",
            "title_i18n": {
              "en": "Volume Title",
              "ja": "部編名"
            },
            "type": "string"
          },
          "volume_title_language": {
            "currentEnum": [null, "ja",
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
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "string"
          }
        },
        "title": "volume_title",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "部編名",
      "type": "array"
    },
    "item_1698591609": {
      "items": {
        "format": "object",
        "properties": {
          "edition": {
            "format": "text",
            "title": "版",
            "title_i18n": {
              "en": "Edition",
              "ja": "版"
            },
            "type": "string"
          },
          "edition_language": {
            "currentEnum": [null, "ja",
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
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "string"
          }
        },
        "title": "edition",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "版",
      "type": "array"
    },
    "item_1698591610": {
      "items": {
        "format": "object",
        "properties": {
          "jpcoar_format": {
            "format": "text",
            "title": "物理的形態",
            "title_i18n": {
              "en": "Physical Format",
              "ja": "物理的形態"
            },
            "type": "string"
          },
          "jpcoar_format_language": {
            "currentEnum": [null, "ja",
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
            "enum": [null, "ja",
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
            "title_i18n": {
              "en": "Language",
              "ja": "言語"
            },
            "type": "string"
          }
        },
        "title": "jpcoar_format",
        "type": "object"
      },
      "maxItems": 9999,
      "minItems": 1,
      "title": "物理的形態",
      "type": "array"
    },
    "item_1727008761239": {
      "properties": {
        "interim": {
          "enum": [null, "a",
            "b",
            "c",
            "d"
          ],
          "format": "select",
          "title": "abc",
          "type": [
            "null",
            "string"
          ]
        }
      },
      "title": "abc",
      "title_i18n": {
        "en": "",
        "ja": ""
      },
      "type": "object"
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
          "currentEnum": [
            "DOI",
            "HDL",
            "URI"
          ],
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
          "currentEnum": [
            "DOI",
            "HDL",
            "URI"
          ],
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
          "currentEnum": [
            "DOI",
            "HDL",
            "URI"
          ],
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