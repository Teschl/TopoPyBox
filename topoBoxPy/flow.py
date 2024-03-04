import numpy as np

from .grid import GridObject

from .flow_mixins.test import TestMixin


# as of right now, only works with DEM not just a matrix M
class FlowObject(TestMixin):
    def __init__(self, DEM, **kwargs):
        # evaluate kwargs
        preprocess = kwargs.get("preprocess", 'carve')
        internaldrainage = kwargs.get("internaldrainage", False)
        cweight = kwargs.get("cweight", 1)
        verbose = kwargs.get("verbose", False)

        # get properties from DEM
        if isinstance(DEM, GridObject):
            self.size = DEM.rows * DEM.columns
            self.type = 'single'
            self.data_type = DEM.data_type
            self.cellsize = DEM.cellsize
            self.georef = DEM.georef

            # generate ix and blank ixc
            self.ix = np.argsort(-DEM.z.flatten())
            self.ixc = np.zeros_like(self.ix)
            
            # hier muss ixc noch berechent werden, Algorithmus fehlt noch

        else :
            raise ValueError("Argument DEM has to be instance of GridObject.")
        
        
