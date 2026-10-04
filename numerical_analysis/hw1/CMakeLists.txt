add_executable(hw1 main.cpp)

target_link_libraries(hw1 PRIVATE na_common)

# The program writes the LaTeX fragments it generates into <source>/out, so that
# report.tex can \input them no matter which directory the binary runs from.
target_compile_definitions(hw1 PRIVATE "NA_SOURCE_DIR=\"${CMAKE_CURRENT_SOURCE_DIR}\"")
