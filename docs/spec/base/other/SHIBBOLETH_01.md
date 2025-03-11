## Shibboleth 対応

1\. Shibboleth IdP からの属性情報に基づき、ユーザへのロール割り当てをする

- Idp から取得した属性情報は、以下の設定に従って WEKO に渡される

  - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/nginx/login.php#L16-L20>

  - 「$\_SERVER\\[Idp側での属性名\\]」で渡された情報を「$post_args\\[WEKO 側での属性名\\]」として受け取る

- 認証時に IdP より取得した属性情報に基づきログインユーザに対してロール割り当てを行う

  - IdP 属性情報は以下とする

    - ロール：wekoSocietyAffiliation

  - IdP 属性値に対するロール割り当ては以下とする

    - 「管理者」→ システム管理者ロール'System Administrator'

    - 「学認 IdP 経由」→ 一般利用者ロール'Contributor'

    - 「機関内の Orthros 経由」→ リポジトリ管理者ロール'Repository Administrator'

    - 「機関外の Orthros 経由」→ コミュニティ管理者ロール'Community Administrator'

    - 「その他」→ ロール無'None'

  - 上記の IdP 属性値とロールとの対応は、以下のコンフィグで設定する

    - パス：(暫定)<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L140-L146>

    - 設定キー：WEKO_ACCOUNTS_SHIB_ROLE_RELATION

2\. Shibboleth IdP からの属性情報に基づき、サイトライセンス機能を制御する

- 認証時に IdP より取得した属性情報に基づきログインユーザに対してサイトライセンス制御を行う

  - IdP 属性情報は以下とする

    - サイトライセンス：wekoSiteUserWithinIpRange

  - IdP 属性値に対するサイトライセンスは以下とする

    - "False"の場合は以下のエラーメッセージを表示し、ログイン不可とする  
      　 JP: ログインに失敗しました。  
      　 EN: Failed to login.

3\. Shibboleth でのアカウント情報(ロール含む)の利用

- シボレス経由でログインする都度、シボレス属性値を WEKO3 のユーザ情報に反映

  - SHIB_ATTR_USER_NAME は、invenio の仕様でユニークである必要がある。

  - SHIB_ATTR_ROLE_AUTHORITY_NAME について、ロールの紐づけを config で指定できるものとし、config に含まれないロールであった場合は、WEKO のロールとしては設定しない

    - SHIB_ATTR_ROLE_AUTHORITY_NAME に複数属性が含まれている場合は，複数ロールの割当を行えるようにする。（複数属性が含まれている場合は属性値を半角セミコロン「;」で区切られている）

- シボレスユーザの紐づけキー

  - SHIB_ATTR_EPPN とする

  - 存在しない場合は、かわりに SHIB_ATTR_USER_NAME を利用することができる

  - SHIB_ATTR_USER_NAME を利用するかどうかは、以下の config で指定する

    - > パス：（暫定）<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L158>

    - > 設定キー：WEKO_ACCOUNTS_SHIB_ALLOW_USERNAME_INST_EPPN

4\. 実装

- weko_accounts.views. shib_sp_login 関数によって、IdP からのリクエストを処理する

  - リクエストに SHIB_ATTR_SESSION_ID が含まれず、以下のコンフィグ WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED が false の場合はエラーとして WEKO のログイン画面に遷移する

    - > パス（instance.cfg）：  
      > <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L436>

    - > パス（config.py）：  
      > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L29>

  - weko_accounts.utils. parse_attributes 関数によってリクエストの内容を確認し、必須の項目が含まれない場合はエラーとして WEKO のログイン画面に遷移する

    - 必須項目は以下のコンフィグで設定する

      - > パス（instance.cfg）：  
        > <https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg#L442-L448>

      - > パス（config.py）：  
        > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-accounts/weko_accounts/config.py#L64-L74>

      - > 設定キー：WEKO_ACCOUNTS_SSO_ATTRIBUTE_MAP

  - リクエストの内容に SHIB_ATTR_EPPN が含まれず、かわりに SHIB_ATTR_USER_NAME を利用しない設定である場合はエラーとして WEKO のログイン画面に遷移する

  - セッション情報は Redis に保存する

    - キーは、以下のコンフィグの値にログイン画面での入力値 SHIB_ATTR_SESSION_ID を加えたものを用いる

      - > パス：<https://github.com/RCOSDP/weko/blob/13c305a3048309dbda87a614ffedac18423820aa/modules/weko-accounts/weko_accounts/config.py#L32>

      - > 設定キー：WEKO_ACCOUNTS_SHIB_CACHE_PREFIX

  - リクエストの内容をもとに、shibboleth_user テーブルから SHIB_ATTR_EPPN または SHIB_ATTR_USER_NAME を使用してレコードの存在を確認する

- 上記の処理で、shibboleth_user テーブルにレコードが存在する場合は、weko_accounts.views.shib_auto_login 関数で続きの処理を行う

  - リクエストの SHIB_ATTR_SESSION_ID と session\['shib_session_id'\]のどちらかに情報がある場合は、ログインする

    - リクエストに SHIB_ATTR_SESSION_ID が含まれず、session\['shib_session_id'\]に情報がある場合は、weko_accounts.api.ShibUser.new_relation_info メソッドによって shibboleth_user テーブルにレコードを作成、および WEKO3 の新規 ID を作成する

      - あわせて、userprofiles_userprofile テーブルに以下の内容でレコードを作成する

        - user_id：shibboleth_user テーブルに作成するレコードの id フィールドと同じ

        - timezone：コンフィグのデフォルト値

        - language：コンフィグのデフォルト値

        - username：shibboleth_user テーブルに作成するレコードの shib_user_name フィールドと同じ

    - レコード作成の有無にかかわらず、weko_accounts.api.ShibUser. check_in メソッドの中で、ロールの割り当てを行う

- 新規 ID 作成後は、weko_accounts.views.shib_auto_login 関数でログインする

- shibboleth_user テーブルにレコードを作成する場合は、あわせてユーザ関連テーブルも上書きする

  - 1\) シボレス属性値を shibboleth_user テーブルに登録する

    - SHIB_ATTR_MAIL ⇒ shibboleth_user.shib_mail

    - SHIB_ATTR_USER_NAME ⇒ shibboleth_user.shib_user_name

    - SHIB_ATTR_ROLE_AUTHORITY_NAME ⇒shibboleth_user.shib_role_authority_name

  - 2\) shibboleth_user テーブルから各テーブルに登録する

    - shibboleth_user.shib_mail ⇒ accounts_user.email

    - shibboleth_user.shib_user_name ⇒ userprofiles_userprofile.username

    - shibboleth_user.shib_role_authority_name ⇒ accounts_userrole.user_id,role_id

  - 1\),2\) どちらの登録の際も値のチェックは行わず、登録先の値を上書きする

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
<p>2025/02/-</p>
</blockquote></td>
<td></td>
<td>ユーザープロビジョニング自動化追記、ロール情報修正</td>
</tr>
</tbody>
</table>
