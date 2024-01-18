import ctypes
import numpy as np
import copy
import os

# find .so file that contains c func
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './private/gradient8.so')
lib = ctypes.CDLL(filename)

# define parameters for opening c file:
lib.gradient8.argtypes = [
    ctypes.c_int,   # rows
    ctypes.c_int,   # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # output Matrix
    ctypes.c_int,
    ctypes.c_float
]
lib.gradient8.restype = None

class Gradient8Mixin:
    # später geren mit unit* damit 
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

        # copy object witch new z and return
        copy_self = copy.copy(self)
        copy_self.z = output_matrix

        return copy_self
