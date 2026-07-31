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
| ロール | アクセス権限の単位。System Administrator / Repository Administrator / Community Administrator / Contributor（登録ユーザー）/ 一般ユーザー / ゲスト。 |
| AdminSettings | 管理設定を JSON で保持するテーブル（`admin_settings`。name をキーに各機能の設定を格納）。 |
| 永続識別子（PID） | recid / doi / hdl 等のアイテム識別子（`invenio-pidstore`、table `pidstore_pid`）。 |
| DOI / CNRI(ハンドル) | 外部識別子。ワークフローの Identifier Grant で付与（`weko-handle`）。 |
| 学認 / Shibboleth | 学術認証フェデレーションによるログイン（`weko-accounts`）。 |
| OAアシスト | 外部システムへ公開ステータスを連携する機能（`weko-records-ui` external）。 |
