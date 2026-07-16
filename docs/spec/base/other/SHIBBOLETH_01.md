# Shibboleth対応

1\. Shibboleth IdPからの属性情報に基づき、ユーザへのロール割り当てをする

  - Idpから取得した属性情報は、以下の設定に従ってWEKOに渡される

    - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/nginx/login.php#L16-L20>

    - 「$_SERVER[Idp側での属性名]」で渡された情報を「$post_args[WEKO側での属性名]」として受け取る

  - 認証時にIdPより取得した属性情報に基づきログインユーザに対してロール割り当てを行う

    - IdP属性情報は以下とする

      - ロール：wekoSocietyAffiliation

    - IdP属性値に対するロール割り当ては以下とする（WEKO_ACCOUNTS_SHIB_ROLE_RELATION）

      - 「管理者」→システム管理者ロール'System Administrator'

      - 「図書館員」→ リポジトリ管理者ロール'Repository Administrator'

      - 「教員」→ 一般利用者ロール'Contributor'

      - 「教官」→ 一般利用者ロール'Contributor'

    - 上記のIdP属性値とロールとの対応は、以下のコンフィグで設定する

      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L77-L82>

      - 設定キー：WEKO_ACCOUNTS_SHIB_ROLE_RELATION

    - IdP属性値がconfigに含まれないロールであった場合は、ロールを持たないユーザとなる

      - 設定値によって既定のロールが設定されている場合は、設定値を用いて既定のロールを付与する。

    - isMemberOfの属性値が付与されている場合、学認mAPグループからロールを割り当てる。

      - 以下のフォーマットに従う学認mAPグループを持つ場合、それぞれ以下のロールに割り当てる。

        - 「jc_roles_sysadm」→ システム管理者ロール'System Administrator'

        - 「jc_<fqdn>_ro_radm」→ リポジトリ管理者ロール'Repository Administrator'

        - 「jc_<fqdn>_ro_cadm」→ コミュニティ管理者ロール'Community Administrator'

        - 「jc_<fqdn>_ro_cont」→ 一般利用者ロール'Contributor'

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

    - HTTP_WEKOID は、invenio の仕様でユニークである必要がある。

    - HTTP_WEKOSOCIETYAFFILIATIONについて、ロールの紐づけをconfig で指定できるものとし、configに含まれないロールであった場合は、WEKOのロールとしては設定しない

      - HTTP_WEKOSOCIETYAFFILIATIONに複数属性が含まれている場合は，複数ロールの割当を行えるようにする。（複数属性が含まれている場合は属性値を半角セミコロン「;」で区切られている）

    - 設定値WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPSが有効（True）の場合、isMemberOfについて、所属している学認mAPグループをWEKO3に紐づける。

      - 学認mAPグループはそのグループエンティティIDを名前に持つロールとして登録される。

      - ログイン時に所属している学認mAPグループをWEKO3のユーザーに付与する。

  - シボレスユーザの紐づけキー

    - eppnとする

    - 存在しない場合は、かわりにHTTP_WEKOIDを利用することができる

    - HTTP_WEKOIDを利用するかどうかは、以下のconfigで指定する

      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L97>

      - 設定キー：WEKO_ACCOUNTS_SHIB_ALLOW_USERNAME_INST_EPPN

4\. 設定

  -  学認mAPグループ情報をWEKO3と連携するか設定する。(Trueの場合、学認mAPグループとWEKO3を連携する。)

    - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L111>

    - 設定キー：WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS

    - 現在の設定値：

> WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS = False

  - GakuNin mAPグループのグループIDのフォーマットおよびWEKO3のロールを紐づけるキーワード

    - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L114>

    - 設定キー：WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT

    - 現在の設定値：

