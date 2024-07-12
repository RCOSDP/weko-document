
### 言語切替

  - > 目的・用途

本機能は、ユーザーの操作によって表示言語を切り替えられるようにする機能である。

  - > 利用方法

画面のヘッダ部分にある表示言語切替のプルダウンを操作する。

または、「\[トップページURL\]/lang/\<lang\_code\>」のURLでアクセスする。

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

<!-- end list -->

  - ユーザー画面のヘッダ部分に表示言語切替のプルダウンを設ける
    
      - 選択肢は、【Administration \> 設定（Setting） \> 言語表示（Language）画面】での「登録言語」に指定されている言語一覧である
    
      - 「登録言語」に1番上の言語はデフォルト言語とする
    
      - 選択している言語に対応がない場合、表示言語は英語とする
    
      - 詳細は[ADMIN-14-3: 言語表示](\\l)参照。

  - URLを用いて本機能を利用する場合、【Administration \> 設定（Setting） \> 言語表示（Language）画面】に表示されている言語なら「登録言語」に指定されていない言語でも利用可能

  - URLに ?next=\<リダイレクト先のパス\> を付加することで、直接言語のページに遷移することができる
    
      - 例：\[トップページURL\]/lang/en?next=/workflow/

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > invenio-i18n（WEKOソース内にforkされていない）

<!-- end list -->

  - > 処理概要

> \<lang\_code\> で指定された言語コードが instance.config の BABEL\_DEFAULT\_LOCALE または I18N\_LANGUAGES で定義されたリストのキーに合致した場合、その言語が選択されたことをSessionに保存して言語切替を行ったページにリダイレクトしている。

  - > 保存先のSessionは、session\[current\_app.config\["I18N\_SESSION\_KEY"\]\]である。

  - > コンフィグI18N\_SESSION\_KEYのデフォルト値は”language”である。

> リストに無い言語コードが指定された場合は 404 を返す。

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
</tbody>
</table>