import numpy as np
from matplotlib.colors import LightSource
import copy

class HillshadeMixin:
    def hillshade(self,**kwargs):
        azimuth = kwargs.get("azimuth", 315)
        altitude = kwargs.get("altitude", 60)
        exaggerate = kwargs.get("exaggerate", 1)
        useblockproc = kwargs.get("useblockproc", False)    # vermutlich unnötig
        useparallel = kwargs.get("useparallel", False)     # vermutlich unnötig
        blocksize = kwargs.get("blocksize", 5000)        # vermutlich unnötig
        method = kwargs.get("method", 'surfnorm')     # da von matplotlib fragwürdig?

        ls = LightSource(azdeg=azimuth, altdeg=altitude)
        hillshade = ls.hillshade(self.z, vert_exag=exaggerate/self.cellsize)

        H = copy.copy(self)
        H.z = hillshade.copy()

        return H
    