### Identifier Grant

#### 目的・用途

- DOI未付与、かつDOI取り下げ済みではないアイテムに対してはDOIを付与する事が可能である

- DOIのURL形式：<ルートURL>/<Prefix>/<suffix>

  - <ルートURL>：コンフィグファイルでの設定
  - <Prefix>：アドミン画面に指定されている値
  - <suffix>：コンフィグファイルでの設定値によって異なる

- ハンドルのURL形式：<ハンドルのURL>/<Prefix>/<ハンドルローカル名>

  - <ハンドルのURL>：コンフィグファイルでの設定
  - <Prefix>：「handle_creds.json 」ファイルに設定値  
    キー："prefix"
  - <ハンドルローカル名>：LHS（Local Handle Server）から返却される値で、ユニークの値

- 外部機能として、  
  WEKOからDOI付与申請を行う場合は、IRDBのハーベスト処理で学術機関リポジトリデータベース(IRDB)を経由して、  
  JaLCに対してDOI付与を申請する事が可能である  
  　WEKO -> IRDB -> JaLC

#### 利用方法

ワークフロー一覧にて、ワークフローを選択後、「Identifier Grant」アクションが表示される。

※ワークフローのアクションの１つとして、「Identifier Grant」アクションが定義されていることが前提である

　ワークフローによっては、アクションの順番が異なるため、他のアクションから「Identifier Grant」アクションに遷移することもある

「Identifier Grant」アクションで必要な情報を選択／入力後、[次へ]ボタンを押下することで、次のアクションに進む。

#### 利用可能なロール

| ロール   | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| :------: | :------------: | :--------------: | :----------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       ○       |        ○        |         ○         |      ○      |      ※      |                    |

※一般ユーザーは、ロールとして利用可能に設定することはできないが、個別のユーザーをAction Userとして設定することはできる。

#### 機能内容

DOI付与の種類

現在4つのDOI付与を以下のように対応している

- JaLC DOI
- JaLC CrossRef DOI
- JaLC DataCite DOI
- NDL JaLC DOI

1. 構成

1.1. 外部からの設定

- HANDLEツール（https://www.handle.net/tech_manual/HandleTool_Ver2.pdf）
- CNRIのHANDLEツールを使い、ハンドルアクセスのURLを要求する。

1.2. 管理者からの設定

- 【Administration > 設定（Setting） > 識別子（Identifier） > 作成（Create）画面】

  - 「Prefix」領域より、テナント別に各DOI発行機関のプレフィックス情報を設定  
    　　プレフィックス設定項目：Reposiitory(必須)、JaLC DOI、JaLC CrossRef DOI、JaLC DataCite DOI、NDL JaLC DOI

  - 「Suffix」領域より、テナント別にサフィックスの前半部分を設定  
    　　サフィックス設定項目：Reposiitory(必須)、Semi-automatic suffix

  - 「Enable/Disable」領域より、テナント別に各DOI発行機関の利用可否を設定

- 【Administration > ワークフロー管理（WorkFlow） > フロー（Flow List） > Create Flowの画面】

  - フローにて「Item Registration」のアクション後に「Identifier Grant」のアクションを定義

- 【Administration > ワークフロー管理（WorkFlow） > ワークフロー（WorkFlow List） > Create WorkFlowの画面】

  - 「Identifier Grant」がフローに含まれるワークフローを定義

2. 機能

2.1. 前提条件

- 機能内容の「1. 構成」、処理概要の「2. サーバー設定」のように設定済みである

2.2. 識別子付与画においてDOI発行機関を選択可能

- 選択肢

  - Not Grant（デフォルト）
  - JaLC DOI
  - JaLC CrossRef DOI
  - JaLC DataCite DOI
  - NDL JaLC DOI

2.3. PID発行機関が指定するメタデータ制約条件に基づきバリデート

- 「Identifier Grant」画面から[次へ（Next）]ボタン押下時に、設定したPID発行機関と、アイテムの入力値を以下の資料で比較する  
  　　PID付与の制約条件の資料：　別紙「JPCOARv2_JaLC_Guideline_appendix_ver1.pdf」

  - 添付のPID付与の条件を満たしている場合  
    　・　[次へ（Next）]ボタン押下で次のアクションに進める

  - 添付のPID付与の条件を満たしていない場合  
    　・　「Item Registration」画面に遷移する  
    　・　画面上に「PID付与の条件を満たしていません。」とエラーメッセージを表示する  
    　・　制約条件と不適合なアイテムの項目の枠を、太い赤枠に変更する  
    　・　「Identifier Grant」アクションのステータスは「やり直し」となる

