# ワークフロー連携

## 1. WEB APIを用いてGakuNinRDMから登録対象データを受領する

- WEB APIを用いて「WEKO3の一括登録フォーマット※」を取得する（OAuth2による認証・認可を行う）

  - (※)WEKO3での一括登録フォーマット：　アイテムタイプ単位のTSV形式ファイルのzipファイル  
    今回の実証では、「デフォルトアイテムタイプ(フル)」を使用する

- 接続および対象データの取得が行えない場合は、受付エラーとしてWEB APIでの受領に対してのエラーとして返す。（APIエラー、認証エラーを想定）

- 「WEKO３の一括登録フォーマット」として対象データを受取れなかった場合は、フォーマットエラーとしてWEB APIの受領に対してのエラーとして返す。（フォーマット不正を想定）

- 受け付けた「WEKO3の一括登録フォーマット」の対象データを保持する。（WEKO3のアクティビティ生成で利用する）

- WEB APIを介した登録データの受付情報を記録する。

  - タイムスタンプ、接続者の情報を記録する。エラーがある場合はエラー情報を記録する。

- 詳細のシーケンス図は以下を参照  
  <https://redmine.devops.rcos.nii.ac.jp/attachments/25959/SequenceDiagram.xlsx>

![](media/media/image6.png)

## 2. アイテム登録するフローを用意する

- WEB API経由で受け取る「一括登録フォーマット」でのアイテム情報を、ワークフローでアイテム登録をするためのフローを用意する。

  - 使用するアクションおよびアクション実施順序を確定させる。

  - アクションを定義しフローを作成する。フローは以下の通り。

    1.  Item Registration

    2.  Item Link

    3.  Identifier Grant

    4.  Approval

## 3. 一括登録フォーマットのアイテム情報からアイテムを登録する

- 一括登録フォーマットに従ったアイテム情報1件分からアイテムを登録する

  - アクティビティに関連付けられるアイテムを指定されるアイテムタイプから生成する

    - 一括登録フォーマットに従ったアイテム情報を登録する処理において行う事前チェックを実施する。

  - 事前チェックにてエラーが発生した場合は、アクティビティの作成を中止する

    - エラー情報を返す。

  - 事前チェックにてエラーがなかった場合に、アイテムを登録する。

- ワークフロー上はItemRegistrationで留めておく

  - 登録完了までいかず、途中からワークフローを再開できるようにする

- システム連携において、一括登録フォーマットのアイテム情報からアイテムの  
  メタデータ項目とインデックス情報を取り込んだアクティビティを生成する。

- 該当のアクティビティは、アクティビティ一覧にDoingの状態で表示され、クリックすることでItemRegistration画面のメタデータ入力画面が表示される。  
  （このとき、メタデータ項目が入力されている状態である）

- [次へ]でインデックス選択画面を表示した際も、取り込んだ該当のインデックスにチェックが付いている状態で保持されているものとする

**【補足】**

- アイテムIDは指定をしても、値は無視して自動採番する

## 4. システムからAPIを経由したアイテム登録の実証

- WEB APIを用いて、アイテムを取得し、WEKO3のワークフローを通したアイテム登録の流れは以下の通り

### 4.1. OAuth2による認証・認可設定

- 連携システムからのAPI接続にはOAuth2認証を用いるため、事前に接続用の認証トークンを生成する

- API経由での登録アクティビティを利用するためのScopeとして、「user:activity」を用いる

- Access Admin> Profile　画面の "New token" ボタンを押下し、生成したいScopesの選択肢から「user:activity」Scopesにチェックを入れる

- 生成したトークンをシステム側のAPIで利用する

![グラフィカル ユーザー インターフェイス, アプリケーション 自動的に生成された説明](media/media/image7.png)
![グラフィカル ユーザー インターフェイス, テキスト, アプリケーション, メール, Web サイト 自動的に生成された説明](media/media/image8.png)

- ※実証実験にあたっては、上記で発行したアクセストークンをPosmanツールに指定して利用

- ※実証用のプログラムをマージ後にクリーンビルドせずに、既に稼働している環境に取り込む場合、以下の設定を行う必要がある

```
* Update folder permission:

-----

　sudo chown -R 1000:1000 ./modules/invenio-oauth2server/

　sudo chown -R 1000:1000 ./modules/weko-workflow/

-----

* Reinstall module's packages:

-----

　docker-compose exec web pip install -e /code/modules/invenio-oauth2server

　docker-compose exec web pip install -e /code/modules/weko-workflow

-----

* Restart docker:

-----

　docker-compose stop; docker-compose up -d

-----

* Rebuild bundle/static files:

-----

　docker-compose exec web invenio collect -v;docker-compose exec web invenio assets build

-----
```

