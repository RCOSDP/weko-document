### Identify設定

## 目的・用途

本機能は、Identifyの作成・編集を行う機能である。Identifyとは、リポジトリに関する情報を検索する場合に使用されるものである。

## 利用方法

【Administration＞OAI-PMH＞Identify】の順で画面遷移して利用する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | | | | |

## 機能内容

- Identify出力に対してリポジトリの情報を設定可能
  - 設定内容
    - Output Set：チェックボックス
      - チェックボックスにチェックを入れる場合、OAI-PMHリクエストに対して、正常レスポンスを返す。
      - チェックボックスにチェックを入れない場合、OAI-PMHリクエストに対して、エラーレスポンスを返す。  
        [エラーと例外状況](https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/OpenArchivesProtocol.htm#ErrorConditions)
    - Emails：管理者メールアドレスを入れる。
    - Repository Name：リポジトリ名を入れる。
    - Earliest Datastamp：Identifyの作成時間を自動で入れる。  
      フォーマット：YYYY-MM-DD HH:MM:SS
  - [保存（Save）]ボタンを押すと、設定された内容をIdentify一覧に追加させ、メッセージをIdentify一覧に表示させる  
    メッセージ：「レコードが正常に作成されました。（Record was successfully saved）」
  - [保存して編集を続ける（Save and Continue Editing）]ボタンを押すと、メッセージを編集画面での上端に表示させ、作成されたIdentiftyの編集を続けることを可能とする。  
    メッセージ：「レコードが正常に作成されました。（Record was successfully saved）」
  - 1つのリポジトリに対して1つしか登録できない。

- OAI-PMHのIdentify情報を返戻可能

  【Admin > OAI-PMH > Identify画面】上の設定値に基づき、OAI-PMHのIdentifyリクエスト(verb=Identify)に対してレスポンス可能とする。詳細は[Web-API API-2:OAI-PMH](#_OAI-PMH)を参照。

## 関連モジュール

- Invenio-oaiserver

## 処理概要

画面表示について

- 一覧タブ  
  invenio_oaiserver.admin.IdentifyModelViewが継承しているModelViewからflask_admin.model.base.index_viewが呼び出され、db内のoaiserver_identifyテーブルより情報を取得し画面に表示する。
- 編集タブ  
  [鉛筆]ボタン押下時、invenio_oaiserver.admin.IdentifyModelViewが継承しているModelViewからflask_admin.model.base.edit_viewが呼び出され、db内のoaiserver_identifyテーブルより情報を取得し編集画面へ遷移する。
  - 編集画面で[保存（Save）]ボタンもしくは[保存して編集を続ける（Save and Continue Editing）]を押下時、flask_admin.model.base.edit_viewが呼び出され、編集内容をdb内のoaiserver_identifyテーブルに保存し、更新する。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
