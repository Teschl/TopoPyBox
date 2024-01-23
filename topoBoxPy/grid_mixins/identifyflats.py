import ctypes
import numpy as np
import copy
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './private/libidentifyflats.so')
lib = ctypes.CDLL(filename)

lib.identifyflats.argtypes = [
    ctypes.c_int,   # rows
    ctypes.c_int,   # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix 
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # output Matrix 1
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # output Matrix 2
]
lib.identifyflats.restype = None

class Identifyflats:
    def identifyflats(self):

        input_matrix = self.z.astype(np.float32)
        flats_matrix = np.zeros_like(input_matrix)
        stills_matrix = np.zeros_like(input_matrix)
        rows, cols = input_matrix.shape

        lib.identifyflats(rows, cols, input_matrix, flats_matrix, stills_matrix)

        flats = copy.copy(self)
        flats.z = flats_matrix

        stills = copy.copy(self)
        stills.z = stills_matrix 

        return flats, stills
    