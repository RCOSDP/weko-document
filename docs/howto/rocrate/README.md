# 

## install

```
git clone https://github.com/crs4/rocrate-validator.git
cd rocrate-validator
poetry install
```

## validate 

```
{
   "@context": [
      "https://w3id.org/ro/crate/1.1/context",
      {
         "name_en": "http://schema.org/name"
      },
      {
         "name_ja": "http://schema.org/name"
      }
   ],
   "@graph": [
      {
         "@type": "CreativeWork",
         "@id": "ro-crate-metadata.json",
         "conformsTo": {
            "@id": "https://w3id.org/ro/crate/1.1"
         },
         "about": {
            "@id": "./"
         }
      },
      {
         "@id": "./",
         "identifier": "https://doi.org/10.4225/59/59672c09f4a4b",
         "@type": "Dataset",
         "datePublished": "2017",
         "name": "Data files associated with the manuscript:Effects of facilitated family case conferencing for ...",
         "description": "Palliative care planning for nursing home residents with advanced dementia ...",
         "license": {
            "@id": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/"
         }
      },
      {
         "@id": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/",
         "@type": "CreativeWork",
         "description": "This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Australia License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/au/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.",
         "identifier": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/",
         "name": "Attribution-NonCommercial-ShareAlike 3.0 Australia (CC BY-NC-SA 3.0 AU)"
      }
   ]
}
```

```
$ poetry run rocrate-validator validate -p ro-crate-1.1 -v --no-paging -f json ../rocrate/example3
```

```
$ poetry run rocrate-validator validate -p ro-crate-1.1 -v --no-paging -f json ../rocrate/example3
{
    "meta": {
        "version": "0.1"
    },
    "validation_settings": {
        "profile_identifier": "ro-crate-1.1",
        "enable_profile_inheritance": true,
        "abort_on_first": false,
        "requirement_severity": "REQUIRED",
        "rocrate_validator_version": "0.5.0_fa8c6c7+401-dirty"
    },
    "passed": true,
    "issues": []
}
```

## 

```
{
   "@context": [
      "https://w3id.org/ro/crate/1.1/context",
      {
         "name": {"@id": "name","@container": "@language"}
      }
   ],
   "@graph": [
      {
         "@type": "CreativeWork",
         "@id": "ro-crate-metadata.json",
         "conformsTo": {
            "@id": "https://w3id.org/ro/crate/1.1"
         },
         "about": {
            "@id": "./"
         }
      },
      {
         "@id": "./",
         "identifier": "https://doi.org/10.4225/59/59672c09f4a4b",
         "@type": "Dataset",
         "datePublished": "2017",
         "name": {
            "ja":"名前",
            "en":"Name"
         },
         "description": "Palliative care planning for nursing home residents with advanced dementia ...",
         "license": {
            "@id": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/"
         }
      },
      {
         "@id": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/",
         "@type": "CreativeWork",
         "description": "This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Australia License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/au/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.",
         "identifier": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/",
         "name": "Attribution-NonCommercial-ShareAlike 3.0 Australia (CC BY-NC-SA 3.0 AU)"
      }
   ]
}
```

```
$ poetry run rocrate-validator validate -p ro-crate-1.1 -v --no-paging -f json ../rocrate/example3
{
    "meta": {
        "version": "0.1"
    },
    "validation_settings": {
        "profile_identifier": "ro-crate-1.1",
        "enable_profile_inheritance": true,
        "abort_on_first": false,
        "requirement_severity": "REQUIRED",
        "rocrate_validator_version": "0.5.0_fa8c6c7+401-dirty"
    },
    "passed": false,
    "issues": [
        {
            "severity": "REQUIRED",
            "message": "RO-Crate file descriptor \"ro-crate-metadata.json\" is not fully flattened at entity \"./\"",
            "violatingEntity": null,
            "violatingProperty": null,
            "violatingPropertyValue": null,
            "check": {
                "identifier": "ro-crate-1.1_2.2",
                "label": "REQUIRED 2.2",
                "order": 2,
                "name": "File Descriptor JSON-LD must be flattened",
                "description": "Check if the file descriptor is flattened",
                "severity": "REQUIRED",
                "requirement": {
                    "identifier": "ro-crate-1.1_2",
                    "name": "File Descriptor JSON-LD format",
                    "description": "The file descriptor MUST be a valid JSON-LD file",
                    "order": 2,
                    "profile": {
                        "identifier": "ro-crate-1.1",
                        "uri": "https://w3id.org/ro/crate/1.1",
                        "name": "RO-Crate Metadata Specification 1.1",
                        "description": "RO-Crate Metadata Specification."
                    }
                }
            }
        },
        {
            "severity": "REQUIRED",
            "message": "The Root Data Entity MUST have a `name` property (as specified by schema.org)",
            "violatingEntity": "./",
            "violatingProperty": "http://schema.org/name",
            "violatingPropertyValue": null,
            "check": {
                "identifier": "ro-crate-1.1_8.1",
                "label": "MUST 8.1",
                "order": 1,
                "name": "Root Data Entity: `name` property",
                "description": "Check if the Root Data Entity includes a `name` (as specified by schema.org) \n to clearly identify the dataset and distinguish it from other datasets.",
                "severity": "REQUIRED",
                "requirement": {
                    "identifier": "ro-crate-1.1_8",
                    "name": "RO-Crate Root Data Entity REQUIRED properties",
                    "description": "The Root Data Entity MUST have a `name`, `description`, `license` and `datePublished`",
                    "order": 8,
                    "profile": {
                        "identifier": "ro-crate-1.1",
                        "uri": "https://w3id.org/ro/crate/1.1",
                        "name": "RO-Crate Metadata Specification 1.1",
                        "description": "RO-Crate Metadata Specification."
                    }
                }
            }
        }
    ]
}
```

##

```
{
   "@context": [
      "https://w3id.org/ro/crate/1.1/context",
      {"name_ja":{"@id": "name","@language":"ja"}},
      {"name_en":{"@id": "name","@language":"en"}}
   ],
   "@graph": [
      {
         "@type": "CreativeWork",
         "@id": "ro-crate-metadata.json",
         "conformsTo": {
            "@id": "https://w3id.org/ro/crate/1.1"
         },
         "about": {
            "@id": "./"
         }
      },
      {
         "@id": "./",
         "identifier": "https://doi.org/10.4225/59/59672c09f4a4b",
         "@type": "Dataset",
         "datePublished": "2017",
         "name_ja":"名前",
         "name_en":"Name",
         "description": "Palliative care planning for nursing home residents with advanced dementia ...",
         "license": {
            "@id": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/"
         }
      },
      {
         "@id": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/",
         "@type": "CreativeWork",
         "description": "This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Australia License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/au/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.",
         "identifier": "https://creativecommons.org/licenses/by-nc-sa/3.0/au/",
         "name": "Attribution-NonCommercial-ShareAlike 3.0 Australia (CC BY-NC-SA 3.0 AU)"
      }
   ]
}
```

```
$ poetry run rocrate-validator validate -p ro-crate-1.1 -v --no-paging -f json ../rocrate/example3
{
    "meta": {
        "version": "0.1"
    },
    "validation_settings": {
        "profile_identifier": "ro-crate-1.1",
        "enable_profile_inheritance": true,
        "abort_on_first": false,
        "requirement_severity": "REQUIRED",
        "rocrate_validator_version": "0.5.0_fa8c6c7+401-dirty"
    },
    "passed": true,
    "issues": []
}
```