### OAuthアプリケーショントークン

## 目的・用途

本機能は、管理者として登録されているOAuthアプリケーショントークンを閲覧、編集、削除する機能である。

※invenioデフォルト機能を使用

## 利用方法

【Administration > ユーザー管理(User Management) > OAuthアプリケーショントークン(OAuth Application Tokens)】を表示する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | | | | | |

## 機能内容

- 【OAuthアプリケーショントークン(OAuth Application Tokens)画面】には以下のタブが表示される
  - 一覧（List）
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

- 「一覧」（List）タブにトークン一覧を表示する。
  - 表示項目は以下の通りである。
    - チェックボックス
    - アクセス（閲覧・編集・削除）
      - 目のマークを押すと「詳細」タブに遷移する。
      - 鉛筆のマークを押すと「編集」タブに遷移する。
      - ゴミ箱のマークを押すとその行のトークンは削除される。
        なお、oauth2server_tokenテーブルからは削除されるがoauth2server_clientテーブルの対応したものは削除されない。
    - 「Id」：トークンのID
    - 「Client Id」：OAuthアプリケーション側のID
    - 「User Id」：接続するユーザーID
    - 「Token Type」：bearerのみ
    - 「Expires」：有効期限

  - 左から2列目にある目アイコンを押すと、該当トークンの詳細情報を「詳細」（Details）タブに表示する
    - 表示項目：Id, Client id, User Id', Token Type, Expires

  - 左から２列目にある鉛筆アイコンを押すと、「編集」（Edit）タブに表示し、ユーザーの情報が編集できる
    - 編集可能な項目は以下の通りである
      - 「Client」
        - 選択肢：OAuthアプリケーションにて登録されているものからプルダウンで選択する。
        - 部分一致検索ができる。
        - 必須項目である。
      - 「User」
        - 選択肢：登録されているユーザーから選択する。
        - 部分一致検索ができる。
      - 「Token Type」:対応しているものはbearerのみである。
        ただし、編集、保存する際は自由記述
      - 「Expires」:カレンダーから指定できる。
      - 「Is Personal」：個人用
      - 「Is Internal」：内部用
    - 「保存」（Save）ボタンを押すと、編集内容を保存し、メッセージを一覧画面の上部に表示する
      メッセージ：
      　日本語：「レコードが正常に保存されました。」
      　英語：「Record was successfully saved.」

  - 複数のトークンを一度に削除する。
    - 左端のチェックボックスにチェックを入れ、選択タブから「削除」を選ぶと、削除するかの確認アラートが表示される、
      - OKを押すとチェックボックスにチェックを入れた行のトークンは削除される。
      - キャンセルを押すとキャンセルできる。

## 関連モジュール

- invenio_oauth2server
- flask_admin: <https://github.com/flask-admin/flask-admin/blob/e764f6f0be3facbefb2b4d30b5c3f2f2c630d530/flask_admin/model/base.py>

## 処理概要

OAuthアプリケーショントークン画面の処理について（以下トークン画面とする）

- トークン画面を表示する。この操作によって、invenio_oauth2server.admin.TokenViewが継承したModelViewよりflask_admin.model.base.index_viewメソッドを呼び出す。このメソッドでoauth2server_tokenテーブルよりトークン情報を取得し、TokenViewcolumn_listにあるキーに対応する情報を画面に表示する。
  - トークン詳細画面を表示する。この操作によって、invenio_oauth2server.admin.TokenViewが継承したModelViewよりflask_admin.model.base.details_viewメソッドを呼び出す。このメソッド下でoauth2server_tokenテーブルよりトークン情報を取得し、TokenViewのcolumn_details_listにあるキーに対応する情報を画面に表示する。
- トークン編集画面を表示する。この操作によって、invenio_oauth2server.admin.TokenViewが継承したModelViewよりflask_admin.model.base.edit_viewメソッドをGETで呼び出す。このメソッド下で開いたid列を用いて、oauth2server_tokenテーブルよりトークン情報を取得し、表示する。
  - トークン編集画面で「保存」ボタンを押下する。この操作によって、flask_admin.model.base.edit_viewメソッドをPOSTで呼び出す。このメソッド下で、get_save_return_urlメソッドが呼ばれ、編集内容をoauth2server_tokenテーブルに保存し、更新する。
- トークン画面に表示される表の左から２列目のゴミ箱マークを押下する。この操作によって、invenio_oauth2server.admin.TokenViewが継承したModelViewよりflask_admin.model.base.delete_viewメソッドを呼び出す。このメソッド下でdelete_modelメソッドが呼ばれ、押下したゴミ箱の行のトークンをoauth2server_tokenテーブルから削除する。
- トークン画面に表示される表の左端のチェックボックスにチェックを入れ、選択タブから「削除」を押下する。この操作によってinvenio_oauth2server.admin.TokenViewが継承したModelViewよりflask_admin.model.base.action_viewメソッドを呼び出す。ここでDeleteRowActionが呼ばれ、チェックを入れた行のトークンをoauth2server_tokenテーブルから削除する。

トークン情報は以下のようなデータベースに保存する。

- テーブル名：「oauth2server_token」
- フィールド名：
  ・「id」
  ・「client_id」
  ・「user_id」
  ・「token_type」
  ・「access_token」
  ・「refresh_token」
  ・「expires」
  ・「_scopes」
  ・「is_personal」
  ・「is_internal」

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_oauth2server.admin.TokenView`（model `Token`、テーブル `oauth2server_token`、`can_create=False`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
