
### コンテンツポリシー

  - > 目的・用途

本機能は、サブリポジトリに設定されたコンテンツポリシーの表示を行う機能である

  - > 利用方法

コミュニティのトップページから「コンテンツポリシー(Content Policy)」タブを押すと、【コミュニティ(Content Policy)画面】に移動する

  - > 利用可能なロール

<table>
<thead>
<tr class="header">
<th>ロール</th>
<th>システム<br />
管理者</th>
<th>リポジトリ<br />
管理者</th>
<th>サブリポジトリ<br />
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

  - コミュニティのトップページから「コンテンツポリシー(Content Policy)」タブを押すと、【コミュニティ(Content Policy)画面】に移動する

      - 表示項目は以下の通りである

          - コンテンツポリシーのエリア

            - 【Administration \> コミュニティ管理（Communinites） \> コミュニティ（Community）画面】で当該コミュニティに設定したコンテンツポリシーを表示する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_communities：画面表示を管理するモジュール

  - > weko\_theme：ページレイアウトを管理するモジュール

<!-- end list -->

  - > 処理概要

- 「コンテンツポリシー(Content Policy)」タブを押すと、invenio\_communities.views.ui.content_policy_view関数が呼び出される

  - 画面表示には以下のテンプレートを使用する

    - パス：modules/invenio-communities/invenio_communities/templates/invenio_communities/content_policy.html

  - content_policy_view 関数は、以下のデータを取得してテンプレートに渡す：

    - コンテンツポリシー情報

      - データソース: communities_community

      - 取得条件: 対象コミュニティのサブリポジトリIDをキーに検索する

  - テンプレート中でweko\_themeのwidget.jsを読み込んでおり、そのgetWidgetDesignSetting()関数でwidget\_design\_pageテーブルからページレイアウト情報を取得している

<!-- end list -->

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
<p>YYYY/MM/DD</p>
</blockquote></td>
<td></td>
<td>初版作成</td>
</tr>
</tbody>
</table>