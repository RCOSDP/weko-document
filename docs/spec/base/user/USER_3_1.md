
### メタデータ表示

  - > 目的・用途

本機能は、登録されたアイテムの詳細情報を閲覧できる機能である。

  - > 利用方法

アイテムのメタデータは、アイテムリストにおいて表示されているアイテムを押下することで表示される。

  - > 利用可能なロール

<table>
<thead>
<tr class="header">
<th>ロール</th>
<th>システム<br />
管理者</th>
<th>リポジトリ<br />
管理者</th>
<th>コミュニティ<br />
管理者</th>
<th>登録ユーザー</th>
<th>一般ユーザー</th>
<th>ゲスト<br />
(未ログイン)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>利用可否</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
<td>○</td>
</tr>
</tbody>
</table>

  - > 機能内容

1\. アイテムの詳細情報を表示する。

  - アイテムの詳細画面について、メタデータの表示を階層表示とする。
    
      - 表を階層ごとに分ける。
    
      - 階層表示は、アイテムタイプ設定における「プロパティの階層構造」に基づくものとする。

  - アイテム詳細画面のメタデータのラベルが複数言語表示される
    
      - ラベルの表示を、【Administration \> アイテムタイプ管理(ItemTypes) \>メタデータ (Metadata) 画面】の 「Localization Settings」 での「Japanese」/「English」テキストボックスに設定する。

  - アイテムの詳細画面での作成者について表示する。
    
      - アイテムの詳細画面に作成者の氏名リンクを以下の優先順位で表示する。
        
          - 言語の優先順位  
            1.1 UI表示言語に一致した言語の値  
            1.2 1.1が無い場合、入力順で最初に入力された言語の値
        
          - アイテムリストに表示される作成者について、画面表示と同じ言語の姓名を表示する。表示する姓名は、「Web画面の表示言語＞英語＞アイテム登録時の１つ目の言語＞言語無しで登録した時の１つ目の値」の表示順に従う。
        
          - 言語はアイテムリストには表示しない。
        
          - 姓、または名のみのフィールドを入力していた場合も同様に、「Web画面の表示言語＞英語＞アイテム登録時の１つ目の言語＞言語無しで登録した時の１つ目の値」の表示順に従って表示する。
        
          - 【Administration \> アイテムタイプ管理(ItemTypes) \> メタデータ (Metadata) 画面】の言語のサブプロパティの"Show List"のチェックを非活性とする。
        
          - 作成者の「姓名」「姓」「名」「別名」  
            1.1 作成者姓名  
            1.2 作成者姓  
            1.3 作成者名  
            1.4 作成者別名
    
      - 作成者の氏名リンクを押すと、作成者の詳細情報をフォームで表示する。
        
          - フォームのテンプレートを以下の通りである。

> \[タイトル\]
> 
> \[作成者識別子Scheme\] \[作成者識別子(作成者識別子URIのリンクを付く)\]
> 
> \[言語\]　\[作成者姓名\]
> 
> 　　　　\[作成者別名\]
> 
> 　　　　\[所属機関識別子Scheme\] \[所属機関識名\] \[所属機関識別子(所属機関識別子URIのリンクを付く)\]
> 
> \[リポジトリを検索する\]リンク

  - 説明
    
      - \[タイトル\]  
        作成者の氏名リンク
    
      - \[作成者識別子\]  
        作成者識別子の情報をまとめる。
    
      - \[作成者の情報\]
    
      - 言語のごとに氏名、所属項目をまとめる。  
        ・言語の表示順位に対して、システム言語設定順で言語を並べる。  
        ・ja-kanaがある場合、jaの直下に配置する。  
        ・言語がない場合、フォームの下部に配置する。
        
          - \[作成者姓名\]  
            同一言語で「姓名」が入力されている場合、「姓」「名」が表示されない。
    
      - \[リポジトリを検索する\]リンク  
        リンクを押すと、該当作成者名を条件とし、アイテム検索を実施する。

