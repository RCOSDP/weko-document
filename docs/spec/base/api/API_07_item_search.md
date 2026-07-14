### アイテム検索用API

  - 目的・用途

アイテム検索機能を提供する。

  - 利用方法

| **Method** | **HTTP request**     | **Description** |
| ---------- | -------------------- | --------------- |
|            | **GET /api/records** | アイテムを検索する       |

クエリパラメータ

| **GET /api/opensearch/search** |  |  |  |
| --- | --- | --- | --- |
| パラメータ | 必須 | 値 | 説明 |
| search_type |  | 0:フルテキスト<br>1:キーワード | フルテキストを指定した場合は本文ファイルから抽出されたテキストも検索対象とする。<br>キーワードを指定した場合はメタデータ項目のみを検索対象とする。 |
| q |  | string | 検索キーワードを指定する。 |
| size |  | int | 検索結果の件数を指定する |
| page |  | Int | 検索結果で表示するページ番号を指定する。 |
| Sort |  | +controlnumber<br>-controlnumber<br>+wtl<br>+wtl<br>+itemType<br>-itemType<br>他 | ソートキーを指定する。接頭辞「+」は昇順、「-」は降順となる。 |
| 以下は設定ファイルやアイテムタイプマッピングにより定義が変化する |  |  |  |
| title |  | string | dc:titleにマッピングされた項目の検索 |
| des |  | strin | datacite:descriptionにマッピングされた項目の検索 |
| type |  | string | dc:typeにマッピングされた項目の検索 |
| wid |  | Int | 作成者（著者）識別子（`creator.nameIdentifier`）を指定して検索。※「アイテムIDを指定」ではない点に注意 |
| iid |  | Int | インデックスID（`path.tree`）を指定して検索 |
| date_range1_from<br>date_range1_to |  | yyymmdd | dte_range1 に対して期間の範囲を指定して検索 |

レスポンス例：

/api/records/?page=1&size=1&sort=controlnumber&search_type=0&q=%E6%A6%82%E8%A6%81

