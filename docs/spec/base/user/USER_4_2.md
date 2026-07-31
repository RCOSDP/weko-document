# ワークフロー一覧表示

## 目的・用途

ワークフロー一覧はアイテムを登録するためにワークフローを選択する（アクティビティを新規作成する）機能である。

## 利用方法

ワークフロー一覧で、登録したいアイテムのワークフローの行にある[新規（New）]ボタンを押下することで、アイテム登録のワークフローが起動される。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       〇       |        〇        |         〇         |      〇      |      ×      |        ×          |


## 機能内容

- 【アクティビティ一覧画面】から[New Activity]ボタンを押すと、【ワークフロー一覧画面】に移動する

- 以下のようなワークフロー情報を表示する

|  # | 表示項目                    | 説明             |
| -- | --------------------------- | ---------------- |
| 1  | No.                         |                  |
| 2  | ワークフロー（WorkFlow）    | ワークフロー名   |
| 3  | アイテムタイプ（Item Type） | アイテムタイプ名 |
| 4  | フロー（Flow）              | フロー名         |
| 5  | ［新規］（New）ボタン       |                  |

- ワークフロー一覧から、［新規］（New）ボタンを押すと、該当アクティビティを新規作成する

-  ワークフロー一覧画面及びアクティビティへのアクセス制限がかけられる
    - アクセス権限のないユーザーは[WorkFlow]タブが表示されず、画面上の操作によってはワークフロー一覧画面に到達できないが、URLを用いて直接画面に移動しようとした場合には以下のようにしてアクセスを拒否する。
  - ゲストユーザーに対してログイン画面に移動する
  - 権限がないユーザーに対して「権限が必要です」とのメッセージを表示する

- アクティビティの実行に制約をかける。 
  - 同一ユーザによる複数アクティビティの実行を禁止する。
  - 同一アクティビティを複数ユーザが開けないようロックする（/workflow/activity/lock/<ActivityID>）。

## 関連モジュール

- weko_workflow


## 処理概要

### ワークフロー一覧

[New Activity]ボタンを押すと、ワークフロー一覧の情報をデータベースから「new_activity」メソッドで取得する。  
各ワークフローの情報は、WorkFlowクラスで扱われる。

テーブル名：workflow_workflow、workflow_flow_define、item_type、files_location

取得情報：
  - flows_id
  - flows_name
  - itemtype_id
  - itemtype
  - index_tree_id
  - flow_id
  - flow_define
  - is_deleted
  - open_restricted
  - location_id
  - location
  - is_gakuninrdm

これらのうち、表示に使用するのは以下である。

- flows_name
- itemtype
- flow_define

取得されたワークフロー一覧の情報を以下のテンプレートで表示する  
<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/templates/weko_workflow/workflow_list.html>

 ワークフローのactivity_idの採番ロジックは以下の通り。  
登録・更新用アクティビティは 「A-YYYYMMDD-nnnnn」、削除用アクティビティは「D-YYYYMMDD-nnnnn」の形式で生成される。  
（nnnnn=00001 を初期値としてアクティビティを生成する度にカウントアップする）

```python
WEKO_WORKFLOW_ACTIVITY_ID_FORMAT = 'A-{}-{}'
"""Activity Id's format (A-YYYYMMDD-NNNNN with NNNNN starts from 00001)."""

WEKO_WORKFLOW_DELETION_ACTIVITY_ID_FORMAT = 'D-{}-{}'
"""Deletion Activity Id's format (D-YYYYMMDD-NNNNN with NNNNN starts from 00001)."""

def get_new_activity_id(self, for_delete=False):
    """Get new an activity ID.

    :return: activity ID.
    """
    number = 1
    try:
        # Table lock for calculate new activity id
        if db.get_engine().driver!='pysqlite':
            db.session.execute(
                'LOCK TABLE ' + ActivityCount.__tablename__ + ' IN EXCLUSIVE MODE'
            )

        # Calculate activity_id based on id
        utc_now = datetime.now(timezone.utc)
        current_date = utc_now.strftime("%Y-%m-%d")
        today_count = ActivityCount.query.filter_by(date=current_date).one_or_none()
        # Cannot use '.with_for_update()'. FOR UPDATE is not allowed
        # with aggregate functions

        if today_count:
            # Calculate aid
            number = today_count.activity_count + 1
            if number > current_app.config['WEKO_WORKFLOW_MAX_ACTIVITY_ID']:
                raise IndexError(
                    'The number is out of range (maximum is {}, current is {}'
                    .format(current_app.config['WEKO_WORKFLOW_MAX_ACTIVITY_ID'], number)
                )
            today_count.activity_count = number
        else:
            # The default activity Id of the current day
            _activty_count = ActivityCount(date=current_date, activity_count=number)
            db.session.add(_activty_count)
            prev_counts = ActivityCount.query.filter(ActivityCount.date<current_date).all()
            if prev_counts:
                for prev_count in prev_counts:
                    db.session.delete(prev_count)
    except SQLAlchemyError as ex:
        raise ex
    except IndexError as ex:
        raise ex

    # Activity Id's format
    activity_id_format = (
        current_app.config["WEKO_WORKFLOW_ACTIVITY_ID_FORMAT"]
        if not for_delete
        else current_app.config["WEKO_WORKFLOW_DELETION_ACTIVITY_ID_FORMAT"]
    )

    # A-YYYYMMDD-NNNNN (NNNNN starts from 00001)
    date_str = utc_now.strftime("%Y%m%d")

    # Define activity Id of day
    return activity_id_format.format(
        date_str, "{inc:05d}".format(inc=number)
    )
```

### アクティビティロックの仕組み

- ユーザが現在開いているアクティビティIDがredisのキー「workflow_userlock_activity_<user_id>」に格納される。
- アクティビティを開いているユーザはredisのキー「workflow_locked_activity_<avtivity_id>」に値「<user_id>-str(int(datetime.timestamp(datetime.now()) * 10 ** 3))」という形式で格納される
- アクティビティのロック解除はブラウザの「beforeunloadイベント」 や 「unloadイベント」をとらえ、アンロックを行うAPIを呼び出している。※「beforeunloadイベント」 や 「unloadイベント」の発火率がブラウザにより安定しないため、ユーザが自身でアンロックするボタンも設けた。

| Redisキー名 | 説明 |キー名例|値例|
| ---- | ---- |---- | ---- |
| workflow_userlock_activity_<user_id> | TD |cache::workflow_userlock_activity_1||
| workflow_locked_activity_<avtivity_id> | TD |cache::workflow_locked_activity_A-20241031-00004||


## 実装補足（v2.0.2 実装との突き合わせ）

- アクティビティID採番は `weko_workflow.api.WorkActivity.get_new_activity_id`（`A-{}-{}` / 削除は `D-{}-{}`）。ロックは `views.lock_activity` / `unlock_activity`（Redis `workflow_userlock_activity_<user_id>` / `workflow_locked_activity_<activity_id>`）。一覧は `new_activity` → `WorkFlow.get_workflow_list` → `get_workflows_by_roles`。

## 更新履歴

| 日付       | GitHubコミットID                           | 更新内容                                            |
| ---------- | ------------------------------------------ | --------------------------------------------------- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562   | 初版作成                                            |
| 2024/07/01 | 7733de131da9ad59ab591b2df1c70ddefcfcad98   | v1.0.7対応                                          |
| 2025/07/17 |                                            | 削除用ワークフローのactivity_idの採番ロジックを記載 |
