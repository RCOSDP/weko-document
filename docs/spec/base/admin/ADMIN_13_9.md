### ロール

## 目的・用途

本機能は、システムのロールを管理（追加・編集・削除）する際に使用する機能である。

## 利用方法

【Administration > ユーザー管理（User Management） > ロール（Role）画面】にて操作を行う。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 【ロール（Role）画面】には以下のタブが表示される
  - 一覧（List）
  - 作成（Create）
  - フィルターを追加▼（Add Filter▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 選択▼（With selected▼）
    - 一覧（List）タブ選択中のみ表示
    - 外観はタブだが機能としてはプルダウンメニュー
  - 編集（Edit）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
  - 詳細（Details）
    - 一覧（List）タブ選択中は非表示
    - 一覧（List）タブの操作によって表示される
    - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

- 「一覧」（List）タブに現在のシステムのロールを表示する
  - 表示項目は以下の通りである
    - チェックボックス
    - アクション（閲覧・編集・削除を表すアイコン）
    - 「Id」
    - 「Name」
    - 「Description」

  - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する
    - フィルター名
      - 「Id」
        - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Name」
        - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
      - 「Description」
        - フィルター方式の選択肢：上記の「Name」と同じである
        - 入力された文字列を使い、選択したフィルター方式で絞り込む
    - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される
    - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる

  - 「選択▼」（With selected▼）ボタンをクリックすると、以下の追加可能な機能（現在削除ボタンのみ）を表示する
    - レコードにチェックを入れない場合、「削除」（Delete）ボタンを押すと、エラーメッセージを表示する
      メッセージ：
      　日本語：「少なくとも一つのレコードを選択してください。」
      　英語：「Please select at least one record.」
    - レコードにチェックを入れる場合、「削除」（Delete）ボタンを押すと、確認ダイアログを表示する
      メッセージ：
      　日本語：「選択したレコードを削除してもよろしいですか。」
      　英語：「Are you sure you want to delete selected records?」
      - 「OK」ボタンを押すと、該当ロールを削除し、メッセージを画面上部に表示する
        メッセージ：
        　日本語：「レコード数＋レコードが正常に削除されました。」
        　英語：「Record was successfully deleted.」
      - 「キャンセル」（Cancel）ボタンを押すと、確認ダイアログを閉じる

  - 検索テキストボックスでロールを検索する
    - プレースホルダー：「Search: id, name, description」
    - 任意テキストを入力し、キーボードでの「Enter」を押すと、Id、ロール名、説明での検索を行う
    - テキストボックスの右端での「X」ボタンを押すと、検索条件がクリアーされる

  - ロール行にて目アイコンを押すと、該当ロールの詳細情報を「詳細」（Details）タブに表示する
    - 表示項目：ID、ロール名、説明

  - ロール行にて鉛筆アイコンを押すと、該当ロールを「編集」（Edit）タブに表示し、ロールの情報が編集できる

  - ロール行にて削除アイコンを押すと、該当ロールを削除し、メッセージを画面上部に表示する
    メッセージ：
    　日本語：「レコード数＋レコードが正常に削除されました。」
    　英語：「Record was successfully deleted.」

- 「一覧」（List）から「作成」（Create）タブを押すと、「作成」（Create）タブに移動し、ロールを新規作成できる
  - 入力情報：「Name」（ロール名）、「Description」（ロールの説明）、「Users」
    - NameとDescriptionは自由入力
    - Usersは、Emailを選択する
  - ［保存（Save）］ボタンを押すと、設定されたロール内容をロール一覧に追加させ、メッセージをロール一覧に表示させる
    メッセージ：
    　日本語：「レコードが正常に作成されました。」
    　英語：「Record was successfully created.」
    - ロールをデータベースに保存する
      - テーブル名：「accounts_role」
      - フィールド名：
        ・「id」
        ・「name」
        ・「description」
  - ［保存してもう一つ追加（Save and Add Another）］ボタンを押すと、設定されたロール内容をロール一覧に追加させ、他のロールを追加設定可能とする
    メッセージを画面上部に表示させる
    メッセージ：
    　日本語：「レコードが正常に作成されました。」
    　英語：「Record was successfully created.」
  - ［保存して編集を続ける（Save and Continue Editing）］ボタンを押すと、設定されたロール内容をロール一覧に追加させ、該当ロールの編集を続けることを可能とする
    メッセージを画面上部に表示させる
    メッセージ：
    　日本語：「レコードが正常に作成されました。」
    　英語：「Record was successfully created.」
  - ［キャンセル（Cancel）］ボタンを押すと、設定されたロール内容をロール一覧に追加せず、「一覧」（List）タブに戻る
  - 新規作成時、コンフィグでACCOUNTS_WORKFLOW_ROLE_HIDE_FILTER=Trueだった場合には、そのロールのユーザーでは各ワークフローが表示されないように設定される
    - そのロールで操作するときは、ワークフロー一覧に表示されず、アクティビティ作成時にそのワークフローを選択できない
    - 詳細は[ADMIN-7-2: ワークフロー](./ADMIN_7_2.md)を参照

- v0.9.22でのデフォルトロールは以下の通りである
  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/populate-instance.sh#L228-L231>
  - ロール：
    - 「System Administrator」
    - 「Repository Administrator」
    - 「Community Administrator」
    - 「Contributor」

## 関連モジュール

- invenio_accounts

## 処理概要

- 環境構築時にpopulate-instance.shで初期データを登録することで、デフォルトロールの作成と、各ロールへの権限付与が行われる。
  - 各デフォルトロールの名前は、作成時に環境変数で設定される
    - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/docker-compose.yml#L57-L60>

- 本画面では、accounts_roleテーブルのデータを作成、編集、削除する。
  - 作成、編集時は、画面の設定をもとに、以下のようにaccess_actionssystemrolesテーブルに保存する。
    - 「id」フィールド：画面上の入力によらない
    - 「name」フィールド：画面上の「Name」で入力されたもの
    - 「description」フィールド：画面上の「Description」で入力されたもの

- ロールを作成、編集したとき、invenio_accounts.admin.RoleView.after_model_changeメソッドが呼び出される。分岐によって、以下の場合のみ処理を行う。
  - ロールを新規作成したとき、コンフィグのACCOUNTS_WORKFLOW_ROLE_HIDE_FILTERがTrueである場合にのみ、workflow_userroleテーブルにレコードが作成される。
    - コンフィグは以下を参照する。
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-accounts/invenio_accounts/config.py#L227>
      - キー：ACCOUNTS_WORKFLOW_ROLE_HIDE_FILTER
    - 作成前にworkflow_workflowテーブルを参照して、is_deletedがfalseであるレコードを取得する。その数だけworkflow_userroleテーブルにレコードを作成する。
    - 作成するレコードでは、フィールドを以下のように設定する。
      - 「workflow_id」：workflow_workflowテーブルから取得した各レコードの「id」フィールドの値。１レコードにつき１idを設定する。
      - 「role_id」：それぞれのレコードに、accounts_roleテーブルに新規作成したレコードの「id」フィールドの値を設定する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_accounts.admin.RoleView`（model `Role`、テーブル `accounts_role`）。Users は Email によるAjax選択。`after_model_change` で `ACCOUNTS_WORKFLOW_ROLE_HIDE_FILTER`（既定 False）が True のとき `workflow_userrole` にレコードを追加。処理概要の「`access_actionssystemroles` に保存」は誤りで、保存先は `accounts_role`。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
