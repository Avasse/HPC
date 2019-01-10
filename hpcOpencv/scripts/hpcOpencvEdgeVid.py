#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

	# arguments
	if len(sys.argv) != 1:
		print("usage:", sys.argv[0], "<filename> <outfile> <scalaire>")
		sys.exit(-1)


	# load input image
	cap = cv.VideoCapture(0)
		
	#blur
	t0 = time.time()
	
	t1 = time.time()
	
	# flux de sortie (fichier)
	fourcc = cv.VideoWriter_fourcc(*'MPEG')
	fps = cap.get(cv.CAP_PROP_FPS)
	width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
	out = cv.VideoWriter('output.avi', fourcc, fps, (width, height))

	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break
		frame = cv.GaussianBlur(frame,(9,9),1.5)
		frame = cv.Canny(frame,0,40)
		out.write(frame)
		cv.imshow('frame', frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

