from hashlib import md5
from pathlib import Path

import pytest

import archi

expected_md5 = {
    "archive/__init__.py": "29a6a1e050bd42fe24cd17b138d4b08d",
    "archive/core.pyx": "1bd9e27890beb0b576a2122e7b57ca8c",
    "setup.py": "de88961c0eca3d7875894eae7d551d18",
}

test_tgz_path = Path(__file__).parent / "fixtures" / "test.tgz"


def test_names():
    ar = archi.Archive(test_tgz_path)
    assert set(a.filename for a in ar) == set(expected_md5.keys())


def test_read():
    ar = archi.Archive(test_tgz_path)
    assert {a.filename: md5(a.read()).hexdigest() for a in ar} == expected_md5


def test_filelike_object():
    with open(str(test_tgz_path), "rb") as f:
        ar = archi.Archive(f)
    assert {a.filename: md5(a.read()).hexdigest() for a in ar} == expected_md5


def test_read_size():
    ar = archi.Archive(test_tgz_path)
    data = {}
    for ent in ar:
        buf = b""
        while True:
            chunk = ent.read(100)
            if not chunk:
                break
            buf += chunk
        data[ent.filename] = md5(buf).hexdigest()
    assert data == expected_md5


def test_handle_ARCHIVE_FAILED():
    # https://github.com/libarchive/libarchive/issues/373
    ar = archi.Archive(Path(__file__).parent / "fixtures" / "libarchive_issue_373.rar")
    with pytest.raises(archi.Error) as e:
        for ent in ar:
            ent.read()
    assert "Parsing filters is unsupported." in str(e)
