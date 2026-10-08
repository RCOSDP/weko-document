---
name: weko-release-doc-update
description: WEKO3 の新リリース（例 release_vX.Y.Z）に合わせて weko-document のマニュアル・機能仕様書・登録ガイド・英語版・アップデート手順書を実装と突き合わせて更新し、【vX.Y.Z】タグ付け・スクリーンショット撮影と注記付けまで行う手順。「vX.Y.Z 向けにドキュメントを更新して」「リリースに合わせてマニュアルを直して」などの依頼で使う。
---

# WEKO3 リリースに合わせたドキュメント更新

v2.1.0（2026-10）で実施した作業を手順化したもの。人が読む解説は `docs/develop/base/release_doc_update.md`。

## 0. 最初に決める値（ユーザーに確認する）

| 変数 | 意味 | v2.1.0 での値 |
|---|---|---|
| `NEW_VER` | 今回のバージョン | v2.1.0 |
| `RELEASE_REF` | 実装のリリースブランチ／コミット | `origin/release_v2.1.0`（508030789） |
| `PREV_TAG` | 直前のリリースタグ（**タグ判定の基準**） | `refs/tags/v2.0.4` |
| `LAST_AUDIT` | 前回ドキュメントを突合した実装コミット | b19e39d8a |
| `DOC_BASE` | weko-document の main から分岐した点（タグ付け対象の起点） | d11f699 |
| 実装リポジトリ | ローカル clone | `/home/mhaya/weko`（RCOSDP/weko） |
| 撮影環境 | RELEASE_REF で動くローカル環境 | wekov2（`https://localhost:8443`） |

実装ソースは `git -C <impl> archive <RELEASE_REF> | tar -x -C <scratchpad>/weko_src` で作業フォルダに展開して読む（実装リポジトリの checkout は変えない）。

## 1. 全体の流れ

1. **差分の棚卸し**：`git log --merges LAST_AUDIT..RELEASE_REF`、`git diff --dirstat`。テーマ（認可・新機能・設定・DB 移行など）に分ける。
2. **機能仕様書の突合**（`docs/spec/base`）：カテゴリ（api／access_control+restricted_access／admin／ams／user／other+tools+直下）ごとに並列エージェント。テンプレート `prompts/spec_audit.md`、ルール `rules/COMMON_RULES.md`。
3. **マニュアルの突合**（`docs/manuals/{ADMIN,USER}/base/README.md`）：章境界で分割したチャンクを並列エージェントで編集し、`cat` で結合（分割直後に `cmp` で一致確認）。テンプレート `prompts/manual_chunk_audit.md`。結合後に取りまとめ役が目次・版数・改定履歴を更新。
4. **登録ガイド**（`docs/manuals/GUIDE`）：1エージェント。CRLF のファイルがあるので改行を保つ。
5. **アップデート手順書**（`docs/operation/vPREV_vNEW.md`）：`PREV_TAG..RELEASE_REF` の差分（DB 更新 SQL、Alembic、ES、config、nginx/Dockerfile）から作成。実機未検証は【要確認】。テンプレート `prompts/upgrade_guide.md`。
6. **英語版**（`docs/manuals_en`）：
   - 日本語版の差分を英語版の対応節へ反映（`prompts/en_mirror.md`）。
   - 英語版に無い章・節は「断片」を作って `scripts/insert_frags.py` で一括差し込み（`rules/EN_FRAG_RULES.md`）。既存節の不足は1エージェントが直接編集（断片担当と同じファイルを触らせない）。
   - 章番号がずれたら `scripts/caption_renum.py`／`scripts/table_renum.py` で表・図番号を振り直し、`scripts/caption_check.py` で確認。
