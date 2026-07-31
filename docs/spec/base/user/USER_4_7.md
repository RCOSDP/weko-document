# Item Registration：代理投稿

## 目的・用途

Item Registrationの一部として、画面上の設定エリアで代理投稿者を指定する。

## 利用方法

アイテムメタデータ登録画面の[Contributor]エリアで「Other user」ラジオボタンを選択すると、ユーザ設定エリアが表示される。そこで入力されたユーザを代理投稿者として設定する。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       ○        |        ○         |         ○          |      ○       |      ※       |                    |

※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

## 機能内容

### 1. アイテムに代理投稿を指定する

- アイテムメタデータ登録画面に[Contributor]エリアを表示する
- アイテムの登録者は、Contributorをシステムに登録されている他のユーザから選択できる  
  ただし、アイテム登録者は、他ユーザを選択してもContributorとして有効のままとする
- デフォルトは[This user]とする（アイテム登録者のみをContributorとする）
- 他のユーザから選択する場合は、[Other user]を選択する  
  選択すると、Username テキストおよび Email テキスト、ゴミ箱アイコン、Newボタンが表示される。
  - WEKO_ITEMS_UI_PROXY_POSTING が False の場合、末尾のユーザの Username テキストと Email テキストのみ活性化し、ゴミ箱アイコンとNew ボタンが非表示となる。
  - [Other user]で未登録の場合：初期表示は、Username テキストと Email テキストは空欄である。
  - [Other user]で登録済みの場合：初期表示は、Username テキストと Email テキストに登録済みのユーザー名とEmailアドレスが表示される。
  - Newボタン押下：Username テキストと Email テキストは空欄で1行追加する。  
    追加できる行に上限はない。
  - ゴミ箱アイコン押下：2行以上存在する場合、1行削除する。
    - 1行のみ存在し、ゴミ箱アイコンを押下した場合、以下のエラーメッセージを表示し、削除をキャンセルする。  
      英語：「At least 1 user is required.」  
      日本語：「ユーザーは1名以上必要です。」
- Username または Email に任意の文字列を入力すると、インクリメンタルサーチでヒットするユーザが候補一覧に自動表示される
  - ヒットするユーザが無い場合、「No result found」のメッセージを候補一覧に表示する
- ユーザ候補一覧よりユーザを選択すると、該当ユーザの「Username」、「Email」が自動入力される
- 「Username」及び「Email」を手動入力することもできる
- ［保存］ボタン、［次へ（Next）］ボタンを押したときに、以下のチェックを行う
  - 入力したUsernameが存在しない、または[Other user]を選択してユーザ設定エリアに何も入力していない場合は、指定されたユーザが存在しない旨メッセージを表示し、入力確定できない  
    メッセージ：  
    「Shared user information is not valid  
    Please check it again!」
  - Usernameを入力しておらず、入力したEmailが存在しない場合は、Usernameの入力が必要である旨のメッセージを表示し、入力確定できない  
    メッセージ：  
    「An error ocurred while processing the input data!  
    Cannot read properties of null (reading 'username')」
  - 入力ユーザがアイテム登録ユーザーであれば、メッセージを表示する  
    メッセージ：「You cannot specify yourself in "Other user" setting.」
  - WEKO_ITEMS_UI_PROXY_POSTING が True で、入力されたメールアドレスに重複がある場合、重複している旨のメッセージを表示し、入力確定できない  
    メッセージ：  
    「Duplicate email addresses found:」
- Contributorとして指定されたユーザは、アイテム登録者と同様に該当アイテムの登録(編集)権限が付与される

## 関連モジュール

- 「weko_items_ui」：代理投稿を登録する処理モジュールである
- 「weko_workflow」：アイテム編集可能な権限をチェックする処理モジュールである

## 処理概要

アイテム登録/編集画面に代理投稿を登録する処理

- アイテム登録/編集画面で「Contributor」エリアのテキストボックスにクリックすると、「get_search_data」メソッドでデータを以下の情報から取得する
  - 「Username」：「userprofiles_userprofile.username」
  - 「Email」：「accounts_user.email」
- 「Contributor」エリアのテキストボックスに任意の文字列を入力すると、ブラウザ側JS（app.js）の「autocomplete」処理で入力したテキストにヒットするデータを候補一覧に表示する
- ユーザ候補一覧よりユーザを選択すると、「validate_user_info」メソッドで選択したユーザー情報をチェックし、ブラウザ側JS（app.js）の「get_autofill_data」処理で「Username」と「Email」テキストにユーザー情報を表示させる
- ［次へ（Next）］または［保存（Save）］ボタンを押すと、代理投稿としてユーザー情報を再度チェックする、問題なければ、入力したユーザーが「shared_user_ids」としてメタデータに保存する

アイテム編集の権限を確認する処理

- アクティビティにアクセスすると、「check_authority_action」メソッドでログインしているユーザーの権限をチェックし、管理者及び登録者以外、ログインしているユーザーIDが「shared_user_ids」に属すれば、アクティビティ詳細画面に移動する

## 設定値

- WEKO_ITEMS_UI_PROXY_POSTING
  - パス：<https://github.com/RCOSDP/weko/blob/develop_v2.0.0/modules/weko-items-ui/weko_items_ui/config.py>
  - 初期値： False
  - 代理投稿を複数登録可能な機能の有効無効を切り替える。
  - scripts/instance.cfg で定義されている場合は、そちらの設定を優先する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 代理投稿は config `WEKO_ITEMS_UI_PROXY_POSTING`（既定 False）。サーバ側 `weko_items_ui.views.get_search_data` / `validate_user_info`、権限判定 `weko_workflow.views.check_authority_action`。`autocomplete` / `get_autofill_data` はブラウザ側JS（`app.js`）。

## 更新履歴

| 日付       | GitHubコミットID                         | 更新内容                             |
| ---------- | ---------------------------------------- | ------------------------------------ |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成                             |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | 設定値による代理投稿者の制御を記載   |
