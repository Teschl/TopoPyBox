# $ cd lib/build
# $ cmake ..
# $ make


# CMakeLists.txt
cmake_minimum_required(VERSION 3.5)

project(TopoPyBox)
set(CMAKE_C_STANDARD 11)

# Create a shared library from mylibrary.c
add_library(gradient SHARED gradient.c)
# .so suffix erzwingen, könnte für problemen mit Win/Mac sorgen
set_target_properties(gradient PROPERTIES SUFFIX ".so")