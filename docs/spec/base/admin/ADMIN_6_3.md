
### サイトライセンス

  - > 目的・用途

本機能は、サイトライセンスユーザーによる操作ログの集計、解析を行い、その結果をサイトライセンス管理者にメールで送信する機能である。

  - > 利用方法

【Administration \> 統計（Statistics） \> サイトライセンス（Site License）画面】にて操作を行う。

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

  - 【Administration \> 統計（Statistics） \> サイトライセンス（Site License）画面】にてサイトライセンスの集計メール送信設定を管理する
    
      - 表示項目は以下の通りである
        
          - サイトライセンス機関
            
              - 【Administration \> 設定（Setting） \> サイトライセンス（Site License）画面】に登録された機関名のリストを表示し、チェックボックスを用意する
                
                  - 機関名の表示情報は以下の通りである
                    
                      - 「Organization」：機関名
                    
                      - 「メールアドレス」（Email Address）
            
              - リポジトリ管理者は、送信したい機関にチェックボックスでチェックできる
            
              - 初期値は全てのチェックボックスにチェックがついていない状態とする
            
              - 選択状態を変更すると、［保存（Save）］ボタンを押すまで［メール手動送信（Manual Send）］ボタンが非活性になる
        
          - 「Automatic Send」
            
              - 自動送信を「送信／無効」（Enable／Disable）のラジオボタンを設ける
            
              - ラジオボタンの初期値は「無効」（Disable）とする
            
              - 送信する期間（from-to）はコンフィグで設定し、初期値は１ヶ月分（先月）とする。  
                例：7月にメールを送信する場合は、6月分のデータを集計して送信する
            
              - 選択状態を変更すると、［保存（Save）］ボタンを押すまで［メール手動送信（Manual Send）］ボタンが非活性になる
        
          - 「メール手動送信」（Manual Send）
            
              - 画面上に集計年と月を設定するプルダウンを表示し、年月を選択できる
            
              - 集計月は単月以外も集計できるようにfromとtoをそれぞれ設定する
            
              - from-toの初期値は１ヶ月分（先月）とする。たとえば、2019年7月に本画面を開いた場合は、from-toの初期値は「2019/06 - 2019/06」となる
            
              - ［メール手動送信（Manual Send）］ボタンを押すと、メール送信確認ダイヤログを表示する  
                確認メッセージ：「Are you sure you want to send an email?」
                
                  - ［Confirm］ボタンを押すと、後述の送信時の処理に従って、対象機関にメールを発信する
                
                  - ［閉じる（Close）］ボタンを押すと、ダイヤログを閉じる
        
          - ［保存（Save）］ボタンを押すと、設定内容を保存し、メッセージを表示する  
            メッセージ：「Update successfully」
        
          - 送信時の処理(v0.9.22)
            
              - 宛先：チェックした機関のメールアドレス
            
              - 件名：\[○○機関リポジトリ\]YYYY.MM-yyyy.mm statistics report  
                ※YYYY.MMは集計月(from), yyyy.mmは集計月(to)を表示
            
              - メールのテンプレート： https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko\_admin/templates/weko\_admin/email\_templates/site\_license\_report.html
            
              - 本文：サイトライセンス利用統計の内容
                
                  - WEKO Top Page Access Count
                
                  - Number Of Searches
                
                  - Number Of Views
                
                  - Number Of File download
                
                  - Number Of File Regeneration
        
          - 送信時の処理(※)
            
              - ※0.9.22には取り込まれていないが、メールの内容が既存の機能仕様書の通りになるよう修正されているので、以下に既存の機能仕様を残しておく。
            
              - 宛先：チェックした機関のメールアドレス
            
              - 件名：\[○○機関リポジトリ\]YYYY.MM-yyyy.mm 利用統計レポート  
                ※YYYY.MMは集計月(from), yyyy.mmは集計月(to)を表示
            
              - メールのテンプレート： サイトライセンス利用統計メールひな形.docx
            
              - サイトライセンス利用統計の内容

