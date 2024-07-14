### Workflow API

  - 目的・用途

GakuNinRDMと連携してアイテムを登録する際に使用するAPIである

  - 利用方法

scopeに「user:activity」をもつアクセストークンを使用してAPIを呼び出す

<table>
<thead>
<tr class="header">
<th><strong>Method</strong></th>
<th><strong>HTTP request</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ActivityActionResource.post</td>
<td><p>POST</p>
<p>/api/depositactivity</p></td>
<td>ワークフローを作成する</td>
</tr>
<tr class="even">
<td>ActivityActionResource.get</td>
<td><p>GET</p>
<p>/api/depositactivity/&lt;string:activity_id&gt;</p></td>
<td>アクティビティの状態を取得する</td>
</tr>
<tr class="odd">
<td>ActivityActionResource.delete</td>
<td><p>DELETE</p>
<p>/api/depositactivity/&lt;string:activity_id&gt;</p></td>
<td>アクティビティを中断する</td>
</tr>
</tbody>
</table>

curlによるGETのリクエスト例

|                                                                                     |
| ----------------------------------------------------------------------------------- |
| curl <https://ホスト/api/depositactivity/>アクティビティID -H "Authorization:Bearer アクセストークン" |

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

  - 使用方法については、[その他-10: GakuNinRDM連携](#gakuninrdm連携)を参照

<!-- end list -->

  - 関連モジュール

<!-- end list -->

  - weko\_workflow

<!-- end list -->

  - 処理概要

<!-- end list -->

  - Scope:
    
      - /weko-workflow/weko\_workflow/scopes.py

  - API:
    
      - /weko-workflow/weko\_workflow/views.py

  - ActivityActionResourceクラスのメソッドで処理を行う

  - POSTの場合、フォームからの送信としてリクエストに以下の情報を含める必要がある
    
      - アイテムタイプID
    
      - ファイル

  - POST、GETの場合は、返却値はactivity\_informationメソッドで作成する

  - POSTでは、以下の場合にInvalidInputRESTErrorが発生する
    
      - アイテムタイプIDまたはファイルがリクエストに含まれない場合
    
      - ファイルの形式が不正だった場合
    
      - ファイルの内容が不正だった場合
    
      - アクティビティを作成または取得できなかった場合

  - GETでは、以下の場合にActivityBaseRESTErrorが発生する
    
      - ActivityBaseRESTError：
        
          - > アクティビティIDが指定されていない場合
    
      - ActivityNotFoundRESTError：
        
          - > 指定のアクティビティIDでアクティビティを取得できなかった場合

  - DELETEでは、以下の場合にエラーが発生する
    
      - ActivityBaseRESTError：
        
          - > アクティビティIDが指定されていない場合
    
      - RegisteredActivityNotFoundRESTError：
        
          - > 指定のアクティビティIDでアクティビティを取得できなかった場合
    
      - DeleteActivityFailedRESTError：
        
          - > 取得したアクティビティのactibity\_statusがdoingでない場合
        
          - > 強制終了に失敗した場合

  - エラー発生時にはloging\_errorメソッドを呼び出して、ログレベルをINFOとしてログを出力する

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
