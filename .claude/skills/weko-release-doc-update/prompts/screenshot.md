# スクリーンショットの撮影と注記
まず `{{WORKDIR}}/SCREENSHOT_RULES.md` を読み、そのルールに従ってください。
- 対象：{{IMAGE_LIST}}（差し替えが必要な画像。マニュアルごと）
- 撮影：`scripts/capture.js`（全画面、幅1180）。古い画像を見て同じ状態を再現。必要なサンプルデータは `screenshot-sample` 付きで登録し `sample_data_log.md` に記録。
- 注記：古い画像の赤枠・矢印・番号を `annotate`／`crop` で同じ部品に描く。番号は本文の表の現在の項番。
- 出力：`out/<lang>_annot_<manual>/`、比較ページ `review/<lang>_annot_<manual>/index.html`（`scripts/stage2.py`）、targets JSON を残す。
- リポジトリは変更しない（差し替えはレビュー後に取りまとめ役が行う）。
- 最終報告：撮影・注記した画像、注記なし、撮影／再現できなかったものと理由、登録したサンプルデータ、画面が大きく変わり本文も確認が必要なもの。
