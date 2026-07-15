#### ADMIN-5-1-3:Affiliation ID

## 目的・用途

本機能は、登録済みの所属機関識別子の編集や、新たな所属機関識別子を追加するための機能である。

## 利用方法

【Administration>著者DB管理（Author Management）>編集（Edit）】の順で編集画面に遷移し、Affiliation　IDタブを押下する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○※ | | | |

※サブリポジトリ管理者の場合は管理するコミュニティに紐づく所属機関識別子のみ編集可能

## 機能内容

- 【Administration>著者DB管理（Author Management）>編集（Edit）】でのAffiliation IDタブに登録されている所属機関識別子一覧が表示される。
  - 表示項目は以下の通りである。
    - 「所属機関識別子（Name）」：所属機関の名前が表示される。
    - 「IDスキーマ名（Scheme）」：所属機関のSchemeが表示される。
    - 「URL」：所属機関のURLが表示される。
    - 「コミュニティ（Community）」：所属機関を管理するコミュニティが表示される。
    - 「コントロール（Control）」：コントロールのボタンが表示される。  
      コントロールのボタンは［編集（Edit）］、［追加（Add）］である。  
      コミュニティ管理者の場合、管理対象外のコミュニティに紐づく所属機関の［編集（Edit）］ボタンは非活性表示される。
  - クリーンビルド環境での初期設定値は以下の通りである。
    - ISNI (URL: https://www.isni.org/isni/##)
    - GRID(URL: https://www.grid.ac/institutes/##)
    - Ringgold
    - Kakenhi
    - ROR
  - [追加（Add）]ボタンを押すと、入力内容をチェックする。
    - 問題があれば、Affiliation IDを追加せず、エラーメッセージを表示する。
      - 何かの項目を入力しない場合、またはURL形式が不正場合は以下のメッセージを表示する。  
        エラーメッセージ：「Please enter the correct ＋　項目名」
      - 設定されたSchemeを選択する場合は以下のメッセージを表示する。  
        エラーメッセージ：「Specified scheme is already exist.」
      - コミュニティ管理者が管理対象外のコミュニティを選択した場合は以下のメッセージを表示する。  
        エラーメッセージ：「You do not have permission for this Affiliation ID’s communities: {1}.」  
        ※ {1}: 該当コミュニティのID
      - コミュニティ管理者が自身の管理するコミュニティを一つも選択しない場合以下のメッセージを表示する。  
        エラーメッセージ：「You must include at least one managed community.」
    - 問題なければ、Affiliation IDを追加し、以下のメッセージを表示する。  
      メッセージ：「Successfully added」
  - [編集（Edit）]ボタンを押すと、該当のAffiliation ID情報を編集可能とし、コントロールのボタンを該当行の直下に表示する。  
    コントロールのボタン：[保存 （Save）」、[キャンセル（Cancel）]、[削除（Delete）]
    - 該当のAffiliation ID情報を編集してから、[保存 （Save）]ボタンを押すと、編集内容を保存し、以下のメッセージを表示する。  
      メッセージ：「Update completed」
    - [削除（Delete）]ボタンを押すと、該当のAffiliation IDを削除し、以下のメッセージを表示する  
      メッセージ：「Successfully deleted」
      - コミュニティ管理者が管理対象外のコミュニティに紐づくID Prefixを削除しようとした場合、Affiliation IDを削除せず、以下のエラーメッセージを表示する。  
        エラーメッセージ：「You do not have permission for this Affiliation ID’s communities: {1}.」  
        ※ {1}: 該当コミュニティのID
    - [キャンセル（Cancel）]ボタンを押すと、編集前の状態に戻る。

## 関連モジュール

- weko-authors

## 処理概要

IDスキーマ名（Scheme）プルダウンに表示するScheme一覧の設定をする。

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L32>
- 設定キー：WEKO_AUTHORS_LIST_SCHEME_AFFILIATION
- 現在の設定値：`WEKO_AUTHORS_LIST_SCHEME_AFFILIATION = ['ISNI', 'GRID', 'Ringgold', 'kakenhi', 'ROR', 'Other']`

「Other」のインデックスを設定する。

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L36>
- 設定キー：WEKO_AUTHORS_AFFILIATION_IDENTIFIER_ITEM_OTHER
- 現在の設定値：`WEKO_AUTHORS_AFFILIATION_IDENTIFIER_ITEM_OTHER = 5`

Affiliation ID画面のテンプレートを設定する。

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L51>
- 設定キー：WEKO_AUTHORS_ADMIN_AFFILIATION_TEMPLATE
- 現在の設定値：`WEKO_AUTHORS_ADMIN_AFFILIATION_TEMPLATE = 'weko_authors/admin/affiliation_list.html'`

- 【Administration>著者DB管理(Author Management)>編集(edit)】からAffiliation IDタブ押下で遷移する初期画面は、Affiliation IDタブ押下時にweko_authors.views.get_affiliation_listが呼び出され、db内のauthors_affiliation_settingsテーブルの情報が取り出されて表示される。
- 編集時は、[編集（Edit）]ボタンを押下することで編集が可能となり、内容の変更後に[保存(Save)]ボタンを押すことで、weko_authors.views.update_affiliationが呼び出されて、db内のauthors_affiliation_settingsテーブルの情報が更新される。
- 削除時は、[編集（Edit）]ボタン押下後に出現する[削除（Delete）]ボタンを押下することで、weko_authors.views.delete_affiliationが呼び出され、db内のauthors_affiliation_settingsテーブルから削除対象が削除される。
- 追加時は、追加したい情報を最下部のテキストボックスに入力後に[追加（Add）]ボタンを押すことで、weko_authors.views.create_affiliationが呼び出され、db内のauthors_affiliation_settingsテーブル内に情報が追加される。
- Affiliation IDとコミュニティとの関連付けは、中間テーブル`author_affiliation_community_relations`により多対多の関係で管理される。各操作時には、ログインユーザーが所属するコミュニティに紐づくAffiliation IDのみを対象として処理が行われる。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_authors.views`（`/authors/search_affiliation`（GET）,`/edit_affiliation`（POST）,`/delete_affiliation/<id>`（DELETE）,`/add_affiliation`（PUT））。テーブル `authors_affiliation_settings`（`AuthorsAffiliationSettings`）＋中間 `author_affiliation_community_relations`。テンプレート `WEKO_AUTHORS_ADMIN_AFFILIATION_TEMPLATE`。
- config：`WEKO_AUTHORS_LIST_SCHEME_AFFILIATION` は `['ISNI','GRID','Ringgold','kakenhi','ROR','Other']`、`WEKO_AUTHORS_AFFILIATION_IDENTIFIER_ITEM_OTHER` は `5`。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2025/01/23|-|サブリポジトリ対応|
