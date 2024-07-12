### ファイルアップロード

  - > 目的・用途

大容量データを安定的にWEKO3へアップロードする

  - > 利用方法

ユーザ画面のLarge File Uploadタブからファイルをアップロードする。

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

  - 大容量のファイルアップロードを行う。

  - 大容量ファイルアップロード失敗した場合のレジュームアップロードを行う。

  - レジュームアップロードのため、ログインユーザ自身がアップロードしたファイルの履歴を確認できる

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio-files-rest

<!-- end list -->

  - > 処理概要
    
      - 下記をJavaScriptから行うことでファイルアップロード・レジュームアップロードを実現する。
    
      - 新規アップロードの場合
        
          - files\_filesレコードを作成し、FileInstanceのUUIDを取得する
        
          - ObjectStorageへマルチパートアップロードの初期化APIを英クエストし、upload\_idを取得する
        
          - upload\_id, file\_idでfiles\_multipartrobjectレコードを追加する
    
      - レジュームアップロードの場合 upload\_idが正しい形式、有効かを検証するその後、新規アップロード・レジュームアップロード共通で下記を行う
        
          - ファイルをパートごとに分割し、files\_multipartobject\_partにすでにレコードが存在し、パートのハッシュ値を比較する
        
          - files\_multipartobject\_partにレコードが存在しない場合、ObjectStorageにパートをアップロードし、files\_multipartobject\_partにレコードを追加する

すべてのパートをアップロードし終えたら、ObjectStorageへマルチパートアップロードの完了APIをリクエストし、files\_multipartobjectレコードとfiles\_filesレコードを更新する

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
<p>2023/12/22</p>
</blockquote></td>
<td>4ec162bf3bdcf843df23863fbf7d5bb36ba875e4</td>
<td>W2023-42</td>
</tr>
</tbody>
</table>