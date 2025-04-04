### Elasticsearchインデックス

<!-- end list -->

  - > 目的・用途

Elasticsearchのマッピング変更や検索設定の変更を反映するために、

管理画面からWEKOに登録されたアイテムの再インデックスを可能にする機能を提供する画面。

  - > 利用方法

管理画面の「メンテナンス機能」にある「Elasticsearchインデックス」メニューから、「アイテムインデックスの再作成」「アイテムの再インデックス」を実行できる。  
本機能の利用は、メンテナンス期間中に限られる。また、本機能にて万が一障害が発生した場合は、下記の方法での対応を想定している。

  - 障害原因の調査
    
      - 原因特定のためにまず確認すべきと想定される情報ソースを下記に記載します。
        
          - 画面上部の赤帯に記載のエラーメッセージ
        
          - ※同様のERRORがログに記載されているはずなので必須ではありませんが、原因特定にかかる時間を短縮できます
        
          - アプリケーションログ
        
          - Celery taskの実行ログ
        
          - ElasticSearchの起動状況
        
          - RabbitMQの起動状況
        
          - ElasticSearchのアイテムインデックス（\*-weko-item-\*）と本処理の一時保管用のインデックスElasticSearchのアイテムインデックス（\*-weko-item-\*-tmp）の、ドキュメント・Mappings・Settings・Aliasの情報

  - 障害原因の解消およびデータの修正
    
      - ケースバイケースとなるため、省略します。

  - 実行制御の解除
    
      - エラーが発生した際に、画面からの処理実行ができないように制御がされているので、これを下記の方法で解除します。
        
          - データベースのadmin\_settingsテーブルのelastic\_reindex\_settingsという名のレコードのsettingsが{"has\_errored": true}となっているため、これを{"has\_errored": false}に変更します。

<!-- end list -->

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

  - 「アイテムインデックスの再作成」の実行機能
    
      - マッピング・セッティング定義を初期状態にリセットして、現在のElasticSearchのアイテムインデックスをもとに再度ElasticSearchのアイテム・インデックスツリーの情報を作成しなおす機能。

  - 「アイテムの再インデックス」の実行機能
    
      - マッピング・セッティング定義を初期状態にリセットした後、DataBaseにある情報をもとにElasticSearchのアイテム・インデックスツリーの情報を作成しなおす機能。

  - 同時実行を制限する機能
    
      - 二重実行や、「アイテムインデックスの再作成」と「アイテムの再インデックス」の同時実行を防ぐ機能。

  - エラー発生時、再実行を禁止する機能
    
      - 障害原因の解消とデータメンテナンスが完了するまでは再実行禁止する運用前提。

  - 実行前に、処理に時間がかかる旨を確認する機能
    
      - 「アイテムインデックスの再作成」「アイテムの再インデックス」どちらの場合も確認を行う。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_admin

<!-- end list -->

  - > 処理概要

> 対応しているViewクラス：admin.py:: ReindexElasticSearchView
> 
> 「アイテムの再インデックス」でのDBからElasticSearchへ登録する機能は、既存実装を呼び出す形で行っている。レコードメタデータにある値をElasticSearchの検索フィールドにマッピングは、Signalから呼び出される処理を利用して達成している。
> 
> エラー発生の情報はDBで管理する

  - テーブル：「admin\_settings」

  - フィールド：'name'="elastic\_reindex\_settings"

例：

> {"has\_errored": false}

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