>      WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT = {
>          "prefix": "jc",                             # Prefix
>          "sysadm_group": "jc_roles_sysadm",          # システム管理者のグループ名
>          "role_keyword": "ro",                    # ロールグループを表すキーワード
>          "role_mapping": {
>              "radm": "Repository Administrator",  # リポジトリ管理者グループ
>              "cadm": "Community Administrator",    # コミュニティ管理者グループ
>              "cont": "Contributor"            # コントリビュータグループ
>          }
>      }

  -  isMemberOf属性がない場合に付与する、IdP毎のデフォルトの学認mAPグループを設定する。

    - IdPのエンティティIDをキーとして、デフォルトの学認mAPグループをリストで値に設定する。

      - 例 {"abc_idp_ac_jp": ["jc_abc_idp_ac_jp_groups_yyy"] }

    - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L126>

    - 設定キー：WEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPING

    - 現在の設定値：

> WEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPING = {}

  - 自機関のIdPを判別するためのIdPのentityID。

    - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L129>

    - 設定キー：WEKO_ACCOUNTS_IDP_ENTITY_ID

    - 現在の設定値：

> WEKO_ACCOUNTS_IDP_ENTITY_ID = ""

  - 学認mAPのグループ情報を取得するキー値のsuffix

    - パス：<https://github.com/RCOSDP/weko/blob/v1.1.0/modules/weko-accounts/weko_accounts/config.py#L131>

    - 設定キー：WEKO_ACCOUNTS_GAKUNIN_GROUP_SUFFIX

    - 現在の設定値：

> WEKO_ACCOUNTS_GAKUNIN_GROUP_SUFFIX = "_gakunin_groups"

