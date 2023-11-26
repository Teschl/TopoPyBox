import ctypes
import numpy as np
import os

# relativen Path finden
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
bibliothek_pfad = os.path.join(script_dir, "lib", "aspect","libaspect.so")

# Load the C library
# lib = ctypes.CDLL(bibliothek_pfad)
lib = ctypes.CDLL("/home/theo/Documents/Praktikum/TopoPyBox/lib/aspect/libaspect.so")

# Define the argument and return types for the C function
lib.aspect.argtypes = [
    ctypes.c_int,    # rows
    ctypes.c_int,    # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS')      # output Matrix
]
lib.aspect.restype = None

# --------------------------------------------------------------------------------
def aspect(input_matrix):
    rows, cols = input_matrix.shape
    input_matrix = input_matrix.astype(np.float32)
    # generate output_matrix like the input, just filled with zeros
    output_matrix = np.zeros_like(input_matrix)

    # Call the C function
    lib.aspect(rows, cols, input_matrix, output_matrix)

    return output_matrix
