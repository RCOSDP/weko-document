### コミュニティ

<!-- end list -->

  - > 目的・用途

本機能は、コミュニティの作成、編集、詳細情報及び一覧の閲覧の為の機能である。

  - > 利用方法

【Administration\>コミュニティ管理(Communities)\>コミュニティ(Community)】画面にて操作を行う

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

  - 【コミュニティ（Community）画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - 作成（Create）
    
      - 編集（Edit）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
    
      - 詳細（Details）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

  - 一覧（List）タブにて現在登録されているコミュニティを表示する
    
      - コミュニティが登録されていない場合、登録されたアイテムがない旨のメッセージが一覧に表示される  
        メッセージ：  
        日本語：「表にはアイテムがありません。」  
        英語：「There are no items in the table.」
    
      - 表示項目は以下の通りである
        
          - アクション  
            目アイコン及び鉛筆アイコンである
        
          - 「Id」  
            設定されたコミュニティIdである
        
          - 「Title」  
            設定されたコミュニティタイトルである
        
          - 「Owner.Name」  
            指定された所有者のロール名を表示する
        
          - 「Index」  
            選択されたコミュニティを設定しているインデックス名である
        
          - 「Deleted At」
        
          - 「Last Record Accepted」
        
          - 「Ranking」  
            ユーザ画面にてRanking順で表示する際は、ここで設定した値の降順となる
        
          - 「Fixed Points」  
            設定された固定点である
    
      - 検索テキストボックスでコミュニティを検索する
        
          - プレースホルダー：「Search: id, title, description」
        
          - 任意テキストを入力し、キーボードでの「Enter」を押すと、Id、タイトル、説明での検索を行う
        
          - テキストボックスの右端での「X」ボタンを押すと、検索条件がクリアーされる
    
      - コミュニティ行にて目アイコンを押すと、該当コミュニティの詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目は以下の通りである
            
              - 「Owner」
            
              - 「Index」
            
              - 「Created」
            
              - 「Updated」
            
              - 「Title」
            
              - 「Description」
            
              - 「Page」
            
              - 「Curation Policy」
            
              - 「Community Header」
            
              - 「Community Footer」
            
              - 「Last Record Accepted」
            
              - 「Logo Ext」
            
              - 「Ranking」
            
              - 「Fixed Points」
            
              - 「Deleted At」
            
              - 「Inclusion Requests」
            
              - 「Featuredcommunity」
    
      - コミュニティ行にて鉛筆アイコンを押すと、該当コミュニティを「編集」（Edit）タブに表示し、コミュニティの情報が編集できる
    
      - 「作成」（Create）ボタンを押すと、コミュニティの作成画面に移動する
        
          - 入力項目は以下の通りである
            
              - 「Id」テキストボックス
                
                  - コミュニティIdを入力する。必須項目である
                
                  - 入力可能な形式はアルファベットの小文字、「-」、 「\_」、数字となる
                
                  - 最初の1文字には数字を使うことはできない
                
                  - 最初の1文字に「-」を使うことができるが、その直後に数字を使うことはできない
                
                  - アルファベットの大文字が入力された場合、作成時に小文字に直す。
                
                  - 入力不可な形式を入力する場合、エラーメッセージを「Id」テキストボックスの直下に表示する
                    
                      - 最初の1文字についてのエラーメッセージ：「The first character cannot be a number or special character. It should be an alphabet character, "-" or "\_"」
                    
                      - 2文字目以降についてのエラーメッセージ：「Don't use space or special character except \`-\` and \`\_\`.」
                
                  - > 最初の文字が「-」+数字だった場合のエラーメッセージ：「Cannot set negative number to ID.」
                
                  - Idに入力したものがが既に存在している場合、作成時エラーメッセージ「Id」テキストボックスの直下に表示する。  
                    エラーメッセージ：「既に存在しています。」
            
              - 「Owner」プルダウン
                
                  - 所有者のロールを選択する。必須項目である。デフォルトは1番目の項目とする
                
                  - 「Owner」プルダウンの選択肢はシステムに登録されたロールの一覧である
                
                  - 表示形式は以下の通りである

> ロール - ロール説明(description)

  - 「Index」プルダウン
    
      - コミュニティを設定するインデックスを選択する。必須項目である。デフォルトは1番目の項目とする
    
      - 「Index」プルダウンの選択肢は自身の関連しているコミュニティに限定されたインデックス一覧である
    
      - 各インデックスの表示形式は以下の通りである

