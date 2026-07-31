#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MODULE_INDEX.md（モジュール逆引きリファレンス）を再生成するスクリプト。

各機能仕様（spec/base/**/*.md）の「関連モジュール」節を機械集計し、
モジュール → 機能仕様の逆引きリンクを含む spec/base/MODULE_INDEX.md を生成する。

使い方:
    python3 spec/tools/generate_module_index.py
    # WEKO 実装の場所を変える場合:
    WEKO_ROOT=/path/to/weko python3 spec/tools/generate_module_index.py

前提:
    - WEKO_ROOT/modules/ に実モジュール群があること（モジュール名の正）。
    - spec/base/ に機能仕様があること。
出力:
    - spec/base/MODULE_INDEX.md を上書き生成。

備考:
    - モジュールの1行説明（DESC）は人手で維持する（実ソースの docstring は定型的で
      説明として不足するため）。新規モジュール追加時は DESC / NON_MODULE に追記する。
    - 逆引きは「関連モジュール」節での明示参照(strong)と、本文中の言及(weak)を区別する。
"""
import os
import re
import glob

# --- パス設定 -------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))          # .../docs/spec/tools
SPEC_BASE = os.path.normpath(os.path.join(HERE, "..", "base"))
WEKO_ROOT = os.environ.get("WEKO_ROOT", "/home/mhaya/weko")
MODULES_DIR = os.path.join(WEKO_ROOT, "modules")
TARGET = os.path.join(SPEC_BASE, "MODULE_INDEX.md")

# --- モジュール1行説明（人手で維持） --------------------------------------
DESC = {
    "invenio-accounts": "ユーザ管理・認証の基盤（ログイン／セッション／ロール）。Flask-Security/Flask-Login ベース。",
    "invenio-communities": "コミュニティ（サブリポジトリ）機能の基盤。",
    "invenio-db": "SQLAlchemy によるDB接続・マイグレーション管理の基盤。",
    "invenio-deposit": "レコードの deposit（登録）とファイルアップロードの REST 基盤。",
    "invenio-files-rest": "ファイルのアップロード／ダウンロード REST（バケット／オブジェクト／ロケーション。S3類似API）。",
    "invenio-iiif": "IIIF 画像 API（画像プレビュー／変換）。",
    "invenio-indexer": "レコードの Elasticsearch インデクシング基盤。",
    "invenio-mail": "メール送信の基盤（Flask-Mail ラッパ）。",
    "invenio-oaiharvester": "OAI-PMH ハーベスト（他リポジトリからのメタデータ収集）。",
    "invenio-oaiserver": "OAI-PMH サーバ（メタデータの外部提供）。",
    "invenio-oauth2server": "OAuth2 サーバ（WebAPI のトークン／スコープ管理）。",
    "invenio-previewer": "ファイルプレビューの基盤。",
    "invenio-queues": "メッセージキュー（イベント）管理の基盤。",
    "invenio-records": "メタデータ（レコード）格納の中核基盤。",
    "invenio-records-rest": "レコードの REST API 基盤。",
    "invenio-resourcesyncclient": "ResourceSync クライアント（Resync による外部リソース取り込み）。",
    "invenio-resourcesyncserver": "ResourceSync サーバ（Resource List／Change List の公開）。",
    "invenio-s3": "S3 互換オブジェクトストレージ対応。",
    "invenio-stats": "利用統計の収集・集計基盤（ES の events／aggregations）。",
    "weko-accounts": "WEKO 独自の認証連携（Shibboleth／セキュリティ設定）を invenio-accounts に付加。",
    "weko-admin": "管理画面全般（各種設定／運用統計レポート／ログ解析／サイト情報／メール等）の中核。",
    "weko-authors": "著者DB（著者の編集／一括登録・出力／名寄せ／外部著者ID prefix）。",
    "weko-bulkupdate": "アイテムの一括更新機能。※現状は cookiecutter 雛形のまま実機能を持たない。実際の一括更新は [ADMIN-2-1: 一括更新](admin/ADMIN_2_1.md)（`weko-search-ui` / `weko-index-tree` / `weko-deposit`）が担う。",
    "weko-deposit": "アイテム登録の中核。メタデータ整形と Elasticsearch への投入、ファイル情報の DB 格納を担う（invenio-deposit を拡張）。",
    "weko-gridlayout": "ウェブデザイン管理（ウィジェット／ページレイアウト）。",
    "weko-groups": "ユーザグループの管理（GakuNin mAP 連携によるグループ取込を含む）。",
    "weko-handle": "CNRI Handle による永続識別子の発行。",
    "weko-index-tree": "インデックスツリー（分類階層）の管理・表示・権限判定。",
    "weko-indextree-journal": "インデックスに紐づく雑誌情報の管理。",
    "weko-items-autofill": "メタデータ自動補完（CrossRef／CiNii 等、外部IDからの取得）。",
    "weko-items-ui": "アイテム登録・編集 UI およびエクスポート／インポートの UI。",
    "weko-itemtypes-ui": "アイテムタイプ・メタデータ・マッピング・プロパティ定義の UI。",
    "weko-logging": "ロギング（ファイル／DB）の基盤。",
    "weko-notifications": "COAR Notify 準拠のプッシュ通知（inbox）機能。",
    "weko-plugins": "プラグイン機構（flask_plugins）。",
    "weko-records": "レコード（メタデータ）とアイテムタイプ／マッピングのモデル・API 中核（invenio-records を拡張）。",
    "weko-records-ui": "アイテム詳細表示・ファイル配信・アクセス制御・利用申請入口・引用／統計表示。",
    "weko-redis": "Redis 接続ヘルパ。",
    "weko-schema-ui": "メタデータスキーマ（OAI／JPCOAR 等）とマッピングによる出力生成。",
    "weko-search-ui": "検索結果表示・ファセット・インポート／一括処理・検索設定。",
    "weko-signposting": "FAIR Signposting（アイテム詳細への HTTP Link ヘッダ付与。rel=cite-as／describedby）。",
    "weko-sitemap": "sitemap.xml の生成。",
    "weko-swordserver": "SWORD（v3）によるアイテム受入 API。",
    "weko-theme": "サイトのテーマ・トップページ・共通レイアウト。",
    "weko-user-profiles": "ユーザプロファイル（表示名／所属等）の管理。",
    "weko-workflow": "登録・利用申請等のワークフロー（アクティビティ／フロー／承認／Identifier付与／フィードバックメール）の中核。",
    "weko-workspace": "ワークスペース（簡易アイテム登録／一覧取得／メタデータ自動補完）。",
}

NON_MODULE = {
    "resources": "Python モジュールではない。CNRI Handle サーバ用の証明書・鍵・認証情報を格納。",
    "cookiecutter-weko-module": "新規 weko モジュールを生成するためのテンプレート（スキャフォールド）。",
}

CATLABEL = {
    "user": "ユーザ機能", "admin": "管理機能", "api": "WebAPI",
    "access_control": "アクセスコントロール", "restricted_access": "制限公開",
    "ams": "AMS", "other": "その他/データ構造", "tools": "ツール",
}

heading_re = re.compile(r'^(#{1,6})\s*(.*)$')


def list_modules():
    return sorted(d for d in os.listdir(MODULES_DIR)
                  if os.path.isdir(os.path.join(MODULES_DIR, d)))


def _clean_title(t):
    # inline markdown link [text](url) -> text
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    # leftover brackets / trailing page numbers
    t = t.replace("[", "").replace("]", "")
    t = re.sub(r'\s+\d+$', '', t)
    return t.strip()


def extract_title(lines):
    for ln in lines:
        m = heading_re.match(ln)
        if m and m.group(2).strip():
            return _clean_title(m.group(2))
    return ""


def extract_related_section(lines):
    out = []
    i, n = 0, len(lines)
    while i < n:
        m = heading_re.match(lines[i])
        if m and '関連モジュール' in m.group(2):
            level = len(m.group(1))
            i += 1
            while i < n:
                m2 = heading_re.match(lines[i])
                if m2 and len(m2.group(1)) <= level:
                    break
                out.append(lines[i])
                i += 1
            continue
        i += 1
    return "\n".join(out)


def key_files(mod):
    pkg = mod.replace("-", "_")
    pkgdir = os.path.join(MODULES_DIR, mod, pkg)
    files = []
    if os.path.isdir(pkgdir):
        for f in ("views.py", "rest.py", "api.py", "models.py", "tasks.py",
                  "config.py", "permissions.py", "admin.py", "utils.py"):
            if os.path.exists(os.path.join(pkgdir, f)):
                files.append(f)
    return files


def build_reverse(modules):
    rev = {m: [] for m in modules}
    for path in glob.glob(os.path.join(SPEC_BASE, "**", "*.md"), recursive=True):
        rel = os.path.relpath(path, SPEC_BASE)
        fname = os.path.basename(path)
        if fname in ("SUMMARY.md", "GLOSSARY.md", "README.md",
                     "MODULE_INDEX.md", "ARCHITECTURE.md",
                     "DEV_GUIDE.md", "CROSS_REFERENCE.md"):
            continue
        lines = open(path, encoding="utf-8").read().splitlines()
        title = extract_title(lines)
        sec = extract_related_section(lines)
        whole = "\n".join(lines)
        for m in modules:
            variants = {m, m.replace("-", "_")}
            in_sec = bool(sec.strip()) and any(v in sec for v in variants)
            in_body = any(v in whole for v in variants)
            if in_sec or in_body:
                rev[m].append((rel, title, "strong" if in_sec else "weak"))
    return rev


def cat_of(rel):
    return rel.split("/")[0] if "/" in rel else "(base)"


def emit_module(mod, rev):
    entries = rev.get(mod, [])
    strong = [e for e in entries if e[2] == "strong"]
    weak = [e for e in entries if e[2] == "weak"]
    d = DESC.get(mod, "")
    kf = key_files(mod)
    lines = [f"### `{mod}`", "", d, ""]
    if kf:
        lines.append("- 主なファイル: " + ", ".join("`" + f + "`" for f in kf))
    lines.append(f"- 実装: `modules/{mod}/`")
    if strong:
        by = {}
        for e in strong:
            by.setdefault(cat_of(e[0]), []).append(e)
        lines.append(f"- このモジュールを「関連モジュール」に挙げる機能仕様（{len(strong)}件）:")
        for cat in sorted(by):
            label = CATLABEL.get(cat, cat)
            items = " / ".join(f"[{(e[1] or e[0])}]({e[0]})" for e in by[cat])
            lines.append(f"    - {label}: {items}")
    if weak:
        lines.append(f"- 本文中で言及する機能仕様: {len(weak)}件")
    lines.append("")
    return "\n".join(lines)


def main():
    modules = list_modules()
    rev = build_reverse(modules)
    weko = sorted(m for m in DESC if m.startswith("weko"))
    inv = sorted(m for m in DESC if m.startswith("invenio"))

    header = """# モジュール索引（逆引きリファレンス）

