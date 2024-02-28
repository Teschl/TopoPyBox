import numpy as np

from .grid import GridObject

from .flow_mixins.test import TestMixin


# as of right now, only works with DEM not just a matrix M

class FlowObject(TestMixin):
    def __init__(self, DEM, **kwargs):
        # evaluate kwargs
        preprocess = 'carve'
        internaldrainage = False
        cweight = 1
        verbose = False

        if 'preprocess' in kwargs:
            preprocess = kwargs['preprocess']
        if 'sinks' in kwargs:
            sinks = kwargs['sinks']
        if 'internaldrainage' in kwargs:
            internaldrainage = bool(kwargs['internaldrainage'])
        if 'cweight' in kwargs:
            cweight = int(kwargs['cweight'])
        if 'verbose' in kwargs:
            verbose = bool(kwargs['verbose'])

        # get properties from DEM
        if isinstance(DEM, GridObject):
            self.size = DEM.rows * DEM.columns
            self.type = 'single'
            self.data_type = DEM.data_type
            self.cellsize = DEM.cellsize
            self.georef = DEM.georef

            # generate ix and blank ixc
            sorted_indices = np.argsort(DEM.z, axis=None)
            self.ix = np.unravel_index(sorted_indices, DEM.z.shape)
            self.ixc = np.zeros_like(self.ix)
        else :
            raise ValueError("Argument DEM has to be instance of GridObject.")
        
        
