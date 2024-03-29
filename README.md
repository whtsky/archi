# Archi

[![Build Status](https://whtsky.visualstudio.com/archi/_apis/build/status/whtsky.archi?branchName=master)](https://whtsky.visualstudio.com/archi/_build/latest?definitionId=2&branchName=master)

Multi-format archive library based on [libarchive](https://github.com/libarchive/libarchive) . Forked from [pyarchive](https://github.com/tailhook/pyarchive)

## Usage

```python
import archi

with open("test.tgz", "rb") as f:
    archive = archi.Archive(f)
for file in archive:
    print(file.filename)
    print(file.read())
```

Keep in mind that you **can't** store `Entry`s, they're freed as soon as the loop moves on to the next or ends. So this won't do:

```python
archi = archi.Archive('file.zip')
files = [f for f in archi]
files[0].filename # Address boundary error !
```

## Changelog

### vnext
- (wheels) Upgrade bundled libarchive to [v3.6.1](https://github.com/libarchive/libarchive/releases/tag/v3.6.1)
- Fix SIGSEGV when received ARCHIVE_FATAL error

### v0.2.3

- (wheels) Upgrade bundled libarchive to [v3.4.3](https://github.com/libarchive/libarchive/releases/tag/v3.4.3)

### v0.2.2

- (wheels) Upgrade bundled libarchive to [v3.4.2](https://github.com/libarchive/libarchive/releases/tag/v3.4.2)
- (wheels) Build macOS wheels on macOS 10.14 (https://github.com/whtsky/archi/pull/6)

### v0.2.1

- (wheels) Upgrade bundled libarchive to [v3.4.1](https://github.com/libarchive/libarchive/releases/tag/v3.4.1)

### v0.2.0

- Add support for libarchive's `ARCHIVE_FAILED` error
- use PyMem_Malloc & PyMem_Free instead of alloca

### v0.1.1

- Fix binary wheels for macOS

## TODO

- [ ] compression
- [ ] build wheels for Windows: https://discuss.python.org/t/need-auditwheel-like-utility-for-other-platforms/2028 , https://discuss.python.org/t/packaging-dlls-on-windows/1401
