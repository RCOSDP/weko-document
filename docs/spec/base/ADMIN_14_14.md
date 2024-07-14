### サイトライセンス

  - > 目的・用途

<!-- end list -->

  - > 本機能は、サイトライセンスの設定を行う機能である。利用方法

【Administration＞設定（Setting）＞サイトライセンス（Site License）】の順でSite License画面へ遷移して利用する。

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
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  - > 機能内容
    
      - > 【Administration\>設定（Setting）\>サイトライセンス（Site Licsnse）】の順で、Site License画面へ遷移しサイトライセンスの設定を行う。設定できる項目を以下に示す。  
        > 以下の項目の設定後、画面最下部の\[保存（Save）\]ボタン押下で、変更が適応される。「ログインせずにコンテンツをダウンロードできるIPアドレスの範囲を指定してください(Please specify range of IP address which allow users can download contents without login.)」：初期状態では、\[その他の入力行（More Inpit Row）\]ボタンのみがあり、押下することで以下のテキストボックスが現れ、設定を可能とする。
        
          - > 機関名（Organization Name）：機関名を設定するテキストボックス。初期値はなし。
        
          - > メールアドレス（E-Mail Address）：メールアドレスを設定するテキストボックス。初期値はなし。
        
          - > ドメイン名（Domain Name）：ドメイン名を設定するテキストボックス。初期値はなし。
        
          - > IPアドレスの範囲（IP Address Range）（from-to）：半角数字のみ受け付けるテキストボックス。初期値はなし。入力必須項目であり、半角数字以外を入力すると「正しい数値を入力してください（Please input a correct number）」と表示される。また、\[その他の入力行（More Input Row）\]ボタンが直下に追加され、押下することで、複数のＩＰアドレスの範囲を指定することができる。
        
          - > \[削除（delete）\]ボタンを押下することで、テキストボックスを削除することができる。
    
      - > 「サイトライセンスから除外できるアイテムタイプを指定してください（Please specify item type to be excluded from the site license）」:サイトライセンスから除外するアイテムタイプの設定を行う。初期状態では、登録されているアイテムタイプのすべてが「表示する（Allow）」リストに格納されており、除外したいアイテムタイプを選択し、\[→\]ボタンを押下することで「表示しない（Deny）」リストへ移動させる。

<!-- end list -->

  - > 関連モジュール

<!-- end list -->

  - > weko-admin

<!-- end list -->

  - > 処理概要

> 任意の設定値入力後、\[保存（Save）\]ボタンを押下することで、weko\_admin.admin.SiteLicenseView.indexが呼び出され、そこで入力項目に問題がなければdb内のsitelicense\_infoに入力した情報と更新時間（最初の一回は作成時間）が保存され、「Site license was successfully updated」というメッセージが上部に表示され、入力内容を保持した画面に遷移する。

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