```json
{
  "aggregations": {
    "Access": {
      "buckets": [
        {
          "doc_count": 1761,
          "key": "open access"
        }
      ],
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0
    },
    "Data Language": {
      "buckets": [
        {
          "doc_count": 1761,
          "key": "jpn"
        }
      ],
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0
    },
    "Data Type": {
      "Data Type": {
        "buckets": [],
        "doc_count_error_upper_bound": 0,
        "sum_other_doc_count": 0
      },
      "doc_count": 0
    },
    "Distributor": {
      "Distributor": {
        "buckets": [],
        "doc_count_error_upper_bound": 0,
        "sum_other_doc_count": 0
      },
      "doc_count": 0
    },
    "Location": {
      "buckets": [
        {
          "doc_count": 1761,
          "key": "Japan"
        }
      ],
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0
    },
    "Temporal": {
      "buckets": [
        {
          "doc_count": 1761,
          "key": "Temporal"
        }
      ],
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0
    },
    "Topic": {
      "buckets": [
        {
          "doc_count": 1761,
          "key": "Sibject1"
        }
      ],
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0
    },
    "path": {
      "buckets": [],
      "doc_count_error_upper_bound": "0",
      "sum_order_doc_count": "0"
    }
  },
  "hits": {
    "hits": [
      {
        "created": "2023-11-06T05:43:58.044449+00:00",
        "id": 1,
        "links": {
          "self": "https://dev.ir.rcos.nii.ac.jp/api/records/1"
        },
        "metadata": {
          "_comment": [
            "public-item-0-public-oai-guest-1-en",
            "Source Title,1,111,12,1,3,en,2021-06-30",
            "Conference Name",
            "1",
            "JPN",
            "Sponsor",
            "Conference Venue",
            "Conference Place"
          ],
          "_creator_info": [
            {
              "creatorAffiliations": [
                {
                  "affiliationNameIdentifiers": [
                    {
                      "affiliationNameIdentifier": "0000000121691048",
                      "affiliationNameIdentifierScheme": "ISNI",
                      "affiliationNameIdentifierURI": "http://isni.org/isni/0000000121691048"
                    }
                  ],
                  "affiliationNames": [
                    {
                      "affiliationName": "University",
                      "affiliationNameLang": "en"
                    }
                  ]
                }
              ],
              "creatorMails": [
                {
                  "creatorMail": "wekosoftware@nii.ac.jp"
                }
              ],
              "creatorNames": {
                "creatorName": "Joho\t Taro",
                "creatorNameLang": "en",
                "idx": 2
              },
              "familyNames": {
                "familyName": "Joho",
                "familyNameLang": "en",
                "idx": 2
              },
              "givenNames": {
                "givenName": "Taro",
                "givenNameLang": "en",
                "idx": 2
              },
              "nameIdentifiers": [
                {
                  "nameIdentifier": "4",
                  "nameIdentifierScheme": "WEKO"
                },
                {
                  "nameIdentifier": "xxxxxxx",
                  "nameIdentifierScheme": "ORCID",
                  "nameIdentifierURI": "https://orcid.org/"
                },
                {
                  "nameIdentifier": "xxxxxxx",
                  "nameIdentifierScheme": "CiNii",
                  "nameIdentifierURI": "https://ci.nii.ac.jp/"
                },
                {
                  "nameIdentifier": "zzzzzzz",
                  "nameIdentifierScheme": "KAKEN2",
                  "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                }
              ]
            },
            {
              "creatorMails": [
                {
                  "creatorMail": "wekosoftware@nii.ac.jp"
                }
              ],
              "creatorNames": {
                "creatorName": "Joho\t Taro",
                "creatorNameLang": "en",
                "idx": 2
              },
              "familyNames": {
                "familyName": "Joho",
                "familyNameLang": "en",
                "idx": 2
              },
              "givenNames": {
                "givenName": "Taro",
                "givenNameLang": "en",
                "idx": 2
              },
              "nameIdentifiers": [
                {
                  "nameIdentifier": "xxxxxxx",
                  "nameIdentifierScheme": "ORCID",
                  "nameIdentifierURI": "https://orcid.org/"
                },
                {
                  "nameIdentifier": "xxxxxxx",
                  "nameIdentifierScheme": "CiNii",
                  "nameIdentifierURI": "https://ci.nii.ac.jp/"
                },
                {
                  "nameIdentifier": "zzzzzzz",
                  "nameIdentifierScheme": "KAKEN2",
                  "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                }
              ]
            },
            {
              "creatorMails": [
                {
                  "creatorMail": "wekosoftware@nii.ac.jp"
                }
              ],
              "creatorNames": {
                "creatorName": "Joho\t Taro",
                "creatorNameLang": "en",
                "idx": 2
              },
              "familyNames": {
                "familyName": "Joho",
                "familyNameLang": "en",
                "idx": 2
              },
              "givenNames": {
                "givenName": "Taro",
                "givenNameLang": "en",
                "idx": 2
              },
              "nameIdentifiers": [
                {
                  "nameIdentifier": "xxxxxxx",
                  "nameIdentifierScheme": "ORCID",
                  "nameIdentifierURI": "https://orcid.org/"
                },
                {
                  "nameIdentifier": "xxxxxxx",
                  "nameIdentifierScheme": "CiNii",
                  "nameIdentifierURI": "https://ci.nii.ac.jp/"
                },
                {
                  "nameIdentifier": "zzzzzzz",
                  "nameIdentifierScheme": "KAKEN2",
                  "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                }
              ]
            }
          ],
          "_files_info": [
            {
              "extention": "pdf",
              "label": "1KB.pdf",
              "url": "https://weko3.example.org/record/1/files/1KB.pdf"
            }
          ],
          "_item_metadata": {
            "author_link": [
              "4"
            ],
            "control_number": "1",
            "item_1617186331708": {
              "attribute_name": "Title",
              "attribute_value_mlt": [
                {
                  "subitem_title": "public-item-0-public-oai-guest-1-ja",
                  "subitem_title_language": "ja"
                },
                {
                  "subitem_title": "public-item-0-public-oai-guest-1-en",
                  "subitem_title_language": "en"
                }
              ]
            },
            "item_1617186385884": {
              "attribute_name": "Alternative Title",
              "attribute_value_mlt": [
                {
                  "subitem_alternative_title": "Alternative Title",
                  "subitem_alternative_title_language": "en"
                },
                {
                  "subitem_alternative_title": "Alternative Title",
                  "subitem_alternative_title_language": "ja"
                }
              ]
            },
            "item_1617186419668": {
              "attribute_name": "Creator",
              "attribute_type": "creator",
              "attribute_value_mlt": [
                {
                  "creatorAffiliations": [
                    {
                      "affiliationNameIdentifiers": [
                        {
                          "affiliationNameIdentifier": "0000000121691048",
                          "affiliationNameIdentifierScheme": "ISNI",
                          "affiliationNameIdentifierURI": "http://isni.org/isni/0000000121691048"
                        }
                      ],
                      "affiliationNames": [
                        {
                          "affiliationName": "University",
                          "affiliationNameLang": "en"
                        }
                      ]
                    }
                  ],
                  "creatorMails": [
                    {
                      "creatorMail": "wekosoftware@nii.ac.jp"
                    }
                  ],
                  "creatorNames": {
                    "creatorName": "Joho\t Taro",
                    "creatorNameLang": "en",
                    "idx": 2
                  },
                  "familyNames": {
                    "familyName": "Joho",
                    "familyNameLang": "en",
                    "idx": 2
                  },
                  "givenNames": {
                    "givenName": "Taro",
                    "givenNameLang": "en",
                    "idx": 2
                  },
                  "nameIdentifiers": [
                    {
                      "nameIdentifier": "4",
                      "nameIdentifierScheme": "WEKO"
                    },
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "ORCID",
                      "nameIdentifierURI": "https://orcid.org/"
                    },
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "CiNii",
                      "nameIdentifierURI": "https://ci.nii.ac.jp/"
                    },
                    {
                      "nameIdentifier": "zzzzzzz",
                      "nameIdentifierScheme": "KAKEN2",
                      "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                    }
                  ]
                },
                {
                  "creatorMails": [
                    {
                      "creatorMail": "wekosoftware@nii.ac.jp"
                    }
                  ],
                  "creatorNames": {
                    "creatorName": "Joho\t Taro",
                    "creatorNameLang": "en",
                    "idx": 2
                  },
                  "familyNames": {
                    "familyName": "Joho",
                    "familyNameLang": "en",
                    "idx": 2
                  },
                  "givenNames": {
                    "givenName": "Taro",
                    "givenNameLang": "en",
                    "idx": 2
                  },
                  "nameIdentifiers": [
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "ORCID",
                      "nameIdentifierURI": "https://orcid.org/"
                    },
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "CiNii",
                      "nameIdentifierURI": "https://ci.nii.ac.jp/"
                    },
                    {
                      "nameIdentifier": "zzzzzzz",
                      "nameIdentifierScheme": "KAKEN2",
                      "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                    }
                  ]
                },
                {
                  "creatorMails": [
                    {
                      "creatorMail": "wekosoftware@nii.ac.jp"
                    }
                  ],
                  "creatorNames": {
                    "creatorName": "Joho\t Taro",
                    "creatorNameLang": "en",
                    "idx": 2
                  },
                  "familyNames": {
                    "familyName": "Joho",
                    "familyNameLang": "en",
                    "idx": 2
                  },
                  "givenNames": {
                    "givenName": "Taro",
                    "givenNameLang": "en",
                    "idx": 2
                  },
                  "nameIdentifiers": [
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "ORCID",
                      "nameIdentifierURI": "https://orcid.org/"
                    },
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "CiNii",
                      "nameIdentifierURI": "https://ci.nii.ac.jp/"
                    },
                    {
                      "nameIdentifier": "zzzzzzz",
                      "nameIdentifierScheme": "KAKEN2",
                      "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                    }
                  ]
                }
              ]
            },
            "item_1617186476635": {
              "attribute_name": "Access Rights",
              "attribute_value_mlt": [
                {
                  "subitem_access_right": "open access",
                  "subitem_access_right_uri": "http://purl.org/coar/access_right/c_abf2"
                }
              ]
            },
            "item_1617186499011": {
              "attribute_name": "Rights",
              "attribute_value_mlt": [
                {
                  "subitem_rights": "Rights Information",
                  "subitem_rights_language": "ja",
                  "subitem_rights_resource": "http://localhost"
                }
              ]
            },
            "item_1617186609386": {
              "attribute_name": "Subject",
              "attribute_value_mlt": [
                {
                  "subitem_subject": "Sibject1",
                  "subitem_subject_language": "ja",
                  "subitem_subject_scheme": "Other",
                  "subitem_subject_uri": "http://localhost/"
                }
              ]
            },
            "item_1617186626617": {
              "attribute_name": "Description",
              "attribute_value_mlt": [
                {
                  "subitem_description": "Description\nDescription\nDescription",
                  "subitem_description_language": "en",
                  "subitem_description_type": "Abstract"
                },
                {
                  "subitem_description": "概要\n概要\n概要\n概要",
                  "subitem_description_language": "ja",
                  "subitem_description_type": "Abstract"
                }
              ]
            },
            "item_1617186643794": {
              "attribute_name": "Publisher",
              "attribute_value_mlt": [
                {
                  "subitem_publisher": "en",
                  "subitem_publisher_languag": "Publisher"
                }
              ]
            },
            "item_1617186660861": {
              "attribute_name": "Date",
              "attribute_value_mlt": [
                {
                  "subitem_date_issued_datetime": "2021-06-30",
                  "subitem_date_issued_type": "Available"
                }
              ]
            },
            "item_1617186702042": {
              "attribute_name": "Language",
              "attribute_value_mlt": [
                {
                  "subitem_language": "jpn"
                }
              ]
            },
            "item_1617186783814": {
              "attribute_name": "Identifier",
              "attribute_value_mlt": [
                {
                  "subitem_identifier_type": "URI",
                  "subitem_identifier_uri": "http://localhost"
                }
              ]
            },
            "item_1617186859717": {
              "attribute_name": "Temporal",
              "attribute_value_mlt": [
                {
                  "subitem_temporal_languag": "en",
                  "subitem_temporal_text": "Temporal"
                }
              ]
            },
            "item_1617186882738": {
              "attribute_name": "Geo Location",
              "attribute_value_mlt": [
                {
                  "subitem_geolocation_place": [
                    {
                      "subitem_geolocation_place_text": "Japan"
                    }
                  ]
                }
              ]
            },
            "item_1617186901218": {
              "attribute_name": "Funding Reference",
              "attribute_value_mlt": [
                {
                  "subitem_award_numbers": {
                    "subitem_award_number": "Award Number",
                    "subitem_award_uri": "Award URI"
                  },
                  "subitem_award_titles": [
                    {
                      "subitem_award_title": "Award Title",
                      "subitem_award_title_language": "en"
                    }
                  ],
                  "subitem_funder_identifiers": {
                    "subitem_funder_identifier": "http://xxx",
                    "subitem_funder_identifier_type": "ISNI"
                  },
                  "subitem_funder_names": [
                    {
                      "subitem_funder_name": "Funder Name",
                      "subitem_funder_name_language": "en"
                    }
                  ]
                }
              ]
            },
            "item_1617186920753": {
              "attribute_name": "Source Identifier",
              "attribute_value_mlt": [
                {
                  "subitem_source_identifier": "xxxx-xxxx-xxxx",
                  "subitem_source_identifier_type": "ISSN"
                }
              ]
            },
            "item_1617186941041": {
              "attribute_name": "Source Title",
              "attribute_value_mlt": [
                {
                  "subitem_record_name": "Source Title",
                  "subitem_record_name_languag": "en"
                }
              ]
            },
            "item_1617186959569": {
              "attribute_name": "Volume Number",
              "attribute_value_mlt": [
                {
                  "subitem_volume": "1"
                }
              ]
            },
            "item_1617186981471": {
              "attribute_name": "Issue Number",
              "attribute_value_mlt": [
                {
                  "subitem_issue": "111"
                }
              ]
            },
            "item_1617186994930": {
              "attribute_name": "Number of Pages",
              "attribute_value_mlt": [
                {
                  "subitem_number_of_pages": "12"
                }
              ]
            },
            "item_1617187024783": {
              "attribute_name": "Page Start",
              "attribute_value_mlt": [
                {
                  "subitem_start_page": "1"
                }
              ]
            },
            "item_1617187045071": {
              "attribute_name": "Page End",
              "attribute_value_mlt": [
                {
                  "subitem_end_page": "3"
                }
              ]
            },
            "item_1617187112279": {
              "attribute_name": "Degree Name",
              "attribute_value_mlt": [
                {
                  "subitem_degreename": "en",
                  "subitem_issue": "Degree Name"
                }
              ]
            },
            "item_1617187136212": {
              "attribute_name": "Date Granted",
              "attribute_value_mlt": [
                {
                  "subitem_dategranted": "2021-06-30"
                }
              ]
            },
            "item_1617187187528": {
              "attribute_name": "Conference",
              "attribute_value_mlt": [
                {
                  "subitem_conference_country": "JPN",
                  "subitem_conference_date": {
                    "subitem_conference_date_language": "ja",
                    "subitem_conference_end_day": "1",
                    "subitem_conference_end_month": "12",
                    "subitem_conference_end_year": "2020",
                    "subitem_conference_period": "2020/12/11",
                    "subitem_conference_start_day": "1",
                    "subitem_conference_start_month": "12",
                    "subitem_conference_start_year": "2000"
                  },
                  "subitem_conference_names": [
                    {
                      "subitem_conference_name": "Conference Name",
                      "subitem_conference_name_language": "ja"
                    }
                  ],
                  "subitem_conference_places": [
                    {
                      "subitem_conference_place": "Conference Place",
                      "subitem_conference_place_language": "ja"
                    }
                  ],
                  "subitem_conference_sequence": "1",
                  "subitem_conference_sponsors": [
                    {
                      "subitem_conference_sponsor": "Sponsor",
                      "subitem_conference_sponsor_language": "ja"
                    }
                  ],
                  "subitem_conference_venues": [
                    {
                      "subitem_conference_venue": "Conference Venue",
                      "subitem_conference_venue_language": "ja"
                    }
                  ]
                }
              ]
            },
            "item_1617258105262": {
              "attribute_name": "Resource Type",
              "attribute_value_mlt": [
                {
                  "resourcetype": "conference paper",
                  "resourceuri": "http://purl.org/coar/resource_type/c_5794"
                }
              ]
            },
            "item_1617265215918": {
              "attribute_name": "Version Type",
              "attribute_value_mlt": [
                {
                  "subitem_version_resource": "http://purl.org/coar/version/c_b1a7d7d4d402bcce",
                  "subitem_version_type": "AO"
                }
              ]
            },
            "item_1617349709064": {
              "attribute_name": "Contributor",
              "attribute_value_mlt": [
                {
                  "contributorMails": [
                    {
                      "contributorMail": "wekosoftware@nii.ac.jp"
                    }
                  ],
                  "contributorNames": [
                    {
                      "contributorName": "情報, 太郎",
                      "lang": "ja"
                    },
                    {
                      "contributorName": "ジョウホウ\t タロウ",
                      "lang": "ja-Kana"
                    },
                    {
                      "contributorName": "Joho\t Taro",
                      "lang": "en"
                    }
                  ],
                  "contributorType": "ContactPerson",
                  "familyNames": [
                    {
                      "familyName": "情報",
                      "familyNameLang": "ja"
                    },
                    {
                      "familyName": "ジョウホウ",
                      "familyNameLang": "ja-Kana"
                    },
                    {
                      "familyName": "Joho",
                      "familyNameLang": "en"
                    }
                  ],
                  "givenNames": [
                    {
                      "givenName": "太郎",
                      "givenNameLang": "ja"
                    },
                    {
                      "givenName": "タロウ",
                      "givenNameLang": "ja-Kana"
                    },
                    {
                      "givenName": "Taro",
                      "givenNameLang": "en"
                    }
                  ],
                  "nameIdentifiers": [
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "ORCID",
                      "nameIdentifierURI": "https://orcid.org/"
                    },
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "CiNii",
                      "nameIdentifierURI": "https://ci.nii.ac.jp/"
                    },
                    {
                      "nameIdentifier": "xxxxxxx",
                      "nameIdentifierScheme": "KAKEN2",
                      "nameIdentifierURI": "https://kaken.nii.ac.jp/"
                    }
                  ]
                }
              ]
            },
            "item_1617349808926": {
              "attribute_name": "Version",
              "attribute_value_mlt": [
                {
                  "subitem_version": "Version"
                }
              ]
            },
            "item_1617351524846": {
              "attribute_name": "APC",
              "attribute_value_mlt": [
                {
                  "subitem_apc": "Unknown"
                }
              ]
            },
            "item_1617353299429": {
              "attribute_name": "Relation",
              "attribute_value_mlt": [
                {
                  "subitem_relation_name": [
                    {
                      "subitem_relation_name_language": "en",
                      "subitem_relation_name_text": "Related Title"
                    }
                  ],
                  "subitem_relation_type": "isVersionOf",
                  "subitem_relation_type_id": {
                    "subitem_relation_type_id_text": "xxxxx",
                    "subitem_relation_type_select": "arXiv"
                  }
                }
              ]
            },
            "item_1617605131499": {
              "attribute_name": "File",
              "attribute_type": "file",
              "attribute_value_mlt": [
                {
                  "accessrole": "open_access",
                  "date": [
                    {
                      "dateType": "Available",
                      "dateValue": "2021-07-12"
                    }
                  ],
                  "displaytype": "simple",
                  "filename": "1KB.pdf",
                  "filesize": [
                    {
                      "value": "1 KB"
                    }
                  ],
                  "format": "text/plain",
                  "mimetype": "application/pdf",
                  "url": {
                    "url": "https://dev.ir.rcos.nii.ac.jp/record/1/files/1KB.pdf"
                  },
                  "version_id": "b1a73fe7-5325-4819-953b-722518118e3d"
                }
              ]
            },
            "item_1617610673286": {
              "attribute_name": "Rights Holder",
              "attribute_value_mlt": [
                {
                  "nameIdentifiers": [
                    {
                      "nameIdentifier": "xxxxxx",
                      "nameIdentifierScheme": "ORCID",
                      "nameIdentifierURI": "https://orcid.org/"
                    }
                  ],
                  "rightHolderNames": [
                    {
                      "rightHolderLanguage": "ja",
                      "rightHolderName": "Right Holder Name"
                    }
                  ]
                }
              ]
            },
            "item_1617620223087": {
              "attribute_name": "Heading",
              "attribute_value_mlt": [
                {
                  "subitem_heading_banner_headline": "Banner Headline",
                  "subitem_heading_headline": "Subheading",
                  "subitem_heading_language": "ja"
                },
                {
                  "subitem_heading_banner_headline": "Banner Headline",
                  "subitem_heading_headline": "Subheding",
                  "subitem_heading_language": "en"
                }
              ]
            },
            "item_1617944105607": {
              "attribute_name": "Degree Grantor",
              "attribute_value_mlt": [
                {
                  "subitem_degreegrantor": [
                    {
                      "subitem_degreegrantor_language": "en",
                      "subitem_degreegrantor_name": "Degree Grantor Name"
                    }
                  ],
                  "subitem_degreegrantor_identifie": [
                    {
                      "subitem_degreegrantor_identifier_name": "xxxxxx",
                      "subitem_degreegrantor_identifier_scheme": "kakenhi"
                    }
                  ]
                }
              ]
            },
            "item_title": "public-item-0-public-oai-guest-1-ja",
            "item_type_id": "15",
            "owner": "1",
            "path": [
              "1"
            ],
            "pubdate": {
              "attribute_name": "PubDate",
              "attribute_value": "2021-11-20"
            },
            "publish_date": "2021-11-20",
            "publish_status": "0",
            "relation_version_is_last": true,
            "title": [
              "public-item-0-public-oai-guest-1-ja"
            ],
            "weko_shared_id": -1
          },
          "_oai": {
            "id": "oai:weko3.example.org:00000001",
            "sets": [
              "1"
            ]
          },
          "accessRights": [
            "open access"
          ],
          "alternative": [
            "Alternative Title",
            "Alternative Title"
          ],
          "apc": [
            "Unknown"
          ],
          "author_link": [
            "4"
          ],
          "conference": {
            "conferenceCountry": [
              "JPN"
            ],
            "conferenceDate": [
              "2020/12/11"
            ],
            "conferenceName": [
              "Conference Name"
            ],
            "conferenceSequence": [
              "1"
            ],
            "conferenceSponsor": [
              "Sponsor"
            ],
            "conferenceVenue": [
              "Conference Venue"
            ]
          },
          "contributor": {
            "@attributes": {
              "contributorType": [
                [
                  "ContactPerson"
                ]
              ]
            },
            "affiliation": {
              "affiliationName": [],
              "nameIdentifier": []
            },
            "contributorAlternative": [],
            "contributorName": [
              "情報, 太郎",
              "ジョウホウ\t タロウ",
              "Joho\t Taro"
            ],
            "familyName": [
              "情報",
              "ジョウホウ",
              "Joho"
            ],
            "givenName": [
              "太郎",
              "タロウ",
              "Taro"
            ],
            "nameIdentifier": [
              "xxxxxxx",
              "xxxxxxx",
              "xxxxxxx"
            ]
          },
          "control_number": "1",
          "creator": {
            "affiliation": {
              "affiliationName": [
                "University"
              ],
              "nameIdentifier": [
                "0000000121691048"
              ]
            },
            "creatorAlternative": [],
            "creatorName": [
              "情報, 太郎",
              "ジョウホウ\t タロウ",
              "Joho\t Taro",
              "情報, 太郎",
              "ジョウホウ\t タロウ",
              "Joho\t Taro",
              "情報, 太郎",
              "ジョウホウ\t タロウ",
              "Joho\t Taro"
            ],
            "familyName": [
              "情報",
              "ジョウホウ",
              "Joho",
              "情報",
              "ジョウホウ",
              "Joho",
              "情報",
              "ジョウホウ",
              "Joho"
            ],
            "givenName": [
              "太郎",
              "タロウ",
              "Taro",
              "太郎",
              "タロウ",
              "Taro",
              "太郎",
              "タロウ",
              "Taro"
            ],
            "nameIdentifier": [
              "4",
              "xxxxxxx",
              "xxxxxxx",
              "zzzzzzz",
              "xxxxxxx",
              "xxxxxxx",
              "zzzzzzz",
              "xxxxxxx",
              "xxxxxxx",
              "zzzzzzz"
            ]
          },
          "date": [
            {
              "dateType": "Available",
              "value": "2021-06-30"
            }
          ],
          "dateGranted": [
            "2021-06-30"
          ],
          "degreeGrantor": {
            "degreeGrantorName": [
              "Degree Grantor Name"
            ],
            "nameIdentifier": [
              "xxxxxx"
            ]
          },
          "degreeName": [
            "en"
          ],
          "description": [
            {
              "descriptionType": "Abstract",
              "value": "Description\nDescription\nDescription"
            },
            {
              "descriptionType": "Abstract",
              "value": "概要\n概要\n概要\n概要"
            }
          ],
          "feedback_mail_list": [
            {
              "author_id": "",
              "email": "wekosoftware@nii.ac.jp"
            }
          ],
          "fundingReference": {
            "awardNumber": [
              "Award Number"
            ],
            "awardTitle": [
              "Award Title"
            ],
            "funderIdentifier": [
              "http://xxx"
            ],
            "funderName": [
              "Funder Name"
            ]
          },
          "geoLocation": {
            "geoLocationPlace": [
              "Japan"
            ]
          },
          "identifier": [
            {
              "identifierType": "URI",
              "value": "http://localhost"
            }
          ],
          "issue": [
            "111"
          ],
          "itemtype": "デフォルトアイテムタイプ（フル）",
          "language": [
            "jpn"
          ],
          "numPages": [
            "12"
          ],
          "pageEnd": [
            "3"
          ],
          "pageStart": [
            "1"
          ],
          "path": [
            "1"
          ],
          "publish_date": "2021-11-20",
          "publish_status": "0",
          "publisher": [
            "Publisher"
          ],
          "relation": {
            "@attributes": {
              "relationType": [
                [
                  "isVersionOf"
                ]
              ]
            },
            "relatedIdentifier": [
              {
                "identifierType": "arXiv",
                "value": "xxxxx"
              }
            ],
            "relatedTitle": [
              "Related Title"
            ]
          },
          "relation_version_is_last": true,
          "rights": [
            "Rights Information"
          ],
          "rightsHolder": {
            "nameIdentifier": [
              "xxxxxx"
            ],
            "rightsHolderName": [
              "Right Holder Name"
            ]
          },
          "sourceIdentifier": [
            {
              "identifierType": "ISSN",
              "value": "xxxx-xxxx-xxxx"
            }
          ],
          "sourceTitle": [
            "Source Title"
          ],
          "subject": [
            {
              "subjectScheme": "Other",
              "value": "Sibject1"
            }
          ],
          "temporal": [
            "Temporal"
          ],
          "title": [
            "public-item-0-public-oai-guest-1-en",
            "public-item-0-public-oai-guest-1-ja"
          ],
          "type": [
            "conference paper"
          ],
          "version": [
            "Version"
          ],
          "versiontype": [
            "AO"
          ],
          "volume": [
            "1"
          ],
          "weko_creator_id": "1",
          "weko_shared_id": -1
        },
        "updated": "2023-11-15T02:46:32.217662+00:00"
      }
    ],
    "total": 1761
  },
  "links": {
    "next": "https://dev.ir.rcos.nii.ac.jp/api/records/?page=2&q=%E6%A6%82%E8%A6%81&size=1",
    "self": "https://dev.ir.rcos.nii.ac.jp/api/records/?page=1&q=%E6%A6%82%E8%A6%81&size=1"
  }
}
```

  - 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | 〇 | 〇 | 〇 | 〇 | 〇 | 〇 |

  - 機能内容

