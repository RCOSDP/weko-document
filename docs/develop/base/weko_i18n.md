
## B. AngularJS htmlの多言語化について

＜概要＞
AngularJS html(テンプレート) →(1)→(2)→　messages-js.pot　→(3)→ messages-js.po　→(4)→(5)→ AngularJS 多言語モジュール

(1)テンプレートの多言語化対象タグにtranslate 属性付与
(2)python setup.py extract_messages_js (angular-gettextを利用)にて多言語化対象テキストを抽出
(3)python setup.py init_catalog_js -l ja にて、日本語リソースを作成
(4)翻訳
(5)invenio assets build にて、多言語化用AngularJS モジュールを作成

問題点

AngularJS html を表示した際に、AngularJS モジュールが呼び出されず多言語対応できない。
invenio でAngularJS html とAngularJS 多言語モジュールの紐づけをどのようにしているか
解読できていない。

なお、invenioでは、invenio-search-ui モジュールで唯一実装されているが、多言語対応できているかは未確認。

refs. https://invenio-i18n.readthedocs.io/en/latest/usage.html#angular


## C. Angular5 htmlの多言語化について
＜概要＞
Angular－－html（静的）－－gettext－→　messages.po　－→　json　－→　josn@container　－→Angularはjsonを読み込んで翻訳
　　　　｜　　　　　　　　　　　　　　　　↑
　　　　└－ts（動的）－－－手動－－－－－┘
　　　　　　
angular5で作るmodulesは下記な手順を実施する必要があります。
（weko-authors、weko-index-tree、weko-items-ui)

1. po2jsonをインストールします

$ npm install -g po2json

2. messages.poを作る。 * html（静的生成する部分） ** gettext * ts（動的生成する部分） ** 手動
messages.po

msgid "Search" 
msgstr "検索" 

msgid "Name" 
msgstr "氏名" 

msgid "Mail Address" 
msgstr "メールアドレス" 

msgid "To Page 1" 
msgstr "1ページに" 

msgid "Add organization" 
msgstr "組織追加" 

msgid "Sorry, this process is not implemented now." 
msgstr "すみません、今、この処理は実装されていません。" 

msgid "Add author" 
msgstr "著者追加" 

msgid "Add New Author" 
msgstr "著者新規追加" 

msgid "First Name" 
msgstr "姓" 

msgid "Last Name" 
msgstr "名" 

msgid "First and Last Name" 
msgstr "姓・名" 

msgid "Full Name" 
msgstr "フールネーム" 

msgid "Display" 
msgstr "表示" 

msgid "Hide" 
msgstr "非表示" 

msgid "Add author item" 
msgstr "著者項目を追加" 

msgid "Author ID" 
msgstr "著者ID" 

msgid "Confirm" 
msgstr "確認" 

msgid "Add Author ID" 
msgstr "著者IDを追加" 

msgid "Add E-mail" 
msgstr "e-mailを追加" 

msgid "Delete" 
msgstr "削除" 

msgid "Save" 
msgstr "保存" 

3. 元ソースにフォルダーを作成する
static/json/[weko_XXX]/translations/[lang]/messages.json

例：
weko_devXはweko_dev7
weko_xxxはweko_authors
langはja

static/json/weko_dev7/translations/ja/messages.json


4. containerに移動する
$ cd /home/centos/weko_devX/modules/weko-XXXX

例：
weko_devXはweko_dev7
weko_xxxはweko_authors

5. poをjsonに変換する
$ po2json [weko_xxx]/translations/[lang]/LC_MESSAGES/messages.po [weko_xxx]/static/json/[weko_xxx]/translations/[lang]/messages.json

例：
weko_devXはweko_dev7
weko_xxxはweko_authors
lang はja

po2json weko_authors/translations/ja/LC_MESSAGES/messages.po weko_authors/static/json/weko_authors/translations/ja/messages.json

messages.json

{"Search":[null,"検索"],"Name":[null,"氏名"],"Mail Address":[null,"メールアドレス"],"To Page 1":[null,"1ページに"],"Add organization":[null,"組織追加"],"Sorry, this process is not implemented now.":[null,"すみません、今、この処理は実装されていません。"],"Add author":[null,"著者追加"],"Add New Author":[null,"著者新規追加"],"First Name":[null,"姓"],"Last Name":[null,"名"],"First and Last Name":[null,"姓・名"],"Full Name":[null,"フールネーム"],"Display":[null,"表示"],"Hide":[null,"非表示"],"Add author item":[null,"著者項目を追加"],"Author ID":[null,"著者ID"],"Confirm":[null,"確認"],"Add Author ID":[null,"著者IDを追加"],"Add E-mail":[null,"e-mailを追加"],"Delete":[null,"削除"],"Save":[null,"保存"]}

6. 多言語ファイルを反映
docker-compose exec web invenio collect -v

7. Angularはmessages.jsonを読み込んで翻訳する。
※今、ja、en多言語.poに対応していました。新しい言語を追加する場合は下記な手順を実施ください。

1. messages.poを作る。
2. containerに移動する
3. 新言語フォルダーを追加
   mkdir -p [weko_xxx]/static/json/[weko_xxx]/translations/[lang]
   例：
   weko_devXはweko_dev7
   weko_xxxはweko_authors
   lang はfr
   mkdir -p weko_authors/static/json/weko_authors/translations/fr
4. poをjsonに変換する
5. 多言語ファイルを反映

----------------------------------------------------------------------------------------------------------------------
このセクションを編集
D. メタデータ項目名の多言語化について
substack/js-traverse を使ってフィルタリングする。

サンプルコード：

var traverse = require('traverse');

// filter json obj by language
var filter_language = function(language, obj) {
  var result = traverse(obj).map(function(item) {
    if (this.key === language) {
      this.parent.update(item);
    }
  });
  return result;
};

// example object in the multi-lingual format
var obj = {
  "id": "C001",
  "title": {
    "en": "Pro Shogi Player's Rating and Game Records Analysis",
    "ja": "将棋名人のレーティングと棋譜分析" 
  },
  "name": {
    "en": "Hiroshi Yamashita",
    "ja": "山下 宏" 
  }
};

console.log(filter_language('en', obj));
console.log(filter_language('ja', obj));
参考サイト：
〇substack/js-traverse
https://github.com/substack/js-traverse