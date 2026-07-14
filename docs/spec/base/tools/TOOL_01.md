### Render

#### 目的・用途

指定したアイテムタイプの「render」定義（描画・入力設定の構造）を取得する機能。アイテムタイプ編集画面の描画や他アプリ連携に利用される。

#### 利用方法

`GET /admin/itemtypes/{item_type_id}/render` を実行する（管理画面配下のビュー。OAuth を用いる REST API `/api/...` ではない）。

#### 機能内容

- 指定アイテムタイプの `render` 定義を返す。パスパラメータ `item_type_id`（int）、HTTPメソッド GET。
- 返却されるのは `weko_records.models.ItemType.render` カラム（JSON）で、`meta_fix`（pubdate 等のシステム項目）・`meta_list`（プロパティ毎の入力設定）・`table_row` / `schemaeditor` 等を含む。render 定義のサンプルは [その他: Render (SCHEMA_1_1)](../other/SCHEMA_1_1.md) を参照。

#### 関連モジュール

- weko-itemtypes-ui（ハンドラ `admin.ItemTypeMetaDataView.render_itemtype`、Flask-Admin `@expose('/<int:item_type_id>/render')`）
- weko-records（`ItemType.render` カラムに格納）

> 注：`tool/` と `tools/` は同一内容（Render）の重複ディレクトリ。[tool/TOOL_01.md](../tool/TOOL_01.md) と同じ。

#### 更新履歴

| 日付 | GithubコミットID | 更新内容 |
| :--- | :---: | :---: |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。Renderエンドポイント・ハンドラ・データ構造・関連モジュールを記入。tool/ との重複を注記 |
