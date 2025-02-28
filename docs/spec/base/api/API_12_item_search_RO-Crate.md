### アイテム検索用API

#### 目的・用途

本機能は、ユーザーがアイテムを検索する際に用いるAPIである。
ユーザーが指定したキーワードで検索をリクエストした際に、指定したキーワードを含むアイテムの検索を行う。またメタデータ項目を指定した検索や、ファセット検索にも対応する。

#### 利用方法

キーワード及びメタデータ項目、ファセット検索項目を指定しAPIを実行する。

#### 利用可能なロール

  <table>
  <thead>
  <tr>
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
  <tr>
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

#### 機能内容

  - 指定したキーワード及びメタデータ項目、ファセット検索項目に該当するアイテムをRO-Crate形式で返す。

#### 関連モジュール

  - weko_search_ui:query.py

  - invenio_records_rest:views.py

#### 処理概要

  - OAuth2認証機能を用いてユーザーの適切なアクセス制限を行う。
  - クライアントキャッシュを防ぐため既定の値をレスポンスヘッダーに加える。
  - サーバー負荷軽減のためリクエストのアクセス制限機能をかける。
  - キーワード検索を行う場合は以下の流れで処理を行う。
    - リクエストパラメータからキーワード、表示するアイテム数、ソートの情報を取得する。
    - 関連モジュールを用いて、Elasticsearchに適切な形のクエリを作成する。
    - ソートした際にElasticsearchから得られる最後のアイテムのソート情報を、ページネーションで使うカーソル情報とする。
    - Elasticsearchのカーソル情報をページネーションで使うため、一意になるよう必ずIDでのソートを降順で行う。ただし、他にソートの指定がある場合は優先度を最も低く設定する。
    - RO-Crateマッピングが存在するアイテムタイプのアイテムのみを検索の対象とする。
  - メタデータ項目による検索もキーワード検索と同様に行うが、次の処理を行う。
    - 値を候補から選択する形式のメタデータ項目に対して複数の値を選択した場合、それらの値のOR検索として検索する。
    - 複数のメタデータ項目を指定した場合、全ての条件を満たすAND検索として検索する。
    - ソートはキーワード検索と同様に行うが、ソートキーが複数ある場合は最初のソートキーの優先度を最も高く設定する。
  - オフセットページネーション、カーソルページネーションの両方のパラメータが指定されていた場合はオフセットページネーションを優先する。
  - キーワード検索、メタデータ項目による検索について、以下を除きWEKOの検索画面からの検索と同一の検索を行う。
    - タイトル完全一致検索が指定された場合は、Elasticsearchでキー「title」、「alternative」を検索に使用し、キーに対応する値のうち少なくとも一つが検索文字列に完全一致するドキュメントを検索する。
    - メタデータ項目のうち、アイテムタイプは使用できない。
  - パラメータがq, title, creator, des, publisher, cname, id, srctitle, degreename, dgname, text1~text10の場合
    - 文字列をスペースで区切った場合はAND検索として検索する。
    - 文字列を「OR」(大文字、前後にスペースが必要)、「\|」(パイプ、前後にスペースが必要)で区切った場合、OR検索として検索する。前後一方でもスペースが無い場合や、「or」(小文字)で区切った場合は通常通り検索する。「OR」、「|」で区切ったことによるOR検索よりも、スペースで区切ったことによるAND検索の方を優先して処理する。
  - パラメータ sbjscheme, fd_attr, id_attr, type, lang, version, license について
    - 使用可能な値が事前に定義されている  
    - 使用可能な値と、値を指定した際に検索に用いられる値はDBのsearch_managementテーブルのsearch_conditions列(DBにデータがない場合はmodules/weko-admin/weko_admin/config.pyのdetail_condition) を参照する
    - 使用できない値を指定したパラメータは無視される
    - 複数の値を指定する場合は「,」(カンマ)で区切って指定する
  
  - (subject, sbjscheme), (fd_attr, filedate_from, filedate_to), (id, id_attr), (dategranted_from, dategranted_to), (integer_rangeX_from, integer_rangeX_to), (float_rangeX_from, float_rangeX_to), (date_rangeX_from, date_rangeX_to) は括弧内のパラメータを全て指定した場合のみ検索条件として使用される

  - ファセット検索
    - 検索結果をファセット検索項目の値ごとに集計しアイテム数を返却する機能と、ファセット検索項目の値を指定して検索結果の絞り込みを行う機能の2つの機能を持つ。
    - 集計機能
      - ファセット検索の設定画面でActive列にチェックされているファセット検索項目を対象に集計を行う。
      - 設定画面は[ADMIN-14-12: ファセット検索](../admin/ADMIN_14_12.md)を参照。
      - 各ファセット検索項目について、ファセット検索項目の値ごとに集計後のアイテム数を検索結果から取得し、レスポンスボディで返却する。
      - 値はアイテム数の多い順にソートし返却する。返却対象とするファセット検索項目の値はアイテム数が多い順に並べて上位から指定した件数までである。件数の上限はmodules/weko-admin/weko_admin/config.pyのWEKO_ADMIN_FACET_SEARCH_SETTING_BUCKET_SIZEで定義され、初期値は1000件である。
    - 絞り込み機能
      - ファセット検索項目について、値を指定して完全一致による絞り込みを行う。
      - ファセット検索項目と値はリクエストパラメータで指定する。
      - パラメータ名はファセット検索の設定画面でItem Name(EN)列に設定されているものを使用する。
      - ファセット検索の設定画面でActive列にチェックされているファセット検索項目を使用可能とする。
      - Elasticsearchに対し、ファセット検索の設定時に作成されるクエリをfilterとして、検索クエリと同時に適用する。
      - 同一のパラメータを複数指定した場合、それらの条件のOR検索として検索する。
      - 複数のパラメータを指定した場合、それらの条件のAND検索として検索する。
      - メタデータ項目による検索と同時に使用した場合、それらの条件のAND検索として検索する。
    - 集計機能と絞り込み機能を同時に使用した場合、集計機能、絞り込み機能の順で適用する。

  - HTTPメソッド  
  GET

