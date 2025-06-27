# Render


## 目的・用途



## 利用方法


## 構造

| # | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
|   | { |   |   |   |   |   |
|   |  "edit_notes":{ |   |   |   |   |   |
|   |   |  "item_1617186331708":"", |   |   |   |   |
|   |   |  ... |   |   |   |   |
|   | }, |   |   |   |   |   |
|   | "key_subproperty_languague":[ |   |   |   |   |   |
|   |  |  "item_1617186331708.subitem_title_language",  |   |   |   |   |
|   |  |  ... |   |   |   |   |
|   | ], |   |   |   |   |   |
|   | "meta_fix":{ |   |   |   |   |   |
|   |  | "pubdate":{  |   |   |   |   |
|   |  |  "input_type":"datetime",  |   |   |   |   |
|   |  |   "input_value":"", |   |   |   |   |
|   |  |  "option":{ |   |   |   |   |
|   |  |   | "crtf":false,  |   |   |   |
|   |  |   | "hidden":false,  |   |   |   |
|   |  |   | "multiple":false,  |   |   |   |
|   |  |   |"required":true, |   |   |   |
|   |  |   | "showlist":false  |   |   |   |
|   |  |  }, |   |   |   |   |
|   |  |  "title":"PubDate", |   |   |   |   |
|   |  |  "title_i18n":{ |   |   |   |   |
|   |  |   |  "en":"PubDate", |   |   |   |
|   |  |  |  "ja":"公開日" |   |   |   |
|   |  |  } |   |   |   |   |
|   |  | }, |   |   |   |   |
|   |  | ... |   |   |   |   |
|   | }, |   |   |   |   |   |
|   | "meta_list":{ |   |   |   |   |   |
|   |  | "item_1617186331708":{ |   |   |   |   |
|   |  |  |"input_maxItems":"9999", |   |   |   |
|   |  |  |"input_minItems":"1",  |   |   |   |
|   |  |  |"input_type":"cus_1001",  |   |   |  cus_<property id> |
|   |  |  |"input_value":"",   |   |   |   |
|   |  |  | "option":{  |   |   |   |
|   |  |  |  |"crtf":true, |   |   |
|   |  |  |  |"hidden":false, |   |   |
|   |  |  |  |"multiple":true, |   |   |
|   |  |  |  |"oneline":true, |   |   |
|   |  |  |  |"required":true, |   |   |
|   |  |  |  |"showlist":true |   |   |
|   |  |  |},  |   |   |   |
|   |  |  |"title":"Title",  |   |   |   |
|   |  |  |"title_i18n":{  |   |   |   |
|   |  |  ||"en":"Title",  |   |   |
|   |  |  ||"ja":"タイトル"  |   |   |
|   |  |  |},  |   |   |   |
|   |  | }, |   |   |   |   |
|   |  | "item_1617186331709":{ |   |   |   |   |
|   |  |  |"input_maxItems":"9999", |   |   |   |
|   |  |  |"input_minItems":"1",  |   |   |   |
|   |  |  |"input_type":"checkboxes",  |   |   | checkboxes |
|   |  |  |"input_value":"check1|check2|check3",   |   |   |   |
|   |  |  | "option":{  |   |   |   |
|   |  |  |  |"crtf":true, |   |   |
|   |  |  |  |"hidden":false, |   |   |
|   |  |  |  |"multiple":true, |   |   |
|   |  |  |  |"oneline":true, |   |   |
|   |  |  |  |"required":true, |   |   |
|   |  |  |  |"showlist":true |   |   |
|   |  |  |},  |   |   |   |
|   |  |  |"title":"Checkbox",  |   |   |   |
|   |  |  |"title_i18n":{  |   |   |   |
|   |  |  ||"en":"Checkbox",  |   |   |
|   |  |  ||"ja":"Checkbox"  |   |   |
|   |  |  |},  |   |   |   |
|   |  | }, |   |   |   |   |
|   |  | "item_1617186331710":{ |   |   |   |   |
|   |  |  |"input_maxItems":"9999", |   |   |   |
|   |  |  |"input_minItems":"1",  |   |   |   |
|   |  |  |"input_type":"radios",  |   |   |  radios |
|   |  |  |"input_value":"radio1|radio2|radio3",   |   |   |   |
|   |  |  | "option":{  |   |   |   |
|   |  |  |  |"crtf":true, |   |   |
|   |  |  |  |"hidden":false, |   |   |
|   |  |  |  |"multiple":true, |   |   |
|   |  |  |  |"oneline":true, |   |   |
|   |  |  |  |"required":true, |   |   |
|   |  |  |  |"showlist":true |   |   |
|   |  |  |},  |   |   |   |
|   |  |  |"title":"Radios",  |   |   |   |
|   |  |  |"title_i18n":{  |   |   |   |
|   |  |  ||"en":"Radios",  |   |   |
|   |  |  ||"ja":"Radios"  |   |   |
|   |  |  |},  |   |   |   |
|   |  | }, |   |   |   |   |
|   |  | "item_1617186331711":{ |   |   |   |   |
|   |  |  |"input_maxItems":"9999", |   |   |   |
|   |  |  |"input_minItems":"1",  |   |   |   |
|   |  |  |"input_type":"select",  |   |   |  |
|   |  |  |"input_value":"",   |   |   |   |
|   |  |  | "option":{  |   |   |   |
|   |  |  |  |"crtf":true, |   |   |
|   |  |  |  |"hidden":false, |   |   |
|   |  |  |  |"multiple":true, |   |   |
|   |  |  |  |"oneline":true, |   |   |
|   |  |  |  |"required":true, |   |   |
|   |  |  |  |"showlist":true |   |   |
|   |  |  |},  |   |   |   |
|   |  |  |"title":"Select",  |   |   |   |
|   |  |  |"title_i18n":{  |   |   |   |
|   |  |  ||"en":"Select",  |   |   |
|   |  |  ||"ja":"Select"  |   |   |
|   |  |  |},  |   |   |   |
|   |  | }, |   |   |   |   |
|   |  | ... |   |   |   |   |
|   | }, |   |   |   |   |   |
|   | } |   |   |   |   |   |



