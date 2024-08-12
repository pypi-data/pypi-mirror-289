cmake_minimum_required(VERSION 3.2)

project(socom LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Choosing compiler (clang has preference).
if (CMAKE_CXX_COMPILER MATCHES ".*clang.*" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
	set (CMAKE_COMPILER_IS_CLANGXX 1)
endif()

add_subdirectory(ext/pybind11)

file (GLOB_RECURSE SOURCES 
    src/*.cxx
    src/*.cpp
    ext/uunet/ext/eclat/*.c
    ext/uunet/ext/infomap/*.cpp
    ext/uunet/src/*.cpp)

pybind11_add_module(_multinet MODULE ${SOURCES})
target_include_directories (_multinet PRIVATE
    ext/uunet/ext/eclat/eclat/src
    ext/uunet/ext/eclat/tract/src
    ext/uunet/ext/eclat/math/src
    ext/uunet/ext/eclat/util/src
    ext/uunet/ext/eclat/apriori/src
    ext/uunet/ext/infomap
    ext/uunet/ext/boost
    ext/uunet/src)

add_definitions(-DNS_INFOMAP -DONLY_C_LOCALE=1)