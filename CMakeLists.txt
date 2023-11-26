# $ cd build
# $ cmake ..
# $ make


# CMakeLists.txt
cmake_minimum_required(VERSION 3.5)

project(TopoPyBox)
set(CMAKE_C_STANDARD 11)


# Füge alle C-Programm-Quelldateien im Verzeichnis 'src' hinzu
file(GLOB PROGRAM_SOURCES "src/*.c")

foreach(program_source ${PROGRAM_SOURCES})
    # bekomme den dateinamen ohne endung
    get_filename_component(program_name ${program_source} NAME_WE)
    add_library(${program_name} SHARED ${program_source})
    # setzte das zielverzeichnis
    set_target_properties(${program_name} PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/../lib/${program_name}  # Hier werden die dylibs erstellt
    )
    # force die dylib einen .so suffix zu haben
    set_target_properties(${program_name} PROPERTIES SUFFIX ".so")
    # Füge den Include-Pfad für Header-Dateien hinzu (falls benötigt)
    target_include_directories(${program_name} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)


endforeach()
