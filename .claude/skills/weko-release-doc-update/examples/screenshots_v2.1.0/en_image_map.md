# 日本語版差し替え画像 → 英語版画像の対応（release_v2.1.0）

英語版：`docs/manuals_en/ADMIN/admin_manual.md`、`docs/manuals_en/USER/user_manual.md`（画像は `docs/manuals_en/{ADMIN,USER}/media/media/`）。
対応付けは節の対応と、英語版の画像を目視して同じ画面であることを確認して行った。

## ADMIN（日本語版 docs/manuals/ADMIN/base/README.md）

| 日本語画像 | 英語画像 | 英語版の行 | 英語版の節 | 状態 |
|---|---|---|---|---|
| image4 | image4.png | 1684 | Access the Administration screen | 撮影・注記済み（赤枠3＋矢印2） |
| image88 | image86.png | 9215 | Import items（"Result" タブ） | **未撮影**：Result タブはインポートを実行しないと表示されない（データが変わるため実施せず）。注記なし |
| image189 | image188.png | 11186 | Add an author ID（手順2） | 撮影・注記済み（赤枠：氏名行） |
| image199 | image197.png | 11468 | View external author ID Prefixes | 撮影・注記済み（赤枠：ID Prefix タブ） |
| image200 | image198.png | 11512 | Add an external author ID Prefix | 撮影・注記済み（赤枠：追加行）。英語版の古い画像に合わせ Scheme のプルダウンは閉じた状態 |
| image204 | （なし） | 11648–11709 | Manage affiliation ID Prefixes | 対象外：英語版の節に画像が無い |
| image259 | image256.png | 13285 | Edit a workflow（手順2） | 撮影済み（注記なし） |
| image326 | image323.png | 14703 | Create a Location | 撮影・注記済み（赤枠：Name〜Quota Size） |
| image327 | image324.png | 14751 | Edit a Location | 撮影・注記済み（赤枠：Name〜Default） |
| image330 | image327.png | 14793 | View Multipart Objects | 撮影・注記済み（赤枠：List タブ） |
| image365 | image361.png | 15592 | Add a user | 撮影・注記済み（赤枠：入力欄） |
| image366 | image362.png | 15623 | Edit a user | 撮影・注記済み（赤枠：入力欄） |
| image370 | image366.png | 15699 | Configure the author display setting | 撮影・注記済み（赤枠：ラジオボタン2行。英語版の古い画像は Save を含まない） |
| image406 | image397.png | 16706 | Configure the site information | 撮影済み（注記なし） |
| image418 | image409.png | 17507 | Allow Shibboleth users | 撮影・注記済み（赤枠：有効/無効ラジオ） |
| image457 | （なし） | 14357 | SWORD API > Set up TSV/CSV | 対象外：英語版の節に画像が無い |
| image458 | （なし） | 14379 | SWORD API > Set up XML | 対象外：英語版の節に画像が無い |
| image460 | （なし） | 14404 | SWORD API > Create a JSON-LD setting | 対象外：英語版の節に画像が無い |
| image480 | （なし） | 18547 | Manage the CRIS linkage > Set up the merge mode | 対象外：英語版の節に画像が無い |
| image493.png | （なし） | 7933 | Edit or delete a JSON-LD mapping | 対象外：英語版の節に画像が無い |
| （image493.jpeg） | （なし） | 7414 | Troubleshooting item types | 参考：日本語版の差し替え対象外の別画像。英語版にも画像なし |
| storage000〜002 | （なし） | 14820–14900 | Use the institutional storage feature | 対象外：英語版の節に画像が無く、英語版 media に storage フォルダも無い |

## USER（日本語版 docs/manuals/USER/base/README.md）

| 日本語画像 | 英語画像 | 英語版の行 | 英語版の節 | 状態 |
|---|---|---|---|---|
| image134 | image117.png | 2138 | Register items > Automatically populate metadata（"Automatic metadata input" ダイアログ） | **未撮影**：アクティビティの登録画面を開く必要があり、既存アクティビティは承認待ちで登録画面に戻れない。新規アクティビティ作成はデータ変更になるため実施せず |
| image266 | image235.png（**図 7-1**） | 4228 | Export items（Figure 7-1. The "Items to Export" screen） | **未撮影**：英語セッションでは検索結果が0件になり Export 画面へ進めない（下記）。指定案は `annot_en_user.json`（未検証） |
| image307 | （なし） | 4753 | Workspace > Export the item list | 対象外：英語版ワークスペース章に画像が無い |
| image309 | （なし） | 4753 | 同上 | 対象外 |
| image312 | （なし） | 4789 | Register an item quickly | 対象外 |
| image313 | （なし） | 4789 | 同上 | 対象外 |
| image314 | （なし） | 4789 | 同上 | 対象外 |
| image316 | （なし） | 4701 | Workspace > View the item list | 対象外 |

依頼項目2「英語版ユーザマニュアルの図 7-1」は image235（= 日本語版 image266 の対応先）と同じもの。

## 英語画面で検索結果が0件になる件
英語セッションではトップのインデックスツリーに「Sample Index」しか表示されず（日本語では screenshot-sample インデックス、テスト大学 学術情報リポジトリ も表示される）、インデックス検索・全文検索とも結果0件。
redis の `index_tree_view_weko3.example.org_en`（TTL なし）に screenshot-sample インデックス（1791272758678）が含まれておらず、英語用のツリーキャッシュが古いままと見られる（`_ja` 側には含まれる）。
キャッシュの更新は手元環境の共有リソース変更になるため実施していない（自動モードでも拒否された）。
