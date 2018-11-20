from astropy.io import fits
import argparse


parser=argparse.ArgumentParser(description="...", usage="...")
parser.add_argument("-f", "--filename", nargs='+')

args = parser.parse_args()
filename=args.filename

# filename = [x.strip(",") for x in filename]
print(type(filename))

for x in filename:
	print(x)
	hdu_list = fits.open(x)
	print(len(hdu_list))
	hdu_list.close()
