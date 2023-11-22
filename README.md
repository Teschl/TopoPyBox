# TopoPyBox - proof of concept

```text
___________                    __________         __________              
\__    ___/___ ______   ____   \______   \___.__. \______   \ _______  ___
  |    | /  _ \\____ \ /  _ \   |     ___<   |  |  |    |  _//  _ \  \/  /
  |    |(  <_> )  |_> >  <_> )  |    |    \___  |  |    |   (  <_> >    < 
  |____| \____/|   __/ \____/   |____|    / ____|  |______  /\____/__/\_ \
               |__|                       \/              \/            \/
```

## How to compile

### Compile the src/dateiname.c

Compiling all Files at once

```bash
  ~$ cd build
  ~$ cmake ..
  ~$ make
```

Compmile a single file

```bash
  ~$ gcc -fPIC -shared -o compiledName.so uncompiledFile.c
```

### Compile the toolBox/mex_dateiname.c

In MATLAB mit dem Terminal

```bash
  ~$ mex toolBox/dateiname.c
```

## Example Scripts

Either run the .m File in MATLAB or run the Jupyter Notebook

## requirements

- make
- cmake
- ctypes
- MATLAB
