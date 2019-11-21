@ECHO OFF
SET ZLIB_VERSION=1.2.11
IF NOT EXIST build_ci\libs (
    MKDIR build_ci\libs
)
CD build_ci\libs
IF NOT EXIST zlib-%ZLIB_VERSION%.tar.gz (
curl -o zlib-%ZLIB_VERSION%.tar.gz https://www.zlib.net/zlib-%ZLIB_VERSION%.tar.gz
)
IF NOT EXIST zlib-%ZLIB_VERSION% (
tar -x -z -f zlib-%ZLIB_VERSION%.tar.gz
)
CD zlib-%ZLIB_VERSION%
cmake -G "Visual Studio 15 2017" . || EXIT /b 1
cmake --build . --target ALL_BUILD --config Release || EXIT /b 1
cmake --build . --target RUN_TESTS --config Release || EXIT /b 1
cmake --build . --target INSTALL --config Release || EXIT /b 1
CD ..\..\..


MKDIR build_ci\cmake
CD build_ci\cmake
cmake -G "Visual Studio 15 2017" -D CMAKE_BUILD_TYPE="Release" ..\..\libarchive || EXIT /b 1
cmake --build . --target ALL_BUILD --config Release
