### その他

  - > 目的・用途

本機能は、その他の運用設定を設定する機能である

  - > 利用方法

【Administration \> Setting (設定) \> Others (その他)】において、機関名を入力し、【Save (保存)】を押下することで、GoogleScholar向けメタデータのひとつの「学位授与機関名」として入力した機関名を付与する。

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

  - 【Administration \> Setting (設定)\> Others (その他) 画面】での「Institution Name」エリアに機関名を設定する  
    ※設定された機関名がGoogleScholar向けにアイテムメタデータとあわせて、「学位授与機関名」として出力される
    
      - デフォルト：空白
    
      - 「機関名」（Institution Name）テキストボックスに機関名を入力してから、「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する  
        メッセージ：「Institution Name was updated.」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_records\_ui

<!-- end list -->

  - > 処理概要

> 機関名を入力し、【Save (保存)】を押下した際に、weko\_records\_ui.admin.InstitutionNameSettingが呼び出される。

  - > weko\_records\_ui.models.InstitutionName.set\_institution\_nameが呼び出され、  
    > 入力した機関名をinstitution\_nameテーブルに設定する。

> 「INSTITUTION\_NAME\_SETTING\_TEMPLATE」：weko\_records\_ui.config

  - > 'weko\_records\_ui/admin/institution\_name\_setting.html'

> Google Scholar向けメタデータの出力の際は、weko\_records\_ui.utils.get\_google\_scholar\_metaからweko\_records\_ui.models.InstitutionName.get\_institution\_nameを呼び出して  
> intitution\_nameテーブルから機関名を取得する。

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
