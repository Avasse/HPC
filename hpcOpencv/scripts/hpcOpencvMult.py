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

    imgOut = cv.imread(FILENAME) * (float(0.5) / 255)

    # affiche l'image
    cv.imshow(FILENAME, imgOut)

    # lit le clavier en boucle et quitte si "esc"
    while True:
        k = cv.waitKey() & 0xFF
        if (k == 27):
            break
