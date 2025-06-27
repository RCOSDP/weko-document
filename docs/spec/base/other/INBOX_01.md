# 登録完了・承認通知機能

## 用途・目的
セルフアーカイブによるアイテム登録が完了した際、登録者に状況を通知する機能を提供する。  
また、登録されたアイテムが承認待ち状態になった際、承認者に通知する機能を提供する。  
セルフアーカイブにより、登録されるアイテムのリポジトリ上での状況管理が煩雑化するため、
これを支援することを目的とする。

## 機能内容
- アイテム登録・編集・削除が行われた際、登録者に状況を通知する。
- 通知方法としてメールおよびCOAR Notifyに対応する。
- 承認が必要なアイテムが発生した場合は、承認者に対してメールで通知する。  
  メールには承認フローにダイレクトにアクセスできるURLを含む。
- ユーザプロファイル画面でオン・オフできる。

## 利用可能なロール

|  ロール  | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| -------- | -------------- | ---------------- | ------------------ | ------------ | ------------ | ------------------ |
| 利用可否 |       〇       |        〇        |         〇         |      〇      |      〇      |        ×          |

## 利用方法
開発時向けの設定は[開発環境の構築](#開発環境の構築)を参照。

### 環境設定

WEKO3のアプリケーション環境設定（instance.cfg）で、通知機能を有効にする。

```config
WEKO_NOTIFICATIONS = True
```

通知サーバーの環境設定（docker-compose.yml）で、プッシュ通知に使用する認証鍵の設定を行う。  
各機関リポジトリごとにプッシュ通知を発行するためにVAPIDの秘密鍵と公開鍵を生成し、環境変数として設定が必要である。  

```diff
# docker-compose.yml
  inbox:
    environment:
-     - VAPID_PUBLIC_KEY=
+     - VAPID_PUBLIC_KEY=BENmk-3PWlV9zoIRMOgzJrpgnk0bzCPNWqs2T4TchRKigOjAUBdeyEKntjixJuEJDhvC2XYVHeKQCv1OxVCiX4s
-     - VAPID_PRIVATE_KEY=
+     - VAPID_PRIVATE_KEY=7794peKggbs6fd2TwZkfQ-AtybMj5PEz4tkD9VW1e6s
```

この変更をした後、両コンテナを再起動する。

### サーバー証明書のインポート

開発環境でもWebプッシュ通知を利用するためには、サーバー証明書をインポートする必要がある。  
`subjectnames.txt`を使用する環境のIPアドレスに合わせて修正し、サーバー証明書を再作成する。

```bash
$ cd nginx/keys
$ openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt -extfile subjectnames.txt
```

これをnginxのコンテナに反映し、ブラウザにインポートする。

### 通知の購読設定

![通知の購読設定画面](../media/media/image36.png)

ユーザーは、設定画面からWebプッシュ通知とメール通知の購読および解除を行うことができる。  

プッシュ通知は、Webpush APIを使用して、購読情報を発行し、INBOXに登録する。  
また、購読の解除時は、Webpush APIを使用して購読を取りやめ、INBOXから購読情報を削除することで通知を停止する。

メール通知は、ユーザープロフィールで設定されているメールアドレスが確認済みである場合、設定をONにすることでメール通知を有効にする。

## 仕様概要

### 通知形態

- メール通知
- Webプッシュ通知

通知の言語はユーザープロファイルに設定した言語とする。


### 通知イベントと通知先
  - アイテム登録・編集・削除完了：登録者、代理投稿者
  - 登録・編集・削除承認リクエスト：承認者
  - リクエスト受理・拒否：登録者、代理投稿者

ただし、操作者本人には通知しない。

### 通知内容のカスタマイズ性

管理者は通知内容（タイトル・本文）をカスタマイズすることができる。  
多言語対応のため、言語ごとにテンプレートを作成でき、
通知の生成時に受信者のユーザープロファイルに設定された言語に応じたテンプレートが選択される。  

```
Title: 【登録完了】
Body:  あなたのアイテム「{{ item_title }}」が登録されました。
```

```
Title: Conpleted registration
Body:  Your item "{{ item_title }}" has been registered.
```

## 基本設計

### 通知フロー

アイテム登録完了などをトリガーにプッシュ通知を発行するとき、LDN生成、通知先の選定、本文生成、
通知の送信、永続化の5つのステップで構成される。

![通知生成時のフロー](../media/media/image34.png)

1. LDN生成  
   アイテム登録完了などのイベントが発生したとき、まず、通知の内容をCoarNotifyで表現するために必要なパラメータを生成する。  
   生成されるパラメータは、通知の種類、通知の対象、通知の発行元、通知の宛先などが含まれる。  
   そして、これらのパラメータをもとにCoarNotifyに基づいたLDN形式の通知を生成する。  

2. 通知先の選定  
   ユーザーの購読情報をもとに、プッシュ通知またはメール通知が必要かを確認し、送信先を選定する。  

3. タイトル・本文内容の生成  
   CoarNotifyに基づいたLDN形式ではユーザーには内容がわかりにくいため、通知の内容を生成する。  
   タイトル・本文は、通知の種類に応じて、テンプレートをもとに生成する。  
   現時点では通知先はWEKO3ユーザーのみであるが、将来的に外部サービスのINBOXへ通知する場合は、LDN形式のまま送信する。

4. 通知の送信  
   生成した通知のタイトル・本文を、通知先の選定で選ばれた送信先に送信する。  
   送信先は、メールアドレスやWebpushエンドポイントなどがある。

5. 永続化
   最後に、通知の二次利用に備えて、LDN形式の通知を永続化する。  
   ユーザーに表示する際は、永続化された通知をもとに、通知の本文を再生成する。

### システム構成

前述の通知フローのうち、LDN生成（パラメータ生成）はアプリケーションサーバー（以降、WEKO3）で行い、
以降のステップは通知サーバー（以降、INBOX）で行う。  
WEKO3からINBOXへの通知の送信にはHTTP通信を利用し、そのコンテンツはCoarNotifyに基づいたLDN形式の通知となる。  
この構成は、CoarNotifyのアーキテクチャ[Option3](https://coar-notify.net/guide/architecture/)に基づく。

![システム構成](../media/media/image35.png)

WEKO3は、invenioフレームワークをベースにしたアプリケーションサーバーで、Flaskを使用したWebアプリケーションとして実装される。  
一方、INBOXはCoarNotifyに基づいた通知サーバーで、FastAPIを使用したWebアプリケーションとして実装された
[coar-notify-inbox](https://github.com/seanwiseman/coar-notify-inbox) をベースにプッシュ通知の機能を追加したものである。

プッシュ通知は、INBOXがWebpushプロトコルを使用して、Webpushエンドポイントに通知を送信する。  
メール通知は、WEKO3に実装されているメール送信機能を使用して、ユーザーのメールアドレスに通知を送信する。

### データベース

WEKO3はPostgreSQL、INBOXはMongoDBを使用する。  
両者は、HTTP通信を介して連携するため、データベースの直接的な連携は行わない。

WEKO3は以下の情報を永続化する。

- ユーザーの購読情報
  - ユーザーID
  - ユーザープロフィールID
  - メール通知購読の有無

INBOXは以下の情報を永続化する。RDBではないため、カラムを記しているわけではない。  

- ユーザーの購読情報
  - ユーザーID
  - 言語
  - 購読情報（Webhook エンドポイント、認証鍵）

  ユーザーの購読情報とは、Webプッシュ通知を送信するためのエンドポイントや認証鍵などの情報を指す。  
  ユーザーが複数の端末で通知を受け取ることを想定し、ユーザーIDに対して複数の購読情報を持つことができるようにする。  

- 通知内容(LDN形式)
  - 通知ID
  - 通知の種類
  - 通知の対象
  - 通知の発行元
  - 通知の宛先
  - 通知の文脈

  通知内容を永続化することで、通知の二次利用を可能にする。

- 通知ステータス
  - 未読/既読

  主に二次利用のために、通知が読まれたかどうかを管理する。

- 通知のテンプレート
  - 通知の種類
  - 通知の言語
  - 通知のタイトルテンプレート
  - 通知のテンプレート

  通知のテンプレートを永続化することで、通知のタイトル・本文を動的に生成する。

### 通知生成

アイテム登録完了などのイベントが発生した際、アイテムIDやアイテム詳細画面のURL、登録者や承認者の情報などを通知パラメータとして生成する。  
このパラメータをもとにCoarNotifyに基づいたLDN形式の通知を作成し、INBOXに送信する。

### 通知の種類

LDNには通知のシナリオに応じてタイプがあり、WEKO3では以下の通りに割り当てる。

**タイプ**
- `Accept,coar-notify:ReviewAction`
- `Reject`
- `TentativeAccept`
- `TentativeReject`
- `Announce`
- `Announce,coar-notify:EndorsementAction`
- `Announce,coar-notify:IngestAction`
- `Announce,coar-notify:RelationshipAction`
- `Announce,coar-notify:ReviewAction`
- `Offer,coar-notify:EndorsementAction`
- `Offer,coar-notify:IngestAction`
- `Offer,coar-notify:ReviewAction`
- `Undo`

**シナリオ**

- アイテムの登録完了時：`Announce,coar-notify:IngestAction`
- アイテム承認リクエスト： `Offer,coar-notify:EndorsementAction`
- アイテム登録承認： `Announce,coar-notify:EndorsementAction`
- アイテム登録拒否： `Reject`

### 通知先の選定

通知の宛先に対応する購読情報が存在する場合、通知の本文を生成し送信する。

### タイトル・本文の動的生成

あらかじめプレースホルダを埋め込んた通知のテンプレートを用意する。  
通知の送信時にプレースホルダをLDNから取り出したパラメータで置換することで、通知する前に内容を動的に生成する。  
使用するテンプレートの言語は、プッシュ通知の場合はユーザープロフィールの設定値を使用する。  
ユーザープロフィールが変更された時、INBOXに通知を送信して、購読情報を更新する。

二次利用時はリクエストの`Accept-Language`ヘッダに基づいて選択する。  
選択された言語のテンプレートが存在しない場合、英語のテンプレートを使用する。

```python
>>> template = 'Your item "{{ object_name }}" has been registered.'
>>> body = template.replace("{{ ", "{").replace(" }}", "}").format(object_name=object_name)
'Your item "Sample Journal" has been registered.'
```

**利用可能なプレースホルダ**
- `{{ timestamp }}`: 通知の発行日時（ISO8601形式）
- `{{ object_name }}`: アイテムのタイトル
- `{{ object_uri }}`: アイテム詳細画面のURL
- `{{ context_uri }}`: アクティビティ詳細画面のURL
- `{{ actor_name }}`: 操作者の表示名
- `{{ target_name }}`: 受信者の表示名

### 通知の送信

Webpush APIを使用してユーザーの購読情報に基づき生成された通知内容をエンドポイントに送信する。  
エンドポイントが無効になっていることによってエラーとなった場合、購読情報を削除する。

### 通知の永続化

  通知はLDN形式のBSONで永続化される。  
  JSONとは異なりバイナリであり、日付やオブジェクトを含むことができる。


### その他

- 通知にユーザーの名前を含める必要がある場合、ユーザープロフィールのユーザー名（displayname）を使用する。
- 通知に含む時刻は、かならずタイムゾーンを含める。これは、ISO8601(RFC3339)形式で記述する。
- 外部サービスやユーザーが受信ボックスのURLを知るためには、一度WEKO側のトップページのエンドポイント("/")にアクセスする。  
  トップページはHEADリクエストに対して、レスポンスにLinkヘッダで受信ボックスのURIを含めるようにする。

  ```
  Link: <https://example.repo.nii.ac.jp/inbox>; rel="http://www.w3.org/ns/ldp#inbox"
  ```

  参考: [Coar Notify: Discovery](https://coar-notify.net/guide/discovery/)

## 開発環境の構築
weko のプロジェクト直下に index ディレクトリがあり、 INBOX 用の Dockerfile を配置している。  
普段はこの Dockerfile を使って、INBOX のイメージをビルドする。

INBOX の開発時は、あらかじめinbox ディレクトリにリポジトリをクローンしておき、Dockerfile.dev を使う。  
このとき、docker-compose.yml を

```diff
  inbox:
    restart: "always"
    build:
      context: ./inbox
-     dockerfile: Dockerfile
+     dockerfile: Dockerfile.dev
    ports:
      - "8080:8080"
    environment:
      - MONGO_DB_URI=mongodb://inbox:ibpass123@mongo:27017
      - ON_RECEIVE_NOTIFICATION_WEBHOOK_URL=""
      - ALLOWED_ADMIN_ORIGINS=["*"]
      - ALLOWED_ORIGINS=["*"]
    links:
      - mongo
+   volumes:
+     - ./inbox:/app
```

として、ホットリロードを有効にする。


## 関連モジュール

- WEKO3
    - weko-notifications：通知生成、送信、取得のコア機能、ユーザーによる購読設定画面を提供する
    - weko-workflow：アクティビティの進行に応じて通知を生成する
    - weko-swordserver：SWORDv3プロトコルを使用したアイテム登録・更新・削除の際に通知を生成する

- INBOX
    - [coar-notify-inbox (nii_main)](https://github.com/RCOSDP/coar-notify-inbox)

## 変更履歴

| 日付       | GitHubコミットID                           | 更新内容                                        |
| ---------- | ------------------------------------------ | ----------------------------------------------- |
| 2025/03/17 |                                            | 初版作成                                        |
| 2025/06/09 | c6cf6e817c99bdb58acd33cb9d9cc06c5f73cabf   | 通知の購読設定画面の画像を追加                  |
