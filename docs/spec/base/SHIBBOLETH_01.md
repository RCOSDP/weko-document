## Shibboleth対応

1\. Shibboleth IdPからの属性情報に基づき、ユーザへのロール割り当てをする

  - Idpから取得した属性情報は、以下の設定に従ってWEKOに渡される
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/nginx/login.php#L16-L20>
    
      - 「$\_SERVER\\[Idp側での属性名\\]」で渡された情報を「$post\_args\\[WEKO側での属性名\\]」として受け取る

  - 認証時にIdPより取得した属性情報に基づきログインユーザに対してロール割り当てを行う
    
      - IdP属性情報は以下とする
        
          - ロール：wekoSocietyAffiliation
    
      - IdP属性値に対するロール割り当ては以下とする
        
          - 「管理者」→システム管理者ロール'System Administrator'
        
          - 「図書館員」→リポジトリ管理者ロール'Repository Administrator'
        
          - 「教員」→一般利用者ロール'Contributor'
        
          - 「教官」→一般利用者ロール'Contributor'
    
      - 上記のIdP属性値とロールとの対応は、以下のコンフィグで設定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L77-L82>
        
          - 設定キー：WEKO\_ACCOUNTS\_SHIB\_ROLE\_RELATION
    
      - IdP属性値がconfigに含まれないロールであった場合は、ロールを持たないユーザとなる

2\. Shibboleth IdPからの属性情報に基づき、サイトライセンス機能を制御する

  - 認証時にIdPより取得した属性情報に基づきログインユーザに対してサイトライセンス制御を行う
    
      - IdP属性情報は以下とする
        
          - サイトライセンス：wekoSiteUserWithinIpRange
    
      - IdP属性値に対するサイトライセンスは以下とする
        
          - "False"の場合は以下のエラーメッセージを表示し、ログイン不可とする  
            　JP: ログインに失敗しました。  
            　EN: Failed to login.

3\. Shibbolethでのアカウント情報(ロール含む)の利用

  - シボレス経由でログインする都度、シボレス属性値をWEKO3のユーザ情報に反映
    
      - SHIB\_ATTR\_USER\_NAME は、invenio の仕様でユニークである必要がある。
    
      - SHIB\_ATTR\_ROLE\_AUTHORITY\_NAMEについて、ロールの紐づけをconfig で指定できるものとし、configに含まれないロールであった場合は、WEKOのロールとしては設定しない
        
          - SHIB\_ATTR\_ROLE\_AUTHORITY\_NAMEに複数属性が含まれている場合は，複数ロールの割当を行えるようにする。（複数属性が含まれている場合は属性値を半角セミコロン「;」で区切られている）

  - シボレスユーザの紐づけキー
    
      - SHIB\_ATTR\_EPPNとする
    
      - 存在しない場合は、かわりにSHIB\_ATTR\_USER\_NAMEを利用することができる
    
      - SHIB\_ATTR\_USER\_NAMEを利用するかどうかは、以下のconfigで指定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L97>
        
          - 設定キー：WEKO\_ACCOUNTS\_SHIB\_ALLOW\_USERNAME\_INST\_EPPN

