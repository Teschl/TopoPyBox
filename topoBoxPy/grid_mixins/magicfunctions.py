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

    # equal
    def eq(self, other):
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] == other.z[i]:
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("eq is only supported between instances of DEM.")

    # greater than
    def gt(self, other):
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] > other.z[i]:
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("gt is only supported between instances of DEM.")

    # greater than or equal
    def ge(self, other):
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] >= other.z[i]:
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("ge is only supported between instances of DEM.")

    # less than or equal
    def le(self, other):
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] <= other.z[i]:
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("le is only supported between instances of DEM.")

    # less than
    def lt(self, other):
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] < other.z[i]:
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("lt is only supported between instances of DEM.")

    # apply log() on all values in DEM
    def log(self):
        # check if z is not int/bool missing
        result = copy.copy(self)
        result.z = np.log(self.z)

    # apply log2() on all values in DEM
    def log2(self):
        # check if z is not int/bool missing
        result = copy.copy(self)
        result.z = np.log2(self.z)

    # apply log10() on all values in DEM
    def log10(self):
        # check if z is not int/bool missing
        result = copy.copy(self)
        result.z = np.log10(self.z)

    def minus(self, other):
        pass

    def power(self, other):
        pass

    def plus(self, other):
        pass

    # not equal
    def ne(self, other):
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] != other.z[i]:
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("ne is only supported between instances of DEM.")

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
        if(isinstance(other, self.__class__)):
            z = np.zeros_like(self.z)
            for i in range(len(self.z)):
                if self.z[i] != other.z[i] and (other.z[i] == 0 or self.z[i] == 0):
                    z[i] == 1
            result = copy.copy(self)
            result.z = z
            return result
        else:
            raise ValueError("xor is only supported between instances of DEM.")

    def uplus(self, other):
        pass

    def uminus(self, other):
        pass

    def times(self, other):
        pass
