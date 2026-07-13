### その他

## 目的・用途

本機能は、その他の運用設定を設定する機能である

## 利用方法

【Administration > Setting (設定) > Others (その他)】において、機関名を入力し、【Save (保存)】を押下することで、GoogleScholar向けメタデータのひとつの「学位授与機関名」として入力した機関名を付与する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

## 機能内容

  - 【Administration > Setting (設定)> Others (その他) 画面】での「Institution Name」エリアに機関名を設定する  
    ※設定された機関名がGoogleScholar向けにアイテムメタデータとあわせて、「学位授与機関名」として出力される
    
      - デフォルト：空白
    
      - 「機関名」（Institution Name）テキストボックスに機関名を入力してから、「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する  
        メッセージ：「Institution Name was updated.」

## 関連モジュール

  - weko_records_ui

## 処理概要

> 機関名を入力し、【Save (保存)】を押下した際に、weko_records_ui.admin.InstitutionNameSettingViewが呼び出される。

  - weko_records_ui.models.InstitutionName.set_institution_nameが呼び出され、  
    > 入力した機関名をinstitution_nameテーブルに設定する。

> 「INSTITUTION_NAME_SETTING_TEMPLATE」：weko_records_ui.config

  - 'weko_records_ui/admin/institution_name_setting.html'

> Google Scholar向けメタデータの出力の際は、weko_records_ui.utils.get_google_scholar_metaからweko_records_ui.models.InstitutionName.get_institution_nameを呼び出して  
> institution_nameテーブルから機関名を取得する。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