- キーワード・各種条件でアイテムメタデータ（および `search_type=0` の場合は本文抽出テキスト）を検索し、`hits` / `aggregations` / `links` 形式のJSONで返す。
- ログイン状態・ロールに応じて閲覧可能なアイテムのみを返す（権限フィルタ）。
- 本APIはInvenio標準形式のメタデータ検索であり、RO-Crate形式の検索（[API-12](./API_12_item_search_RO-Crate.md)）とは別物である。

  - 関連モジュール

- invenio-records-rest（実ハンドラ `views.RecordsListResource.get`、レスポンス生成）
- weko-search-ui（検索ファクトリ `query.es_search_factory`（`/api/records/` 用）/ `query.opensearch_factory`、権限フィルタ `query.get_permission_filter` / `query.check_permission_user`、`config.RECORDS_REST_ENDPOINTS` 上書き）
- weko-records（レスポンスシリアライザ `serializers.json_v1_search` / `opensearch_v1_search`、`record_class = api.WekoRecord`）

  - 処理概要

1. エンドポイント `GET /api/records/`（`RECORDS_REST_ENDPOINTS["recid"]` の `list_route`）。ハンドラは `invenio_records_rest.views.RecordsListResource.get`。
2. 検索ファクトリ（`es_search_factory`）が `search_type`（`WEKO_SEARCH_TYPE_DICT`＝FULL_TEXT:0 / KEYWORD:1 / INDEX:2）・`q`・`size`・`page`・`sort` 等からESクエリを構築する。
3. `get_permission_filter` により公開範囲を絞り込む。
4. レスポンスは JSON（`hits` / `aggregations` / `links`）。`search_index="{prefix}-weko"`、`max_result_window = WEKO_SEARCH_MAX_RESULT`（10000）。

  - 主要設定値

`RECORDS_REST_ENDPOINTS`（weko-search-ui で上書き）、`SEARCH_UI_SEARCH_INDEX`、`WEKO_SEARCH_TYPE_DICT`、`WEKO_SEARCH_MAX_RESULT`（10000）

  - 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/11/14 | V0.9.27 | 初版作成 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。機能内容・関連モジュール・処理概要・主要設定値を追記。`wid`（作成者識別子）・`iid` の説明を修正、API-12との違いを明記 |