- DOIの付与、削除等に関わらず、すべてのパターンでバリデーションチェックを実施する

- JPCOARスキーマ ver.2.0において追加された資源タイプについて、以下の表に従いチェックを行う。バリデーション対象は設定ファイル（weko_workflow/config.py）のDOI_VALIDATION_INFO、DOI_VALIDATION_INFO_CROSSREF、DOI_VALIDATION_INFO_DATACITEで指定する。

- 「NDL JaLC DOI」を選択している場合、資源タイプ(dc:type)は「doctoral thesis」のみ許可される。それ以外を指定している場合、「Item Registration」画面に遷移し、「NDL JaLCに割り当てる場合、資源タイプは「doctoral thesis」である必要があります。」とエラーメッセージを表示する

| **資源タイプ（dc:type）** | **コンテンツ種別** |
| ------------------------- | ------------------ |
| other, conference paper, data paper, departmental bulletin paper,editorial, journal article,periodical, review article,article,newspaper,software paper | journalarticle_type |
| thesis, bachelor thesis, master thesis,doctoral thesis | thesis_types |
| technical report, research report, report,book, book part | report_types |
| learning object, learning material | elearning_type |
| software, dataset, aggregated data,clinical trial data, compiled data, encoded data, experimental data, genomic data,geospatial data, laboratory notebook, measurement and test data,observational data, recorded data, simulation data,survey data, source code | dataset_type |
| internal report, policy report, report part,working paper, interactive resource,musical notation, research proposal,technical documentation, workflow,other, sound, patent,cartographic material, map, lecture, image,still image, moving image, video,conference object, conference proceedings,conference poster,manuscript, data management plan, interview | datageneral_types |

2.4. DOIを付与

- DOI発行機関の選択肢から「Not Grant」を選択すると、付与を実施しない

- 取り下げたアイテムはDOIを付与できない

  - DOIを一度取り下げたアイテムでは、  
    [Identifier Grant]アクション画面において DOIを付与できない旨のメッセージを表示し、当該アクションの実行はできない

  - メッセージ：「DOIを取り下げたアイテムにはDOIを付与できません」

- 付与条件を満たしている場合、DOIを一度だけ付与する

- コンフィグファイルでの設定値通りに、識別子付与画面にDOI発行のサフィックス表示を調整可能

  - 詳細は処理概要の「2. サーバー設定」を参照

- サフィックス表示ごとにDOIを付与

  - ①自動連番の方法でのサフィックス（IDENTIFIER_GRANT_SUFFIX_METHOD：0）  
    ・ 「Identifier Grant」画面に、設定されるプレフィックスおよびサフィックスを表示し、エンドユーザ側の設定は無し  
    ・ サフィックス値：RecordIDを設定する  
    　そのとき、サフィックスの桁数は10桁とし、RecordIDが10桁未満の場合は0埋めして設定する

  - ②半自動入力でのサフィックス（IDENTIFIER_GRANT_SUFFIX_METHOD：1）  
    ・ 「Identifier Grant」画面に設定されるプレフィックスおよびサフィックスの前半部分を表示し、サフィックスの後半部分を入力可能  
    　　入力されたサフィックスの書式は以下の条件を満たすかどうかチェックする  
    　　-【条件】　　　　+ 「info:doi/[DOIのPrefix]/[入力値]」が255文字以内である  
    　　　　+ 他のアイテムで既に使用されているDOIではない  
    　　　　+ 取り下げられたDOIではない  
    　　　　+ DOIが入力されている(未入力ではない)  
    　　- 条件を満たしている場合、次のアクションに進める  
    　　- 条件を満たしていない場合、画面上にエラーメッセージを表示し、次のアクションには進めない  
    　　　　+ 未入力の場合：「DOIが入力されていません。」  
    　　　　+ エラーメッセージの内容は、該当条件のエラー内容を以下のように表示する　　　　　 (1)入力値が255文字を超えています  
    　　　　　 (2)他のアイテムで既に使用されているDOIのため、他のDOIを入力してください  
    　　　　　 (3)このDOIは取り下げられたため、他のDOIを入力してください  
    　　　　　 (4)DOIが入力されていません

  - ③自由入力でのサフィックス（IDENTIFIER_GRANT_SUFFIX_METHOD：2）  
    ・ 「Identifier Grant」画面に設定されるプレフィックスを表示し、サフィックスを入力可能  
    ・ 入力されたサフィックスの書式チェックと処理は「半自動入力でのサフィックス」のような同じになる

  - NDL JaLC DOIの選択肢はIDENTIFIER_GRANT_SUFFIX_METHODの値にかかわらず③自動入力のサフィックスとなる

