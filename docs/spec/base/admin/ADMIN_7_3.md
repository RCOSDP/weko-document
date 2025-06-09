
### ワークスペース設定

#### 目的・用途

本機能は、ワークスペースの登録形式の選択を行う機能である。

#### 利用方法

【Administration＞ワークフロー管理（WorkFlow）＞ワークスペース設定（WorkSpace WorkFlow Setting）】の順で画面遷移することで利用可能。

#### 利用可能なロール

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

#### 機能内容

  - 【Administration \> ワークフロー管理（WorkFlow） \> ワークスペース設定（WorkSpace WorkFlow Setting）】に登録形式が表示される。
    
      - 表示項目は以下の通りである
        
          - 「直接登録」（Direct Registration）  
            ラジオボタンの形式で表示される。
        
            - 「アイテムタイプ選択」（Item Type Select）  
              指定されたアイテムタイプ名である。プルダウンの形式で表示される。
        
          - 「ワークフロー経由で登録」（Workflow Select）  
            ラジオボタンの形式で表示される。 
        
            - 「ワークフロー選択」（Work Flow Select）  
              指定されたワークフロー名である。プルダウンの形式で表示される。
    
      - \[保存（Save）\]ボタンを押すと、登録形式とアイテムタイプあるいは、ワークフローを保存し、メッセージを表示する。  
        メッセージ： 「ワークスペースのワークフロー設定を更新しました。」 / 「WorkSpace WorkFlow Setting was updated.」

#### 関連モジュール

  -  weko\_workflow

#### 処理概要

  - 【Administration＞ワークフロー管理（Work flow）＞ワークスペース設定（WorkSpace WorkFlow Setting）】の順で画面遷移すると、weko\_workflow.admin.WorkSpaceWorkFlowSettingView.indexが呼び出される。

  - 情報の入力後に\[保存（Save）\]ボタン押下で、weko\_workflow.admin.WorkSpaceWorkFlowSettingView.indexが呼び出される。  

    - 入力された設定値は admin\_settingsテーブルの nameカラムの値が「workspace_workflow_settings」であるレコードに保存される。

#### 更新履歴

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
<p>2025/03/27</p>
</blockquote></td>
<td>057e4d8985a4b5526c0db7f07f717a4bb45bc984</td>
<td>初版作成</td>
</tr>
</tbody>
</table>