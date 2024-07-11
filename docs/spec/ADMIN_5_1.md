### 編集
        
        1.  #### 著者名典拠

<!-- end list -->

  - > 目的・用途

本機能は、ユーザーが著者の追加・編集・削除・統合を行う機能である。

氏名やメールアドレスでの検索を可能とすることで、ユーザーが目的の著者に効率よくたどり着くことができる。

  - > 利用方法

【Administration\>著者DB管理（Author Management）\>編集（Edit）】の順で編集画面に遷移し、Author IDタブを押下する。

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

1 Author IDを参照する

  - 【Administration\>著者DB管理（Author Management）\>編集（Edit）】での「Author ID」タブに登録されているAuthor IDが表示される。
    
      - 表示項目は以下の通りである。
        
          - \[統合元（Origin」\]チェックボックス  
            マージ機能を使用する。
        
          - \[統合先（Target）\]ラジオボタン  
            マージ機能を使用する。
        
          - 「氏名（Name）」  
            登録されている氏名を表示する。氏名が複数登録されている場合、改行で表示する。
        
          - 「メールアドレス（Mail Address）」  
            登録されているメールアドレスを表示する。メールアドレスが複数登録されている場合、改行で表示する。
        
          - 「アイテム件数（Item Count）」  
            Author IDが作成者として登録されているアイテムの件数を表示する。
        
          - \[編集（Edit）\]ボタン  
            押下することで、編集画面へ遷移する。
    
      - Author ID検索エリアをAuthor ID一覧の上部に設ける
        
          - 検索テキストボックスに検索条件を入力して、\[検索（Search）\]ボタンを押すと、検索結果が表示される。
            
              - 検索方式：AND
            
              - 検索条件：姓、名、メールアドレス

> 検索結果が0件の場合は、以下のメッセージを Author IDの表示エリアに表示する。  
> 日本語：「検索結果は0件です。」  
> 英語：「Sorry，No results.」

  - 検索の仕様

> 　・ 漢字氏名の検索：　１文字から検索可能
> 
> 　・ カナ氏名の検索：　姓または名の完全一致
> 
> 　・ 英語氏名の検索：　姓または名の完全一致
> 
> 　・ メールアドレスの検索：　＠の前後の完全一致（＠は含めても可）、またはメールの完全一致
> 
> 　【データ例】
> 
> 　　　山田　太郎　　　(ja)
> 
> 　　　Yamada　Tarou　(en)
> 
> 　　　ヤマダ　タロウ　(ja-kana)
> 
> 　　　sample@test.co.jp　(Email)
> 
> 　　　　検索条件　：　検索可否
> 
> 　　　　山田　　　：　○
> 
> 　　　　山　　　　：　○
> 
> 　　　　田　　　　：　○
> 
> 　　　　太郎　　　：　○
> 
> 　　　　太　　　　：　○
> 
> 　　　　郎　　　　：　○
> 
> 　　　　山田太郎　：　○
> 
> 　　　　山田太　　：　○
> 
> 　　　　田太郎　　：　○
> 
> 　　　　田太　　　：　○
> 
> 　　　　山太　　　：　×
> 
> 　　　　ヤマダ　　：　○
> 
> 　　　　ヤマ　　　：　×
> 
> 　　　　マダ　　　：　×
> 
> 　　　　ヤ　　　　：　×
> 
> 　　　　タロウ　　：　○
> 
> 　　　　タロ　　　：　×
> 
> 　　　　ロウ　　　：　×
> 
> 　　　　タ　　　　：　×
> 
> 　　　　ヤマダタロウ：　×
> 
> 　　　　ヤマダ　タロウ：　○　　※半角または全角スペース含む場合
> 
> 　　　　ヤマダタロ：　×
> 
> 　　　　マダタロ　：　×
> 
> 　　　　やまだ　　：　×
> 
> 　　　　たろう　　：　×
> 
> 　　　　Yamada　：　○
> 
> 　　　　Tarou　　：　○
> 
> 　　　　Yam　　　：　×
> 
> 　　　　sample　　：　○
> 
> 　　　　sample@　：　○
> 
> 　　　　sam　　　：　×
> 
> 　　　　test.co.jp　：　○
> 
> 　　　　@test.co.jp　：　○
> 
> 　　　　test　　　　：　×
> 
> 　　　　sample@test.co.jp　：　○
> 
> 　　　　sample@test　：　×

  - Author ID一覧にページング機能を設ける。
    
      - ページ当たりの表示件数（Display Number）をプルダウンより選択できる。
        
          - 選択可能な件数は「25, 50, 100」でデフォルトは「25」とする。
    
      - ページングナビゲーションを操作することで、表示内容が切り替わる。

