@ECHO OFF
SETLOCAL EnableDelayedExpansion

REM Read version from LIBARCHIVE_VERSION
SET /p LIBARCHIVE_VERSION=<"%~dp0..\LIBARCHIVE_VERSION"
SET LIBARCHIVE_VERSION=%LIBARCHIVE_VERSION: =%

REM Strip leading 'v' for directory name
SET VERSION_NUM=%LIBARCHIVE_VERSION:v=%

IF NOT EXIST libarchive (
    echo Downloading libarchive %LIBARCHIVE_VERSION%...
    curl -sL "https://github.com/libarchive/libarchive/archive/refs/tags/%LIBARCHIVE_VERSION%.tar.gz" -o libarchive.tar.gz || EXIT /b 1
    tar xzf libarchive.tar.gz || EXIT /b 1
    ren "libarchive-%VERSION_NUM%" libarchive || EXIT /b 1
    del libarchive.tar.gz
)

MKDIR build_ci 2>NUL
CD build_ci
cmake -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release -DENABLE_TEST=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5 ..\libarchive || EXIT /b 1
cmake --build . --config Release || EXIT /b 1
cmake --install . --prefix install || EXIT /b 1
CD ..
