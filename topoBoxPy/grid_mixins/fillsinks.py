import ctypes
import numpy as np
import copy
import os

# find .so file that contains c func
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './private/libfillsinks.so')
lib = ctypes.CDLL(filename)

# define parameters for opening c file:
lib.fillsinks.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),
]
lib.fillsinks.restype = None

class FillsinksMixin:
    def fillsinks(self, *args, **kwargs):
        # handle arguments
        if 'maxdepth' in kwargs:
            maxdepth = kwargs['maxdepth']
        if 'sinks' in kwargs:
            sinks = kwargs['sinks']
        if 'option' in kwargs:
            option = kwargs['option']

        # prepare arguments for c function
        input_matrix = self.z
        input_matrix = input_matrix.astype(np.float32)
        rows, cols = input_matrix.shape
        output_matrix = np.zeros_like(input_matrix)

        # call C function
        lib.fillsinks(rows, cols, input_matrix, output_matrix)

        copy_self = copy.copy(self)
        copy_self.z = input_matrix.copy()
        
        return copy_self