5\. 実装

  - weko_accounts.views.shib_sp_login関数によって、IdPからのリクエストを処理する

    - WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPSがTrueのとき、学認mAPグループをWEKO3にロールとして作成する

      - Redisの情報を用いて、WEKO3の学認mAPグループリストを更新する

        - Redisから「<institution_fqdn>とWEKO_ACCOUNTS_GAKUNIN_GROUP_SUFFIXを結合した値」をキーとして対応する機関の学認mAPグループをリストで取得する

          - <institution_fqdn>は対象機関のIdPのentityID（変数 WEKO_ACCOUNTS_IDP_ENTITY_ID）からFQDNを取得し、"."または"-"を"_"に置き換えた値になる

        - 取得した学認mAPグループリストはロールとして登録されていないかチェックする。ロールとして登録されていない学認mAPグループの場合、新規ロールとしてaccounts_roleテーブルにレコード追加する

          - 学認mAPグループのインデックスツリーの権限の初期値を併せて登録する

    - リクエストにShib-Session-IDが含まれず、以下のコンフィグWEKO_ACCOUNTS_SHIB_LOGIN_ENABLEDがfalseの場合はエラーとしてWEKOのログイン画面に遷移する

      - パス（instance.cfg）：  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L436>

      - パス（config.py）：  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L29>

    - weko_accounts.utils.parse_attributes関数によってリクエストの内容を確認し、必須の項目が含まれない場合はエラーとしてWEKOのログイン画面に遷移する

      - 必須項目は以下のコンフィグで設定する

        - パス（instance.cfg）：  
          <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L442-L448>

        - パス（config.py）：  
          <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L64-L74>

        - 設定キー：WEKO_ACCOUNTS_SSO_ATTRIBUTE_MAP

    - リクエストの内容にeppnが含まれず、かわりにHTTP_WEKOIDを利用しない設定である場合はエラーとしてWEKOのログイン画面に遷移する

    - セッション情報はRedisに保存する

      - キーは、以下のコンフィグの値にログイン画面での入力値Shib-Session-IDを加えたものを用いる

        - パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-accounts/weko_accounts/config.py#L32>

        - 設定キー：WEKO_ACCOUNTS_SHIB_CACHE_PREFIX

    - リクエストの内容をもとに、shibboleth_userテーブルからeppnまたはHTTP_WEKOIDを使用してレコードの存在を確認する

  - 上記の処理で、shibboleth_userテーブルにレコードが存在する場合は、weko_accounts.views.shib_auto_login関数で続きの処理を行う

    - リクエストのShib-Session-IDとsession['shib_session_id']のどちらかに情報がある場合は、ログインする

    - この先の処理は以下設定キーに応じて流れが異なる

      - パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-accounts/weko_accounts/config.py> 

      - 設定キー：WEKO_ACCOUNTS_SKIP_CONFIRMATION_PAGE

      - WEKO_ACCOUNTS_SKIP_CONFIRMATION_PAGE が false の場合は weko_accounts.views.shib_login 関数で ID 選択画面に遷移する

        - 登録済みの ID でログインする場合は、weko_accounts.views.confirm_user 関数で続きの処理を行う

          - リクエストに、有効な WEKO アカウントとパスワードが含まれない場合は、WEKO のログイン画面に遷移する

          - リクエストの WEKO アカウントのメールアドレスを使用して、shibboleth_user テーブルにレコードを作成する

          - weko_accounts.api.ShibUser.check_in メソッドの中で、ロールの割り当てを行う

          - ログインする

        - リクエストにShib-Session-IDが含まれず、session['shib_session_id']に情報がある場合は、weko_accounts.api.ShibUser.new_relation_infoメソッドによってshibboleth_userテーブルにレコードを作成する

          - あわせて、userprofiles_userprofileテーブルに以下の内容でレコードを作成する

            - user_id：shibboleth_userテーブルに作成するレコードのidフィールドと同じ

            - timezone：コンフィグのデフォルト値

            - language：コンフィグのデフォルト値

            - username：shibboleth_userテーブルに作成するレコードのshib_user_nameフィールドと同じ

        - レコード作成の有無にかかわらず、weko_accounts.api.ShibUser.check_inメソッドの中で、ロールの割り当てを行う

        - 学認mAPグループの更新（isMemberOf属性値に基づく割り当て）は、weko_accounts.api.ShibUser.check_inメソッド内でインラインに行われる。

          - shibboleth_userroleテーブルでisMemberOf属性の値を基に、ユーザの学認mAPグループを割り当てる。

      - WEKO_ACCOUNTS_SKIP_CONFIRMATION_PAGE が true の場合は weko_accounts.views.confirm_user_without_page 関数で新規 ID および shibboleth_user テーブルのレコードの自動生成を行う

        - ログインする

    - 上記以外の場合は、WEKOのログイン画面に遷移する

  - shibboleth_userテーブルにレコードが存在しなかった場合は、weko_accounts.views.shib_login関数でID選択画面に遷移する

    - 登録済みのIDでログインする場合は、weko_accounts.views.confirm_user関数で続きの処理を行う

      - リクエストに、有効なWEKOアカウントとパスワードが含まれない場合は、WEKOのログイン画面に遷移する

      - リクエストのWEKOアカウントのメールアドレスを使用して、shibboleth_userテーブルにレコードを作成する

      - weko_accounts.api.ShibUser.check_inメソッドの中で、ロールの割り当てを行う

        - WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPSがTrueのとき、ログインユーザーに学認mAPグループを割り当てる

          - shibboleth_userroleテーブルでisMemberOf属性の値を基に、ユーザーの学認mAPグループをロールとして割り当てる

            - 学認mAPグループが割り当てられていないShibbolethログインユーザーの場合、WEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPINGの設定値を基に、ログインユーザーのデフォルトのロールを割り当てる

              - 認証されたIdPのentityIDの".", "-"を"_"に置き換えた値をキーとして利用して、デフォルトの学認mAPグループを取得して割り当てる

              - 該当グループが見つからない場合、またはWEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPINGに該当するキー値が存在しない場合はユーザーにロールを付与しない

          - 学認mAPグループの情報を基に、WEKO3のロールをShibbolethログインユーザーに割り当てる

            - 以下のフォーマットに従う場合、対応するWEKO3のロールをログインユーザーに割り当てる

              - 「jc_roles_sysadm」→ システム管理者ロール'System Administrator'

              - 「jc_<fqdn>_ro_radm」→ リポジトリ管理者ロール'Repository Administrator'

              - 「jc_<fqdn>_ro_cadm」→ コミュニティ管理者ロール'Community Administrator'

              - 「jc_<fqdn>_ro_cont」→ 一般利用者ロール'Contributor'

      - ログインする

    - 新規IDでログインする場合は、weko_accounts.views.shib_auto_login関数でログインする

      - weko_accounts.api.ShibUser.check_inメソッドの中で、ロールの割り当てを行う

        - WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPSがTrueのとき、ログインユーザーに学認mAPグループを割り当てる

          - shibboleth_userroleテーブルでisMemberOf属性の値を基に、ユーザの学認mAPグループをロールとして割り当てる

            - 学認mAPグループが割り当てられていないShibbolethログインユーザーの場合、WEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPINGの設定値を基に、ログインユーザーのデフォルトのロールを割り当てる

              - 認証されたIdPのentityIDの".", "-"を"_"に置き換えた値をキーとして利用して、デフォルトの学認mAPグループを取得して割り当てる

              - 該当グループが見つからない場合、またはWEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPINGに該当するキー値が存在しない場合はユーザーにロールを付与しない

          - 学認mAPグループの情報を基に、WEKO3のロールをShibbolethログインユーザーに割り当てる

            - 以下のフォーマットに従う場合、対応するロールをログインユーザーに割り当てる

              - 「jc_roles_sysadm」→ システム管理者ロール'System Administrator'

              - 「jc_<fqdn>_ro_radm」→ リポジトリ管理者ロール'Repository Administrator'

              - 「jc_<fqdn>_ro_cadm」→ コミュニティ管理者ロール'Community Administrator'

              - 「jc_<fqdn>_ro_cont」→ 一般利用者ロール'Contributor'

  - shibboleth_userテーブルにレコードを作成する場合は、あわせてユーザ関連テーブルも上書きする

    - 1) シボレス属性値をshibboleth_userテーブルに登録する

      - mail ⇒ shibboleth_user.shib_mail

      - HTTP_WEKOID ⇒ shibboleth_user.shib_user_name

      - HTTP_WEKOSOCIETYAFFILIATION ⇒shibboleth_user.shib_role_authority_name

    - 2) shibboleth_userテーブルから各テーブルに登録する

      - shibboleth_user.shib_mail ⇒ accounts_user.email

      - shibboleth_user.shib_user_name ⇒ userprofiles_userprofile.username

      - shibboleth_user.shib_role_authority_name ⇒ accounts_userrole.user_id,role_id

    - 1),2) どちらの登録の際も値のチェックは行わず、登録先の値を上書きする。