- インデックス状態が「公開」かつハーベスト公開が「公開」であるインデックスとリンクしていない場合は登録・更新を認めない  
  　日本語：アイテムにDOIを付与する場合、インデックス状態が「公開」かつハーベスト公開が「公開」のインデックスとの関連付けが必要です。  
  　英語：When assigning a DOI to an item, it must be associated with an index whose index status is "Public" and Harvest Publishing is "Public".

- 必須のマッピング項目がひとつのアイテムタイプ内に複数ある場合、複数あるうちのひとつに入力されていれば、DOI付与の条件を満たすものとする

- DOI付与済みアイテムを新規登録後、編集時に必須項目の値の削除や必須項目のプロパティの削除はできない。  
  削除をした場合、［Identifier Grant］画面から［Item Registration］画面に遷移し、「PID付与の条件を満たしていません。」とエラーメッセージが表示される。

- 編集時の資源タイプ（dc:type）の変更は、同じコンテンツ種類内でのみ許可される。それ以外の資源タイプにを変更した場合、インポートタブのチェック処理で「DOI付与済みアイテムの資源タイプの変更はできません。」とエラーメッセージが表示される。

2.5. 付与済みDOI及びCNRIハンドルを表示

　 アイテム詳細画面の パーマリンクエリアにDOIのURLを表示する

2.6. アイテムに付与したDOIを取り下げ

- アイテム登録者は、アイテムに付与されたDOIを取り下げることができる  
  　　 (1) DOIが付与されたアイテムでは、 [Identifier Grant]アクション画面において [DOIの取り下げ（Withdraw DOI）]ボタン が表示される  
  　　　[DOIの取り下げ（Withdraw DOI）]ボタンを押さずに次アクションに進むことはできる

- 　　(2) DOIを取り下げる場合は、[DOIの取り下げ（Withdraw DOI）]ボタンを押す  
  　　(3) [DOIの取り下げ（Withdraw DOI）]ボタンを押すと、確認メッセージとパスワード入力画面がモーダル表示される  
  　　　・ 取り下げをキャンセルする場合は、[Cancel]ボタンを押す  
  　　　・ 取り下げを続行する場合は、パスワード「DELETE」を入力のうえ[継続（Continue）]ボタンを押す  
  　　(4) 入力パスワードが正しい場合は、モーダル表示を閉じ、DOIを取り下げる．パスワードは大文字で「DELETE」  
  　　　・ DOIが取り下げられた旨のメッセージを表示する  
  　　　・ アイテムメタデータ項目のうち[jpcoar:identifierRegistration]（ID登録）にマッピングされるデータを空白にする  
  　　　・入力パスワードが正しくない場合は、メッセージ「Invalid password」を表示する。

- また、DOIを取り下げたアイテムに対して、以下の対応もおこなう

  - パーマリンク表示は、もとのアイテム詳細URLに戻す

2.7. DOI及びハンドルのPIDステータスを管理

- 【Administration > レコード管理（Records） > 永続識別子（Persistent Identifier）画面】にてPIDステータスを確認可能  
  　「PID Type」：doi/hdl  
  　「status」：REGISTERED/DELETED

- DOI及びハンドルのPIDステータスは以下のテーブルに管理している。（－：ステータス管理しない）

| **PIDステータス** | **説明** | **DOI** | **ハンドル** | **対応箇所** |
| ------------ | -------------------------------------------------------------- | ------- | -------- | -------- |
| 登録済み | DOIが登録された状態。 | ○ | ○ | ○ |
| 取り下げ済み | DOIが取り下げられた状態。DOI発行機関のAPIでコールが返ってくることを確認後「DOI取り下げ済み」のステータスとする。 | ○ | － | ○ |

