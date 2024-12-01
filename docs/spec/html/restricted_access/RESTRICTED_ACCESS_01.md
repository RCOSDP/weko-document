### アイテムタイプ管理（制限公開）

  - 制限公開機能に対して対応しているアイテムタイプは以下の通りである（日立納品時）
    
      - 「利用申請」
    
      - 「二段階利用申請」
    
      - 「利用報告-Data Usage Report」  
        これら3つのアイテムタイプの構成は以下の通りである

  - 制限公開アイテム登録用ファイル情報  
    制限公開機能を利用するには、「制限公開用のコンテンツファイル」が必要である
    
      - アイテム登録画面でファイルをアップロードすると、ファイル名を自動設定する
    
      - アップロードしたファイルのフォーマット・ファイルサイズをDBに格納する  
        \*\*Meta画面のAllow Multipleのオプションはオンに設定し非活性

<table>
<thead>
<tr class="header">
<th>プロパティ定義</th>
<th>備考</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>表示名</td>
<td>Text</td>
<td>-</td>
<td>-</td>
<td>ファイル名を登録する</td>
</tr>
<tr class="even">
<td>本文URL</td>
<td>Object</td>
<td>本文URL</td>
<td>Text</td>
<td>コンテンツファイルの格納先が自動で登録される<br />
コンテンツファイルが無い場合は手入力でURLを入力可能</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ラベル</td>
<td>Text</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>オブジェクトタイプ</td>
<td>Select</td>
<td>選択肢<br />
　abstract/summary/fulltext/thumbnail/other　</td>
</tr>
<tr class="odd">
<td>フォーマット</td>
<td>Text</td>
<td>-</td>
<td>-</td>
<td>コンテンツファイルのMIMEタイプを取得して自動で登録される</td>
</tr>
<tr class="even">
<td>サイズ</td>
<td>List</td>
<td>サイズ</td>
<td>Text</td>
<td>コンテンツファイルのサイズを取得して自動で登録される</td>
</tr>
<tr class="odd">
<td>日付</td>
<td>List</td>
<td>日付</td>
<td>Datetime</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>日付タイプ</td>
<td>Select</td>
<td>選択肢<br />
　Accepted/Collected/Copyrighted /Issued/Submitted/Updated/Valid　</td>
</tr>
<tr class="odd">
<td>バージョン情報</td>
<td>Text</td>
<td>-</td>
<td>-</td>
<td></td>
</tr>
<tr class="even">
<td>表示形式</td>
<td>Select</td>
<td>-</td>
<td>-</td>
<td>detail/simple/preview</td>
</tr>
<tr class="odd">
<td>ライセンス</td>
<td>Select</td>
<td>-</td>
<td>-</td>
<td></td>
</tr>
<tr class="even">
<td>自由ライセンス</td>
<td>Textarea</td>
<td>-</td>
<td>-</td>
<td>"ライセンス"で"自由入力"を選択した場合に登録する</td>
</tr>
<tr class="odd">
<td>アクセス</td>
<td>Radios</td>
<td>-</td>
<td>-</td>
<td>オープンアクセス/オープンアクセス日を指定する/ログインユーザのみ/公開しない/制限公開（デフォルト）</td>
</tr>
<tr class="even">
<td>グループ</td>
<td>Select</td>
<td>-</td>
<td>-</td>
<td>"アクセス"で"ログインユーザのみ"を選択したときに登録する</td>
</tr>
<tr class="odd">
<td>公開日（オープンアクセスの日付）</td>
<td>List</td>
<td>日付</td>
<td>Datetime</td>
<td>"アクセス"で"オープンアクセス日を指定する"を選択したときに登録する</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>タイプ</td>
<td>Select</td>
<td>日付タイプは「Available」固定（Item Registration画面では入力エリアは存在しない）</td>
</tr>
<tr class="odd">
<td>データタイプ</td>
<td>Radios</td>
<td>-</td>
<td>-</td>
<td>"アクセス"で"ログインユーザのみ"を選択したときに登録するライフ/累積/組み合わせ分析l都道府県/地点情報</td>
</tr>
<tr class="even">
<td>提供方法</td>
<td>List</td>
<td>ロール</td>
<td>Select</td>
<td>"アクセス"で"制限公開"を選択したときに登録する/ Administration &gt;UserManagement&gt;Roleで管理しているロールと「非ログインユーザ（Guest）」をリストに表示する</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ワークフロー</td>
<td>Select</td>
<td>Administration &gt;WorkFlow&gt;WorkFlow Listで管理しているワークフローのうち「制限公開フラグ」（関連ストーリー： <a href="https://redmine.devops.rcos.nii.ac.jp/issues/24080"><del>#24080</del></a>）が有効なものをリストに表示する</td>
</tr>
<tr class="even">
<td>利用規約</td>
<td>Select</td>
<td>-</td>
<td>-</td>
<td>"アクセス"で"制限公開"を選択したときに登録する。管理画面で登録した利用規約をリストで表示する。選択肢に「自由入力」を設ける</td>
</tr>
</tbody>
</table>

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