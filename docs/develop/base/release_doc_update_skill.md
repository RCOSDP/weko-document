# ドキュメント更新スキルの使い方

WEKO3 の新しいリリースに合わせて weko-document を更新するための Claude Code のスキル `weko-release-doc-update` の使い方です。作業の流れそのものは「[リリースに合わせたドキュメント更新の手順](release_doc_update.md)」を参照してください。

## 1. スキルでできること

- 機能仕様書・マニュアル（日本語／英語）・登録ガイドを、実装のリリースブランチと突き合わせて直す
- 実装に有って文書に無い記述を追記する（英語版に無い章を日本語版から書き起こす、を含む）
- 新しいバージョンのアップデート手順書を作る
- 今回のバージョンで変わった箇所に【vX.Y.Z】タグを付ける
- 手順番号・節番号の参照・表／図番号の崩れを直す
- 機能仕様書・マニュアル（日本語／英語）・登録ガイドを honkit でビルドし、リンク切れ・画像の欠落を確認する
- スクリーンショットを撮り直し、古い画像と同じ赤枠・矢印・番号を描いて差し替える
- カテゴリ単位でコミットし、push する（push は指示したときだけ）

## 2. 準備

| 必要なもの | 内容 |
|---|---|
| Claude Code | weko-document のリポジトリで起動する。スキルは `.claude/skills/weko-release-doc-update/` にあり、リポジトリを開くと自動で読み込まれる |
| weko-document | 作業ブランチ（例 `develop_v2.1.0`）を checkout しておく |
| 実装リポジトリ | RCOSDP/weko の clone（例 `/home/mhaya/weko`）。`git fetch` でリリースブランチとタグを取得しておく。スキルは checkout を変えず、ソースを作業フォルダに展開して読む |
| 撮影用の環境（スクリーンショットを撮る場合） | リリースブランチで動くローカル環境（例 docker の wekov2、`https://localhost:8443`）。Node.js と Playwright 用の Chromium（`~/.cache/ms-playwright`）があること |

## 3. 呼び出し方

Claude Code に次のように依頼します。スキル名を含めなくても、内容から自動で選ばれます。明示する場合は `/weko-release-doc-update` と入力します。

```
v2.2.0 向けにドキュメントを更新して。実装は RCOSDP/weko の release_v2.2.0。
```

依頼の際に、次の値を伝えると最初の確認が早く済みます（伝えなければ Claude が git の履歴から候補を出して確認します）。

| 値 | 例 |
|---|---|
| 今回のバージョン | v2.2.0 |
| 実装のリリースブランチ | release_v2.2.0 |
| 直前のリリースタグ（タグ付けの判定基準） | v2.1.0 |
| 前回ドキュメントを突合した実装のコミット | （前回のリリースコミット） |
| weko-document の作業ブランチ | develop_v2.2.0 |
| 撮影用の環境 | wekov2（https://localhost:8443） |

## 4. 進め方の例

作業は大きいので、段階ごとに依頼して、結果を確認しながら進めるのがおすすめです。

1. **棚卸し**：「release_v2.2.0 で前回から何が変わったか棚卸しして」
2. **仕様書・マニュアル・ガイドの突合**：「マニュアル、機能仕様書、ガイドラインを release_v2.2.0 と突き合わせて、齟齬を直して足りない記述を追記して」
   - 大きいマニュアルは章ごとに分けて並列に作業し、終わったら結合して目次・版数・改定履歴を更新します。
3. **アップデート手順書**：「v2.1.0 から v2.2.0 へのアップデート手順書を作って」
4. **英語版**：「日本語版の修正を英語版に反映して」「英語版に無い章を日本語版から生成して」
5. **タグ付け**：「v2.2.0 で変わった箇所に【v2.2.0】タグを付けて」（見出しには付けません）
6. **番号と参照**：「手順番号の崩れと節番号の参照を直して」
7. **スクリーンショット**：「撮影用の管理者アカウントを作って、差し替えが必要な画像を撮って注記を付けて」→ 比較ページを確認 →「差し替えて」
8. **ビルド確認**：「ビルドしてリンク切れを確認して」
9. **コミット**：「カテゴリ単位でコミットして push して」

各段階の終わりに、Claude は「直した齟齬」「追記した内容」「実装側の不具合と思われる点」「確認が必要な点」を報告します。

## 5. 確認を求められること（自動では進めない）

次の操作は、ユーザーの了承を得てから行います。

- コミット後の push
- 撮影用のローカル環境での操作（撮影用アカウントの作成、サンプルデータの登録、キャッシュの削除、アクティビティの作成など）
- 判断が分かれる内容（例：画面に無い機能の記述を削るか「未リリース」と書くか）

サブエージェントが手元環境を変える操作は、了承があっても権限の判定で止められることがあります。その場合は取りまとめ役（メインのセッション）が実行します。

## 6. スクリーンショットだけ使う場合

スクリプトは単独でも使えます（作業フォルダで `npm install playwright` をしたうえで実行）。

