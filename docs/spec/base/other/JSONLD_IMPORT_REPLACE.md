# JSONLDインポート文字列置換

## 目的・用途

【v2.1.0】JSONLDファイルのインポート時に、JSON内の指定されたパスに対して文字列の置換を適用する。

## 利用方法

設定値で置換ルール定義(`WEKO_SEARCH_UI_IMPORT_REPLACE_RULES`)、適用ルールマップ(`WEKO_SEARCH_UI_IMPORT_REPLACE_RULE_MAP`)の2つを設定する。  
いずれも weko-search-ui の config（`weko_search_ui/config.py`）に既定値が定義されており、変更する場合は `instance.cfg` 等で上書きする。release_v2.1.0 の既定値は以下のとおり（#63281 で `scripts/instance.cfg` に置いていた同内容の設定を削除し、モジュールの既定値に移した）。既定ルール `pipe_full_width` は `target_path` が空のため、既定のままでは置換は行われない。

```Python
WEKO_SEARCH_UI_IMPORT_REPLACE_RULES = {
    "pipe_full_width": {
        "from": "|",
        "to": "｜",
        "is_regex": False,
        "target_path": []
    }
}
WEKO_SEARCH_UI_IMPORT_REPLACE_RULE_MAP = {
    "32001": [
        "pipe_full_width"
    ]
}
```

JSONLD形式のメタデータを取り込む際、自動で以下の文字列置換処理が適用される。

- 取り込みに使用中のJSONLDマッピングのidをキーとして、適用ルールマップから適用するルール名のリストを取得する。
- 各ルール名を使用して、置換ルール定義から置換ルールを取得する。
- 各置換ルールに従い、JSONLDファイルに文字列置換を適用する。

### `WEKO_SEARCH_UI_IMPORT_REPLACE_RULES`(置換ルール定義)の詳細

#### 型定義

辞書型(dict)

#### 概要

インポート時に適用する文字列置換ルールの定義を保持する辞書。各ルールはルール名によって識別される。

#### 置換ルールの定義方法

置換ルールは以下のような構成で定義する。

```Python
ルール名: {
    "from": ...,
    "to": ...,
    "is_regex": ...,
    "target_path": [...]
}
```