> Index\<id=インデックスId, index\_name=インデックス名\>

  - 「Title」テキストボックス  
    コミュニティのタイトルを入力する

  - 「Description」テキストボックス  
    説明を入力する

  - 「Page」テキストボックス  
    ページ数を入力する

  - 「Curation Policy」テキストボックス  
    ポリシーを入力する

  - 「Ranking」テキストボックス  
    ランキングの表示件数を入力する。デフォルトの値は「0」とする  
    数字のみ入力可能である。
    
      - 全角数字を入れた場合、作成時に半角になる。
    
      - 数字以外を入れて、作成した場合、作成時エラーメッセージを「Ranking」テキストボックスの下に表示する。  
        エラーメッセージ：無効な整数です。

  - 「Fixed Points」テキストボックス  
    固定点を入力する。デフォルトの値は「0」とする  
    数字のみ入力可能である。
    
      - 全角数字を入れた場合、作成時に半角になる。
    
      - 数字以外を入れて、作成した場合、作成時エラーメッセージを「Ranking」テキストボックスの下に表示する。  
        エラーメッセージ：無効な整数です。

<!-- end list -->

  - ［保存（Save）］ボタンを押すと、設定されたコミュニティの内容をコミュニティ一覧に追加させ、メッセージをコミュニティ一覧に表示させる  
    メッセージ：  
    　日本語：「レコードが正常に作成されました。」  
    　英語：「Record was successfully created.」

  - ［保存してもう一つ追加（Save and Add Another）］ボタンを押すと、設定されたコミュニティの内容をコミュニティ一覧に追加させ、他のコミュニティを追加設定可能とする。メッセージを画面上部に表示させる  
    メッセージ：  
    　日本語：「レコードが正常に作成されました。」  
    　英語：「Record was successfully created.」

  - ［保存して編集を続ける（Save and Continute Editing）］ボタンを押すと、設定されたコミュニティの内容をコミュニティ一覧に追加させ、該当コミュニティの編集を続けることを可能とする。メッセージを画面上部に表示させる  
    メッセージ：  
    　日本語：「レコードが正常に作成されました。」  
    　英語：「Record was successfully created.」

  - ［キャンセル（Cancel）］ボタンを押すと、設定されたコミュニティ内容をロール一覧に追加せず、「一覧」（List）タブに戻る

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_communities

<!-- end list -->

  - > 処理概要

> 本画面は、flaskのModelViewでcommunities\_communityテーブルのメンテナンスを行う機能である
> 
> 本画面を操作すると、ModelView を継承するinvenio\_communities.admin. CommunityModelViewクラスのメソッドが呼び出される
> 
> 一覧（List）タブ表示時、編集（Edit）タブ表示時に、操作するユーザのロールを確認して、それらのidで最小のものが以下のコンフィグで指定する値より大きい場合にはModelViewとは異なる処理を行う

  - > パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-communities/invenio_communities/config.py#L165>

  - > 設定キー：COMMUNITIES\_LIMITED\_ROLE\_ACCESS\_PERMIT

> 一覧（List）タブ表示時に、index\_viewメソッド（WEKOソースでオーバーライドされていない）が呼び出される

  - > この中で呼び出されるget\_queryメソッドとget\_count\_queryメソッドでは、上記の分岐によるModelViewと異なる処理として、取得するコミュニティの絞り込みを行う
    
      - > id\_roleが操作するユーザのロールのidに含まれるものか、id\_userが操作するユーザのユーザidと一致するものだけに絞り込む

> 編集（Edit）タブ表示時に、edit\_viewメソッド（WEKOソースでオーバーライドされていない）が呼び出される

  - > この中で呼び出されるedit\_formメソッドでは、上記の分岐によるModelViewと異なる処理として、CommunityModelViewのインスタンスにindex\_id属性を追加して、入力フォームに「action」「edit」を追加する

> 作成（Create）、編集（Edit）タブで［保存（Save）］ボタンを押すと、\_validate\_input\_idメソッドでidのバリデーションチェックを行い、保存処理中のon\_model\_changeメソッドでレコードのid\_userカラムを操作ユーザのidで更新する

  - > 編集（Edit）タブでの保存時はidを編集できないため、実質的には作成（Create）タブでの保存時のみにバリデーションチェックしている

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
