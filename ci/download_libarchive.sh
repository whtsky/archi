#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VERSION=$(cat "$SCRIPT_DIR/../LIBARCHIVE_VERSION" | tr -d '[:space:]')

if [ ! -d libarchive ]; then
    echo "Downloading libarchive $VERSION..."
    curl -sL "https://github.com/libarchive/libarchive/archive/refs/tags/${VERSION}.tar.gz" | tar xz
    mv "libarchive-${VERSION#v}" libarchive
fi
