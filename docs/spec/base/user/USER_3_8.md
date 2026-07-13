### Google Scholar メタデータ出力

#### 目的・用途

本機能は、アイテム詳細画面から特定のアイテム情報をGoogle Scholar向けにGoogle Scholar meta tagを付与した状態でアイテムメタデータを出力する機能である

#### 利用方法

アイテムリストから特定のアイテムを選択することで、アイテム詳細画面を構成する要素、構造化データのheaderのタグの一つとして、Google Scholar meta tagが付与されたアイテムメタデータが表示される。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

#### 機能内容

  - Google Scholar meta tagを利用することで、論文検索に特化したGoogle Scholarにメタデータを登録することが出来る。

  - Google Scholar の実装にはGoogle Scholar meta tagが必要である。meta tag はOAI-PMHのXML出力と同じ機能を用いて出力される。

  - そのため、OAI-PMH出力をしなければ、Google Scholar meta tagは出力されない。OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。

#### 関連モジュール

  - weko_records_ui

#### 処理概要

1. 設定

jpcoarのマッピングとGoogle Scholar meta tagとの対応をtarget_mapに設定する。  
<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/utils.py#L1204-L1213>

  - 設定タグ：

    ```
    target_map = {
        'dc:title': 'citation_title',
        'jpcoar:creatorName': 'citation_author',
        'dc:publisher': 'citation_publisher',
        'jpcoar:subject': 'citation_keywords',
        'jpcoar:sourceTitle': 'citation_journal_title',
        'jpcoar:volume': 'citation_volume',
        'jpcoar:issue': 'citation_issue',
        'jpcoar:pageStart': 'citation_firstpage',
        'jpcoar:pageEnd': 'citation_lastpage',
    }
    ```

Google Scholar出力をすることのできるリソースタイプ

  - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py#L526-L574>

  - 設定キー：「WEKO_RECORDS_UI_GOOGLE_SCHOLAR_OUTPUT_RESOURCE_TYPE」

2. 実装方法

アイテムリストから特定のアイテムを選択し、アイテム詳細画面を表示する際に、get_google_scholar_metaを使用して、画面を構成する要素として、Goggle Scholar meta tagをheaderのテンプレートに埋め込む。

  - weko_records_ui.views.default_view_methodからweko_records_ui.utils.get_google_scholar_metaを呼び出して使用する。

  - アイテムの識別子としてoaiが含まれているかを確認する。

      - OAI-PMH出力で使用されるjpcoarマッピングと置き換える形でGoogle Scholar meta tagを付与するため、OAI-PMH出力が出来る状態でなければGoogle Scholar meta tagを出力することは出来ない。

          - 【前提条件】  
            USER3-7「1. OAI-PMHスキーマを管理」及び「2. OAI-PMHスキーマをマッピング」が設定済み

  - アイテムのリソースタイプがGoogle Scholar出力することができるか確認する。

  - メタデータに含まれるjpcoarタグの種類に対応するGoogle Scholar meta tagをresリストに追加する。

resリストをgoogle_scholar_metaで受け取り、templating.render_templateを呼び出してアイテムメタデータを作成する。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
