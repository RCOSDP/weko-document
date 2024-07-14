### 言語表示

  - > 目的・用途

本機能は、リポジトリ管理者として、ユーザーが選択可能な表示言語を設定できる機能である

  - > 利用方法

【Administration \> 設定（Setting） \> 言語設定（Language）画面】にて操作を行う

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

使用している画面

  - 【Administration \> 設定（Setting） \> 言語設定（Language）画面】にて表示言語を設定する
    
      - 「対象言語」(Target language）に設定可能な表示言語をリスト表示する  
        デフォルトリストは以下とする（ ただし、言語実装は日本語、英語のみとする ）
        
          - 日本語\[Japanese ja\]
        
          - 英語(米)\[English en\]
        
          - 中国簡体\[Chinese zh\]
        
          - インドネシア語\[Indonesian id\]
        
          - ベトナム語\[Vietnamese vi\]
        
          - マレー語\[Malay ms\]
        
          - タガログ語\[Filipino (Pilipinas) fil\]
        
          - タイ語\[Thai th\]
        
          - ヒンディー語\[Hindi hi\]
    
      - 言語リストから表示言語とする言語を選択して、\[\>\]ボタンを押すと、「登録言語」（Registered language）に選択言語の表示が移る  
        選択肢は同時に複数選択可能とする
    
      - 選択言語リストから任意言語を選択して、\[\<\]ボタンを押すと、「登録言語」（Registered language）から「対象言語」(Target language）に表示が移る
    
      - 登録言語リストから任意言語を選択しない場合、\[↟\]、\[ʌ\]、\[ⅴ\]、\[↡\]ボタンを無効とする
    
      - 登録言語リストから任意言語を選択している場合
        
          - \[↟\]ボタンを押すと、登録言語リストの上頭に表示が移る
        
          - \[ʌ\]ボタンを押すと、登録言語リストの１つ上言語に表示が移る
        
          - \[ⅴ\]ボタンを押すと、登録言語リストの１つ下言語に表示が移る
        
          - \[↡\]ボタンを押すと、登録言語リストの下頭に表示が移る
    
      - 登録言語リストが空である間は、［保存（Save）］ボタンは非活性になる
    
      - ［保存（Save）］ボタンを押すと、「登録言語」（Registered language）の対象が表示言語として設定され、メッセージを画面上部に表示される
        
          - メッセージ：「Update languages action successfully」
        
          - 変更された内容をデータベースに保存する
            
              - テーブル名：admin\_lang\_settings
            
              - カラム名：  
                ・lang\_code  
                ・lang\_name  
                ・is\_registered  
                ・sequence  
                ・is\_active

  - 【言語設定（Language）画面】で設定した表示言語は、ユーザ側の表示言語選択プルダウンから使用可能となる
    
      - 【言語設定（Language）画面】で設定した順番でプルダウン表示する
    
      - 【言語設定（Language）画面】で設定した順番の一番上の言語をデフォルト表示とする

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_admin

<!-- end list -->

  - > 処理概要

1\. 設定

  - 言語一覧のデフォルトを設定する
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/populate-instance.sh#L343-L368>  
        ※「登録言語」に対して、以下の設定を追加する  
        ・「--registered」をステータス後に追加する  
        ・表示位置を最後の属性で設定する
    
      - 現在の設定：

> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active --registered "en" "English" 001
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "zh" "中文" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "id" "Indonesia" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "vi" "Tiếng Việt" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "ms" "Bahasa Melayu" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "fil" "Filipino (Pilipinas)" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "th" "ไทย" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active "hi" "हिन्दी" 000
> 
> ${INVENIO\_WEB\_INSTANCE} language create \\
> 
> \--active --registered "ja" "日本語" 002
> 
> 対象言語一覧に言語を追加する場合、以下のコマンドを実施する
> 
> docker-compose exec web invenio language create --active "言語コード" "言語名" 000

2\. 画面操作にともなう処理

  - 画面表示時に、weko\_admin.views. get\_lang\_list関数が呼び出される
    
      - レスポンスとして、admin\_lang\_settingsテーブルから「is\_active」フィールドがtrueであるレコードを「sequence」昇順で受け取る
    
      - 各レコードの言語は、「is\_registered」フィールドがtrueなら登録言語リストに、falseなら対象言語リストに配置する

  - ［保存（Save）］ボタンを押すと、.views.save\_lang\_list関数が呼び出される
    
      - リクエストのペイロードとして、要素が以下の内容であるJSON配列を送り、配列要素ごとにadmin\_lang\_settingsテーブルの「lang\_code」フィールドが配列要素の「lang\_code」に一致するレコードをその配列要素の内容で更新する。
        
          - is\_registered：登録言語にある場合はtrue、そうでなければfalse
        
          - lang\_code：言語コード
        
          - lang\_name：言語名
        
          - sequence：表示順（対象言語リストにある場合は0固定）

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