# Importing all necessary libraries

import numpy as np
import cv2 as cv
import os
import glob, errno

def Capturevideo():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('Subscribe3.mp4', fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if (ret == True):
            out.write(frame)
            cv.imshow('output',frame)
            if(cv.waitKey(1) &  0xFF == ord('q')):
                break
        else:
            break

    