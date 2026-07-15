# Task Plan: 機能仕様書を weko 実装で整備

## Goal
`/home/mhaya/weko-document/docs/spec/base` 配下の機能仕様書を、実装 `/home/mhaya/weko`（現在 tag `v2.0.2`）の実際のソースコードと突き合わせて整備する。実装と食い違う記述を修正し、機能仕様書として足りていない情報（処理フロー・分岐・エラー処理・設定値・DBスキーマ・API仕様・権限判定など）を追記する。

## Settings (ユーザー確定事項)
- **深さ = 重**: 関連ソースを深く読み、処理概要を再構成・拡充。エッジケース/DBスキーマ/API仕様/権限判定まで網羅。
- **進め方 = 1カテゴリ試行→確認**: restricted_access で試行→確認済み。以降は残りカテゴリへ展開。
- **コミット = カテゴリ単位**: 1カテゴリ整備完了ごとにコミット（`docs/spec/base/<cat>/` を stage）。
- **粒度 (確認済OK)**: 関連モジュール/処理概要(実メソッド・ルート)/モデル・テーブルスキーマ/configキー/内部値マッピング。現状の restricted_access と同程度。
- **矛盾の扱い = 実装準拠に書き換え**: 仕様と実装が食い違う箇所は実装の挙動に書き換える（「注記で残す」ではない）。
- **ソース参照 = ファイル名・記号名まで（行番号は載せない）**: 本文には module/file/クラス・メソッド/config・テーブル名を書く。`:行番号` は書かない（findings.md には可）。
- **手法**: カテゴリ毎に複数ファイルを並列リサーチエージェントで実装突き合わせ→結果を統合編集。findings.md に要点保存。

## 対象カテゴリと状態
| # | category | files(.md) | status | commit |
|---|----------|-----------|--------|--------|
| 0 | restricted_access (試行) | 6 | done (確認済) | 623924c, cda6559 |
| 1 | ams | 5 | done | ab4499d |
| 2 | api | 21 | done | b3afce1 |
| 3 | access_control | 39 | done | 78847a5 |
| 4 | admin | 83 | done | 348758c, 60b3f97 |
| 5 | user | 56 | done | f9934f3 |
| 6 | other | 20 | done | 88a4bed |
| 7 | tool + tools | 4 | done | 23bf1d4 |
| 8 | base直下 (README/SUMMARY/GLOSSARY) | 3 | done | 23bf1d4 |

## 全カテゴリ完了（2026-07-14）
commits: 623924c/cda6559(restricted_access), ab4499d(ams), b3afce1(api), 78847a5(access_control), 348758c/60b3f97(admin), f9934f3(user), 88a4bed(other), 23bf1d4(tool+base) + 3f84a77/4e1186c(tool統合) + 4cf3cf0(SUMMARY) + 7565acc(RADME削除)

## フォローアップ（ユーザー指示「全部」2026-07-14）
- A: 真に空のセクションを補完（真空は約10箇所。多くは下位###に内容ありで誤検出）
  - 目的・用途: admin/ADMIN_1_3, other/USAGE_LOG
  - 機能内容+処理概要: admin/ADMIN_13_4,13_5,13_6
  - 処理概要: user/USER_4_12, USER_4_15
  - 関連モジュール: user/USER_4_4, USER_4_8
- B: 矛盾する本文プロ―ズを実装準拠に書き換え（各ファイルの「実装補足（訂正）」が指す誤記述をinline修正）。対象90ファイル（grep '（訂正）/誤り/誤植/存在しない/コピペ誤り'）。カテゴリ別に並列エージェントで実施。
- C: 要検証項目の実機/ソース確認（SWORD JSON-LD所有者フィルタ=ADMIN_16_2/access_control API_SWORD、USER_4_16/4_17「Request Email Addresses do not exist.」文言）
- D: 高価値ファイルのエラー/分岐/DBスキーマ深掘り（curated subset）
- status: A/B/C/D 完了（2026-07-14）
  - A: 真空セクション補完 → c1cd237
  - B: 矛盾90ファイルの本文を実装準拠に書き換え（9並列） → 80794b1
  - C: 要検証(SWORD所有者フィルタ・request-mail文言)を実ソース確定 → 81677f9
  - D: 中核5機能の詳細リファレンス(エラー/分岐/DBスキーマ) → dd3c14d

## 実装リポジトリ
- path: `/home/mhaya/weko`  (現在 detached HEAD @ tag `v2.0.2`, commit f0488c699)
- modules: `/home/mhaya/weko/modules/` に 49 モジュール
- 各仕様書の「## 関連モジュール」に対応モジュール名がある → そこを起点にソースを読む

## 仕様書の定型セクション
`### タイトル` / `## 目的・用途` / `## 利用方法` / `## 利用可能なロール` / `## 機能内容` / `## 関連モジュール` / `## 処理概要` / `## 更新履歴`

## 手順 (1ファイルあたり)
1. 仕様書を読む → 現状の記述内容と関連モジュールを把握
2. 関連モジュールのソース（views/utils/models/api/config/templates）を読む
3. 記述と実装の食い違いを findings.md に記録
4. 定型セクションの欠落を補い、処理概要を実装に沿って再構成・拡充
5. 足りない情報（分岐/エラー/設定値/DBスキーマ/権限）を追記
6. 編集完了を progress.md に記録

## Resume 手順 (OOM等で中断した場合)
1. この task_plan.md と progress.md, findings.md を読む
2. progress.md の "Last completed file" と上表の status で現在位置を特定
3. `git status --short docs/spec/base/` で未コミットの編集を確認
4. in_progress のカテゴリの続きから再開

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| (なし) | | |
