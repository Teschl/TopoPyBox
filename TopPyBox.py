import ctypes
import numpy as np
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
bibliothek_pfad = os.path.join(script_dir, "lib", "gradient","libgradient.so")
print(bibliothek_pfad)
# Load the C library
example_lib = ctypes.CDLL(bibliothek_pfad)

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



# Load the C library
lib = ctypes.CDLL("../src/build/libaspect.so")

# Define the argument and return types for the C function
lib.aspect.argtypes = [
    ctypes.c_int,    # rows
    ctypes.c_int,    # cols
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS'),     # input Matrix
    np.ctypeslib.ndpointer(dtype=np.float32, flags='C_CONTIGUOUS')      # output Matrix
]
lib.aspect.restype = None

def aspect(input_matrix):
    rows, cols = input_matrix.shape
    output_matrix = np.zeros_like(input_matrix)

    # Call the C function
    lib.aspect(rows, cols, input_matrix, output_matrix)

    return output_matrix
