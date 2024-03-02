import numpy as np
from matplotlib.colors import LightSource
import copy

class HillshadeMixin:
    def hillshade(self,**kwargs):
        azimuth = 315
        altitude = 60
        exaggerate = 1

        # can be removed?
        useblockproc = False    # vermutlich unnötig
        useparallel = False     # vermutlich unnötig
        blocksize = 5000        # vermutlich unnötig
        method = 'surfnorm'     # da von matplotlib fragwürdig?

        if 'azimuth' in kwargs:
            azimuth = kwargs['azimuth']
        if 'altitude' in kwargs:
            altitude = kwargs['altitude']
        if 'exaggerate' in kwargs:
            exaggerate = kwargs['exaggerate']

        # can be removed?
        if 'useblockproc' in kwargs:
            useblockproc = kwargs['useblockproc']
        if 'useparallel' in kwargs:
            useparallel = kwargs['useparallel']
        if 'blocksize' in kwargs:
            blocksize = kwargs['blocksize']
        if 'method' in kwargs:
            method = kwargs['method']

        ls = LightSource(azdeg=azimuth, altdeg=altitude)
        hillshade = ls.hillshade(self.z, vert_exag=exaggerate)

        H = copy.copy(self)
        H.z = hillshade.copy()

        return H
    