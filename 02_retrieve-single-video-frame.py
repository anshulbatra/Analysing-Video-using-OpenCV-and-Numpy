#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:02:14 2020

@author: anshul
"""

import cv2

VFILE = "./Pexels Videos 2880.mp4"
index = 54;

def get_frame(filename, index):
    count = 0
    video = cv2.VideoCapture(filename)
    while video.isOpened():
        ret, frame = video.read()
        
        if ret:
            if count == index:
                return frame
            count += 1
        else:
            break
    video.release()
    return None
    

#Calling
frame = get_frame(VFILE, index)
    
if frame is None:
    print("frame not found")
else: 
    print("frame found")
    cv2.imshow('frame', frame) 
    if cv2.waitKey(25000) == 27:
        cv2.destroyAllWindows()
   
cv2.destroyAllWindows()