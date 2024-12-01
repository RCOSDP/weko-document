### 画面背景色

  - > 目的・用途

本機能は、画面背景色表示を設定する機能である

  - > 利用方法

【Administration \> 設定(Setting) \> 画面背景色(Style)画面】を開き、色を選択後「保存」ボタンを押下する。

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
<td>〇</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容

画面背景色表示を設定する

  - > 【Administration \> 設定(Setting) \> 画面背景色(Style)画面】に画面背景色表示を設定する。
    
      - 現在選択している色を表示する。
    
      - 背景１の下にある四角をクリックすると、背景色を設定できる。
    
      - 画面背景色表示の設定は、背景色をカラーピッカーから選択できる。
        
          - また、背景色をカラーモデルで指定できる。  
            対応しているカラーモデル：RGB、HSL、HEX
    
      - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する。  
        メッセージ：「Successfully update color.」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - 
  - > weko\_theme

<!-- end list -->

  - > 処理概要

> 画面背景色表示について

  - > 【Administration \> 設定 \> 画面背景色】画面を開く。この操作によって、weko\_admin.templates.weko\_admin.admin.block\_styleにてweko\_admin.admin.StyleSettingView.indexがGETで呼び出され、変数WEKO\_THEME\_INSTANCE\_DATA\_DIRに保存されているディレクトリの\_variables.scssより現在の色設定を取得し、画面に表示する。

> 画面背景色設定

  - > 背景１下の四角を押下した時、weko\_admin.templates.weko\_admin.admin.block\_style.htmlよりカラーピッカーが表示される。このとき表示される色は現在設定されている色で表示される。

  - > 色を選択し、「保存」ボタンを押下する。この操作によって、weko\_admin.admin.StyleSettingView.indexがPUTで呼び出され、背景１で選択されている色の数値を変数WEKO\_THEME\_INSTANCE\_DATA\_DIRに保存されているディレクトリの\_variables.scssに保存する。

  - > なお、変数WEKO\_THEME\_INSTANCE\_DATA\_DIRはweko\_theme.config.pyに保存されている変数である。

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