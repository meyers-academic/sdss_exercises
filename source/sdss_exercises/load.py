from astropy.io import fits
import argparser


parser=argparse.ArgumentParser(description="...", usage="...")
parser.add_argument("-f", "--numfiles", type=int, choices=range(100))

args =parser.parse_args()


filename = "spec-3949-55650-0042.fits"

hdu_list = fits.open(filename)
hdu1 = hdu_list[0] # FITS HDU counting is from 1
print(f"This file has {len(hdu_list)} HDUs.") print(hdu1.header) # prints header print(hdu_list.info())
object of type HDUList, can treat at list of HDUs
hdu_list.info() returns structure of file (no. of HDUs, type of each, dimensions, etc.)
 # print primary HDU header
#
for key, value in hdu1.header.items(): ! print("{0} = {1}".format(key, value))
generator to loop over each header item
  hdu_list.close()