2.8. CNRIハンドルを付与

- アイテムの新規登録時にクライアントからハンドルアクセスが要求され、  
  設定情報に基づき、クライアントのハンドルアクセスはリダイレクトされる

- 「4.1. 前提条件」を満たしていると、アイテムの新規登録時にハンドルは必ずおこなわれる

- アイテムに対してDOIを1つのみ付与できる制御について、CNRIを対象から外す

#### 関連モジュール

- 「weko_workflow」識別子付与全般を管理する
- 「weko_handle」：register_handleメソッドでCNRIハンドルを付与する

#### 処理概要

1. 使用しているライブラリ

なし

2. サーバー設定

WEB環境にてCNRIローカルハンドルサーバ認証情報を設定

- weko_handle.config.WEKO_HANDLE_CREDS_JSON_PATH に指定したディレクトリを作成  
  デフォルト： /code/modules/resources  
  ※「modules/weko-handle/weko_handle/config.py」でのコンフィグをベースとする

```
mkdir modules/resources
```

- 「cnri-handle」フォルダーから、「handle_creds.json」を以下のコマンドでコピー

```
cp ../cnri-handle/creds.json modules/resources/handle_creds.json
```

- プライベートキーをコピー

```
cp ../cnri-handle/privatekey.pem modules/resources/
cp ../cnri-handle/certificate_only.pem modules/resources/
cp ../cnri-handle/privatekey.pem .
cp ../cnri-handle/certificate_only.pem .
```

- ビルドを実施

```
docker-compose exec web invenio collect -v && docker-compose exec web invenio assets build && docker-compose restart web
```

- ハンドル登録が失敗になる場合、ハンドルサーバーのキャッシュを削除する必要である。  
  エラーのサンプル：

```
[2020-05-27 07:34:14,129] ERROR in api: Handle 20.500.12465/0000000003 already exists: Could not register handle.
```

CNRIハンドルのURLをコンフィグファイルに設定

- コンフィグキー：WEKO_SERVER_CNRI_HOST_LINK
- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py#L114>

サフィックスの設定方法をコンフィグファイルに設定

- コンフィグキー：IDENTIFIER_GRANT_SUFFIX_METHOD
- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py#L56>
- 設定値：0、1、2  
  　　0：自動連番  
  　　1：半自動入力  
  　　2：自由入力

各DOI発行機関のルートURLをコンフィグファイルに設定

- コンフィグキー：IDENTIFIER_GRANT_LIST
- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/config.py#L48>

invenio.cfg のコンフィグに設定しているものでオーバーライドできるように、current_app.configを以下のように設定する

current_app.config['IDENTIFIER_GRANT_SUFFIX_METHOD']

※invenio.cfg に設定されないときのために、デフォルト値が設定されるよう weko_workflow/config.py の「IDENTIFIER_GRANT_SUFFIX_METHOD」は残す

modules/weko-handle/weko_handle/config.py について

```
12 WEKO_HANDLE_BASE_TEMPLATE= 'weko_handle/base.html'
13 """Default base template for the demo page."""
14
15 WEKO_HANDLE_CREDS_JSON_PATH = '/code/modules/resources/handle_creds.json'
16 """Default dir contain Handle Cred Json."""
17
18 WEKO_HANDLE_ALLOW_REGISTER_CNRI = False
19 """Allow registering CNRI."""
```

- 各パラメタについて、weko_hanl.config.WEKO_HANDLE_CREDS_JSON_PATH をinvenio.cfg で指定した値で上書きし、利用できるように対応する

3. 実装方法

「Item Registration」アクションから次のアクションに移動する時、アイテムにCNRI項目がなく、コンフィグでWEKO_HANDLE_ALLOW_REGISTER_CNRI = Trueである場合に、以下の処理を実施している。

CNRIハンドルをregister_handleメソッドで付与する

- LHS（Local Handle Server）にハンドルの登録を要求する  
  ・ 登録が成功すると、LHSからハンドルアクセスのサフィックスが返却される。そうしたら、IdentifierHandle.register_pidstoreメソッドでハンドル情報をデータベースでの「pidstore_pid」テーブルに保存する  
  ・ LHSからエラーを返却する場合、エラー内容をログファイルに出力する

「pidstore_pid」テーブルの情報

