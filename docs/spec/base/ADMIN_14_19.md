### Shibboleth

  - > 目的・用途

本機能は、システム利用者がログインする際のシボレスユーザーの許可/拒否を設定する機能である。

  - > 利用方法

【Administration \> 設定（Setting） \> Shibboleth画面】にて操作を行う。

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

  - 画面には以下の選択肢を持つラジオボタンがあり、現在の許可/拒否設定を反映して表示される
    
      - 「Shibbolethを有効にする」(Enable Shibboleth Authentication)
        
          - シボレスユーザーを許可とし、「Shibboleth User」ボタンをログイン画面に表示させる設定
    
      - 「Shibbolethを無効にする」（Disable Shibboleth Authentication）
        
          - シボレスユーザーを拒否とし、「Shibboleth User」ボタンをログイン画面に表示させない設定

  - ［保存（Save）］ボタンを押すと、設定内容を保存し、以下のメッセージを画面上部に表示する  
    JP：「Shibboleth設定を更新しました」  
    EN：「Updated Shibboleth settings」

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - weko\_accounts

<!-- end list -->

  - > 処理概要

<!-- end list -->

  - 画面表示時に、weko\_accounts.admin.ShibSettingView.indexメソッドをGETで呼び出して、instance.cfgまたはweko-accountsで以下のコンフィグからShibbolethの許可設定を読み込む。両方で設定されている場合、instance.cfgの設定が優先される。また、画面で設定を変更した場合は、その変更が最優先される。
    
      - パス（instance.cfg）：  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L436>
    
      - パス（config.py）：  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L29>
    
      - 設定キー：WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED

  - ［保存（Save）］ボタンを押すと、weko\_accounts.admin.ShibSettingView.indexメソッドをPOSTで呼び出して、以下のようにしてコンテキストに設定を保存する。

> \_app = LocalProxy(lambda: current\_app.extensions\['weko-admin'\].app)
> 
> ※上記はShibSettingViewクラスの外で定義
> 
> shib\_flg = request.form.get('shibbolethRadios', '0')
> 
> if shib\_flg == '1':
> 
> \_app.config\['WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED'\] = True
> 
> else:
> 
> \_app.config\['WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED'\] = False

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