#!/bin/bash

echo "build 未病USER manual"
rm -r ./build/未病USER
mkdir -p ./build/未病USER/pdf
mkdir -p ./build/未病USER/html
npx honkit pdf $(pwd)/manuals/未病USER/base $(pwd)/build/未病USER/pdf/未病USER.pdf
npx honkit build $(pwd)/manuals/未病USER/base $(pwd)/build/未病USER/html