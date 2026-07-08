# JDCat Master Data Migration Program — User Manual

Target system: Weko3 (JDCat instance)
Target work: Master data migration for the version upgrade from the develop_v1.0.8 line (＋ JDCat-specific support `feature/jdcat_202601`) to develop_v2.0.0

| Item | Content |
|---|---|
| Requirement specification | Requirement Spec: J2026-01_v4.docx |
| Design document | [JDCat Master Data Migration Program — Design Document](JDCat_Master_Data_Migration_Design_Spec.md) |
| Related material (appendix) | [別紙_v3.xlsx](attachments/別紙_v3.xlsx) (provided by NII. Contains 別紙1–3 in separate sheets) |
| Japanese version | [利用者マニュアル（日本語）](JDCat_Master_Data_Migration_Tool_Manual.md) |

This document summarizes the **operating procedures for end users** of the migration program set (`scripts/demo/jdcat_migration/`). For the detailed design rationale and processing internals, refer to the [Design Document](JDCat_Master_Data_Migration_Design_Spec.md). This manual centers on **Chapter 5, "Program Structure"** of the design document, describing the concrete execution method for each tool.

---

# 1. What this program does

It performs **migration of master data (`item_type` / `item_type_property` / `item_type_mapping`)** required when upgrading JDCat (Weko3) from the `develop_v1.0.8` line to `develop_v2.0.0`.

- Target item types are **12 (Multiple) / 20 (Harvesting DDI)** only.
- The conversion rules are consolidated into an external configuration file `mapping_config.json` — a **configuration-driven** design.
- A **non-destructive**, re-runnable, **idempotent** design that does **not** TRUNCATE `item_type_property`.
- **Registered metadata (`item_metadata` / `records_metadata`) is not converted.** After migration, metadata in v2.0.0 structure is regenerated via **re-harvesting** through OAI-PMH / ResourceSync (Design Document 2.4).

> ⚠️ **Note**: This program handles master data only. Metadata re-acquisition (re-harvesting) is out of scope for this program and is performed separately after migration completes.

---

# 2. Prerequisites and Execution Environment

## 2.1 Where to run

The migration core (`migrate.py`) and the development-support tool (`gen_properties.py`) are run **inside the Weko web container** via `invenio shell`. The configuration-file generator (`convert_xlsx.py`) is **DB-independent and stdlib-only**, so it can also run with plain `python3` outside the container.

| Tool | Where to run | DB connection |
|---|---|---|
| `convert_xlsx.py` | Anywhere (plain `python3` is fine) | Not required |
| `gen_properties.py` | Inside web container (`invenio shell`) | Required (development only) |
| `migrate.py` | Inside web container (`invenio shell`) | Required |

## 2.2 Placement of the program

Place the migration program set under `scripts/demo/jdcat_migration/` of the Weko main body (visible from the web container as `/code/scripts/demo/jdcat_migration/`).

```
scripts/demo/jdcat_migration/
  __init__.py
  config.py          # Loads / schema-validates / consistency-checks mapping_config.json
  convert_xlsx.py    # xlsx answers -> mapping_config.json
  gen_properties.py  # DB -> properties/*.py draft generation (development)
  engine.py          # Conversion engine core (Phases 1-3)
  migrate.py         # CLI entry point (run from invenio shell)
  report.py          # dry-run / progress / post-verification report
```

## 2.3 [Important] `invenio shell` and how to pass arguments

The actual implementation of `invenio shell` is **IPython**, which **intercepts `--` flags such as `--config` itself** (they never reach the script). For this reason, `migrate.py` / `gen_properties.py`, which are run via `invenio shell`, **pass arguments through environment variables (`JDCAT_*`)** (IPython does not touch environment variables).

- Via `invenio shell` (the production method) → **pass via environment variables** (`docker compose exec -e ...`).
- Plain `python` execution (development, requires a separately prepared app context) → `--` flags can be used.

The command examples below follow this premise.

---

# 3. Overall flow

```
[1] convert_xlsx.py  ... filled-in xlsx -> generate mapping_config.json
        |
       (only when needed)
[2] gen_properties.py ... generate properties/*.py drafts for new properties (development)
        |
[3] Preparation      ... take a DB backup (pg_dump etc., manual)
        |
[4] migrate.py --dry-run ... pre-check intended changes without updating the DB
        |
[5] migrate.py (real run) ... apply Phases 1-3
        |
[6] Check the report ... confirm overall judgment / 0 remaining old keys / 0 unknown property references
```

- **[2] can normally be skipped.** Use it only during development when you want to create draft `.py` files for new properties (Design Document 4.2).
- **[3][4] must always be performed before the real run** (Design Document 5.3).

---

# 4. Execution methods

## 4.1 convert_xlsx.py (filled-in xlsx -> generate config JSON)

Converts `マッピング必要データ_XXXXXXXX.xlsx`, filled in by NII, into `mapping_config.json`, which is the actual input to the migration program.

### Input / Output