- 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2025/02/03 | a62f7a5ea350ec1a811cb053dd27c54f284705a4 | 学認mAP対応 |
| 2025/03/12 | 407a511f757c1991078dc69f4560a2f64a42b615 | ユーザープロビジョニング自動化追記、ロール情報修正 |
| 2026/07/14 |  | 本文を実装準拠に修正 |

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足（訂正、v2.0.2）：Shibboleth ログインの実エンドポイントは `POST /weko/shib/login`（`weko_accounts.views.shib_sp_login`）。ロール付与は `ShibUser.check_in`（`gakunin_check_in` というメソッドは存在せず、mAPグループ処理は check_in 内にインライン）→ `_find_organization_name`（organizationName判定。真なら mAPグループ判定 `_assign_roles_to_user` をスキップ）。
- config 実値：`WEKO_ACCOUNTS_SHIB_ROLE_RELATION = {'管理者':'System Administrator','図書館員':'Repository Administrator','教員':'Contributor','教官':'Contributor'}`。`WEKO_ACCOUNTS_GAKUNIN_GROUP_PATTERN_DICT` は `role_keyword='ro'`、`role_mapping={'radm':'Repository Administrator','cadm':'Community Administrator','cont':'Contributor'}`（グループ名例は `jc_<fqdn>_ro_radm` 等）。`WEKO_ACCOUNTS_IDP_ENTITY_ID` の既定は空文字。
- table `shibboleth_user`（`ShibbolethUser`）＋中間表 `shibboleth_userrole`。紐づけキーは `shib_eppn`。ブロックユーザーは AdminSettings `blocked_user_settings.blocked_ePPNs` で拒否。関連：[AMS Shibboleth対応](../ams/AMS_SHIBBOLETH_01.md)。