```       

         
         
            
           
      ...
      {
         "type": "object", 
         "format": "object", 
         "properties": {
            "resourceuri": {
               "type": "string", 
               "title": "資源タイプ識別子", 
               "format": "text",  
               "title_i18n": {"en": "Resource Type Identifier", "ja": "資源タイプ識別子"}
            },
            "resourcetype": {
               "enum": [
                  null, "conference paper", "data paper", "departmental bulletin paper", "editorial", "journal", "journal article", "newspaper", "review article", "other periodical", "software paper", "article", "book", "book part", "cartographic material", "map", "conference output", "conference presentation", "conference proceedings", "conference poster", "aggregated data", "clinical trial data", "compiled data", "dataset", "encoded data", "experimental data", "genomic data", "geospatial data", "laboratory notebook", "measurement and test data", "observational data", "recorded data", "simulation data", "survey data", "image", "still image", "moving image", "video", "lecture", "design patent", "patent", "PCT application", "plant patent", "plant variety protection", "software patent", "trademark", "utility model", "report", "research report", "technical report", "policy report", "working paper", "data management plan", "sound", "thesis", "bachelor thesis", "master thesis", "doctoral thesis", "commentary", "design", "industrial design", "interactive resource", "layout design", "learning object", "manuscript", "musical notation", "peer review", "research proposal", "research protocol", "software", "source code", "technical documentation", "transcription", "workflow", "other"
               ], 
               "type": ["null", "string"], 
               "title": "資源タイプ", 
               "format": "select", 
               "title_i18n": {"en": "Resource Type", "ja": "資源タイプ "}, 
               "currentEnum": [
                  "conference paper", "data paper", "departmental bulletin paper", "editorial", "journal", "journal article", "newspaper", "review article", "other periodical", "software paper", "article", "book", "book part", "cartographic material", "map", "conference output", "conference presentation", "conference proceedings", "conference poster", "aggregated data", "clinical trial data", "compiled data", "dataset", "encoded data", "experimental data", "genomic data", "geospatial data", "laboratory notebook", "measurement and test data", "observational data", "recorded data", "simulation data", "survey data", "image", "still image", "moving image", "video", "lecture", "design patent", "patent", "PCT application", "plant patent", "plant variety protection", "software patent", "trademark", "utility model", "report", "research report", "technical report", "policy report", "working paper", "data management plan", "sound", "thesis", "bachelor thesis", "master thesis", "doctoral thesis", "commentary", "design", "industrial design", "interactive resource", "layout design", "learning object", "manuscript", "musical notation", "peer review", "research proposal", "research protocol", "software", "source code", "technical documentation", "transcription", "workflow", "other"
               ]
            }
         }, 
         "system_prop": true
      }
      ...
   },
   "meta_system":{
      "system_file":{
         "input_type":"cus_125",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"File Information",
         "title_i18n":{
            "en":"File Information",
            "ja":"ファイル情報"
         }
      },
      "system_identifier_doi":{
         "input_type":"cus_123",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"Persistent Identifier(DOI)",
         "title_i18n":{
            "en":"Persistent Identifier(DOI)",
            "ja":"永続識別子（DOI）"
         }
      },
      "system_identifier_hdl":{
         "input_type":"cus_123",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"Persistent Identifier(HDL)",
         "title_i18n":{
            "en":"Persistent Identifier(HDL)",
            "ja":"永続識別子（HDL）"
         }
      },
      "system_identifier_uri":{
         "input_type":"cus_123",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"Persistent Identifier(URI)",
         "title_i18n":{
            "en":"Persistent Identifier(URI)",
            "ja":"永続識別子（URI）"
         }
      }
   },
   "schemaeditor":{
      "schema":{
         "item_1617186331708":{
            "format":"object",
            "properties":{
               "subitem_title":{
                  "format":"text",
                  "title":"タイトル",
                  "title_i18n":{
                     "en":"Title",
                     "ja":"タイトル"
                  },
                  "type":"string"
               },
               "subitem_title_language":{
                  "currentEnum":[
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
                  "enum":[
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
                  "format":"select",
                  "title":"言語",
                  "type":[
                     "null",
                     "string"
                  ]
               }
            },
            "required":[
               "subitem_title"
            ],
            "type":"object"
         },
       ...
      }
   },
   "table_row":[
      "item_1617186331708",
      ...
   ],
   "table_row_map":{
      "action":"upt",
      "form":[
         {
            "format":"yyyy-MM-dd",
            "key":"pubdate",
            "required":true,
            "templateUrl":"/static/templates/weko_deposit/datepicker.html",
            "title":"PubDate",
            "title_i18n":{
               "en":"PubDate",
               "ja":"公開日"
            },
            "type":"template"
         },
         {
            "add":"New",
            "items":[
               {
                  "isHide":true,
                  "isNonDisplay":true,
                  "isShowList":true,
                  "isSpecifyNewline":true,
                  "key":"item_1617186331708[].subitem_title",
                  "required":true,
                  "title":"タイトル",
                  "title_i18n":{
                     "en":"Title",
                     "ja":"タイトル"
                  },
                  "type":"text"
               },
               {
                  "key":"item_1617186331708[].subitem_title_language",
                  "title":"言語",
                  "titleMap":[
                     {
                        "name":"ja",
                        "value":"ja"
                     },
                     {
                        "name":"ja-Kana",
                        "value":"ja-Kana"
                     },
                     {
                        "name":"ja-Latn",
                        "value":"ja-Latn"
                     }
                  ],
                  "title_i18n":{
                     "en":"Language",
                     "ja":"言語"
                  },
                  "type":"select"
               }
            ],
            "key":"item_1617186331708",
            "style":{
               "add":"btn-success"
            },
            "title":"Title",
            "title_i18n":{
               "en":"Title",
               "ja":"タイトル"
            }
         },
         ...
         {
            "items":[
               {
                  "key":"parentkey.subitem_systemidt_identifier",
                  "title":"SYSTEMIDT Identifier",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemidt_identifier_type",
                  "title":"SYSTEMIDT Identifier Type",
                  "titleMap":[
                     {
                        "name":"DOI",
                        "value":"DOI"
                     },
                     {
                        "name":"HDL",
                        "value":"HDL"
                     },
                     {
                        "name":"URI",
                        "value":"URI"
                     }
                  ],
                  "type":"select"
               }
            ],
            "key":"system_identifier_doi",
            "title":"Persistent Identifier(DOI)",
            "title_i18n":{
               "en":"Persistent Identifier(DOI)",
               "ja":"永続識別子（DOI）"
            },
            "type":"fieldset"
         },
         {
            "items":[
               {
                  "key":"parentkey.subitem_systemidt_identifier",
                  "title":"SYSTEMIDT Identifier",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemidt_identifier_type",
                  "title":"SYSTEMIDT Identifier Type",
                  "titleMap":[
                     {
                        "name":"DOI",
                        "value":"DOI"
                     },
                     {
                        "name":"HDL",
                        "value":"HDL"
                     },
                     {
                        "name":"URI",
                        "value":"URI"
                     }
                  ],
                  "type":"select"
               }
            ],
            "key":"system_identifier_hdl",
            "title":"Persistent Identifier(HDL)",
            "title_i18n":{
               "en":"Persistent Identifier(HDL)",
               "ja":"永続識別子（HDL）"
            },
            "type":"fieldset"
         },
         {
            "items":[
               {
                  "key":"parentkey.subitem_systemidt_identifier",
                  "title":"SYSTEMIDT Identifier",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemidt_identifier_type",
                  "title":"SYSTEMIDT Identifier Type",
                  "titleMap":[
                     {
                        "name":"DOI",
                        "value":"DOI"
                     },
                     {
                        "name":"HDL",
                        "value":"HDL"
                     },
                     {
                        "name":"URI",
                        "value":"URI"
                     }
                  ],
                  "type":"select"
               }
            ],
            "key":"system_identifier_uri",
            "title":"Persistent Identifier(URI)",
            "title_i18n":{
               "en":"Persistent Identifier(URI)",
               "ja":"永続識別子（URI）"
            },
            "type":"fieldset"
         },
         {
            "items":[
               {
                  "add":"New",
                  "items":[
                     {
                        "key":"parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_label",
                        "title":"SYSTEMFILE Filename Label",
                        "type":"text"
                     },
                     {
                        "key":"parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_type",
                        "title":"SYSTEMFILE Filename Type",
                        "titleMap":[
                           {
                              "name":"Abstract",
                              "value":"Abstract"
                           },
                           {
                              "name":"Fulltext",
                              "value":"Fulltext"
                           },
                           {
                              "name":"Summary",
                              "value":"Summary"
                           },
                           {
                              "name":"Thumbnail",
                              "value":"Thumbnail"
                           },
                           {
                              "name":"Other",
                              "value":"Other"
                           }
                        ],
                        "type":"select"
                     },
                     {
                        "key":"parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_uri",
                        "title":"SYSTEMFILE Filename URI",
                        "type":"text"
                     }
                  ],
                  "key":"parentkey.subitem_systemfile_filename",
                  "style":{
                     "add":"btn-success"
                  },
                  "title":"SYSTEMFILE Filename"
               },
               {
                  "key":"parentkey.subitem_systemfile_mimetype",
                  "title":"SYSTEMFILE MimeType",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemfile_size",
                  "title":"SYSTEMFILE Size",
                  "type":"text"
               },
               {
                  "add":"New",
                  "items":[
                     {
                        "format":"yyyy-MM-dd",
                        "key":"parentkey.subitem_systemfile_datetime[].subitem_systemfile_datetime_date",
                        "templateUrl":"/static/templates/weko_deposit/datepicker.html",
                        "title":"SYSTEMFILE DateTime Date",
                        "type":"template"
                     },
                     {
                        "key":"parentkey.subitem_systemfile_datetime[].subitem_systemfile_datetime_type",
                        "title":"SYSTEMFILE DateTime Type",
                        "titleMap":[
                           {
                              "name":"Accepted",
                              "value":"Accepted"
                           },
                           {
                              "name":"Available",
                              "value":"Available"
                           },
                           {
                              "name":"Collected",
                              "value":"Collected"
                           },
                           {
                              "name":"Copyrighted",
                              "value":"Copyrighted"
                           },
                           {
                              "name":"Created",
                              "value":"Created"
                           },
                           {
                              "name":"Issued",
                              "value":"Issued"
                           },
                           {
                              "name":"Submitted",
                              "value":"Submitted"
                           },
                           {
                              "name":"Updated",
                              "value":"Updated"
                           },
                           {
                              "name":"Valid",
                              "value":"Valid"
                           }
                        ],
                        "type":"select"
                     }
                  ],
                  "key":"parentkey.subitem_systemfile_datetime",
                  "style":{
                     "add":"btn-success"
                  },
                  "title":"SYSTEMFILE DateTime"
               },
               {
                  "key":"parentkey.subitem_systemfile_version",
                  "title":"SYSTEMFILE Version",
                  "type":"text"
               }
            ],
            "key":"system_file",
            "title":"File Information",
            "title_i18n":{
               "en":"File Information",
               "ja":"ファイル情報"
            },
            "type":"fieldset"
         }
      ],
      "mapping":{
         "item_1617186331708":{
            "display_lang_type":"",
            "jpcoar_mapping":{
               "title":{
                  "@attributes":{
                     "xml:lang":"subitem_title_language"
                  },
                  "@value":"subitem_title"
               }
            },
            "jpcoar_v1_mapping":{
               "title":{
                  "@attributes":{
                     "xml:lang":"subitem_title_language"
                  },
                  "@value":"subitem_title"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "title":{
                  "@value":"subitem_title"
               }
            },
            "spase_mapping":""
         },
        ...
         "pubdate":{
            "display_lang_type":"",
            "jpcoar_mapping":"",
            "jpcoar_v1_mapping":"",
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":"",
            "spase_mapping":""
         },
         "system_file":{
            "display_lang_type":"",
            "jpcoar_mapping":{
               "system_file":{
                  "URI":{
                     "@attributes":{
                        "label":"subitem_systemfile_filename_label",
                        "objectType":"subitem_systemfile_filename_type"
                     },
                     "@value":"subitem_systemfile_filename_uri"
                  },
                  "date":{
                     "@attributes":{
                        "dateType":"subitem_systemfile_datetime_type"
                     },
                     "@value":"subitem_systemfile_datetime_date"
                  },
                  "extent":{
                     "@value":"subitem_systemfile_size"
                  },
                  "mimeType":{
                     "@value":"subitem_systemfile_mimetype"
                  },
                  "version":{
                     "@value":"subitem_systemfile_version"
                  }
               }
            },
            "jpcoar_v1_mapping":{
               "system_file":{
                  "URI":{
                     "@attributes":{
                        "label":"subitem_systemfile_filename_label",
                        "objectType":"subitem_systemfile_filename_type"
                     },
                     "@value":"subitem_systemfile_filename_uri"
                  },
                  "date":{
                     "@attributes":{
                        "dateType":"subitem_systemfile_datetime_type"
                     },
                     "@value":"subitem_systemfile_datetime_date"
                  },
                  "extent":{
                     "@value":"subitem_systemfile_size"
                  },
                  "mimeType":{
                     "@value":"subitem_systemfile_mimetype"
                  },
                  "version":{
                     "@value":"subitem_systemfile_version"
                  }
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":"",
            "spase_mapping":""
         },
         "system_identifier_doi":{
            "ddi_mapping":{
               "stdyDscr":{
                  "citation":{
                     "holdings":{
                        "@attributes":{
                           "URI":"subitem_systemidt_identifier"
                        }
                     }
                  }
               }
            },
            "display_lang_type":"",
            "jpcoar_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "jpcoar_v1_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "identifier":{
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "spase_mapping":""
         },
         "system_identifier_hdl":{
            "ddi_mapping":{
               "stdyDscr":{
                  "citation":{
                     "holdings":{
                        "@attributes":{
                           "URI":"subitem_systemidt_identifier"
                        }
                     }
                  }
               }
            },
            "display_lang_type":"",
            "jpcoar_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "jpcoar_v1_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "identifier":{
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "spase_mapping":""
         },
         "system_identifier_uri":{
            "ddi_mapping":{
               "stdyDscr":{
                  "citation":{
                     "holdings":{
                        "@attributes":{
                           "URI":"subitem_systemidt_identifier"
                        }
                     }
                  }
               }
            },
            "display_lang_type":"",
            "jpcoar_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "jpcoar_v1_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "identifier":{
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "spase_mapping":""
         }
      },
      "name":"デフォルトアイテムタイプ（フル）",
      "schema":{
         "$schema":"http://json-schema.org/draft-04/schema#",
         "description":"",
         "properties":{
            "item_1617186331708":{
               "items":{
                  "properties":{
                     "subitem_title":{
                        "format":"text",
                        "title":"タイトル",
                        "title_i18n":{
                           "en":"Title",
                           "ja":"タイトル"
                        },
                        "type":"string"
                     },
                     "subitem_title_language":{
                        "currentEnum":[
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
                        "enum":[
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
                        "format":"select",
                        "title":"言語",
                        "type":[
                           "null",
                           "string"
                        ]
                     }
                  },
                  "required":[
                     "subitem_title"
                  ],
                  "type":"object"
               },
               "maxItems":"9999",
               "minItems":"1",
               "title":"Title",
               "type":"array"
            },
            ...
            "pubdate":{
               "format":"datetime",
               "title":"PubDate",
               "type":"string"
            },
            "system_file":{
               "format":"object",
               "properties":{
                  "subitem_systemfile_datetime":{
                     "format":"array",
                     "items":{
                        "format":"object",
                        "properties":{
                           "subitem_systemfile_datetime_date":{
                              "format":"datetime",
                              "title":"SYSTEMFILE DateTime Date",
                              "type":"string"
                           },
                           "subitem_systemfile_datetime_type":{
                              "enum":[
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
                              "format":"select",
                              "title":"SYSTEMFILE DateTime Type",
                              "type":"string"
                           }
                        },
                        "type":"object"
                     },
                     "title":"SYSTEMFILE DateTime",
                     "type":"array"
                  },
                  "subitem_systemfile_filename":{
                     "format":"array",
                     "items":{
                        "format":"object",
                        "properties":{
                           "subitem_systemfile_filename_label":{
                              "format":"text",
                              "title":"SYSTEMFILE Filename Label",
                              "type":"string"
                           },
                           "subitem_systemfile_filename_type":{
                              "enum":[
                                 "Abstract",
                                 "Fulltext",
                                 "Summary",
                                 "Thumbnail",
                                 "Other"
                              ],
                              "format":"select",
                              "title":"SYSTEMFILE Filename Type",
                              "type":"string"
                           },
                           "subitem_systemfile_filename_uri":{
                              "format":"text",
                              "title":"SYSTEMFILE Filename URI",
                              "type":"string"
                           }
                        },
                        "type":"object"
                     },
                     "title":"SYSTEMFILE Filename",
                     "type":"array"
                  },
                  "subitem_systemfile_mimetype":{
                     "format":"text",
                     "title":"SYSTEMFILE MimeType",
                     "type":"string"
                  },
                  "subitem_systemfile_size":{
                     "format":"text",
                     "title":"SYSTEMFILE Size",
                     "type":"string"
                  },
                  "subitem_systemfile_version":{
                     "format":"text",
                     "title":"SYSTEMFILE Version",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"File Information",
               "type":"object"
            },
            "system_identifier_doi":{
               "format":"object",
               "properties":{
                  "subitem_systemidt_identifier":{
                     "format":"text",
                     "title":"SYSTEMIDT Identifier",
                     "type":"string"
                  },
                  "subitem_systemidt_identifier_type":{
                     "currentEnum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "enum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "format":"select",
                     "title":"SYSTEMIDT Identifier Type",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"Persistent Identifier(DOI)",
               "type":"object"
            },
            "system_identifier_hdl":{
               "format":"object",
               "properties":{
                  "subitem_systemidt_identifier":{
                     "format":"text",
                     "title":"SYSTEMIDT Identifier",
                     "type":"string"
                  },
                  "subitem_systemidt_identifier_type":{
                     "currentEnum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "enum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "format":"select",
                     "title":"SYSTEMIDT Identifier Type",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"Persistent Identifier(HDL)",
               "type":"object"
            },
            "system_identifier_uri":{
               "format":"object",
               "properties":{
                  "subitem_systemidt_identifier":{
                     "format":"text",
                     "title":"SYSTEMIDT Identifier",
                     "type":"string"
                  },
                  "subitem_systemidt_identifier_type":{
                     "currentEnum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "enum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "format":"select",
                     "title":"SYSTEMIDT Identifier Type",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"Persistent Identifier(URI)",
               "type":"object"
            }
         },
         "required":[
            "pubdate",
            "item_1617186331708",
            ...
         ],
         "type":"object"
      }
   },
   "upload_file":false
}
```

