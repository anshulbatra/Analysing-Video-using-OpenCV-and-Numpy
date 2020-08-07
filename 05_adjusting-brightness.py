#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:36:49 2020

@author: anshul
"""

import cv2
import numpy as np

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
for frame in get_frames(VFILE):
    if frame is None:
        break
    if cv2.waitKey(10) == 27:
        break
    
    darker = 0.5 * frame
    darker = darker.astype(np.uint8)
    #For Comparison
    final = cv2.hconcat([frame, darker])
    cv2.imshow('frame', final)
    
cv2.destroyAllWindows()