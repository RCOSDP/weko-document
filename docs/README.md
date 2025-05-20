# WEKO3 documents


```
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin version=4.23.0
```

## build

```
npx honkit pdf spec/base spec/pdf/spec.pdf
npx honkit build spec/base spec/html
npx honkit pdf manuals/ADMIN/base manuals/ADMIN/pdf/admin.pdf
npx honkit html manuals/ADMIN/base manuals/ADMIN/html
npx honkit pdf manuals/USER/base manuals/ADMIN/pdf/admin.pdf
npx honkit html manuals/USER/base manuals/ADMIN/html
```