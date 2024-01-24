import ctypes
import numpy as np
import copy
import os
import time

# find .so file that contains c func
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './private/libgradient8.so')
lib = ctypes.CDLL(filename)

# define parameters for opening c file:
lib.gradient8.argtypes = [
    ctypes.c_int,   # rows
    ctypes.c_int,   # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # output Matrix
    ctypes.c_int,   # unit
    ctypes.c_float  # distance
]
lib.gradient8.restype = None

class Gradient8Mixin:
    # später dann mit *unit damit liste von eingaben! 
    def gradient8(self, unit="tan"):
        # get z of object got get inputmatrix in float32
        input_matrix = self.z
        input_matrix = input_matrix.astype(np.float32)

        # get size of matrix
        rows, cols = input_matrix.shape

        # make outputmatrix (filled with zeros)
        output_matrix = np.zeros_like(input_matrix)

        # generate unit for calculation
        units = {"tan": 0,
                 "rad": 1,
                 "deg": 2,
                 "sin": 3,
                 "per": 4 }
        unit = units[unit]

        # get distance between cells
        distance = self.cellsize

        # call c function
        lib.gradient8(rows, cols, input_matrix, output_matrix, unit, distance)

        # copy object which new z and return
        copy_self = copy.copy(self)
        copy_self.z = output_matrix.copy()
        print(len(np.unique(output_matrix)))
        return copy_self
