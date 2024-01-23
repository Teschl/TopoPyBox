import matplotlib.pyplot as plt
import numpy as np


class Imageschsmixin:
    def imagesc(self, *arguments):
        for i, element in enumerate(arguments):
            if element == "":
                pass
            elif element == "caxis":
                pass
            elif element == "colorbar":
                plt.colorbar()
            elif element == "colorbarlabel":
                plt.colorbar(sc, label='Colorbar Label')
            elif element == "colorbarylabel":
                pass
            elif element == "colormap":
                pass
            elif element == "percentclip":
                pass
            elif element == "truecolor":
                pass
            elif element == "falsecolor":
                pass
            elif element == "nancolor":
                pass
            elif element == "brighten":
                pass
            elif element == "usepermanent":
                pass
            elif element == "medfilt":
                pass
            elif element == "method":
                pass
            elif element == "azimuth":
                pass
            elif element == "altitude":
                pass
            elif element == "exaggerate":
                pass
            elif element == "ticklabels":
                pass
            elif element == "tickstokm":
                pass
            elif element == "gridmarkers":
                pass
            elif element == "gridmarkercolor":
                pass

            plt.show()
            