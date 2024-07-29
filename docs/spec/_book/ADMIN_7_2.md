
### ワークフロー

  - > 目的・用途

本機能は、ワークフローの作成、編集を行う機能。

  - > 利用方法

【Administration＞ワークフロー管理（WorkFlow）＞ワークフロー（WorkFlow List）】の順で画面遷移することで利用可能。

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
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 【Administration \> ワークフロー管理（WorkFlow） \> ワークフロー（WorkFlow List）】に登録されたワークフローが一覧に表示される。
    
      - 表示項目は以下の通りである
        
          - 「No.」
        
          - 「ワークフロー」（WorkFlow）  
            登録されたワークフロー名である。リンクの形式で表示される。
        
          - 「アイテムタイプ」（Item Type）  
            指定されたワークフロー名である。
        
          - 「フロー」（Flow）  
            指定されたフロー名である。
        
          - 「制限公開フラグ」（Restricted Access Flag）  
            指定された制限公開フラグ名である。
        
          - 「GakuNinRDM Flag」  
            GakuNinRDMからWEB API経由で受け取るアイテムの一括登録を行う際のワークフローを作成するためのフラグ。
        
          - 「登録先インデックス」（Registration Destination Index Designation）  
            指定された登録先インデックスの指定名である。
        
          - 「ストレージロケーション」(Storage Location)  
            ファイルを保存するストレージロケーション名である。
        
          - 「表示」(Display)  
            ワークフローを表示するロールを表示する。
        
          - 「Hide」  
            ワークフローを非表示とするロールを表示する。
        
          - 「ステータス」（Status）  
            ワークフローのステータス
        
          - 「更新日」（Updated）  
            ワークフローの更新日である。フォーマット：YYYY-MM-DD

<!-- end list -->

  - 「Create WorkFlow」ボタンを押すと、ワークフローの作成画面に移動する。
    
      - 入力項目は以下の通りである。
        
          - 「ワークフロー」（WorkFlow）：テキストボックスにワークフロー名を入力する。
        
          - 「フロー」（Flow）：プルダウンからフローを選択する。  
            プルダウンの選択肢は【Administration \> ワークフロー管理（WorkFlow） \> フロー（Flow）】で登録されたフロー一覧である。
        
          - 「アイテムタイプ」（Item Type）：プルダウンからアイテムタイプを選択する。  
            アイテムタイププルダウンの選択肢は【Administration＞アイテムタイプ管理（Item Types）＞メタデータ（Metadata）】で登録された標準アイテムタイプ一覧である。
        
          - 「制限公開フラグ」（Restricted Access Flag）：制限公開フラグをチェックする。  
            デフォルトはチェック無し。チェックありの場合、アイテム登録画面でコンテンツファイルの制限公開指定時に「提供方法」の「ワークフロー」の選択肢として表示する。
        
          - GakuNinRDM Flag： チェックを入れるとGakuNinRDMからWEB APIで受け取る「一括登録フォーマット」の利用を可能とするワークフローとなる。
        
          - 「登録先インデックスの指定」（Registration Destination Index Designation）：プルダウンから登録先インデックスの指定を選択する。インデックスプルダウンの選択肢は【Administration＞インデックスツリー管理（Index Tree）＞ツリー編集（Edit Tree）】で登録されたインデックス一覧である。
            
              - \[登録先インデックスの指定（Registration Destination Index Designation）\] を「指定なし（Enable）」とした場合
                
                  - ワークフローで項目入力後にインデックスを指定してアイテムを登録する。
            
              - \[登録先インデックスの指定（Registration Destination Index Designation）\] でインデックスを指定した場合
                
                  - ワークフローで項目入力後に、指定したインデックスを自動で登録する。
        
          - 「ストレージロケーション」(Storage Location)： プルダウンから登録先ストレージロケーションを選択する。
        
          - 「表示／非表示」（Diplay/Hide）ロール毎にワークフローの表示・非表示を設定する。
            
              - invenio\_account.ACCOUNTS\_WORKFLOW\_ROLE\_HIDE\_FILTER = False とすると、新規ロール追加時にデフォルトで表示となる。(v0.9.22)
    
    <!-- end list -->
    
      - \[保存（Save）\]ボタンを押すと、ワークフローを保存し、メッセージを表示する。  
        メッセージ：「Workflow created successfully.」

