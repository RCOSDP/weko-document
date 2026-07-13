### ユーザープロファイル設定

#### 目的・用途

本機能は、ユーザーとして、ユーザープロファイルを閲覧・編集できる機能である。

#### 利用方法

画面ヘッダで、ログインユーザのメールアドレスが表示されている部分またはその右側の［▼］ボタンをクリックすると、【プロフィール（Profile）画面】に遷移する。画面上で操作を行う。

#### 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
| --- | --- | --- | --- | --- | --- | --- |
| 利用可否 | ○ | ○ | ○ | ○ | ○ |  |

#### 機能内容

1. ユーザープロファイルを閲覧・編集する

- 【プロフィール（Profile）画面】にユーザーの情報を管理する

  - 表示項目は以下の通りである

    - ［確認メールを再送（Resend verification email）］ボタン  
      ボタンを押すと、確認メールを再送信し、メッセージを画面上部に表示する  
      メッセージ：  
      　日本語：「確認メールを送信しました」  
      　英語：「Verification email sent.」

    - 「ユーザー名」（Username）：必須項目

      - 入力必須は「ユーザー名」（Username）テキストボックスの下に表示する  
        日本語：「ユーザー名は3文字以上を指定してください(英数字, ハイフン, アンダーバーのみ使用可能)は入力必須です」  
        英語：「Required. Username must start with a letter, be at least three characters long and only contain alphanumeric characters, dashes and underscores.」

    - 「タイムゾーン」（Timezone）  
      デフォルト値：「(GMT+9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk」

    - 「言語」（Language）  
      選択肢：「自動」（Automatic）、「日本語」（Japanese）、「英語」（English）  
      デフォルト値：日本語

    - 「メールアドレス」（Email address）

    - 「メールアドレスの再入力」（Re-enter email address）

    - 「access key」

    - 「secret key」

    - 「endpoint url」

    - 「region name」

    ※以下、管理者画面のプロフィール設定編集画面の操作により表示される項目

    | 項目名 | 初期ラベル名 | 初期表示設定 |
    | -------------- | ------------------- | ------------ |
    | fullname       | 氏名                | True         |
    | university     | 大学・機関         | True         |
    | department     | 所属部局・部署      | True         |
    | position       | 役職                | True         |
    | item1          | 役職（その他）      | True         |
    | item2          | 電話番号            | True         |
    | item3          | 所属学会名          | True         |
    | item4          | 所属学会役職        | True         |
    | item5          | 所属学会名          | True         |
    | item6          | 所属学会役職        | True         |
    | item7          | 所属学会名          | True         |
    | item8          | 所属学会役職        | True         |
    | item9          | 所属学会名          | True         |
    | item10         | 所属学会役職        | True         |
    | item11         | 所属学会名          | True         |
    | item12         | 所属学会役職        | True         |
    | item13         | item13              | False        |
    | item14         | item14              | False        |
    | item15         | item15              | False        |
    | item16         | item16              | False        |

  - ［Update Profile］ボタンを押すと、設定内容をチェックし、エラーがない場合、設定内容を保存する

    - 「メールアドレス」を変更する場合、変更されたメールアドレスに確認メールを送信し、メッセージを画面上部に表示する  
      メッセージ：  
      　日本語：「プロフィールを更新しました+「メールアドレス」+に確認メールを送信しましたので、ご確認ください」  
      　英語：「Profile was updated. We have sent a verification email to + 「email address」 +. Please check it.」

    - 「メールアドレス」を変更しない場合、以下のメッセージを画面上部に表示する  
      メッセージ：  
      　日本語：「プロフィールを更新しました」  
      　英語：「Profile was updated.」

  - エラーメッセージは以下の通りである

    - 「ユーザー名」（Username）を指定しない場合、エラーメッセージを「ユーザー名」（Username）エリアの下に表示する  
      メッセージ：  
      　日本語：「ユーザー名を入力してください」  
      　英語：「Please input username」

    - フォーマットのチェックによるエラーメッセージが以下のように定義されているが、v0.9.22ではチェックメソッドを呼び出していないため表示されることはない

    - 指定している「ユーザー名」（Username）のフォーマットが不正の場合、エラーメッセージを「ユーザー名」（Username）エリアの下に表示する  
      メッセージ：  
      　日本語：「ユーザー名は3文字以上を指定してください(英数字, ハイフン, アンダーバーのみ使用可能)」  
      　英語：「Username must start with a letter, be at least three characters long and only contain alphanumeric characters, dashes and underscores.」

    - 管理者画面にて入力方法が「phoneNumber」に設定されている項目のフォーマットが以下の条件の場合、エラーメッセージを項目エリアの下に表示する。  
      条件：入力文字数が15文字を超える場合。  
      メッセージ：  
      英語：「Phone number must be less than 15 characters.」

    - 管理者画面にて入力方法が「position(other)」に設定されている項目のフォーマットが以下の条件の場合、エラーメッセージを項目エリアの下に表示する。  
      項目「position」の値が「その他」もしくは「Others」以外の時に「item1」項目に入力し保存を行った場合  
      メッセージ：  
      日本語「役職が入力されています（「その他」選択時のみ入力可能）」  
      英語：「Position is being inputted (Only input when selecting 'Others')」

    - 管理者画面にて入力方法が「identifier」に設定されている項目のフォーマットが不正の場合、エラーメッセージを項目エリアの下に表示する。  
      メッセージ：Only digits are allowed.

  - 「キャンセル」（Cancel）ボタンを押すと、プロフィール画面に再度遷移することで設定内容をリセットする

  - この画面では「ユーザー名」（Username）は入力必須だが、データベース上は必須ではない。空にする場合は、管理者機能で設定する。（[ADMIN-13-12: ユーザープロファイル](../admin/ADMIN_13_12.md)を参照）

#### 関連モジュール

- weko-user-profiles

#### 処理概要

プロフィール入力フォームとその入力内容チェックは、以下で定義している。

- パス：  
  <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-user-profiles/weko_user_profiles/forms.py>

- ProfileFormクラスの内容を、テンプレートprofile.htmlに設定している。

［Update Profile］ボタンを押すと、リクエストペイロードにsubmit: profileを含むaccount/settings/profile/ リクエストがPOSTされる。

- これによって、weko_user_profiles.views.profileメソッドが呼び出される。この中でhandle_profile_formメソッドを呼び出してユーザープロファイルを更新する。

プロフィールの設定は、userprofiles_userprofileテーブルに保存される。

- ユーザー名（Username）はdisplaynameカラムに保存される。

- タイムゾーン（Timezone）はtimezoneカラムに保存される。

- 言語（Language）はlanguageカラムに保存される。

- access key はaccess_keyカラムに保存される。

- secret key はsecret_keyカラムに保存される。

- endpoint url はs3_endpoint_urlカラムに保存される。

- region name はs3_region_nameカラムに保存される。

- fullnameはfullnameカラムに保存される。

- universityはuniversityカラムに保存される。

- departmentはdepartmentカラムに保存される。

- positionはpositionカラムに保存される。

- item1はotherPositionカラムに保存される。

- item2はphoneNumberカラムに保存される。

- item3はinstituteNameカラムに保存される。

- item4はinstitutePositionカラムに保存される。

- item5はinstituteName2カラムに保存される。

- item6はinstitutePosition2カラムに保存される。

- item7はinstituteName3カラムに保存される。

- item8はinstitutePosition3カラムに保存される。

- item9はinstituteName4カラムに保存される。

- item10はinstitutePosition4カラムに保存される。

- item11はinstituteName5カラムに保存される。

- item12はinstitutePosition5カラムに保存される。

- item13はitem13カラムに保存される。

- item14はitem14カラムに保存される。

- item15はitem15カラムに保存される。

- item16はitem16カラムに保存される。

メールアドレスの変更は、flask_loginのグローバル変数current_user.emailを更新することで保存される。

#### 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| --- | --- | --- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2024/10/18 | 6bf785b2956fb19773f22681db7080425c5544f2 | プロフィール設定編集機能追加 |
