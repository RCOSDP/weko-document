### Cookie使用確認画面表示

#### 目的・用途

ユーザに対してCookie利用の確認を行う。

#### 利用方法

画面フッタの「Change consent settings」をクリックすると、Cookie利用の同意画面が表示される。

ユーザはCookie利用の同意画面にて、同意することで、Cookieを利用したサービスを利用できるようになる。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

#### 機能内容

- コンフィグで機能が有効化されているとき、画面フッタに「Change consent settings」が表示される。これをクリックすると、Cookie利用の同意画面がポップアップで表示される。

- Addthis および Google Analystics の利用について、Cookie利用の同意をとることで利用可能とする。

- Googleアナリティクス(システム)については、サービス利用の必須としている。

#### 関連モジュール

- weko-theme

#### 処理概要

- Cookie利用の同意画面は、Klaro ( https://github.com/kiprotect/klaro ) ライブラリを利用して作成している。

- 本機能の有効化を設定するコンフィグは、instance.cfgまたはweko-themeのconfig.pyで設定する。両方で設定されている場合、instance.cfgの設定が優先される。

  - パス（instance.cfg）：  
    https://github.com/RCOSDP/weko/blob/v0.9.22/scripts/instance.cfg

  - パス（config.py）：  
    https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-theme/weko_theme/config.py

- ENABLE_COOKIE_CONSENT = True の場合に機能が有効となる。

- 「Change consent settings」は、コンフィグで機能が有効化されているときのみ表示されるようにテンプレートで制御されている。

## 実装補足（v2.0.2 実装との突き合わせ）

- 有効化 config は `ENABLE_COOKIE_CONSENT`（`weko_theme`、既定 False。`weko_theme.ext` で登録）。同意UIは Klaro（v0.7.16）を `base.html` で使用。
- 実装補足（訂正）：同意で制御される任意サービスは AddThis ではなく Facebook と X(Twitter)（＋必須の Google Analytics）。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
