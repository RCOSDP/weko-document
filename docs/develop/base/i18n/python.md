# python の多言語対応

## 言語リソース化手法

### 言語リソースの定義

#### .py の場合

flask_babelexのlazy_gettextを利用する。
WEKO3では _ に置き換えて利用している。

例：
```
from flask_babelex import lazy_gettext as _ 

flash(_("ERROR"), category='error')
```


#### jinja2 (.html)の場合

weko-accounts/weko_accounts/templates/.html

```
{{ _('Welcome!') }} 
```

NOTE:
実装にあたっては、i18nスコープを意識すること

(1)リソース化できる実装パターン

```
{% macro tabs_selector(tab_value='top') %}
    <li role="presentation" {% if tab_value=='top' %}class="active"{% endif %}><a href="/">{{ _('Top') }}</a></li>
    <li role="presentation" {% if tab_value=='item' %}class="active"{% endif %}><a href="{{url_for('weko_items_ui.index')}}">{{ _('Item Registration') }}</a></li>
    <li role="presentation" {% if tab_value=='author' %}class="active"{% endif %}><a href="{{url_for('weko_authors.index')}}">{{ _('Author Management') }}</a></li>
{% endmacro %}
```

(2)リソース化できない実装パターン

```
{% macro tabs_selector(tab_value='top') %}
{% set tabs_list = [('top', 'Top', '/'),
('item', 'Item Registration', url_for('weko_items_ui.index')),
('author', 'Author Management', url_for('weko_authors.index'))] %}
{% for (value, name, href) in tabs_list %}
<li role="presentation" {% if tab_value == value %}class="active"{% endif %}><a href="{{href}}">{{_(name)}}</a></li>
{% endfor %}
{% endmacro %}
```


### 言語リソースの取得準備

setup.pyに以下のrequireを追加する。

```
setup_requires = [
    'Babel>=1.3',
]
```

setup.cfgに以下のコンフィグを追加する。

weko-accountsの場合：
```
[extract_messages]
copyright_holder = National Institute of Informatics
msgid_bugs_address = wekosoftware@nii.ac.jp
mapping-file = babel.ini
output-file = weko_accounts/translations/messages.pot
add-comments = NOTE

[init_catalog]
input-file = weko_accounts/translations/messages.pot
output-dir = weko_accounts/translations/

[compile_catalog]
directory = weko_accounts/translations/
```

weko_accounts/babel.ini

jinja2のプラグインを追加

```
[python: **.py]
encoding = utf-8

# Extraction from Jinja2 templates

[jinja2: **/templates/**.html]
encoding = utf-8
extensions = jinja2.ext.autoescape, jinja2.ext.with_, webassets.ext.jinja2.AssetsExtension, jinja2.ext.loopcontrols, jinja2.ext.i18n

# Extraction from JavaScript files

[javascript: **.js]
encoding = utf-8
extract_messages = $._, jQuery._

# 説明:
# 例えば、webassets.ext.jinja2.AssetsExtensionがないと、jinja2テンプレートの {% assets %}{% endassets %}で囲まれた翻訳文が取れなくなる。
```

### 言語リソースの抽出

以下コマンドを実行する。

```
python setup.py extract_messages
```

実行すると、翻訳用テキストが translations/messages.pot に出力される。

translations/messages.pot の例

```
#. NOTE: This is a note to a translator.
#: weko_accounts/ext.py:41
msgid "Hello World!" 
msgstr "" 

#: weko_accounts/templates/weko_accounts/index.html:24
msgid "Welcome!" 
msgstr "" 
```

### 言語ファイルの作成

messages.potから言語別のカタログファイルを作成する。

新規作成時は以下コマンドを実行する。

```
python setup.py init_catalog -l 言語コード
```

カタログ更新時は以下を実行する。

```
python setup.py update_catalog -l 言語コード
```

実行すると、translations/言語コード/LC_MESSAGES/message.poが作成される。

message.poの内容はmessages.potと同一となる。

[言語コード一覧](https://ja.wikipedia.org/wiki/ISO_639-1%E3%82%B3%E3%83%BC%E3%83%89%E4%B8%80%E8%A6%A7)


### 翻訳の追加

ja/LC_MESSAGES/messages.po　は基本的に以下構造となる。

```
#: 言語リソースの位置
msgid "言語リソースID"
msgstr "翻訳"
```

実際の例は以下の通り。

```
#. NOTE: This is a note to a translator.
#: weko_accounts/ext.py:41
msgid "Hello World!" 
msgstr "はじめまして、世界！"

#: weko_accounts/templates/weko_accounts/index.html:24
msgid "Welcome!" 
msgstr "ようこそ!"                
```

### カタログのコンパイル

以下コマンドを実行し、各言語のmessages.poをコンパイルする。

```
python setup.py compile_catalog
```

translations/言語コード/LC_MESSAGES/message.moが作成される。

### 言語の追加

invenio.cfg　に言語を追加する。

```
I18N_LANGUAGES = [('en', 'English'),('ja', 'Japanese'),('言語コード', '言語名')]
```

populate-instance.sh に以下を追加する。

```
${INVENIO_WEB_INSTANCE} language create --active --registered "言語コード" "言語名" 順番
```

または直接invneioコマンドを実行する。

```
invenio language create --active --registered "言語コード" "言語名" 順番
```

例：

```
${INVENIO_WEB_INSTANCE} language create --active --registered "fr" "Franch" 003
```

### 追加言語の確認

追加言語の確認を行うために、モジュールの再インストールとコンテナのリスタートを行う。


```
docker-compose -f docker-compose2.yml exec web 
cd modules/weko-accounts
pip install -e .
exit
```

```
docker-compose -f docker-compose2.yml restart web
```

