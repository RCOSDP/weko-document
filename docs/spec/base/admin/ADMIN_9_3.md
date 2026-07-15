### Sets

## 目的・用途

本機能は、setの作成・編集を行う機能である（実装上、削除は不可＝`can_delete=False`）。Setとは、選択的ハーベスティングを行う目的でアイテムをグループ化するための任意の構成隊のことを示す。

## 利用方法

【Administration＞OAI-PMH＞Sets】の順で画面遷移して利用する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | | | |

## 機能内容

- 【Administration > OAI-PMH > Sets 】：アイテムをグループ化する情報を設定可能。
  - 設定内容
    - Created、Updated：カレンダーから選択可能。  
      フォーマット：YYYY-MM-DD HH:MM:DD」  
      デフォルト：現在のシステム時刻を自動的に入れる
    - Spec：スペックの情報を入れる。ユニークとする。入力必須項目。
    - Name：セットの命名を入れる
    - Description：セットの説明を入れる
    - Search Pattern
  - 「保存（Save）」ボタンを押すと、設定されたセット内容をセット一覧に追加させ、メッセージをセット一覧に表示させる  
    メッセージ：「レコードが正常に作成されました。（Record was successfully saved）」
  - [保存してもう一つ追加（Save Add Another）]ボタンを押すと、設定されたセット内容をセット一覧に追加させ、他のセットを追加設定可能とする。
  - [保存して編集を続ける（Save and Continue Editing）]ボタンを押すと、設定されたセット内容をセット一覧に追加させ、該当セットの編集を続けることを可能とする。
  - Sets一覧は、更新日時降順で表示されている。

- 使い方
  - 【ハーベスト機関元】
    - 【Administration >コミュニティ管理（ Communities） >コミュニティ（Community）】においてコミュニティを新規作成すると、  
      作成されたコミュニティに対して、【Administration > OAI-PMH > Sets】に以下のセットが自動作成される。  
      「Spec」：「user-」+ コミュニティID  
      「Name」：コミュニティID  
      「Updated」、「Created」：セット作成時間
    - OAISetにそれぞれのアイテムを登録する際は以下のコマンドを実行する。  
      「community_id」：該当コミュニティ  
      「record_id」：アイテムのuuid値

      ```
      docker-compose exec web invenio communities request -a community_id record_id
      ```
  - 【ハーベスト機関先】  
    ハーベスト設定画面での「Set Spec」に該当「Spec」値をいれば、登録アイテムをハーベストできる。

## 関連モジュール

- Invenio_oaiserver

## 処理概要

画面表示について

- 一覧タブ  
  invenio_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask_admin.model.base.index_viewが呼び出され、db内のoaiserver_setテーブルより情報を取得し画面に表示する。
- 編集タブ  
  [鉛筆]ボタン押下時、invenio_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask_admin.model.base.edit_viewが呼び出され、db内のoaiserver_setテーブルより情報を取得し編集画面へ遷移する。
  - 編集画面で[保存（Save）]ボタンもしくは[保存して編集を続ける（Save and Continue Editing）]を押下時、flask_admin.model.base.edit_viewが呼び出され、編集内容をdb内のoaiserver_setテーブルに保存し、更新する。
- 作成タブ  
  作成タブに遷移時、invenio_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask_admin.model.base.create_viewが呼び出される。
  - 情報の入力後に[保存（Save）]ボタン押下すると、invenio_oaiserver.admin.OAISetModelViewが継承しているModelViewからflask_admin.model.base.create_viewが呼び出され、新しいSetの情報をdb内のoaiserver_setテーブルに保存する。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_oaiserver.admin.OAISetModelView`（endpoint `oaiset`、テーブル `oaiserver_set`、カテゴリ OAI-PMH）。`column_default_sort=('updated', True)`（更新日時降順）。
- 実装補足：`can_delete=False`（**削除不可**）。`can_create=True` / `can_edit=True`。`edit_form` で `del form.spec`（Spec は作成後編集不可）。本 ModelView にリポジトリ絞り込みは無く、アクセス制御は権限機構に依存。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2025/01/23 | - | サブリポジトリ対応 |
