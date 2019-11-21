import platform
import sys

from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup
from setuptools.command.test import test as TestCommand
from setuptools.extension import Extension

ENABLE_LINETRACE = "test" in sys.argv and platform.python_implementation() == "CPython"


class PyTest(TestCommand):
    def run_tests(self):
        import pytest

        errno = pytest.main(
            ["--cov", "--cov-report", "xml", "--cov-report", "term-missing"]
        )

        sys.exit(errno)


setup(
    name="archi",
    version="0.1.0",
    description="Multi-format archive library based on libarchive",
    author="Wu Haotian",
    author_email="whtsky@gmail.com",
    url="https://github.com/whtsky/archi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    cmdclass={"test": PyTest},
    ext_modules=cythonize(
        Extension(
            "archi",
            ["archi.pyx"],
            libraries=["archive"],
            define_macros=[("CYTHON_TRACE", ENABLE_LINETRACE and "1" or "0")],
        ),
        gdb_debug=True,
        compiler_directives={
            "linetrace": ENABLE_LINETRACE,
            "binding": ENABLE_LINETRACE,
        },
    ),
)
