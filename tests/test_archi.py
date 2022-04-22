from hashlib import md5
from pathlib import Path

import archi
import pytest

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
    del ar
    assert data == expected_md5

def test_raise_error():
    with pytest.raises(archi.Error) as e:
        archi.Archive("some_file_that_does_not_exist")
    assert "Failed to open" in str(e)
