import gstools as gs
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal

MODEL_TYPES = ['Exponential', 'Gaussian', 'Matern', 'Spherical']

# this class implements gis kriging
# which can take a set of points and interpolate
class Kriger:

  def __init__(self, ul, lr, cell_size):
    self.min_x = ul[0]
    self.min_y = lr[1]
    self.max_x = lr[0]
    self.max_y = ul[1]
    self.cell_size = cell_size
    self.variogram_var = 1
    self._interpolated_values = None
    self._interpolated_variance = None

  # data MUST be a N x 3 list or numpy array
  def set_data(self, data):
    if type(data) == list:
      data = np.array(data)
    assert data.shape[1] == 3

    # make sure all data points are within the bounds
    assert np.all(data[:, 0] >= self.min_x), "Data point outside of bounds"
    assert np.all(data[:, 0] <= self.max_x), "Data point outside of bounds"
    assert np.all(data[:, 1] >= self.min_y), "Data point outside of bounds"
    assert np.all(data[:, 1] <= self.max_y), "Data point outside of bounds"

    # calculate the variogram variance
    total_variance = np.var(data[:, 2])
    if total_variance > 0:
      self.variogram_var = total_variance

    self.data = data

  # main interpolation function
  # model = Variogram model to use
  #   options = ['Exponential', 'Gaussian', 'Matern', 'Spherical']
  # var = Variogram variance 
  # len_scale = The len_scale (length scale) in a variogram model represents 
  #   the distance over which the spatial correlation between data 
  #   points significantly decreases. In simpler terms, it is the 
  #   distance beyond which the values of the spatial 
  #   variable become essentially uncorrelate
  # nugget = Variogram nugget
  def interpolate(self, model='Exponential', len_scale=1, nodata=False, nugget=0):
    assert model in MODEL_TYPES, "Invalid model type"

    model_class = getattr(gs, model) # variogram model
    model = model_class(dim=2, var=self.variogram_var, len_scale=len_scale, nugget=nugget)

    # make sure data has the right shape
    assert self.data.shape[1] == 3

    # Extract latitudes, longitudes, and data from the input
    lons, lats, data = self.data[:, 0], self.data[:, 1], self.data[:, 2]
      
    # Set up the kriging "model", which is the variogram model and the data
    krige = gs.krige.Ordinary(model, cond_pos=[lons, lats], cond_val=data)
      
    # Create a meshgrid of points to interpolate
    x = np.linspace(self.min_x, self.max_x,
      int((self.max_x - self.min_x) / self.cell_size) + 1)
    y = np.linspace(self.min_y, self.max_y,
      int((self.max_y - self.min_y) / self.cell_size) + 1)
    grid_x, grid_y = np.meshgrid(x, y, indexing='xy')
     
    # Perform kriging on the entire grid and extract the values and
    # the variance profile. then take the interpolated values and reshape
    # them to the shape of the grid
    krige_result = krige([grid_x.flatten(), grid_y.flatten()])
    (interpolated_values, krige_variance) = krige_result

    if nodata is True:
      min_variance = np.min(krige_variance)
      max_variance = np.max(krige_variance)
      if min_variance < max_variance:
        normalized_variance = (krige_variance - min_variance) / (max_variance - min_variance)
      interpolated_values[normalized_variance > 0.95] = np.nan

    # now we have to flip the interpolated values so that the 
    # origin is in the upper left
    self._interpolated_values = interpolated_values.reshape(grid_y.shape)[::-1, :]

    return self._interpolated_values

  def plot_interpolated_grid(self):
    plt.imshow(self._interpolated_values, origin='upper', cmap='viridis')
    plt.colorbar()
    plt.show()
