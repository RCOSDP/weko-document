# 用語集

WEKO3 機能仕様書で用いる主要用語。

| 用語 | 説明 |
| --- | --- |
| アイテム | WEKO に登録されるコンテンツの単位（メタデータ＋添付ファイル）。永続識別子（recid）で識別される。 |
| アイテムタイプ | アイテムのメタデータ構造を定義するテンプレート。`schema`（JSON Schema）/ `form`（入力フォーム）/ `render`（描画設定）の3定義を持つ（`weko_records.models.ItemType`）。 |
| インデックス | アイテムを分類・公開するツリー構造のカテゴリ（`weko-index-tree`）。公開/非公開・閲覧/投稿権限を持つ。 |
| コミュニティ（サブリポジトリ） | インデックスに紐づく運用単位。コミュニティ管理者が自身の範囲を管理する（`invenio-communities`）。 |
| ワークフロー | アイテム登録・利用申請等の一連のアクション手順（`weko-workflow`）。実体は WorkFlow。 |
| フロー | ワークフローを構成するアクション（Start / Item Registration / Approval / Item Link / Identifier Grant / End 等）の並び。 |
| アクティビティ | ワークフローの実行インスタンス（Activity ID `A-...`）。 |
| 制限公開 | ファイルのアクセスを「制限公開（open_restricted）」に設定し、利用申請・承認を経てワンタイムURLでダウンロードさせる機能。 |
| 提供方法 | 制限公開ファイルに設定するロール／ワークフローの組（`provide`）。 |
| 利用申請 / 利用報告 | 制限公開コンテンツの利用を申請するワークフロー、およびダウンロード後の利用報告ワークフロー。 |
| OAI-PMH | メタデータ・ハーベスティングのプロトコル（`/oai`、`invenio-oaiserver`）。 |
| SWORD API | 外部から一括登録を行う API（`/sword/...`、`weko-swordserver`）。 |
| RO-Crate | 研究データのパッケージング形式。SWORD/インポート/検索で扱う。 |
| ロール | アクセス権限の単位。System Administrator / Repository Administrator / Community Administrator / Contributor（登録ユーザー）/ 一般ユーザー / ゲスト。mAPグループとの関係は「[ロールとグループ](#ロールとグループ)」を参照。 |
| AdminSettings | 管理設定を JSON で保持するテーブル（`admin_settings`。name をキーに各機能の設定を格納）。 |
| 永続識別子（PID） | recid / doi / hdl 等のアイテム識別子（`invenio-pidstore`、table `pidstore_pid`）。 |
| DOI / CNRI(ハンドル) | 外部識別子。ワークフローの Identifier Grant で付与（`weko-handle`）。 |
| 学認 / Shibboleth | 学術認証フェデレーションによるログイン（`weko-accounts`）。 |
| OAアシスト | 外部システムへ公開ステータスを連携する機能（`weko-records-ui` external）。 |

## ロールとグループ

WEKO3 では、出自と保存先の異なる複数の概念を「ロール」「グループ」と呼んでいる。仕様書では以下の名称で呼び分ける。

この呼び分けは仕様書内に限る。マニュアルや画面表示では利用者がこれらの違いを意識する必要はなく、従来どおり「ロール」「グループ」と表記してよい。

| 仕様書での名称 | 英語表記 | 説明 | 例 | 保存先 | 実装上の判定 |
| --- | --- | --- | --- | --- | --- |
| ロール | Role | WEKO3 で定義するアクセス権限の単位。修飾なしの「ロール」は常にこれを指す | System Administrator、Repository Administrator、Contributor、管理画面で作成したロール | `accounts_role` | mAPロールグループ・mAPユーザー定義グループのいずれにも該当しないもの |
| ゲスト / ログインユーザー | Guest / Authenticated User | インデックス等の権限設定でのみ用いる仮想的なロール | ゲスト（`-99`）、ログインユーザー（`-98`） | なし（ID のみ） | — |
| mAPロールグループ | mAP role group | 学認mAPのグループのうち、WEKO3 のロールに対応づくもの。ログイン時に対応するロールをユーザーに付与する | `jc_roles_sysadm`、`jc_<repository_id>_ro_radm` | `accounts_role`（同期により登録） | `weko_accounts.api.is_map_role` / `map_role_condition` |
| mAPユーザー定義グループ | mAP user-defined group | 学認mAPのグループのうち、リポジトリ管理者が任意に作成するもの。インデックスの閲覧・投稿権限の設定に用いる | `jc_<repository_id>_gr_<任意のID>` | `accounts_role`（同期により登録） | `weko_accounts.api.is_map_group` / `map_group_condition` |
| mAPグループ | mAP groups | mAPロールグループと mAPユーザー定義グループの総称 | — | `accounts_role` | `weko_accounts.api.is_map_managed_name` |
| WEKOグループ（非推奨） | WEKO group (deprecated) | `weko-groups` モジュールのグループ。ユーザーのアカウント設定画面（`/accounts/settings/groups/`）で作成・管理する。将来削除する予定 | — | `accounts_group` | `weko_groups.models.Group` |

- mAPロールグループ・mAPユーザー定義グループの名称は、学認mAPのグループを作成する JAIRO Cloud Groups Manager の呼び方（ロールグループ / ユーザー定義グループ）に合わせている。グループ ID の命名規則と同期の仕組みは「[mAPグループ連携](./other/GAKUNIN_MAP_GROUP_CACHE_01.md)」を参照。

- 以下の表記は用いない。

  | 用いない表記 | 代わりに用いる表記 |
  | --- | --- |
  | mAPロール、学認mAPロール | mAPロールグループ |
  | 学認グループ、学認mAPグループ | mAPグループ（総称）、または mAPロールグループ / mAPユーザー定義グループ |
  | 修飾なしの「グループ」 | mAPユーザー定義グループ、または WEKOグループ（どちらを指すか明記する） |

- 保存先のテーブルを指す場合は「ロール」と書かず、`accounts_role` と書く。`accounts_role` にはロールに加えて mAPグループも登録されるため、「mAPグループは内部的にはロールとして扱う」のような書き方は、テーブルの話か概念の話か区別できなくなる。

- 画面上の「グループ」が何を含むかは画面ごとに異なるため、画面の仕様では含まれるものを明記する。

  | 画面 | 「ロール」として表示するもの | 「グループ」として表示するもの |
  | --- | --- | --- |
  | ユーザー管理（管理画面） | ロール（mAPロールグループを除く） | mAPユーザー定義グループ（`invenio_accounts.admin.UserView`） |
  | インデックスの閲覧・投稿権限設定 | ロール（`WEKO_PERMISSION_SUPER_ROLE_USER` と mAPロールグループを除く）、ゲスト / ログインユーザー | WEKOグループ、No Group（`-89`）、mAPユーザー定義グループ（`weko_index_tree.api.Indexes.get_index_with_role`） |
  | アカウント設定のグループ画面 | — | WEKOグループ |

- インデックスの権限設定では、mAPユーザー定義グループは `browsing_role` / `contribute_role` 列に、WEKOグループは `browsing_group` / `contribute_group` 列に保存される。判定時は `weko_index_tree.utils.get_user_roles_and_groups` で `*_role` 列からmAPユーザー定義グループを分離し、WEKOグループと合わせて「グループ」として扱う。
