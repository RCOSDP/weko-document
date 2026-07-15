### ワークスペース設定

## 目的・用途

本機能は、ワークスペースの登録形式の選択を行う機能である。

## 利用方法

【Administration＞ワークフロー管理（WorkFlow）＞ワークスペース設定（WorkSpace WorkFlow Setting）】の順で画面遷移することで利用可能。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | | | | |

## 機能内容

- 【Administration > ワークフロー管理（WorkFlow） > ワークスペース設定（WorkSpace WorkFlow Setting）】に登録形式が表示される。
  - 表示項目は以下の通りである
    - 「直接登録」（Direct Registration）  
      ラジオボタンの形式で表示される。
      - 「アイテムタイプ選択」（Item Type Select）  
        指定されたアイテムタイプ名である。プルダウンの形式で表示される。
    - 「ワークフロー経由で登録」（Workflow Select）  
      ラジオボタンの形式で表示される。
      - 「ワークフロー選択」（Work Flow Select）  
        指定されたワークフロー名である。プルダウンの形式で表示される。
  - [保存（Save）]ボタンを押すと、登録形式とアイテムタイプあるいは、ワークフローを保存し、メッセージを表示する。  
    メッセージ： 「ワークスペースのワークフロー設定を更新しました。」 / 「WorkSpace WorkFlow Setting was updated.」

## 関連モジュール

- weko_workflow

## 処理概要

- 【Administration＞ワークフロー管理（Work flow）＞ワークスペース設定（WorkSpace WorkFlow Setting）】の順で画面遷移すると、weko_workflow.admin.WorkSpaceWorkFlowSettingView.indexが呼び出される。
- 情報の入力後に[保存（Save）]ボタン押下で、weko_workflow.admin.WorkSpaceWorkFlowSettingView.indexが呼び出される。
  - 入力された設定値は admin_settingsテーブルの nameカラムの値が「workspace_workflow_settings」であるレコードに保存される。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_workflow.admin.WorkSpaceWorkFlowSettingView.index`（endpoint `workspaceworkflowsetting`、GET 表示・POST 保存とも `index`）。成功メッセージ「WorkSpace WorkFlow Setting was updated.」。
- 実装補足：保存先は `AdminSettings`（`workspace_workflow_settings`、`item_type_id` / `work_flow_id` / `workFlow_select_flg`）。ラジオ `registrationRadio` の '1' が「直接登録」（`workFlow_select_flg='1'`）、それ以外が「ワークフロー経由」。アイテムタイプ一覧は harvesting を除外。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2025/03/27 | 057e4d8985a4b5526c0db7f07f717a4bb45bc984 | 初版作成 |
