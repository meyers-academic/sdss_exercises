import matplotlib.pyplot as plt
from astropy.io import fits

class Spectrum(object):
  def __init__(self, filepath=None):
    self.filepath = filepath
    self._datafile = None
    self._ra = None
    self._dec = None

  @property
  def ra(self):
    ''' Returns the RA of this spectrum in degrees. '''
    if self._ra == None:
        hdu_list = self.datafile
        hdu1 = hdu_list[0] # FITS HDU counting is from 1
        self._ra = hdu1.header['RA']
    return self._ra

  @property
  def dec(self):
    ''' Returns the DEC of this spectrum in degrees. '''
    if self._dec == None:
        hdu_list = self.datafile
        hdu1 = hdu_list[0] # FITS HDU counting is from 1
        self._dec = hdu1.header['DEC']
    return self._dec

  @property
  def datafile(self):
    if self._datafile == None:
      self._datafile = fits.open(self.filepath)
    return self._datafile
