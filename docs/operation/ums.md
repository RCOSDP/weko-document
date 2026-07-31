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