## 解析基盤連携

- 目的・用途

本機能はリポジトリに公開されたデータを解析基盤で処理させるための機能である。

これによって、研究者がリポジトリに公開されたデータやプログラムを直接解析基盤で処理させることが可能となる。

- 利用方法

アイテム詳細画面で weko-records-ui が表示する「オンライン分析（Online Analysis）」ボタンをクリックする。ボタン押下により、既定の連携先である Binder（`https://binder.cs.rcos.nii.ac.jp/v2/weko3/`）で当該データを解析基盤上で処理できる。

このボタンは、config `WEKO_RECORDS_UI_DISPLAY_ONLINE_ANALYSIS_FLG`（既定 False）が True で、かつアイテムがオープンアクセス（`accessRight == 'open access'`）である場合にのみ表示される。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/14 |  | 本文を実装準拠に修正 |

## 実装補足（v2.0.2 実装との突き合わせ）

- オンライン分析（解析基盤連携）は **weko-records-ui** の「Online Analysis」ボタン（テンプレート `box/analysis.html`、`views.default_view_method` が `WEKO_RECORDS_UI_ONLINE_ANALYSIS_URL` を渡す）。既定の連携先は Binder（`https://binder.cs.rcos.nii.ac.jp/v2/weko3/`）。
- 表示条件：config `WEKO_RECORDS_UI_DISPLAY_ONLINE_ANALYSIS_FLG`（既定 False）が True かつアイテムがオープンアクセス（`accessRight == 'open access'`）の場合のみボタンを表示する。
