### 識別子

  - > 目的・用途

本機能は、ワークフロー中でアイテムに付与するための識別子を作成、編集する際に使用する機能である。

  - > 利用方法

【Administration \> 設定（Setting） \> 識別子（Identifier）画面】にて操作を行う。

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
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - 【識別子（Identifier）画面】には以下のタブが表示される
    
      - 一覧（List）
    
      - 作成（Create）
    
      - 編集（Edit）
        
          - 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示
    
      - 詳細（Details）
        
          - 一覧（List）タブ選択中は非表示
        
          - 一覧（List）タブの操作によって表示される
        
          - 編集（Edit）タブまたは詳細（Details）タブ選択中に表示

  - 「一覧」（List）タブにて識別子情報を表示する
    
      - 表示項目は以下の通りである
        
          - アクション（閲覧・編集を表すアイコン）
        
          - 「Repository」
        
          - 「JaLC DOI」
        
          - 「JaLC CrossRef DOI」
        
          - 「JaLC DataCite DOI」
        
          - 「NDL JaLC DOI」
        
          - 「Semi-automatic Suffix」
        
          - 「Jalc Flag」
        
          - 「Jalc Crossref Flag」
        
          - 「Jalc Datacite Flag」
        
          - 「Ndl Jalc Flag」
    
      - 識別子行にて目アイコンを押すと、該当識別子の詳細情報を「詳細」（Details）タブに表示する
        
          - 表示項目：Repository、JaLC DOI、JaLC CrossRef DOI、JaLC DataCite DOI、NDL JaLC DOI、Semi-automatic Suffix、Created Userid、Created Date、Updated Userid、Updated Date
        
          - 「移動」（Filter）テキストボックスにテキストを入力すると、入力値が項目名またはその値に含まれている項目に絞り込んで表示する
    
      - 識別子行にて鉛筆アイコンを押すと、該当識別子を「編集」（Edit）タブに表示し、編集できる

  - 「作成」（Create）タブにて新規作成、または「編集」（Edit）タブにて既存の情報を編集する
    
      - 「Prefix」領域の入力値により、テナント別に各DOI発行機関のプレフィックス情報を設定
        
          - プレフィックス設定項目は以下の通り
            
              - Reposiitory(必須)：プルダウン
                
                  - 「Root Index」または「communities\_community」テーブルの各レコードのidを選択肢とする
            
              - JaLC DOI：自由入力。100字まで入力可能
            
              - JaLC CrossRef DOI：自由入力。100字まで入力可能
            
              - JaLC DataCite DOI：自由入力。100字まで入力可能
            
              - NDL JaLC DOI：自由入力。100字まで入力可能
    
      - 「Suffix」領域の設定値の入力値により、テナント別にサフィックスの前半部分を設定
        
          - サフィックス設定項目は以下の通り
            
              - Semi-automatic suffix：自由入力
    
      - 「Enable/Disable」領域の設定により、テナント別に各DOI発行機関の利用可否を設定
        
          - Disableに設定されているDOIは、入力欄が非活性化する
    
      - ［保存（Save）］ボタンを押すと、入力値のエラーチェックを行う
        
          - 「Repository」の選択値について、作成時に登録済みのリポジトリを選択したか、編集時に登録済みの他のリポジトリに変更した場合、画面上部に以下のエラーメッセージが表示される
            
              - エラーメッセージ：  
                日本語：「指定したリポジトリが既に登録されています。」  
                英語：「Specified repository is already registered.」
        
          - 各プレフィックスの入力欄と、サフィックスの入力欄では、全角文字が入力されていると、該当する入力欄の下にエラーメッセージが表示される
            
              - エラーメッセージ：「Only allow half with 1-bytes character in input」
        
          - エラーが発生した場合、保存されず、画面の「Repository」の選択値が「Root Index」に変わる
        
          - エラーチェックを通過すると、「doi\_identifier」テーブルを更新する。その後、設定された内容を反映した「一覧」（List）タブに移動して、メッセージを画面上部に表示する
            
              - メッセージ：  
                　日本語：「レコードが正常に作成されました。」  
                　英語：「Record was successfully created.」
    
      - ［保存してもう一つ追加（Save and Add Another）］ボタンを押すと、［保存（Save）］ボタンによるものと同様の処理を行い、チェック通過時には「一覧」（List）タブのかわりに「作成」（Create）タブに移動して、同様のメッセージを画面上部に表示する
    
      - ［保存して編集を続ける（Save and Continute Editing）］ボタンを押すと、［保存（Save）］ボタンによるものと同様の処理を行い、チェック通過時には他のタブに移動せずに、同様のメッセージを画面上部に表示する
    
      - ［キャンセル（Cancel）］ボタンを押すと、設定された内容を反映せず、「一覧」（List）タブに戻る

  - 作成した情報は、以下の画面で利用する
    
      - 【Administration \> ワークフロー管理（WorkFlow） \> フロー（Flow List） \> Create Flow画面】
        
          - フローにて「Item Registration」のアクション後に「Identifier Grant」のアクションを定義
        
          - 詳細は[ADMIN-7-1: フロー](#フロー)参照
    
      - 【Administration \> ワークフロー管理（WorkFlow） \> ワークフロー（WorkFlow List） \> Create WorkFlow画面】
        
          - 「Identifier Grant」がフローに含まれるワークフローを定義
        
          - 詳細は[ADMIN-7-2: ワークフロー](#ワークフロー-2)参照

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_admin

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 「作成」（Create）タブの表示時には、weko\_admin.admin.IdentifierSettingView.create\_formメソッドから同クラスの\_use\_append\_repositoryメソッド、そこから同クラスの\_get\_community\_listメソッドを呼び出して、communities\_communityテーブルの情報を取得する

  - 「編集」（Edit）タブの表示時には、weko\_admin.admin.IdentifierSettingView.edit\_formメソッドから同クラスの\_use\_append\_repository\_editメソッド、そこから同クラスの\_get\_community\_listメソッドを呼び出して、communities\_communityテーブルの情報を取得する

  - 入力値のバリデーションチェックは、weko\_admin.admin.IdentifierSettingView.validate\_formメソッドの中で、同クラスの\_validator\_halfwidth\_inputメソッドで行う

  - 「doi\_identifier」テーブルの更新時にweko\_admin.admin.IdentifierSettingView. on\_model\_changeメソッドが呼び出されて、以下の設定値を作成する
    
      - 「created\_userId」（作成時のみ）：操作しているユーザのid
    
      - 「created\_date」（作成時のみ）：現在の日時を取得して、マイクロ秒部分を0に置き換える
    
      - 「updated\_userId」：操作しているユーザのid
    
      - 「updated\_date」：現在の日時を取得して、マイクロ秒部分を0に置き換える
    
      - 「repository」：「Repository」プルダウンで選択したもののid

  - 「doi\_identifier」テーブルのレコードは、以下のように更新する
    
      - 「id」：作成時に自動採番
    
      - 「repository」：上述のon\_model\_changeメソッドで作成したもの
    
      - 「jalc\_flag」：「Enable/Disable」領域での設定
    
      - 「jalc\_crossref\_flag」：「Enable/Disable」領域での設定
    
      - 「jalc\_datacite\_flag」：「Enable/Disable」領域での設定
    
      - 「ndl\_jalc\_flag」：「Enable/Disable」領域での設定
    
      - 「jalc\_doi」：「JaLC DOI」入力欄の入力値
    
      - 「jalc\_crossref\_doi」：「JaLC CrossRef DOI」入力欄の入力値
    
      - 「jalc\_datacite\_doi」：「JaLC DataCite DOI」入力欄の入力値
    
      - 「ndl\_jalc\_doi」：「NDL JaLC DOI」入力欄の入力値
    
      - 「suffix」：「Semi-automatic Suffix」入力欄の入力値
    
      - 「created\_userId」：上述のon\_model\_changeメソッドで作成したもの
    
      - 「created\_date」：上述のon\_model\_changeメソッドで作成したもの
    
      - 「updated\_userId」：上述のon\_model\_changeメソッドで作成したもの
    
      - 「updated\_date」：上述のon\_model\_changeメソッドで作成したもの

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