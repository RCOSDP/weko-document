### Workflow API

- 目的・用途

GakuNinRDMと連携してアイテムを登録する際に使用するAPIである

- 利用方法

scopeに「user:activity」をもつアクセストークンを使用してAPIを呼び出す

| **Method** | **HTTP request** | **Description** |
| ---- | ---- | ---- |
| ActivityActionResource.post | POST `/api/depositactivity` | ワークフローを作成する |
| ActivityActionResource.get | GET `/api/depositactivity/<string:activity_id>` | アクティビティの状態を取得する |
| ActivityActionResource.delete | DELETE `/api/depositactivity/<string:activity_id>` | アクティビティを中断する |

curlによるGETのリクエスト例

```
curl https://ホスト/api/depositactivity/アクティビティID -H "Authorization:Bearer アクセストークン"
```

- 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | |

- 機能内容

- 使用方法については、[その他-10: GakuNinRDM連携](#gakuninrdm連携)を参照

- 関連モジュール

- weko_workflow

- 処理概要

- Scope:
  - /weko-workflow/weko_workflow/scopes.py

- API:
  - /weko-workflow/weko_workflow/views.py

- ActivityActionResourceクラスのメソッドで処理を行う

- POSTの場合、フォームからの送信としてリクエストに以下の情報を含める必要がある
  - アイテムタイプID
  - ファイル

- POST、GETの場合は、返却値はactivity_informationメソッドで作成する

- POSTでは、以下の場合にInvalidInputRESTErrorが発生する
  - アイテムタイプIDまたはファイルがリクエストに含まれない場合
  - ファイルの形式が不正だった場合
  - ファイルの内容が不正だった場合
  - アクティビティを作成または取得できなかった場合

- GETでは、以下の場合にActivityBaseRESTErrorが発生する
  - ActivityBaseRESTError：
    - アクティビティIDが指定されていない場合
  - ActivityNotFoundRESTError：
    - 指定のアクティビティIDでアクティビティを取得できなかった場合

- DELETEでは、以下の場合にエラーが発生する
  - ActivityBaseRESTError：
    - アクティビティIDが指定されていない場合
  - RegisteredActivityNotFoundRESTError：
    - 指定のアクティビティIDでアクティビティを取得できなかった場合
  - DeleteActivityFailedRESTError：
    - 取得したアクティビティのactivity_statusがdoingでない場合
    - 強制終了に失敗した場合

- エラー発生時にはlogging_errorメソッドを呼び出して、ログレベルをINFOとしてログを出力する

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
