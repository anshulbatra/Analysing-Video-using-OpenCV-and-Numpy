#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:10:34 2020

@author: anshul
"""

import cv2
from matplotlib import pyplot as plt

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
    print("Dimensions: ", frame.shape)
    print("B G R ", frame[0,0,:])
    print("cv2 follows BGR where as matplotlib follows RGB")
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax1.imshow(frame)
    
    '''cv2.imshow('By CV -> B G R', frame)
    if(cv2.waitKey(5000) == 27):               #Delay in milliseconds
        cv2.destroyAllWindows()
    '''
    
    #Fixing -> Converting BGR to RGB
    print("Changing BGR to RGB")
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print("R G B ", new_frame[0,0,:])
    ax2 = fig.add_subplot(1,2,2)
    ax2.imshow(new_frame)