<!-- end list -->

  - ワークフロー名のリンクを押すと、ワークフローの編集画面に移動する。
    
      - ワークフローの編集画面で、ワークフローの情報を編集できる。
        
          - ワークフローの情報を編集してから、\[保存（Save）\]ボタンを押すと、ワークフローを編集し、下記メッセージを一覧画面の上部に表示し、WorkFlow List画面に遷移する。  
            メッセージ：「Workflow created successfully.」
    
    <!-- end list -->
    
      - ワークフローの編集画面で、\[削除（Delete）\]ボタンを押すと、ワークフローを削除する。削除後、WorkFlow List画面に遷移する。
        
          - 対象のワークフローが使用されていた場合は削除できない。\[削除（Delete）\]ボタンを押すと、エラーメッセージを表示する。  
            エラーメッセージ：「Cannot be deleted because workflow is used.」
        
          - ワークフローの編集画面で、\[戻る（Back）\]ボタンを押すと、ワークフロー一覧画面に移動する。

  - システム管理者でない（リポジトリ管理者）の場合、利用申請に関するワークフローは閲覧・編集ができない。また利用申請に関するワークフローを追加できない。（利用申請フラグが非表示であり、登録時に利用申請フラグがFalseとして登録される）。利用申請フラグの編集はシステム管理者のみ可能。

  - 戻るボタンをクリックすると、一つ前のアクションに戻ることが可能(v1.0.7追加)。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_workflow

<!-- end list -->

  - > 処理概要

> 【Administration＞ワークフロー管理（Work flow）＞ワークフロー（Work Flow List）】の順で画面遷移すると、weko\_workflow.admin.WorkFlowSettingView.indexが呼び出され、db内のworkflow\_workflowテーブルからis\_deletedカラムにチェックが入っていないワークフローの情報を取り出し、WorkFlow Listとして表示する。

  - > \[Create Workflow\]ボタン押下時もしくはワークフロー名を押下指定のワークフローの編集時は、weko\_workflow.admin.WorkFlowSettingView.workflow\_detailが呼び出される。ここではメソッド内の変数workflow\_idの値を用いて条件分岐している。新規作成時は、workflow\_id=0であり、それ以外はworkflow\_idに指定したワークフローのidを代入している。新規作成の場合、入力欄の初期値は以下のようになる。
    
      - > ワークフロー（Work Flow）：空欄
    
      - > フロー（Flow）：【Administration＞ワークフロー管理（Work Flow）＞フロー（Flow　List）】のFlow Listの情報をプルダウン形式で表示する。初期状態では、No.が一番小さいものとなっている。
    
      - > アイテムタイプ（ItemType）：db内のitem\_type\_nameテーブルのnameカラムから情報を取り出し、プルダウン形式で表示する。初期状態では、idカラムの数が一番小さいものとなっている。
    
      - > 制限公開フラグ（Restrictedke）：チェックなし
    
      - > GakuNinRDM Flag：チェックなし
    
      - > 登録先インデックスの指定（Registration Destination Index Designation）：db内のindexテーブルのindex\_nameカラムから情報を取り出し、プルダウン形式で表示する。初期状態ではどの情報も選択されておらず、「指定なし（Undesignated）」と表示されている。
    
      - > ストレージロケーション（Storage Location）：：db内のfiles\_locationテーブルのnameカラムから情報を取り出し、プルダウン形式で表示する。初期状態ではどの情報も選択されておらず、「指定なし（Undesignated）」と表示されている。
    
      - > 表示/非表示（Display/Hide）：db内のacounts\_roleのnameカラムから情報を取り出し表示（Display）ボックス内に表示する。初期状態では、すべてのroleが表示側に表示される。

  - > 既存のワークフローの編集の場合、入力欄の値は指定したworkflow\_idを用いてweko\_workflow.api.Workflow.get\_workflow\_detailを使用して情報をdb内のworkflow\_workflowテーブルから取り出して表示する。

> 情報の入力後に\[保存（Save）\]ボタン押下で、weko\_workflow.admin.WorkFlowSettingView.update\_worrkflowが呼び出される。  
> ただし、\[保存（Save）\]ボタンは、ワークフロー名が空欄の時は非活性となる。

  - > 新規作成の場合、UUIDが新たに作成され、その後db内のworkflow\_workflowテーブルに入力したワークフローを保存する。作成されたUUIDはflow\_idとして使用される。

  - > 既存のワークフローの編集の時は、db内のworkflow\_workflowテーブルの情報を更新する。

  - > \[保存（Save）\]ボタン押下前に、\[戻る（Back）\]ボタン押下で入力内容を破棄しWorkFlow List画面へ戻る。

> ワークフロー名押下で編集画面に移行した際は、\[保存（Save）\]ボタンの横に\[削除（Delete）\]ボタンが配置される。\[削除（Delete）\]ボタン押下時は、削除可能なワークフローである場合はdb内のworkflow\_workflowテーブルのis\_deletedカラムにチェックが入る。

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