- ルール名  
    ルール定義のキー名。  
    同じキー名を複数用いた場合、同一キー名の最後のルール定義のみ有効になる。([注意点](#注意点)参照)
- 各要素

    <table>
    <thead>
    <tr>
    <th>要素名</th>
    <th>必須</th>
    <th>型</th>
    <th>空文字指定</th>
    <th>複数指定</th>
    <th>概要</th>
    <th>備考</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>from</td>
    <td>〇</td>
    <td>str</td>
    <td>×</td>
    <td>×</td>
    <td>置換<strong>前</strong>の文字列を指定する。</td>
    <td></td>
    </tr>
    <tr>
    <td>to</td>
    <td>〇</td>
    <td>str</td>
    <td>〇</td>
    <td>×</td>
    <td>置換<strong>後</strong>の文字列を指定する。</td>
    <td>・ 空文字を指定した場合は置換前の文字列が削除される。<br>・指定した文字列にそのまま置換されるため、<strong>正規表現ではなく</strong>、単一の文字列を指定する。</td>
    </tr>
    <tr>
    <td>is_regex</td>
    <td>×</td>
    <td>bool</td>
    <td>×</td>
    <td>×</td>
    <td>Trueの場合は正規表現が一致した文字列を置換、Falseの場合は完全一致した文字列を通常置換する。</td>
    <td>指定しなかった場合はFalseとなる。</td>
    </tr>
    <tr>
    <td>target_path</td>
    <td>×</td>
    <td>list</td>
    <td>×</td>
    <td>〇</td>
    <td><code>jsonld_mappings</code>テーブルの<code>mapping</code>カラムで定義されたプロパティ名(JSON-LDマッピングの右側の値)を指定する。</td>
    <td>・空リストの場合は該当のルール定義の置換処理をスキップする。<br>・例：<code>"データ作成者.作成者姓名.姓名": "creator.name.value"</code>を置換対象としたい場合、<br>右側の<code>"creator.name.value"</code>を指定する。<br>・target_pathにはオブジェクトに対応するパスは指定できない。<br>指定した場合、置換は行わずスキップする。</td>
    </tr>
    </tbody>
    </table>

#### 記述例

is_regexのTrue/Falseでfromの書き方が変わるため、例を記載する。  

```Python
WEKO_SEARCH_UI_IMPORT_REPLACE_RULES = {
    # is_regexがFalseの場合の定義の書き方例
    "pipe_full_width": {
        "from": "|",
        "to": "｜",
        "is_regex": False,
        "target_path": [
            "ams:industrialUse.value", 
            "ams:anonymousProcessing.value"
        ]
    },
    # is_regexがTrueの場合の定義の書き方例
    "space_full_width": {
        "from": r"(\u3000)|(　)", 
        "to": " ", # toには正規表現は使えない
        "is_regex": True,
        "target_path": [
            "contributor.name.value"
        ]
    }
}
```

#### 注意点

1. 文字列置換ルールに同一のルール名を複数回用いた場合  
    同一ルール名のうち、最後のルール定義が有効になる。最後以外のルール定義は使用されない。

    例： 同一ルール名を定義した場合

    ```Python
    WEKO_SEARCH_UI_IMPORT_REPLACE_RULES = {
        # 無効
        "rule_name": {
            "from": "abc",
            "to": "あ",
            "is_regex": False,
            "target_path": [
                "abc.value"
            ]
        },
        # 無効
        "rule_name": {
            "from": "abc",
            "to": "い",
            "is_regex": False,
            "target_path": [
                "abc.value"
            ]
        },
        # 有効
        "rule_name": { 
            "from": "abc",
            "to": "う",
            "is_regex": False,
            "target_path": [
                "abc.value"
            ]
        }
    }
    ```

2. `to`に正規表現を用いた場合  
    toに指定した文字列は**そのままの文字列**として置換されるため、正規表現を用いると意図した置換にはならない。

    ```Python
    "rule_name": {
        "from": r"\|",
        "to": r"\uFF5C",　# 全角パイプ相当の正規表現
        "is_regex": True,
        "target_path": [
            "abc.value"
        ]
    }
    ```

    上記のように指定すると、fromに指定した`|`(半角パイプ)が`\\\\uFF5C`(バックスラッシュ4つ+uFF5C)に置換される。  

    以下のようにUnicodeエスケープであれば指定可能。

    ```Python
    "rule_name": {
        "from": r"\|",
        "to": "\uFF5C",　# 全角パイプ相当のUnicodeエスケープ
        "is_regex": True,
        "target_path": [
            "abc.value"
        ]
    }
    ```

    上記の書き方であれば、fromに指定した`|`(半角パイプ)が`｜`(全角パイプ)に置換される。

### `WEKO_SEARCH_UI_IMPORT_REPLACE_RULE_MAP`(適用ルールマップ)の詳細

#### 型定義

辞書型(dict)

#### 概要

`jsonld_mappings`テーブルの`id`(mapping_id)をキーとし、適用すべき置換ルール(`WEKO_SEARCH_UI_IMPORT_REPLACE_RULES`のキー)のリストを持つ辞書。  
各mapping_idごとにどの置換ルールを適用するかを制御する。

#### 記述例

```Python
WEKO_SEARCH_UI_IMPORT_REPLACE_RULE_MAP = {
    "32001": [    # jsonld_mappingsテーブルのid(mapping_id)
        "pipe_full_width"
    ]
}
```

### 警告

- 処理中にエラーが発生した場合はエラー内容をワーニングリストに格納して処理を続行する。
- 警告メッセージがある場合でも、インポート処理上問題がなかった場合はインポート処理は通常通り実行される。
- メッセージの言語やワーニングの表示はインポートを行う方法により異なる。

    <table>
    <thead>
    <tr>
    <th>インポート方法</th>
    <th>メッセージ言語</th>
    <th>ワーニング表示</th>
    <th>備考</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>RO-Crateインポート画面から実行</td>
    <td>日本語・英語対応</td>
    <td>ワーニング・エラーどちらも画面に表示。<br>エラーがなければインポート可能。</td>
    <td></td>
    </tr>
    <tr>
    <td>API経由でインポート</td>
    <td>英語のみ</td>
    <td>エラーがない場合（インポート可能な場合）はワーニングは表示されない。</td>
    <td>エラー発生時のみ、<br>ワーニングも含めて英語でメッセージを返却する。</td>
    </tr>
    </tbody>
    </table>

- 言語設定

    <table>
    <thead>
    <tr>
    <th>内容</th>
    <th>英語メッセージ</th>
    <th>日本語メッセージ</th>
    <th>備考</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>置換ルール定義、置換ルールマッピング、<br>ルールキーリストの型が不正</td>
    <td>Replacement failed.: The type of the jsonld mapping replacement rule is invalid.</td>
    <td>置換処理に失敗しました。: jsonldマッピングの置換ルールの型が不正です。</td>
    <td></td>
    </tr>
    <tr>
    <td>置換ルールIDが取得できない</td>
    <td>Replacement failed.: Required replacement rule: '{rule_id}' is missing.</td>
    <td>置換処理に失敗しました。: 必要な置換ルール：'{rule_id}'が見つかりません。</td>
    <td>{rule id}: 置換ルールID</td>
    </tr>
    <tr>
    <td><code>from</code>、<code>to</code>、<code>target_path</code>の設定が不正</td>
    <td>Replacement failed.: Replacement rule: '{rule_id}' is invalid.</td>
    <td>置換処理に失敗しました。: 置換ルール： '{rule_id}'の設定が不正です。</td>
    <td>{rule id}: 置換ルールID</td>
    </tr>
    <tr>
    <td><code>is_regex</code>の設定が不正</td>
    <td>Replacement rule: '{rule_id}' - 'is_regex' is not boolean. Treated as False.</td>
    <td>置換ルール: '{rule_id}' - 'is_regex' が真偽値ではありません。Falseとして処理します。</td>
    <td>{rule id}: 置換ルールID</td>
    </tr>
    <tr>
    <td>re.error発生時</td>
    <td>Replacement failed.: Replacement rule: '{rule_id}' - regex error: {エラー原因}</td>
    <td>置換処理に失敗しました。: 置換ルール: '{rule_id}' - 正規表現エラー: {エラー原因}</td>
    <td>{rule id}: 置換ルールID</td>
    </tr>
    <tr>
    <td>それ以外のエラー発生時</td>
    <td>Replacement failed.: {起きたエラーのメッセージ}</td>
    <td>置換処理に失敗しました。: {起きたエラーのメッセージ}</td>
    <td></td>
    </tr>
    </tbody>
    </table>

## 実装補足（v2.1.0）

- 処理本体は `weko_search_ui.mapper.JsonLdMapper.apply_import_replace_rules`。`to_item_metadata` の中で、JSON-LD をフラット化したメタデータ（キーは `creator[0].name[0].value` のように配列添字付き）に対して、マッピング処理の前に呼び出される。
- 各ルールの `target_path` と、メタデータのキーから `[n]` を除いたパスが一致する値を置換する。`is_regex` が True の場合は `re.sub`、False の場合は `str.replace`（部分一致の全置換）で置換する。
- 警告は `system_info["warnings"]` に追加され、ログにも WARNING で出力される。`is_regex` が真偽値でない旨の警告のみ「Replacement failed.: 」を付けずに出力する。
- 型不正（ルール定義・ルールマップ・ルールキーリスト）や置換中の想定外の例外が発生した場合は、その時点で残りのルールの適用を打ち切る。
- 置換結果は `[n]` を除いたパス（`target_path` と同名のキー）に書き戻されるため、配列添字を含むキーの値（例 `creator[0].name[0].value`）については元のキーの値が置換されない実装になっている（要確認）。

## 変更履歴

| 日付       | GitHubコミットID | 更新内容 |
| ---------- | ---------------- | -------- |
| 2026/02/13 |                  | 初版作成 |
| 2026/10/05 | 508030789 | release_v2.1.0突合：設定の既定値（#63281 で instance.cfg からモジュール config へ移動）を追記、警告メッセージの書式を実装（`Replacement failed.: `）に合わせて訂正、実装補足を追記 |
