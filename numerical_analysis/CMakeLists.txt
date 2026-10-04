cmake_minimum_required(VERSION 3.20)

project(zju_numerical_analysis LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# clangd reads build/compile_commands.json, so keep this on.
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
endif()

add_subdirectory(common)

# Every homework directory (hw1, hw2, ...) is picked up automatically: a new
# assignment only needs a folder with a CMakeLists.txt next to its sources.
# CONFIGURE_DEPENDS re-globs on build, so no re-configure after adding one.
file(GLOB homework_dirs CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/hw*")

foreach(homework IN LISTS homework_dirs)
  if(IS_DIRECTORY "${homework}" AND EXISTS "${homework}/CMakeLists.txt")
    add_subdirectory("${homework}")
  endif()
endforeach()
