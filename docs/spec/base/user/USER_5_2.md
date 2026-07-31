# コンテンツポリシー

## 目的・用途

本機能は、コミュニティに設定されたコンテンツポリシーの表示を行う機能である

## 利用方法

コミュニティのトップページから「コンテンツポリシー(Content Policy)」タブを押すと、【コミュニティ(Content Policy)画面】に移動する

## 利用可能なロール

| ロール   | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| :------: | :------------: | :--------------: | :------------------: | :----------: | :----------: | :----------------: |
| 利用可否 |       ○       |        ○        |          ○          |      ○      |      ○      |         ○         |

## 機能内容

- コミュニティのトップページから「コンテンツポリシー(Content Policy)」タブを押すと、【コミュニティ(Content Policy)画面】に移動する

  - 表示項目は以下の通りである

    - コンテンツポリシーのエリア

      - 【Administration > コミュニティ管理（Communinites） > コミュニティ（Community）画面】で当該コミュニティに設定したコンテンツポリシーを表示する

## 関連モジュール

- invenio_communities：画面表示を管理するモジュール

- weko_theme：ページレイアウトを管理するモジュール

## 処理概要

- 「コンテンツポリシー(Content Policy)」タブを押すと、invenio_communities.views.ui.content_policy関数が呼び出される

  - 画面表示には以下のテンプレートを使用する

    - パス：modules/invenio-communities/invenio_communities/templates/invenio_communities/content_policy.html

  - content_policy 関数は、以下のデータを取得してテンプレートに渡す：

    - コンテンツポリシー情報

      - テーブル: communities_community

      - 取得条件: URLで指定されたコミュニティのidをキーに検索する

  - テンプレート中でweko_themeのwidget.jsを読み込んでおり、そのgetWidgetDesignSetting()関数でwidget_design_pageテーブルからページレイアウト情報を取得している

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`invenio_communities.views.ui.content_policy`（route `/c/<community_id>/content_policy/`、`@pass_community`）。model `Community`（table `communities_community`、列 `content_policy`）。

## 更新履歴

| 日付       | GitHubコミットID | 更新内容 |
| :--------: | :--------------: | :------: |
| 2025/01/23 | -                | 初版作成 |
