# WEKO3 documents


```
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin version=4.23.0
```

## ドキュメントのビルド

### ユーザ操作マニュアル

```
rm -r build/user
mkdir -p build/user/pdf
mkdir -p build/user/html
npx honkit pdf manuals/USER/base build/user/pdf/user.pdf
npx honkit build manuals/USER/base build/user/html/
```

### システム管理マニュアル

```
rm -r build/admin
mkdir -p build/admin/pdf
mkdir -p build/admin/html
npx honkit pdf manuals/ADMIN/base build/admin/pdf/admin.pdf
npx honkit build manuals/ADMIN/base build/admin/html
```

### 機能仕様書のビルド

```
rm -r build/spec
mkdir -p build/spec/pdf
mkdir -p build/spec/html
npx honkit pdf spec/base build/spec/spec.pdf
npx honkit build spec/base build/spec/html
```



