
### コミュニティ

  - > 目的・用途

本機能は、コミュニティの一覧表示と個別のコミュニティの表示を行う機能である

  - > 利用方法

管理画面でコミュニティを表示する設定にした状態で、トップページの「コミュニティ(Communities)」タブを選択する

※管理画面での設定は、[ADMIN-14-11: 検索設定](#検索設定)を参照

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

  - トップページから「コミュニティ(Communities)」タブを押すと、【コミュニティ(Communities)画面】に移動する
    
      - 表示項目は以下の通りである
        
          - コミュニティ検索のエリア  
            検索条件を入力して、キーボードでの「Enter」を押すと、コミュニティを検索し、検索結果が表示される
            
              - 初期表示では全件取得する
        
          - コミュニティ一覧のエリア
            
              - 【Administration \> コミュニティ管理（Communinites） \> コミュニティ（Community）画面】に作成されたコミュニティ一覧を表示する
            
              - デフォルトとして、コミュニティをランキングの順次で表示する
            
              - 各コミュニティに以下の表示項目を表示する
                
                  - コミュニティのタイトル（そのコミュニティへのリンク）
                
                  - コミュニティの説明
            
              - 「Sort By」プルダウンで、コミュニティの表示順次を選択できる  
                選択肢は「title」、「ranking」とする
            
              - ページングエリア

<!-- end list -->

  - コミュニティを表示する  
    コミュニティ名のリンクを押すと、該当コミュニティのページに移動する
    
      - 【Administration \> ウェブデザイン管理（Web Design） \> ページレイアウト（Page Layout）画面】に選択しているコミュニティのページレイアウトが登録されている場合、その設定通りにコミュニティが表示される
    
      - 選択しているコミュニティのページレイアウトが登録されていない場合、コミュニティは「Main contents」ウィジェットが配置されたページが表示される
    
      - ページレイアウトについては[ADMIN-4-2: ページレイアウト](\\l)を参照

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_communities：画面表示を管理するモジュール

  - > weko\_theme：ページレイアウトを管理するモジュール

<!-- end list -->

  - > 処理概要

> 「コミュニティ(Communities)」タブを押すと、invenio\_communities.views.ui.community\_list関数が呼び出される
> 
> 画面表示には以下のテンプレートを使用する

  - > パス：https://github.com/RCOSDP/weko/blob/v0.9.22/modules/invenio-communities/invenio\_communities/templates/invenio\_communities/communities\_list.html

> 「コミュニティ(Communities)」タブを押すと、invenio\_communities.views.ui.community\_list関数が呼び出される

  - > 検索条件とソート条件に基づいてコミュニティを取得して表示する

> コミュニティのリンクを押すと、invenio\_communities.views.ui.view関数が呼び出される

  - > コミュニティのリンクは「/コミュニティID/?view=weko」となっており、コミュニティIDがview関数の引数となる

  - > 「?view=weko」の情報は使用しない（ソースの該当箇所がコメントアウトされている）

  - > 画面表示には以下のテンプレートを使用する
    
      - > パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-theme/weko_theme/config.py#L76>

  - > テンプレート中でweko\_themeのwidget.jsを読み込んでおり、そのgetWidgetDesignSetting()関数でwidget\_design\_pageテーブルからページレイアウト情報を取得している

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
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
</tbody>
</table>