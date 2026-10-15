import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location(
    "release_version", ROOT / "release_version.py"
)
release_version = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release_version)
resolve_release_version = release_version.resolve_release_version


def test_checked_in_release_version_is_preserved():
    libarchive_version = (ROOT / "LIBARCHIVE_VERSION").read_text().strip()
    recorded_version = (ROOT / "VERSION").read_text().strip()

    assert resolve_release_version(libarchive_version, recorded_version) == "3.8.10.1"


@pytest.mark.parametrize("recorded_version", ["3.8.10.1", "3.8.10.2"])
def test_matching_libarchive_version_preserves_recorded_version(recorded_version):
    assert resolve_release_version("v3.8.10", recorded_version) == recorded_version


def test_changed_libarchive_version_resets_archi_patch():
    assert resolve_release_version("v3.8.11", "3.8.10.1") == "3.8.11.0"


@pytest.mark.parametrize("recorded_version", ["3.8.10", "3.8.10.1.2"])
def test_version_requires_exactly_four_components(recorded_version):
    with pytest.raises(ValueError, match="VERSION"):
        resolve_release_version("v3.8.10", recorded_version)


@pytest.mark.parametrize("libarchive_version", ["v3.8", "v3.8.10.1"])
def test_libarchive_version_requires_exactly_three_components(libarchive_version):
    with pytest.raises(ValueError, match="LIBARCHIVE_VERSION"):
        resolve_release_version(libarchive_version, "3.8.10.1")


@pytest.mark.parametrize(
    ("libarchive_version", "recorded_version", "invalid_name"),
    [
        ("v3.8.1٠", "3.8.10.1", "LIBARCHIVE_VERSION"),
        ("v3.8.10", "3.8.10.1١", "VERSION"),
    ],
)
def test_non_ascii_digits_are_rejected(
    libarchive_version, recorded_version, invalid_name
):
    with pytest.raises(ValueError, match=invalid_name):
        resolve_release_version(libarchive_version, recorded_version)


@pytest.mark.parametrize(
    ("libarchive_version", "recorded_version", "invalid_name"),
    [
        ("3.8.10", "3.8.10.1", "LIBARCHIVE_VERSION"),
        ("v3.8.x", "3.8.10.1", "LIBARCHIVE_VERSION"),
        ("v3.8.10", "1", "VERSION"),
        ("v3.8.10", "3.8.10.x", "VERSION"),
    ],
)
def test_malformed_versions_are_rejected(
    libarchive_version, recorded_version, invalid_name
):
    with pytest.raises(ValueError, match=invalid_name):
        resolve_release_version(libarchive_version, recorded_version)
