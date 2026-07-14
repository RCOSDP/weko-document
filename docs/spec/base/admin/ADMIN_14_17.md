# WebAPIアカウント

## 目的・用途

本機能は、アイテムメタデータ自動入力機能におけるAPIアカウント認証で使用する情報を設定する機能である

## 利用方法

【Administration > 設定（Setting） > WebAPIアカウント（WebAPI Account）画面】にてアイテムメタデータ自動入力機能で連携するWeb APIのアカウント情報を設定する

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ |  |  |  |  |  |

## 機能内容

  - v2.0.0では、CrossRefおよびOA Assist APIの設定に対応している

  - 設定項目は以下とする
    
      - 「入力タイプ」（Input Type） ：タイプを選択する
        
          - 画面表示時の選択値は、「入力タイプを選択してください」（Please selected the input type）
    
      - 各種APIに必要なアカウント設定フィールド
        
          - 入力タイプで "CrossRef" を選択した場合は、以下の入力フィールドを表示する  
            「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）
          - 入力タイプで "OA Assist" を選択した場合は、以下の入力フィールドを表示する  
            「OA assist API Client ID」
            「OA assist API Client Secret」

  - ［保存（Save）］ボタンを押すと入力内容のチェックを行い、エラーがなければ設定情報が保存される
    
      - 「入力タイプ」（Input Type）の選択値が「入力タイプを選択してください」（Please selected the input type）である間、［保存（Save）］ボタンは非活性である
    
      - 「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）が空の状態でボタンを押すと、保存されずに以下のエラーメッセージがポップアップで表示される  
        エラーメッセージ：「Account information is invalid. Please check again.」
    
      - 「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）に入力値がある場合は、その内容を使って接続の確認を行い、正常に接続できなかった場合は、保存されずに保存されずに以下のエラーメッセージがポップアップで表示される  
        エラーメッセージ：  
        　日本語：「アカウント情報が無効です。再度確認してください」  
        　英語：「Account information is invalid. Please check again.」
    
      - エラーが発生しなかった場合は、以下のメッセージが表示される  
        メッセージ：「Account info has been saved successfully.」

## 関連モジュール

- weko_admin

## 処理概要

  - 画面表示時は、weko_admin.admin.WebApiAccount.indexメソッドがGETで呼び出される
    
      - テーブルから情報を取得するなどの処理は行わない

  - 「入力タイプ」（Input Type）でタイプを選択すると、weko_admin.views. get_curr_api_cert関数が呼び出される
    
      - この中では、weko_admin.utils.get_current_api_certification関数で、api_certificateテーブルから「入力タイプ」（Input Type）の選択値のvalueと「api_code」フィールドが一致するレコードを取得する
    
      - 取得した値を、「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）入力フィールドに設定する

  - ［保存（Save）］ボタンを押すと、web_api_account.jsで入力値のチェックを行い、エラーがなければweko_admin.views. save_api_cert_data関数がajaxで呼び出される
    
      - 「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）が空だった場合のチェックはweb_api_account.jsで行う
    
      - save_api_cert_data関数の中で、weko_admin.utils.calidate_certification関数によって接続確認を行う
    
      - 接続確認に成功した場合に、api_certificateテーブルに「入力タイプ」（Input Type）の選択値のvalueと「api_code」フィールドが一致するレコードがあるかどうか確認して、あった場合にそのレコードを更新する

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_admin.admin.WebApiAccount`（endpoint `webapiaccount`）＋ API `weko_admin.views.get_curr_api_cert`（`/get_curr_api_cert/<api_code>`）/ `save_api_cert_data`（POST）/ `get_api_cert_type`。model `ApiCertificate`（テーブル `api_certificate`、PK `api_code`）。
- 実装補足（訂正）：接続確認関数は `weko_admin.utils.validate_certification`（「calidate_certification」は誤り）で、確認を行うのは `api_code=='crf'`（CrossRef）のみ。OA Assist（`oaa`）は接続確認なしで保存。保存は `utils.save_api_certification`（`update_api_cert`/`insert_new_api_cert`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2026/03/18 | 37ff130e96e87f9d012917cd160e7fbc08d0c19a | v2.0.0 |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
