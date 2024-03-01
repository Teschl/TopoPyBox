import numpy as np
import copy

# These are not really python magic functions, but they
# are short and dont each require an file on their own.
# Also they dont call C functions.

class MagicFunctionsMixin:
    def andGrid(self, other):
        pass

    def orGrid(self, other):
        pass

    def notGrid(self, other):
        pass

    def all(self, other):
        pass

    def any(self, other):
        pass

    def eq(self, other):
        pass
    # greater than
    def gt(self, other):
        pass

    # greater than or equal
    def ge(self, other):
        if len(self.z) != len(other.z):
            raise ValueError("Both DEM must have the same size")

        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self)):
                if self.z[i] >= other.z[i]:
                    z[i] == 1
    
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("ge is only supported between instances of DEM.")


    def le(self, other):
        pass

    def lt(self, other):
        pass

    def log(self, other):
        pass

    def log2(self, other):
        pass

    def log10(self, other):
        pass

    def minus(self, other):
        pass

    def power(self, other):
        pass

    def plus(self, other):
        pass

    def ne(self, other):
        pass

    def ntimes(self, other):
        pass

    def mrdivide(self, other):
        pass

    def sqrt(self, other):
        pass

    def mpower(self, other):
        pass

    def zscore(self, other):
        pass

    def xor(self, other):
        pass

    def uplus(self, other):
        pass

    def uminus(self, other):
        pass

    def times(self, other):
        pass
