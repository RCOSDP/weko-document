### ワークフロー管理（制限公開）

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

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2025/10/31 | 160a811eed2c61492558905db34fa0619da6b18f | 設定値による表示制御を記載 |
| 2024/01/19 |  |  |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
