
### Item Registration：フィードバックメール機能

  - > 目的・用途

フィードバックメールの送信有無をアイテム単位で設定する。

  - > 利用方法

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

【前提条件】

  - 【Administration \> 統計（Statistics） \> フィードバックメール（Feedback Mail）画面】で、フィードバックメールを送信する設定になっていること。

  - 詳細は、管理機能の[フィードバックメール](#_フィードバックメール)を参照。

  - アイテム登録画面の一番下での「フィードバックメール送信先」領域にフィードバックメール送信先を設定できる
    
      - ［著者DBから入力（From author DB）］ボタン
        
          - ボタンを押下すると、著者DBの検索ウィンドウが表示される
        
          - 「検索」ボタンを押すと、【Admin \> Setting \> Author Management \> Author ID 】登録された著者DB一覧を表示する
        
          - メールが設定されていない著者がいた場合でも著者を表示するが、Importボタンを非活性にする
            
              - メールアドレスがリストボックスに表示されていない著者を選択すると、リストボックス上にメールアドレスがインポートされる
            
              - メールアドレスがリストボックスに表示された著者を選択すると、以下のエラーメッセージを表示し、リストボックス上にインポートされない  
                エラーメッセージ：「Duplicate Email Addresses.」
    
      - リストボックス
        
          - 送信対象者となる著者のメールアドレスが表示される
        
          - メールアドレスはクリックすると選択できる
        
          - メールアドレスを選択している状態で、\[Delete\]ボタンを押下すると、選択した著者のメールアドレスがリストボックスから消える(送信対象者から外れる)
        
          - リストボックスはテキスト入力できる  
            テキスト入力されたデータの"先頭"と"末尾"にスペースがあった場合はトリム処理をした上で設定する
        
          - 次のアクションに進むタイミングで、リストボックス内のメールアドレスのバリデート処理(メールアドレスとして満たしているか)を行う。
        
          - バリデート処理で問題があった場合、エラーを表示して次のアクションには進めない。
            
              - 入力されたメールアドレスの形式が不正の場合、以下のエラーメッセージを表示する  
                エラーメッセージ：「Invalid email format.」
            
              - 入力されたメールアドレスが重複している場合、以下のエラーメッセージを表示する  
                エラーメッセージ：「Duplicate Email Addresses.」

  - フィードバックメール送信先の設定はアイテムタイプによらず表示されるものとする

  - フィードバックメール送信先は必須項目ではないため、入力しなくても次のアクションへ進める

  - フィードバックメール送信先はメタデータの登録・編集時のみ表示され、当該アイテムの登録者及び管理者は表示される  
    ただし、Contributorとして指定されたユーザは、 アイテム登録者と同様に該当アイテムの登録(編集)権限が付与されるため、フィードバックメール送信先も設定できるものとする

  - フィードバックメール送信先は、承認者が承認をした時点から有効となる

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - 
<!-- end list -->

  - > 処理概要

1\. 設定

> フィードバックメール送信タイミングを設定

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L98>

  - > 設定キー：「send-feedback-mail-schedules」

  - > 設定値: day\_of\_month、hour、minute  
    > 現在の設定値：day\_of\_month='1', hour=0, minute=0

> フィードバックメールの送信履歴の表示件数

  - > パス：modules/weko-admin/weko\_admin/config.py

  - > 設定値：WEKO\_ADMIN\_NUMBER\_OF\_SEND\_MAIL\_HISTORY = 20

> フィードバックメールの送信履歴の送信失敗の表示件数

  - > パス：modules/weko-admin/weko\_admin/config.py

  - > 設定値：WEKO\_ADMIN\_NUMBER\_OF\_FAILED\_MAIL = 10

> フィードバックメールの送信件数を設定

  - > パス：modules/weko-search-ui/weko\_search\_ui/config.py

  - > 設定値：WEKO\_SEARCH\_MAX\_FEEDBACK\_MAIL = 100

> １メールアドレスで送信できるアイテムの数： 最大10,000件を取得(ESの制限値)

2\. 実装方法

> 実装モジュール：weko-admin
> 
> 設定情報を保存する

  - > アイテム登録時、 フィードバックメール送信先を入力する場合、「Approval」ステップに承認した後、  
    > フィードバックメール送信先の情報を以下のように保存される
    
      - > データベースに保存する  
        > テーブル名：feedback\_mail\_list  
        > 保存情報：item\_id、mail\_list
    
      - > Elasticsearchに「feedback\_mail\_list」属性に保存する

  - > 【Administration \> 統計（Statistics） \> フィードバックメール（Feedback Mail）】に入力した情報をデータベースに以下のように保存する  
    > テーブル名：feedback\_email\_setting  
    > 保存情報：is\_sending\_feedback、manual\_mail

> フィードバックメール送信のフロー  
> celaryタスクでフィードバックメールを送信するかどうか、チェックする  
> 「schedule」に設定された時刻にフィードバックメール送信を「task」でのタスク（weko\_admin.tasks.send\_feedback\_mail）で実施する
> 
> (1) 「feed\_back\_email\_setting」の情報を「feedback\_email\_setting」テーブルから取得する
> 
> 　・「is\_sending\_feedback = false」の場合、何も処理しない
> 
> 　・「is\_sending\_feedback = true」の場合、(2)に進む
> 
> (2)Elasticsearchからフィードバックメールの情報を取得する
> 
> 　・アイテムごとの最新版に"feedback\_mail\_list"のデータがあるかどうか、チェックする
> 
> 　"feedback\_mail\_list"のデータがある場合、フィードバックメールの情報を取得する
> 
> (3)アイテムごとの統計情報を「invenio-stats」から「get\_list\_statistic\_data」メソッドで取得する
> 
> 　・閲覧回数
> 
> 　　アイテムID及び統計期間（年、月）の情報を元に「get\_item\_view」メソッドでアイテムごとの閲覧回数を取得する
> 
> 　・ファイルダウンロード回数
> 
> 　　バケツID（bucket\_id）及びファイル名及び統計期間（年、月）の情報を元に、「get\_item\_download」メソッドでファイルダウンロード回数を取得する
> 
> (4)フィードバックメール送信先ごとにアイテムをまとめ、以下の情報を合計する
> 
> 　・アイテム総数
> 
> 　・ファイル総数
> 
> 　・閲覧回数合計
> 
> 　・ファイルダウンロード回数合計
> 
> (5)送信除外対象者を「get\_banned\_mail」メソッドで取得し、送信除外対象者一覧に含まれてないメールアドレスへフィードバックメール送信を実施する
> 
> 　・送信が完了した後、送信履歴をデータベースに保存する
> 
> 　　テーブル名：feedback\_mail\_history
> 
> 　　履歴内容：id、start\_time、end\_time、stats\_date、total\_mail、failed\_mail
> 
> 　・送信が失敗になる場合、送信が失敗する情報をデータベースに保存する
> 
> 　　テーブル名：feedback\_mail\_failed
> 
> 　　履歴内容：id、history\_id、author\_id、mail
> 
> (6)送信履歴を【Admin \> Statistics \> Feedback Mail画面】に表示させる
> 
> 　送信失敗行にて、送信できなかった件数（「エラー」カラム）をアンカーで表示する
> 
> フィードバックメールを再送信する処理に対して「resend\_failed\_mail」のAPIを実施する  
> 再送信結果をデータベースでの該当レコードに更新する

3\. 手動実行

タスクを呼び出すことで任意のタイミングでフィードバックメールを送信する。

|                                                                           |
| ------------------------------------------------------------------------- |
| celery -A invenio\_app.celery call weko\_admin.tasks.send\_feedback\_mail |

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