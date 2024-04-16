
### Item Link

  - > 目的・用途

本機能は、システムに登録している他のアイテムを関連付ける機能である。

  - > 利用方法

「Item Link」アクションを含むフローを使ったワークフローによるアクティビティを開始していることを前提とする。

フローで「Item Link」アクションより前に設定されたアクションが完了すると、「Item Link」アクションが表示される。

「Item Link」アクションで関連アイテムを指定後、\[次へ\]ボタンを押下することで、次のアクションに進む。

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

1\. 登録者として、アイテム間リンクを設定する

  - 【前提条件】
    
      - 【Administration \> ワークフロー管理（WorkFlow） \> フロー（Flow List） \> Create Flowの画面】「Item Registration」のアクション後に「Item Link」のアクションを行うフローを定義する
    
      - 【Administration \> ワークフロー管理（WorkFlow） \> ワークフロー（WorkFlow List） \> Create WorkFlowの画面】  
        「Item Link」がフローに含まれるワークフローを定義する

  - 【Item Link】画面にアイテム間リンクを設定する
    
      - インデックスツリーから任意のインデックスを選択する
        
          - 選択したインデックス名が「インデックスを指定」（Designate Index）エリアに表示される
        
          - 選択インデックス配下のアイテムが「アイテムリンク」(ItemLink）エリアに一覧表示される  
            一覧表示ソートは、アイテム検索結果一覧のデフォルトソートと同じとする
            
              - 「アイテムリンク」(ItemLink）エリアに表示項目は以下の通りである
                
                  - No.
                
                  - Title：アイテムのタイトル
                
                  - Item Type：対象アイテムタイプ
                
                  - Add
    
      - アイテム間リンクを設定したいアイテムの「Add」列に「+」ボタンを押すと、アイテムリンク表の上部にアイテム間リンクの関係性選択のプルダウンが表示される
    
      - プルダウンから関係性を選択する
    
      - 「Delete」ボタンを押すと、設定済みのアイテム間リンクを削除する

  - 「送信」（Next）ボタンを押すと、設定されたアイテム間リンクの情報をデータベースに保存し、ワークフロー定義通りの次アクションに進む

  - 「保存」（Save）ボタンを押すと、設定されたアイテム間リンクや入力したコメントの情報をデータベースに保存する。ワークフローを抜けた後、再度アクティビティを起動しても、設定したアイテム間リンクや、入力したコメントを保持したままとする

  - 選択したアイテム間リンク情報は、  
    JPCOARスキーマの jpcoar:relation -\> relationType にマッピングしてアイテムメタデータとして登録する

  - アイテム間の関係性：

| 関連性              | 内容           | junii2 | JPCOAR |
| ---------------- | ------------ | ------ | ------ |
| relateTo         | 関連している       |        |        |
| isVersionOf      | 異版である        | ○      | ○      |
| hasVersion       | 異版あり         | ○      | ○      |
| isReplacedBy     | 置換される        | ○      | ○      |
| replaces         | 置換する         | ○      | ○      |
| isRequiredBy     | 要件とされる       | ○      | ○      |
| requires         | 要件とする        | ○      | ○      |
| isPartOf         | 部分である        | ○      | ○      |
| hasPart          | 部分を持つ        | ○      | ○      |
| isReferencedBy   | 参照される        | ○      | ○      |
| references       | 参照する         | ○      | ○      |
| isFormatOf       | 別フォーマットである   | ○      | ○      |
| hasFormat        | 別フォーマットあり    | ○      | ○      |
| isSupplementedBy | ～によって補足されている |        | ○      |
| isSuppllementTo  | ～を補足している     |        | ○      |
| isIdenticalTo    | ～と同一である      |        | ○      |
| isDeriverdFrom   | ～に由来している     |        | ○      |
| isSourceOf       | ～の由来になっている   |        | ○      |
| isCitedBy        | ～によって引用されている |        | ○※     |
| Cites            | ～を引用している     |        | ○※     |

※JPCPAR2.0で追加（https://schema.irdb.nii.ac.jp/ja/schema/2.0/20）

2\. 設定されたアイテム間リンクを表示する

  - 設定されたアイテム間リンクは、アイテム詳細表示画面の「リンク」（Link）項目として表示される
    
      - リンクはリンク先アイテムの タイトルリンク とする  
        （複数アイテムあった場合はすべてのリンクを表示する）
    
      - リンクを選択すると、 リンク先アイテムのアイテム詳細表示画面に遷移する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_workflow

  - > weko\_records：「get\_item\_link\_info」メソッドで、既存のアイテム間リンクの情報を取得する

  - > weko\_search\_ui：インデックスツリーからインデックスを選択したときに、「search」メソッドが呼び出される。「search」メソッドの中で「get\_item\_link\_info」メソッドを呼び出している

<!-- end list -->

  - > 処理概要

実装方法

> 新規アイテム登録時、アイテム間リンクを設定する処理

  - > アイテム間リンクの設定画面を表示する

> 「action\_endpoint 'item\_link'」の場合、以下の定義からアイテム間の関係性を取得、以下のテンプレートで取得した情報を表示する

  - > アイテム間の関係性の定義： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/static/js/weko_workflow/workflow_item_link.js#L387>

  - > テンプレート： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/templates/weko_workflow/item_link.html>

<!-- end list -->

  - > 「送信」（Next）または「保存」（Save）ボタンを押すと、設定されたアイテム間リンクや入力したコメントの情報をデータベースに保存する
    
      - > データベースの情報
        
          - > テーブル名：item\_reference
        
          - > フィールド名：

> ・src\_item\_pid
> 
> ・dst\_item\_pid
> 
> ・reference\_type
> 
> ・created
> 
> ・updated
> 
> アイテム編集時、アイテム間リンクを設定する処理

  - > アイテム間リンクの設定画面を表示する  
    > 「action\_endpoint 'item\_link'」の場合、及び該当アイテムのメタデータにアイテム間リンクの情報が存在している場合、「get\_item\_link\_info」メソッドで設定されたアイテム間リンクの情報を取得する
    
      - > 「get\_item\_link\_info」メソッドは、画面表示時とインデックス選択時に呼び出される
        
          - > 「get\_item\_link\_info」メソッドは、item\_referenceテーブルからsrc\_item\_pidフィールドと引数recidが一致するレコードをあるだけ取得して、加工したものを返す。
        
          - > src\_item\_pidフィールドは整数で保存されている。
        
          - > 画面表示時には、recidに使用する値が小数であってもそのまま「get\_item\_link\_info」メソッドを呼び出す。
        
          - > インデックス選択時には、recidに使用する値は小数点以下を切り捨てて「get\_item\_link\_info」メソッドを呼び出す。

  - > 「送信」（Next）または「保存」（Save）ボタンを押すときの処理は、新規アイテム登録時の処理と同じである

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