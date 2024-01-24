import matplotlib.pyplot as plt
import numpy as np

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

class Imageschsmixin:
    def imageschs(self, *arguments):

        plt.imshow(self.z, cmap='terrain', interpolation='nearest')

        for i, element in enumerate(arguments):
            if element == "caxis":
                continue
            elif element == "colorbar":
                plt.colorbar()
                continue
            elif element == "colorbarlabel":
                plt.colorbar(label=arguments[i+1])
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
            






'''
Konzept für später:

def imageschs(self, *arguments):
    actions = {
        "caxis": lambda: None,  # Replace with the appropriate action
        "colorbar": plt.colorbar,
        "colorbarlabel": lambda label: plt.colorbar(label=label),
        "colorbarylabel": lambda: None,  # Replace with the appropriate action
        "colormap": lambda: None,  # Replace with the appropriate action
        "percentclip": lambda: None,  # Replace with the appropriate action
        "truecolor": lambda: None,  # Replace with the appropriate action
        "falsecolor": lambda: None,  # Replace with the appropriate action
        "nancolor": lambda: None,  # Replace with the appropriate action
        "brighten": lambda: None,  # Replace with the appropriate action
        "usepermanent": lambda: None,  # Replace with the appropriate action
    }

    for i, element in enumerate(arguments):
        if element in actions:
            action = actions[element]
            if len(action.__code__.co_varnames) == 1:  # Check the number of parameters the function takes
                action(arguments[i+1])
            else:
                action()
'''