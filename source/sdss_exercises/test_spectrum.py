from spectrum import Spectrum


def test_representation():
    data = Spectrum.from_file('../../data_files/spec-10000-57346-0002.fits')
    print(data)
    print(data.__dict__)


test_representation()
