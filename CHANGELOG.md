# Changelog

## v3.8.7

- (wheels) Upgrade bundled libarchive to [v3.8.7](https://github.com/libarchive/libarchive/releases/tag/v3.8.7)

## v3.6.1
- Version now mirrors bundled libarchive version
- (wheels) Bundled libarchive [v3.6.1](https://github.com/libarchive/libarchive/releases/tag/v3.6.1)
- (wheels) Add Windows wheel builds
- (wheels) Add Linux aarch64 wheel builds
- Fix SIGSEGV when received ARCHIVE_FATAL error
- Migrate CI from Azure Pipelines to GitHub Actions

## v0.2.3

- (wheels) Upgrade bundled libarchive to [v3.4.3](https://github.com/libarchive/libarchive/releases/tag/v3.4.3)

## v0.2.2

- (wheels) Upgrade bundled libarchive to [v3.4.2](https://github.com/libarchive/libarchive/releases/tag/v3.4.2)
- (wheels) Build macOS wheels on macOS 10.14 (https://github.com/whtsky/archi/pull/6)

## v0.2.1

- (wheels) Upgrade bundled libarchive to [v3.4.1](https://github.com/libarchive/libarchive/releases/tag/v3.4.1)

## v0.2.0

- Add support for libarchive's `ARCHIVE_FAILED` error
- use PyMem_Malloc & PyMem_Free instead of alloca

## v0.1.1

- Fix binary wheels for macOS