- **Input**: filled-in `マッピング必要データ_XXXXXXXX.xlsx` (`item` / `property` sheets)
- **Output**: `mapping_config.json` (schema in Design Document 3.2)

### Command

Because it is DB-independent and stdlib-only, it can run standalone with plain `python3`.

```bash
python3 convert_xlsx.py マッピング必要データ_20260423.xlsx mapping_config.json \
    --item-types 12,20
```

| Argument | Description |
|---|---|
| 1st arg (`input`) | filled-in `マッピング必要データ_*.xlsx` (required) |
| 2nd arg (`output`) | path of the `mapping_config.json` to output (required) |
| `--item-types` | target item types (comma-separated; default `12,20`) |

### Checking output and warnings

- Processing results and warnings are written to standard error. On success, the last line shows `OK: ... を出力（property_id_map N件 / item_key_map {...}）`.
- Unfilled cells (`#N/A`) and inconsistencies (old/new id not an integer, prop_name not in identifier form, duplicate keys, etc.) are emitted as `[WARN]`; fatal problems such as a missing sheet or missing header are emitted as `[ERROR]`. **If there is any `[ERROR]`, conversion fails and returns exit code 1.** Review the warnings and, if needed, fix the xlsx and re-run.

> The generated `mapping_config.json` is an operational artifact and is not managed in the Weko repository. The migration core (`migrate.py`) operates by referencing only this JSON.

<br/>

## 4.2 gen_properties.py (property definition .py draft generation — development)

A **development-time helper tool** that generates draft `.py` files with the same contract as existing `properties/*.py`, using the current DB `item_type_property` as templates. It replaces subitem keys with a conversion map during generation. **It is not used by the migration core (Phases 1-3).**

> ℹ️ **In normal operation, you do not need to use this tool.** When properties already exist in the standard set, use the existing `properties/*.py`. The main use of this tool is draft generation for "new" properties, and its output is only a **starting draft** (assumed to be manually corrected/verified against 別紙2 and 別紙3) (Design Document 4.2).

### Input / Output

- **Input**: DB connection, target property_ids, subitem-key conversion map (optional), output directory
- **Output**: draft `.py` in the same style as `properties/*.py` (UTF-8). Since `mapping` is not in the DB, `DEFAULT_MAPPING` is placed as a placeholder.

### Command (via invenio shell — environment-variable input)

```bash
docker compose exec \
    -e JDCAT_GEN_IDS=1042,305 \
    -e JDCAT_GEN_OUT=scripts/demo/jdcat_migration/_gen \
    -e JDCAT_GEN_SUBITEM=scripts/demo/jdcat_migration/subitem_map.json \
    web invenio shell scripts/demo/jdcat_migration/gen_properties.py
```

| Environment variable | Description |
|---|---|
| `JDCAT_GEN_IDS` | property_ids to generate (comma-separated; **required**) |
| `JDCAT_GEN_OUT` | output directory (**required**; created if it does not exist) |
| `JDCAT_GEN_SUBITEM` | subitem-key conversion map (`.json` = `{old:new}` or `.xlsx`). Optional |
| `JDCAT_GEN_SUBITEM_SHEET` | sheet name for xlsx (default `subitem`) |

### Work after generation

1. The head of each generated `.py` carries `★GENERATED DRAFT（要手修正）★` (generated draft — requires manual correction).
2. Because `mapping` / `name_en` / `multiple_flag` cannot be determined from the DB, **manually correct and verify** them against 別紙2 and 別紙3.
3. Place the finalized `.py` under `properties/` and register it in `properties/__init__.py`; it will then be **registered automatically in Phase 1 of `migrate.py`**.
4. As an aid, diffing the generated output against the existing standard `properties/*.py` reveals the gap between "current DB structure vs. v2.0.0 standard".

<br/>

## 4.3 migrate.py (migration core)

Using `mapping_config.json` as input, migrates the master data of the target item types (12/20) to the v2.0.0 form.

### 4.3.1 Preparation before the run (Design Document 5.3)

Before the real run, always perform the following as operational steps.

1. **Take a DB backup** (manual; out of scope for this program): take the target tables (`item_type` / `item_type_mapping` / `item_type_property`) with `pg_dump` etc. Restore from here if something goes wrong.
2. **Pre-check with dry-run** (next section): confirm config-JSON validation and intended changes without updating the DB.

### 4.3.2 dry-run (pre-check without DB update)

Always confirm the intended changes with a dry-run first.

```bash
docker compose exec \
    -e JDCAT_CONFIG=scripts/demo/jdcat_migration/mapping_config.json \
    -e JDCAT_ITEM_TYPES=12,20 \
    -e JDCAT_PHASE=all \
    -e JDCAT_DRY_RUN=1 \
    web invenio shell scripts/demo/jdcat_migration/migrate.py
```

### 4.3.3 Real run

If there are no problems in the dry-run output, remove `JDCAT_DRY_RUN` (or set it to `0`) and perform the real run.

