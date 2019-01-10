#!/usr/bin/env python3


import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt
import cv2 as cv
import time
import sys
import numpy as np

if __name__ == '__main__':

	

	# arguments
	if len(sys.argv) != 2:
		print("usage:", sys.argv[0], "<filename>")
		sys.exit(-1)
	FILENAME = sys.argv[1]
    


	# load input image
	img = cv.imread(FILENAME)
	if img.size == 0:
		print("failed to load", FILENAME)
		sys.exit(-1)

	color = ('b','g','r')
	for i,col in enumerate(color):
		histr = cv.calcHist([img],[i],None,[256],[0,256])
		plt.plot(histr,color = col)
		print(histr)
	plt.yscale('log')
	plt.xlim([0,256])
	plt.show()
