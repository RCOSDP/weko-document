#!/bin/bash

echo "build spec document"
rm -r ./build/spec
mkdir -p ./build/spec/pdf
mkdir -p ./build/spec/html
# npx honkit pdf spec/base build/spec/pdf/spec.pdf
npx honkit build $(pwd)/spec/base $(pwd)/build/spec/html