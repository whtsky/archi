#!/usr/bin/env bash
set -e

VERSION=$(cat "$(dirname "$0")/../LIBARCHIVE_VERSION" | tr -d '[:space:]')

if [ ! -d libarchive ]; then
    git clone https://github.com/libarchive/libarchive.git
fi

cd libarchive
git fetch --tags
git checkout "$VERSION"
