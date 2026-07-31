# 制限公開

制限公開（Restricted Access）は、コンテンツファイルのアクセスを「制限公開」に設定し、利用者からの利用申請・承認ワークフローを経てワンタイムURLでのダウンロードを許可する機能である。ダウンロード後には利用報告の登録を促す。

## 本カテゴリの構成

| ドキュメント | 内容 |
| --- | --- |
| [RESTRICTED-ACCESS-1: アイテムタイプ管理（制限公開）](./RESTRICTED_ACCESS_01.md) | 対応アイテムタイプと制限公開用コンテンツファイルのプロパティ構成 |
| [RESTRICTED-ACCESS-2: アイテム詳細(制限公開)](./RESTRICTED_ACCESS_02.md) | 詳細画面・ファイル詳細画面のアクセス制御、利用申請、ワンタイムURL、ダウンロードログ |
| [RESTRICTED-ACCESS-3: ワークフロー管理（制限公開）](./RESTRICTED_ACCESS_03.md) | 利用申請／利用報告フロー、Action Role/User、通知メール設定 |
| [RESTRICTED-ACCESS-4: メールテンプレート](./RESTRICTED_ACCESS_04.md) | 自動送信メールの件名・本文・追加宛先・プレースホルダ |
| [RESTRICTED-ACCESS-5: プロフィール表示設定](./RESTRICTED_ACCESS_05.md) | プロフィール項目の表示／非表示・ラベル・入力方式 |

## 関連モジュール

- weko-records-ui（アクセス制御・ダウンロード処理・ワンタイムURLモデル）
- weko-workflow（利用申請／利用報告ワークフロー・承認処理・通知メール）
- weko-admin（Restricted Access 設定・メールテンプレート・プロフィール表示設定）
- invenio-mail（メールテンプレート編集・宛先検証）
- weko-user-profiles（プロフィール表示設定の消費側）

## 設定

### WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG

制限公開機能の管理画面の表示項目を制御する。
Falseが設定された場合は、シークレットURL設定画面しか表示しない。またワンタイムURLによるダウンロードも不許可（403）となる。

- デフォルト値: False
- 設定場所：
  - `modules/weko-admin/weko_admin/config.py`
  - `scripts/instance.cfg`

### AdminSettings `restricted_access`

管理画面（Administration > Setting > Restricted Access）で編集する設定。`AdminSettings` テーブル（name=`restricted_access`）にJSONで保持される。主な項目：

- `edit_mail_templates_enable`（既定 False）：メールテンプレート編集機能／通知メール設定・Specify property・アイテム登録者承認 の有効化
- `error_msg`：権限不一致時の警告メッセージ（既定値は `WEKO_ADMIN_RESTRICTED_ACCESS_ERROR_MESSAGE`）
- `content_file_download`：コンテンツファイルダウンロードの有効期限・回数
- `usage_report_workflow_access.expiration_date_access`（既定 500）：ゲスト利用報告ワークフローリンクの有効期限（日）
