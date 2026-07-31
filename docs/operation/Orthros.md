# Orthros（テストフェデレーション）対応手順

[学認（テストフェデレーション）対応手順](./gakunin.md)との差分について説明する。

## Orthrosテスト環境へのSP登録申請

以下サイトを参照しながら登録する。

[SP管理者向けマニュアル](https://github.com/gakunin/orthros-docs/tree/main/docs/SP%E7%AE%A1%E7%90%86%E8%80%85%E5%90%91%E3%81%91%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB)


具体的には以下サイトのとおりに実施する。

[Orthrosとの接続依頼方法](https://github.com/gakunin/orthros-docs/blob/main/docs/SP%E7%AE%A1%E7%90%86%E8%80%85%E5%90%91%E3%81%91%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB/2%20Orthros%E3%81%A8%E3%81%AE%E6%8E%A5%E7%B6%9A%E4%BE%9D%E9%A0%BC%E6%96%B9%E6%B3%95%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/1%20Orthros%E3%81%A8%E3%81%AE%E6%8E%A5%E7%B6%9A%E4%BE%9D%E9%A0%BC%E6%96%B9%E6%B3%95.md)


申請本文の例

```
■ご担当者様情報
・氏名：XXX
・フリガナ：XXX

・機関名称：XXX
・フリガナ：XXX

・所属学部/部署
XXX
・職名
XXX
・電話番号
XXX
・E-mail
XXX
・住所
XXX

[テスト環境]
・接続SPのentityID※1：
https://${FQDN}/shibboleth-sp
・OrthrosのSP管理者として登録する方のOrthrosアカウントID（メールアドレス）※2：
XXX
・サービス名称：XXX
・サービス名称（英語）：XXX
・サービスURL：https://${FQDN}/
・サービス説明：XXX
```

## Shibboleth-SPの設定

### メタデータを設定する。

Orthrosから送らてきたメタデータを```/etc/shibboleth/metadata/```に設置する。


```/etc/shibboleth/sihbboleth2.xml```の```<MetadataProvider>```の最後の要素の次に以下を挿入する。

```
<!-- Orthrosメタデータの設定-->
<MetadataProvider type="XML" path="/etc/shibboleth/metadata/orthrosstg-idp-metadata.xml"/>
```

shibdを再起動し、ログにエラーがでてないことを確認する。

```
supervisorctl restart shibd
```