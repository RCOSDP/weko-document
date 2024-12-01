### アイテムバージョン管理

  - > 目的・用途

本機能は、アイテムを更新したバージョンの情報を表示し、アイテムバージョンを管理する機能である。

  - > 利用方法

アイテムバージョンは、アイテム詳細画面の右端にあるバージョンの一覧を押下することで表示される。  
アイテムバージョンの管理は、アイテム詳細画面の【編集 (Edit)】からバージョンの変更/維持を選択し、管理する。

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
<td>○</td>
<td>○</td>
</tr>
</tbody>
</table>

  - > 機能内容

1\. アイテムバージョン一覧を表示する

  - アイテム詳細画面での「バージョン (Versions)」領域にアイテムバージョン一覧を表示する
    
      - 4つの最新バージョンを以下のフォーマットで表示する
        
          - 「Ver.」 +バージョン番号
        
          - 更新日付。フォマード：YYYY-MM-DD hh:mm:ss.tttttt
    
      - 「Show all versions」リンクを押すと、すべてのバージョンを表示する

  - アイテムバージョン一覧から、バージョンリンクを押すと、該当バージョンのアイテム情報を反映する
    
      - T「here is a newer version of this record available.」のメッセージを画面上部に表示する
    
      - 最新バージョン以外のアイテムは更新できない（「編集」ボタンを非表示とする）
    
      - OAI-PMH出力のボタンを押すと、画面で表示しているバージョンを対象とする
    
      - JSON、BIBTEX出力のリンクを押すと、画面で表示しているバージョンを対象とする

2\. アイテム編集時にバージョンの変更／維持を選択できる

  - > アイテムの編集権限があるユーザーには、アイテム詳細画面での【編集（Edit）】ボタンを押すと、アイテムのメタデータが編集できる。  
    > アイテム編集画面に編集したアイテムのバージョンの変更／維持が選択できる。

  - バージョンの変更 (Upgrade Version)／維持 (Keep Version)の選択をアイテム編集画面の「バージョン管理」（Version Management）に表示する  
    必須項目とする

  - 初期値は維持 (Keep Version)

  - 選択肢：「バージョンを更新する」（Upgrade Version）、「バージョンを維持する」（Keep Version）
    
      - 「バージョンを更新する」を選択
        
          - 編集したアイテムのバージョンを新規バージョンとする
    
      - 「バージョンを維持する」を選択
        
          - バージョンを維持してアイテムを更新する
        
          - バージョンを維持して更新したことをアプリケーションのログに記録する

  - 【アイテム編集について】
    
      - アイテム編集時に旧バージョンは以前の公開ステータスが引き継がれること
    
      - バージョン数が10を超えても正しく登録できること
    
      - ItemRegistration画面のバージョンを更新／維持のラジオボタンについて、デフォルトで「バージョンを維持する」にチェックが入っていること

  - 【アイテム削除について】
    
      - アイテム詳細画面では以下のようになること  
        →旧バージョン：「削除」ボタンを非表示とする  
        →最新バージョン：「削除」ボタンを表示する  
        →「Delete This version」ボタンを押下すると当該バージョンのみのを削除する
    
      - ハーベストの時に、対象のアイテムが削除された場合（ハーベスト先のリポジトリからdelete情報を受け取った際）全バージョンを論理削除する
    
      - 一括削除（Administration\>アイテム (Items)\>一括削除 (Bulk Delete)）時に、対象としたアイテムのすべてのバージョンを論理削除する
    
      - 削除／復元（Administration\>レコード管理 (Records)\>レコードメタデータ (Record Metadata)で旧バージョンのみの論理削除はできないこと
    
      - 最新バージョン削除時は旧バージョンもすべて論理削除されること

3\. アイテムバージョンの表示/非表示を設定できる

【Administration \> アイテムタイプ管理 (Item Types) \>メタデータ (Meta)画面】から、アイテムタイプのバージョンの表示／非表示を設定できる

1.  > 過去のバージョンを表示（初期値）

2.  > 過去のバージョンは非表示

ログイン有無またユーザのロールによる区別は行わない

  - > 関連モジュール

<!-- end list -->

  - weko-records-ui

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - アイテムのバージョン一覧を表示する処理
    
      - 該当アイテムのpid\_ver、active\_versionsをweko\_records\_ui.view.default\_view\_methodで取得する
    
      - アイテムが下書きの状態の場合、アイテムバージョン一覧には表示しない。  
        \['\_deposit'\]\['status'\] == 'draft' の場合は取得したactive\_versionsを削除する。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/views.py#L423>
    
      - デフォルトとし、4つの最新バージョンをアイテム詳細画面に表示する
        
          - 表示内容：バージョン番号、更新日付
    
      - 「Show all versions」リンクを押すと、すべてバージョンを表示する

  - 該当バージョンのアイテムメタデータを表示する処理
    
      - アイテムバージョン一覧からバージョンをクリックすると、PIDの値を取得し、該当メタデータを取得し、表示する  
        weko\_records\_ui.templates.weko\_records\_ui.box.versionsにおいてinvenio\_records\_ui.recidを使用する。  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/box/versions.html>
    
      - OAI-PMH出力及びJSON、BIBTEX出力を実行する時、表示しているバージョンのPID値を取得し、実行する  
        invenio\_oaiserver.response.pyを使用する。

  - アイテムのバージョンダウンをする操作は無い（バージョンダウンをするためにはDB,ESで紐づいているファイルのデータの変更や削除をする必要があり、そのような実装はしていない）
    
      - 暫定対策( [WEKO3\_OPE-282](https://nii.backlog.jp/view/WEKO3_OPE-282#comment-1296314189) )
        
          - 旧バージョンのPIDのステータスを"D"にすることで、関連ファイルへのアクセスを防ぐことができる  
            ※ver.1 が表示されなくなるため、 ver.1へのアクセスもできなくなる。  
            　ただし、ver.2という表示が残るのと、物理ファイルは残る。

  - バージョンアップして更新した場合、古いバージョンのアイテムの公開状態はそのまま維持する（新しいバージョンは公開状態となる）

  - バージョン欄の時刻は UTC として表記されている。  
    JSTに切り替える機能は無く、切り替えるためには、 <https://invenio-i18n.readthedocs.io/en/latest/api.html#module-invenio_i18n.jinja2> を使用して実装する必要がある。
  
  - バージョン欄の時刻は pidstore_pid の pid_type: recid の updated カラムの日時を表示している。

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