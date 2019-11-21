#!/usr/bin/env bash

# todo: git submodule does not support tags
if [ ! -d libarchive ]; then
    git clone https://github.com/libarchive/libarchive.git
    pushd libarchive
    git checkout v3.4.0
    popd
fi