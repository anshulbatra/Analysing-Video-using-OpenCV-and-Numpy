#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 07:21:07 2020

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
for frame in get_frames(VFILE):
    if frame is None:
        break
    if cv2.waitKey(10) == 27:
        break
    
    cv2.imshow('frame', frame)
    
cv2.destroyAllWindows()
        