# 学認（テストフェデレーション）対応手順（DS利用の場合）

[学認（テストフェデレーション）対応手順](./gakunin.md)との差分を説明する。

## DS(Discovery Service)を設定する。

/etc/shibboleth/shibboleth2.xml ファイルの
「</Sessions>」の直前に以下を挿入する。

```
<SessionInitiator type="Chaining" Location="/DS" isDefault="true" id="DS">
    <SessionInitiator type="SAML2" template="bindingTemplate.html"/>
    <SessionInitiator type="Shib1"/>
    <SessionInitiator type="SAMLDS" URL="https://test-ds.gakunin.nii.ac.jp/WAYF"/>
</SessionInitiator>
```

shibdを再起動し、ログにエラーがでてないことを確認する。

```
supervisorctl restart shibd
```

## WEKO3の設定​

instance.cfgの以下設定を変更する。

```
WEKO_ACCOUNTS_SHIB_LOGIN_ENABLED = True
WEKO_ACCOUNTS_SHIB_IDP_LOGIN_ENABLED = False
WEKO_ACCOUNTS_SHIB_DP_LOGIN_DIRECTLY_ENABLED = True
WEKO_ACCOUNTS_SHIB_INST_LOGIN_DIRECTLY_ENABLED = False
WEKO_ACCOUNTS_SHIB_BIND_GAKUNIN_MAP_GROUPS = True
```

```isMemberOf```に含まれないユーザのデフォルト権限の設定は現状機能しないため、
設定値を削除する。

```
WEKO_ACCOUNTS_GAKUNIN_DEFAULT_GROUP_MAPPING = {}
```

WEKO3を再起動する。

