#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:30:41 2020

@author: anshul
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
 
VFILE = "./Pexels Videos 2880.mp4"

#Generator
def get_frames(filename):
    video = cv2.VideoCapture(filename)
    
    while video.isOpened:
        ret, frame = video.read()
        if ret:
            yield frame
        else:
            break
    video.release()
    yield None

'''
#creating plot
fig = plt.figure() 
#Size = 1080 by 1920
'''

#calling
for frame in get_frames(VFILE):
    if frame is None:
        break

    if cv2.waitKey(1) == 27:
        break
    #print(frame.shape)
    ''' MATPLOTLIB DOESN'T WORK FOR VIDEOS
    ax1 = fig.add_subplot(2,2,1)
    ax1.imshow(frame[0:541, 0:961])
    ax2 = fig.add_subplot(2,2,2)
    ax2.imshow(frame[0:541, 961:1920])
    ax3 = fig.add_subplot(2,2,3)
    ax3.imshow(frame[541:1080, 0:961])
    ax4 = fig.add_subplot(2,2,4)
    ax4.imshow(frame[541:1080, 961:1920])
    '''
    frame_segments = [frame[0:540, 0:960], frame[0:540, 960:1920], frame[540:1080, 0:960], frame[540:1080, 960:1920]]
    vcat = []
    
    black = [0,0,0]     #---Color of the border---
    violetColor = [255, 0, 180]
    
    for f in frame_segments:
        #--- Here I am creating the border---
        f = cv2.copyMakeBorder(f,10,10,10,10,cv2.BORDER_CONSTANT,value=black )
        #--- Here I created a violet background to include the text ---
        violet= np.zeros((30, f.shape[1], 3), np.uint8)
        violet[:] = violetColor
        #--- I then concatenated it vertically to the image with the border ---
        vcat_temp = cv2.vconcat( [violet, f] )
        #--- Now I included some text ---
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(vcat_temp,'Top - Left',(30,25), font, 1,(0,0,0), 3, 0)
        
        vcat.append(vcat_temp)
    
    
    vcat_left = cv2.vconcat([vcat[0], vcat[2]])
    vcat_right = cv2.vconcat([vcat[1], vcat[3]])
    
    #--- I finally concatenated both the above images horizontally---
    final_img = cv2.hconcat([vcat_left, vcat_right])
    cv2.imshow('Final', final_img)
    
    print("1", frame_segments[0].shape)
    print("2", frame_segments[1].shape)
    print("3", frame_segments[2].shape)
    print("4", frame_segments[3].shape)
    
    
cv2.destroyAllWindows()   
    
        
    