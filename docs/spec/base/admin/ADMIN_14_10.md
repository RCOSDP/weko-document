### ログ解析

  - > 目的・用途

本機能は、リポジトリ管理者として、利用統計の集計除外とするIPアドレスとユーザエージェントを設定できる機能である

  - > 利用方法

【Administration \> 設定（Setting） \> ログ解析（Log Analysis）画面】にて操作を行う

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

  - 利用統計の集計除外とするIPアドレスとユーザエージェントを設定する
    
      - 「フィルタリングするIPアドレスの入力」（Enter the IP Addresses to Filter）
        
          - ログ解析から除外するIPアドレスを指定する
        
          - 各入力欄は、半角数字以外の入力は自動的に削除するようになっている
        
          - IPアドレスは複数入力可能とし、［+］ボタンを押すと、IPアドレスを入力するエリアを追加する
        
          - ［x］ボタンを押すと、該当入力エリアを削除する
        
          - ［+］、［x］ボタンは、一番下の行にのみ表示される
    
      - 「共有クローラーリスト」（Shared Crawler Lists）
        
          - ログ解析から除外するIPアドレス、ユーザエージェントの部分一致キーワードリストを定義し、ネットワークを介して取得、設定する
        
          - デフォルトは以下の通りである
            
              - IPアドレスリスト  
                <https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_ip_blacklist.txt>
            
              - ユーザエージェントリスト  
                <https://bitbucket.org/niijp/jairo-crawler-list/raw/master/JAIRO_Crawler-List_useragent.txt>
            
              - 共用クローラーリストの使用可否は、チェックボックスで設定できる
    
      - ［保存（Save）］ボタンを押下すると、削除してよいかの確認用のモーダルを表示する  
        メッセージ：  
        　日本語：「与えられたアドレスをブロックしてもよろしいですか？」  
        　英語：「Are you sure you want to block the given addresses?」
        
          - ［保存（Save）］：
            
              - 除外対象アドレスおよび共用クローラーリストが、画面の設定内容で更新される
            
              - 画面上部に以下のメッセージが表示される  
                メッセージ：  
                　日本語：「設定を変更しました」  
                　英語：「Successfully Changed Settings.」
        
          - ［閉じる（Close）］：
            
              - モーダルを閉じて、設定画面に戻る

  - ブロックの処理
    
      - 利用統計等の集計時に参照するアクセスログに対し、除外対象アドレスおよび共用クローラーリストから、指定されたIPアドレス、ユーザエージェントを持つアクセスログが集計されないようになる
    
      - 除外されるアクセスログは、画面上で設定したIPアドレスおよび共用クローラーリストに記載されているIPアドレスを持つアクセスログと、共用クローラーリストに記載されている文字列に部分一致するユーザエージェントを持つアクセスログとする
        
          - weko\_admin.config.WEKO\_ADMIN\_USE\_REGEX\_IN\_CRAWLER\_LIST = True とすると正規表現を利用することができる
    
      - 除外されるアクセスログは、ESへ「is\_restricted」がtrueとして登録される
        
          - 通常はfalseとして登録される
        
          - 登録済みのアクセスログには影響しない

  - 設定による影響
    
      - 影響を受ける集計結果は以下のものとする
        
          - ランキング
        
          - 利用統計
        
          - サイトライセンスフィードバックメール送信
        
          - 利用統計フィードバックメール送信
        
          - 定型レポート
        
          - カスタムレポート
    
      - 設定した情報は、IPアドレスについてはloganalysis\_restricted\_ip\_addressテーブルに、共有クローラーリストについてはloganalysis\_restricted\_crawler\_listテーブルに保存される
        
          - 共有クローラーリストのURLの参照先の情報はRedisに保存される
    
      - 画面にてIPアドレスを削除、または共用クローラーリストを有効から無効に変更しても、一度除外されたアクセスログは集計されない

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio-stats：register\_events 関数にて、各インデックスに対する処理クラス、前処理を設定している

  - > weko-admin：画面表示と集計除外処理を定義する

  - > weko-redis：集計除外処理中で、Redisとの接続を管理する

<!-- end list -->

  - > 処理概要

1\. 画面表示

  - 画面表示時には、weko\_admin.admin.LogAnalysisSettings.indexメソッドをGETで呼び出して以下の情報を取得する
    
      - loganalysis\_restricted\_ip\_addressテーブルの全件
    
      - loganalysis\_restricted\_crawler\_listテーブルの全件
        
          - loganalysis\_restricted\_crawler\_listテーブルが空だった場合は、以下のコンフィグからデフォルトの共有クローラーリストのURLを取得してテーブルに追加して、再度全件取得する
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L120-L122>
            
              - 設定キー：WEKO\_ADMIN\_DEFAULT\_CRAWLER\_LISTS

  - 画面側では、IPアドレスと共有クローラーリストそれぞれについて、レコードの数だけ入力欄を表示する
    
      - loganalysis\_restricted\_ip\_addressテーブルから取得した情報は、IPアドレスの入力欄に設定する
        
          - IPアドレスの行ごとに、0始まりの行番号を設定する
        
          - 行ごとに、hiddenのinput要素を配置して、以下のnameとvalueを設定する
            
              - name：ip\_address\_行番号\_id
            
              - value：レコードのid
        
          - 行ごとに、入力欄の各input要素に「address\_list\_行番号」の形のname属性が設定される
        
          - 情報が0件だった場合は、入力欄を1行だけ表示する
    
      - loganalysis\_restricted\_ crawler\_listテーブルから取得した情報は、共有クローラーリストの入力欄に設定する
        
          - 共有クローラーリストの行ごとに、0始まりの行番号を設定する
        
          - 行ごとに、hiddenのinput要素を配置して、以下のnameとvalueを設定する
            
              - name：shared\_crawler\_行番号\_id
            
              - value：レコードのid
        
          - 行ごとに、入力欄の各input要素に「shared\_crawler\_行番号」の形のname属性が設定される
        
          - 情報が0件だった場合は、入力欄を2行だけ表示する

