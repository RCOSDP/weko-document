#!/bin/bash

echo "build admin manual (English)"
rm -r ./build/admin_en
mkdir -p ./build/admin_en/pdf
mkdir -p ./build/admin_en/html
npx honkit pdf $(pwd)/manuals_en/ADMIN $(pwd)/build/admin_en/pdf/admin_en.pdf
npx honkit build $(pwd)/manuals_en/ADMIN $(pwd)/build/admin_en/html
