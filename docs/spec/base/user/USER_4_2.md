# ワークフロー一覧表示

## 目的・用途

ワークフロー一覧はアイテムを登録するためにワークフローを選択する（アクティビティを新規作成する）機能である。

## 利用方法

ワークフロー一覧で、登録したいアイテムのワークフローの行にある\[新規（New）\]ボタンを押下することで、アイテム登録のワークフローが起動される。

## 利用可能なロール

<table>
<thead>
<tr class="header">
<th>ロール</th>
<th>システム<br />
管理者</th>
<th>リポジトリ<br />
管理者</th>
<th>コミュニティ<br />
管理者</th>
<th>登録ユーザー</th>
<th>一般ユーザー</th>
<th>ゲスト<br />
(未ログイン)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>利用可否</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## 機能内容

- 【アクティビティ一覧画面】から\[New Activity\]ボタンを押すと、【ワークフロー一覧画面】に移動する

- 以下のようなワークフロー情報を表示する

| \# | 表示項目               | 説明       |
| -- | ------------------ | -------- |
| 1  | No.                |          |
| 2  | ワークフロー（WorkFlow）   | ワークフロー名  |
| 3  | アイテムタイプ（Item Type） | アイテムタイプ名 |
| 4  | フロー（Flow）          | フロー名     |
| 5  | ［新規］（New）ボタン       |          |

- ワークフロー一覧から、［新規］（New）ボタンを押すと、該当アクティビティを新規作成する

-  ワークフロー一覧画面及びアクティビティへのアクセス制限がかけられる
    - アクセス権限のないユーザーは\[WorkFlow\]タブが表示されず、画面上の操作によってはワークフロー一覧画面に到達できないが、URLを用いて直接画面に移動しようとした場合には以下のようにしてアクセスを拒否する。
  - ゲストユーザーに対してログイン画面に移動する
  - 権限がないユーザーに対して「権限が必要です」とのメッセージを表示する

- アクティビティの実行に制約をかける。 
  - 同一ユーザによる複数アクティビティの実行を禁止する。
  - 同一アクティビティを複数ユーザが開けないようロックする（/workflow/activity/lock/<ActivityID>）。

## 関連モジュール
  
- weko\_workflow


## 処理概要

> ワークフロー一覧

  - > \[New Activity\]ボタンを押すと、ワークフロー一覧の情報をデータベースから「new\_activity」メソッドで取得する。各ワークフローの情報は、WorkFlowクラスで扱われる。
    
      - > テーブル名：workflow\_workflow、workflow\_flow\_define、item\_type、files\_location
    
      - > 取得情報：

> ・flows\_id
> 
> ・flows\_name
> 
> ・itemtype\_id
> 
> ・itemtype
> 
> ・index\_tree\_id
> 
> ・flow\_id
> 
> ・flow\_define
> 
> ・is\_deleted
> 
> ・open\_restricted
> 
> ・location\_id
> 
> ・location
> 
> ・is\_gakuninrdm

  - > これらのうち、表示に使用するのは以下である。

> ・flows\_name
> 
> ・itemtype
> 
> ・flow\_define

  - > 取得されたワークフロー一覧の情報を以下のテンプレートで表示する
    
      - > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/templates/weko_workflow/workflow_list.html>

> ワークフローのactivity\_idの採番ロジックは以下の通り。  
> 「A-YYYYMMDD-nnnnn」の形式で生成される。（nnnnn=00001 を初期値としてアクティビティを生成する度にカウントアップする）
> 
> def get\_new\_activity\_id(self):
> 
> """Get new an activity ID.
> 
> :return: activity ID.
> 
> """
> 
> number = 1
> 
> try:
> 
> \# Table lock for calculate new activity id
> 
> if db.get\_engine().driver\!='pysqlite':
> 
> db.session.execute(
> 
> 'LOCK TABLE ' + ActivityCount.\_\_tablename\_\_ + ' IN EXCLUSIVE MODE')
> 
> \# Calculate activity\_id based on id
> 
> utc\_now = datetime.utcnow()
> 
> current\_date = utc\_now.strftime("%Y-%m-%d")
> 
> today\_count = ActivityCount.query.filter\_by(date=current\_date).one\_or\_none()
> 
> \# Cannot use '.with\_for\_update()'. FOR UPDATE is not allowed
> 
> \# with aggregate functions
> 
> if today\_count:
> 
> \# Calculate aid
> 
> number = today\_count.activity\_count + 1
> 
> if number \> current\_app.config\['WEKO\_WORKFLOW\_MAX\_ACTIVITY\_ID'\]:
> 
> raise IndexError('The number is out of range \\
> 
> (maximum is {}, current is {}'.format(current\_app.config\['WEKO\_WORKFLOW\_MAX\_ACTIVITY\_ID'\],number))
> 
> today\_count.activity\_count = number
> 
> else:
> 
> \# The default activity Id of the current day
> 
> \_activty\_count = ActivityCount(date=current\_date, activity\_count=number)
> 
> db.session.add(\_activty\_count)
> 
> prev\_counts = ActivityCount.query.filter(ActivityCount.date\<current\_date).all()
> 
> if prev\_counts:
> 
> for prev\_count in prev\_counts:
> 
> db.session.delete(prev\_count)
> 
> except SQLAlchemyError as ex:
> 
> raise ex
> 
> except IndexError as ex:
> 
> raise ex
> 
> \# Activity Id's format
> 
> activity\_id\_format = current\_app.\\
> 
> config\['WEKO\_WORKFLOW\_ACTIVITY\_ID\_FORMAT'\]
> 
> \# A-YYYYMMDD-NNNNN (NNNNN starts from 00001)
> 
> date\_str = utc\_now.strftime("%Y%m%d")
> 
> \# Define activity Id of day
> 
> return activity\_id\_format.format(
> 
> date\_str,
> 
> '{inc:05d}'.format(inc=number))

### アクティビティロックの仕組み

- ユーザが現在開いているアクティビティIDがredisのキー「workflow_userlock_activity_<user_id>」に格納される。
- アクティビティを開いているユーザはredisのキー「workflow_locked_activity_<avtivity_id>」に値「<user_id>-str(int(datetime.timestamp(datetime.now()) * 10 ** 3))」という形式で格納される
- アクティビティのロック解除はブラウザの「beforeunloadイベント」 や 「unloadイベント」をとらえ、アンロックを行うAPIを呼び出している。※「beforeunloadイベント」 や 「unloadイベント」の発火率がブラウザにより安定しないため、ユーザが自身でアンロックするボタンも設けた。


## 更新履歴

<table>
<thead>
<tr class="header">
<th>日付</th>
<th>GitHubコミットID</th>
<th>更新内容</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>