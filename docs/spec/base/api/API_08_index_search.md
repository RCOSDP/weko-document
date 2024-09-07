### インデックス検索用API

  - 目的・用途

インデックスIDを指定しての検索機能を提供する。

  - 利用方法

| **Method** | **HTTP request**   | **Description** |
| ---------- | ------------------ | --------------- |
|            | **GET /api/index** | アイテムを検索する       |

クエリパラメータ

| **GET /api/opensearch/search** |    |     |             |
| ------------------------------ | -- | --- | ----------- |
| パラメータ                          | 必須 | 値   | 説明          |
| q                              | 〇  | int | インデックスIDを指定 |

レスポンス例：



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
<td>〇</td>
<td>〇</td>
<td>〇</td>
<td>〇</td>
<td>〇</td>
<td>〇</td>
</tr>
</tbody>
</table>

  - 機能内容

  - 関連モジュール

  - 処理概要

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
<p>2023/11/14</p>
</blockquote></td>
<td>V0.9.27</td>
<td>初版作成</td>
</tr>
</tbody>
</table>
