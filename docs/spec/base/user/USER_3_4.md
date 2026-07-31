# 引用情報表示

## 目的・用途

本機能は、引用情報を表示する機能である

## 利用方法

引用情報表示は、アイテム詳細画面のCite asエリアに表示される。表示のスタイルを「Start typing a citation style」から変更する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

## 機能内容

  - アイテム詳細画面での「Cite as」エリアに引用情報を表示する

      - デフォルトスタイル：AAPG Bulletin

  - 「Start typing a citation style」テキストボックスに表示したいスタイルを選択できる

      - 「Start typing a citation style」テキストボックスにスタイルを入力すると、入力された値に合うスタイルが自動提案される

      - スタイルを選択すると、選択スタイルを適用した引用情報が[Cite as]エリアに表示される  
        選択スタイルが「Start typing a citation style」テキストボックスに表示される  
        ※それぞれのスタイルに応じて、UIに表示する引用情報が異なる

## 関連モジュール

  - weko_records_ui
  - invenio_records_rest

## 処理概要

1. 設定

デフォルトスタイルを設定する

  - パス：  
    <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/box/share.html#L50>

  - デフォルトの設定値：「style= 'aapg-bulletin'」

表示内容

  - 「n.d.」：「no date」の省略( <https://docs.citationstyles.org/en/v1.0.1/specification.html#date> )

      - datacite:dateにマッピングしているものを表示する  
        複数の項目をdatacite:dateにマッピングすると、ランダムに取得して表示する

      - 日付のフォーマットとして以下のものに対応する。データがない、もしくは以下のフォーマットに合致しない場合、「n.d.」となる。

          - YYYY

          - YYYY-MM

          - YYYY-MM-DD

以下にマッピングされた項目が出力される

  - 作成者：jpcoar:creatorName

  - 日付：datacite:date

  - タイトル：dc:title

  - 出版者：dc:publisher

  - 開始ページ：jpcoar:pageStart

  - 終了ページ：jpcoar:pageEnd

使用しているスタイル（packages.txt）

  - citeproc-py-styles==0.1.2

2. 実装方法

モジュール：  
invenio_records_rest.serializers.citeprocにおいてciteproc_stylesを取得する。

  - weko_records：アイテムメタデータを取得するモジュールである

  - invenio-records-rest：取得されたアイテムメタデータを引用情報として登録するモジュールである

引用情報の表示スタイルについて  
アイテム詳細画面にアクセスする時、引用情報の表示スタイルを「invenio_records_rest」モジュールでの「citeproc_styles」から、取得し表示する

引用情報について

  - アイテム詳細画面にアクセスすると、以下のようなアイテムメタデータをweko_records.serializer.schemas.cslのRecordSchemaCSLJSON」で取得する

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

      - id (pid_value)

  - 選択された表示スタイルによって、上記のアイテムの情報を取得し、「serialize」メソッドで引用情報とし登録し、UIに表示する  
    invenio_records_rest.serializers/citeproc/CIteprocSerializerを使用する。

【補足】

Cite asの情報での表示言語の優先度は以下の通りです。画面表示言語＞英語＞アイテム登録時のタイトルの言語

## 実装補足（v2.0.2 実装との突き合わせ）

- 引用情報は `invenio_records_rest.serializers.citeproc.CiteprocSerializer`＋`weko_records.serializers.schemas.csl.RecordSchemaCSLJSON`。既定スタイル `aapg-bulletin`。レンダリングは Jinja フィルタ `weko_records_ui.views.citation`。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