WEKO3 を構成する各モジュールが「何をするか」と、「そのモジュールを扱う機能仕様はどれか」を
逆引きするための索引である。ある実装モジュールに手を入れる際、影響範囲となる機能仕様を素早く辿れる。

- **順引き（機能 → モジュール）** は各機能仕様の「関連モジュール」節を参照。
- **逆引き（モジュール → 機能）** が本ページ。各機能仕様の「関連モジュール」節を機械集計して生成している。
- モジュール実装は `/home/mhaya/weko/modules/<モジュール名>/` にある。突き合わせ基準は tag `v2.0.2`。
- 利用ライブラリ・パッケージの一覧は [その他 › モジュール、ライブラリ](other/MODULE_01.md) を参照。
- 全体像・レイヤ構造は [アーキテクチャ全体像](ARCHITECTURE.md)、変更作業の入口は [開発者ガイド](DEV_GUIDE.md) を参照。

各モジュールの「主なファイル」は Blueprint／REST／モデル／Celery タスク／設定などの標準的な入口
（`views.py` `rest.py` `api.py` `models.py` `tasks.py` `config.py` `permissions.py` `utils.py`）を示す。

> このページは `spec/tools/generate_module_index.py` で再生成できる（`python3 spec/tools/generate_module_index.py`）。
> 機能仕様の「関連モジュール」節を編集したら、本スクリプトを実行して逆引きを更新すること。
> モジュールの1行説明はスクリプト内の `DESC` を人手で維持する。

