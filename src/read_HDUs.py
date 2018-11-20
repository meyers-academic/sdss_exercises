import argparse
from astropy.io import fits


def load_file(file_name):
  """loads file and returns hdu list"""
  try:
    hdu_list = fits.open(file_name.rstrip(','))
  except OSError as e:
    print('{0} likely not found'.format(file_name))
    raise OSError(e)
  return hdu_list


def load_and_print_file_list(file_list):
  """loads a list of files and prints how many hdus it has"""
  for file in file_list:
    hdu_list = load_file(file)
    print("'{0}' has {1} hdus in it".format(file, len(hdu_list)))
    for i in range(len(hdu_list)):
      hdu1 = hdu_list[i]
      print('BITPIX type of HDU{0} = {1}'.format(i+1, hdu1.header['BITPIX']))
    print('\n')


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='parse fits files')
  parser.add_argument("-f", '--files', nargs='+')
  args = parser.parse_args()
  load_and_print_file_list(args.files)