- URL  
  api/:version/records

  | パラメータ | 値             |
  |------------|----------------|
  | version    | バージョン情報 |

- リクエスト  
  - ヘッダ
    <table>
    <thead>
    <tr>
    <th>キー名</th>
    <th>値</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Accept-Language</td>
    <td>言語設定<br>
    デフォルトはen</td>
    </tr>
    <tr>
    <td>Authorization</td>
    <td>認可情報</td>
    </tr>
    </tbody>
    </table>

  - クエリ
    <table>
    <thead>
    <tr>
    <th>パラメータ</th>
    <th>型</th>
    <th>説明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>q</td>
    <td>string</td>
    <td>検索するキーワード</td>
    </tr>
    <tr>
    <td>search_type</td>
    <td>int</td>
    <td>検索形式 (0: 全文検索、1: キーワード検索)</td>
    </tr>
    <tr>
    <td>pretty</td>
    <td>bool</td>
    <td>レスポンスの整形の有無 (デフォルト: false)</td>
    </tr>
    <tr>
    <td>page</td>
    <td>int</td>
    <td>取得するページ番号</td>
    </tr>
    <tr>
    <td>cursor</td>
    <td>int</td>
    <td>ページネーションのカーソル</td>
    </tr>
    <tr>
    <td>size</td>
    <td>int</td>
    <td>取得する検索結果の最大数</td>
    </tr>
    <tr>
    <td>sort</td>
    <td>string</td>
    <td>ソートキー</td>
    </tr>
    <tr>
    <td colspan="3">以下、メタデータ項目</td>
    </tr>
    <tr>
    <td>title</td>
    <td>string</td>
    <td>タイトル</td>
    </tr>
    <tr>
    <td>exact_title_match</td>
    <td>bool</td>
    <td>タイトル完全一致検索を指定する (デフォルト: false)</td>
    </tr>
    <tr>
    <td>creator</td>
    <td>string</td>
    <td>著者名</td>
    </tr>
    <tr>
    <td>subject</td>
    <td>string</td>
    <td>件名</td>
    </tr>
    <tr>
    <td>sbjscheme</td>
    <td>int (候補から選択)</td>
    <td>件名種別</td>
    </tr>
    <tr>
    <td>spatial</td>
    <td>string</td>
    <td>地域</td>
    </tr>
    <tr>
    <td>des</td>
    <td>string</td>
    <td>内容記述</td>
    </tr>
    <tr>
    <td>publisher</td>
    <td>string</td>
    <td>出版者</td>
    </tr>
    <tr>
    <td>cname</td>
    <td>string</td>
    <td>寄与者</td>
    </tr>
    <tr>
    <td>fd_attr</td>
    <td>string (候補から選択)</td>
    <td>日付種別</td>
    </tr>
    <tr>
    <td>filedate_from</td>
    <td>date (YYYYMMDD形式)</td>
    <td>日付下限を指定</td>
    </tr>
    <tr>
    <td>filedate_to</td>
    <td>date (YYYYMMDD形式)</td>
    <td>日付上限を指定</td>
    </tr>
    <tr>
    <td>mimetype</td>
    <td>string</td>
    <td>フォーマット</td>
    </tr>
    <tr>
    <td>id</td>
    <td>string</td>
    <td>識別子</td>
    </tr>
    <tr>
    <td>id_attr</td>
    <td>string (候補から選択)</td>
    <td>識別子種別</td>
    </tr>
    <tr>
    <td>srctitle</td>
    <td>string</td>
    <td>雑誌名</td>
    </tr>
    <tr>
    <td>type</td>
    <td>int (候補から選択)</td>
    <td>資源タイプ</td>
    </tr>
    <tr>
    <td>lang</td>
    <td>string (候補から選択)</td>
    <td>言語</td>
    </tr>
    <tr>
    <td>temporal</td>
    <td>string</td>
    <td>期間</td>
    </tr>
    <tr>
    <td>dategranted_from</td>
    <td>date (YYYYMMDD形式)</td>
    <td>学位取得日下限を指定</td>
    </tr>
    <tr>
    <td>dategranted_to</td>
    <td>date (YYYYMMDD形式)</td>
    <td>学位取得日上限を指定</td>
    </tr>
    <tr>
    <td>version</td>
    <td>string (候補から選択)</td>
    <td>著者版フラグ</td>
    </tr>
    <tr>
    <td>dissno</td>
    <td>string</td>
    <td>学位番号</td>
    </tr>
    <tr>
    <td>degreename</td>
    <td>string</td>
    <td>学位名</td>
    </tr>
    <tr>
    <td>dgname</td>
    <td>string</td>
    <td>学位授与機関</td>
    </tr>
    <tr>
    <td>wid</td>
    <td>int</td>
    <td>作成者識別子</td>
    </tr>
    <tr>
    <td>iid</td>
    <td>int</td>
    <td>インデックスID</td>
    </tr>
    <tr>
    <td>license</td>
    <td>string (候補から選択)</td>
    <td>ライセンス</td>
    </tr>
    <tr>
    <td>textX<br>
    (Xは1~10の整数)</td>
    <td>string</td>
    <td>詳細検索条件設定でtextXに割り当てた項目の値</td>
    </tr>
    <tr>
    <td>integer_rangeX_from<br>
    (Xは1~5の整数)</td>
    <td>int</td>
    <td>詳細検索条件設定でinteger_rangeXに割り当てた項目の値の下限</td>
    </tr>
    <tr>
    <td>integer_rangeX_to<br>
    (Xは1~5の整数)</td>
    <td>int</td>
    <td>詳細検索条件設定でinteger_rangeXに割り当てた項目の値の上限</td>
    </tr>
    <tr>
    <td>float_rangeX_from<br>
    (Xは1~5の整数)</td>
    <td>float</td>
    <td>詳細検索条件設定でfloat_rangeXに割り当てた項目の値の下限</td>
    </tr>
    <tr>
    <td>float_rangeX_to<br>
    (Xは1~5の整数)</td>
    <td>float</td>
    <td>詳細検索条件設定でfloat_rangeXに割り当てた項目の値の上限</td>
    </tr>
    <tr>
    <td>date_rangeX_from<br>
    (Xは1~5の整数)</td>
    <td>date</td>
    <td>詳細検索条件設定でdate_rangeXに割り当てた項目の値の下限 (YYYYMMDD形式)</td>
    </tr>
    <tr>
    <td>date_rangeX_to<br>
    (Xは1=5の整数)</td>
    <td>date</td>
    <td>詳細検索条件設定でdate_rangeXに割り当てた項目の値の上限 (YYYYMMDD形式)</td>
    </tr>
    <tr>
    <td >ファセット検索項目</td>
    <td ></td>
    <td >ファセット検索の設定でActiveとした項目</td>
    </tr>
    </tbody>
    </table>

  - リクエスト例  
    `curl <WEKO3のURL>/api/v1/records?title=jumps`

