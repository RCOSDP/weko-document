
## Approval

  - > 目的・用途

本機能は、ワークフローにて、入力したメタデータの内容を認証する機能である。

本機能は承認者が使用することができる。

  - > 利用方法

承認者は、入力したデータの内容を認証（承認・却下・差し戻し）することができる。

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
<td>○</td>
<td>○</td>
<td>○</td>
<td>※</td>
<td></td>
</tr>
</tbody>
</table>

※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

  - > 機能内容

1\. 承認者として、入力したメタデータの内容を認証する

  - 【前提条件】
    
      - 【Administration \> ワークフロー管理（WorkFlow） \> フロー（Flow List） \> Create Flowの画面】「Approval」のアクションを含むフローを定義する
    
      - 【Administration \> ワークフロー管理（WorkFlow） \> ワークフロー（WorkFlow List） \> Create WorkFlowの画面】  
        「Approval」がフローに含まれるワークフローを定義する

  - 入力したメタデータの内容を認証する
    
      - 「Approval」画面にて、「承認」（Approval）ボタンを押すと、アイテム登録が完了とする
    
      - 「Approval」画面にて、「保存」（Save）ボタンを押すと、入力したメタデータの内容を保存する
    
      - 「Approval」画面にて、「却下」（Reject）ボタンを押すと、ワークフローの１つ前アクションに戻る
    
      - 「Approval」画面にて、「強制終了」（Quit）ボタンを押すと、確認ダイヤログを表示する

> メッセージ：JP：「このアクティビティを終了してもよろしいですか？」  
> 　　　　　　EN：「Are you sure you want to quit the activity?」

  - 「継続」（Continue）ボタンを押すと、該当アクティビティが強制終了とする

  - 「キャンセル」（Cancel）ボタンを押すと、確認ダイヤログを閉じる

<!-- end list -->

  - 「Approval」画面へのアクセス権限がかけられる
    
      - ゲストユーザーに対してログイン画面に移動する
    
      - 権限がないユーザーに対して「権限が必要です」（Permission required）とのメッセージを表示する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_workflow

<!-- end list -->

  - > 処理概要

> ［次へ（Next）］ボタンを押すと呼び出されるnext\_actionメソッド中で、action\_endpointが'approval'であるときに承認処理を行う。

  - > この後にアクションがない場合、メッセージ「server error」が表示されて承認に失敗する。
    
      - > ログにはメッセージ「next\_action: can not get next\_flow\_action」が出力される。

  - > アクティビティ中で識別子を付与する設定を行っていた場合、saving\_doi\_pidstoreメソッドで付与を行う。

  - > フィードバックメールを送信する設定になっている場合、update\_by\_list\_item\_idメソッドでfeedback\_mail\_listテーブルを更新する。

> 直後のアクションが「End」である場合、end\_activityメソッドでアクティビティの完了処理を行う。
> 
> 【補足】
> 
> ワークフローの各画面のモーダル、およびApproval画面から、ファイルをダウンロードできる。
> 
> ファイルサイズが閾値を超えていた場合はマルチパートダウンロードとなる。
> 
> マルチパートダウンロードの詳細は、\[アイテム詳細\]\>\[コンテンツファイル管理\]\>\[ マルチパートダウンロード処理について\]と同様

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