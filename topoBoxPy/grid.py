# import external modules
import numpy as np
import rasterio

# import functions for Grid
from .grid_mixins.aspect import AspectMixin
from .grid_mixins.imagesc import ImagescMixin
from .grid_mixins.info import InfoMixin
from .grid_mixins.gradient8 import Gradient8Mixin
from .grid_mixins.andGrid import AndGridMixin

class Grid(AspectMixin,
           ImagescMixin,
           InfoMixin,
           Gradient8Mixin,
           AndGridMixin):

    def __init__(self, path):
        # path: path of .tif file
        self.path = path

        # open tiff
        tiff = rasterio.open(path)

        # read z of tiff
        self.z = tiff.read(1).astype(np.float32)

        self.name = tiff.name
        self.data_type = tiff.dtypes[0]
        self.rows = tiff.height
        self.columns = tiff.width
        self.cellsize = tiff.res[0]
        self.georef = [tiff.bounds, tiff.transform]

        # Example for metadata with: tiff.profile
        # alternative of reading with Image

        # self.z = np.array(Image.open(path))
        