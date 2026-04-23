@ECHO OFF
SETLOCAL

REM Read version from LIBARCHIVE_VERSION
SET /p LIBARCHIVE_VERSION=<"%~dp0..\LIBARCHIVE_VERSION"
SET LIBARCHIVE_VERSION=%LIBARCHIVE_VERSION: =%

IF NOT EXIST libarchive (
    git clone https://github.com/libarchive/libarchive.git
)
CD libarchive
git fetch --tags
git checkout %LIBARCHIVE_VERSION%
CD ..

MKDIR build_ci 2>NUL
CD build_ci
cmake -G "Visual Studio 17 2022" -A x64 -D CMAKE_BUILD_TYPE=Release -D ENABLE_TEST=OFF ..\libarchive || EXIT /b 1
cmake --build . --config Release || EXIT /b 1
cmake --install . --prefix install || EXIT /b 1
CD ..
