import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


class ImagescMixin:
    def imagesc(self):
        plt.imshow(self.z, cmap='terrain', interpolation='nearest')
        
        #color_bar = plt.colorbar()
        plt.colorbar()
        #color_bar.formatter.set_useMathText(False)
        #color_bar.update_ticks()
        plt.show()
