# TopoToolBox

## in Python, R, MATLAB using C

## How compile for Python

First Compile the C Code in Terminal

```bash
  cd ./topoBoxC
  cmake .
  make
```

Now move the .so files to the "private" folders in topoBoxPy

## How to compile for Matlab

Veraltet!

```bash
  cd ./Bulid
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
TopoToolBox
├── topoBoxC
│   ├── compiled
│   │   └── {contains cthe compiled .so files}
│   ├── GRIDobj
│   │   └── functions.c
│   ├── CMakeLists.txt
│   └── Makefile
├── topoBoxMatlab
│   └── {work in progress}
└── topoBoxPy
    ├── flow_mixins
    │   └── {work in progress}
    ├── flow.py
    ├── grid_mixins
    │   ├── functions.py
    │   └── private
    │       └── compiled_c_files.so
    ├── grid.py
    ├── stream_mixins
    │   └── {work in progress}
    └── stream.py
```
