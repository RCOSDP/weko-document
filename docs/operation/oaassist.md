# OA Assist連携利用手順（WEKO3→OA Assist）

WEKO3からOA AssistのAPIを呼び出すには、
OA AssistのOAuth2トークンをWEKO3側に登録する必要がある。

この連携により、以下の機能がWEKO3で利用可能になる。

- アイテム登録時のOAポリシDB検索
- 研究者用ワークスペースのステータス連携機能

この機能を利用するにはHTTPSによる双方向通信ができる必要がある。

## OA Assist

アプリケーション環境サーバに入る。

```
$ docker exec -it 7d6916ba66ef bash
```

Railsに入る。

```
rails console
```

OAuth2キーを発行する。

```
Doorkeeper::Application.find_by(organization_id: 723)
```

## WEKO3

管理画面でOAuth2キーを登録する。

```
invenio cert insert oaa "OAアシスト"
```







ポリシー検索はメタデータ入力項目の「収録物名（Source Title）」および「収録物識別子（Source Identifier）」に入力されたメタデータを参照して、OAアシスト側に問い合わせています。
以下のいずれかのメタデータ（複合指定も可）を入力して検索することで該当のポリシー情報が取得できるかと思いますので、ご確認いただけますでしょうか。

---上記画像の上から2番目のポリシー情報---
収録物名：
　VIRTUAL REALITY
収録物識別子：
　収録物識別子タイプ=ISSN の場合 ⇒ 13594338
　収録物識別子タイプ=EISSN の場合 ⇒ 14349957

ポリシーURL： https://www.springer.com/gp/open-access/publication-policies/copyright-transfer

