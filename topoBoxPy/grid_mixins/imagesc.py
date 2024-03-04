import matplotlib.pyplot as plt
from matplotlib import colormaps

class ImagescMixin:
    def imagesc(self, **kwargs):
        # Get inputs from kwargs
        colormap = kwargs.get('colormap', "terrain")

        # Type checking inputs
        if not isinstance(colormap, str) or colormap not in colormaps:
            raise ValueError("colrmap must be a string chosen from the matplotlib colormap variants.")

        plt.imshow(self.z, cmap=colormap, interpolation='nearest')
        plt.colorbar()
        plt.show()
