class InfoMixin:
    def info(self):
        print("name: " , self.name)
        print("data type: " , self.data_type)
        print("number of rows: ", self.rows)
        print("number of columns",self.columns)
        print("cellsize: ",self.cellsize)
        print("extend in x-direction: ")
        print("extend in y-direction: ")
        print("maximum z-value: ")
        print("minimum z-value: ")
        print("z-unit: ")
        print("georef: ", self.georef)
        