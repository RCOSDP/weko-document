## メールテンプレート編集画面

-   目的・用途

本機能は、ユーザーや管理者に送信するメールのテンプレート（タイトル、文面）を登録・編集する機能である。

-   利用方法

1.  Administration画面のメニューから【設定】>
    【メールテンプレート】を選択する。

2.  メールテンプレート編集画面上で、編集するメールテンプレートを選択する。

    -   新規にメールを追加する場合は[+追加]ボタンを押下する。

3.  件名とメールの内容を編集後、[保存]ボタンを押下する。

-   利用可能なロール

| ロール   | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | -------------- | ---------------- | ------------------ | ------------ | ------------ | ------------------ |
| 利用可否 | ○              | ○                | ×                  | ×            | ×            | ×                  |

-   機能内容

-   メールテンプレート編集画面  

    メールのテンプレート一覧、およびメールのテンプレート編集フォームを表示する。

-   自動送信するメールの内容を編集する。

    -   送信者は【設定】> 【メール送信】の[Mail
        Setting]で設定したメールアドレス

-   設定項目は主に以下の2つとする。

    -   Subject：メールタイトル

    -   (メール内容）：メール内容

-   メールテンプレート編集機能の有効・無効をコンフィグにて制御できるようにする。

    -   ※実装(v2.0.2)では、`WEKO_ADMIN_USE_MAIL_TEMPLATE_EDIT`（既定 False）は定義のみでどこからも参照されていない。実際の画面／サイドメニュー表示は AdminSettings の `restricted_access.edit_mail_templates_enable` で制御される（下記「実装補足」参照）。

    -   メールテンプレート機能が無効の場合、サイドメニューから非表示にする。

-   あらかじめ制限公開機能で用いる自動送信するメールが設定される。（付録参照）

    -   既存のメールについても、内容の編集が可能とする。

-   以下の項目ごとに、テンプレートの一覧を表示する。

    -   シークレットURL提供メール

        -   シークレットURLダウンロード機能が有効な場合のみ表示

    -   ゲストユーザー申請フォーム案内メール

    -   その他メールテンプレート

-   メールテンプレートを選択した際に、メールの件名・本文が編集フォームに表示される。

    -   メールテンプレートの編集フォーム上でテンプレートの編集可能

    -   メール文面を編集する際、表 1の変数を利用可能

        -   メール送信時に、変数が登録内容に置換される。

        -   ヘルプ画面に変数一覧が表示される。

-   [保存]ボタンを押下することで、メールテンプレートの更新が可能

-   フロー編集画面

> フロー編集画面において、メールテンプレート機能が有効の場合、Flow
> Listのメール送信チェックボックスが表示される。

表 1 メールテンプレートで利用可能な変数

 | 変数名                                | 変数の内容                                  |
 | ------------------------------------- | ------------------------------------------- |
 | [url_guest_user]                    | ゲスト用の利用申請登録の案内URL             |
 | [register_date]                     | 登録年月日、報告年月日                      |
 | [restricted_fullname]               | 登録者名                                    |
 | [restricted_university_institution] | 登録者の所属機関                            |
 | [restricted_activity_id]            | 利用申請の申請番号                          |
 | [restricted_research_title]         | 登録者の研究題目                            |
 | [restricted_data_name]              | 利用申請データ                              |
 | [restricted_application_date]       | 利用申請年月日                              |
 | [restricted_mail_address]           | 登録者のメールアドレス                      |
 | [advisor_fullname]                  | 指導教員の姓名                              |
 | [advisor_university_institution]    | 指導教員の所属機関                          |
 | [guarantor_fullname]                | 保証人の姓名                                |
 | [guarantor_university_institution]  | 保証人の所属機関                            |
 | [restricted_download_link]          | ファイルのダウンロードURL                   |
 | [restricted_expiration_date]        | ダウンロードURLの有効期限日数               |
 | [restricted_expiration_date_ja]     | 日本語のダウンロード回数説明                |
 | [restricted_expiration_date_en]     | 英語のダウンロード回数説明                  |
 | [restricted_site_name_ja]           | 日本語のサイト名                            |
 | [restricted_site_name_en]           | 英語のサイト名                              |
 | [restricted_institution_name_ja]    | 日本語のサイト機関名                        |
 | [restricted_institution_name_en]    | 英語のサイト機関名                          |
 | [restricted_site_mail]              | サイトの連絡メール                          |
 | [restricted_site_url]               | サイトのURL                                 |
 | [data_download_date]                | データダウンロード日                        |
 | [usage_report_url]                  | 利用報告登録の案内URL                       |
 | [restricted_usage_activity_id]      | 利用報告の申請番号                          |
 | [output_report_activity_id]         | 成果物登録の申請番号                        |
 | [output_report_title]               | 成果物登録のタイトル                        |
 | [terms_of_use_jp]                   | 申請対象の利用規約（日本語）                |
 | [terms_of_use_en]                   | 申請対象の利用規約（英語、自由入力）        |
 | [secret_url]                        | 非公開、エンバーゴデータ向けシークレットURL |
 | [landing_url]                       | 申請対象のランディングページURL             |
 | [restricted_research_plan]          | 研究計画（利用申請/二段階利用申請アイテム） |

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ（追記）：本画面の実体は **invenio-mail** の `MailTemplatesView`（endpoint `mailtemplates`。`index` / `save_mail_template` / `delete_mail_template`）。model `MailTemplates` / `MailTemplateUsers`（送信元は `MailConfig`）。テンプレート `INVENIO_MAIL_TEMPLATES_TEMPLATE`。
- 有効化フラグは `AdminSettings` の `restricted_access.edit_mail_templates_enable`（`ext.py` が endpoint `mailtemplates` を非表示化）で制御される。`WEKO_ADMIN_USE_MAIL_TEMPLATE_EDIT`（既定 False）は定義のみでどこからも参照されていない。

