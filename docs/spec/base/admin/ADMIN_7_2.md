### ワークフロー

## 目的・用途

本機能は、ワークフローの作成、編集を行う機能。

## 利用方法

【Administration＞ワークフロー管理（WorkFlow）＞ワークフロー（WorkFlow List）】の順で画面遷移することで利用可能。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

- 【Administration > ワークフロー管理（WorkFlow） > ワークフロー（WorkFlow List）】に登録されたワークフローが一覧に表示される。
  - 表示項目は以下の通りである
    - 「No.」
    - 「ワークフロー」（WorkFlow）  
      登録されたワークフロー名である。リンクの形式で表示される。
    - 「アイテムタイプ」（Item Type）  
      指定されたワークフロー名である。
    - 「フロー」（Flow）  
      指定されたフロー名である。
    - 「制限公開フラグ」（Restricted Access Flag）  
      指定された制限公開フラグ名である。
    - 「GakuNinRDM Flag」  
      GakuNinRDMからWEB API経由で受け取るアイテムの一括登録を行う際のワークフローを作成するためのフラグ。
    - 「登録先インデックス」（Registration Destination Index Designation）  
      指定された登録先インデックスの指定名である。
    - 「ストレージロケーション」(Storage Location)  
      ファイルを保存するストレージロケーション名である。
    - 「表示」(Display)  
      ワークフローを表示するロールを表示する。
    - 「Hide」  
      ワークフローを非表示とするロールを表示する。
    - 「ステータス」（Status）  
      ワークフローのステータス
    - 「更新日」（Updated）  
      ワークフローの更新日である。フォーマット：YYYY-MM-DD
  - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに属するワークフローが一覧に表示される。

- 「Create WorkFlow」ボタンを押すと、ワークフローの作成画面に移動する。
  - 入力項目は以下の通りである。
    - 「ワークフロー」（WorkFlow）：テキストボックスにワークフロー名を入力する。
    - 「フロー」（Flow）：プルダウンからフローを選択する。  
      プルダウンの選択肢は【Administration > ワークフロー管理（WorkFlow） > フロー（Flow）】で登録されたフロー一覧である。
      - サブリポジトリ管理者の場合は、管理対象のサブリポジトリに属するフローが一覧に表示される。
    - 「アイテムタイプ」（Item Type）：プルダウンからアイテムタイプを選択する。  
      アイテムタイププルダウンの選択肢は【Administration＞アイテムタイプ管理（Item Types）＞メタデータ（Metadata）】で登録された標準アイテムタイプ一覧である。
    - 「リポジトリ」（Repository）：プルダウンからリポジトリを選択する。  
      リポジトリプルダウンの選択肢は【Administration＞コミュニティ管理（Communities）＞コミュニティ（Community）】で登録されたコミュニティ一覧と"Root Index"である
    - 「制限公開フラグ」（Restricted Access Flag）：制限公開フラグをチェックする。  
      デフォルトはチェック無し。チェックありの場合、アイテム登録画面でコンテンツファイルの制限公開指定時に「提供方法」の「ワークフロー」の選択肢として表示する。
    - GakuNinRDM Flag： チェックを入れるとGakuNinRDMからWEB APIで受け取る「一括登録フォーマット」の利用を可能とするワークフローとなる。
    - 「登録先インデックスの指定」（Registration Destination Index Designation）：プルダウンから登録先インデックスの指定を選択する。インデックスプルダウンの選択肢は【Administration＞インデックスツリー管理（Index Tree）＞ツリー編集（Edit Tree）】で登録されたインデックス一覧である。サブリポジトリ管理者の場合は、管理対象のサブリポジトリに属するインデックスが一覧に表示される。
      - [登録先インデックスの指定（Registration Destination Index Designation）] を「指定なし（Enable）」とした場合
        - ワークフローで項目入力後にインデックスを指定してアイテムを登録する。
      - [登録先インデックスの指定（Registration Destination Index Designation）] でインデックスを指定した場合
        - ワークフローで項目入力後に、指定したインデックスを自動で登録する。
    - 「ストレージロケーション」(Storage Location)： プルダウンから登録先ストレージロケーションを選択する。
    - 「表示／非表示」（Diplay/Hide）ロール毎にワークフローの表示・非表示を設定する。
      - invenio_account.ACCOUNTS_WORKFLOW_ROLE_HIDE_FILTER = False とすると、新規ロール追加時にデフォルトで表示となる。(v0.9.22)
  - [保存（Save）]ボタンを押すと、ワークフローを保存し、メッセージを表示する。  
    メッセージ：「Workflow created successfully.」

    対象のワークフローが使用されていた場合、アイテムタイプの変更ができません。

- ワークフロー名のリンクを押すと、ワークフローの編集画面に移動する。
  - ワークフローの編集画面で、ワークフローの情報を編集できる。
    - ワークフローの情報を編集してから、[保存（Save）]ボタンを押すと、ワークフローを編集し、下記メッセージを一覧画面の上部に表示し、WorkFlow List画面に遷移する。  
      メッセージ：「Workflow created successfully.」
  - ワークフローの編集画面で、[削除（Delete）]ボタンを押すと、ワークフローを削除する。削除後、WorkFlow List画面に遷移する。
    - 対象のワークフローが使用されていた場合は削除できない。[削除（Delete）]ボタンを押すと、エラーメッセージを表示する。  
      エラーメッセージ：「Cannot be deleted because workflow is used.」
    - ワークフローの編集画面で、[戻る（Back）]ボタンを押すと、ワークフロー一覧画面に移動する。

- WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG が True かつシステム管理者でない（リポジトリ管理者、サブリポジトリ管理者）の場合、利用申請に関するワークフローは閲覧・編集ができない。また利用申請に関するワークフローを追加できない。（利用申請フラグが非表示であり、登録時に利用申請フラグがFalseとして登録される）。利用申請フラグの編集は WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG と WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS が True かつシステム管理者の場合のみ可能。

- 戻るボタンをクリックすると、一つ前のアクションに戻ることが可能(v1.0.7追加)。

## 関連モジュール

- weko_workflow

## 処理概要

【Administration＞ワークフロー管理（Work flow）＞ワークフロー（Work Flow List）】の順で画面遷移すると、weko_workflow.admin.WorkFlowSettingView.indexが呼び出され、db内のworkflow_workflowテーブルからis_deletedカラムにチェックが入っていないワークフローの情報を取り出し、WorkFlow Listとして表示する。

- [Create Workflow]ボタン押下時もしくはワークフロー名を押下指定のワークフローの編集時は、weko_workflow.admin.WorkFlowSettingView.workflow_detailが呼び出される。ここではメソッド内の変数workflow_idの値を用いて条件分岐している。新規作成時は、workflow_id=0であり、それ以外はworkflow_idに指定したワークフローのidを代入している。新規作成の場合、入力欄の初期値は以下のようになる。
  - ワークフロー（Work Flow）：空欄
  - フロー（Flow）：【Administration＞ワークフロー管理（Work Flow）＞フロー（Flow　List）】のFlow Listの情報をプルダウン形式で表示する。初期状態では、No.が一番小さいものとなっている。
  - アイテムタイプ（ItemType）：db内のitem_type_nameテーブルのnameカラムから情報を取り出し、プルダウン形式で昇順で表示する。初期状態では、idが一番小さいものとなっている。
  - リポジトリ（Repository）：db内のcommunities_communityテーブルのidカラムから情報を取り出し、プルダウン形式で昇順で表示する。初期状態では、idが一番小さいものとなっている。
  - 制限公開フラグ（Restrictedke）：チェックなし
  - GakuNinRDM Flag：チェックなし
  - 登録先インデックスの指定（Registration Destination Index Designation）：db内のindexテーブルのindex_nameカラムから情報を取り出し、プルダウン形式で表示する。初期状態ではどの情報も選択せず、「指定なし（Undesignated）」とする。
  - ストレージロケーション（Storage Location）：db内のfiles_locationテーブルのnameカラムから情報を取り出し、プルダウン形式で表示する。初期状態ではどの情報も選択せず、「指定なし（Undesignated）」とする。
  - 表示/非表示（Display/Hide）：db内のacounts_roleのnameカラムから情報を取り出し表示（Display）ボックス内に表示する。初期状態では、すべてのroleが表示側に表示される。
- 既存のワークフローの編集の場合、入力欄の値は指定したworkflow_idを用いてweko_workflow.api.Workflow.get_workflow_detailを使用して情報をdb内のworkflow_workflowテーブルから取り出して表示する。

情報の入力後に[保存（Save）]ボタン押下で、weko_workflow.admin.WorkFlowSettingView.update_workflowが呼び出される。  
ただし、[保存（Save）]ボタンは、ワークフロー名が空欄の時は非活性となる。

- 新規作成の場合、UUIDが新たに作成され、その後db内のworkflow_workflowテーブルに入力したワークフローを保存する。作成されたUUIDはflow_idとして使用される。
- 既存のワークフローの編集の時は、db内のworkflow_workflowテーブルの情報を更新する。
- [保存（Save）]ボタン押下前に、[戻る（Back）]ボタン押下で入力内容を破棄しWorkFlow List画面へ戻る。

ワークフロー名押下で編集画面に移行した際は、[保存（Save）]ボタンの横に[削除（Delete）]ボタンが配置される。[削除（Delete）]ボタン押下時は、削除可能なワークフローである場合はdb内のworkflow_workflowテーブルのis_deletedカラムにチェックが入る。

設定値

- WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS
  - パス：<https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/weko-admin/weko_admin/config.py#L1380>
  - 初期値：True
  - 利用申請フラグの表示非表示を切り替える。
  - scripts/instance.cfg で定義されている場合は、そちらの設定を優先する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_workflow.admin.WorkFlowSettingView`（endpoint `workflowsetting`）。`index` / `workflow_detail`（workflow_id='0' で新規、`flows_id` は `uuid4()`）/ `update_workflow` / `delete_workflow`（`is_deleted` 更新、使用中は「Cannot be deleted because workflow is used.」）。表示/非表示ロールは `WorkflowRole` に保存。
- config：`WEKO_ADMIN_DISPLAY_RESTRICTED_SETTINGS` の初期値は True。利用申請フラグのチェックボックス表示はシステム管理者かつ `WEKO_ADMIN_RESTRICTED_ACCESS_DISPLAY_FLAG` 有効時。成功メッセージはフロントJS で付与される。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2025/01/23 | - | サブリポジトリ対応 |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | 要素の表示条件・アクセス権限を記載 |
