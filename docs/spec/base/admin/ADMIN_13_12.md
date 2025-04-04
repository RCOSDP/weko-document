### ユーザープロファイル

  - > 目的・用途

本機能は、ユーザーのユーザー名、タイムゾーン、言語を個別に設定する際に用いる機能である。

  - > 利用方法

【Administration \> ユーザー管理（User Management） \> ユーザープロファイル（User Profile）画面】にて操作を行う。

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

  - 【ユーザープロファイル（User Profile）画面】には以下のタブが表示される
    
      - 一覧（List）
    
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
        
          - 「User Id」
        
          - 「ユーザー名（Username）」
        
          - 「タイムゾーン（Timezone）」
        
          - 「言語（Language）」
    
      - 表示内容は、userprofiles\_userprofileテーブルから取得した情報である
    
      - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルターの入力エリアを追加する
        
          - フィルター名
            
              - 「User Id」
                
                  - フィルター方式の選択肢：フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「ユーザー名（Username）」
                
                  - フィルター方式の選択肢：含む（contains）、含まれていません（not contains）、等しい（equals）、等しくない（not equal）、空（empty）、一覧にある（in list）、一覧にない（not in list）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「タイムゾーン（Timezone）」
                
                  - フィルター方式の選択肢：上記の「ユーザー名」と同じである
                
                  - プルダウンメニューからタイムゾーンを選択して、選択したフィルター方式で絞り込む
            
              - 「言語（Language）」
                
                  - フィルター方式の選択肢：上記の「ユーザー名」と同じである
                
                  - プルダウンメニューから言語を選択して、選択したフィルター方式で絞り込む
                
                  - 選択肢は、「自動（Automatic）」「日本語（Japanese）」「英語（English）」
        
          - 設定したフィルターは［適用（Apply）］ボタンを押下することで一覧に適用される
        
          - ［フィルターをリセット（Reset filter）］ボタンを押下すると、設定したフィルターがリセットされる
    
      - 「選択▼」（With selected▼）ボタンをクリックすると、以下の追加可能な機能（現在削除ボタンのみ）を表示する
        
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
        
          - プレースホルダー：「Search」
        
          - 任意のテキストを入力し、キーボードでの「Enter」を押すと、ユーザープロファイル検索を行う
        
          - テキストボックスの右端での［X］ボタンを押すと、検索条件がクリアーされる
    
      - ユーザープロファイル行にて目アイコンを押すと、該当ユーザーの詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目：User Id、Username、Fullname、Timezone、Language
            
              - それぞれ、userprofiles\_userprofileテーブルのuser\_id、username、fullname、timezone、languageフィールドに対応している
        
          - UsernameとFullnameは、設定できる画面がWEKOにないため、userprofiles\_userprofileテーブルを直接編集しない限り空欄となる
            
              - WEKO内では使用する箇所もない
        
          - 一覧タブや編集タブ、各ユーザーが個別に表示するユーザープロフィール画面で表示や編集を行う「ユーザー名（username）」は、userprofiles\_userprofileテーブルではdisplaynameである
    
      - ユーザー行にて鉛筆アイコンを押すと、該当ユーザーを「編集」（Edit）タブに表示し、ユーザーの情報が編集できる
        
          - 編集項目： Username、Timezone、Language
            
              - それぞれ、userprofiles\_userprofileテーブルのdisplayname、timezone、languageフィールドに対応している

  - 関連コンフィグ
    
      - WEKO\_USERPROFILES\_ROLES:
        
          - JGSS専用のコンフィグです。  
            JGSSの4つロール（管理者、一般、院生、学部生）を指定するものです。
    
      - WEKO\_USERPROFILES\_POSITION\_LIST\_GRADUATED\_STUDENT:
        
          - JGSS専用のコンフィグです。  
            JGSSでは、ユーザーの役割を選択した場合、その役割に該当するロールを自動設定するものです。  
            例：役割一覧は以下のコンフィグに定義されています。  
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py#L113-L121>  
            この役割一覧の１つを選択した場合、該当するロールに「学院性」ロールが自動設定されます。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_user\_profiles

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 一覧タブ表示時は、weko\_user\_profiles.admin.UserProfileView.index\_viewメソッドで情報を取得している

  - 一覧タブの表示内容は、以下のコンフィグで決定している
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py#L168-L169>
    
      - 設定キー：WEKO\_USERPROFILES\_FORM\_COLUMN
    
      - 以下の表示候補の中から、このコンフィグにあるものを表示している
        
          - User Id
        
          - ユーザー名（Username）
        
          - 氏名（Fullname）
        
          - タイムゾーン（Timezone）
        
          - 言語（Language）
        
          - 大学・機関（University/Institution）
        
          - 所属部局・部署（Affiliated Division/Department）
        
          - 役職（Position）
        
          - 役職（その他）（Position (Others)）
        
          - 電話番号（Phone number）
        
          - 所属学会名（Affiliated Academic Society）
        
          - 所属学会役職（Affiliated Academic Society Position）
            
              - 所属学会名と所属学会役職は最大５つまで設定可能

  - 編集タブ表示時は、UserProfileView\_edit\_viewメソッドで情報の取得、更新を行う
    
      - 「Timezone」の選択肢は、以下のコンフィグで設定している
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/config.py#L46-L83>
        
          - キー：USERPROFILES\_TIMEZONE\_LIST
    
      - ［保存（Save）］ボタンを押すと、以下の内容でフォームデータが送信される
        
          - 「displayname」：画面上の「ユーザー名（Username）」で入力されたもの
        
          - 「timezone」：画面上の「Timezone」で選択されたもの
        
          - 「language」：画面上の「Language」で選択されたもの
    
      - 送信されたフォームデータによって、userprofiles\_userprofileテーブルの内容が更新される

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