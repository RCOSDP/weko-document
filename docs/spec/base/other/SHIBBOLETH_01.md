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
        
          - 「学認 IdP 経由」→ 一般利用者ロール'Contributor' 
        
          - 「機関内の Orthros 経由」→ リポジトリ管理者ロール'Repository Administrator'
        
          - 「機関外の Orthros 経由」→ コミュニティ管理者ロール'Community Administrator'
          
          - 「その他」→ ロール無'None'
    
      - 上記のIdP属性値とロールとの対応は、以下のコンフィグで設定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L77-L82>
        
          - 設定キー：WEKO\_ACCOUNTS\_SHIB\_ROLE\_RELATION
    
      - IdP属性値がconfigに含まれないロールであった場合は、ロールを持たないユーザとなる

          - 設定値によって既定のロールが設定されている場合は、設定値を用いて既定のロールを付与する。

      - isMemberOfの属性値が付与されている場合、学認mAPグループからロールを割り当てる。

          - 以下のフォーマットに従う学認mAPグループを持つ場合、それぞれ以下のロールに割り当てる。

            - 「jc\_roles\_sysadm」→ システム管理者ロール'System Administrator'

            - 「jc\_\<entityid\>\_roles\_repoadm」→ リポジトリ管理者ロール'Repository Administrator'

            - 「jc\_\<entityid\>\_roles\_comadm」→ コミュニティ管理者ロール'Community Administrator'

            - 「jc\_\<entityid\>\_roles\_contributor」→ 一般利用者ロール'Contributor'

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
    
      - HTTP\_WEKOID は、invenio の仕様でユニークである必要がある。
    
      - HTTP\_WEKOSOCIETYAFFILIATIONについて、ロールの紐づけをconfig で指定できるものとし、configに含まれないロールであった場合は、WEKOのロールとしては設定しない
        
          - HTTP\_WEKOSOCIETYAFFILIATIONに複数属性が含まれている場合は，複数ロールの割当を行えるようにする。（複数属性が含まれている場合は属性値を半角セミコロン「;」で区切られている）

      - 設定値WEKO\_ACCOUNTS\_SHIB\_BIND\_GAKUNIN\_MAP\_GROUPSが有効（True）の場合、isMemberOfについて、所属している学認mAPグループをWEKO3に紐づける。

         - 学認mAPグループはそのグループエンティティIDを名前に持つロールとして登録される。

         - ログイン時に所属している学認mAPグループをWEKO3のユーザーに付与する。

  - シボレスユーザの紐づけキー
    
      - eppnとする
    
      - 存在しない場合は、かわりにHTTP\_WEKOIDを利用することができる
    
      - HTTP\_WEKOIDを利用するかどうかは、以下のconfigで指定する
        
          - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L97>
        
          - 設定キー：WEKO\_ACCOUNTS\_SHIB\_ALLOW\_USERNAME\_INST\_EPPN

4\. 設定

  -  学認mAPグループ情報をWEKO3と連携するか設定する。(Trueの場合、学認mAPグループとWEKO3を連携する。)

      - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L111>

      - 設定キー：WEKO\_ACCOUNTS\_SHIB\_BIND\_GAKUNIN\_MAP\_GROUPS

      - 現在の設定値：

> WEKO\_ACCOUNTS\_SHIB\_BIND\_GAKUNIN\_MAP\_GROUPS = False

  - GakuNin mAPグループのグループIDのフォーマットおよびWEKO3のロールを紐づけるキーワード

      - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L114>

      - 設定キー：WEKO\_ACCOUNTS\_GAKUNIN\_GROUP\_PATTERN\_DICT

      - 現在の設定値：

