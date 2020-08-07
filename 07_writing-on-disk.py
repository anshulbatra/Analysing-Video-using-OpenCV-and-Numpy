#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:33:57 2020

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
    
    
#Writing on disk
fourcc = cv2.VideoWriter_fourcc(*'I420')
output_video = cv2.VideoWriter("output.mp4", fourcc, 20, (640,480))


#Calling
count = 0
for frame in get_frames(VFILE):
    if frame is None:
        break
    if cv2.waitKey(10) == 27:
        break
    
    cv2.putText(img = frame, 
                text = str(count), 
                org = (200,200), 
                fontFace = cv2.FONT_HERSHEY_COMPLEX , 
                fontScale = 1, 
                color = (0,255,0))      #BGR Convention of CV2
    output_video.write(frame)
    count += 1
    
print("Total Frames :", count)
output_video.release()
cv2.destroyAllWindows()