import matplotlib.pyplot as plt

class ImagescMixin:
    def imagesc(self):
        plt.imshow(self.z, cmap='terrain', interpolation='nearest')
        plt.colorbar()
        plt.show()
