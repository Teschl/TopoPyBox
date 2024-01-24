# TopoToolBox

## in Python, R and MATLAB using C

## How to install

### Installing the Python package

Install the package from local files using pip.

```bash
cd path/to/project/topoBoxPy
pip install -e .
```

or keep the package in the same folder as your script

```bash
some_folder
├── topoBoxPy
├── your_script.ipynb
└── your_script.py
```

## How compile C code for Python

```bash
  cd ./topoBoxC
  cmake .
  make
```

or maunally for single files

```bash
gcc -fPIC -shared -o compiled_name.so uncompiled_file.c
```

## How to compile for Matlab

**Veraltet!**

```bash
  cd ./Bulid
  cmake ..
  make
```

in Matlab run

```bash
  compileMexFiles.m
```

### general information about the project

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
