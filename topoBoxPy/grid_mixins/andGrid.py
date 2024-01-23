import ctypes
import numpy as np
import copy
import os

# find .so file that contains c func
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './private/libandGrid.so')
lib = ctypes.CDLL(filename)

# set variables
lib.andGrid.argtypes = [
    ctypes.c_int,   # rows
    ctypes.c_int,   # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix 1
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix 2
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # output Matrix
]
lib.andGrid.restype = None

class AndGridMixin:
    def andGrid(self, grid):

        input_matrix1 = self.z.astype(np.float32)
        input_matrix2 = grid.z.astype(np.float32)
        output_matrix = np.zeros_like(input_matrix1)
        rows, cols = input_matrix1.shape

        # call c function
        lib.andGrid(rows, cols, input_matrix1, input_matrix2, output_matrix)

        # copy object witch new z and return
        copy_self = copy.copy(self)
        copy_self.z = output_matrix  

        return copy_self
