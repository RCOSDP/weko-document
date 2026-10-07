#!/bin/bash

echo "build user manual (English)"
rm -r ./build/user_en
mkdir -p ./build/user_en/pdf
mkdir -p ./build/user_en/html
npx honkit pdf $(pwd)/manuals_en/USER $(pwd)/build/user_en/pdf/user_en.pdf
npx honkit build $(pwd)/manuals_en/USER $(pwd)/build/user_en/html
