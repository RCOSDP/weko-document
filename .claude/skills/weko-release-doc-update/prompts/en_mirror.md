# 日本語版の修正を英語版へ反映
まず `{{WORKDIR}}/COMMON_RULES.md` を読み、「マニュアル」のルール（英語版）に従ってください。
担当: 英語版 `/home/mhaya/weko-document/docs/manuals_en/{{ADMIN|USER}}/{{file}}.md`（このファイルだけ）
- 日本語版の差分（`git diff {{BASE}} -- docs/manuals/...` を `{{WORKDIR}}/ja_{{x}}.diff` に保存して渡す）を、英語版の対応する節に英語で反映。英語版は構成・見出しが異なる（LINKID 付き見出し等）ので対応節を探す。
- 画面ラベルは英語 UI の実際の文言（テンプレート・messages.po の msgid/英語 msgstr）。日本語を直訳しない。既存の英語版の訳語に合わせる。
- 対応節が無い新規節は、構成上自然な位置に新設してよい（目次も更新）。英語版に元々無い章まで作る必要は無い（別途 EN_FRAG_RULES で生成する）。
- 最終報告: 反映した項目、新設した節、反映しなかった項目と理由。
