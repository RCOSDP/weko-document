# UMS設定

## shibboleth-sp

## 設定

shibboleth2.xml

```
<SPConfig xmlns="urn:mace:shibboleth:3.0:native:sp:config"
    xmlns:conf="urn:mace:shibboleth:3.0:native:sp:config"
    clockSkew="180">
    <OutOfProcess tranLogFormat="%u|%s|%IDP|%i|%ac|%t|%attr|%n|%b|%E|%S|%SS|%L|%UA|%a" />
    <UnixListener address="/tmp/shibd.sock"/>
    <RequestMapper type="XML">
        <RequestMap>
            <Host name="jc-app-rc.repo.nii.ac.jp"
                authType="shibboleth"
                requireSession="true"
                redirectToSSL="443">
                <Path name="/secure" />
            </Host>
        </RequestMap>
    </RequestMapper>
    <ApplicationDefaults entityID="https://jc-app-rc.repo.nii.ac.jp/shibboleth-sp"
        REMOTE_USER="eppn persistent-id targeted-id"
        cipherSuites="DEFAULT:!EXP:!LOW:!aNULL:!eNULL:!DES:!IDEA:!SEED:!RC4:!3DES:!kRSA:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1">
        <Sessions lifetime="28800" timeout="3600" relayState="ss:mem"
                  checkAddress="false" handlerSSL="false" cookieProps="http">
            <SSO entityID="https://idp.repo.nii.ac.jp/idp/shibboleth"
                 discoveryProtocol="SAMLDS" discoveryURL="https://ds.example.org/DS/WAYF">
              SAML2
            </SSO>
            <Logout>SAML2 Local</Logout>
            <LogoutInitiator type="Admin" Location="/Logout/Admin" acl="127.0.0.1 ::1" />
            <Handler type="MetadataGenerator" Location="/Metadata" signing="false"/>
            <Handler type="Status" Location="/Status" acl="127.0.0.1 ::1"/>
            <Handler type="Session" Location="/Session" showAttributeValues="false"/>
            <Handler type="DiscoveryFeed" Location="/DiscoFeed"/>
        </Sessions>
        <Errors supportContact="root@localhost"
            helpLocation="/about.html"
            styleSheet="/shibboleth-sp/main.css"/>
        <MetadataProvider type="XML" url="https://idp.repo.nii.ac.jp/metadata/irjaya.xml"
             backingFilePath="irjaya.xml" reloadInterval="7200">
        </MetadataProvider>
        <AttributeExtractor type="XML" validate="true" reloadChanges="false" path="attribute-map.xml"/>
        <AttributeFilter type="XML" validate="true" path="attribute-policy.xml"/>
        <CredentialResolver type="File" use="signing"
            key="shibboleth-common.key" certificate="shibboleth-common.cer"/>
        <CredentialResolver type="File" use="encryption"
            key="shibboleth-common.key" certificate="shibboleth-common.cer"/>
    </ApplicationDefaults>
    <SecurityPolicyProvider type="XML" validate="true" path="security-policy.xml"/>
    <ProtocolProvider type="XML" validate="true" reloadChanges="false" path="protocols.xml"/>
</SPConfig>
```

attribute-map.xml

```
<Attributes xmlns="urn:mace:shibboleth:2.0:attribute-map" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <!-- First some useful eduPerson attributes that many sites might use. -->

    <Attribute name="urn:mace:dir:attribute-def:eduPersonPrincipalName" id="eppn">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder"/>
    </Attribute>
    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.6" id="eppn">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder"/>
    </Attribute>

    <Attribute name="urn:mace:dir:attribute-def:eduPersonScopedAffiliation" id="affiliation">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>
    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.9" id="affiliation">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>

    <Attribute name="urn:mace:dir:attribute-def:eduPersonAffiliation" id="unscoped-affiliation">
        <AttributeDecoder xsi:type="StringAttributeDecoder" caseSensitive="false"/>
    </Attribute>
    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.1" id="unscoped-affiliation">
        <AttributeDecoder xsi:type="StringAttributeDecoder" caseSensitive="false"/>
    </Attribute>

    <Attribute name="urn:mace:dir:attribute-def:eduPersonEntitlement" id="entitlement"/>
    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.7" id="entitlement"/>

    <!-- A persistent id attribute that supports personalized anonymous access. -->

    <!-- First, the deprecated version, decoded as a scoped string: -->
    <Attribute name="urn:mace:dir:attribute-def:eduPersonTargetedID" id="targeted-id">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder"/>
        <!-- <AttributeDecoder xsi:type="NameIDFromScopedAttributeDecoder" formatter="$NameQualifier!$SPNameQualifier!$Name"/> -->
    </Attribute>

    <!-- Second, an alternate decoder that will turn the deprecated form into the newer form. -->
    <!--
    <Attribute name="urn:mace:dir:attribute-def:eduPersonTargetedID" id="persistent-id">
        <AttributeDecoder xsi:type="NameIDFromScopedAttributeDecoder" formatter="$NameQualifier!$SPNameQualifier!$Name"/>
    </Attribute>
    -->

    <!-- Third, the new version (note the OID-style name): -->
    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.10" id="persistent-id">
        <AttributeDecoder xsi:type="NameIDAttributeDecoder" formatter="$NameQualifier!$SPNameQualifier!$Name"/>
    </Attribute>

    <!-- Fourth, the SAML 2.0 NameID Format: -->
    <Attribute name="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent" id="persistent-id">
        <AttributeDecoder xsi:type="NameIDAttributeDecoder" formatter="$NameQualifier!$SPNameQualifier!$Name"/>
    </Attribute>

    <!-- Some more eduPerson attributes, uncomment these to use them... -->

    <!--Examples of LDAP-based attributes, uncomment to use these... -->

    <Attribute name="urn:mace:dir:attribute-def:mail" id="mail"/>
    <Attribute name="urn:mace:dir:attribute-def:displayName" id="displayName"/>
    <Attribute name="urn:mace:dir:attribute-def:wekoId" id="wekoId"/>
    <Attribute name="urn:mace:dir:attribute-def:wekoGmoIdentifier" id="wekoGmoIdentifier"/>
    <Attribute name="urn:mace:dir:attribute-def:wekoSocietySubGroup" id="wekoSocietySubGroup"/>
    <Attribute name="urn:mace:dir:attribute-def:wekoSocietyAffiliation" id="wekoSocietyAffiliation"/>
    <Attribute name="urn:mace:dir:attribute-def:wekoActiveUser" id="wekoActiveUser"/>

    <Attribute name="urn:oid:0.9.2342.19200300.100.1.3" id="mail"/>
    <Attribute name="urn:oid:2.16.840.1.113730.3.1.241" id="displayName"/>
    <Attribute name="urn:oid:1.3.6.1.4.1.32264.2.1.1" id="wekoId"/>
    <Attribute name="urn:oid:1.3.6.1.4.1.32264.2.1.2" id="wekoGmoIdentifier"/>
    <Attribute name="urn:oid:1.3.6.1.4.1.32264.2.1.6" id="wekoSocietyAffiliation"/>
    <Attribute name="urn:oid:1.3.6.1.4.1.32264.2.1.7" id="wekoSocietySubGroup"/>
    <Attribute name="urn:oid:1.3.6.1.4.1.32264.2.1.8" id="wekoActiveUser"/>
</Attributes>
```
