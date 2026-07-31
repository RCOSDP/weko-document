# ログ解析

## 目的・用途

本機能は、リポジトリ管理者として、利用統計の集計除外とするIPアドレスとユーザエージェントを設定できる機能である

## 利用方法

【Administration > 設定（Setting） > ログ解析（Log Analysis）画面】にて操作を行う

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ |  |  |  |  |

## 機能内容

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
        
          - weko_admin.config.WEKO_ADMIN_USE_REGEX_IN_CRAWLER_LIST = True とすると正規表現を利用することができる
    
      - 除外されるアクセスログは、ESへ「is_restricted」がtrueとして登録される
        
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
    
      - 設定した情報は、IPアドレスについてはloganalysis_restricted_ip_addressテーブルに、共有クローラーリストについてはloganalysis_restricted_crawler_listテーブルに保存される
        
          - 共有クローラーリストのURLの参照先の情報はRedisに保存される
    
      - 画面にてIPアドレスを削除、または共用クローラーリストを有効から無効に変更しても、一度除外されたアクセスログは集計されない

## 関連モジュール

  - invenio-stats：register_events 関数にて、各インデックスに対する処理クラス、前処理を設定している

  - weko-admin：画面表示と集計除外処理を定義する

  - weko-redis：集計除外処理中で、Redisとの接続を管理する

## 処理概要

1. 画面表示

  - 画面表示時には、weko_admin.admin.LogAnalysisSettings.indexメソッドをGETで呼び出して以下の情報を取得する
    
      - loganalysis_restricted_ip_addressテーブルの全件
    
      - loganalysis_restricted_crawler_listテーブルの全件
        
          - loganalysis_restricted_crawler_listテーブルが空だった場合は、以下のコンフィグからデフォルトの共有クローラーリストのURLを取得してテーブルに追加して、再度全件取得する
            
              - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L120-L122>
            
              - 設定キー：WEKO_ADMIN_DEFAULT_CRAWLER_LISTS

  - 画面側では、IPアドレスと共有クローラーリストそれぞれについて、レコードの数だけ入力欄を表示する
    
      - loganalysis_restricted_ip_addressテーブルから取得した情報は、IPアドレスの入力欄に設定する
        
          - IPアドレスの行ごとに、0始まりの行番号を設定する
        
          - 行ごとに、hiddenのinput要素を配置して、以下のnameとvalueを設定する
            
              - name：ip_address_行番号_id
            
              - value：レコードのid
        
          - 行ごとに、入力欄の各input要素に「address_list_行番号」の形のname属性が設定される
        
          - 情報が0件だった場合は、入力欄を1行だけ表示する
    
      - loganalysis_restricted_ crawler_listテーブルから取得した情報は、共有クローラーリストの入力欄に設定する
        
          - 共有クローラーリストの行ごとに、0始まりの行番号を設定する
        
          - 行ごとに、hiddenのinput要素を配置して、以下のnameとvalueを設定する
            
              - name：shared_crawler_行番号_id
            
              - value：レコードのid
        
          - 行ごとに、入力欄の各input要素に「shared_crawler_行番号」の形のname属性が設定される
        
          - 情報が0件だった場合は、入力欄を2行だけ表示する

2. 設定の保存

  - 保存時には、weko_admin.admin.LogAnalysisSettings.indexメソッドをPOSTで呼び出す
    
      - loganalysis_restricted_ip_addressテーブルへの保存時には、すべてのレコードを物理削除して、画面の各IPアドレスの行の入力内容からレコードを作成する
        
          - 「id」：自動採番
        
          - 「ip_address」：nameが「shared_crawler_行番号」であるinputの各入力値を「.」で連結したもの
    
      - loganalysis_restricted_crawler_listテーブルへの保存時には、以下の処理を行う
        
          - 共有クローラーリストの入力ごとに、レコードから、idが「shared_crawler_行番号_id」の値と等しいものを取得する
            
              - 該当するレコードがあったら、それを入力内容で更新する
            
              - 該当するレコードがなかったら、入力内容で新たにレコードを作成する
    
      - その後、GETで呼び出されたときと同様の処理を行う