7. **【NEW_VER】タグ付け**：`DOC_BASE` 以降の差分のうち、**`PREV_TAG..RELEASE_REF` の実装差分で挙動が変わったもの**だけに付ける。見出しには付けない（`rules/TAG_RULES.md`、`prompts/tagging.md`）。
8. **整合チェック**：`scripts/verify_manual.py`（見出し文言・タグ数・目次の連番とリンク先）。手順番号の通し番号崩れ・節番号参照の不一致は `prompts/fix_numbering.md`。
   **ビルド確認**：`scripts/build_docs.sh --compare <DOC_BASE> --work <作業フォルダ>/docbuild` で spec・admin・user・GUIDE・admin_en・user_en を honkit でビルドし、`scripts/check_build.py` で分岐点からの**新しい**リンク切れ（PAGE／ANCHOR／IMAGE）を確認する。分岐点に既にあったものは「existing」として数だけ出る。SLUG（GitHub では効くが honkit では切れるアンカー）は `scripts/add_anchors.py` で見出しの前に id を足して直し、`check_build.py --strict` で 0 件を確認する。さらに `scripts/scan_rendered.py docs/build/<本>/html` で、honkit が Markdown として解釈せず文字のまま出した箇所（パイプ表、`1)` リスト、コメント、エスケープ、コードブロックになった段落など）が無いことを確認する（LESSONS.md「ビルド」）。develop・operation はビルド対象外（book.json が無い）。ビルド結果は別リポジトリに登録して github.io（https://rcosdp.github.io/weko/）で公開しているので、HTML 版で切れるリンク（SLUG を含む）は公開サイトで切れる。
9. **スクリーンショット**：`rules/SCREENSHOT_RULES.md`。撮影用管理者アカウント作成 → `scripts/capture.js` で全画面撮影 → サンプルデータは記録して登録 → 古い画像の注記を `scripts/annotate.js` で再現 → `scripts/stage2.py` で比較ページ → レビュー後に `scripts/apply_screenshots.py` で差し替え。 英語版は画像番号が違うので、節単位で日本語版との対応表を作ってから英語画面で撮る。
10. **コミット**：カテゴリ単位（`spec(api): ...`、`manual(ADMIN): ...`、`manual_en(USER): ...`、`operation: ...`）。push 前に `git fetch` してリモートの変更をマージ。push はユーザーの指示があってから。

## 2. 作業の原則（`LESSONS.md` に詳細）

- 推測で書かない。実装（テンプレート・JS・views・config・messages.po）で裏取りする。画面ラベルは**実際の表示**を正とする（翻訳ファイルと画面が違うことがある）。
- 並列エージェントに同じファイルを同時編集させない（チャンク分割か、断片→一括差し込み）。
- 見出しの文字列を変えない（アンカーが変わり、目次・他ファイルからのリンクが切れる）。
- 作業記録（findings・計画・進捗・変更点一覧）はリポジトリに入れない（`.gitignore` 済み：`/findings*.md`、`/task_plan.md`、`/progress.md`、`/manual_changes*.md`、`/docs/superpowers/`）。
- 編集後は機械的に検証してからコミット（見出し不変・タグ数・目次の連番・リンク先の実在・タグ以外の本文不変など）。
- 実装側の不具合を見つけたらドキュメントでは誤魔化さず、報告事項として残す（必要なら実装に PR）。

## 3. ファイル

- `rules/COMMON_RULES.md` — 全エージェント共通（実装参照方法・記述ルール・報告形式）
- `rules/TAG_RULES.md` — 【NEW_VER】タグの判定と付け方
- `rules/EN_FRAG_RULES.md` — 英語版の断片生成
- `rules/SCREENSHOT_RULES.md` — 撮影・サンプルデータ・注記
- `prompts/*.md` — エージェントへの依頼文の雛形（`{{...}}` を置き換えて使う）
- `scripts/` — `insert_frags.py`（英語版断片の差し込み）、`caption_check.py`／`caption_renum.py`／`table_renum.py`（表・図番号）、`verify_manual.py`（コミット前検証）、`build_docs.sh`／`check_build.py`／`add_anchors.py`／`strip_heading_fieldcodes.py`／`scan_rendered.py`／`fix_tables.py`（honkit ビルド、リンク切れ確認、honkit 用アンカーの補完、見出しの Word フィールドコード除去、honkit で崩れた表示の検出、リスト内の表の HTML 化）、`capture.js`／`annotate.js`／`overlay.js`（撮影・注記）、`stage2.py`（比較ページ）、`apply_screenshots.py`（レビュー後の差し替え）、`sample_data/`（撮影用サンプルデータの登録）
- `examples/screenshots_v2.1.0/` — v2.1.0 の撮影・注記指定（英語版や次のバージョンで流用）
- `LESSONS.md` — v2.1.0 で得た注意点