2\. 設定の保存

  - 保存時には、weko\_admin.admin.LogAnalysisSettings.indexメソッドをPOSTで呼び出す
    
      - loganalysis\_restricted\_ip\_addressテーブルへの保存時には、すべてのレコードを物理削除して、画面の各IPアドレスの行の入力内容からレコードを作成する
        
          - 「id」：自動採番
        
          - 「ip\_address」：nameが「shared\_crawler\_行番号」であるinputの各入力値を「.」で連結したもの
    
      - loganalysis\_restricted\_crawler\_listテーブルへの保存時には、以下の処理を行う
        
          - 共有クローラーリストの入力ごとに、レコードから、idが「shared\_crawler\_行番号\_id」の値と等しいものを取得する
            
              - 該当するレコードがあったら、それを入力内容で更新する
            
              - 該当するレコードがなかったら、入力内容で新たにレコードを作成する
    
      - その後、GETで呼び出されたときと同様の処理を行う

3\. イベントログ処理

  - modules/invenio-stats/invenio\_stats/contrib/registrations.py の register\_events 関数で初期化

  - 下記、register\_events 関数にて、各インデックスに対する処理クラス、前処理を設定している。  
    ログ解析機能を利用して設定された情報は flag\_restricted 関数内で利用されている。

> 〜省略〜
> 
> def register\_events():
> 
> """Register sample events."""
> 
> return \[
> 
> dict(
> 
> event\_type='celery-task',
> 
> templates='invenio\_stats.contrib.celery\_task',
> 
> processor\_class=EventsIndexer,
> 
> processor\_config=dict(
> 
> preprocessors=\[
> 
> flag\_restricted,
> 
> flag\_robots,
> 
> anonymize\_user,
> 
> build\_celery\_task\_unique\_id
> 
> \],
> 
> suffix="%Y",
> 
> )),
> 
> 〜省略〜

  - 上記のflag\_restricted関数内でweko\_admin.api.is\_restricted\_user関数を呼び出して対象のログが除外対象かどうかのチェックを行う
    
      - 除外対象となるログは、「is\_restricted」がtrueとなる
    
      - ログの「ip\_address」と「user\_agent」についてチェックを行い、どちらかで除外対象に含まれていればそのログは集計除外となる
        
          - 「ip\_address」について、loganalysis\_restricted\_ip\_addressテーブルにip\_addressフィールドと「ip\_address」とが一致するものがあった場合は除外対象となる
        
          - 「ip\_address」と「user\_agent」について、weko\_admin.api.\_is\_crawler関数を呼び出してチェックを行う
            
              - 以下のコンフィグで、共有クローラーリストによるチェックで正規表現を使用するかどうかを制御する
                
                  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L1278>
                
                  - 設定キー：WEKO\_ADMIN\_USE\_REGEX\_IN\_CRAWLER\_LIST
            
              - 以下のコンフィグで定めたRedisデータベースに接続する
                
                  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L43>
                
                  - 設定キー：CRAWLER\_REDIS\_DB
            
              - loganalysis\_restricted\_crawler\_listテーブルのアクティブな各レコードから取得した「list\_url」をキーとして、接続したRedisデータベースから共有クローラーリストを取得する
                
                  - 正規表現を使用する場合は文字列、そうでなければset型で取得する
                
                  - 取得できなかった場合は、「list\_url」を使ってインターネット上から共有クローラーリストを取得して、内容を加工したものをRedisデータベースに保存する
                    
                      - キーは「list\_url」の値とする
                    
                      - 内容は以下のように加工する
                        
                          - 正規表現を使用する場合は、「\#」で始まる行を除いた各行の内容を「|」で結合した文字列
                        
                          - 正規表現を使用しない場合は「\#」で始まる行を除いた各行の内容
                    
                      - 保存するデータには、以下のコンフィグで定めたTTLを設定する
                        
                          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L44>
                        
                          - 設定キー：CRAWLER\_REDIS\_TTL
                    
                      - インターネット接続に失敗した場合、例外となって処理が終了する
                
                  - 「ip\_address」と「user\_agent」を、Redisデータベースに保存されていた、または保存した情報の中から探して、どちらか片方でも存在していたら除外対象に含める
                    
                      - 「is\_restricted」に、is\_restricted\_user関数が返却する真偽値を設定する

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
