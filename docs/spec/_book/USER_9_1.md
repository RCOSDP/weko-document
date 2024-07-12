
### Cookie使用確認画面表示

  - > 目的・用途

ユーザに対してCookie利用の確認を行う。

  - > 利用方法

画面フッタの「Change consent settings」をクリックすると、Cookie利用の同意画面が表示される。

ユーザはCookie利用の同意画面にて、同意することで、Cookieを利用したサービスを利用できるようになる。

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

  - コンフィグで機能が有効化されているとき、画面フッタに「Change consent settings」が表示される。これをクリックすると、Cookie利用の同意画面がポップアップで表示される。

  - Addthis および Google Analystics の利用について、Cookie利用の同意をとることで利用可能とする。

  - Googleアナリティクス(システム)については、サービス利用の必須としている。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-theme

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - Cookie利用の同意画面は、Klaro ( https://github.com/kiprotect/klaro ) ライブラリを利用して作成している。

  - 本機能の有効化を設定するコンフィグは、instance.cfgまたはweko-themeのconfig.pyで設定する。両方で設定されている場合、instance.cfgの設定が優先される。
    
      - パス（instance.cfg）：  
        https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg
    
      - パス（config.py）：  
        https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko\_theme /config.py

  - > ENABLE\_COOKIE\_CONSENT = True の場合に機能が有効となる。

  - 「Change consent settings」は、コンフィグで機能が有効化されているときのみ表示されるようにテンプレートで制御されている。

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