
npx honkit init admin_manual
npx honkit serve
npx honkit build

sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin version=4.23.0

npx honkit pdf . ../ADMIN.pdf


```
cd spec/
node app.js
cd ../
npx honkit pdf spec/base spec/pdf/spec.pdf
npx honkit html spec/base spec/html
npx honkit pdf manuals/ADMIN/base manuals/ADMIN/pdf/admin.pdf
npx honkit html manuals/ADMIN/base manuals/ADMIN/html
npx honkit pdf manuals/USER/base manuals/ADMIN/pdf/admin.pdf
npx honkit html manuals/USER/base manuals/ADMIN/html
```