```
# 撮影用アカウントの情報（リポジトリの外に置く）
printf 'email=screenshot-admin@example.org\npassword=...\n' > ~/weko-shots/.cred && chmod 600 ~/weko-shots/.cred
export WEKO_CRED=~/weko-shots/.cred

# 撮影（targets.json に URL・操作・注記を書く。例は examples/screenshots_v2.1.0/）
node .claude/skills/weko-release-doc-update/scripts/capture.js targets.json out/ja ja

# 比較ページ（新旧をマニュアルの登場順に並べる）
python3 .claude/skills/weko-release-doc-update/scripts/stage2.py docs/manuals/ADMIN/base/README.md docs/manuals/ADMIN/base/media/media out/ja review/ja_admin

# 差し替え（--apply を付けないと表示だけ）
python3 .claude/skills/weko-release-doc-update/scripts/apply_screenshots.py review/ja_admin docs/manuals/ADMIN/base/media/media --apply
```

注記の書き方（赤枠・矢印・番号の吹き出し・切り出し）は `rules/SCREENSHOT_RULES.md` を参照してください。

## 7. 単独で使える検証スクリプト

```
# 見出しが変わっていないか、タグ数、目次の連番とリンク先を確認
python3 .claude/skills/weko-release-doc-update/scripts/verify_manual.py --tag '【v2.1.0】' docs/manuals/ADMIN/base/README.md

# 英語版の表・図番号が章ごとに連番か確認
python3 .claude/skills/weko-release-doc-update/scripts/caption_check.py docs/manuals_en/USER/user_manual.md
```

## 8. ビルドしてリンク切れを確認する

機能仕様書・管理者マニュアル・ユーザーマニュアル・登録ガイド・英語版マニュアル（管理者・ユーザー）を honkit でビルドし、HTML のリンク切れを確認します。Claude に「ビルドして確認して」と依頼するか、weko-document のルートで次を実行します。

```
# 分岐点（例 main）もビルドし、そこから増えた問題だけを数える
.claude/skills/weko-release-doc-update/scripts/build_docs.sh --compare main --work ~/weko-docbuild

# 一部の本だけ／PDF も作る（PDF は calibre の ebook-convert が必要）
.claude/skills/weko-release-doc-update/scripts/build_docs.sh admin user --pdf
```

- 出力は `docs/build/<本>/html`（`.gitignore` 済み）、ログは `--work` のフォルダです。
- 初回は `npm ci` で honkit を入れます。arm64 では puppeteer の Chromium が無いので、そのダウンロードを省いて入れます。`package-lock.json` は変わりません。
- 結果の見方：

| 種類 | 意味 | 扱い |
|---|---|---|
| PAGE | リンク先のページが無い | 新しいものは直す |
| ANCHOR | リンク先の見出しが無い（GitHub でも切れる） | 新しいものは直す |
| SLUG | GitHub では効くが honkit のサイトでは切れるアンカー（honkit は全角括弧・中黒を残し、`_` を消し、同名見出しに `-1` を付けない） | `add_anchors.py` で見出しの直前に `<a id="…"></a>` を足して直す（見出しは変えない）。`--strict` で失敗扱いにできる |
| IMAGE | 画像ファイルが無い | 新しいものは直す |

  `new` が今回増えた問題、`existing` は分岐点に既にあった問題です。新しい PAGE／ANCHOR／IMAGE があるか、ビルドが終わらなければ終了コード 1 になります。
- GitHub でのみ有効なアンカー（SLUG）は次で直します（先にビルドしておく）。

  ```
  python3 .claude/skills/weko-release-doc-update/scripts/add_anchors.py docs/spec/base docs/build/spec/html --apply
  ```

- ログに出る shelljs の警告、`prism-Python.js` が見つからないエラー、deprecated 警告は、最後に「generation finished with success」があれば問題ありません。
- 本の名前は `spec`、`admin`、`user`、`GUIDE`、`admin_en`、`user_en` です。開発者向け文書・運用文書は book.json が無いため対象外です。
- ビルド結果は別リポジトリに登録して github.io で公開しているので、公開サイトで切れるリンクを残さないよう、SLUG も直します。

## 9. スキルの中身

| 場所 | 内容 |
|---|---|
| `SKILL.md` | 手順の全体、最初に決める値、作業の原則 |
| `LESSONS.md` | これまでの作業で得た注意点 |
| `rules/` | 作業ルール（共通、タグ付け、英語版生成、撮影）。`{{...}}` を今回の値に置き換えて使う |
| `prompts/` | 作業の種類ごとの依頼文の雛形 |
| `scripts/` | 差し込み、番号の振り直し、検証、ビルドとリンク切れ確認、撮影、注記、比較ページ、差し替え、撮影用サンプルデータの登録 |
| `examples/` | v2.1.0 での撮影・注記の指定、日本語版と英語版の画像の対応表 |

## 10. 注意

- 作業記録（突合のメモ、計画、進捗）は作業フォルダに出力し、リポジトリには入れません（`.gitignore` 済み）。
- 撮影用アカウントのパスワードはリポジトリの外に置きます。
- スキルを使って新しい教訓が得られたら、`LESSONS.md` や `rules/` に追記して次回に引き継いでください。
