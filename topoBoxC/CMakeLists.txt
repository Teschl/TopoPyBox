# CMakeLists.txt

cmake_minimum_required(VERSION 3.5)

# Project name
project(TopoBox)

# Set the output directory for compiled shared libraries (.so files)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/compiled)

# Collect all source files in the grid directory
file(GLOB GRID_SOURCES "GRIDobj/*.c")

# Generate shared libraries from the source files
foreach(SOURCE_FILE ${GRID_SOURCES})
    # Get the file name without the extension
    get_filename_component(FILE_NAME ${SOURCE_FILE} NAME_WE)
    
    # Generate the shared library (.so file)
    add_library(${FILE_NAME} MODULE ${SOURCE_FILE})
    
    # Set the output directory for each shared library
    set_target_properties(${FILE_NAME} PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/compiled/GRIDobj
    )
endforeach()
