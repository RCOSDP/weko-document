
### Item Registration：代理投稿

  - > 目的・用途

Item Registrationの一部として、画面上の設定エリアで代理投稿者を指定する。

  - > 利用方法

アイテムメタデータ登録画面の\[Contributor\]エリアで「Other user」ラジオボタンを選択すると、ユーザ設定エリアが表示される。そこで入力されたユーザを代理投稿者として設定する。

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

1\. アイテムに代理投稿を指定する

  - アイテムメタデータ登録画面に\[Contributor\]エリアを表示する

  - アイテムの登録者は、Contributorをシステムに登録されている他のユーザから選択できる  
    ただし、アイテム登録者は、他ユーザを選択してもContributorとして有効のままとする

  - デフォルトは\[This user\]とする（アイテム登録者のみをContributorとする）

  - 他のユーザから選択する場合は、\[Other users\]を選択する  
    選択すると、ユーザ設定エリア(下記2項目)が表示される
    
      - Username
    
      - Email

  - 上記の2項目に任意の文字列を入力すると、インクリメンタルサーチでヒットするユーザが候補一覧に自動表示される
    
      - ヒットするユーザが無い場合、「No result found」のメッセージを候補一覧に表示する

  - ユーザ候補一覧よりユーザを選択すると、該当ユーザの「Username」、「Email」が自動入力される

  - 「Username」及び「Email」を手動入力することもできる

  - ［次へ（Next）］ボタンを押したときに、以下のチェックを行う
    
      - 入力したUsernameが存在しない、または\[Other users\]を選択してユーザ設定エリアに何も入力していない場合は、指定されたユーザが存在しない旨メッセージを表示し、入力確定できない  
        メッセージ：  
        「Shared user information is not valid  
        Please check it again\!」
    
      - Usernameを入力しておらず、入力したEmailが存在しない場合は、Usernameの入力が必要である旨のメッセージを表示し、入力確定できない  
        メッセージ：  
        「An error ocurred while processing the input data\!  
        Cannot read properties of null (reading 'username')」
    
      - 入力ユーザがアイテム登録ユーザーであれば、メッセージを表示する  
        メッセージ：「You cannot specify yourself in "Other users" setting.」

  - Contributorとして指定されたユーザは、アイテム登録者と同様に該当アイテムの登録(編集)権限が付与される

  - Contributorの設定は1つのユーザのみできる

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > 「weko\_items\_ui」：代理投稿を登録する処理モジュールである

  - > 「weko\_workflow」：アイテム編集可能な権限をチェックする処理モジュールである

<!-- end list -->

  - > 処理概要

> アイテム登録/編集画面に代理投稿を登録する処理

  - > アイテム登録/編集画面で「Contributor」エリアのテキストボックスにクリックすると、「get\_search\_data」メソッドでデータを以下の情報から取得する
    
      - > 「Username」：「userprofiles\_userprofile.username」
    
      - > 「Email」：「accounts\_user.email」

  - > 「Contributor」エリアのテキストボックスに任意の文字列を入力すると、「autocomplete」メソッドで入力したテキストにヒットするデータを候補一覧に表示する

  - > ユーザ候補一覧よりユーザを選択すると、「validate\_user\_info」メソッドで選択したユーザー情報をチェックし、「get\_autofill\_data」メソッドで「Username」と「Email」テキストにユーザー情報を表示させる

  - > ［次へ（Next）］または［保存（Save）］ボタンを押すと、代理投稿としてユーザー情報を再度チェックする、問題なければ、入力したユーザーが「shared\_user\_id」としてメタデータに保存する

> アイテム編集の権限を確認する処理

  - > アクティビティにアクセスすると、「check\_authority\_action」メソッドでログインしているユーザーの権限をチェックし、管理者及び登録者以外、ログインしているユーザーIDが「shared\_user\_id」に属すれば、アクティビティ詳細画面に移動する

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