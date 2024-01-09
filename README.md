# TopoPyBox - proof of concept

```text
___________                    __________         __________              
\__    ___/___ ______   ____   \______   \___.__. \______   \ _______  ___
  |    | /  _ \\____ \ /  _ \   |     ___<   |  |  |    |  _//  _ \  \/  /
  |    |(  <_> )  |_> >  <_> )  |    |    \___  |  |    |   (  <_> >    < 
  |____| \____/|   __/ \____/   |____|    / ____|  |______  /\____/__/\_ \
               |__|                       \/              \/            \/
```

## How compile for Python

First Compile the C Code in Terminal

```bash
  cd ./build
  cmake ..
  make
```

Now the Python Scrips can use the function written in C

## How to compile for Matlab 

in Terminal
```bash
  cd ./build
  cmake ..
  make
```

in Matlab run
```bash
  compileMexFiles.m
```

### Manual Compiling

```bash
gcc -fPIC -shared -o compiledName.so uncompiledFile.c
```

### requirements

- make
- cmake
- ctypes

### informations about the project

We use a typical cmake-cpp directory hierarchie with the addition of lib (equivalent of bin directory), libMatlab(for matlab conversion and inclusion in Matlab scripts) and libPython(for inclusion in a python scripts). Out of convenience we made a separate repository for the core source files, hence other Toolboxes with different programmming languages use the same source files and we prefere a united source code for all languages.

```bash
Projektverzeichnis
|-- CMakeLists.txt
|-- Core
|   |-- GridObj
|        |-- aspect.c 
|   |-- FlowObj
|        |-- bla.c
|-- include
|   |-- aspect.h
|-- lib 
|   |-- libmylibrary.so
|-- libMatlab
|   |-- mexAspect.c
|   |-- mexAspect.mexmaca64
|-- libPython
|   |-- aspect.py 
|-- build
```
