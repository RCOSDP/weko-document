### ユーザー

  - > 目的・用途

本機能は、ユーザーの新規作成、編集、削除を行う際に使用する機能である。

  - > 利用方法

【Administration \> ユーザー管理（User Management） \> ユーザー（User）画面】にて操作を行う。

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

  - 【ユーザー（User）画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - 作成（Create）
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 選択▼（With selected▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 編集（Edit）
        
          - 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
    
      - 詳細（Details）
        
          - 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

  - 「一覧」（List）タブに登録されているユーザーを表示する
    
      - 表示項目は以下の通りである
        
          - チェックボックス
        
          - アクション（閲覧・編集・削除を表すアイコン）
        
          - 「Id」
        
          - 「Email」
        
          - 「Active」
        
          - 「Confirmed At」
        
          - 「Last Login At」  
            フォーマット：「YYYY-MM-DDThh:mm:ss.tttttt」
        
          - 「Current Login At」  
            フォーマット：「YYYY-MM-DDThh:mm:ss.tttttt」
        
          - 「Last Login IP」
        
          - 「Current Login IP」
        
          - 「Login Count」
    
      - 表示内容は、accounts\_userテーブル、accounts\_userroleテーブルから取得した情報である
    
      - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルターの入力エリアを追加する
        
          - フィルター名
            
              - 「Id」
                
                  - フィルター方式の選択肢：フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Email」
                
                  - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Active」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
                
                  - 入力エリアではなく選択肢「はい」「いいえ」を使い、「はい」ならアクティブなユーザー、「いいえ」ならそうでないユーザーを絞り込む
            
              - 「Confirmed At」
                
                  - フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
                
                  - 入力エリアをクリックするとカレンダーが表示されるので、日時を選択して［Apply］押下することで絞り込む日時を設定する（入力することもできる）
                
                  - 日時を設定しなかった場合は現在日時を設定する
            
              - 「Last Login At」
                
                  - フィルター方式の選択肢：上記の「Confirmed At」と同じである
            
              - 「Current Login At」
                
                  - フィルター方式の選択肢：上記の「Confirmed At」と同じである
            
              - 「Login Count」
                
                  - フィルター方式の選択肢：上記の「Id」と同じである
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
        
          - 設定したフィルターは［適用（Apply）］ボタンを押下することで一覧に適用される
        
          - ［フィルターをリセット（Reset filter）］ボタンを押下すると、設定したフィルターがリセットされる
    
      - 「選択▼」（With selected▼）ボタンをクリックすると、以下の追加可能な機能（削除、Activate、Inactivateボタン）を表示する
        
          - 機能：Activate、Inactivate
            
              - レコードにチェックを入れない場合、「Activate」「Inactivate」または「削除」ボタンを押すと、エラーメッセージを表示する  
                メッセージ：  
                　日本語：「少なくとも一つのレコードを選択してください。」  
                　英語：「Please select at least one record.」
            
              - レコードにチェックを入れて「Activate」ボタンを押すと、確認ダイアログを表示する  
                メッセージ：「Are you sure you want to activate selected users?」
                
                  - ［OK］ボタンを押すと、該当ユーザーを活動化する  
                    メッセージ：  
                    　日本語：「ユーザーを無効化しました」  
                    　英語：「User(s) were successfully inactivated.」
                
                  - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
            
              - レコードにチェックを入れて「Inactivate」ボタンを押すと、確認ダイアログを表示する  
                メッセージ：「Are you sure you want to inactivate selected users?」
                
                  - ［OK］ボタンを押すと、該当ユーザーを無効化し、メッセージを画面上部に表示する  
                    メッセージ：  
                    　日本語：「ユーザーを無効化しました」  
                    　英語：「User(s) were successfully inactivated.」
                
                  - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
        
          - 機能：削除
            
              - レコードにチェックを入れない場合、「削除」（Delete）ボタンを押すと、エラーメッセージを表示する  
                メッセージ：  
                　日本語：「少なくとも一つのレコードを選択してください。」  
                　英語：「Please select at least one record.」
            
              - レコードにチェックを入れる場合、「削除」（Delete）ボタンを押すと、確認ダイアログを表示する  
                メッセージ：  
                　日本語：「選択したレコードを削除してもよろしいですか。」  
                　英語：「Are you sure you want to delete selected records?」
                
                  - ［OK］ボタンを押すと、該当ロールを削除し、メッセージを画面上部に表示する  
                    メッセージ：  
                    　日本語：「レコード数＋レコードが正常に削除されました。」  
                    　英語：「Record was successfully deleted.」
                
                  - ［キャンセル（Cancel）］ボタンを押すと、確認ダイアログを閉じる
    
      - 検索テキストボックスでユーザーを検索する
        
          - プレースホルダー：「Search: id, email, active, confirmed\_at, last\_login\_at, current\_login\_at, Last Login IP, Current Login IP, login\_count」
        
          - 任意のテキストを入力し、キーボードでの「Enter」を押すと、ユーザー検索を行う
        
          - テキストボックスの右端での［X］ボタンを押すと、検索条件がクリアーされる
    
      - ユーザー行にて目アイコンを押すと、該当ユーザーの詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目：Id、Email、Active、Confirmed At、Last Login At、Current Login At、Last Login IP、Current Login IP、Login Count
    
      - ユーザー行にて鉛筆アイコンを押すと、該当ユーザーを「編集」（Edit）タブに表示し、ユーザーの情報が編集できる
        
          - 入力情報は以下の通りである
            
              - 「Email」：必須項目
            
              - 「Password」  
                デフォルト値：その都度ランダムなパスワードが生成される
            
              - 「Active」  
                デフォルト：チェックなし
            
              - 「Roles」  
                デフォルト：空白  
                選択肢：【Administration \> ユーザー管理（User Management） \> ロール（Role）画面】に登録されているロール一覧  
                ※選択肢にあるもの以外は設定できない
            
              - 「Send User Notification」：登録されているアカウント情報をメールに送信する  
                デフォルト：チェックなし
        
          - ［保存（Save）］ボタンを押すと、設定された内容をユーザー一覧に追加して、メッセージをユーザー一覧に表示させる  
            メッセージ：  
            　日本語：「レコードが正常に作成されました。」  
            　英語：「Record was successfully created.」
        
          - ［保存してもう一つ追加（Save and Add Another）］ボタンを押すと、設定された内容をユーザー一覧に追加して、他のユーザーを追加設定可能とする  
            メッセージを画面上部に表示させる  
            メッセージ：  
            　日本語：「レコードが正常に作成されました。」  
            　英語：「Record was successfully created.」
        
          - ［保存して編集を続ける（Save and Continute Editing）］ボタンを押すと、設定された内容をユーザー一覧に追加して、該当ユーザーの編集を続けることを可能とする  
            メッセージを画面上部に表示させる  
            メッセージ：  
            　日本語：「レコードが正常に作成されました。」  
            　英語：「Record was successfully created.」
        
          - ［キャンセル（Cancel）］ボタンを押すと、設定された内容をユーザー一覧に追加せず、「一覧」（List）タブに戻る
        
          - 表示内容は、accounts\_userテーブル、accounts\_userroleテーブルから取得した情報である
        
          - 「Password」については、暗号化された状態で表示される

  - 「一覧」（List）から「作成」（Create）タブを押すと、「作成」（Create）タブに移動し、ユーザーを新規作成できる
    
      - 入力情報とボタン操作は、編集タブと同じである

  - 「編集」（Edit）、「作成」（Create）ともに、［保存（Save）］ボタンや［保存してもう一つ追加（Save and Add Another）］すると、パスワードが入力されていた場合はハッシュ化される
    
      - 「Password」に全角文字を入力していると、以下のエラーメッセージが表示されて保存されない
        
          - エラーメッセージ：  
            日本語：「レコードの更新に失敗しました。'ascii' codec can't decode byte 0xe3 in position 0: ordinal not in range(128)」  
            英語：「 to update record. 'ascii' codec can't decode byte 0xe3 in position 0: ordinal not in range(128)」
    
      - ハッシュ化されたパスワードがさらにハッシュ化されることはない

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - invenio\_accounts（WEKOソース内にforkされていない箇所がある）

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 編集タブで［保存（Save）］ボタンを押すと、以下の内容でフォームデータが送信される
    
      - 「email」：画面上の「Email」で入力されたもの
    
      - 「password」：画面上の「Password」で入力されたもの
    
      - 「active」：画面上の「Active」がチェックされていた場合のみ、「y」が設定される  
        チェックされていなかった場合はフォームデータに含まれない
    
      - 「roles」：画面上の「Roles」でロールが選択されていた場合のみ、  
        チェックされていなかった場合はフォームデータに含まれない
    
      - 「notification」：画面上の「Send User Notification」がチェックされていた場合のみ、「y」が設定される  
        チェックされていなかった場合はフォームデータに含まれない

  - パスワードはflask\_security.utils. hash\_passwordメソッドでハッシュ化している
    
      - 全角文字を設定していると、この中のasciiでデコードする段階で失敗する

  - 送信されたフォームデータによって、accounts\_userテーブルとaccounts\_userroleテーブルの内容が更新される

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
