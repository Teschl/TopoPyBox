import numpy as np
import rasterio

from .grid_mixins.aspect import AspectMixin
from .grid_mixins.imagesc import ImagescMixin
from .grid_mixins.info import InfoMixin
from .grid_mixins.gradient8 import Gradient8Mixin
from .grid_mixins.magicfunctions import MagicFunctionsMixin
from .grid_mixins.identifyflats import IdentifyflatsMixin
from .grid_mixins.imageschs import ImageschsMixin
from .grid_mixins.fillsinks import FillsinksMixin
from .grid_mixins.hillshade import HillshadeMixin

class GridObject(AspectMixin,
           ImagescMixin,
           ImageschsMixin,
           InfoMixin,
           Gradient8Mixin,
           MagicFunctionsMixin,
           FillsinksMixin,
           HillshadeMixin,
           IdentifyflatsMixin):

    def __init__(self, path):
        self.path = path
        self.load_data()

    def load_data(self):
        tiff = rasterio.open(self.path)
        self.z = tiff.read(1).astype(np.float32)

        self.name = tiff.name
        self.data_type = tiff.dtypes[0]
        self.rows = tiff.height
        self.columns = tiff.width
        self.cellsize = tiff.res[0]
        self.georef = [tiff.bounds, tiff.transform]


    def __sub__(self, other):
        if isinstance(other, GridObject):
            result = GridObject(self.path)
            result.z = self.z - other.z
            return result
        else:
            raise ValueError("Subtraction is only supported between instances of DEM.")
        
    def __add__(self, other):
        if isinstance(other, GridObject):
            result = GridObject(self.path)
            result.z = self.z + other.z
            return result
        else:
            raise ValueError("Addition is only supported between instances of DEM.")
