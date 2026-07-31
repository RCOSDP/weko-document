#!/bin/bash

echo "build GUIDE manual"
rm -r ./build/GUIDE
mkdir -p ./build/GUIDE/pdf
mkdir -p ./build/GUIDE/html
npx honkit pdf $(pwd)/manuals/GUIDE/base $(pwd)/build/GUIDE/pdf/GUIDE.pdf
npx honkit build $(pwd)/manuals/GUIDE/base $(pwd)/build/GUIDE/html/
