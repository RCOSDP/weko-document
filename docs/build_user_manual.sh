#!/bin/bash

echo "build user manual"
rm -r ./build/user
mkdir -p ./build/user/pdf
mkdir -p ./build/user/html
npx honkit pdf $(pwd)/manuals/USER/base $(pwd)/build/user/pdf/user.pdf
npx honkit build $(pwd)/manuals/USER/base $(pwd)/build/user/html/
