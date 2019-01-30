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

    imgInput = cv.imread("kermorvan.png", cv.IMREAD_GRAYSCALE)

    # fonction de rappel pour le trackbar (capture imgInput)
    def update_treshold(x):
        th, img = cv.threshold(imgInput, x, 255, cv.THRESH_BINARY);
        cv.imshow(FILENAME, img)

    # affiche l'image + trackbar
    cv.namedWindow(FILENAME)
    cv.createTrackbar('treshold', FILENAME, 0, 255, update_treshold)
    cv.setTrackbarPos('treshold', FILENAME, 120)

    while True:
        if cv.waitKey() == 27:
            break