# TopoPyBox - proof of concept

```text
___________                    __________         __________              
\__    ___/___ ______   ____   \______   \___.__. \______   \ _______  ___
  |    | /  _ \\____ \ /  _ \   |     ___<   |  |  |    |  _//  _ \  \/  /
  |    |(  <_> )  |_> >  <_> )  |    |    \___  |  |    |   (  <_> >    < 
  |____| \____/|   __/ \____/   |____|    / ____|  |______  /\____/__/\_ \
               |__|                       \/              \/            \/
```

## How to execute

First Compile the C Code

```bash
  cd ./build
  cmake ..
  make
```

Now the Python Scrips can use the C Code

### Manual Compiling

```bash
gcc -fPIC -shared -o compiledName.so uncompiledFile.c
```

### requirements

- make
- cmake
- ctypes

### informations about the project

we use a typical cmake-cpp directory hierarchie with the addition of separate libraries.so

```bash
Projektverzeichnis
|-- CMakeLists.txt
|-- src
|   |-- main.c
|   |-- mylibrary.c
|-- include
|   |-- mylibrary.h
|-- lib
|   |-- libmylibrary.so
|-- build  (nicht im Quellcode-Repository, wird durch CMake erstellt)
|-- bin    (nicht im Quellcode-Repository, wird durch CMake erstellt)
```