- レスポンス
  - ヘッダ
    | キー名        | 値       |
    |---------------|----------|
    | Cache-Control | no-store |
    | Pragma        | no-cache |
    | Expires       | 0        |

  - ボディ  
    Elasticsearchから得られた検索結果のメタデータをRO-Crate形式に変換して返す。
    ただし、ユーザーが設定できるkeyに関しては、要素数によらず配列型に変換して返す。
    ファセット検索による集計結果を返却する。

  - レスポンスボディ例
    ```
    {
      "total_results": 1,
      "count_results": 1,
      "cursor": "15",
      "page": 1,
      "search_results": [
        {
          "id": "15",
          "metadata": {
            "@context": "https://w3id.org/ro/crate/1.1/context",
            "@graph": [
              {
                "@id": "./",
                "@type": "Dataset",
                "datePublished": "2024-11-27T01:13:50+00:00",
                "mainEntity": [],
                "subjectOf": ["quick brown fox jumps over the lazy dog"],
                "hasPart": [{ "@id": "\u5927\u9805\u76ee/" }]
              },
              {
                "@id": "ro-crate-metadata.json",
                "@type": "CreativeWork",
                "conformsTo": { "@id": "https://w3id.org/ro/crate/1.1" },
                "about": { "@id": "./" }
              },
              {
                "@id": "\u5927\u9805\u76ee/",
                "@type": "Dataset",
                "additionalType": "tab",
                "name": "\u5927\u9805\u76ee",
                "subjectOf": ["aaa"],
                "hasPart": [{ "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/" }]
              },
              {
                "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/",
                "@type": "Dataset",
                "additionalType": "section",
                "name": "\u5c0f\u9805\u76ee",
                "hasPart": [
                  { "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/\u8aac\u660e/" }
                ]
              },
              {
                "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/\u8aac\u660e/",
                "@type": "Dataset",
                "additionalType": "subsection",
                "name": "\u8aac\u660e",
                "text": ["2024-11-05"]
              }
            ]
          }
        }
      ],
      "aggregations": {
        "title_facet": {
            "buckets": [
                {
                    "key": "quick brown fox jumps over the lazy dog",
                    "doc_count": 1
                }
            ]
        }
      }
    }
    ```

