### ワークフロー管理（制限公開）

  - フロー:　Flow List
    
      - 【Admin \> WorkFlow \> Flow List画面】から利用申請フローを登録することができる
        
          - 現在利用申請フローとして動作が保証されているのは以下の2つである。
            
              - 利用申請： 　\[Start\]-\[Item Resistration\]-\[Approval(1)\]-\[End\]
            
              - 二段階利用申請：　\[Start\]-\[Item Resistration\]-\[Approval(1)\]-\[Approval(2)\]-\[End\]
            
              - 利用登録： 　\[Start\]-\[Item Resistration\]-\[End\]
            
              - 利用規約のみ： 　\[Start\] -\[End\]
        
          - 利用登録は、Approvalを承認扱いでスキップする利用申請。利用規約のみは、申請なしでそのまま制限公開のコンテンツファイルをダウンロードできる。
        
          - 利用報告フローは以下の通り定義している。
            
              - 利用報告： 　\[Start\]-\[Item Resistration\]-\[Approval(1)\]-\[End\]
    
      - 「Action Role」カラムに、アクションを実行するロールを限定できる
        
          - 「Action Role」プルダウンを選択する。「Action Role」プルダウンでの選択肢は現在システムに設定されたロールである
        
          - 「Deny」チェックボックスにチェックを入れる場合、選択されているロールが実施不可とする
    
      - 「Action User」カラムに、アクションを実行するユーザーを限定できる
        
          - 「Action User」プルダウンを選択する。「Action User」プルダウンでの選択肢は現在システムに登録されたユーザーである
            
              - 「Approval」アクションに対して
                
                  - 選択肢はシステムに登録しているユーザーと、「プロパティを指定」(Specify Property)である
                    
                      - 「プロパティを指定」(Specify Property)を選択した場合、「プロパティを指定する」(Specify Property)モーダル画面を表示する。当該画面でプロパティを選択する
                    
                      - モーダル画面には、プロパティ定義に「"approval":true」キーワードを持つプロパティ名を表示する
                    
                      - モーダルに表示しているプロパティを選択して「設定」(Setting)ボタンを押すことで、プロパティを指定できる
                    
                      - 「閉じる」（Close）ボタンを押すと、モーダルを閉じる
                
                  - 「Item Resistration」アクションの以下チェックボックスにチェックを入れることで、管理者画面で登録したメールを自動送信することができる
                    
                      - チェックボックス：「Send an email to the registrant」  
                        Item Resistration登録完了時に、登録者にリマインドメールを送信する  
                        **\*\***\*チェックボックスをクリックすると、チェックボックス下のリストボックスが活性する。
                        
                          - リストボックスから、【Admin \> 設定 \> メールテンプレート】で登録したメールのタイトルを選択することができる。
                
                  - 「Approval」アクションごとに以下チェックボックスにチェックを入れることで、管理者画面で登録したメールを自動送信することができる
                    
                      - チェックボックス
                        
                          - 「承認依頼通知メール」（Approval Request Notification Email）  
                            Approvalフロー遷移時に、設定した承認者に承認を依頼するメールを送信する
                        
                          - 「承認却下通知メール」（Approval Rejection Notification Email）  
                            Approvalフローにて承認者が却下を行った場合、登録者に承認者が却下された旨を通知するメールを送信する
                        
                          - 「承認通知メール」（Approval Notification Email）  
                            Approvalフローにて承認者が承認を行った場合、登録者に承認者が承認された旨を通知するメールを送信する
                    
                      - チェックボックスをクリックすると、チェックボックス下のリストボックスが活性する。
                        
                          - リストボックスから、【Admin \> 設定 \> メールテンプレート】で登録したメールのタイトルを選択することができる。
        
          - 「Deny」チェックボックスにチェックを入れる場合、選択されているユーザーが実施不可とする
    
      - 「Change Order」カラムにアクションの順序を設定できる  
        一番上の項目は、［↑］ボタンが無効になる。一番下の項目は、［↓］ボタンが無効になる
    
      - 画面の下部に表示されている［保存］を押すと、フローを保存し、メッセージを一覧画面の上部に表示する  
        メッセージ：「Updated flow action successfully」

  - ワークフロー:　WorkFlow List
    
      - 【Admin \> WorkFlow \> WorkFlow List画面】に登録されたワークフローが一覧に表示される
        
          - 制限公開機能を利用するためには、「利用報告/Data Usage Report」という名前のワークフローを用意しておく必要がある
            
              - 「利用報告/Data Usage Report」の推奨設定は以下のとおり  
                ワークフロー: 利用報告/Data Usage Report  
                フロー：利用報告  
                アイテムタイプ：利用報告  
                制限公開フラグ：チェックしない  
                GakuNinRDM Flag：チェックしない  
                登録インデックスの指定：利用報告（インデックスにて登録）  
                表示/非表示：利用者が自分でワークフローを作成させないために、「提供方法：ロール」にて設定したロールは非表示とするのが望ましい。
        
          - 利用申請用のワークフローの推奨設定は以下のとおり
            
              - 利用申請  
                ワークフロー: 利用申請  
                フロー：利用報申請  
                アイテムタイプ：利用申請  
                制限公開フラグ：チェックする  
                GakuNinRDM Flag：チェックしない  
                登録インデックスの指定：利用申請（インデックスにて登録）
            
              - 表示/非表示  
                　表示：System Administrator, Repository Administrator  
                　非表示：Contributor,Community Administrator
            
              - 二段階利用申請  
                ワークフロー: 二段階利用申請  
                フロー：二段階利用申請  
                アイテムタイプ：二段階利用申請  
                制限公開フラグ：チェックする  
                GakuNinRDM Flag：チェックしない  
                登録インデックスの指定：利用申請（インデックスにて登録)
            
              - 
              - 
表示/非表示 　

> 表示：System Administrator, Repository Administrator  
> 　 非表示：Contributor,Community Administrator

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
<td>2024/01/19</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>