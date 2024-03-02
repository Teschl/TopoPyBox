import matplotlib.pyplot as plt
from matplotlib import colormaps

class ImagescMixin:
    def imagesc(self, **kwargs):
        # select colormap from plt colormaps
        if 'colormap' in kwargs:
            if kwargs['colormap'] in colormaps:
                colormap = kwargs['colormap']
            else:
                raise ValueError("Choose from the matplotlib colormap options.")
        else:
            colormap = 'gist_earth'

        plt.imshow(self.z, cmap=colormap, interpolation='nearest')
        plt.colorbar()
        plt.show()
