# Identify設定

  - > 目的・用途

本機能は、Identifyの作成・編集を行う機能である。Identifyとは、リポジトリに関する情報を検索する場合に使用されるものである。

  - > 利用方法

【Administration＞OAI-PMH＞Identify】の順で画面遷移して利用する。

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

  - Identify出力に対してリポジトリの情報を設定可能
    
      - 設定内容
        
          - Output Set：チェックボックス
            
              - チェックボックスにチェックを入れる場合、OAI-PMHリクエストに対して、正常レスポンスを返す。
            
              - チェックボックスにチェックを入れない場合、OAI-PMHリクエストに対して、エラーレスポンスを返す。  
                [エラーと例外状況](https://www.nii.ac.jp/irp/archive/translation/oai-pmh2.0/OpenArchivesProtocol.htm#ErrorConditions)
        
          - Emails：管理者メールアドレスを入れる。
        
          - Repository Name：リポジトリ名を入れる。
        
          - Earliest Datastamp：Identifyの作成時間を自動で入れる。  
            フォーマット：YYYY-MM-DD HH:MM:SS
    
      - \[保存（Save）\]ボタンを押すと、設定された内容をIdentify一覧に追加させ、メッセージをIdentify一覧に表示させる  
        メッセージ：「レコードが正常に作成されました。（Record was successfully saved）」
    
      - \[保存して編集を続ける（Save and Continue Editing）\]ボタンを押すと、メッセージを編集画面での上端に表示させ、作成されたIdentiftyの編集を続けることを可能とする。  
        メッセージ：「レコードが正常に作成されました。（Record was successfully saved）」
    
      - 1つのリポジトリに対して1つしか登録できない。

  - OAI-PMHのIdentify情報を返戻可能

【Admin \> OAI-PMH \> Identify画面】上の設定値に基づき、OAI-PMHのIdentifyリクエスト(verb=Identify)に対してレスポンス可能とする。詳細は[Web-API API-2:OAI-PMH](#_OAI-PMH)を参照。

  - > 関連モジュール

<!-- end list -->

  - > Invenio-oaiserver

<!-- end list -->

  - > 処理概要

> 画面表示について

  - > 一覧タブ  
    > invenio\_oaiserver.admin.IdentifyModelViewが継承しているModelViewからflask\_admin.model.base.index\_viewが呼び出され、db内のoaiserver\_identifyテーブルより情報を取得し画面に表示する。

  - > 編集タブ  
    > \[鉛筆\]ボタン押下時、invenio\_oaiserver.admin.IdentifyModelViewが継承しているModelViewからflask\_admin.model.base.edit\_viewが呼び出され、db内のoaiserver\_identifyテーブルより情報を取得し編集画面へ遷移する。
    
      - > 編集画面で\[保存（Save）\]ボタンもしくは\[保存して編集を続ける（Save and Continue Editing）\]を押下時、flask\_admin.model.base.edit\_viewが呼び出され、編集内容をdb内のoaiserver\_identifyテーブルに保存し、更新する。

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