- 異常系  
  1ページに表示する値がElasticsearchの表示上限の設定値より大きい場合、エラーコードと対応するエラーメッセージをJSON形式で返す。

- 検索文字列とマッチする文字列の例  
  ◯: マッチする、 ✕: マッチしない  
  ただし、括弧による優先度の操作は現在未実装

  |検索文字列\検索対象の文字列      |quick brown|brown quick|quick|
  |---------------------------------|-----------|-----------|-----|
  | quick OR brown                  |◯          |◯          |◯    |
  | quick brown                     |◯          |◯          |✕    |
  | quick brown OR fox jumps        |◯          |◯          |✕    |
  | quick (brown OR fox) jumps      |✕          |✕          |✕    |

#### 更新履歴

  | 日付       | 更新内容                                   |
  |------------|--------------------------------------------|
  | 2023/02/13 | 初版作成                                   |
  | 2024/07/31 | ユーザーが設定できるkeyの変換形式を変更    |
  | 2025/02/14 | OR検索機能、タイトル完全一致検索機能、集計機能の追加 |

### アイテム詳細情報取得用API

#### 目的・用途  
  本APIはアイテムの詳細情報を取得するAPIである。

#### 利用方法  
APIを実行する。

#### 利用可能なロール

  <table>
  <thead>
  <tr>
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
  <tr>
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

#### 機能内容

  - 指定されたアイテムの情報を取得する。

#### 関連モジュール

  - weko_index_tree.rest.py:GetIndex

