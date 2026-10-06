# スクリーンショット撮影・注記ルール

## 環境
- `{{RELEASE_REF}}` で動くローカル環境（v2.1.0 では wekov2、`https://localhost:8443`）。自己署名証明書なので `ignoreHTTPSErrors`。
- 撮影用の管理者アカウントを作る（例）：
  ```
  docker exec <web> bash -c "invenio users create screenshot-admin@example.org --password '<random>' --active; invenio roles add screenshot-admin@example.org 'System Administrator'"
  ```
  パスワードは作業フォルダの `.cred`（`email=` / `password=` の2行、権限 600）にだけ置く。リポジトリには入れない。
- Playwright：作業フォルダで `npm install playwright` し、`~/.cache/ms-playwright/chromium-*/chrome-linux/chrome` を `CHROME` 環境変数で指定（バージョン不一致でもキャッシュ済みのものを使える）。

## 撮影
- `scripts/capture.js <targets.json> <outdir> ja|en`。ビューポート幅 1180、**全画面（fullPage）**。
- targets の要素：`{image, url, wait?, steps?: [{click|fill|clear|select|check|hover|press|eval|waitFor|goto, ...}], fullPage?, clip?, fullViewport?, annotate?, crop?}`
- フォームに自動で入る値（パスワード欄など）は `clear` してから撮る。
- 撮る前に**古い画像を見て**、同じタブ・同じ状態（開いたメニュー、入力例、ダイアログ）を再現する。ドロップダウンを開いた状態は撮れないので、選択肢をページ上に展開する等で代替する。
- ADMIN と USER で同名の画像（image134 など）があるので、出力フォルダはマニュアルごとに分ける。

## サンプルデータ
- 登録には `scripts/sample_data/` のスクリプトを流用できる（v2.1.0 向け。README 参照）。
- 撮影に必要なデータ（著者、アイテム、インデックス、ロケーション、OAuth アプリ、SWORD/JSON-LD 設定、承認待ちアクティビティ等）は登録してよいが、名前に `screenshot-sample` を含め、**すべて `sample_data_log.md` に記録**（種類、ID、作成方法、削除方法と順序）。
- 既存データ・既存ユーザ・既存設定は変えない。設定画面のために値を変えたら撮影後に戻して記録。DB 直接書き換えは最後の手段で、行ったら記録。
- 外部サービス（学認、GakuNin RDM、CrossRef、arXiv 等）へ実通信はしない。撮れない状態は「撮影できなかったもの」として報告。

## 注記（赤枠・矢印・番号）
- 古い画像の注記を読み取り、`scripts/annotate.js` の指定で新しい画面の**同じ部品**に描いてから撮る（座標の移植はしない）。
  - `{id?, box: [locator...], pad?}`：赤枠
  - `{arrow: {from, to, fromSide?, toSide?, elbow?: 'v'|'h', at?: 0..1, straight?: 'v'|'h'}}`：赤い矢印（from/to は box の id かロケーター）
  - `{callout: {target, label, side?, dist?}}`：青い番号の吹き出し。番号は**マニュアル本文の表の現在の項番**に合わせる
  - `crop: {around: [locator...], pad}`：古い画像が部分切り出しの場合
- ロケーターは表示テキストで指定するのが確実（例 `text="参加リクエスト" >> visible=true`、`button:has-text("保存") >> visible=true`）。
- 撮った画像は必ず目視で確認し、ずれ・重なりがあれば直す。注記が指す部品が新しい画面に無い場合は付けずに報告。
- 使った targets JSON は残す（英語版で同じ指定を流用する）。
- データや設定を変えないと再現できない画面（承認待ちを進める必要がある等）は、撮影済みの画像に `scripts/overlay.js` で注記だけを描く（矩形を座標で指定）。
- v2.1.0 で使った指定の例：`examples/screenshots_v2.1.0/annot_all_*.json`（日本語版の33枚分）。

## 英語版
- 英語画面は `capture.js … en`（`/lang/en` に切り替える）。最初の1枚で英語になっているか必ず確認する。クッキー同意のボタンは「That's ok」。
- **英語版は画像番号が日本語版と違う。** 日本語版で差し替える画像が使われている節に対応する英語版の節を探し、その節の画像を見て同じ画面か確かめて対応付ける。対応表を残す（例 `examples/screenshots_v2.1.0/en_image_map.md`）。英語版に画像が無い節（英語版で新しく書いた章など）は対象外。
- 日本語版の撮影指定を流用し、ロケーターを英語画面の文言に書き換える。注記は**英語版の古い画像**に合わせ、番号は英語版の表の項番にする。
- 出力ファイル名は英語版の画像名。比較ページは英語版のマニュアル・media を指定して作る。
- 撮影のついでに、英語画面に残る日本語・生のキー・綴り誤り（翻訳漏れ）を記録して実装側へ報告する。

## つまずきやすい点
- **英語画面で検索結果が0件になる**：インデックスツリーのキャッシュが言語ごとに Redis にあり（`index_tree_view_<host>_<lang>`、有効期限なし）、撮影用インデックスを追加した後も英語用が古いままになることがある。キーを削除すると次の表示で作り直される（**共有環境の変更なのでユーザーの了承を得てから**、取りまとめ役が実行し記録する）。
- **アクティビティのロック**：1ユーザーは同時に1つのアクティビティしか開けない。調査用のスクリプトで開いたまま終わると「One user cannot open multiple activities simultaneously」になる。自分のロックは画面の「Force Unlock」（`#user_locked_btn` → `#btn_unlock`）で解除してから撮る（`examples/screenshots_v2.1.0/annot_en_user117.json` の steps 参照）。
- **Angular の画面は読み込みに時間がかかる**：`waitFor` で目的の要素を待ってから操作する。同じ文言の要素が複数ある（モーダルの見出しとボタン等）ときは `button:has-text(...)` のように絞る。
- **サブエージェントの権限**：手元環境へのデータ登録やキャッシュ削除は、ユーザーが了承していても、サブエージェントでは自動の権限判定で止められることがある。その場合は取りまとめ役が（ユーザーの了承の範囲で）自分で実行する。
- **差し替えた後に比較ページを作り直すと**「現在」の列も新しい画像になる。比較ページは差し替え前に作るか、git の HEAD から旧画像を取り出して使う。

## レビューと差し替え
- `scripts/stage2.py <manual.md> <media dir> <newdir> <outdir>`：新旧をマニュアルの登場順（`NNNN_imageXXX__current/new`）に並べ、`index.html` の比較ページと `index.json` を作る（同名で拡張子違いの参照を除外するときは `SKIP_REFS=image493.jpeg`）。
- 差し替えはレビュー後に `scripts/apply_screenshots.py <review dir> <media dir> [--apply] [--only …]`（既定は試行のみ。PNG は上書き、現在が JPEG のものは `--rewrite-ext <manual.md>` を付けたときだけ PNG にして参照を書き換える）。
- 画面が大きく変わった画像は、本文の記述も合っているかを確認する。
