### ワークフロー管理（制限公開）

> 補足（実装）：フロー名や段数（アクションの構成）はコードで固定されておらず、`FlowDefine` / `FlowAction` として管理者がDBに登録するデータである。以下の構成は「動作が保証されている運用上の推奨構成」であり、コードによる強制ではない。選択可能なアクションは `WEKO_WORKFLOW_ACTIONS`（Start / End / Item Registration / Approval / Item Link / Identifier Grant）で、各アクション名は `WEKO_WORKFLOW_ACTION_*`（`weko-workflow/config.py`）で定義される。承認(Approval)の段数は `FlowAction.action_order` で管理される（二段階＝Approval が2レコード）。

- フロー:　Flow List
  - 【Admin > WorkFlow > Flow List画面】から利用申請フローを登録することができる
    - 現在利用申請フローとして動作が保証されているのは以下の2つである。
      - 利用申請： 　[Start]-[Item Registration]-[Approval(1)]-[End]
      - 二段階利用申請：　[Start]-[Item Registration]-[Approval(1)]-[Approval(2)]-[End]
      - 利用登録： 　[Start]-[Item Registration]-[End]
      - 利用規約のみ： 　[Start] -[End]
    - 利用登録は、Approvalを承認扱いでスキップする利用申請。利用規約のみは、申請なしでそのまま制限公開のコンテンツファイルをダウンロードできる。
    - 利用報告フローは以下の通り定義している。
      - 利用報告： 　[Start]-[Item Registration]-[Approval(1)]-[End]
  - 「Action Role」カラムに、アクションを実行するロールを限定できる
    - 「Action Role」プルダウンを選択する。「Action Role」プルダウンでの選択肢は現在システムに設定されたロールである
    - 「Deny」チェックボックスにチェックを入れる場合、選択されているロールが実施不可とする
  - 「Action User」カラムに、アクションを実行するユーザーを限定できる
    - 「Action User」プルダウンから選択する。「Action User」プルダウンの選択肢は以下である。
      - システム管理者、リポジトリ管理者は、システムに登録されたすべてのユーザが表示される。
      - サブリポジトリ管理者は、自身が管理するサブリポジトリに関連するユーザのみが表示される。
      - 「Item Registration」アクションに対して
        - 「Action User」プルダウンの値下にある、「登録者にメールを送信する」チェックボックスと「利用申請時に、アイテム登録者に対しメールを送信する」チェックボックスで利用申請時に送信するメールの送信可否を設定する。
          - admin_settings テーブルの name が restricted_access のレコードの settings.edit_mail_templates_enable が true の場合のみ有効
          - 「登録者にメールを送信する」チェックボックス：利用申請時に、申請者に対して送信するメールを設定する。
          - 「利用申請時に、アイテム登録者に対しメールを送信する」チェックボックス：利用登録/利用申請時に、申請先アイテムの登録者に対して送信するメールを設定する。
      - 「Approval」アクションに対して
        - 選択肢は上記のユーザーと、「アイテム登録者」、「プロパティを指定」(Specify Property)である
          - 「アイテム登録者」および「プロパティを指定」は　admin_settings テーブルの name が restricted_access のレコードの settings.edit_mail_templates_enable が true の場合のみ有効
          - 「アイテム登録者」を設定した場合には、workflow_flow_action_role テーブルの action_item_registrant に true を設定する。
          - action_item_registrant が true の場合には該当フローを用いたワークフローで approval 時にアイテム登録者が承認者として action_user に設定される。
          - 「アイテム登録者」を選択した場合には、「承認依頼通知メール」は発行されない。
          - 「プロパティを指定」(Specify Property)を選択した場合、「プロパティを指定する」(Specify Property)モーダル画面を表示する。当該画面でプロパティを選択する。
          - モーダル画面には、プロパティ定義に「"approval":true」キーワードを持つプロパティ名を表示する。
          - モーダルに表示しているプロパティを選択して「設定」(Setting)ボタンを押すことで、プロパティを指定できる。
          - 「閉じる」（Close）ボタンを押すと、モーダルを閉じる。
        - 「Approval」アクションごとに通知メールを設定できるモーダル画面を表示する「通知メール設定」ボタンを表示する。
          - admin_settings テーブルの name が restricted_access のレコードの settings.edit_mail_templates_enable が true の場合のみ有効
          - モーダル画面に表示されたチェックボックスにチェックを入れ、プルダウンからメールテンプレートを設定することで、管理者画面で登録したメールを自動送信することができる。
            - 「承認依頼通知メール」（Approval Request Notification Email）  
              承認者に承認を依頼するメールを送信する。
            - 「承認却下通知メール」（Approval Rejection Notification Email）  
              登録者に承認者が却下された旨を通知するメールを送信する。
            - 「承認通知メール」（Approval Notification Email）  
              登録者に承認者が承認された旨を通知するメールを送信する。
    - 「Deny」チェックボックスにチェックを入れる場合、選択されているユーザーが実施不可とする
  - 「Change Order」カラムにアクションの順序を設定できる  
    一番上の項目は、［↑］ボタンが無効になる。一番下の項目は、［↓］ボタンが無効になる
  - 画面の下部に表示されている［保存］を押すと、フローを保存し、メッセージを一覧画面の上部に表示する  
    メッセージ：「Updated flow action successfully」

