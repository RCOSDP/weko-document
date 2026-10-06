# アップデート手順書の作成
まず `{{WORKDIR}}/COMMON_RULES.md` を読み、実装参照方法・禁止事項に従ってください。
担当: `/home/mhaya/weko-document/docs/operation/{{PREV_VER}}_{{NEW_VER}}.md` を新規作成（{{PREV_VER}} から {{NEW_VER}} へのアップデート方法）。
- 既存の手順書（例 `docs/operation/v2.0.4_v2.1.0.md`、`v1.0.8b_v2.0.0.md`）の構成・粒度・文体に合わせる。
- 根拠は `git -C {{IMPL_REPO}} diff {{PREV_TAG}} {{RELEASE_REF}}` のみ：DB 更新 SQL（postgresql/update・ddl、tools/update）と適用順・冪等性、Alembic の変更（既存 DB の alembic_version の扱い）、ES マッピング、追加・変更された config と既定値、nginx・Dockerfile・docker-compose、OAuth スコープなどの事後作業、CHANGELOG。
- 実機未検証である旨を冒頭に注記し、確証の無い手順には【要確認】を付ける。推測で手順を作らない。
- 最終報告: 作成内容の要約、要確認事項一覧。
