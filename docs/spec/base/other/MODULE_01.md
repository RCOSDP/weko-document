# モジュール、ライブラリ

利用モジュール、ライブラリは以下のとおり

- invenioモジュール（<https://github.com/RCOSDP/weko/blob/hfix/packages-invenio.txt>）
- wekoモジュール（<https://github.com/RCOSDP/weko/blob/v0.9.22/requirements-weko-modules.txt>）
- パッケージ（<https://github.com/RCOSDP/weko/blob/v0.9.22/packages.txt>）

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：モジュール構成に変化がないことを確認し実装補足を追記 |

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足：モジュール一覧は `requirements-weko-modules.txt` / `packages-invenio.txt` / `packages.txt`（いずれもリポジトリ直下）が出典。v2.0.2 では weko-redis / weko-swordserver / weko-workspace / weko-signposting / weko-notifications / invenio-iiif 等が追加されている（参照リンクの v0.9.22 は陳腐化）。
- 実装補足（v2.1.0）：release_v2.1.0（508030789）でも `modules/` 配下は 49 ディレクトリ（実モジュール 47＋`resources/`・`cookiecutter-weko-module/`）で、b19e39d8a 以降のモジュールの追加・削除、`setup.py`（entry_points）の変更はない。各モジュールの説明は [モジュール索引](../MODULE_INDEX.md) を参照。
