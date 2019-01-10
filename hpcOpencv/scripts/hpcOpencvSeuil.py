#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

	

	# arguments
	if len(sys.argv) != 2:
		print("usage:", sys.argv[0], "<filename>")
		sys.exit(-1)
	FILENAME = sys.argv[1]
    


	# load input image
	imgIn = cv.imread(FILENAME)
	if imgIn.size == 0:
		print("failed to load", FILENAME)
		sys.exit(-1)

	def update_win(x):
		img = cv.split(imgIn)[0]
		(retVal, newImg) = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
		cv.imshow('kermorvan', newImg)
		
	cv.namedWindow('kermorvan')
	cv.createTrackbar('mytrackbar', 'kermorvan', 0, 255, update_win)
	cv.setTrackbarPos('mytrackbar', 'kermorvan', 126)

while True:
    if cv.waitKey() == 27:
        break
    