```
{
   "edit_notes":{
      "item_1617186331708":"",
     ...
   },
   "key_subproperty_languague":[
      "item_1617186331708.subitem_title_language",
      ...
   ],
   "meta_fix":{
      "pubdate":{
         "input_type":"datetime",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":false,
            "multiple":false,
            "required":true,
            "showlist":false
         },
         "title":"PubDate",
         "title_i18n":{
            "en":"PubDate",
            "ja":"公開日"
         }
      }
   },
   "meta_list":{
      "item_1617186331708":{
         "input_maxItems":"9999",
         "input_minItems":"1",
         "input_type":"cus_1001",
         "input_value":"",
         "option":{
            "crtf":true,
            "hidden":false,
            "multiple":true,
            "oneline":true,
            "required":true,
            "showlist":true
         },
         "title":"Title",
         "title_i18n":{
            "en":"Title",
            "ja":"タイトル"
         }
      },
      ...
      {
         "type": "object", 
         "format": "object", 
         "properties": {
            "resourceuri": {
               "type": "string", 
               "title": "資源タイプ識別子", 
               "format": "text",  
               "title_i18n": {"en": "Resource Type Identifier", "ja": "資源タイプ識別子"}
            },
            "resourcetype": {
               "enum": [
                  null, "conference paper", "data paper", "departmental bulletin paper", "editorial", "journal", "journal article", "newspaper", "review article", "other periodical", "software paper", "article", "book", "book part", "cartographic material", "map", "conference output", "conference presentation", "conference proceedings", "conference poster", "aggregated data", "clinical trial data", "compiled data", "dataset", "encoded data", "experimental data", "genomic data", "geospatial data", "laboratory notebook", "measurement and test data", "observational data", "recorded data", "simulation data", "survey data", "image", "still image", "moving image", "video", "lecture", "design patent", "patent", "PCT application", "plant patent", "plant variety protection", "software patent", "trademark", "utility model", "report", "research report", "technical report", "policy report", "working paper", "data management plan", "sound", "thesis", "bachelor thesis", "master thesis", "doctoral thesis", "commentary", "design", "industrial design", "interactive resource", "layout design", "learning object", "manuscript", "musical notation", "peer review", "research proposal", "research protocol", "software", "source code", "technical documentation", "transcription", "workflow", "other"
               ], 
               "type": ["null", "string"], 
               "title": "資源タイプ", 
               "format": "select", 
               "title_i18n": {"en": "Resource Type", "ja": "資源タイプ "}, 
               "currentEnum": [
                  "conference paper", "data paper", "departmental bulletin paper", "editorial", "journal", "journal article", "newspaper", "review article", "other periodical", "software paper", "article", "book", "book part", "cartographic material", "map", "conference output", "conference presentation", "conference proceedings", "conference poster", "aggregated data", "clinical trial data", "compiled data", "dataset", "encoded data", "experimental data", "genomic data", "geospatial data", "laboratory notebook", "measurement and test data", "observational data", "recorded data", "simulation data", "survey data", "image", "still image", "moving image", "video", "lecture", "design patent", "patent", "PCT application", "plant patent", "plant variety protection", "software patent", "trademark", "utility model", "report", "research report", "technical report", "policy report", "working paper", "data management plan", "sound", "thesis", "bachelor thesis", "master thesis", "doctoral thesis", "commentary", "design", "industrial design", "interactive resource", "layout design", "learning object", "manuscript", "musical notation", "peer review", "research proposal", "research protocol", "software", "source code", "technical documentation", "transcription", "workflow", "other"
               ]
            }
         }, 
         "system_prop": true
      }
      ...
   },
   "meta_system":{
      "system_file":{
         "input_type":"cus_125",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"File Information",
         "title_i18n":{
            "en":"File Information",
            "ja":"ファイル情報"
         }
      },
      "system_identifier_doi":{
         "input_type":"cus_123",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"Persistent Identifier(DOI)",
         "title_i18n":{
            "en":"Persistent Identifier(DOI)",
            "ja":"永続識別子（DOI）"
         }
      },
      "system_identifier_hdl":{
         "input_type":"cus_123",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"Persistent Identifier(HDL)",
         "title_i18n":{
            "en":"Persistent Identifier(HDL)",
            "ja":"永続識別子（HDL）"
         }
      },
      "system_identifier_uri":{
         "input_type":"cus_123",
         "input_value":"",
         "option":{
            "crtf":false,
            "hidden":true,
            "multiple":false,
            "oneline":false,
            "required":false,
            "showlist":false
         },
         "title":"Persistent Identifier(URI)",
         "title_i18n":{
            "en":"Persistent Identifier(URI)",
            "ja":"永続識別子（URI）"
         }
      }
   },
   "schemaeditor":{
      "schema":{
         "item_1617186331708":{
            "format":"object",
            "properties":{
               "subitem_title":{
                  "format":"text",
                  "title":"タイトル",
                  "title_i18n":{
                     "en":"Title",
                     "ja":"タイトル"
                  },
                  "type":"string"
               },
               "subitem_title_language":{
                  "currentEnum":[
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
                  "enum":[
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
                  "format":"select",
                  "title":"言語",
                  "type":[
                     "null",
                     "string"
                  ]
               }
            },
            "required":[
               "subitem_title"
            ],
            "type":"object"
         },
       ...
      }
   },
   "table_row":[
      "item_1617186331708",
      ...
   ],
   "table_row_map":{
      "action":"upt",
      "form":[
         {
            "format":"yyyy-MM-dd",
            "key":"pubdate",
            "required":true,
            "templateUrl":"/static/templates/weko_deposit/datepicker.html",
            "title":"PubDate",
            "title_i18n":{
               "en":"PubDate",
               "ja":"公開日"
            },
            "type":"template"
         },
         {
            "add":"New",
            "items":[
               {
                  "isHide":true,
                  "isNonDisplay":true,
                  "isShowList":true,
                  "isSpecifyNewline":true,
                  "key":"item_1617186331708[].subitem_title",
                  "required":true,
                  "title":"タイトル",
                  "title_i18n":{
                     "en":"Title",
                     "ja":"タイトル"
                  },
                  "type":"text"
               },
               {
                  "key":"item_1617186331708[].subitem_title_language",
                  "title":"言語",
                  "titleMap":[
                     {
                        "name":"ja",
                        "value":"ja"
                     },
                     {
                        "name":"ja-Kana",
                        "value":"ja-Kana"
                     },
                     {
                        "name":"ja-Latn",
                        "value":"ja-Latn"
                     }
                  ],
                  "title_i18n":{
                     "en":"Language",
                     "ja":"言語"
                  },
                  "type":"select"
               }
            ],
            "key":"item_1617186331708",
            "style":{
               "add":"btn-success"
            },
            "title":"Title",
            "title_i18n":{
               "en":"Title",
               "ja":"タイトル"
            }
         },
         ...
         {
            "items":[
               {
                  "key":"parentkey.subitem_systemidt_identifier",
                  "title":"SYSTEMIDT Identifier",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemidt_identifier_type",
                  "title":"SYSTEMIDT Identifier Type",
                  "titleMap":[
                     {
                        "name":"DOI",
                        "value":"DOI"
                     },
                     {
                        "name":"HDL",
                        "value":"HDL"
                     },
                     {
                        "name":"URI",
                        "value":"URI"
                     }
                  ],
                  "type":"select"
               }
            ],
            "key":"system_identifier_doi",
            "title":"Persistent Identifier(DOI)",
            "title_i18n":{
               "en":"Persistent Identifier(DOI)",
               "ja":"永続識別子（DOI）"
            },
            "type":"fieldset"
         },
         {
            "items":[
               {
                  "key":"parentkey.subitem_systemidt_identifier",
                  "title":"SYSTEMIDT Identifier",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemidt_identifier_type",
                  "title":"SYSTEMIDT Identifier Type",
                  "titleMap":[
                     {
                        "name":"DOI",
                        "value":"DOI"
                     },
                     {
                        "name":"HDL",
                        "value":"HDL"
                     },
                     {
                        "name":"URI",
                        "value":"URI"
                     }
                  ],
                  "type":"select"
               }
            ],
            "key":"system_identifier_hdl",
            "title":"Persistent Identifier(HDL)",
            "title_i18n":{
               "en":"Persistent Identifier(HDL)",
               "ja":"永続識別子（HDL）"
            },
            "type":"fieldset"
         },
         {
            "items":[
               {
                  "key":"parentkey.subitem_systemidt_identifier",
                  "title":"SYSTEMIDT Identifier",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemidt_identifier_type",
                  "title":"SYSTEMIDT Identifier Type",
                  "titleMap":[
                     {
                        "name":"DOI",
                        "value":"DOI"
                     },
                     {
                        "name":"HDL",
                        "value":"HDL"
                     },
                     {
                        "name":"URI",
                        "value":"URI"
                     }
                  ],
                  "type":"select"
               }
            ],
            "key":"system_identifier_uri",
            "title":"Persistent Identifier(URI)",
            "title_i18n":{
               "en":"Persistent Identifier(URI)",
               "ja":"永続識別子（URI）"
            },
            "type":"fieldset"
         },
         {
            "items":[
               {
                  "add":"New",
                  "items":[
                     {
                        "key":"parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_label",
                        "title":"SYSTEMFILE Filename Label",
                        "type":"text"
                     },
                     {
                        "key":"parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_type",
                        "title":"SYSTEMFILE Filename Type",
                        "titleMap":[
                           {
                              "name":"Abstract",
                              "value":"Abstract"
                           },
                           {
                              "name":"Fulltext",
                              "value":"Fulltext"
                           },
                           {
                              "name":"Summary",
                              "value":"Summary"
                           },
                           {
                              "name":"Thumbnail",
                              "value":"Thumbnail"
                           },
                           {
                              "name":"Other",
                              "value":"Other"
                           }
                        ],
                        "type":"select"
                     },
                     {
                        "key":"parentkey.subitem_systemfile_filename[].subitem_systemfile_filename_uri",
                        "title":"SYSTEMFILE Filename URI",
                        "type":"text"
                     }
                  ],
                  "key":"parentkey.subitem_systemfile_filename",
                  "style":{
                     "add":"btn-success"
                  },
                  "title":"SYSTEMFILE Filename"
               },
               {
                  "key":"parentkey.subitem_systemfile_mimetype",
                  "title":"SYSTEMFILE MimeType",
                  "type":"text"
               },
               {
                  "key":"parentkey.subitem_systemfile_size",
                  "title":"SYSTEMFILE Size",
                  "type":"text"
               },
               {
                  "add":"New",
                  "items":[
                     {
                        "format":"yyyy-MM-dd",
                        "key":"parentkey.subitem_systemfile_datetime[].subitem_systemfile_datetime_date",
                        "templateUrl":"/static/templates/weko_deposit/datepicker.html",
                        "title":"SYSTEMFILE DateTime Date",
                        "type":"template"
                     },
                     {
                        "key":"parentkey.subitem_systemfile_datetime[].subitem_systemfile_datetime_type",
                        "title":"SYSTEMFILE DateTime Type",
                        "titleMap":[
                           {
                              "name":"Accepted",
                              "value":"Accepted"
                           },
                           {
                              "name":"Available",
                              "value":"Available"
                           },
                           {
                              "name":"Collected",
                              "value":"Collected"
                           },
                           {
                              "name":"Copyrighted",
                              "value":"Copyrighted"
                           },
                           {
                              "name":"Created",
                              "value":"Created"
                           },
                           {
                              "name":"Issued",
                              "value":"Issued"
                           },
                           {
                              "name":"Submitted",
                              "value":"Submitted"
                           },
                           {
                              "name":"Updated",
                              "value":"Updated"
                           },
                           {
                              "name":"Valid",
                              "value":"Valid"
                           }
                        ],
                        "type":"select"
                     }
                  ],
                  "key":"parentkey.subitem_systemfile_datetime",
                  "style":{
                     "add":"btn-success"
                  },
                  "title":"SYSTEMFILE DateTime"
               },
               {
                  "key":"parentkey.subitem_systemfile_version",
                  "title":"SYSTEMFILE Version",
                  "type":"text"
               }
            ],
            "key":"system_file",
            "title":"File Information",
            "title_i18n":{
               "en":"File Information",
               "ja":"ファイル情報"
            },
            "type":"fieldset"
         }
      ],
      "mapping":{
         "item_1617186331708":{
            "display_lang_type":"",
            "jpcoar_mapping":{
               "title":{
                  "@attributes":{
                     "xml:lang":"subitem_title_language"
                  },
                  "@value":"subitem_title"
               }
            },
            "jpcoar_v1_mapping":{
               "title":{
                  "@attributes":{
                     "xml:lang":"subitem_title_language"
                  },
                  "@value":"subitem_title"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "title":{
                  "@value":"subitem_title"
               }
            },
            "spase_mapping":""
         },
        ...
         "pubdate":{
            "display_lang_type":"",
            "jpcoar_mapping":"",
            "jpcoar_v1_mapping":"",
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":"",
            "spase_mapping":""
         },
         "system_file":{
            "display_lang_type":"",
            "jpcoar_mapping":{
               "system_file":{
                  "URI":{
                     "@attributes":{
                        "label":"subitem_systemfile_filename_label",
                        "objectType":"subitem_systemfile_filename_type"
                     },
                     "@value":"subitem_systemfile_filename_uri"
                  },
                  "date":{
                     "@attributes":{
                        "dateType":"subitem_systemfile_datetime_type"
                     },
                     "@value":"subitem_systemfile_datetime_date"
                  },
                  "extent":{
                     "@value":"subitem_systemfile_size"
                  },
                  "mimeType":{
                     "@value":"subitem_systemfile_mimetype"
                  },
                  "version":{
                     "@value":"subitem_systemfile_version"
                  }
               }
            },
            "jpcoar_v1_mapping":{
               "system_file":{
                  "URI":{
                     "@attributes":{
                        "label":"subitem_systemfile_filename_label",
                        "objectType":"subitem_systemfile_filename_type"
                     },
                     "@value":"subitem_systemfile_filename_uri"
                  },
                  "date":{
                     "@attributes":{
                        "dateType":"subitem_systemfile_datetime_type"
                     },
                     "@value":"subitem_systemfile_datetime_date"
                  },
                  "extent":{
                     "@value":"subitem_systemfile_size"
                  },
                  "mimeType":{
                     "@value":"subitem_systemfile_mimetype"
                  },
                  "version":{
                     "@value":"subitem_systemfile_version"
                  }
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":"",
            "spase_mapping":""
         },
         "system_identifier_doi":{
            "ddi_mapping":{
               "stdyDscr":{
                  "citation":{
                     "holdings":{
                        "@attributes":{
                           "URI":"subitem_systemidt_identifier"
                        }
                     }
                  }
               }
            },
            "display_lang_type":"",
            "jpcoar_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "jpcoar_v1_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "identifier":{
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "spase_mapping":""
         },
         "system_identifier_hdl":{
            "ddi_mapping":{
               "stdyDscr":{
                  "citation":{
                     "holdings":{
                        "@attributes":{
                           "URI":"subitem_systemidt_identifier"
                        }
                     }
                  }
               }
            },
            "display_lang_type":"",
            "jpcoar_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "jpcoar_v1_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "identifier":{
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "spase_mapping":""
         },
         "system_identifier_uri":{
            "ddi_mapping":{
               "stdyDscr":{
                  "citation":{
                     "holdings":{
                        "@attributes":{
                           "URI":"subitem_systemidt_identifier"
                        }
                     }
                  }
               }
            },
            "display_lang_type":"",
            "jpcoar_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "jpcoar_v1_mapping":{
               "identifier":{
                  "@attributes":{
                     "identifierType":"subitem_systemidt_identifier_type"
                  },
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "junii2_mapping":"",
            "lido_mapping":"",
            "lom_mapping":"",
            "oai_dc_mapping":{
               "identifier":{
                  "@value":"subitem_systemidt_identifier"
               }
            },
            "spase_mapping":""
         }
      },
      "name":"デフォルトアイテムタイプ（フル）",
      "schema":{
         "$schema":"http://json-schema.org/draft-04/schema#",
         "description":"",
         "properties":{
            "item_1617186331708":{
               "items":{
                  "properties":{
                     "subitem_title":{
                        "format":"text",
                        "title":"タイトル",
                        "title_i18n":{
                           "en":"Title",
                           "ja":"タイトル"
                        },
                        "type":"string"
                     },
                     "subitem_title_language":{
                        "currentEnum":[
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
                        "enum":[
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
                        "format":"select",
                        "title":"言語",
                        "type":[
                           "null",
                           "string"
                        ]
                     }
                  },
                  "required":[
                     "subitem_title"
                  ],
                  "type":"object"
               },
               "maxItems":"9999",
               "minItems":"1",
               "title":"Title",
               "type":"array"
            },
            ...
            "pubdate":{
               "format":"datetime",
               "title":"PubDate",
               "type":"string"
            },
            "system_file":{
               "format":"object",
               "properties":{
                  "subitem_systemfile_datetime":{
                     "format":"array",
                     "items":{
                        "format":"object",
                        "properties":{
                           "subitem_systemfile_datetime_date":{
                              "format":"datetime",
                              "title":"SYSTEMFILE DateTime Date",
                              "type":"string"
                           },
                           "subitem_systemfile_datetime_type":{
                              "enum":[
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
                              "format":"select",
                              "title":"SYSTEMFILE DateTime Type",
                              "type":"string"
                           }
                        },
                        "type":"object"
                     },
                     "title":"SYSTEMFILE DateTime",
                     "type":"array"
                  },
                  "subitem_systemfile_filename":{
                     "format":"array",
                     "items":{
                        "format":"object",
                        "properties":{
                           "subitem_systemfile_filename_label":{
                              "format":"text",
                              "title":"SYSTEMFILE Filename Label",
                              "type":"string"
                           },
                           "subitem_systemfile_filename_type":{
                              "enum":[
                                 "Abstract",
                                 "Fulltext",
                                 "Summary",
                                 "Thumbnail",
                                 "Other"
                              ],
                              "format":"select",
                              "title":"SYSTEMFILE Filename Type",
                              "type":"string"
                           },
                           "subitem_systemfile_filename_uri":{
                              "format":"text",
                              "title":"SYSTEMFILE Filename URI",
                              "type":"string"
                           }
                        },
                        "type":"object"
                     },
                     "title":"SYSTEMFILE Filename",
                     "type":"array"
                  },
                  "subitem_systemfile_mimetype":{
                     "format":"text",
                     "title":"SYSTEMFILE MimeType",
                     "type":"string"
                  },
                  "subitem_systemfile_size":{
                     "format":"text",
                     "title":"SYSTEMFILE Size",
                     "type":"string"
                  },
                  "subitem_systemfile_version":{
                     "format":"text",
                     "title":"SYSTEMFILE Version",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"File Information",
               "type":"object"
            },
            "system_identifier_doi":{
               "format":"object",
               "properties":{
                  "subitem_systemidt_identifier":{
                     "format":"text",
                     "title":"SYSTEMIDT Identifier",
                     "type":"string"
                  },
                  "subitem_systemidt_identifier_type":{
                     "currentEnum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "enum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "format":"select",
                     "title":"SYSTEMIDT Identifier Type",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"Persistent Identifier(DOI)",
               "type":"object"
            },
            "system_identifier_hdl":{
               "format":"object",
               "properties":{
                  "subitem_systemidt_identifier":{
                     "format":"text",
                     "title":"SYSTEMIDT Identifier",
                     "type":"string"
                  },
                  "subitem_systemidt_identifier_type":{
                     "currentEnum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "enum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "format":"select",
                     "title":"SYSTEMIDT Identifier Type",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"Persistent Identifier(HDL)",
               "type":"object"
            },
            "system_identifier_uri":{
               "format":"object",
               "properties":{
                  "subitem_systemidt_identifier":{
                     "format":"text",
                     "title":"SYSTEMIDT Identifier",
                     "type":"string"
                  },
                  "subitem_systemidt_identifier_type":{
                     "currentEnum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "enum":[
                        "DOI",
                        "HDL",
                        "URI"
                     ],
                     "format":"select",
                     "title":"SYSTEMIDT Identifier Type",
                     "type":"string"
                  }
               },
               "system_prop":true,
               "title":"Persistent Identifier(URI)",
               "type":"object"
            }
         },
         "required":[
            "pubdate",
            "item_1617186331708",
            ...
         ],
         "type":"object"
      }
   },
   "upload_file":false
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
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>