>      WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT = {
>          "prefix": "jc",                             # Prefix
>          "sysadm_group": "jc_roles_sysadm",          # システム管理者のグループ名
>          "role_keyword": "roles",                    # ロールグループを表すキーワード
>          "role_mapping": {
>              "repoadm": "Repository Administrator",  # リポジトリ管理者グループ
>              "comadm": "Community Administrator",    # コミュニティ管理者グループ
>              "contributor": "Contributor"            # コントリビュータグループ
>          }
>      }

  -  isMemberOf属性がない場合に付与する、IdP毎のデフォルトの学認mAPグループを設定する。

      - IdPのエンティティIDをキーとして、デフォルトの学認mAPグループをリストで値に設定する。

         - 例 {"abc\_idp\_ac\_jp": \["jc\_abc\_idp\_ac\_jp\_groups\_yyy"\] }

      - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L126>

      - 設定キー：WEKO\_ACCOUNTS\_GAKUNIN\_DEFAULT\_GROUP\_MAPPING

      - 現在の設定値：

> WEKO\_ACCOUNTS\_GAKUNIN\_DEFAULT\_GROUP\_MAPPING = {}

  - 自機関のIdPを判別するためのIdPのentityID。

      - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L129>

      - 設定キー：WEKO\_ACCOUNTS\_IDP\_ENTITY\_ID

      - 現在の設定値：

> WEKO\_ACCOUNTS\_IDP\_ENTITY\_ID = "https://weko3.example.org/idp/simplesamlphp"

  - 学認mAPのグループ情報を取得するキー値のsuffix

      - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L131>

      - 設定キー：WEKO\_ACCOUNTS\_GAKUNIN\_GROUP\_SUFFIX

      - 現在の設定値：

> WEKO\_ACCOUNTS\_GAKUNIN\_GROUP\_SUFFIX = "_gakunin_groups"

