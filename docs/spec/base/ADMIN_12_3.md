
### ロケーション

  - > 目的・用途

本機能は、管理者として、アップロードしているファイルの配置先及びロケーションごとの使用量の情報を管理する機能である

  - > 利用方法

【Administration \> ファイル管理（Files）\> ロケーション（Location）】から、ロケーションの情報の閲覧、編集、作成をする。

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

  - 【ロケーション（Location）画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - 作成（Create）
    
      - フィルターを追加▼（Add Filter▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 選択▼（With selected▼）
        
          - 一覧（List）タブ選択中のみ表示
        
          - 外観はタブだが機能としてはプルダウンメニュー
    
      - 編集（Edit）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
    
      - 詳細（Details）
        
          - > 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

  - 「一覧」（List）タブにロケーション一覧を表示する
    
      - 表示項目は以下の通りである
        
          - チェックボックス
        
          - アクション（閲覧・編集・削除）
        
          - 「Type」：ロケーションタイプ  
            押下すると一覧のロケーションをソートする。
        
          - 「Name」  
            押下すると一覧のロケーションをソートする。
        
          - 「URI」  
            押下すると一覧のロケーションをソートする。
        
          - 「Default」：デフォルトの状態  
            押下すると一覧のロケーションをソートする。
        
          - 「Size」：使用量の情報  
            押下すると一覧のロケーションをソートする。
        
          - 「Quota Size」：ロケーションの使用上限  
            押下すると一覧のロケーションをソートする。
        
          - 「Created」：ロケーションの作成時間  
            フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」  
            押下すると一覧のロケーションをソートする。
        
          - 「Updated」：ロケーションの更新時間  
            フォーマット：「YYYY-MM-DD hh:mm:ss.tttttt」  
            押下すると一覧のロケーションをソートする。
        
          - 「Buckets」リンク  
            リンクをクリックすると、【Admin \> Files \> Bucket画面】に移動し、当該ロケーションが属するバケット一覧がフィルターされる
    
      - 「フィルターを追加▼」（Add Filter▼）ボタンをクリックすると、以下の追加可能なフィルターリストを表示し、フィルター名をクリックすると当該フィルタの入力エリアを追加する
        
          - フィルター名
            
              - > 「Default」
            
              - > フィルター方式の選択肢：等しい（equals）、等しくない（not equal）
                
                  - 選択したフィルター方式に対して「はい」「いいえ」
            
              - 「Created」
            
              - > フィルター方式の選択肢：等しい（equals）、等しくない（not equal）、より大きい（greater than）、より小さい（smaller than）、間（between）、間ではなく（not between）、空（empty）
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
            
              - 「Updated」
            
              - > フィルター方式の選択肢：「Created」と同じである
                
                  - 入力された文字列を使い、選択したフィルター方式で絞り込む
        
          - 設定したフィルターは「適用」（Apply）ボタンを押下することで一覧に適用される
        
          - 「フィルターをリセット」（Reset filter）ボタンを押下すると、設定したフィルターがリセットされる
    
      - 「選択▼」（With selected▼）ボタンをクリックすると、以下の追加可能な機能（現在削除ボタンのみ）を表示する
        
          - レコードにチェックを入れない場合、「削除」（Delete）ボタンを押すと、エラーメッセージを表示する  
            メッセージ：  
            　日本語：「少なくとも一つのレコードを選択してください。」  
            　英語：「Please select at least one record.」
        
          - レコードにチェックを入れる場合、「削除」（Delete）ボタンを押すと、確認ダイヤログを表示する  
            メッセージ：  
            　日本語：「選択したレコードを削除してもよろしいですか。」  
            　英語：「Are you sure you want to delete selected records?」
            
              - 「OK」ボタンを押すと、該当ロールを削除し、メッセージを画面上部に表示する  
                メッセージ：  
                　日本語：「レコード数＋レコードが正常に削除されました。」  
                　英語：「Record was successfully deleted.」
            
              - 「キャンセル」（Cancel）ボタンを押すと、確認ダイヤログを閉じる
    
      - 検索テキストボックスでロケーションを検索する
        
          - プレースホルダー：「Search: URI, name」
        
          - 任意テキストを入力し、キーボードでの「Enter」を押すと、ロケーション検索を行う
        
          - テキストボックスの右端での「X」ボタンを押すと、検索条件がクリアーされる
    
      - ロケーション行に目アイコンを押すと、該当ロケーションの詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目：Type、Name、URI、Default、Size、Quota Size、Created、Updated、Buckets
        
          - 「Buckets」リンクをクリックすると、【Administration \> Files (ファイル管理) \> Bucket (バケット) 画面】に移動し、当該ロケーションが属するバケット一覧がフィルターされる
    
      - ロケーション行に鉛筆アイコンを押すと、該当ロケーションを「編集」（Edit）タブに表示し、ロケーションの情報が編集できる
    
      - ロケーション行に削除アイコンを押すと、該当ロケーションを削除し、メッセージを画面上部に表示する  
        メッセージ：  
        　日本語：「レコード数＋レコードが正常に削除されました。」  
        　英語：「Record was successfully deleted.」
    
      - 「一覧」（List）から「作成」（Create）タブを押すと、「編集」(edit)タブに移動しロケーションを新規作成できる
        
          - 入力情報：
            
              - 「Name」：必須項目  
                入力パターン：「^\[a-z\]\[a-z0-9-\]+$」
            
              - 「URI」：必須項目
            
              - 「Type」  
                選択肢：Amazon S3
            
              - 「access\_key」  
                「Type」に「Amazon S3」を選択する時表示する
            
              - 「secret\_key」  
                「Type」に「Amazon S3」を選択する時表示する
            
              - 「endpoint\_url」  
                「Type」に「Amazon S3」を選択する時表示する
            
              - > 「send\_file\_directrly」  
                > 「Type」に「Amazon S3」を選択する時表示するチェックボックス  
                > デフォルト：チェックあり
            
              - 「Quote Size」：使用上限
            
              - 「Default」  
                デフォルト：チェックなし
        
          - 「保存」（Save）ボタンを押すと、設定内容をバリデーションチェックし、エラーがない場合、設定されたロケーション内容をロケーション一覧に追加させ、メッセージをロケーション一覧に表示させる  
            メッセージ：  
            　日本語：「レコードが正常に作成されました。」  
            　英語：「Record was successfully created.」
            
              - アクセスコントロールをデータベースに保存する
                
                  - テーブル名：「files\_location」
                
                  - フィールド名：  
                    ・「id」  
                    ・「name」  
                    ・「uri」  
                    ・「default」  
                    ・「type」  
                    ・「access\_key」  
                    ・「secret\_key」  
                    ・「size」  
                    ・「quota\_size」  
                    ・「max\_file\_size」
        
          - エラーメッセージは以下の通りである
            
              - 必須項目を指定しない場合、エラーメッセージを該当テキストボックスの下に表示する  
                メッセージ：  
                　日本語：「このフィールドは必須です。」  
                　英語：「This field is required.」
            
              - 「Name」のフォーマットが不正の場合、エラーメッセージを「Name」テキストボックスの下に表示する  
                メッセージ：「Invalid location name.」
        
          - 「保存してもう一つ追加」（Save and Add Another）ボタンを押すと、設定されたロケーション内容をロケーション一覧に追加させ、他のロケーションを追加設定可能とする  
            メッセージを画面上部に表示させる  
            メッセージ：  
            　日本語：「レコードが正常に作成されました。」  
            　英語：「Record was successfully created.」
        
          - 「保存して編集を続ける」（Save and Continute Editing）ボタンを押すと、設定されたロケーション内容をロケーション一覧に追加させ、該当ロケーションの編集を続けることを可能とする  
            メッセージを画面上部に表示させる  
            メッセージ：  
            　日本語：「レコードが正常に作成されました。」  
            　英語：「Record was successfully created.」
        
          - 「キャンセル」（Cancel）ボタンを押すと、設定されたロケーション内容をロール一覧に追加せず、「一覧」（List）タブに戻る

  - ロケーションごとの使用量（Size）を確認できる
    
      - 「一覧」（List）タブ及び「詳細」（Detail）タブに確認できる
    
      - 「Size」の値について
        
          - 当該ロケーション配下に登録されているコンテンツファイルのサイズ合計
        
          - 使用量の合計はコンテンツアップロード時に集計する
        
          - 以下のファイルはシステムで自動削除し、使用量に集計されないようにする
            
              - ワークフローで強制終了したアクティビティに登録していたファイル
            
              - アイテム登録後に削除したファイル
        
          - ファイルアップロード時に Quota Size を越えるときの判定条件として利用する  
            Location で表⽰される Size ＋ アップロードした Size ＞ Quota Size で判定する

  - 設定キー：「update\_location\_size」

  - 合計された「Size」の値はデータベースに保存し、表示の際はデータベースに保存した値をつかう

  - リポジトリ管理者として、ストレージ使用状況をメール通知で確認できる  
    ロケーションの「Size」が指定された閾値を超えていた場合、当該ロケーションが属する機関のリポジトリ管理者にメール通知を行う
    
      - メール通知は定期実行とし、実行頻度はコンフィグファイルに変更可能とする
        
          - 設定キー：「storage\_check\_settings」
        
          - デフォルトは週次とする
    
      - ロケーションの「Size」が指定する閾値を超えた場合メール通知の対象する
    
      - ロケーションの「Quota Size」が設定されていない場合は処理の対象としない
    
      - 閾値はコンフィグファイルに指定する
        
          - 設定キー：「storage\_check\_settings」
        
          - デフォルトは、Quota Sizeに対して「80％」とする
    
      - 通知先は「リポジトリ管理者」ロールを持つユーザーとする
    
      - メール本文は以下の資料を参照する  
        別紙「ディスク容量メールひな形.docx」を参照。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio-files-rest

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - ロケーション画面の処理
    
      - ロケーション画面を表示した際に、invenio\_files\_rest.admin.LocationModelViewが継承したModelViewよりflask\_admin.model.base.index\_viewメソッドが呼び出される。このメソッドでfiles\_locationテーブルより情報を取得し、LocationModelViewのcolumn\_listにあるキーに対応する情報を画面に表示する。
        
          - 目アイコンを押下してロケーション詳細情報を表示する際に、invenio\_files\_rest.admin.LocationModelViewが継承したModelViewよりflask\_admin.model.base.details\_viewメソッドを呼び出す。このメソッド下でfiles\_locationテーブルより情報を取得し、LocationModelViewのcolumn\_details\_listにあるキーに対応する情報を画面に表示する。
        
          - 鉛筆アイコンを押下して編集画面を表示する際に、invenio\_files\_rest.admin.LocationModelViewが継承したModelViewよりflask\_admin.model.base.edit\_viewメソッドをGETで呼び出す。このメソッドでidを用いて、files\_locationテーブルより情報を取得し、表示する。
            
              - 編集画面で「保存」ボタンを押下する。そうすると、flask\_admin.model.base.edit\_viewメソッドをPOSTで呼び出す。このメソッド下で、get\_save\_return\_urlメソッドが呼ばれ、編集内容をfiles\_locationテーブルに保存し、更新する。
        
          - 削除アイコンを押下した際に、invenio\_files\_rest.admin.LocationModelViewが継承したModelViewよりflask\_admin.model.base.delete\_viewメソッドをGETで呼び出してfiles\_locationテーブルから削除する。
    
      - 作成タブを押下した際に、invenio\_files\_rest.admin.LocationModelViewが継承したModelViewよりflask\_admin.model.base.create\_viewメソッドをGETで呼び出す。LocationModelViewのform\_columnsの項目の入力欄を表示する。
        
          - 入力欄に入力後「保存」ボタンを押下する。そうすると、invenio\_files\_rest.admin.LocationModelViewが継承したModelViewよりflask\_admin.model.base.create\_viewメソッドをPOSTで呼び出す。このメソッド下でget\_save\_return\_urlメソッドが呼ばれ、新しいバケットの情報をfiles\_bucketテーブルに保存する。

  - ロケーションの使用量合計はコンテンツアップロード時に集計する
    
      - パス：  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-files-rest/invenio_files_rest/utils.py#L123-L131>

  - メール通知の定期実行を設定する
    
      - パス:   
        <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/populate-instance.sh#L460-L462>
    
      - 設定キー：「storage\_check\_settings」
    
      - 現在の設定値：

> ${INVENIO\_WEB\_INSTANCE} admin\_settings create\_settings \\
> 
> 2 "storage\_check\_settings" \\
> 
> "{'threshold\_rate': 80, 'cycle': 'weekly', 'day': 0}"

  - バケットごとでの使用上限（QUOTA\_SIZE）を設定する
    
      - パス：   
        [o https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko\_deposit/config.py\#L27](file:///C:\\Users\\masah\\Documents\\機能仕様書\\o%09https:\\github.com\\RCOSDP\\weko\\blob\\v0.9.22\\modules\\weko-deposit\\weko_deposit\\config.py#L27)
    
      - 設定キー：「WEKO\_BUCKET\_QUOTA\_SIZE」
    
      - 現在の設定値：

> WEKO\_BUCKET\_QUOTA\_SIZE = 50 \* 1024 \* 1024 \* 1024 \# 50 GB

  - 一つのファイルの最大容量を設定する
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py#L30>
    
      - 設定キー：「WEKO\_MAX\_FILE\_SIZE」
    
      - 現在の設定値：

> WEKO\_MAX\_FILE\_SIZE = WEKO\_BUCKET\_QUOTA\_SIZE

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
