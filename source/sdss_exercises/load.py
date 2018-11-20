#!/usr/bin/env python

from astropy.io import fits
import argparse


parser=argparse.ArgumentParser(description="...", usage="...")

parser.add_argument("-f", "--files", type=str, required = True, nargs="+", \
                    dest="filename", \
                    help = "a list of files to read in from")

args =parser.parse_args()

filename = args.filename

# file name should only be a list



for i in range(len(filename)):
    hdu_list = fits.open(filename[i])
   
    print ((hdu_list))


