import ctypes
import numpy as np
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
bibliothek_pfad = os.path.join(script_dir, "lib", "gradient","libgradient.so")
print(bibliothek_pfad)
# Load the C library
example_lib = ctypes.CDLL("/Users/domenic/Documents/Praktikum/TopoPyBox/lib/gradient/libgradient.so")

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



### Exaple for further function
bibliothek_pfad2 = os.path.join(script_dir, "lib","funktion","libfunktion.so")
print(bibliothek_pfad2)
example_lib2 = ctypes.CDLL(bibliothek_pfad2)
example_lib2.func.argtypes = None
example_lib2.func.restype = ctypes.c_int
def hello_world():
    example_lib2.func()
hello_world() ## Prof that it works