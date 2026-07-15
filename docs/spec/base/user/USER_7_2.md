### 言語切替

#### 目的・用途

本機能は、ユーザーの操作によって表示言語を切り替えられるようにする機能である。

#### 利用方法

画面のヘッダ部分にある表示言語切替のプルダウンを操作する。

または、「[トップページURL]/accounts/settings/lang/<lang_code>」のURLでアクセスする。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○ | ○ | ○ | ○ |

#### 機能内容

- ユーザー画面のヘッダ部分に表示言語切替のプルダウンを設ける

  - 選択肢は、【Administration > 設定（Setting） > 言語表示（Language）画面】での「登録言語」に指定されている言語一覧である

  - 「登録言語」に1番上の言語はデフォルト言語とする

  - 選択している言語に対応がない場合、表示言語は英語とする

  - 詳細は[ADMIN-14-3: 言語表示](\\l)参照。

- URLを用いて本機能を利用する場合、【Administration > 設定（Setting） > 言語表示（Language）画面】に表示されている言語なら「登録言語」に指定されていない言語でも利用可能

- URLに ?next=<リダイレクト先のパス> を付加することで、直接言語のページに遷移することができる

  - 例：[トップページURL]/accounts/settings/lang/en?next=/workflow/

#### 関連モジュール

- weko-admin

#### 処理概要

weko_admin.views.custom_set_lang（blueprint prefix `/accounts/settings`）にて、<lang_code> で指定された言語コードが登録言語（model AdminLangSettings）に合致した場合、その言語が選択されたことをSessionに保存して言語切替を行ったページにリダイレクトしている。

- 保存先のSessionは、session[current_app.config["I18N_SESSION_KEY"]]である。

- コンフィグI18N_SESSION_KEYのデフォルト値は"language"である。

登録言語に無い言語コードが指定された場合は、GET では 404、POST では 400 を返す。

## 実装補足（v2.0.2 実装との突き合わせ）

- 実装補足：言語切替の実ルートは `/accounts/settings/lang/<lang_code>`（`weko_admin.views.custom_set_lang`、blueprint prefix `/accounts/settings`）。無効な言語コードは GET で 404 / POST で 400。セッション保存は `session[I18N_SESSION_KEY]`、`?next=` でリダイレクト。登録言語は model `AdminLangSettings`（table `admin_lang_settings`）、既定言語は `weko_admin.ext.set_default_language`。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
