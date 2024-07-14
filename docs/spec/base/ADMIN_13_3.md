### アクセス\_ユーザー

  - > 目的・用途

本機能は、個別のユーザーに付与する権限を管理する機能である。

  - > 利用方法

【Administration \> ユーザー管理（User Management） \> アクセス：ユーザー（Access: Users）画面】にて操作を行う。

  - > 利用可能なロール

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 画面の主な構成と操作方法は、【アクセス：ロール（Access: Roles）画面】と同様である。[ADMIN-13-1: アクセス\_ロール](\\l)を参照すること。
    
      - 一覧（List）タブでは、【アクセス：ロール（Access: Roles）画面】の「Role」と異なり「User ID」と「Email」が表示される。
        
          - 「User ID」と「Email」には、accounts\_userテーブルの「id」「email」フィールドの値が表示される。
    
      - 「作成」（Create）タブでは、【アクセス：ロール（Access: Roles）画面】の「Role」と異なり「User」を選択する。
        
          - 「User」の選択肢として、accounts\_userテーブルに登録されたユーザーが表示される。
        
          - 各選択肢は、「User\<id=(レコードのid), email=(レコードのemail)\>」の形で表示される。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio\_access（WEKOソース内にforkされていない）

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 画面の設定をもとに、以下のようにaccess\_actionsusersテーブルに保存する。
    
      - 「id」フィールド：画面上の入力によらない
    
      - 「action」フィールド：画面上の「Action」で選択されたもの
    
      - 「exclude」フィールド：画面上の「Deny」にチェックが入っていたらTrue、そうでなければFalse
    
      - 「argument」フィールド：画面上の「Argument」の入力値
    
      - 「user\_id」フィールド：画面上の「User」で選択されたユーザーのid

  - 各actionは、関数へのアノテーションでアクセス制御に利用する。

<!-- end list -->

  - > 更新履歴

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
