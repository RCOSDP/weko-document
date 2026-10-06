# マニュアルの突合（分割チャンク単位）
まず `{{WORKDIR}}/COMMON_RULES.md` を読み、そのルールに従って作業してください。

担当: {{MANUAL_NAME}}（日本語）のチャンク{{N}}
- 編集対象ファイル: `{{WORKDIR}}/chunks/{{CHUNK_FILE}}`（元 `{{MANUAL_PATH}}` の {{START}}〜{{END}} 行）
- 範囲: {{SECTIONS}}
- 重点: {{FOCUS}}（その範囲の画面・項目・権限・手順が {{RELEASE_REF}} の画面（テンプレート・JS・admin.py・messages.po）と一致するか。{{NEW_VER}} で追加・変更された機能の追記）
- 目次（## 目次）は編集しない。最終報告は COMMON_RULES の形式で。

（取りまとめ役：分割は `sed -n 'A,Bp'`、分割直後に `cat chunks/* | cmp - 元ファイル`。結合後に目次・版数・改定履歴を更新し、`scripts/verify_manual.py` で確認）