### 4.2. アイテム登録連携用API

- 以下、3つのAPIを利用する

  - アイテム登録アクティビティの開始: POST /depositactivity

  - 登録アクティビティの取得: GET /depositactivity/{activityId}

    - 登録アクティビティの状態を取得する

  - 登録アクティビティのキャンセル: DELETE /depositactivity/{activityId}

    - 登録したアクティビティを「強制終了」する

### 4.3. アイテム登録連携用APIで利用するワークフローおよびフロー

- アクティビティの生成とworkflow_idについて

  - 連携システム側からAPIでファイルを受け渡し、ワークフローのItemRegistration画面で留めておくためには1件ずつ、アクティビティを生成しておく必要がある

  - また、アクティビティ生成にあたっては、どのワークフローで登録するか、workflow_idを指定する必要がある

  - 今回の実証では、以下の設定値として、configファイル指定(WEKO_WORKFLOW_GAKUNINRDM_DATA)を行った

- **ワークフロー定義**

  - ワークフロー名称：「GRDM_デフォルトワークフロー」

  - 'workflow_id': -1,

![グラフィカル ユーザー インターフェイス, アプリケーション, Word, メール 自動的に生成された説明](media/media/image9.png)

- **アイテムタイプ定義**

  - アイテムタイプは「デフォルトアイテムタイプ（フル）」を使用する

- **フロー定義**

  - 使用するフローは以下の通りとする

    - フロー名称：「GRDM_デフォルトフロー」

      1.  Start

      2.  Item Registration

      3.  Item Link

      4.  Identifier Grant

      5.  Approval

      6.  End

![グラフィカル ユーザー インターフェイス, アプリケーション, Teams 自動的に生成された説明](media/media/image10.png)

### 4.4. 一括登録フォーマットのアイテム情報からアイテムを登録する

- 一括登録フォーマットに従ったアイテム情報1件分からアイテムを登録する

1.  アクティビティに関連付けられるアイテムを指定されるアイテムタイプから生成する

    - 一括登録フォーマットに従ったアイテム情報を登録する処理において行う事前チェックを実施する

        - アイテムの一括登録(インポート)では、ItemRegistrationの後続の処理、ID・DOI付与全ての工程を行えるが、このワークフロー連携では、ワークフロー上はItemRegistrationで留めておく必要がある（登録完了までいかず、途中からワークフローを再開できるようにするため）

        - そのため、ワークフロー連携では一括登録フォーマットに従うものの、以下の項目は指定しても処理に利用しない

            - .id （アイテムID。IDが自動採番されるため、IDのチェックが不要。）

            - .uri　（アイテムのURI。IDが自動採番されるため、URIのチェックが不要。）

            - .edit_mode （アクティビティの新規作成のため無視する。入力しなくてもエラーとならない）

            - .cnri　（ハンドル情報。ハンドル設定がONの場合、Item Registrationの「Next」ボタンを押下する際に自動申請されるため、設定が不要。）

            - .doi_ra　（DOI情報。Item Registrationに止めるので、DOI情報のチェックが不要）

            - .doi　（DOI情報。Item Registrationに止めるので、DOI情報のチェックが不要）

            - .Identifier Registration　（ID登録、ID登録タイプ。DOI情報ですが、DOI付与しないため、無視する）

2.  事前チェックにてエラーが発生した場合は、アクティビティの作成を中止する

    - チェックエラー情報をログに記録する。（今回の実証ではチェック内容の詳細定義や、チェック結果の返戻実装は対象外）

![テキスト 自動的に生成された説明](media/media/image11.png)

3.  事前チェックにてエラーがなかった場合に、アイテムを登録する

    - 以下は、疑似的にPostmanツールを使用して、外部からAPIを叩いてみた内容

![コンピューターのスクリーンショット 自動的に生成された説明](media/media/image12.png)

    - 上記APIを叩くことで、WEKO側に新規のアイテム登録アクティビティを生成することができる

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
|  | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/14 |  | 本文を実装準拠に修正 |

## 実装補足（v2.0.2 実装との突き合わせ）

- GakuNinRDM 連携のエンドポイントは小文字 `/depositactivity`（POST）/ `/depositactivity/<activity_id>`（GET, DELETE）、処理クラスは `weko_workflow.views.ActivityActionResource`。OAuth2 スコープ `user:activity`（`weko_workflow.scopes.activity_scope`）。config `WEKO_WORKFLOW_GAKUNINRDM_DATA`（workflow_id=-1 / flow_id=-1 / item_type_id=15 / action_endpoint_list=[begin_action, item_login, item_link, identifier_grant, approval, end_action]）、`WEKO_WORKFLOW_GAKUNINRDM_PREFIX`（ログ接頭辞）。
