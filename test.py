# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:36:26 2019

@author: Kanav Petkar
"""

import cv2
import numpy as np
import tkinter as tk

cross = cv2.imread("cross.png",-1)

y1, y2 = 0, cross.shape[0]
x1, x2 = 0, cross.shape[1]

alpha_fg = cross[:,:,3] / 255.0
alpha_bg = 1.0 - alpha_fg


def recordHSV(color):
    hsv = color
    print (hsv)
    cv2.destroyAllWindows()
    vc.release()

    
    


vc = cv2.VideoCapture(0)
top = tk.Tk()
B = tk.Button(top, text ="Press when your selection is between the crosshairs", command =recordHSV)
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:


    
    rval, frame = vc.read()
    for c in range(0,3):
        frame[y1:y2, x1:x2, c] = (alpha_fg * cross[:,:,c] + alpha_bg * frame[y1:y2, x1:x2, c])
    #hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #print(np.mean(frame, (0,1)))
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color = hsv_img[240, 320]
    #print (color)
    
   
    cv2.imshow('final', frame)
    key = cv2.waitKey(5)
    
    if key == 27:
        break
recordHSV(color)
    
