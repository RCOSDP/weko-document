
### コンテンツポリシー

  - > 目的・用途

本機能は、コミュニティに設定されたコンテンツポリシーの表示を行う機能である

  - > 利用方法

コミュニティのトップページから「コンテンツポリシー(Content Policy)」タブを押すと、【コミュニティ(Content Policy)画面】に移動する

  - > 利用可能なロール

|ロール|システム<br>管理者|リポジトリ<br>管理者|サブリポジトリ<br>管理者|登録ユーザー|一般ユーザー|ゲスト<br>(未ログイン)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|利用可否|○|○|○|○|○|○|

  - > 機能内容

<!-- end list -->

  - コミュニティのトップページから「コンテンツポリシー(Content Policy)」タブを押すと、【コミュニティ(Content Policy)画面】に移動する

      - 表示項目は以下の通りである

          - コンテンツポリシーのエリア

            - 【Administration \> コミュニティ管理（Communinites） \> コミュニティ（Community）画面】で当該コミュニティに設定したコンテンツポリシーを表示する

<!-- end list -->

  - > 関連モジュール

    - invenio\_communities：画面表示を管理するモジュール

    - weko\_theme：ページレイアウトを管理するモジュール

<!-- end list -->

  - > 処理概要

- 「コンテンツポリシー(Content Policy)」タブを押すと、invenio\_communities.views.ui.content_policy_view関数が呼び出される

  - 画面表示には以下のテンプレートを使用する

    - パス：modules/invenio-communities/invenio_communities/templates/invenio_communities/content_policy.html

  - content_policy_view 関数は、以下のデータを取得してテンプレートに渡す：

    - コンテンツポリシー情報

      - テーブル: communities_community

      - 取得条件: URLで指定されたコミュニティのidをキーに検索する

  - テンプレート中でweko\_themeのwidget.jsを読み込んでおり、そのgetWidgetDesignSetting()関数でwidget\_design\_pageテーブルからページレイアウト情報を取得している

<!-- end list -->

- > 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|> 2025/01/23|-|初版作成|