4\. 実装

  - weko\_accounts.views. shib\_sp\_login関数によって、IdPからのリクエストを処理する
    
      - リクエストにSHIB\_ATTR\_SESSION\_IDが含まれず、以下のコンフィグWEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLEDがfalseの場合はエラーとしてWEKOのログイン画面に遷移する
        
          - > パス（instance.cfg）：  
            > <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L436>
        
          - パス（config.py）：  
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L29>
    
      - weko\_accounts.utils. parse\_attributes関数によってリクエストの内容を確認し、必須の項目が含まれない場合はエラーとしてWEKOのログイン画面に遷移する
        
          - 必須項目は以下のコンフィグで設定する
            
              - > パス（instance.cfg）：  
                > <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L442-L448>
            
              - パス（config.py）：  
                <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L64-L74>
            
              - 設定キー：WEKO\_ACCOUNTS\_SSO\_ATTRIBUTE\_MAP
    
      - リクエストの内容にSHIB\_ATTR\_EPPNが含まれず、かわりにSHIB\_ATTR\_USER\_NAMEを利用しない設定である場合はエラーとしてWEKOのログイン画面に遷移する
    
      - セッション情報はRedisに保存する
        
          - キーは、以下のコンフィグの値にログイン画面での入力値SHIB\_ATTR\_SESSION\_IDを加えたものを用いる
            
              - パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-accounts/weko_accounts/config.py#L32>
            
              - 設定キー：WEKO\_ACCOUNTS\_SHIB\_CACHE\_PREFIX
    
      - リクエストの内容をもとに、shibboleth\_userテーブルからSHIB\_ATTR\_EPPNまたはSHIB\_ATTR\_USER\_NAMEを使用してレコードの存在を確認する

  - 上記の処理で、shibboleth\_userテーブルにレコードが存在する場合は、weko\_accounts.views.shib\_auto\_login関数で続きの処理を行う
    
      - リクエストのSHIB\_ATTR\_SESSION\_IDとsession\['shib\_session\_id'\]のどちらかに情報がある場合は、ログインする
        
          - リクエストにSHIB\_ATTR\_SESSION\_IDが含まれず、session\['shib\_session\_id'\]に情報がある場合は、weko\_accounts.api.ShibUser.new\_relation\_infoメソッドによってshibboleth\_userテーブルにレコードを作成する
            
              - あわせて、userprofiles\_userprofileテーブルに以下の内容でレコードを作成する
                
                  - user\_id：shibboleth\_userテーブルに作成するレコードのidフィールドと同じ
                
                  - timezone：コンフィグのデフォルト値
                
                  - language：コンフィグのデフォルト値
                
                  - username：shibboleth\_userテーブルに作成するレコードのshib\_user\_nameフィールドと同じ
        
          - レコード作成の有無にかかわらず、weko\_accounts.api.ShibUser. check\_inメソッドの中で、ロールの割り当てを行う
    
      - 上記以外の場合は、WEKOのログイン画面に遷移する

  - shibboleth\_userテーブルにレコードが存在しなかった場合は、weko\_accounts.views.shib\_login関数でID選択画面に遷移する
    
      - 登録済みのIDでログインする場合は、weko\_accounts.views.confirm\_user関数で続きの処理を行う
        
          - リクエストに、有効なWEKOアカウントとパスワードが含まれない場合は、WEKOのログイン画面に遷移する
        
          - リクエストのWEKOアカウントのメールアドレスを使用して、shibboleth\_userテーブルにレコードを作成する
        
          - weko\_accounts.api.ShibUser. check\_inメソッドの中で、ロールの割り当てを行う
        
          - ログインする
    
      - 新規IDでログインする場合は、weko\_accounts.views.shib\_auto\_login関数でログインする

  - shibboleth\_userテーブルにレコードを作成する場合は、あわせてユーザ関連テーブルも上書きする
    
      - 1\) シボレス属性値をshibboleth\_userテーブルに登録する
        
          - SHIB\_ATTR\_MAIL ⇒ shibboleth\_user.shib\_mail
        
          - SHIB\_ATTR\_USER\_NAME ⇒ shibboleth\_user.shib\_user\_name
        
          - SHIB\_ATTR\_ROLE\_AUTHORITY\_NAME ⇒shibboleth\_user.shib\_role\_authority\_name
    
      - 2\) shibboleth\_userテーブルから各テーブルに登録する
        
          - shibboleth\_user.shib\_mail ⇒ accounts\_user.email
        
          - shibboleth\_user.shib\_user\_name ⇒ userprofiles\_userprofile.username
        
          - shibboleth\_user.shib\_role\_authority\_name ⇒ accounts\_userrole.user\_id,role\_id
    
      - 1),2) どちらの登録の際も値のチェックは行わず、登録先の値を上書きする。

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