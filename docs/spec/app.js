const fs = require('fs').promises;
const path = require('path');
 
async function main (){
 
  // SUMMARY.md から結合する Markdown ファイル群を取得
  const filepath = path.resolve(__dirname , './base/SUMMARY.md');
  const message = await fs.readFile(filepath, {encoding: 'utf-8'});
  // Markdown のリンク記法の配列で入ってくる
  let resultMarkdownLinkList = message.match(/\[(.*)\]\((.*)\)/gm);
  console.log(resultMarkdownLinkList);
 
  // 大量に取得してしまうと確認がしにくいので、いったん取得後に数件に限定する処理
  // チューニング用
  /*
  resultMarkdownLinkList = [
    resultMarkdownLinkList[0],
    resultMarkdownLinkList[1],
    resultMarkdownLinkList[2]
  ]
  */
 
  // ファイルを結合して README.md 1ファイルに集約
  let targetContent = "";
  let targetContentAll = "";
  for(let i = 0; i < resultMarkdownLinkList.length; i++){
    const targetMatchResult = resultMarkdownLinkList[i];
 
    // Markdown のリンク記法からリンクタイトルとファイルパスを抽出
    const regexp = /\[(.*)\]\((.*)\)/gm;
    const match = regexp.exec(targetMatchResult);
    // console.log(match[1],match[2]);
    const targetSummaryTitle = match[1];
    const targetResolveFilepath = match[2];
 
    // 相対パス化
    const targetFilepath = path.resolve(__dirname , './base/' , targetResolveFilepath);
 
    // 非同期でコンテンツ読み込み
    targetContent = await fs.readFile(targetFilepath, {encoding: 'utf-8'});
    console.log('----');
    console.log(targetContent.substr(0,100));
 
    // コンテンツ連結
    targetContentAll += targetContent;
  }
 
  console.log('----');
  console.log('コンテンツ書き込み');
  console.log('----');
 
  // pdf というフォルダに格納する
  // この pdf フォルダを honkit で書き出し
  const filepathMainContent = path.resolve(__dirname , './pdf/' , 'README.md');
 
  // コンテンツ書き込み
  await fs.writeFile(filepathMainContent,targetContentAll);
}
 
main();