import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import colormaps

class ImageschsMixin:
    def imageschs(self, **kwargs):

        if 'caxis' in kwargs:
            caxis = kwargs['caxis']

        if 'colorbar' in kwargs:
            if isinstance(kwargs['colorbar'], bool):
                add_colorbar = kwargs['colorbar']
            else:
                raise ValueError("colorbar kwargs expects boolean.")
        else:
            add_colorbar = True

        # to be added
        if 'colorbarlabel' in kwargs:
            colorbarlabel = kwargs['colorbarlabel']
        if 'colorbarylabel' in kwargs:
            colorbarylabel = kwargs['colorbarylabel']
            
        # select colormap from plt colormaps
        if 'colormap' in kwargs:
            if kwargs['colormap'] in colormaps:
                colormap = kwargs['colormap']
            else:
                raise ValueError("Choose from the matplotlib colormap options.")
        else:
            colormap = 'gist_earth'

        if 'percentclip' in kwargs:
            percentclip = kwargs['percentclip']
        truecolor = [0,1,0]
        if 'truecolor' in kwargs:
            truecolor = kwargs['truecolor']
        falsecolor = [1,1,1]
        if 'falsecolor' in kwargs:
            falsecolor = kwargs['falsecolor']
        nancolor = [1,1,1]
        if 'nancolor' in kwargs:
            nancolor = kwargs['nancolor']
        brighten = 0
        if 'brighten' in kwargs:
            brighten = kwargs['brighten']
        # important!
        usepermanent = False
        if 'usepermanent' in kwargs:
            usepermanent = kwargs['usepermanent']
        medfilt = False
        if 'medfilt' in kwargs:
            medfilt = kwargs['medfilt']
        # can be removed?
        method = 'surfnorm'
        if 'method' in kwargs:
            method = kwargs['method']

        # set azimuth and altitude 
        azimuth = 315
        if 'azimuth' in kwargs:
            azimuth = kwargs['azimuth']
        altitude = 60
        if 'altitude' in kwargs:
            altitude = kwargs['altitude']
        ls = LightSource(azdeg=azimuth, altdeg=altitude)
        
        exaggerate = 2
        if 'exaggerate' in kwargs:
            exaggerate = kwargs['exaggerate']
        hillshade = ls.hillshade(self.z, vert_exag=exaggerate)

        # missing!
        if 'ticklabels' in kwargs:
            ticklabels = kwargs['ticklabels']
        # missing!
        if 'tickstokm' in kwargs:
            tickstokm = kwargs['tickstokm']
        # missing!
        if 'gridmarkers' in kwargs:
            gridmarkers = kwargs['gridmarkers']
        # missing!
        if 'gridmarkercolor' in kwargs:
            gridmarkercolor = kwargs['gridmarkercolor']

        plt.imshow(hillshade, cmap=colormap, interpolation='nearest')  

        if add_colorbar:
            plt.colorbar()
                

        plt.show()
            