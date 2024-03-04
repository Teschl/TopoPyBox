import numpy as np

class InfoMixin:
    def info(self):
        print("name: " , self.name)
        print("data type: " , self.data_type)
        print("number of rows: ", self.rows)
        print("number of columns",self.columns)
        print("cellsize: ",self.cellsize)
        print("extend in x-direction: ", self.columns * self.cellsize)
        print("extend in y-direction: ", self.rows * self.cellsize)
        print("maximum z-value: ", np.amax(self.z))
        print("minimum z-value: ", np.amin(self.z))
        print("z-unit: ", self.unit)
        print("georef: ", self.georef)
        