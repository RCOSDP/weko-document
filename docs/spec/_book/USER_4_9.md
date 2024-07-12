
### Item Registration：インデックス指定

  - > 目的・用途

Item Registrationの一部として、登録先インデックスを指定する。

  - > 利用方法

ワークフローで登録先インデックスを指定している場合、アイテムの登録先インデックスはユーザの操作によらずワークフローで指定したものが設定され、インデックス指定はスキップされる。

ワークフローで登録先インデックスを指定していない場合、アイテムの登録先インデックスは画面上の操作によって設定される。

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

1\. ワークフローの登録先インデックスの設定

  - 【Administration \> ワークフロー管理（WorkFlow） \> ワークフロー（WorkFlow List）画面】で、各ワークフローの登録先インデックスを指定することができる。  
    詳細は、管理機能の[ADMIN-7-2: ワークフロー](#ワークフロー-2)を参照

2\. インデックスを指定する

  - 1\. で登録先インデックスを指定していないワークフローでのItem Registrationであることを前提とする。

  - インデックスツリーからアイテムを所属させるインデックスにチェックを入れる  
    アイテムは同時に複数のインデックスに所属させることができる

  - チェックしてインデックス名が「インデックス指定」（DESIGNATE INDEX）エリアに表示される

  - インデックスを指定した後、［次へ（Next）］ボタン、または「保存」（Save）ボタンを押す場合
    
      - 該当アイテムタイプのマッピングには、問題がある場合、エラーメッセージを表示する  
        エラーメッセージ：「Please make sure the item type mapping is correct.」
    
      - 問題ない場合、該当ワークフローでのステップに進める

  - インデックスを指定しないと、［次へ（Next）］ボタン、または［保存（Save）］ボタンを押すと、エラーメッセージを表示する  
    エラーメッセージ：「At least one index should be selected.」

  - ［強制終了（Quit）］ボタンを押すと、確認ダイヤログを表示する  
    メッセージ：JP：「このアクティビティを終了してもよろしいですか？」  
    　　　　　　EN：「Are you sure you want to quit the activity?」
    
      - ［継続（Continue）］ボタンを押すと、該当アクティビティが強制終了とする
    
      - ［キャンセル（Cancel）］ボタンを押すと、確認ダイヤログを閉じる

  - ［戻る（Back）］ボタンを押すと、「アクティビティ一覧」画面に移動する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > 「weko\_deposit」：ESとrecords\_metadataテーブルへの登録を行う

  - > 「weko\_items\_ui」：ワークフローで登録先インデックスを指定している場合には、ここからweko\_depositの登録処理を呼び出す

  - > 「weko\_workflow」：アクティビティ全体の管理を行う

<!-- end list -->

  - > 処理概要

> アイテムの編集を行う場合、「Item Resistration」のアクション開始時に、get\_pid\_and\_recordメソッドで登録先インデックスの情報を取得する
> 
> 画面でインデックスを指定して［次へ（Next）］ボタンを押すと、weko\_depositのcommitメソッドでESとrecords\_metadataテーブルへの登録を行う
> 
> ワークフローで登録先インデックスを指定している場合には、画面にてweko\_items\_uiのiframe\_items\_indexメソッドを呼び出し→iframe\_items\_indexメソッド中でupdate\_index\_tree\_for\_recordメソッドを呼び出し→update\_index\_tree\_for\_recordメソッド中でweko\_depositのcommitメソッドを呼び出してESとrecords\_metadataテーブルへの登録を行う

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