3. イベントログ処理

  - modules/invenio-stats/invenio_stats/contrib/registrations.py の register_events 関数で初期化

  - 下記、register_events 関数にて、各インデックスに対する処理クラス、前処理を設定している。  
    ログ解析機能を利用して設定された情報は flag_restricted 関数内で利用されている。

> 〜省略〜
> 
> def register_events():
> 
> """Register sample events."""
> 
> return [
> 
> dict(
> 
> event_type='celery-task',
> 
> templates='invenio_stats.contrib.celery_task',
> 
> processor_class=EventsIndexer,
> 
> processor_config=dict(
> 
> preprocessors=[
> 
> flag_restricted,
> 
> flag_robots,
> 
> anonymize_user,
> 
> build_celery_task_unique_id
> 
> ],
> 
> suffix="%Y",
> 
> )),
> 
> 〜省略〜

  - 上記のflag_restricted関数内でweko_admin.api.is_restricted_user関数を呼び出して対象のログが除外対象かどうかのチェックを行う
    
      - 除外対象となるログは、「is_restricted」がtrueとなる
    
      - ログの「ip_address」と「user_agent」についてチェックを行い、どちらかで除外対象に含まれていればそのログは集計除外となる
        
          - 「ip_address」について、loganalysis_restricted_ip_addressテーブルにip_addressフィールドと「ip_address」とが一致するものがあった場合は除外対象となる
        
          - 「ip_address」と「user_agent」について、weko_admin.api._is_crawler関数を呼び出してチェックを行う
            
              - 以下のコンフィグで、共有クローラーリストによるチェックで正規表現を使用するかどうかを制御する
                
                  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/config.py#L1278>
                
                  - 設定キー：WEKO_ADMIN_USE_REGEX_IN_CRAWLER_LIST
            
              - 以下のコンフィグで定めたRedisデータベースに接続する
                
                  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L43>
                
                  - 設定キー：CRAWLER_REDIS_DB
            
              - loganalysis_restricted_crawler_listテーブルのアクティブな各レコードから取得した「list_url」をキーとして、接続したRedisデータベースから共有クローラーリストを取得する
                
                  - 正規表現を使用する場合は文字列、そうでなければset型で取得する
                
                  - 取得できなかった場合は、「list_url」を使ってインターネット上から共有クローラーリストを取得して、内容を加工したものをRedisデータベースに保存する
                    
                      - キーは「list_url」の値とする
                    
                      - 内容は以下のように加工する
                        
                          - 正規表現を使用する場合は、「#」で始まる行を除いた各行の内容を「|」で結合した文字列
                        
                          - 正規表現を使用しない場合は「#」で始まる行を除いた各行の内容
                    
                      - 保存するデータには、以下のコンフィグで定めたTTLを設定する
                        
                          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L44>
                        
                          - 設定キー：CRAWLER_REDIS_TTL
                    
                      - インターネット接続に失敗した場合、例外となって処理が終了する
                
                  - 「ip_address」と「user_agent」を、Redisデータベースに保存されていた、または保存した情報の中から探して、どちらか片方でも存在していたら除外対象に含める
                    
                      - 「is_restricted」に、is_restricted_user関数が返却する真偽値を設定する

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_admin.admin.LogAnalysisSettings.index`（GET/POST）。保存は `LogAnalysisRestrictedIpAddress.update_table` ＋ `LogAnalysisRestrictedCrawlerList.update_or_insert_list`（テーブル `loganalysis_restricted_ip_address` / `loganalysis_restricted_crawler_list`）。制限判定は `weko_admin.api.is_restricted_user` → `_is_crawler`（`CRAWLER_REDIS_DB` / `CRAWLER_REDIS_TTL`）。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
