import re

_COMPONENT = r"(?:0|[1-9][0-9]*)"
_LIBARCHIVE_VERSION = re.compile(rf"v({_COMPONENT}(?:\.{_COMPONENT}){{2}})")
_ARCHI_VERSION = re.compile(rf"{_COMPONENT}(?:\.{_COMPONENT}){{3}}")


def resolve_release_version(libarchive_version, recorded_version):
    match = _LIBARCHIVE_VERSION.fullmatch(libarchive_version)
    if match is None:
        raise ValueError(
            f"invalid LIBARCHIVE_VERSION: {libarchive_version!r}; "
            "expected vMAJOR.MINOR.PATCH with ASCII numeric components"
        )
    if _ARCHI_VERSION.fullmatch(recorded_version) is None:
        raise ValueError(
            f"invalid VERSION: {recorded_version!r}; "
            "expected MAJOR.MINOR.PATCH.ARCHI_PATCH with ASCII numeric components"
        )

    upstream_version = match.group(1)
    recorded_upstream, _, _ = recorded_version.rpartition(".")
    if recorded_upstream == upstream_version:
        return recorded_version
    return f"{upstream_version}.0"
