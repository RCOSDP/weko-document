
### Google Scholar メタデータ出力

  - > 目的・用途

<!-- end list -->

  - > 本機能は、アイテム詳細画面から特定のアイテム情報をGoogle Scholar向けにGoogle Scholar meta tagを付与した状態でアイテムメタデータを出力する機能である利用方法

アイテムリストから特定のアイテムを選択することで、アイテム詳細画面を構成する要素、構造化データのheaderのタグの一つとして、Google Scholar meta tagが付与されたアイテムメタデータが表示される。

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

<!-- end list -->

  - Google Scholar meta tagを利用することで、論文検索に特化したGoogle Scholarにメタデータを登録することが出来る。

  - Google Scholar の実装にはGoogle Scholar meta tagが必要である。meta tag はOAI-PMHのXML出力と同じ機能を用いて出力される。

  - そのため、OAI-PMH出力をしなければ、Google Scholar meta tagは出力されない。OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。  
    OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_records\_ui

<!-- end list -->

  - > 処理概要

1\. 設定

> jpcoarのマッピングとGoogle Scholar meta tagとの対応をtarget\_mapに設定する。  
> <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/utils.py#L1204-L1213>

  - > 設定タグ：  
    > target\_map = {

> 'dc:title': 'citation\_title',
> 
> 'jpcoar:creatorName': 'citation\_author',
> 
> 'dc:publisher': 'citation\_publisher',
> 
> 'jpcoar:subject': 'citation\_keywords',
> 
> 'jpcoar:sourceTitle': 'citation\_journal\_title',
> 
> 'jpcoar:volume': 'citation\_volume',
> 
> 'jpcoar:issue': 'citation\_issue',
> 
> 'jpcoar:pageStart': 'citation\_firstpage',
> 
> 'jpcoar:pageEnd': 'citation\_lastpage', }
> 
> Google Scholar出力をすることのできるリソースタイプ

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L526-L574>

  - > 設定キー：「WEKO\_RECORDS\_UI\_GOOGLE\_SCHOLAR\_OUTPUT\_RESOURCE\_TYPE」

2\. 実装方法

> アイテムリストから特定のアイテムを選択し、アイテム詳細画面を表示する際に、get\_google\_scholar\_metaを使用して、画面を構成する要素として、Goggle Scholar meta tagをheaderのテンプレートに埋め込む。

  - > weko\_records\_ui.views.default\_view\_methodからweko\_records\_ui.utils.get\_google\_scholar\_metaを呼び出して使用する。

  - > アイテムの識別子としてoaiが含まれているかを確認する。
    
      - > OAI-PMH出力で使用されるjpcoarマッピングと置き換える形でGoogle Scholar meta tagを付与するため、OAI-PMH出力が出来る状態でなければGoogle Scholar meta tagを出力することは出来ない。
        
          - > 【前提条件】  
            > USER3-7「1. OAI-PMHスキーマを管理」及び「2. OAI-PMHスキーマをマッピング」が設定済み

  - > アイテムのリソースタイプがGoogle Scholar出力することができるか確認する。

  - > メタデータに含まれるjpcoarタグの種類に対応するGoogle Scholar meta tagをresリストに追加する。

> resリストをgoogle\_scholar\_metaで受け取り、templating.render\_templateを呼び出してアイテムメタデータを作成する。

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