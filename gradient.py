import ctypes
import numpy as np

# Load the C library
example_lib = ctypes.CDLL('/home/theo/Documents/Praktikum/gradient/lib/build/libgradient.so')

# Define the argument and return types for the C function
example_lib.gradient8.argtypes = [
    ctypes.c_int,    # rows
    ctypes.c_int,    # cols
    np.ctypeslib.ndpointer(dtype=np.int32),  # input_matrix
    np.ctypeslib.ndpointer(dtype=np.int32)   # output_matrix
]
example_lib.gradient8.restype = None

def calculate_matrix_python(input_matrix):
    rows, cols = input_matrix.shape
    output_matrix = np.zeros_like(input_matrix)

    # Call the C function
    example_lib.gradient8(rows, cols, input_matrix, output_matrix)

    return output_matrix
