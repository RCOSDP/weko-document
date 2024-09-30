### コミュニティページ

  - > 目的・用途

本機能は、コミュニティタブの管理を行う為の機能である。

  - > 利用方法

【Administration\>設定(Setting)\>コミュニティページ(Community Page)】画面にて操作を行う

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

  - 【コミュニティページ(Community Page)画面】には以下の設定項目が存在する
    
      - 「タイトル」テキストボックス
          - タイトルを英語で入力する。必須項目
          - デフォルト値は「Communities」
    
      - 「タイトル」テキストボックス
          - タイトルを「言語」日本語で入力する。
          - デフォルト値は「コミュニティ」
    
      - 「補足文」テキストボックス
          - コミュニティの説明を入力する。
          - デフォルト値は「created and curated by WEKO3 users」
    
      - 「アイコン」テキストボックス
          - FontAwesomeのアイコンに対応するクラス名を入力する。
          - デフォルト値は「fa fa-group」
          - 「描画」ボタン押下でアイコンのプレビューが可能

<!-- end list -->

  - 「保存（Save）」ボタンを押すと、設定された内容を保存する。
     保存された設定はトップページから確認可能。
     
  - 「タイトルの追加」ボタンを押すと、日本語タイトル入力欄が追加される。
     - 日本語タイトル入力欄表示時は非活性になる
  
  - 「削除」ボタンを押すと、日本語タイトル入力欄が削除される。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_theme

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 初期表示時は、「admin_settings」テーブルからデータを取得する
    
      - このとき、テーブルにデータが存在しない場合は、以下のコンフィグからデフォルトの内容を取得する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py>
            
          - 設定キー：
            
              - WEKO_COMMUNITIES\_DEFAULT\_PROPERTIES
            
    
      - 取得した情報を各入力欄に設定して画面表示する

  - ［保存（Save）］ボタンを押すと、admin\_settingsテーブルに、以下の内容で保存する
    
     ※nameが同じレコードがなかった場合は新規作成、あった場合は更新する
     日本語のタイトルが入力されなかった場合、タイトルは英語で表示させる。
             
     - id：「0」(serial型であるため、0を指定することで自動的に末尾の数字＋1が採番される)
        
     - name：「community\_settings」
        
     - settings：「{"title1":タイトル(English)の入力値, "title2":タイトル(日本語)の入力値, "supplement":補足文の入力値, "icon\_code":アイコンの入力値}」
    
    その後、初期表示時と同様の処理を行い、画面表示する
  
  - アイコン入力欄にfontAwesomeのクラス名を入力後、［描画］ボタンを押すことで対応するアイコンを確認することができる。
  
    ※\modules\weko-theme\weko_theme\static\css\weko_themeのstyles.scssで定義されているfont-awesomeの内容を取り込んで「/static/gen/weko_styles.9e373b93.css」に集積して出力している。
    
    上記cssに各アイコンのclass設定が書き出されているので、そのclassを動的に変更することでアイコンの描画を変える
    
  - 入力値からアイコンの描画に失敗した場合は以下のエラーメッセージを出力
    
      - 英語："Invalid code value."
        
      - 日本語："無効なコード値です。"
      
  - アイコン入力欄の下に「アイコンについてはこちらを参照」のリンクがあるので、詳しくはそちらを参照。

    参照先：<https://fontawesome.com/v4/icons/>

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
<p>2024/09/30</p>
</blockquote></td>
<td></td>
<td>初版作成</td>
</tr>
</tbody>
</table>
