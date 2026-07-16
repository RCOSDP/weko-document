# アイテムタイプ管理（制限公開）

## 目的・用途

制限公開機能で用いるアイテムタイプと、制限公開用コンテンツファイルのプロパティ構成について定義する。制限公開機能を利用するには、対応するアイテムタイプ（利用申請系・利用報告）と、アクセス制御用のオプション（アクセス／提供方法／利用規約）を持つファイル情報プロパティが必要である。

## 対応アイテムタイプ

- 制限公開機能に対して対応しているアイテムタイプは以下の通りである（日立納品時）
  - 「利用申請」（アイテムタイプID: 31001）
  - 「二段階利用申請」（アイテムタイプID: 31002）
  - 「利用報告-Data Usage Report」（アイテムタイプID: 31003）
    これら3つのアイテムタイプの構成は以下の通りである
- 上記に加え、実装上は利用申請系の派生アイテムタイプ（31004〜31008：二段階利用申請（保証人／指導教員）、三段階利用申請、利用申請（授業利用可）、二段階利用申請（授業利用可）等）が定義されている。
- アイテムタイプIDの分類は以下の設定値で管理される（`modules/weko-workflow/weko_workflow/config.py`）

| 設定キー | 値 | 用途 |
| --- | --- | --- |
| `WEKO_WORKFLOW_USAGE_APPLICATION_ITEM_TYPES_LIST` | `[31001, 31002, 31004, 31005, 31006, 31007, 31008]` | 利用申請系アイテムタイプIDの一覧 |
| `WEKO_WORKFLOW_USAGE_REPORT_ITEM_TYPES_LIST` | `[3007, 31003]` | 利用報告アイテムタイプIDの一覧 |
| `WEKO_WORKFLOW_USAGE_APPLICATION_ITEM_TITLE` | `'利用申請'` | 利用申請アイテムタイプ名 |
| `WEKO_WORKFLOW_USAGE_REPORT_ITEM_TITLE` | `'利用報告'` | 利用報告アイテムタイプ名 |

- これらアイテムタイプの初期データは、Pythonのアイテムタイプ定義ではなくSQL直挿入形式で管理されている（「関連ファイル」節参照）。

## 制限公開用のコンテンツファイル情報

制限公開機能を利用するには、「制限公開用のコンテンツファイル」プロパティが必要である

- アイテム登録画面でファイルをアップロードすると、ファイル名を自動設定する
- アップロードしたファイルのフォーマット・ファイルサイズをDBに格納する
  ※Meta画面のAllow Multipleのオプションはオンに設定し非活性

このプロパティは制限公開専用のスキーマ／フォーム定義（`scripts/demo/resticted_access.sql`）で構成され、標準のファイル情報プロパティ（`scripts/demo/properties/files.py`）に「制限公開（open_restricted）」のアクセス選択肢と「提供方法」「利用規約」を加えたものである。

