# 機能仕様書の突合（カテゴリ単位）
まず `{{WORKDIR}}/COMMON_RULES.md` を読み、そのルールに従って作業してください（「機能仕様書」のルールを適用）。

担当: 機能仕様書 `/home/mhaya/weko-document/docs/spec/base/{{CATEGORY}}/` 配下全ファイル
- (1) `{{LAST_AUDIT}}..{{RELEASE_REF}}` の差分のうち、このカテゴリに関係するもの（{{THEME_HINTS}}）を洗い出し、該当仕様の権限・応答コード・処理概要・設定値を実装準拠に更新。
- (2) 前回突合以降に他者がマージしたこのカテゴリの変更（`git -C /home/mhaya/weko-document log {{DOC_LAST_AUDIT}}..HEAD -- docs/spec/base/{{CATEGORY}}`）を実装と突合して齟齬を修正。
- (3) 実装に存在するのに仕様書に無いもの（新しい API・設定・画面）があれば追記（新規ファイルは SUMMARY.md・カテゴリ README も更新）。
- 最終報告は COMMON_RULES の形式で。
（カテゴリ例：api ／ access_control+restricted_access ／ admin（多いので前半・後半に分割）／ ams ／ user ／ other+tools+base直下）