2 Author IDを追加する。

  - 【Administration\>著者DB管理（Author Management）\>編集（Edit）】での「Author ID」タブに\[著者追加（Add Author）\]ボタンを押すと、著者追加画面に移動する。
    
      - 入力項目は以下の通りである。
        
          - 「氏名」（Name）
            
              - 「セイ」「メイ」テキストボックス：著者の姓・名を入力する。
            
              - 言語：選択肢は「ja-Kana, ja, en,fr,it,de,es,zh-tw,ru,la,ms,eo,ar,el,ko」とする。
            
              - 「姓・名」（First and Last Name）：氏名の入力形式を選択する。
            
              - \[表示／非表示（Display/Hide）\]ラジオボタン
                
                  - 「表示」（Display）を選択すると、「著者DBから入力」（From author DB）機能で、氏名が自動入力される。
                
                  - 「非表示」（Hide）を選択すると、［著者DBから入力］（From author DB）機能で、氏名が自動入力されない。
            
              - \[+著作項目を追加（Add author item）\]ボタンを押すことで、氏名の入力欄が追加される。
            
              - \[X\]ボタンを押すことで、氏名の入力欄が削除される。  
                表示されている入力エリアが１つのみの場合、削除不可とする。
        
          - 「著者ID」（Author ID）
            
              - 外部著者プルダウン：著者の外部著者を選択する。  
                「ID Prefix」画面で登録されている外部著者IDから選択できる。
            
              - 外部著者IDテキストボックス：外部著者IDを入力する。  
                クリーンビルド環境の場合、初期に表示される選択肢は「ORCID, CiNii, KAKEN2,ROR」とする。
            
              - 「ID Prefix」画面にはリスト上に "WEKO" が存在する(WEKO3で著者を一意に決定するWEKO著者ID)が、「著者ID」のプルダウンのリストには表示されない。  
                "WEKO"は著者登録時に自動付番(初期値のWEKO著者IDは1, 以降は2, 3, ...と付番されている max(authors.id)＋１)される。
            
              - \[確認（Confirm）\]ボタンを押すと、選択された外部著者IDに応じたランディングページが表示される。
                
                  - 別ウィンドウで表示させる。
                
                  - 著者IDを入力しない場合、「確認」（Confirm）ボタンが非活性とする。
                
                  - ランディングページのURLについて
                    
                      - 「ID Prefix」に設定されたURLに「\#\#」が含まれている場合、「\#\#」を著者IDに置換してURLとする。
                    
                      - 「ID Prefix」に設定されたURLに「\#\#」が含まれていない場合、そのまま設定されたURLとする。
            
              - \[表示／非表示（Display/Hide）\]ラジオボタン
                
                  - 「表示」（Display）を選択すると、「著者DBから入力」（From author DB）機能で、外部著者IDが自動入力される。
                
                  - 「非表示」（Hide）を選択すると、［著者DBから入力］（From author DB）機能で、外部著者IDが自動入力されない。
            
              - \[+著者IDを追加（Add a new ID）\]ボタンを押すことで、著者IDの入力欄が追加される。
            
              - \[X」ボタンを押すことで、著者IDの入力欄が削除される。  
                表示されている入力エリアが１つのみの場合、削除不可とする。
        
          - 「E-Mail」テキストボックス：メールアドレスを入力する。
            
              - \[+e-mailを追加（Add E-mail）\]ボタンを押すことで、メールアドレスの入力欄が追加される。
            
              - \[X」ボタンを押すことで、メールアドレスの入力欄が削除される。  
                表示されている入力エリアが１つのみの場合、削除不可とする。
    
      - \[取消（Clear）\]ボタンを押すと、入力した内容が取消される。
    
      - \[保存（Save）\]ボタンを押すと、Author IDが追加される。
        
          - ボタン押下後、WEKO著者IDを自動付番し、Author IDの一覧画面に遷移する。
        
          - 姓、名から姓名の情報（fullName）が生成される。
    
      - 追加をキャンセルしたい場合は、\[保存(Save)\]ボタンの押下前に他のタブを押下するなどして著者追加画面から遷移させる必要がある。

3 Author IDを編集・削除する。

  - Author ID一覧に\[編集（Edit）\]ボタンを押すと、Author IDの編集画面に移動する。
    
      - 設定された情報を表示する。
    
      - Author IDの情報を編集してから、\[保存（Save）\]ボタンを押すと、Author IDの情報が更新されて、Author ID一覧画面に移動する。
    
      - Author IDの編集画面に「削除」（Delete）ボタンを押すと、該当の著者が削除されて、Author ID一覧画面に移動する。
    
      - 編集時に外部著者IDの"WEKO"（WEKO著者ID）は編集することはできない（グレーアウトとする）。

  - 著者の削除について
    
      - 削除方式は論理削除とする。
    
      - 削除では、著者情報のテーブルに削除フラグのカラムを設けて、削除情報を管理する。
    
      - 紐づいているアイテムが１件以上存在する状態で\[削除（Delete）\]ボタンを押下すると、以下のポップアップメッセージを表示し、削除することができない。
        
          - 日本語：「アイテムがリンクしているため、指定された著者は削除できません。」
        
          - 英語：「The author is linked to items and cannot be deleted.」

4 Author IDをマージする。

  - Author IDのトップ画面に\[著者統合（Merge）\]ボタンを設ける。
    
      - 以下の場合に\[著者統合（Merge）\]ボタンを非活性とする。
        
          - 「Origin」チェックボックスにチェックを入れない。
        
          - 「Target」ラジオボタンにチェックを入れない。
        
          - 「Origin」チェックボックスと「Target」ラジオボタンに全く同じのレコードを選択する。
    
      - Author ID一覧からマージしたい著者を選択して、\[著者統合（Merge）\]ボタンを押すと、マージ確認画面がモーダル表示される。
        
          - マージ確認画面に表示内容を以下の通りである。
            
              - 「Origin」と「Target」エリアは別に分ける。
            
              - 各エリアに著者情報を表示する。
                
                  - 「氏名」（Name）
                
                  - 「メールアドレス」（Mail Address）
                
                  - 「アイテム件数」（Item Count）
        
          - 「Execute」ボタンを押すことで、著者マージを行って、マージ確認画面を閉じる。
            
              - 「Origin」に選択された著者を論理削除する  
                ※ 「Target」が「Origin」にある場合、該当著者を削除しない
            
              - 「Origin」に選択された著者に紐付いていたアイテムのWEKO著者IDと外部著者IDを「Target」に選択された著者の情報で更新する。
        
          - 「Back」ボタンを押すことで、マージ確認画面を閉じる。
        
          - マージ処理が終わるまで次のマージ処理はできない。
          
          - アイテム更新完了するまで、あるいはエラーが発生するまで、著者DBはコミットしない。

          - マージ状況は author_merge_status.tsv に出力される。



#### 関連モジュール

- weko-authors
- weko-angular/app-author-search
- weko-deposit

<!-- end list -->

  - > 処理概要

1\. 設定

  - 表示件数のデフォルト値を設定する
    
      - パス：  
        https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko\_authors/config.py\#L204 
    
      - 設定キー：WEKO\_AUTHORS\_NUM\_OF\_PAGE
    
      - 現在の設定値：

> WEKO\_AUTHORS\_NUM\_OF\_PAGE = 25

  - Author ID一覧画面のテンプレートを設定する
    
      - パス：   
        https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko\_authors/config.py\#L42
    
      - 設定キー：WEKO\_AUTHORS\_ADMIN\_LIST\_TEMPLATE
    
      - 現在の設定値：

> WEKO\_AUTHORS\_ADMIN\_LIST\_TEMPLATE = 'weko\_authors/admin/author\_list.html'

  - Author ID編集画面のテンプレートを設定する。
    
      - パス：   
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L45> 
    
      - 設定キー：WEKO\_AUTHORS\_ADMIN\_EDIT\_TEMPLATE
    
      - 現在の設定値：

> WEKO\_AUTHORS\_ADMIN\_EDIT\_TEMPLATE = 'weko\_authors/admin/author\_edit.html'

2\. 実装方法

  - nameIdentifiersでnameIdentifierScheme=WEKOを利用して当該アイテムに属性(author\_link)を追加する。  
    著者情報のアイテム件数（Item Count）は以下のようにクエリを作成し、"author\_link"毎に著者情報をカウントする。

> "size": 0,
> 
> "query": {
> 
> "bool": {
> 
> "must": \[
> 
> {
> 
> "match": {
> 
> "publish\_status": 0
> 
> }
> 
> },
> 
> {
> 
> "match": {
> 
> "relation\_version\_is\_last": "true"
> 
> }
> 
> },
> 
> {
> 
> "bool": {
> 
> "should": \[
> 
> {
> 
> "term": {
> 
> "author\_link.raw":
> 
> "@author\_id"
> 
> }
> 
> }
> 
> \]
> 
> }
> 
> }
> 
> \]
> 
> }
> 
> }

**3.処理内容**

  - > **【Administration\>著者DB管理（Author Management）\>編集（edit）】で開かれる編集画面は、初期状態としてweko\_authors.views.getが呼び出され、db内のauthorsテーブルからgather\_flgが0でかつis\_deleteにチェックがついていないものが取り出されて表示されている。**

  - > **著者追加ボタンを押すと著者追加画面へ遷移し、任意の項目を入力後に\[保存（Save）\]ボタン押下で、weko\_authors.views.createが呼び出され、db内のauthorテーブルに情報が追加される。このとき、同メソッド内でidは自動作番され、gather\_flgは０,is\_deleteはFalseの状態で追加される。**

  - > **著者追加時は、各々の項目に対して入力テキストボックスを追加することができる。  
    > それぞれのテキストボックスには以下のような初期値が、あらかじめ入力されている。**

<!-- end list -->

  - > **氏名→言語入力欄に「ja-Kana」**

  - > **著者ID→ID選択欄に「ORCID」(ただし、2項目目以降の追加時は「WEKO」が入力される。著者IDが「WEKO」のものは編集できないため、追加したテキストボックスは自動的に非活性となる。)**

  - > **所属機関識別子→機関識別子選択欄に「ISNI」。所属機関名の言語選択欄に「ja」**

  - > **\[表示/非表示（Display/Hide）\]チェックボタンは、初期値として\[表示（Display）\]にチェックが付いた状態となっている。**

<!-- end list -->

  - > **編集ボタンを押すと編集画面に遷移し、任意の項目を変更後に\[保存（Save）\]ボタン押下で、weko\_authors.views.update\_authorが呼び出され、エンコードされたのちにdb内のauthorテーブルに保存される。編集画面も追加時の画面と同様に、各々の項目に対してテキストボックスの追加が可能となっており、初期値も追加画面のものと同様になっている。**

  - > **著者の削除の際は、編集画面下部の\[削除（delete）\]ボタンを押下することで、weko\_authors.views.delete\_authorが呼び出され、選択した著者のdb内のis\_deleteカラムをTrueへ変更する。**

  - > **検索テキストボックスに、任意の文字列を入力し検索ボタンを押下すると、weko\_authors.views.getが呼び出され、同メソッド内のsearch\_keyに入力した文字列が代入され、検索が行われたのち、検索対象のみがauthorテーブルから取り出されて出力される。**

  - > **著者の統合時は、weko\_authors.views.gatherByIdが呼び出され、統合元(Origin)にチェックを入れた著者のauthorテーブル内のgather\_flgが1に変更される。また、統合の際にweko\_deposit.tasks.items\_by\_authorInfoが呼び出され、db内のitem\_metadataテーブルのjsonカラム内の、**統合元（Origin）に選択された著者に紐付いていたアイテムのWEKO著者IDと外部著者IDを統合先（Target）に選択された著者の情報で更新し、それに関連するES内のメタデータのマッピングの情報も更新する。

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
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>
