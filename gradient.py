import ctypes


# C Dynamic Link Library
gradient = ctypes.CDLL("/home/theo/Documents/Praktikum/gradient/lib/build/libgradient.so") #path to .so file

gradient.display()

