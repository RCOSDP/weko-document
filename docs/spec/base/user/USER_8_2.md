
### ログイン

  - > 目的・用途

本機能は、サインアップ済みのユーザーがログインするための機能である。

  - > 利用方法

ユーザー画面のヘッダから［ログイン（Log in）］ボタンを押す。

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

  - ユーザー画面のヘッダから［ログイン（Log in）］ボタンを押すと、ログイン画面に移動する
    
      - コンフィグの以下設定値の組み合わせに応じて、該当ログイン画面に移動する  
        （シボレスログイン処理について、[ADMIN-14-19: Shibboleth](\\l) を参照）
        
        1.  WEKO login only:
            
              - WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED = False
        
        2.  WEKO login + Shibbolth(Idp):
            
              - WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED = True
            
              - WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_ENABLED = True
        
        3.  WEKO login + Shibbolth(DS):
            
              - WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED = True
            
              - WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_ENABLED = False
        
        4.  Shibbolth(Idp):
            
              - WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED = True
            
              - WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_ENABLED = True
            
              - WEKO\_ACCOUNTS\_SHIB\_INST\_LOGIN\_DIRECTLY\_ENABLED = True
        
        5.  Shibbolth(DS)
            
              - WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED = True
            
              - WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_ENABLED = False
            
              - WEKO\_ACCOUNTS\_SHIB\_DP\_LOGIN\_DIRECTLY\_ENABLED= True

  - WEKOのログイン画面からログインする
    
      - 表示言語はヘッダにて選択しているシステム言語とする
    
      - メールアドレスとパスワードのテキストボックスを設ける
    
      - ［ログイン（Log In）］ボタン、「サインアップ」（Sign Up）リンク、「パスワードをお忘れの方はこちら」（Forgot password?）リンクを設ける
        
          - ［ログイン（Log In）］ボタンを押すと、入力した情報で、ログインリクエストを送信する
            
              - 問題なければ、もともとのユーザー画面に移動する
            
              - エラーがあった場合、エラー内容を メールアドレスとパスワードのテキストボックスの上部に表示させる
                
                  - メールアドレス、またはパスワードを入力しない場合  
                    エラーメッセージ：「{} not provided」
                
                  - メールアドレス、またはパスワードを正しく入力しない場合  
                    エラーメッセージ：「Specified user does not exist」
        
          - 「サインアップ」（Sign Up）リンクを押すと、アカウント登録画面に移動する
        
          - 「パスワードをお忘れの方はこちら」（Forgot password?）リンクを押すと、リセットパスワード画面に移動する

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio\_accounts

  - > weko-accounts

<!-- end list -->

  - > 処理概要

> ログイン画面の種類を決定するコンフィグは、instance.cfgまたはweko-accountsのconfig.pyで設定する。両方で設定されている場合、instance.cfgの設定が優先される。

  - > パス（instance.cfg）：  
    > https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg

  - > パス（config.py）：  
    > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py>

  - > 対象となるコンフィグは以下の通り。
    
      - WEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLED
    
      - WEKO\_ACCOUNTS\_SHIB\_IDP\_LOGIN\_ENABLED
    
      - WEKO\_ACCOUNTS\_SHIB\_INST\_LOGIN\_DIRECTLY\_ENABLED

> ログインボタンを押すと、invenio-accountsのsessions.pyにあるlogin\_listenerのadd\_user\_sessionメソッドが呼び出される。

  - > ログイン時には、accounts\_user\_session\_activityテーブルとredisにセッション情報を記録して、accounts\_userテーブルの最終ログイン情報を更新する。

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