| **カラム名** | **DOI** | **HDL** | **備考** |
| ------------ | ------- | ------- | -------- |
| id | 自動採番 | 自動採番 | - |
| pid_type | doi | hdl | - |
| pid_value | DOIのURL | HDLのURL | - |
| pid_provider | - | - | - |
| status | R/D | R | R: Registered<br>D: Deleted |
|  |  |  |  |
| object_type | rec | rec | - |
| object_uuid | 該当レコードのuuid値 | 該当レコードのuuid値 | 「records_metadata.id」から取得 |
| created | 作成日付 | 作成日付 | - |
| updated | 更新日付 | 更新日付 | - |

「Identifier Grant」アクションの開始時に、doi_identifierテーブルから識別子情報を取得する。

リクエストからコミュニティIDを取得して、doi_identifierテーブルのrepositoryと一致するものを取得する

- リクエストにコミュニティIDが含まれない場合は、repositoryが「Root Index」であるものを取得する

【補足】

ワークフローのアクションで、「Identifier Grant」→「Item Registration」の順序だった場合、DOIは付与されない  
※「Identifier Grant」アクションには、「Not Grant」のみが表示される

[DOIの取り下げ（Withdraw DOI）]押下後、withdraw_confirmメソッドでパスワードを参照する。

- 入力パスワードが正しい場合、アクティビティのworkflow_action_identifierを更新する。

「いずれか必須」のバリデーションチェックは以下の通り

1. Identifier Grant画面にDOI付与し、「Next」ボタンを押下すると、next_actionメソッド中でcheck_doi_validation_not_pass メソッドを呼び出してDOIバリデーションチェックを行う

2. PID付与の制約条件表 (JPCOAR_JaLC_Guideline_appendix_v1.pdf ) を元に、資源タイプと、「いずれか必須」を指定しているDOIタイプの2つ条件をベースにチェックを行う

   - 例：

   資源タイプが「software」あるいは「dataset」、かつDOIタイプ：JaLCの場合、「いずれか必須」の項目は「位置情報」の以下の３つ項目となっている  
   位置情報（点）、位置情報（空間）, 位置情報（自由記述）

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/utils.py#L338>

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/utils.py#L382>

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/utils.py#L653-L684>

3. 「いずれか必須」の項目を入力されたかをチェックするために、validattion_item_property_either_required関数を呼び出す

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/utils.py#L641>

   - 「いずれか必須」の項目のいずれかを入力された場合、エラーなしとして結果を返却する
   - 「いずれか必須」の項目のいずれかも入力されない場合、エラーとして、エラーとなっている項目名の一覧を返却する

4. アイテム登録画面に遷移する

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-workflow/weko_workflow/views.py#L1541-L1550>

5. アイテム登録画面にて、check_validation_error_msgのAPIを呼び出し、返却された項目名一覧を取得し、赤文字で画面に表示する

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/static/js/weko_items_ui/app.js#L2261-L2281>

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/views.py#L359-L363>

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/utils.py#L691-L697>

6. アイテム登録画面にて「いずれか必須」の項目を入力されたかチェックする

   <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-items-ui/weko_items_ui/static/js/weko_items_ui/app.js#L3904>

   入力された場合、次の画面に遷移する

## 実装補足（v2.0.2 実装との突き合わせ）

- Identifier Grant は action_id **7**（endpoint `identifier_grant`、`views.next_action`）。DOI検証 `weko_workflow.utils.check_doi_validation_not_pass` 等、実DOI付与は `saving_doi_pidstore`（Approval時）、CNRIは `register_hdl`→`weko_handle.api.Handle.register_handle`。config `IDENTIFIER_GRANT_LIST` / `IDENTIFIER_GRANT_SUFFIX_METHOD` / `WEKO_SERVER_CNRI_HOST_LINK` / `DOI_VALIDATION_INFO*`。
- 実装補足（追記）：Prefix/Suffix/Enable の設定テーブル `doi_identifier`（model `Identifier`）は **weko-admin** にある（`repository` 列で判定）。`IdentifierHandle` は `weko_workflow.utils`。

#### 更新履歴

| 日付       | GitHubコミットID                         | 更新内容   |
| ---------- | ---------------------------------------- | ---------- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成   |
| 2023/11/11 | V09.27                                   |            |
| 2024/07/1  | 7733de131da9ad59ab591b2df1c70ddefcfcad98 | v1.0.7対応 |
