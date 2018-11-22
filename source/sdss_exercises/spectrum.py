import matplotlib.pyplot as plt
from astropy.io import fits


class Spectrum(object):
    def __init__(self, ra=None, dec=None, flux=None, wavelengths=None,
                 mjd=None, plate_id=None, fiber_id=None, filename=None):
        """ initialize spectrum object """
        self.ra = ra
        self.dec = dec
        self.flux = flux
        self.wavelengths = wavelengths
        self.mjd = mjd
        self.plate_id = plate_id
        self.fiber_id = fiber_id
        self.filename = filename
        self._name = None

    @classmethod
    def from_file(cls, filepath=None):
        """create spectrum object from file"""
        file = fits.open(filepath)
        return cls(flux=file[1].data['flux'],
                   ra=file[0].header['RA'],
                   dec=file[0].header['DEC'],
                   wavelengths=file[1].data['loglam'],
                   plate_id=file[0].header['PLATEID'],
                   fiber_id=file[0].header['FIBERID'],
                   mjd=file[0].header['MJD'],
                   filename=filepath
                   )

    @property
    def name(self):
        if self.filename is not None and self._name is None:
            self._name = '{0}-{1}-{2}'.format(self.plate_id, self.fiber_id,
                                              self.mjd)
        elif self.filename is None:
            raise NotImplementedError('Need to load from file to\
                                       properly create name')
        return self._name

    def __repr__(self):
        try:
            return self.name
        except NotImplementedError:
            print('name not specified')
