# 画面背景色

## 目的・用途

本機能は、画面背景色表示を設定する機能である

## 利用方法

【Administration > 設定(Setting) > 画面背景色(Style)画面】を開き、色を選択後「保存」ボタンを押下する。

## 利用可能なロール

| ロール | システム管理者 | リポジトリ管理者 | コミュニティ管理者 | 登録ユーザー | 一般ユーザー | ゲスト(未ログイン) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 利用可否 | ○ | 〇 | | | | |

## 機能内容

画面背景色表示を設定する

- 【Administration > 設定(Setting) > 画面背景色(Style)画面】に画面背景色表示を設定する。
  - 現在選択している色を表示する。
  - 背景１の下にある四角をクリックすると、背景色を設定できる。
  - 画面背景色表示の設定は、背景色をカラーピッカーから選択できる。
    - また、背景色をカラーモデルで指定できる。
      対応しているカラーモデル：RGB、HSL、HEX
  - 「保存」（Save）ボタンを押すと、設定内容を保存し、メッセージを画面上部に表示する。
    メッセージ：「Successfully update color.」

## 関連モジュール

- weko_theme

## 処理概要

画面背景色表示について

- 【Administration > 設定 > 画面背景色】画面を開く。この操作によって、weko_admin.templates.weko_admin.admin.block_styleにてweko_admin.admin.StyleSettingView.indexがGETで呼び出され、変数WEKO_THEME_INSTANCE_DATA_DIRに保存されているディレクトリの_variables.scssより現在の色設定を取得し、画面に表示する。

画面背景色設定

- 背景１下の四角を押下した時、weko_admin.templates.weko_admin.admin.block_style.htmlよりカラーピッカーが表示される。このとき表示される色は現在設定されている色で表示される。
- 色を選択し、「保存」ボタンを押下する。この操作によって、weko_admin.admin.StyleSettingView.indexがPUTで呼び出され、背景１で選択されている色の数値を変数WEKO_THEME_INSTANCE_DATA_DIRに保存されているディレクトリの_variables.scssに保存する。
- なお、変数WEKO_THEME_INSTANCE_DATA_DIRはweko_theme.config.pyに保存されている変数である。

## 更新履歴

| 日付 | GitHubコミットID | 更新内容 |
|:---:|:---:|:---:|
| 2023/08/31 | 353ba1deb094af5056a58bb40f07596b8e95a562 | 初版作成 |
