### ランキング表示

  - > 目的・用途

本機能は、アイテムの閲覧回数やファイルのダウンロード回数やアイテムの作成ユーザーなどのランキングを閲覧を設定する機能である。

  - > 利用方法

【Administration \> Setting (設定) \> Ranking (ランキング表示)からランキングの機能を設定する。

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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

<!-- end list -->

  - リポジトリ管理者として、【Administration \> Setting (設定) \> Ranking(ランキング表示) 画面】にランキングの機能に対して設定を実行する
    
      - 設定項目は以下の通りである

<table>
<thead>
<tr class="header">
<th>#</th>
<th>設定項目</th>
<th>設定方法</th>
<th>デフォルト</th>
<th>概要</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>「ランキングの表示/非表示」（Show/Hide Ranking）</td>
<td>・「オン」（On）</td>
<td>「オフ」（Off）</td>
<td>Web画面でランキングタブの表示可否を設定する</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>・「オフ」（Off）</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>「新着アイテムとして判断する期間」（Period To Judge As New Item）</td>
<td>N日（Day）</td>
<td>14日</td>
<td>新規に登録されたアイテムとして判断する期間。アイテム登録日からの経過日数を指定する。ただし、設定できる範囲は1日～30日とする</td>
</tr>
<tr class="even">
<td>3</td>
<td>「統計期間」（Statistical Period）</td>
<td>N日（Day）</td>
<td>365日</td>
<td>ランキングとして表示する期間。本日から何日前までを集計期間とするかを指定する。ただし、設定できる範囲は1~3650日とする</td>
</tr>
<tr class="odd">
<td>4</td>
<td>「表示する順位」（Display Rank）</td>
<td>N位</td>
<td>10位</td>
<td>ランキングとして表示する順位を指定する.最大値を100位までとする</td>
</tr>
<tr class="even">
<td>5</td>
<td>「ランキング」（Rankings）</td>
<td>・「最も閲覧されたアイテム」（The Most Viewed Items）</td>
<td>チェックボックスの<br />
チェックなし</td>
<td>Web画面で表示するランキングの種類を設定する。チェックボックス方式で、複数選択可能とする。<br />
チェックの付いた項目をWeb画面のランキングタブに表示する。</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>・「最もダウンロードされたアイテム」（Most Downloaded Items）</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>・「最もアイテムを作成したユーザー」（User Who Created The Most Items）</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>・「最も検索されたキーワード」（Most Searched Keywords）</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>・「新着アイテム」（New Items）</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - 「保存」（Save）ボタンを押すと、画面上の設定情報を保存し、メッセージを画面上部に表示する  
    メッセージ：  
    日本語：「設定を変更しました」  
    英語：「Successfully Changed Settings.」

  - 以下のエラー条件に１つでも当てはまる場合、「保存」（Save）ボタンを押すと、エラーメッセージを画面上部に表示する  
    エラー条件：  
    ・「新着アイテムとして判断する期間」で1～30以外の自然数を設定した場合  
    ・「統計期間」で1\~3650以外の自然数を設定した場合  
    ・「表示する順位」で1\~100以外の自然数を設定した場合  
    エラーメッセージ：  
    日本語：「設定変更に失敗しました」  
    英語：「Failurely Changed Settings.」

  - 「新着アイテムとして判断する期間」「統計期間」「表示する順位」で文字列や小数、負の値、０など、上記のエラー条件以外の値を入れた場合、「指定されている形式で入力してください」というポップアップを表示する

  - 「削除」（Delete）ボタンを押すと、入力中の値が破棄され、入力前の保存された設定情報を表示する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_items\_ui

  - > invenio\_stats

  - > weko\_admin

<!-- end list -->

  - > 処理概要

> 【Administration \>Setting (設定) \>Ranking (ランキング表示)】 からランキングの条件を入力し、【保存(Save)】を押下すると、weko\_admin.models.RankingSettings.updateが呼び出される。ranking\_settingテーブルを入力された情報をもとに更新する。
> 
> \[Administration \>Setting (設定) \>Ranking (ランキング表示)\] からランキングの条件を入力したあと【削除(Delete)】を押下すると、weko\_admin.models.RankingSettings.deleteが呼び出され、ranking\_settingテーブルから入力中の値を削除し、入力前の保存された設定情報を取得する。

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
