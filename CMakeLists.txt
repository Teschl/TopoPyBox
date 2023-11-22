# $ cd build
# $ cmake ..
# $ make


# CMakeLists.txt
cmake_minimum_required(VERSION 3.5)

project(TopoPyBox)
set(CMAKE_C_STANDARD 11)

find_package(Matlab)

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


#### Matlab ####
# Füge die Header-Datei und die C-Quelldatei hinzu
set(SOURCE_FILES
    src/aspect.c
    libMatlab/Mex_aspect.c
)

# Erstelle die MEX-Funktion
add_library(Mex_aspect MODULE ${SOURCE_FILES})

# Verlinke erforderliche Bibliotheken (falls notwendig)
#target_link_libraries(Mex_aspect PRIVATE some_library)

# Füge den Include-Pfad für die Header-Datei hinzu
target_include_directories(Mex_aspect PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Set the library output name, for example, libmylibrary.so
#set_target_properties(gradient PROPERTIES OUTPUT_NAME "gradient")