<!-- end list -->

  - アイテムの詳細画面での書誌情報について以下のようなテンプレートで表示する。
    
      - テンプレート

> \[言語\] : \[タイトル\]
> 
> 巻 {xxx}, 号 {xxx}, p. {開始ページ}-{終了ページ}, ページ数 {xxx}, 発行年 {YYYY-MM-DD} {YYYY-MM-DD}　（日本語の場合）
> 
> Volume {xxx}, Issue {xxx}, p. {開始ページ}-{終了ページ}, Number of Pages {xxx}, Issued Date {YYYY-MM-DD} {YYYY-MM-DD}　（英語の場合）

  - 注意
    
      - 画面表示の多言語化に対応できる。
    
      - \[XX\]がNull（空値）の場合は、「巻 \[XX\]」の部分をまるごと表示しない。
    
      - 終了ページ（\[EP\]）がNull（空値）の場合は、「-」を表示しない。
    
      - 書誌情報プロパティの情報は、以下の表示順に従う。
        
          - 雑誌名は「雑誌名, 」で１つのみ表示する。表示する雑誌名は、「Web画面の表示言語＞英語＞アイテム登録時の１つ目の言語＞言語無しで登録した時の１つ目の値」の表示順に従って表示する。
    
      - 言語はアイテムリストには表示しない。
    
      - 【Administration \> アイテムタイプ管理(ItemTypes) \> メタデータ (Metadata) 画面】の言語のサブプロパティの"Show List"のチェックを非活性とする。

2 Permalink欄の表示について

  - アイテム詳細画面にPermalinkをラベル無しで表示する。

  - DOI \> CNRIハンドル \> URI（https://FQDN/records/\*\*\*\*）の優先順位で表示する。

  - 表示を切り替えるタイミングは、DOI付与申請を含むワークフローが完了したタイミングとする。

  - Yハンドルは表示しない。

3\. アイテムの更新・削除操作

  - 登録者，またはリポジトリ管理者以上でログインしている場合、アイテムの「公開」または「非公開」を選択できる。

  - アイテムにDOIが付与されている場合、「公開」から「非公開」への変更を認めない。  
    　日本語：アイテムにDOIが付与されているため、アイテムを非公開にすることはできません。  
    　英語：You cannot keep an item private because it has a DOI.

  - 登録者，またはリポジトリ管理者以上でログインしている場合、アイテムの \[編集\] ボタンを表示する。ボタンを押下すると、ワークフロー画面に遷移する

  - 登録者，またはリポジトリ管理者以上でログインしている場合、アイテムの \[削除\] ボタンを表示する。ボタンを押下すると、該当アイテムを削除する

    - 過去バージョンがある場合は、最新バージョンに\[削除\]と\[Delete this version\]を表示する。過去バージョンの場合は、\[\Delete this version\]ボタン及び\[戻る\]ボタンを表示する。 

    - 最新バージョンの\[Delete this version\]ボタンが押下された場合は、最新バージョンを論理削除し、ひとつ前のバージョンを最新バージョンに変更する。その後、バージョン更新を行うと、論理削除された次バージョンとして作成する（論理削除されたバージョンは欠番となる）。

  - アイテムにDOIが付与されている場合、アイテムの削除を認めない。  
    　日本語：アイテムにDOIが付与されているため、アイテムを削除することはできません。  
    　英語：The item cannot be deleted because it has a DOI.

  - DOI付与済アイテムについて、アイテムが直接紐づいているインデックスとその上位のインデックスについて、１つでも非表示の設定のものがある場合、アイテムの非公開はできない。  
    　日本語：アイテムにDOIが付与されているため、アイテムを非公開にすることはできません。  
    　英語：You cannot keep an item private because it has a DOI.

  - DOI付与済アイテムの登録・更新時、アイテムが直接紐づいているインデックスとその上位のインデックスについて、全てのインデックス状態が「公開」かつハーベスト公開が「公開」であるインデックスとリンクしていない場合は登録・更新はできない。また、DOI付与済アイテムを公開日が未来のインデックスのみに紐づけることはできない。  
    　日本語：アイテムにDOIが付与されているため、インデックス状態が「公開」かつハーベスト公開が「公開」のインデックスに関連付けが必要です。  
    　英語：Since the item has a DOI, it must be associated with an index whose index status is "Public" and whose Harvest Publishing is "Public".

  - 新規にDOIを付与する際、アイテムが直接紐づいているインデックスとその上位のインデックスについて、全てのインデックス状態が「公開」かつハーベスト公開が「公開」であるインデックスとリンクしていない場合 は登録・更新はできない。また、「公開」であっても、公開日が未来のインデックスのみに紐づくアイテムにはDOI付与はできない

  - 編集ボタンの二重押し抑制する。また、複数人の同時編集が発生しないよう、Redisの「pid\_{}\_will\_be\_edit」で管理する。

