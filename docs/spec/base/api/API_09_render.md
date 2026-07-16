# Render

## 目的・用途

他のウェブアプリがweko3のリソースにアクセスできるようAPI利用を承認することを目的としている。

## 利用方法

API-8-5の機能を用いて、OAuthアプリケーション、またはトークンを登録する。その後、設定された値を利用してAPI接続の設定を行う。

## 機能内容

`GET /admin/itemtypes/{item_type_id}/render`

- 指定したアイテムタイプの描画（render）用定義を返す。
- 本エンドポイントは管理画面（`/admin`）配下のFlask-Adminビューであり、OAuthを用いるREST API（`/api/...`）ではない。パスパラメータ `item_type_id`（int）、HTTPメソッドはGET。

## 関連モジュール

- weko-itemtypes-ui（`admin.py` の `render_itemtype`。Flask-Admin の `@expose('/<int:item_type_id>/render', methods=['GET'])`）

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
| ---- | ---- | ---- |
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
| 2024/07/1 | 7733de131da9ad59ab591b2df1c70ddefcfcad98 | v1.0.7対応 |
| 2026/07/14 |  | 実装(v2.0.2)と突き合わせ。ハンドラ`weko_itemtypes_ui.admin.render_itemtype`、管理画面ビュー（RESTでない）である旨・メソッド・パラメータを追記 |
