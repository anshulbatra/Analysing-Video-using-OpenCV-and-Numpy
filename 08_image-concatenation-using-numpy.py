#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 00:39:53 2020

@author: anshul
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

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
final_cat = []
skip_frames = 12
count = 0
done = 0
for frame in get_frames(VFILE):
    if frame is None:
        break
    if cv2.waitKey(10) == 27:
        break
    
    if count % skip_frames == 0:
        final_cat.append(frame)
        done += 1   
    count += 1
    
#row_len = floor(sqrt(done))
row1 = np.concatenate(final_cat[0:5], axis = 1) #Stack Horizontally
row2 = np.concatenate(final_cat[5:10], axis = 1) #Stack Horizontally
row3 = np.concatenate(final_cat[10:15], axis = 1) #Stack Horizontally
row4 = np.concatenate(final_cat[15:20], axis = 1) #Stack Horizontally

collage = np.concatenate([row1, row2, row3, row4], axis=0)   #Stack Vertically
plt.imshow(collage)
#cv2.imshow('Collage', row1)