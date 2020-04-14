# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:21:37 2020

@author: Lord
"""

import math
from PIL import Image, ImageDraw 

image = Image.open("white.jpg")
draw = ImageDraw.Draw(image) 
width  = image.size[0] 
height = image.size[1] 
hw = width / 2
hh = height / 2
pix = image.load()
x1 = 100
x2 = 600
y1 = 150
y2 = 450
dx = abs(x2 - x1)
dy = abs(y2 - y1)
err = 0
dErr = dy
y = y1
dirY = bool(y2 - y1) 
for x in range(x1, x2 + 1):
    draw.point((x,y), (128, 255, 255))
    err += dErr
    if err * 2 >= dx:
        y += dirY
        err -= dx           
                     
image.show()
#image.save('serj8color.jpg')
del draw
