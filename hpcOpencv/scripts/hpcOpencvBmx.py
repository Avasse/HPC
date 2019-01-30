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

    cap = cv.VideoCapture(FILENAME)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        blurred = cv.GaussianBlur(frame, (9, 9), 1.5)
        cannied = cv.Canny(blurred, 0, 40)
        cv.imshow(FILENAME, cannied)
        if cv.waitKey(30) == 27:
            break

