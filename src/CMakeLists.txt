cmake_minimum_required(VERSION 3.5)

project(TopoPyBox)
set(CMAKE_C_STANDARD 11)

# beispiel.c
#add_library(filename SHARED filename.c)
#set_target_properties(filename PROPERTIES SUFFIX ".so")

# aspect.c
add_library(aspect SHARED aspect.c)
set_target_properties(aspect PROPERTIES SUFFIX ".so")
