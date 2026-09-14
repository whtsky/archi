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

REM cibuildwheel sets CIBW_ARCHS for each wheel job. Fall back to the
REM Visual Studio target architecture when running the script directly.
SET TARGET_ARCH=%CIBW_ARCHS%
IF NOT DEFINED TARGET_ARCH SET TARGET_ARCH=%VSCMD_ARG_TGT_ARCH%
IF NOT DEFINED TARGET_ARCH SET TARGET_ARCH=AMD64

SET CMAKE_ARCH=
IF /I "%TARGET_ARCH%"=="AMD64" SET CMAKE_ARCH=x64
IF /I "%TARGET_ARCH%"=="x64" SET CMAKE_ARCH=x64
IF /I "%TARGET_ARCH%"=="ARM64" SET CMAKE_ARCH=ARM64
IF NOT DEFINED CMAKE_ARCH (
    echo Unsupported Windows target architecture: %TARGET_ARCH%
    EXIT /b 1
)

MKDIR build_ci 2>NUL
CD build_ci
cmake -G "Visual Studio 17 2022" -A %CMAKE_ARCH% -DCMAKE_BUILD_TYPE=Release -DENABLE_TEST=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5 ..\libarchive || EXIT /b 1
cmake --build . --config Release || EXIT /b 1
cmake --install . --prefix install || EXIT /b 1
CD ..
