
### Google Dataset メタデータ出力

  - > 目的・用途

本機能は、Google Dataset Search向けのメタデータを出力する機能である。

  - > 利用方法

  - > アイテムリストから特定のアイテムを選択することで、アイテム詳細画面を構成する要素、構造化データのheaderのタグの一つとして、Google Dataset meta tagが付与されたアイテムメタデータが表示される。利用可能なロール

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

  - Google Dataset meta tagを利用することで、データ検索に特化したGoogle Dataset Searchにメタデータ を登録することが出来る。
    
      - > meta tagはSchema.orgを利用する。  
        > <https://schema.org/>

  - \- 当該アイテムがOAIPMH出力されること
    
      - > Google Dataset の実装にはGoogle Dataset meta tagが必要である。meta tag はOAI-PMHのXML出力と同じ機能を用いて出力される。
        
          - > そのため、OAI-PMH出力をしなければ、Google Scholar meta tagは出力されない。OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。  
            > OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。

  - \- 当該アイテムのアイテムタイプがJPCOARスキーマにマッピングされていること

  - \- dc:typeがdatasetであること

  - \- dc:titleが入力されていること

  - \- datacite:descriptionが50字以上であること

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_records\_ui

<!-- end list -->

  - > 処理概要

1\. 設定

> Google Dataaset出力をすることのできるリソースタイプ

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L577>

  - > 設定キー：  
    > 「WEKO\_RECORDS\_UI\_GOOGLE\_DATASET\_RESOURCE\_TYPE = \[“dataset”\]」

> Google Dataset descriptionの最小文字数

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L580>

  - > 設定キー：  
    > 「WEKO\_RECORDS\_UI\_GOOGLE\_DATASET\_DESCRIPTION\_MIN = 50」

> Google Dataset descriptionの最大文字数

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L582>

  - > 設定キー：  
    > 「WEKO\_RECORDS\_UI\_GOOGLE\_DATASET\_DESCRIPTION\_MAX = 5000」

> 「WEKO\_RECORDS\_UI\_GOOGLE\_DATASET\_DISTRIBUTION\_BUNDLE」

  - > パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L585-L592>

> jpcoarマッピングとGoogle Dataset meta tagとの対応:  
> 別紙「jpcoarスキーマ、schema.org対応表」参照。

2\. 実装方法

> アイテムリストから特定のアイテムを選択し、アイテム詳細画面を表示する際に、get\_google\_dataset\_metaを使用して、画面を構成する要素として、Google Dataset meta tagをheaderのテンプレートに埋め込む。

  - > weko\_records\_ui.views.default\_view\_methodからweko\_records\_ui.utils.get\_google\_dataset\_metaを呼び出して使用する。

  - > アイテムの識別子としてoaiが含まれているかを確認する。
    
      - > OAI-PMH出力で使用されるjpcoarマッピングと置き換える形でGoogle Dataset meta tagを付与するため、OAI-PMH出力が出来る状態でなければGoogle Dateset meta tagを出力することは出来ない。
        
          - > 【前提条件】  
            > USER3-7「1. OAI-PMHスキーマを管理」及び「2. OAI-PMHスキーマをマッピング」が設定済み

  - > リソースタイプがdatasetか確認する。

  - > Google Datasetにおけるデータの説明部分であるdescriptionが50字以上か確認する。5000字よりも多い場合、5000字以降は切り捨てて登録する。

  - > メタデータに含まれるjpcoarタグの種類に対応するGoogle Dataset meta tagをres\_dataリストに追加する。

> resリストをgoogle\_dataset\_metaで受け取り、templating.render\_templateを呼び出してアイテムメタデータを作成する。

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