4\. その他

  - アイテム詳細画面を印刷時、画面上に表示されていない文字列(URL)は印刷をしない。

  - Google Scholar meta tagについて
    
      - Google Scholar の実装にはGoogle Scholar meta tagが必要である。meta tag はOAI-PMHのXML出力と同じ機能を用いて出力される。
    
      - そのため、OAI-PMH出力をしなければ、Google Scholar meta tagは出力されない。OAI-PMH出力時に、メタデータをXMLに出力すると、該当の情報もGoogle Scholarのmeta tagに出力される。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko\_records\_ui

  - > weko\_deposit

  - > weko\_detail

  - > weko\_itemtypes\_ui

<!-- end list -->

  - > 処理概要

1\. 設定

  - 作成者のプロパティーキー
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py#L130>
    
      - 設定キー：WEKO\_DEPOSIT\_SYS\_CREATOR\_KEY
    
      - 現在の設定値：

> WEKO\_DEPOSIT\_SYS\_CREATOR\_KEY = {
> 
> 'creator\_names': 'creatorNames',
> 
> 'creator\_name': 'creatorName',
> 
> 'creator\_lang': 'creatorNameLang',
> 
> 'family\_names': 'familyNames',
> 
> 'family\_name': 'familyName',
> 
> 'family\_lang': 'familyNameLang',
> 
> 'given\_names': 'givenNames',
> 
> 'given\_name': 'givenName',
> 
> 'given\_lang': 'givenNameLang',
> 
> 'alternative\_names': 'creatorAlternatives',
> 
> 'alternative\_name': 'creatorAlternative',
> 
> 'alternative\_lang': 'creatorAlternativeLang',
> 
> 'identifiers': 'nameIdentifiers',
> 
> 'creator\_mails': 'creatorMails',
> 
> 'affiliation\_name\_identifier\_scheme': 'affiliationNameIdentifierScheme',
> 
> 'affiliation\_names': 'affiliationNames',
> 
> 'affiliation\_name': 'affiliationName',
> 
> 'affiliation\_lang': 'affiliationNameLang',
> 
> 'affiliationNameIdentifiers': 'affiliationNameIdentifiers',
> 
> 'affiliation\_name\_identifier': 'affiliationNameIdentifier',
> 
> 'affiliation\_name\_identifier\_URI': 'affiliationNameIdentifierURI','creatorAffiliations': 'creatorAffiliations',
> 
> }

  - 書誌情報のプロパティーキー
    
      - パス： <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py#L190-L198>
    
      - 設定キー：WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_INFO\_SYS\_KEY
    
      - 現在の設定値：

> WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_INFO\_SYS\_KEY = \[
> 
> 'bibliographic\_titles',
> 
> 'bibliographicPageEnd',
> 
> 'bibliographicIssueNumber',
> 
> 'bibliographicPageStart',
> 
> 'bibliographicVolumeNumber',
> 
> 'bibliographicNumberOfPages',
> 
> 'bibliographicIssueDates'
> 
> \]

  - 書誌情報に対して実装に使用するキーを設定
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py#L156>
    
      - 設定キー：WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_INFO\_KEY
    
      - 現在の設定値：

> WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_INFO\_KEY = \[
> 
> 'bibliographicVolumeNumber',
> 
> 'bibliographicIssueNumber',
> 
> 'p.',
> 
> 'bibliographicNumberOfPages',
> 
> 'bibliographicIssueDates'
> 
> \]

  - 書誌情報にて、上記のキーに応じてUIに表示するテキストを設定
    
      - パス：<https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-deposit/weko_deposit/config.py#L165-L186>
    
      - 設定キー：WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_TRANSLATIONS
    
      - 現在の設定値：

> WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_TRANSLATIONS = {
> 
> 'bibliographicVolumeNumber': {
> 
> "en": "Volume",
> 
> "ja": "巻"
> 
> },
> 
> 'bibliographicIssueNumber': {
> 
> "en": "Issue",
> 
> "ja": "号"
> 
> },
> 
> 'p.': {
> 
> "en": "p.",
> 
> "ja": "p."
> 
> },
> 
> 'bibliographicNumberOfPages': {
> 
> "en": "Number of Pages",
> 
> "ja": "ページ数"
> 
> },
> 
> 'bibliographicIssueDates': {
> 
> "en": "Issued Date",
> 
> "ja": "発行年"
> 
> }

2\. 実装方法

  - モジュール：
    
      - weko-deposit：アイテムのメタデータを取得、処理するモジュールである。
    
      - weko-records-ui：アイテムのメタデータを表示するモジュールである。

  - アイテムのメタデータ表示
    
      - データベースから該当アイテムのメタデータを取得する。
    
      - 該当アイテムタイプに「非表示」と設定された属性を非表示とする。
    
      - 特別なプロパティー（作成者、書誌情報）があるかどうか、チェックする。
        
          - 書誌情報に対して、一つのサブアイテムキーが「WEKO\_DEPOSIT\_BIBLIOGRAPHIC\_INFO\_SYS\_KEY」一覧に属される場合、「書誌情報」とする。  
            表示言語を取得、該当するラベルを取得、以下のテンプレートで表示する。  
            テンプレート：  
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/output_bibliographic_information_detail.html>
        
          - 作成者に対して、プロパティー情報に「attribute\_type = creator」が保存する場合、「作成者」とする。  
            表示言語を取得、該当するラベルを取得、以下のテンプレートで表示する。  
            テンプレート：  
            <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/creator_detail_template.html>
    
      - > 残りプロパティーに対して表示言語を取得、該当するラベルを取得、以下のテンプレートで表示する。  
        > テンプレート：  
        > <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/templates/weko_records_ui/output_detail_data.html>

【補足】

  - 以下のサムネイル画像の情報がアイテム詳細画面に表示されている。  
    ・サムネイル画像名  
    ・サムネイル画像
    
      - サムネイル画像の表示サイズについて、横幅の最大値はデフォルトで「100px」としている。
    
      - アップロードされているサムネイル画像の横幅が「100px」を超える場合、横幅を「100px」に自動調整し、あわせて縦の長さも元の画像の比率にあわせて自動調整される。
    
      - なお、横幅の最大値の設定はコンフィグで設定可能：  
        <https://github.com/RCOSDP/weko/blob/v0.9.22/modules/weko-records-ui/weko_records_ui/config.py>  
        「WEKO\_RECORDS\_UI\_DEFAULT\_MAX\_WIDTH\_THUMBNAIL = 100」

<!-- end list -->

  - > 更新履歴

<table>
<thead>
<tr class="header">
<th>日付</th>
<th>GitHubコミットID</th>
<th>更新内容</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2023/08/31</p>
</blockquote></td>
<td>353ba1deb094af5056a58bb40f07596b8e95a562</td>
<td>初版作成</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2024/07/1</p>
</blockquote></td>
<td>7733de131da9ad59ab591b2df1c70ddefcfcad98</td>
<td>v1.0.7対応</td>
</tr>
</tbody>
</table>