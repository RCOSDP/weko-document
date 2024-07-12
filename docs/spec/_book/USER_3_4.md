### 引用情報表示

  - > 目的・用途

本機能は、引用情報を表示する機能である

  - > 利用方法

引用情報表示は、アイテム詳細画面のCite asエリアに表示される。表示のスタイルを「Start typing a citation style」から変更する。

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

  - アイテム詳細画面での「Cite as」エリアに引用情報を表示する
    
      - デフォルトスタイル：AAPG Bulletin

  - 「Start typing a citation style」テキストボックスに表示したいスタイルを選択できる
    
      - 「Start typing a citation style」テキストボックスにスタイルを入力すると、入力された値に合うスタイルが自動提案される
    
      - スタイルを選択すると、選択スタイルを適用した引用情報が\[Cite as\]エリアに表示される  
        選択スタイルが「Start typing a citation style」テキストボックスに表示される  
        ※それぞれのスタイルに応じて、UIに表示する引用情報が異なる

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_records\_ui

  - > invenio\_records\_rest

<!-- end list -->

  - > 処理概要

1\. 設定

> デフォルトスタイルを設定する

  - > パス：  
    > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/box/share.html#L50>

  - > デフォルトの設定値：「style= 'aapg-bulletin'」

> 表示内容

  - > 「n.d.」：「no date」の省略( <https://docs.citationstyles.org/en/v1.0.1/specification.html#date> )
    
      - datacite:dateにマッピングしているものを表示する  
        複数の項目をdatacite:dateにマッピングすると、ランダムに取得して表示する
    
      - 日付のフォーマットとして以下のものに対応する。データがない、もしくは以下のフォーマットに合致しない場合、「n.d.」となる。
        
          - YYYY
        
          - YYYY-MM
        
          - YYYY-MM-DD

> 以下にマッピングされた項目が出力される

  - > 作成者：jpcoar:creatorName

  - > 日付：datacite:date

  - > タイトル：dc:title

  - > 出版者：dc:publisher

  - > 開始ページ：jpcoar:pageStart

  - > 終了ページ：jpcoar:pageEnd

> 使用しているスタイル（packages.txt）

  - > citeproc-py-styles==0.1.2

2\. 実装方法

> モジュール：  
> invenio\_records\_rest.serializers.citeprocにおいてciteproc\_stylesを取得する。

  - > weko\_records：アイテムメタデータを取得するモジュールである

  - > invenio-records-rest：取得されたアイテムメタデータを引用情報として登録するモジュールである

> 引用情報の表示スタイルについて  
> アイテム詳細画面にアクセスする時、引用情報の表示スタイルを「invenio\_records\_rest」モジュールでの「citeproc\_styles」から、取得し表示する
> 
> 引用情報について

  - > アイテム詳細画面にアクセスすると、以下のようなアイテムメタデータをweko\_records.serializer.schemas.cslのRecordSchemaCSLJSON」で取得する
    
      - 公開日
    
      - その他のタイトル
    
      - 言語
    
      - 識別子登録(DOI)
    
      - 作成者
    
      - 内容記述
    
      - 号
    
      - 巻
    
      - 発行日
    
      - ページ数
    
      - 出版者
    
      - バージョン
    
      - id (pid\_value)

  - > 選択された表示スタイルによって、上記のアイテムの情報を取得し、「serialize」メソッドで引用情報とし登録し、UIに表示する  
    > invenio\_records\_rest.serializers/citeproc/CIteprocSerializerを使用する。

【補足】

> Cite asの情報での表示言語の優先度は以下の通りです。画面表示言語＞英語＞アイテム登録時のタイトルの言語

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
