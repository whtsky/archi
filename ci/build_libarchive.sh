#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PREFIX="${LIBARCHIVE_PREFIX:-/usr/local}"

cd libarchive
cmake . -DCMAKE_BUILD_TYPE=Release -DENABLE_TEST=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_INSTALL_PREFIX="$PREFIX"
make -j$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 2)
make install