<table>
<thead>
<tr class="header">
<th>#</th>
<th>ファイル名</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>FileDownloadReport_YYYY-MM - YYYY-MM.tsv</td>
<td>サイトライセンス認可ユーザーが実施したファイルダウンロード回数の統計を出力する<br />
オンラインISSNを設定したインデックスごとにファイルダウンロード回数を出力する<br />
ファイルダウンロード回数が0のインデックスであっても出力する</td>
</tr>
<tr class="even">
<td>2</td>
<td>FileViewReport_YYYY-MM - YYYY-MM.tsv</td>
<td>サイトライセンス認可ユーザーが実施したファイル再生回数の統計を出力する<br />
オンラインISSNを設定したインデックスごとにファイル再生回数を出力する<br />
ファイル再生回数が0のインデックスであっても出力する</td>
</tr>
<tr class="odd">
<td>3</td>
<td>SearchReport_YYYY-MM - YYYY-MM.tsv</td>
<td>サイトライセンス認可ユーザーが実施したキーワード検索の統計を出力する</td>
</tr>
<tr class="even">
<td>4</td>
<td>UsagestatisticsReport_YYYY-MM - YYYY-MM.tsv</td>
<td>サイトライセンス認可ユーザーが実施した詳細画面閲覧回数、ファイルダウンロード回数の統計を出力する<br />
オンラインISSNを設定したインデックスごとに詳細画面閲覧回数、ファイルダウンロード回数を出力する<br />
詳細画面閲覧回数、ファイルダウンロード回数共に0のインデックスであっても出力する</td>
</tr>
</tbody>
</table>

  - > 関連モジュール

<!-- end list -->

  - > weko-admin

  - > invenio-stats：サイトアクセスレポートを取得する

  - > invenio-mail：メールを送信する

<!-- end list -->

  - > 処理概要

> 画面表示したとき、［保存（Save）］ボタンを押したときの処理は、以下で行う。

  - > パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/admin.py>

  - > SiteLicenseSendMailSettingsViewクラスのindexメソッド
    
      - > ［保存（Save）］ボタンを押したときは、画面からPOSTで呼び出される。POSTで呼ばれたときに限り、データの更新を行う。
        
          - > 「Automatic Send」ラジオボタンの選択状態によって、admin\_settingsテーブルの、nameが「site\_license\_mail\_settings」であるレコードを更新する。
        
          - > サイトライセンス機関のチェック状態によって、sitelicense\_infoテーブル各行のreceive\_mail\_flagカラムを更新する。
    
      - > POSTで呼ばれたときのデータ更新後、およびGETで呼ばれたとき、以下の情報を取得する。
        
          - > サイトライセンス機関の情報として、sitelicense\_infoテーブルのレコード全件（organization\_id昇順）
        
          - > 自動送信設定として、admin\_settingsテーブルの、nameが「site\_license\_mail\_settings」であるレコード
        
          - > メール手動送信の集計月の初期値として、「現在のUTC日付のdayを1にした日付の前日」のdayを1にした日付
    
      - > 呼び出し元の画面では、POSTの結果にかかわらず、画面を更新する。

> ［メール手動送信（Manual Send）］ボタンを押したときの処理は、以下で行う。

  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-admin/weko_admin/views.py>

  - manual\_send\_site\_license\_mailメソッド
    
      - sitelicense\_infoテーブルから、receive\_mail\_flagの値が「T」であるレコード全件を取得する。
    
      - レコードが取得できたら、以下の処理を行う。
        
          - 集計月の入力値より、fromの月の1日を「start\_date」、toの月の最終日を「end\_date」とする。
        
          - QueryCommonReportsHelper.getメソッドによって、サイトアクセスレポートを取得する。
        
          - 取得したサイトアクセスレポートを用いて、send\_site\_license\_mailメソッドでサイトライセンス機関のメールアドレスに対してメールを送信する。
            
              - > サイトライセンス機関のアクセスレポートが取得できなかった場合は、各項目を０件とする。
        
          - 送信が失敗した場合は、エラーログを出力する。送信結果にかかわらず、’finish’を返す。

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