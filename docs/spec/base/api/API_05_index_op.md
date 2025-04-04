### Index操作API

  - 目的・用途

新規インデックスを作成する際に使用するAPIである

  - 利用方法

Scopeに「index:create」をもつアクセストークンを使用してAPIを呼び出す

| **Method**    | **HTTP request**           | **Description** |
| ------------- | -------------------------- | --------------- |
| create\_index | POST /api/indextree/create |                 |

パラメータは以下の内容のjsonとする

| **Parameter name**                 | **Value** | **Description**       |
| ---------------------------------- | --------- | --------------------- |
| Path parameters                    |           |                       |
| parent\_id                         | 数値        | 親インデックスのID            |
| index\_info                        | json      | 必須。以下の項目のうち少なくとも1つが必要 |
| index\_info.index\_name            | 文字列       | 日本語のインデックス名           |
| index\_info.index\_name\_english   | 文字列       | 英語のインデックス名            |
| index\_info.comment                | 文字列       | コメント                  |
| index\_info.public\_state          | 真偽値       | 公開設定                  |
| index\_info.harvest\_public\_state | 真偽値       | ハーベスト公開設定             |

curlによるリクエスト例

|                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| curl https://ホスト/api/indextree/create -H "Authorization:Bearer アクセストークン" -H "Content-Type: application/json" -d '{"parent\_id":"0","index\_info":{"index\_name":"APIテスト","index\_name\_english":"API test","comment":"コメント","public\_state":false,"public\_state":false}}' |

  - 利用可能なロール

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
<td>○</td>
<td></td>
</tr>
</tbody>
</table>

  - 機能内容

<!-- end list -->

  - 以下を指定してインデックスを新規作成する
    
      - 親インデックス

  - > 指定されなかった場合はRoot Index直下に作成される
    
      - 日本語のインデックス名
    
      - 英語のインデックス名

  - > 各インデックス名は、指定されなかった場合は「New Index」が設定される
    
      - コメント
    
      - 公開設定

  - > 指定されなかった場合は「False」が設定される
    
      - ハーベスト公開設定

  - > 指定されなかった場合は「True」が設定される

<!-- end list -->

  - 関連モジュール

<!-- end list -->

  - weko\_index\_tree

<!-- end list -->

  - 処理概要

<!-- end list -->

  - Scope:
    
      - weko- index-tree /weko\_ index\_tree /scopes.py

  - API:
    
      - modules/weko-index-tree/weko\_index\_tree/views.py

  - create\_index関数でindexテーブルに新規インデックスを作成する
    
      - 以下の情報を用いてインデックスを新規作成する

  - > id：作成時のUNIX時間を1000倍したものを用いる

  - > parent\_id：パラメータで指定されなかった場合には0を設定する

  - > index\_name：「New Index」固定
    
      - 作成したインデックスを、index\_infoの内容を用いてupdateする
    
      - 作成が成功すると、以下の内容のレスポンスが返却される

  - > Indexes.updateメソッドの返却値をjson形式にエンコードしたものをレスポンスボディに入れようとする

  - > しかし、updateメソッドの返却値はNoneなので、実際に入るのはエラーメッセージ「'NoneType' object is not iterable」である
    
      - パラメータとして空のjsonを渡した場合は、400エラーとなりエラーメッセージ「No data to create.」が返却される
    
      - index\_infoが空だった場合は、400エラーとなりエラーメッセージ「index\_info can not be null.」が返却される

<!-- end list -->

  - 更新履歴

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
</tbody>
</table>

