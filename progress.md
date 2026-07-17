# Progress Log

## Session 2026-07-13 (start)
- 方針確定: 深さ=重 / 1カテゴリ試行→確認 / カテゴリ単位コミット
- 試行カテゴリ = restricted_access に決定
- 計画ファイル3点作成
- Last completed file: (なし)
- Current: restricted_access の整備に着手

### restricted_access 進捗
- 5並列エージェント調査完了→findings.md に要点保存済み
| file | status | notes |
|------|--------|-------|
| RESTRICTED_ACCESS_01.md | done | 目的/対応IT ID/config/内部値/関連モジュール/処理概要/関連ファイル追記 |
| RESTRICTED_ACCESS_02.md | done | 関連モジュール/処理概要/モデル/設定値/ルート追記、EN文言注記 |
| RESTRICTED_ACCESS_03.md | done | 関連モジュール/データモデル/処理概要/メール対応/config追記、推奨構成注記 |
| RESTRICTED_ACCESS_04.md | done | 目的/ロール/関連モジュール/処理概要/config/モデル/プレースホルダ追記、15種注記 |
| RESTRICTED_ACCESS_05.md | done | 実装乖離を修正・注記（weko-admin主体/メニュー名/5種/未実装文言/autofillフラグ）+config/model/route |
| README.md | done | カテゴリ概要・関連モジュール・AdminSettings追記 |

### restricted_access 完了・確認済（commit 623924c, cda6559）
- ユーザー確認済: 粒度OK / 矛盾は実装準拠に書き換え / ソース参照はファイル名・記号名まで(行番号なし)

### ams 完了（commit ab4499d）
- フロント(weko-frontend)は別リポジトリで検証不可→バックエンド接点のみ実装準拠で整備
- Last completed: ams全5ファイル

### api 完了（commit b3afce1）
- 21ファイルを9並列調査→統合。矛盾を実装準拠に修正、関連モジュール/endpoint/handler/scope/config追記。

### access_control 完了（commit 78847a5）
- 39ファイル。共通の権限担保機構注記＋矛盾修正＋READMEバグ修正。

### admin 完了（commit 348758c 前半42, 60b3f97 後半41）
- 2波×8/6並列調査→実装補足ノートをスクリプト一括挿入(scratchpad/admin_wave1_notes.py, admin_wave2_notes.py)＋主要矛盾inline修正＋README記入。

### user 完了（commit f9934f3）
- 8並列調査→ノート一括挿入(scratchpad/user_notes.py)＋README。

### other 完了（commit 88a4bed）
### tool+tools・base直下 完了（commit 23bf1d4）

## 全カテゴリ完了（2026-07-14）
- 237ファイル全てを実装(tag v2.0.2)と突き合わせ整備。カテゴリ単位で9コミット。
- 未コミット変更なし（docs/spec/base）。行番号本文混入なし。
- ブランチ develop_v2.0.1、未push。

## フェーズ2: v2.0.2→develop_v2.1.0 差分反映（2026-07-17 完了）
- 実装差分 427コミット/409ファイルをテーマA〜Hに整理（5並列調査エージェント）。findings は findings_v2.1.0.md ＋ scratchpad/find_{A,B,D,E,F}_*.md。
- 機能仕様書を **変更差分のみ実装突合** で更新（5並列編集エージェント）。27ファイル（新規 api/API_20_bulk_import.md 含む）。
  - api(7) commit 63852a6 / access_control(4) 71e9c52 / admin(9) 2d76fcc / user(5) bf05562 / other+ams(3) e15136e
  - SCHEMA_1_2/1_3 は #58215(JPCOAR nameIdentifierScheme置換)の受け皿として主題不一致のためスキップ（別ページが適切）。
- マニュアルは編集せず **変更点一覧のみ** 作成 → manual_changes_v2.1.0.md（USER 6件/ADMIN 11件/GUIDE 2件）。
- 実装側の要確認: postgresql/ddl/sp72-createindex.sql が item_type_mapping の旧btree 2本＋GIN を作る記述のまま（新規構築とマイグレーション後で不整合の懸念）。
- 全編集で行番号本文混入なし・更新履歴行(2026/07/17)追加済み。ブランチ develop_v2.1.0、未push。