```bash
docker compose exec \
    -e JDCAT_CONFIG=scripts/demo/jdcat_migration/mapping_config.json \
    -e JDCAT_ITEM_TYPES=12,20 \
    -e JDCAT_PHASE=all \
    web invenio shell scripts/demo/jdcat_migration/migrate.py
```

### 4.3.4 List of environment variables

| Environment variable | Description |
|---|---|
| `JDCAT_CONFIG` | path to the config JSON (`mapping_config.json`) (**required**) |
| `JDCAT_ITEM_TYPES` | target item types (comma-separated; default is the config's `target_item_types`) |
| `JDCAT_PHASE` | execution phase `all` / `1` / `2` / `3` / `pre` (default `all`) |
| `JDCAT_DRY_RUN` | `1`/`true`/`yes` for dry-run (no DB update) |
| `JDCAT_CLEANUP` | `1`/`true`/`yes` for Phase 3 logical deletion (opt-in) |
| `JDCAT_REPORT_OUT` | report output file (standard output / log if unspecified) |

- `pre` of `JDCAT_PHASE` performs only pre-run validation (config JSON × DB). `1`/`2`/`3` run each phase individually.
- `JDCAT_CLEANUP` logically deletes (`delflg=true`) JDCat-specific properties that are no longer referenced by any item type. It is not performed by default (opt-in).

### 4.3.5 Overview of processing phases (Design Document Chapter 6)

| Phase | Content |
|---|---|
| Phase 1 | properties (non-destructive UPSERT). Updates v2.0.0 standard properties from the `properties/` definitions via UPDATE. JDCat-specific properties are left in place. |
| Phase 2 | itemtype. Replaces `cus_<old id>` -> `cus_<new id>` in `render` (③), replaces old item keys -> new item keys (①), and reflects property definitions via `ItemTypes.reload()`. |
| Phase 3 | verify & cleanup. Verifies 0 remaining old keys and 0 unknown property references. (Opt-in: logically deletes specific properties.) |

- `migrate.py` wraps the entire run in try/finally, temporarily removing and then restoring the `Timestamp.before_update` listener of `weko_records` (to avoid dirtying the `updated` column of the master tables).

### 4.3.6 Plain python execution (development only)

In a development environment where an app context can be prepared separately, `--` flags can be used.

```bash
python migrate.py --config mapping_config.json --item-types 12,20 \
    --phase all --dry-run
```

| Argument | Corresponding environment variable |
|---|---|
| `--config` | `JDCAT_CONFIG` |
| `--item-types` | `JDCAT_ITEM_TYPES` |
| `--phase` | `JDCAT_PHASE` |
| `--dry-run` | `JDCAT_DRY_RUN` |
| `--cleanup` | `JDCAT_CLEANUP` |
| `--report-out` | `JDCAT_REPORT_OUT` |

---

# 5. How to read the report

After execution, `migrate.py` outputs a text report (to a file when `JDCAT_REPORT_OUT` is specified, otherwise to standard output / log). The main points to check are as follows.

- **Mode**: whether `dry-run（DB無更新）` (no DB update) or `本実行` (real run).
- **Pre-run validation (config JSON × DB)**: if there is any `[ERROR]`, the migration is aborted. Review any `[WARN]`.
- **Phase 1**: number of UPSERT targets (add / update). If there are none, "対象なし" (no target) is stated explicitly.
- **Phase 2**: per item type, the count of ③ (property ID conversion) and ① (item-key conversion), and the `reload` result code. A "変換済み/冪等スキップ" (already converted / idempotent skip) note means it has already been migrated.
- **Phase 3**: per item type, `OK`/`NG`, the **number of remaining old keys** and the **number of unknown property references**. Both 0 and `OK` is normal.
- **Overall judgment**: at the end, `dry-run 完了` / `本実行 完了` (dry-run / real run complete) is shown together with "問題は検出されませんでした" (no problems detected) or items requiring attention.

> ✅ Signs of a successful migration: the overall judgment says "問題は検出されませんでした", and Phase 3 is `OK` for all item types (0 remaining old keys, 0 unknown property references).

---

# 6. Re-run and handling of trouble (Design Document Chapter 7)

- **Idempotent**: Phase 1 uses UPDATE, and Phase 2 skips based on determining "already converted" by key format, so it is **safe to run any number of times**. Proceed in the order dry-run -> real run.
- **Rollback on error**: if an error occurs during processing, that transaction is rolled back and the DB is kept in its pre-change state. Ordinary errors are recovered this way and can be continued with an idempotent re-run (no restore needed).
- **Restore from backup**: a **last resort** for **unexpected situations** (inconsistency after a partial commit, data corruption, etc.) that cannot be recovered by transaction rollback or re-run. Restore from the backup taken in advance (4.3.1).

---

# 7. Work after migration

- After the master-data migration completes, **metadata is re-acquired in v2.0.0 structure via re-harvesting through OAI-PMH / ResourceSync** (out of scope for this program; Design Document 2.4).
- Note that the migration core focuses on preparing the master data (`item_type` definitions, mapping, properties) and does not perform per-record metadata conversion.