5\. 実装

  - weko\_accounts.views. shib\_sp\_login関数によって、IdPからのリクエストを処理する

      - WEKO\_ACCOUNTS\_SHIB\_BIND\_GAKUNIN\_MAP\_GROUPSがTrueのとき、学認mAPグループをWEKO3にロールとして作成する

        - Redisの情報を用いて、WEKO3の学認mAPグループリストを更新する

            - Redisから「<institution_fqdn>とWEKO\_ACCOUNTS\_GAKUNIN\_GROUP\_SUFFIXを結合した値」をキーとして対応する機関の学認mAPグループをリストで取得する

                - <institution_fqdn>は対象機関のIdPのentityID（変数 WEKO\_ACCOUNTS\_IDP\_ENTITY\_ID）からFQDNを取得し、"."または"-"を"_"に置き換えた値になる

            - 取得した学認mAPグループリストはロールとして登録されていないかチェックする。ロールとして登録されていない学認mAPグループの場合、新規ロールとしてaccounts\_roleテーブルにレコード追加する

                - 学認mAPグループのインデックスツリーの権限の初期値を併せて登録する
    
      - リクエストにShib-Session-IDが含まれず、以下のコンフィグWEKO\_ACCOUNTS\_SHIB\_LOGIN\_ENABLEDがfalseの場合はエラーとしてWEKOのログイン画面に遷移する
        
          - > パス（instance.cfg）：  
            > <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L436>
        
          - > パス（config.py）：  
            > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L29>
    
      - weko\_accounts.utils. parse\_attributes関数によってリクエストの内容を確認し、必須の項目が含まれない場合はエラーとしてWEKOのログイン画面に遷移する
        
          - 必須項目は以下のコンフィグで設定する
            
              - > パス（instance.cfg）：  
                > <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L442-L448>
            
              - > パス（config.py）：  
                > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L64-L74>
            
              - > 設定キー：WEKO\_ACCOUNTS\_SSO\_ATTRIBUTE\_MAP
    
      - リクエストの内容にeppnが含まれず、かわりにHTTP\_WEKOIDを利用しない設定である場合はエラーとしてWEKOのログイン画面に遷移する
    
      - セッション情報はRedisに保存する
        
          - キーは、以下のコンフィグの値にログイン画面での入力値Shib-Session-IDを加えたものを用いる
            
              - > パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-accounts/weko_accounts/config.py#L32>
            
              - > 設定キー：WEKO\_ACCOUNTS\_SHIB\_CACHE\_PREFIX
    
      - リクエストの内容をもとに、shibboleth\_userテーブルからeppnまたはHTTP\_WEKOIDを使用してレコードの存在を確認する

  - 上記の処理で、shibboleth\_userテーブルにレコードが存在する場合は、weko\_accounts.views.shib\_auto\_login関数で続きの処理を行う
    
      - リクエストのShib-Session-IDとsession\['shib\_session\_id'\]のどちらかに情報がある場合は、ログインする
      
      - この先の処理は以下設定キーに応じて流れが異なる

          - > パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-accounts/weko_accounts/config.py> 

          - > 設定キー：WEKO\_ACCOUNTS\_SKIP\_CONFIRMATION\_PAGE

          - WEKO\_ACCOUNTS\_SKIP\_CONFIRMATION\_PAGE が false の場合は weko\_accounts.views.shib\_login 関数で ID 選択画面に遷移する

              - 登録済みの ID でログインする場合は、weko\_accounts.views.confirm\_user 関数で続きの処理を行う

                  - リクエストに、有効な WEKO アカウントとパスワードが含まれない場合は、WEKO のログイン画面に遷移する

                  - リクエストの WEKO アカウントのメールアドレスを使用して、shibboleth\_user テーブルにレコードを作成する

                  - weko\_accounts.api.ShibUser.check\_in メソッドの中で、ロールの割り当てを行う

                  - ログインする
        
              - リクエストにShib-Session-IDが含まれず、session\['shib\_session\_id'\]に情報がある場合は、weko\_accounts.api.ShibUser.new\_relation\_infoメソッドによってshibboleth\_userテーブルにレコードを作成する
            
                  - あわせて、userprofiles\_userprofileテーブルに以下の内容でレコードを作成する
                
                      - user\_id：shibboleth\_userテーブルに作成するレコードのidフィールドと同じ
                
                      - timezone：コンフィグのデフォルト値
                
                      - language：コンフィグのデフォルト値
                
                      - username：shibboleth\_userテーブルに作成するレコードのshib\_user\_nameフィールドと同じ
        
              - レコード作成の有無にかかわらず、weko\_accounts.api.ShibUser.check\_inメソッドの中で、ロールの割り当てを行う

              - レコード作成の有無にかかわらず、weko\_accounts.api.ShibUser. gakunin_check\_inメソッドの中で、学認mAPグループを更新する。

                  - shibboleth\_userroleテーブルでisMemberOf属性の値を基に、ユーザの学認mAPグループを割り当てる。
          
          - WEKO\_ACCOUNTS\_SKIP\_CONFIRMATION\_PAGE が true の場合は weko\_accounts.views.confirm\_user\_without\_page 関数で新規 ID および shibboleth\_user テーブルのレコードの自動生成を行う

              - ログインする
    
      - 上記以外の場合は、WEKOのログイン画面に遷移する

  - shibboleth\_userテーブルにレコードが存在しなかった場合は、weko\_accounts.views.shib\_login関数でID選択画面に遷移する
    
      - 登録済みのIDでログインする場合は、weko\_accounts.views.confirm\_user関数で続きの処理を行う
        
          - リクエストに、有効なWEKOアカウントとパスワードが含まれない場合は、WEKOのログイン画面に遷移する
        
          - リクエストのWEKOアカウントのメールアドレスを使用して、shibboleth\_userテーブルにレコードを作成する
        
          - weko\_accounts.api.ShibUser. check\_inメソッドの中で、ロールの割り当てを行う

              - WEKO\_ACCOUNTS\_SHIB\_BIND\_GAKUNIN\_MAP\_GROUPSがTrueのとき、ログインユーザーに学認mAPグループを割り当てる

                  - shibboleth\_userroleテーブルでisMemberOf属性の値を基に、ユーザーの学認mAPグループをロールとして割り当てる

                      - 学認mAPグループが割り当てられていないShibbolethログインユーザーの場合、WEKO\_ACCOUNTS\_GAKUNIN\_DEFAULT\_GROUP\_MAPPINGの設定値を基に、ログインユーザーのデフォルトのロールを割り当てる

                          - 認証されたIdPのentityIDの".", "-"を"\_"に置き換えた値をキーとして利用して、デフォルトの学認mAPグループを取得して割り当てる

                          - 該当グループが見つからない場合、またはWEKO\_ACCOUNTS\_GAKUNIN\_DEFAULT\_GROUP\_MAPPINGに該当するキー値が存在しない場合はユーザーにロールを付与しない

                  - 学認mAPグループの情報を基に、WEKO3のロールをShibbolethログインユーザーに割り当てる

                      - 以下のフォーマットに従う場合、対応するWEKO3のロールをログインユーザーに割り当てる

                          - 「jc\_roles\_sysadm」→ システム管理者ロール'System Administrator'

                          - 「jc\_\<entityid\>\_roles\_repoadm」→ リポジトリ管理者ロール'Repository Administrator'

                          - 「jc\_\<entityid\>\_roles\_comadm」→ コミュニティ管理者ロール'Community Administrator'

                          - 「jc\_\<entityid\>\_roles\_contributor」→ 一般利用者ロール'Contributor'

          - ログインする
    
      - 新規IDでログインする場合は、weko\_accounts.views.shib\_auto\_login関数でログインする

          - weko\_accounts.api.ShibUser. check\_inメソッドの中で、ロールの割り当てを行う

              - WEKO\_ACCOUNTS\_SHIB\_BIND\_GAKUNIN\_MAP\_GROUPSがTrueのとき、ログインユーザーに学認mAPグループを割り当てる

                  - shibboleth\_userroleテーブルでisMemberOf属性の値を基に、ユーザの学認mAPグループをロールとして割り当てる

                      - 学認mAPグループが割り当てられていないShibbolethログインユーザーの場合、WEKO\_ACCOUNTS\_GAKUNIN\_DEFAULT\_GROUP\_MAPPINGの設定値を基に、ログインユーザーのデフォルトのロールを割り当てる

                          - 認証されたIdPのentityIDの".", "-"を"\_"に置き換えた値をキーとして利用して、デフォルトの学認mAPグループを取得して割り当てる

                          - 該当グループが見つからない場合、またはWEKO\_ACCOUNTS\_GAKUNIN\_DEFAULT\_GROUP\_MAPPINGに該当するキー値が存在しない場合はユーザーにロールを付与しない

                  - 学認mAPグループの情報を基に、WEKO3のロールをShibbolethログインユーザーに割り当てる

                      - 以下のフォーマットに従う場合、対応するロールをログインユーザーに割り当てる

                          - 「jc\_roles\_sysadm」→ システム管理者ロール'System Administrator'

                          - 「jc\_\<entityid\>\_roles\_repoadm」→ リポジトリ管理者ロール'Repository Administrator'

                          - 「jc\_\<entityid\>\_roles\_comadm」→ コミュニティ管理者ロール'Community Administrator'

                          - 「jc\_\<entityid\>\_roles\_contributor」→ 一般利用者ロール'Contributor'

  - shibboleth\_userテーブルにレコードを作成する場合は、あわせてユーザ関連テーブルも上書きする
    
      - 1\) シボレス属性値をshibboleth\_userテーブルに登録する
        
          - mail ⇒ shibboleth\_user.shib\_mail
        
          - HTTP\_WEKOID ⇒ shibboleth\_user.shib\_user\_name
        
          - HTTP\_WEKOSOCIETYAFFILIATION ⇒shibboleth\_user.shib\_role\_authority\_name
    
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
<tr class="even">
<td><blockquote>
<p>2025/02/03</p>
</blockquote></td>
<td>a62f7a5ea350ec1a811cb053dd27c54f284705a4</td>
<td>学認mAP対応</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2025/03/12</p>
</blockquote></td>
<td>407a511f757c1991078dc69f4560a2f64a42b615</td>
<td>ユーザープロビジョニング自動化追記、ロール情報修正</td>
</tr>
</tbody>
</table>
