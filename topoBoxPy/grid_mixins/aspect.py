import ctypes
import numpy as np
import copy
import os

# find .so file that contains c func
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './private/aspect.so')
lib = ctypes.CDLL(filename)

# Define the argument and return types for the C function
lib.aspect.argtypes = [
    ctypes.c_int,   # rows
    ctypes.c_int,   # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS')      # output Matrix
]
lib.aspect.restype = None

class AspectMixin:
    def aspect(self):
        # assign the saved matrix as the input_matrix
        input_matrix = self.z

        # generate size ints for matrix
        rows, cols = input_matrix.shape

        # generate input matrix from .tif
        input_matrix = input_matrix.astype(np.float32)

        # generate output_matrix like the input, just filled with zeros
        output_matrix = np.zeros_like(input_matrix)

        # Call the C function
        lib.aspect(rows, cols, input_matrix, output_matrix)

        # returning a copy of Grid
        copy_grid = copy.copy(self)
        copy_grid.z = output_matrix

        return copy_grid
