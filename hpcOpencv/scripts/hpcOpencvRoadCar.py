#!/usr/bin/env python3

import cv2 as cv
import time
import sys
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    video = cv.VideoCapture("road_traffic.mp4")
    blue_car = cv.imread("road_auto.png", 0)
    template = cv.imread("road_auto.png")
    w, h = blue_car.shape[::-1]

    while(video.isOpened()):
        ret, frame = video.read()
        if not ret:
            break

        res = cv.matchTemplate(frame, template, cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv.rectangle(frame, top_left, bottom_right, 100, 2)
            
        # Show the final image with the matched area. 
        cv.imshow('Detected', frame) 

        if cv.waitKey(30) == 27:
            break