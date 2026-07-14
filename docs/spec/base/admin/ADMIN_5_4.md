#### 外部著者ID Prefix

## 目的・用途

本機能は、登録済みの作成者識別子の編集や、新たな作成者識別子を追加するための機能である。

## 利用方法

【Administration>著者DB管理（Author Management）>編集（Edit）】の順で編集画面に遷移し、ID Prefixタブを押下する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | サブリポジトリ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | ○ | ○※ | | | |

※サブリポジトリ管理者の場合は管理するコミュニティに紐づく作成者識別子のみ編集可能

## 機能内容

- 【Administration>著者DB管理（Author Management）>編集（Edit）】での「ID Prefix」タブに登録されている外部著者ID Prefix一覧が表示される。
  - 表示項目は以下の通りである。
    - 「作成者識別子（Name）」：ID Prefixの名前が表示される。
    - 「IDスキーマ名（Scheme）」：ID PrefixのSchemeが表示される。
    - 「URL」：ID PrefixのURLが表示される。
    - 「コミュニティ（Community）」：ID Prefixを管理するコミュニティが表示される。
    - 「コントロール（Control）」：コントロールのボタンが表示される。  
      コントロールのボタンは［編集（Edit）］、［追加（Add）］である。  
      コミュニティ管理者の場合、管理対象外のコミュニティに紐づくID Prefixの［編集（Edit）］ボタンは非活性表示される。
  - クリーンビルド環境での初期設定値は以下の通りである。
    - WEKO
    - ORCID (URL: https://orcid.org/##)
    - CiNii (URL: https://ci.nii.ac.jp/author/##)
    - KAKEN2 (URL: https://kaken.nii.ac.jp/nrid/##)
    - ROR（URL: https://ror.org/##）
- 外部著者ID Prefixを追加するため、ID Prefix一覧での1番下の行に入力エリアを設ける。
  - 入力項目は以下の通りである。
    - 「作成者識別子（Name）」テキストボックス：ID Prefixの名前を入力する。
    - 「IDスキーマ名（Scheme）」プルダウン：ID PrefixのSchemeを選択する。
      - 選択肢はJPCOARスキーマの「nameIdentifierScheme」属性の統制語彙＋「Other」とする。
        - 「Other」を選択した際は「Scheme」の内容を手入力させ、登録完了後は手入力した文字列が表示される。
      - 設定値はユニークである。
    - 「URL」テキストボックス：選択しているSchemeに応じるURLを入力する。
      - 入力しているURL形式をチェックする必要がある。
      - URLについて、URLの末尾に「##」を入れることができる。
        - 「##」が含まれている場合、「ID Prefix」のURLを使用している時、「##」を入力されたIDに置換してURLとする。
      - 「##」が含まれていない場合、そのまま設定されたURLとする。
    - 「コミュニティ（Commmunity）」プルダウン：ID Prefixを管理するコミュニティを選択する。
      - 「コミュニティ管理」画面で登録されたコミュニティを選択肢とする。
      - コミュニティ管理者の場合、管理対象外のコミュニティは選択できない。
      - 複数選択が可能。
  - [追加（Add）」ボタンを押すと、入力内容をチェックする。
    - 問題があれば、外部著者ID Prefixを追加せず、エラーメッセージを表示する。
      - 何かの項目を入力しない場合、またはURL形式が不正場合は以下のメッセージを表示する。  
        エラーメッセージ：「Please enter the correct ＋　項目名」
      - 設定されたSchemeを選択する場合は以下のメッセージを表示する。  
        エラーメッセージ：「Specified scheme is already exist.」
      - コミュニティ管理者が管理対象外のコミュニティを選択した場合は以下のメッセージを表示する。  
        エラーメッセージ：「You do not have permission for this ID Prefix’s communities: {1}.」  
        ※ {1}: 該当コミュニティのID
      - コミュニティ管理者が自身の管理するコミュニティを一つも選択しない場合以下のメッセージを表示する。  
        エラーメッセージ：「You must include at least one managed community.」
    - 問題なければ、外部著者ID Prefixを追加し、以下のメッセージを表示する。  
      メッセージ：「Successfully added」
  - ID Prefix行の[編集（Edit）]ボタンを押すと、該当の外部著者ID Prefix情報を編集可能とし、コントロールのボタンを該当行の直下に表示する。  
    コントロールのボタン：[保存 （Save）」、[キャンセル（Cancel）]、[削除（Delete）]
    - 該当の外部著者ID Prefix情報を編集してから、[保存 （Save）]ボタンを押すと、編集内容を保存し、以下のメッセージを表示する。  
      メッセージ：「Update completed」
    - [削除（Delete）]ボタンを押すと、該当の外部著者ID Prefixを削除し、以下のメッセージを表示する  
      メッセージ：「Successfully deleted」
      - コミュニティ管理者が管理対象外のコミュニティに紐づくID Prefixを削除しようとした場合、ID Prefixを削除せず、以下のエラーメッセージを表示する。  
        エラーメッセージ：「You do not have permission for this ID Prefix’s communities: {1}.」  
        ※ {1}: 該当コミュニティのID
    - [キャンセル（Cancel）]ボタンを押すと、編集前の状態に戻る。
  - 作成者識別子”WEKO” には[編集（Edit）]ボタンは表示しない。（WEKO3の著者IDは一意に決められる値であるため編集できないようにする）

## 関連モジュール

- weko-authors

## 処理概要

IDスキーマ名（Scheme）プルダウンに表示するScheme一覧を設定する

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L25>
- 設定キー：WEKO_AUTHORS_LIST_SCHEME
- 現在の設定値：`WEKO_AUTHORS_LIST_SCHEME = ['e-Rad', 'NRID', 'ORCID', 'ISNI', 'VIAF', 'AID', 'kakenhi', 'Ringgold', 'GRID', 'ROR', 'e-Rad_Researcher', 'researchmap', 'Other']`

インデックスを設定する

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L29>
- 設定キー：WEKO_AUTHORS_INDEX_ITEM_OTHER
- 現在の設定値：`WEKO_AUTHORS_INDEX_ITEM_OTHER = 12`

ID Prefix画面のテンプレートを設定する

- パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-authors/weko_authors/config.py#L48>
- 設定キー：WEKO_AUTHORS_ADMIN_PREFIX_TEMPLATE
- 現在の設定値：`WEKO_AUTHORS_ADMIN_PREFIX_TEMPLATE = 'weko_authors/admin/prefix_list.html'`

- 【Administration>著者DB管理(Author Management)>編集(edit)】からID Prefixタブ押下で遷移する初期画面は、ID Prefix押下時にweko_authors.views.get_prefix_listが呼び出され、db内のauthors_prefix_settingsテーブルの情報が取り出されて表示される。
- 編集時は、[編集（Edit）]ボタンを押下することで編集が可能となり、内容の変更後に[保存(Save)]ボタンを押すことで、weko_authors.views.update_prefixが呼び出されて、db内のauthors_prefix_settingsテーブルの情報が更新される。
- 削除時は、[編集（Edit）]ボタン押下後に出現する[削除（Delete）]ボタンを押下することで、weko_authors.views.delete_prefixが呼び出され、db内のauthors_prefix_settingsテーブルから削除対象が削除される。
- 追加時は、追加したい情報を最下部のテキストボックスに入力後に[追加（Add）]ボタンを押すことで、weko_authors.views.create_prefixが呼び出され、db内のauthors_prefix_settingsテーブル内に情報が追加される。
- 外部著者ID Prefixとコミュニティとの関連付けは、中間テーブル`author_prefix_community_relations`により多対多の関係で管理される。各操作時には、ログインユーザーが所属するコミュニティに紐づくPrefixのみを対象として処理が行われる。

## 実装補足（v2.0.2 実装との突き合わせ）

- 画面/ハンドラ：`weko_authors.views`（`/authors/search_prefix`（GET）,`/edit_prefix`（POST）,`/delete_prefix/<id>`（DELETE）,`/add_prefix`（PUT））。テーブル `authors_prefix_settings`（`AuthorsPrefixSettings`）＋中間 `author_prefix_community_relations`。scheme は一意制約。URL の `#` は識別子で置換（`views.mapping`）。WEKO（idType=1）は編集不可。
- config：`WEKO_AUTHORS_LIST_SCHEME` は `e-Rad_Researcher` と `researchmap` を含む全13件、`WEKO_AUTHORS_INDEX_ITEM_OTHER` は `12`。

## 更新履歴

|日付|GitHubコミットID|更新内容|
|:---:|:---:|:---:|
|2023/08/31|353ba1deb094af5056a58bb40f07596b8e95a562|初版作成|
|2025/01/23|-|サブリポジトリ対応|
