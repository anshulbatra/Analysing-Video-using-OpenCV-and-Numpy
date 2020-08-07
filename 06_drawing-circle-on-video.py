#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:55:02 2020

@author: anshul
"""

import cv2

VFILE = "./Pexels Videos 2880.mp4"

def get_frames(filename):
    video = cv2.VideoCapture(filename)   
    
    while video.isOpened():
        ret, frame = video.read()
        
        if ret:
            yield frame
        else:
            yield None        #Could also use break here
    video.release()
    yield None
    
    
#Calling
count = 0
for frame in get_frames(VFILE):
    if frame is None:
        break
    if cv2.waitKey(10) == 27:
        break
    
    count += 1
    cv2.circle(img = frame, 
               center = (10*count,5*count) if (count<200) else (10*(393-count),5*(393-count)), 
               radius = 5*count if (count < 200) else 5*(393-count), #TERNARY OPERATOR OF PYTHON
               color = (0,0,255), #BGR Convention of CV2
               thickness = 10) 
    cv2.imshow('frame', frame)
    
print("Total Frames :", count)
cv2.destroyAllWindows()