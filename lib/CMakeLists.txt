# $ cd build
# $ cmake ..
# $ make


# CMakeLists.txt
cmake_minimum_required(VERSION 3.5)

project(TopoPyBox)
set(CMAKE_C_STANDARD 11)

# Create a shared library from mylibrary.c
add_library(gradient SHARED gradient.c)
set_target_properties(gradient PROPERTIES SUFFIX ".so")

# Set the library output name, for example, libmylibrary.so
#set_target_properties(gradient PROPERTIES OUTPUT_NAME "gradient")





