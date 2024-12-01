### WebAPIアカウント

  - > 目的・用途

本機能は、アイテムメタデータ自動入力機能におけるAPIアカウント認証で使用する情報を設定する機能である

  - > 利用方法

【Administration \> 設定（Setting） \> WebAPIアカウント（WebAPI Account）画面】にてアイテムメタデータ自動入力機能で連携するWeb APIのアカウント情報を設定する

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

  - v0.9.22では、CrossRefのみ対応している

  - 設定項目は以下とする
    
      - 「入力タイプ」（Input Type） ：タイプを選択する
        
          - 画面表示時の選択値は、「入力タイプを選択してください」（Please selected the input type）
    
      - 各種APIに必要なアカウント設定フィールド
        
          - 入力タイプで "CrossRef" を選択した場合は、以下の入力フィールドを表示する  
            「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）

  - ［保存（Save）］ボタンを押すと入力内容のチェックを行い、エラーがなければ設定情報が保存される
    
      - 「入力タイプ」（Input Type）の選択値が「入力タイプを選択してください」（Please selected the input type）である間、［保存（Save）］ボタンは非活性である
    
      - 「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）が空の状態でボタンを押すと、保存されずに以下のエラーメッセージがポップアップで表示される  
        エラーメッセージ：「Account information is invalid. Please check again.」
    
      - 「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）に入力値がある場合は、その内容を使って接続の確認を行い、正常に接続できなかった場合は、保存されずに保存されずに以下のエラーメッセージがポップアップで表示される  
        エラーメッセージ：  
        　日本語：「アカウント情報が無効です。再度確認してください」  
        　英語：「Account information is invalid. Please check again.」
    
      - エラーが発生しなかった場合は、以下のメッセージが表示される  
        メッセージ：「Account info has been saved successfully.」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_admin

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 画面表示時は、weko\_admin.admin.WebApiAccount.indexメソッドがGETで呼び出される
    
      - テーブルから情報を取得するなどの処理は行わない

  - 「入力タイプ」（Input Type）でタイプを選択すると、weko\_admin.views. get\_curr\_api\_cert関数が呼び出される
    
      - この中では、weko\_admin.utils.get\_current\_api\_certification関数で、api\_certificateテーブルから「入力タイプ」（Input Type）の選択値のvalueと「api\_code」フィールドが一致するレコードを取得する
    
      - 取得した値を、「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）入力フィールドに設定する

  - ［保存（Save）］ボタンを押すと、web\_api\_account.jsで入力値のチェックを行い、エラーがなければweko\_admin.views. save\_api\_cert\_data関数がajaxで呼び出される
    
      - 「CrossRefクエリサービスアカウント」（CrossRef Query Services Account）が空だった場合のチェックはweb\_api\_account.jsで行う
    
      - save\_api\_cert\_data関数の中で、weko\_admin.utils.calidate\_certification関数によって接続確認を行う
    
      - 接続確認に成功した場合に、api\_certificateテーブルに「入力タイプ」（Input Type）の選択値のvalueと「api\_code」フィールドが一致するレコードがあるかどうか確認して、あった場合にそのレコードを更新する

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
