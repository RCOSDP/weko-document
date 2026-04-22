# WEKO3 documents

## ビルド環境の構築

動作確認環境は以下の通り。

```
$ node --version
v24.6.0
$ npm --version
11.5.2
$ calibre --version
calibre (calibre 4.23)
```

nvmをインストールする。

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
```

calibreをインストールする。

```
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh
```

関連パッケージをインストールする。

```
npm install
```

## ドキュメントのビルド

### ユーザ操作マニュアル

```
bash build_user_manual.sh
```

### システム管理マニュアル

```
bash build_admin_manual.sh
```

### 機能仕様書のビルド

```
bash build_spec.sh
```


### JAIRO Cloud（WEKO3）登録ガイドのビルド

```
bash build_guide.sh
```