#### 処理概要

  - OAuth2認証を用いたアクセス制限を行う。
  - ユーザーが持つロールとアイテムの表示権限に従って取得制限を行う。
  - サーバー負荷軽減のため、リクエストのアクセス制限をかける。
  - 多言語対応により、指定された言語でレスポンスを返す。
  - ETag,Last-Modifiedを使用して、以前取得したデータの更新確認を行う。
  - HTTPメソッド  
  GET
  - URL  
    /api/:version/records/:record_id
    | パラメータ | 値                         |
    |------------|----------------------------|
    | version    | バージョン情報             |
    | record_id  | アイテムを一意に識別するID |

- リクエスト
  - ヘッダ
    <table>
    <thead>
    <tr>
    <th>キー名</th>
    <th>値</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Accept-Language</td>
    <td>言語設定<br>
    デフォルトはen</p></td>
    </tr>
    <tr>
    <td>If-None-Match</td>
    <td>1回目のレスポンスヘッダーETagに設定された値</td>
    </tr>
    <tr>
    <td>If-Modified-Since</td>
    <td>1回目のレスポンスヘッダーLast-Modifiedに設定された値</td>
    </tr>
    <tr>
    <td>Authorization</td>
    <td>認可情報</td>
    </tr>
    </tbody>
    </table>

  - クエリ
    | パラメータ | 値                     |
    |------------|------------------------|
    | pretty     | レスポンスの整形フラグ |

  - リクエスト例  
  `curl <WEKO3のURL>/api/v1/records/15`

- レスポンス
  - ヘッダ
    | キー名        | 値                         |
    |---------------|----------------------------|
    | Etag          | アイテム情報のバージョンID |
    | Last-Modified | アイテム情報の更新日時     |

  - ボディ  
  メタデータをRO-Crate形式に変換して返す。
  ユーザーが設定できるkeyに関しては、要素数によらず配列型に変換して返す。
  アイテムに設定されたリクエストメール送信先アドレスの有無をDBのrequest_mail_listテーブルから取得し返却する。

  - レスポンスボディ例
      ```
      {
        "index": "1623632832836",
        "rocrate": {
          "@context": "https://w3id.org/ro/crate/1.1/context",
          "@graph": [
            {
              "@id": "./",
              "@type": "Dataset",
              "datePublished": "2024-11-27T01:22:31+00:00",
              "mainEntity": [],
              "subjectOf": ["quick brown fox jumps over the lazy dog"],
              "hasPart": [{ "@id": "\u5927\u9805\u76ee/" }]
            },
            {
              "@id": "ro-crate-metadata.json",
              "@type": "CreativeWork",
              "conformsTo": { "@id": "https://w3id.org/ro/crate/1.1" },
              "about": { "@id": "./" }
            },
            {
              "@id": "\u5927\u9805\u76ee/",
              "@type": "Dataset",
              "additionalType": "tab",
              "name": "\u5927\u9805\u76ee",
              "subjectOf": ["aaa"],
              "hasPart": [{ "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/" }]
            },
            {
              "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/",
              "@type": "Dataset",
              "additionalType": "section",
              "name": "\u5c0f\u9805\u76ee",
              "hasPart": [
                { "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/\u8aac\u660e/" }
              ]
            },
            {
              "@id": "\u5927\u9805\u76ee/\u5c0f\u9805\u76ee/\u8aac\u660e/",
              "@type": "Dataset",
              "additionalType": "subsection",
              "name": "\u8aac\u660e",
              "text": ["2024-11-05"]
            }
          ]
        },
        "metadata": {
          "Item Type": "\u30c7\u30d5\u30a9\u30eb\u30c8\u30a2\u30a4\u30c6\u30e0\u30bf\u30a4\u30d7\uff08\u30b7\u30f3\u30d7\u30eb\uff09",
          "Title": [
            { "Title": "quick brown fox jumps over the lazy dog", "Language": "en" }
          ],
          "Resource Type": [
            {
              "Resource Type Identifier(Simple)": "http://purl.org/coar/resource_type/c_6501",
              "Resource Type(Simple)": "journal article"
            }
          ],
          "hasRequestmailAddress": false
        }
      }
      ```

#### 更新履歴

| 日付       | 更新内容                                           |
|------------|----------------------------------------------------|
| 2023/09/13 | 初版作成                                           |
| 2024/07/31 | ユーザーが設定できるkeyの変換形式を変更            |
| 2025/02/14 | リクエストボディにメール送信先アドレスの有無を追加 |

