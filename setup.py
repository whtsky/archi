import platform
import sys
from os import path

from setuptools import setup
from setuptools.command.test import test as TestCommand
from setuptools.extension import Extension

ENABLE_LINETRACE = "test" in sys.argv and platform.python_implementation() == "CPython"


try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext

    ext_modules = cythonize(
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
    )
except ImportError:
    ext_modules = [Extension("archi", ["archi.c"], libraries=["archive"],)]


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


class PyTest(TestCommand):
    def run_tests(self):
        import pytest

        errno = pytest.main(
            ["--cov", "--cov-report", "xml", "--cov-report", "term-missing"]
        )

        sys.exit(errno)


setup(
    name="archi",
    version="0.2.0",
    description="Multi-format archive library based on libarchive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    zip_safe=False,
    include_package_data=True,
    keywords=["libarchive", "archive", "compress", "compression"],
    author="Wu Haotian",
    author_email="whtsky@gmail.com",
    url="https://github.com/whtsky/archi",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    cmdclass={"test": PyTest},
    ext_modules=ext_modules,
)
