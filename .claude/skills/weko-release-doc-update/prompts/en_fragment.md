# 英語版に無い章・節を日本語版から生成（断片）
まず `{{WORKDIR}}/EN_FRAG_RULES.md` を読み、そのルールに厳密に従ってください。断片の出力先は `{{WORKDIR}}/en_frag/`（ファイル名 {{ID}}_1.md …）。英語版本体は編集しない。
担当 {{ID}}：英語版 {{ADMIN|USER}} マニュアルに、日本語版の {{SECTIONS}} が無ければ生成する（あるかどうかを必ず確認する。一部だけある場合は不足分だけ）。
- 差し込み位置の目安：{{WHERE}}
- 同じ差し込み位置に複数の断片が入る場合は、日本語版の並び順になるようファイル名の番号を付ける。

（取りまとめ役：全断片が揃ったら `FRAG_DIR=… python3 scripts/insert_frags.py`、`scripts/verify_manual.py` で目次の連番・リンク先、`scripts/caption_check.py`→必要なら `caption_renum.py`／`table_renum.py`、章構成の一覧を更新。既存節の不足を直接編集する担当を同時に動かす場合は、断片との重複を差し込み前に除く）