> 「関連モジュールに挙げる機能仕様」は当該仕様の「関連モジュール」節で明示されているもの。
> 「本文中で言及する機能仕様」は節外の本文でモジュール名に言及があるもの（参考）。

---

## WEKO 独自モジュール（`weko-*`）

WEKO3 が Invenio3 上に独自実装した機能群。開発の主対象はほぼこの層にある。

"""

    inv_header = """
---

## Invenio 基盤モジュール（`invenio-*`）

WEKO3 が土台とする Invenio3 のモジュール群。フレームワークの挙動を変える際に参照する。
これらは上流（inveniosoftware）由来だが、WEKO3 リポジトリ内で改変されているものもある。

"""

    footer = """
---

## モジュール以外のディレクトリ

`modules/` 直下だが Python モジュールではないもの。

- `resources/`: {resources}
- `cookiecutter-weko-module/`: {cookiecutter}

---

## 更新履歴

| 日付 | 更新内容 |
| --- | --- |
| 2026/07/15 | 新規作成。49 ディレクトリ（実モジュール47＋非モジュール2）について、説明と機能仕様の逆引きを整備（tag v2.0.2 で突き合わせ） |
""".format(resources=NON_MODULE["resources"],
           cookiecutter=NON_MODULE["cookiecutter-weko-module"])

    body = (header
            + "\n".join(emit_module(m, rev) for m in weko)
            + inv_header
            + "\n".join(emit_module(m, rev) for m in inv)
            + footer)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"wrote {TARGET} ({len(body)} chars, weko={len(weko)}, invenio={len(inv)})")


if __name__ == "__main__":
    main()