- ワークフロー:　WorkFlow List
  - 【Admin > WorkFlow > WorkFlow List画面】に登録されたワークフローが一覧に表示される
    - 制限公開機能を利用するためには、「利用報告/Data Usage Report」という名前のワークフローを用意しておく必要がある
      - 「利用報告/Data Usage Report」の推奨設定は以下のとおり  
        ワークフロー: 利用報告/Data Usage Report  
        フロー：利用報告  
        アイテムタイプ：利用報告  
        制限公開フラグ：チェックしない  
        GakuNinRDM Flag：チェックしない  
        登録インデックスの指定：利用報告（インデックスにて登録）  
        表示/非表示：利用者が自分でワークフローを作成させないために、「提供方法：ロール」にて設定したロールは非表示とするのが望ましい。
    - 利用申請用のワークフローの推奨設定は以下のとおり
      - 利用申請  
        ワークフロー: 利用申請  
        フロー：利用報申請  
        アイテムタイプ：利用申請  
        制限公開フラグ：チェックする  
        GakuNinRDM Flag：チェックしない  
        登録インデックスの指定：利用申請（インデックスにて登録）
      - 表示/非表示  
        　表示：System Administrator, Repository Administrator  
        　非表示：Contributor,Community Administrator
      - 二段階利用申請  
        ワークフロー: 二段階利用申請  
        フロー：二段階利用申請  
        アイテムタイプ：二段階利用申請  
        制限公開フラグ：チェックする  
        GakuNinRDM Flag：チェックしない  
        登録インデックスの指定：利用申請（インデックスにて登録）
      - 表示/非表示  
        　表示：System Administrator, Repository Administrator  
        　非表示：Contributor,Community Administrator
      - 利用登録  
        ワークフロー: 利用登録  
        フロー：利用登録  
        アイテムタイプ：利用申請  
        制限公開フラグ：チェックする  
        GakuNinRDM Flag：チェックしない  
        登録インデックスの指定：利用申請（インデックスにて登録）
      - 表示/非表示  
        　表示：System Administrator, Repository Administrator  
        　非表示：Contributor,Community Administrator
      - 利用規約のみ  
        ワークフロー: 利用規約のみ  
        フロー：利用規約のみ  
        アイテムタイプ：利用申請  
        制限公開フラグ：チェックする  
        GakuNinRDM Flag：チェックしない  
        登録インデックスの指定：利用申請（インデックスにて登録）  
        表示/非表示  
        　表示：System Administrator, Repository Administrator  
        　非表示：Contributor,Community Administrator

#### 関連モジュール

- weko-workflow（フロー／ワークフロー管理、承認処理、通知メール送信）
- weko-admin（AdminSettings `restricted_access`、`edit_mail_templates_enable` による表示制御）

#### データモデル / テーブルスキーマ

