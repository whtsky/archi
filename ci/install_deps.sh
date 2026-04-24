#!/usr/bin/env bash
set -e

if command -v apk &>/dev/null; then
    apk add --no-cache cmake make gcc g++ musl-dev linux-headers \
        zlib-dev xz-dev lz4-dev zstd-dev acl-dev libzip-dev lzop
elif command -v dnf &>/dev/null; then
    dnf install -y cmake lzop libzip-devel libzstd-devel libacl-devel \
        xz-devel lz4-devel zlib-devel
elif command -v yum &>/dev/null; then
    yum install -y cmake lzop libzip-devel libzstd-devel libacl-devel \
        xz-devel lz4-devel zlib-devel
else
    echo "No supported package manager found" >&2
    exit 1
fi
