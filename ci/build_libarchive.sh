#!/usr/bin/env bash
set -e

cd libarchive
cmake . -DCMAKE_BUILD_TYPE=Release -DENABLE_TEST=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5
make -j$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 2)
make install
