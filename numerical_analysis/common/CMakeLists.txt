add_library(na_common STATIC
    src/common.cpp
    src/fpn.cpp
)

target_include_directories(na_common PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")
target_compile_features(na_common PUBLIC cxx_std_20)
