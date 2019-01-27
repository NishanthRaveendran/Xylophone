# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 02:05:19 2019

@author: nisha
"""

''' tk_Canvas_BGImage1.py
use a Tkinter canvas for a background image
for result see http://prntscr.com/12p9ux
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import _thread
import pygame as pg
from tkinter import *
from ctypes import windll
import tkinter as tk
from xylo import *

root = tk.Tk()

############

pg.mixer.init()
pg.init()

a = pg.mixer.Sound("A.wav")
b = pg.mixer.Sound("B.wav")
c1 = pg.mixer.Sound("C_1.wav")
c2 = pg.mixer.Sound("C_2.wav")
d = pg.mixer.Sound("D.wav")
e = pg.mixer.Sound("E.wav")
f = pg.mixer.Sound("F.wav")
g = pg.mixer.Sound("G.wav")



pg.mixer.set_num_channels(60)

g_aboveToBelow = False
t_aboveToBelow = False

#g_hit = 0
#t_hit = 0

framecount = 0

greenbounds = ([35,70,70], [75,255,255]) #green
tealbounds = ([25,165,140], [35,195,170]) #teal

vc = cv2.VideoCapture(0)

############

def leftClick(event):
    global framecount
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        rval, frame = vc.read()
        hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #    if framecount % 10 == 0:
    #        g_hit = 0
    #        t_hit = 0
        _thread.start_new_thread(showColor, (hsvframe,greenbounds[0],greenbounds[1],0))
        _thread.start_new_thread(showColor, (hsvframe,tealbounds[0],tealbounds[1],1))
        imshowDrumsticks(hsvframe)
        framecount += 1
        key = cv2.waitKey(5)
        
        if key == 27: # exit on ESC
            break
        
    cv2.destroyAllWindows()
    vc.release()

root.title('background image')
# pick a .gif image file you have in the working directory
fname = "first.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
root.geometry("%dx%d+640+480" % (w, h))
root.canvas = tk.Canvas(width=w, height=h)
root.canvas.pack(side='top', fill='both', expand='yes')
root.canvas.create_image(0, 0, image=bg_image, anchor='nw')
    

def motion(event):
    x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
    if y > 333 and y < 392 and x > 238 and x < 413:
        print("go")
        #root.canvas.delete('all')
        #fname = "second.png"
        #bg_image = tk.PhotoImage(file=fname)
        #w = bg_image.width()
        #h = bg_image.height()
        # size the window so the image will fill it
        #root.geometry("%dx%d+640+480" % (w, h))
        #root.canvas = tk.Canvas(width=w, height=h)
        #root.canvas.pack(side='top', fill='both', expand='yes')
        #root.cavas.create_image(0, 0, image=bg_image, anchor='nw')
        #root.canvas.itemconfig(root.geometry, image = bg_image)
        leftClick(event)
        



# add canvas text at coordinates x=15, y=20
# anchor='nw' implies upper left corner coordinates
# now add some button widgets
#btn1 = tk.Button(cv, text="Click")
#btn1.pack(side='left', padx=10, pady=5, anchor='se')
btn2 = tk.Button(root.canvas, text="Quit", command=root.destroy)
btn2.pack(side='left', padx=10, pady=5, anchor='sw')
root.bind('<Button-1>', motion)
root.mainloop()