#!/bin/bash

echo "build admin manual"
rm -r ./build/admin
mkdir -p ./build/admin/pdf
mkdir -p ./build/admin/html
npx honkit pdf $(pwd)/manuals/ADMIN/base $(pwd)/build/admin/pdf/admin.pdf
npx honkit build $(pwd)/manuals/ADMIN/base $(pwd)/build/admin/html