| プロパティ定義 | | | | 備考 |
| --- | --- | --- | --- | --- |
| 表示名 | Text | - | - | ファイル名を登録する |
| 本文URL | Object | 本文URL | Text | コンテンツファイルの格納先が自動で登録される。コンテンツファイルが無い場合は手入力でURLを入力可能 |
| | | ラベル | Text | |
| | | オブジェクトタイプ | Select | 選択肢：abstract/summary/fulltext/thumbnail/other |
| フォーマット | Text | - | - | コンテンツファイルのMIMEタイプを取得して自動で登録される |
| サイズ | List | サイズ | Text | コンテンツファイルのサイズを取得して自動で登録される |
| 日付 | List | 日付 | Datetime | |
| | | 日付タイプ | Select | 選択肢：Accepted/Collected/Copyrighted/Issued/Submitted/Updated/Valid |
| バージョン情報 | Text | - | - | |
| 表示形式 | Select | - | - | detail/simple/preview |
| ライセンス | Select | - | - | |
| 自由ライセンス | Textarea | - | - | "ライセンス"で"自由入力"を選択した場合に登録する |
| アクセス | Radios | - | - | オープンアクセス/オープンアクセス日を指定する/ログインユーザのみ/公開しない/制限公開（デフォルト） |
| グループ | Select | - | - | "アクセス"で"ログインユーザのみ"を選択したときに登録する |
| 公開日（オープンアクセスの日付） | List | 日付 | Datetime | "アクセス"で"オープンアクセス日を指定する"を選択したときに登録する |
| | | タイプ | Select | 日付タイプは「Available」固定（Item Registration画面では入力エリアは存在しない） |
| データタイプ | Radios | - | - | "アクセス"で"ログインユーザのみ"を選択したときに登録する。選択肢は統制語彙リスト（ソース上の統制語彙定義）による |
| 提供方法 | List | ロール | Select | "アクセス"で"制限公開"を選択したときに登録する/ Administration＞UserManagement＞Roleで管理しているロールと「非ログインユーザ（Guest）」をリストに表示する |
| | | ワークフロー | Select | Administration＞WorkFlow＞WorkFlow Listで管理しているワークフローのうち「制限公開フラグ」（`workflow.open_restricted`、関連ストーリー：[#24080](https://redmine.devops.rcos.nii.ac.jp/issues/24080)）が有効なものをリストに表示する |
| 利用規約 | Select | - | - | "アクセス"で"制限公開"を選択したときに登録する。管理画面で登録した利用規約をリストで表示する。選択肢に「自由入力」を設ける（内部値 `term_free`） |

## アクセス選択肢の内部値マッピング

| 表示名 | 内部値 |
| --- | --- |
| オープンアクセス | `open_access` |
| オープンアクセス日を指定する | `open_date` |
| ログインユーザのみ | `open_login` |
| 公開しない | `open_no` |
| 制限公開（デフォルト） | `open_restricted` |

- 「提供方法」プロパティは内部的に `provide[]{role, workflow}` の配列構造で保持される。
- 「利用規約」で「自由入力」を選択した場合の内部値は `term_free`（`modules/weko-records-ui/weko_records_ui/utils.py`）。

## 関連モジュール

- weko-workflow（制限公開フラグ `open_restricted`・ワークフロー／アイテムタイプID分類）
- weko-records / weko-records-ui（ファイルアクセス制御・利用規約 `term_free`）
- weko-itemtypes-ui（Meta画面のAllow Multiple制御）
- weko-items-ui（アイテム登録画面のアップロード・ファイル名／フォーマット／サイズ自動設定）
- weko-deposit（フォーマット・サイズ等のDB格納）

## 処理概要

1. アイテム登録画面で制限公開用ファイルをアップロードすると、`weko-items-ui` のJS（`static/js/weko_items_ui/app.js`）が以下を自動設定する
   - ファイル名（`fileInfo['filename'] = fileData.key`。表示名の選択肢連動）
   - フォーマット（`fileData.mimetype`）／サイズ（`bytesToReadableString(size)`）
2. アイテムタイプのMeta画面では、ファイル系プロパティに対し「Allow Multiple」チェックボックスをオン固定かつ非活性にする（`weko-itemtypes-ui/static/js/weko_itemtypes_ui/create_itemtype.js`）
3. 保存時、フォーマット・サイズ・ファイル名等が記録メタデータとしてDBに格納される（`weko-deposit/weko_deposit/api.py`）
4. 「アクセス」で「制限公開（open_restricted）」を選択した場合に「提供方法」「利用規約」が有効となり、詳細画面でのアクセス制御・利用申請の入口となる（詳細は [RESTRICTED-ACCESS-2: アイテム詳細(制限公開)](./RESTRICTED_ACCESS_02.md) 参照）

## 関連ファイル（初期データ／定義）

- `scripts/demo/resticted_access.sql`：31001／31002／31003 のアイテムタイプ定義（item_type_name、schema／form／render JSON）
- `scripts/demo/item_type_usage_apply.sql`：派生アイテムタイプ（31004〜31008）
- `scripts/demo/restricted_access_upgrade.sql` / `scripts/demo/disable_restricted_access.sql`：更新・無効化用
- `scripts/demo/properties/files.py`：標準ファイル情報プロパティ（制限公開版の基礎）

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/13 |  | 実装(v2.0.2)と突き合わせ、目的・対応アイテムタイプID・configキー・アクセス内部値マッピング・関連モジュール・処理概要・関連ファイルを追記 |
