
### OA Policy Confirmation（現在非対応）

※本機能はv0.9.22時点で非対応の機能だが、ソース上に残っているため機能仕様書としては既存のものを残す。

  - > 目的・用途

本機能は、SHERPA/RoMEOのオープンアクセスポリシー情報を確認できる機能である。

  - > 利用方法

ワークフロー一覧にて、ワークフローを選択後、「OA Policy Confirmation」アクションが表示される。

※ワークフローのアクションの１つとして、「OA Policy Confirmation」アクションが定義されていることが前提である

　ワークフローによっては、アクションの順番が異なるため、他のアクションから「OA Policy Confirmation」アクションに遷移することもある

「OA Policy Confirmation」アクションで雑誌名の情報を選択後、\[次へ\]ボタンを押下することで、次のアクションに進む。

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
<td>○</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

1\. SHERPA/RoMEOのオープンアクセスポリシー情報を確認する

  - 【前提条件】
    
      - 【Admin \> WorkFlow \> Flow List \> Create Flowの画面】  
        フローにて「OA Policy Confirmation」のアクションを定義する
    
      - 【Admin \> WorkFlow \> WorkFlow List \> Create WorkFlowの画面】  
        「OA Policy Confirmation」がフローに含まれるワークフローを定義する

  - SHERPA/RoMEOのオープンアクセスポリシー情報を確認する
    
      - 【OAポリシー確認画面】での「ジャーナル」（Journal）テキストボックスに検索文字列を入力する
        
          - SHERPA/RoMEOへのインクリメンタルサーチを可能とする
        
          - 検索結果を一覧に表示する
    
      - 検索結果より任意の雑誌を選択すると、同一画面上に以下の当該雑誌情報を表示する
        
          - 雑誌名　+　SHERPA/RoMEO詳細表示画面への\[Detail\]リンク
        
          - RoMEOの情報（RoMEO colours）  
            <http://www.sherpa.ac.uk/romeoinfo.html#colours>
        
          - 「Paid OA」の情報
    
      - 「次へ」（Next）ボタンを押すと、次アクションに進む
        
          - 選択した雑誌名の情報がJPCOARマッピングを元に、アイテム登録画面に自動入力される  
            JPCOARの項目：「jpcoar:sourceTitle」
    
      - 「保存」（Save）ボタンを押すと、設定内容を保存する

  - SHERPA/RoMEO検索APIから取得するリクエスト結果を、Redisを利用してキャッシュDB化する  
    また、RedisのTTLはコンフィグ設定可能とする【確認必要】

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - 
<!-- end list -->

  - > 処理概要

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
