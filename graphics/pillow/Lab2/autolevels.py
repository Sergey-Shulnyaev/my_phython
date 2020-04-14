# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:37:36 2020

@author: Lord
"""

import math
from PIL import Image, ImageDraw 

image = Image.open("lego.jpg")
draw = ImageDraw.Draw(image) 
width  = image.size[0] 
height = image.size[1] 
hw = width / 2
hh = height / 2
pix = image.load()
green = [0 for i in range(256)]
blue = [0 for i in range(256)]
red = [0 for i in range(256)]

for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                green[b] += 1
                blue[c] += 1
                red[a] += 1
      
gmin = 0
gMax = 255   
mi = max(green)/100    
for i in range(128):
    if green[i] > mi:
        gmin = i
        break
for i in range(255, 126,-1):
    if green[i] > mi:
        gMax = i
        break
rmin = 0
rMax = 255   
mi = max(red)/100    
for i in range(128):
    if red[i] > mi:
        rmin = i
        break
for i in range(255, 126,-1):
    if red[i] > mi:
        rMax = i
        break
bmin = 0
bMax = 255   
mi = max(blue)/100    
for i in range(128):
    if blue[i] > mi:
        bmin = i
        break
for i in range(255, 126,-1):
    if blue[i] > mi:
        bMax = i    
        break
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                draw.point((x,y),(math.floor((a - rmin) * 255 /(rMax - rmin)),
                            math.floor((b - gmin) * 255 /(gMax - gmin)),
                            math.floor((c - bmin) * 255 /(bMax - bmin))))
#image.show()
image.save('legogenius.jpg')
del draw