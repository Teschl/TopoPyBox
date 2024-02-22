import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource

'''
.imageschs() plot hillshade image 

is made to emulate it's MATLAB counterpart as best
as possible using matplotlib. You can plot manually by
using GRIDobj.z, which is a numpy matrix.

Syntax:
    DEM.imageschs()
    DEM.imageschs(pn, pv, ...)

Input:
    DEM     digital elevation model (GRIDobj)

Parameter/Value Pairs:
    caxis
    colorbar        bool,   true (default) to show colorbar
    colorbarlabel   string, title for colorbar

Output:
'''

class ImageschsMixin:
    def imageschs(self, *arguments):

        elevation_data = np.random.random((10, 10))

        light_source = LightSource(azdeg=315, altdeg=45)

        hillshade = light_source.hillshade(elevation_data)

        plt.imshow(self.z, cmap='terrain', interpolation='nearest')

        for i, element in enumerate(arguments):
            if element == "caxis":
                continue
            elif element == "colorbar":
                if arguments[i+1] in ["True","1","true"]:
                    colorbar = plt.colorbar()
                continue
            elif element == "colorbarlabel":
                colorbar = plt.colorbar(label=arguments[i+1])
                continue
            elif element == "colorbarylabel":
                continue
            elif element == "colormap":
                continue
            elif element == "percentclip":
                continue
            elif element == "truecolor":
                continue
            elif element == "falsecolor":
                continue
            elif element == "nancolor":
                continue
            elif element == "brighten":
                continue
            elif element == "usepermanent":
                continue
            elif element == "medfilt":
                continue
            elif element == "method":
                continue
            elif element == "azimuth":
                continue
            elif element == "altitude":
                continue
            elif element == "exaggerate":
                continue
            elif element == "ticklabels":
                continue
            elif element == "tickstokm":
                continue
            elif element == "gridmarkers":
                continue
            elif element == "gridmarkercolor":
                continue

            
            plt.show()
            