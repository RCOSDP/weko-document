# 撮影用サンプルデータの登録スクリプト（v2.1.0 で使用）

ローカル環境（wekov2、release_v2.1.0）でスクリーンショットを撮るために使ったもの。**v2.1.0 の画面・データに合わせて書いてあるので、次回はセレクタや ID（アイテムタイプ、ワークフロー、インデックス等）を確認・修正してから使う。** 登録したものは必ず作業フォルダの `sample_data_log.md` に記録する（種類、ID、作成方法、削除方法と順序）。

| スクリプト | 登録するもの | 実行方法 |
|---|---|---|
| `mk_index.py` | インデックス（名前に screenshot-sample） | web コンテナで `invenio shell` に流す（`docker exec -i <web> bash -c "cd /code && invenio shell" < mk_index.py`） |
| `mk_location.py` | S3 ロケーション（ダミーのキー） | 同上 |
| `mk_multipart.py` | バケットと Multipart Object（通常の作成処理が失敗したため ORM で直接登録。最終手段） | 同上 |
| `mk_workflow.js` | ワークフロー | `WEKO_CRED=<.cred> node mk_workflow.js`（Playwright、管理画面操作） |
| `mk_app.js` | OAuth アプリケーション | 同上 |
| `mk_mapping.js` | JSON-LD マッピング | 同上 |
| `mk_sword.js` | SWORD JSON-LD 設定（アプリ・ワークフロー・マッピングが必要） | 同上 |
| `mk_activity.js` | ワークフロー経由の承認待ちアクティビティ | 同上 |
| `import_items.js` | 一括インポートでアイテムを登録し、［結果］タブを撮る（`node import_items.js <zip> <ja|en> go <out.png>`） | 同上 |
| `lib.js` | 上記 .js の共通部品（ログイン、言語切替、ページ遷移） | — |

- アイテムは管理画面の一括インポート（TSV）で登録した（`import_items.js`。インポート結果画面の撮影も兼ねる）。
- 削除は依存関係の逆順（アクティビティ処理 → SWORD 設定 → マッピング・アプリ・ワークフロー → アイテム・インデックス → ロケーション・バケット）。
- `.cred`（`email=`／`password=`）はリポジトリ外に置き、`WEKO_CRED` で指定する。