### アイテム検索結果一覧取得用API

#### 目的・用途

本APIはアイテムの検索結果の一覧を取得するAPIである。

#### 利用方法

APIを実行する。

#### 利用可能なロール

<table>
<thead>
<tr>
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
<tr>
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

#### 機能内容

  - 検索結果で表示されたアイテムの情報を取得し、TSV形式で返す。

#### 関連モジュール

  - weko_search_ui:rest.py

#### 処理概要

  - OAuth2認証を用いたアクセス制限を行う。
  - ユーザーが持つロールとアイテムの表示権限に従って取得制限を行う。
  - サーバー負荷軽減のため、リクエストのアクセス制限をかける。
  - 多言語対応により、指定された言語でレスポンスを返す。
  - ETag,Last-Modifiedを使用して、以前取得したデータの更新確認を行う。
  - 検索結果の取得処理
    - アイテム検索用APIと同様にして、クエリパラメータで指定された要素で検索を行う。ただし、アイテム検索用APIのクエリパラメータのうちpage, cursor, sizeは使用しない。ファセット検索の絞り込み機能は使用可能であるが、集計機能は使用しない。
    - 検索結果の情報からTSVファイルを作成する。TSVファイルの項目はリクエストボディのJSONで指定する。
    - 作成したTSVファイルを返す。
  - HTTPメソッド  
  POST

- URL  
/api/:version/records/list  

  | パラメータ | 値             |
  |------------|----------------|
  | version    | バージョン情報 |

- リクエスト
  - ヘッダ
    <table>
    <thead>
    <tr>
    <th>キー名</th>
    <th>値</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Accept-Language</td>
    <td>言語設定<br>
    デフォルトはen</td>
    </tr>
    <tr>
    <td>If-None-Match</td>
    <td>1回目のレスポンスヘッダーETagに設定された値</td>
    </tr>
    <tr>
    <td>If-Modified-Since</td>
    <td>1回目のレスポンスヘッダーLast-Modifiedに設定された値</td>
    </tr>
    <tr>
    <td>Authorization</td>
    <td>認可情報</td>
    </tr>
    </tbody>
    </table>

  - クエリ

    | パラメータ | 値 |
    |----|----|
    | q | 検索するキーワード |
    | search_type | 検索する形式 |
    | sort | ソートキー |

    上記に加え、メタデータ項目のパラメータはアイテム検索用APIと同一のものを使用可能とする。

  - ボディ  
  以下をJSON形式で指定する。

    - name  
    レスポンスボディのTSVファイルのヘッダとして出力したい値
    - roCrateKey  
    レスポンスボディのTSVファイルに出力したい値を、RO-Crateマッピング機能で紐づけているRO-Crateのキーで指定する

  - リクエストボディ例
    ```
    [
      {
        "name": {
          "en": "title",
          "ja": "タイトル"
        },
          "roCrateKey": "subjectOf"
        },
        {
        "name": {
          "en": "creator",
          "ja": "作成者"
        },
        "roCrateKey": "creator"
      }
    ]
    ```

  - リクエスト例
    ```
    curl -X POST -H "Content-Type: application/json" <WEKO3のURL>/api/v1/records/list?title=fox -d '[{"name":{"en":"title","ja":"タイトル"},"roCrateKey":"subjectOf"},{"name":{"en":"creator","ja":"作成者"},"roCrateKey":"creator"}]'
    ```

- レスポンス
  - ヘッダ
    | キー名        | 値                         |
    |---------------|----------------------------|
    | Etag          | アイテム情報のバージョンID |
    | Last-Modified | アイテム情報の更新日時     |
  - ボディ  
  TSVファイルデータ (検索結果をリクエストボディで指定した形式に変換したもの)

  - レスポンスボディ例
    ```
    title	creator
    quick brown fox	John Smith
    quick brown fox jumps over the lazy dog	John Smith
    ```

#### 更新履歴

| 日付       | 更新内容                                   |
|------------|--------------------------------------------|
| 2024/01/22 | 初版作成                                   |
| 2024/01/22 | レビュー指摘事項対応                       |
| 2025/02/14 | OR検索機能、タイトル完全一致検索機能の追加 |