- `workflow_flow_define`（`FlowDefine`）：`flow_id`(UUID) / `flow_name`(unique) / `flow_status` / `flow_type` / `repository_id` / `is_deleted`
- `workflow_flow_action`（`FlowAction`）：`flow_id` / `action_id` / `action_order` / `action_status` / `send_mail_setting`(JSON)
- `workflow_flow_action_role`（`FlowActionRole`）：`action_role`(FK Role) / `action_role_exclude`（＝Deny） / `action_user`(FK User) / `action_user_exclude`（＝Deny） / `specify_property` / `action_item_registrant`(Boolean, default False) / `action_request_mail`(Boolean)
- `workflow_workflow`（`WorkFlow`）：`flows_name` / `itemtype_id` / `flow_id` / `index_tree_id` / `open_restricted`（制限公開フラグ, Boolean, **default True**） / `is_gakuninrdm` / `location_id` / `repository_id`
- `workflow_userrole`（`WorkflowRole`）：ワークフローの表示／非表示ロール設定の実体

#### 処理概要

- フロー（アクション）保存：`FlowSettingView.upt_flow_action`（`POST /action/<flow_id>`）→ `Flow.upt_flow_action`（`FlowActionRole` を全削除後、`action_user` の値により role／アイテム登録者(`-2`)／Request mail(`-3`)／プロパティ指定(`-1`) に振り分けて再作成）→ 成功時「Updated flow action successfully」
- フロー本体保存：`update_flow`（`POST /<flow_id>`）→ 成功時「Updated flow successfully.」（アクション保存とはメッセージが異なる）
- 承認者の解決：`WorkActivity.get_activity_action_role` が `action_item_registrant` / `action_request_mail` を owner／リクエスト宛先へ展開
- 通知メール送信：承認遷移時に `process_send_approval_mails` を呼び出す（`edit_mail_templates_enable` が True のときのみ有効）
- 「Specify Property」候補：プロパティ定義に `"approval":true` を持つプロパティ名を `get_specified_properties`（`recursive_get_specified_properties`）で収集してモーダルに表示

#### 通知メールと send_mail_setting の対応

`FlowAction.send_mail_setting`（JSON）に `previous` / `next` として構成され、各キーは `{send: bool, mail: テンプレートキー}` を持つ。UIの3種は以下に対応する。

| UI表示 | 内部キー | 送信内容 |
| --- | --- | --- |
| 承認依頼通知メール（Approval Request Notification Email） | `request_approval` / `request_approval_for_guest` | 承認者へ承認を依頼 |
| 承認却下通知メール（Approval Rejection Notification Email） | `inform_reject` / `inform_reject_for_guest` | 登録者へ却下を通知 |
| 承認通知メール（Approval Notification Email） | `inform_approval` / `inform_approval_for_guest` | 登録者へ承認を通知 |

#### 主要設定値（config）

| キー | 値 | 用途 |
| --- | --- | --- |
| `WEKO_WORKFLOW_ITEM_REGISTRANT_ID` | `-2` | 「アイテム登録者」の内部value |
| `WEKO_WORKFLOW_REQUEST_MAIL_ID` | `-3` | 「Request mail」の内部value |
| （Specify property のvalue） | `-1` | 「プロパティを指定」の内部value |
| `WEKO_WORKFLOW_ACTIONS` | Start/End/Item Registration/Approval/Item Link/Identifier Grant | フローで選択可能なアクション |
| AdminSettings `restricted_access.edit_mail_templates_enable` | False | Specify property／アイテム登録者／通知メール設定 の表示・送信制御 |

> 実装上の補足：
> - `WorkFlow.open_restricted` の既定値は True（本文の推奨設定「利用報告＝チェックしない」と混同しないこと）。
> - 「アイテム登録者」選択時に承認依頼通知メールが発行されないのは、仕様上の明示的スキップではなく、`action_user` が未設定（宛先id `-1`）で宛先解決不能となり未送信になるためである。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | 設定値による表示制御を記載 |
| 2024/01/19 |  |  |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2026/07/13 |  | 実装(v2.0.2)と突き合わせ、関連モジュール・データモデル・処理概要・通知メールと`send_mail_setting`の対応・configキーを追記。フロー構成がDB管理の推奨構成である旨、`open_restricted`既定値、承認依頼メール未送信の機序を注記 |
