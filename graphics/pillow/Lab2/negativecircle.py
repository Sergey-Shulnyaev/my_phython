# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:37:36 2020

@author: Lord
"""

import math
from PIL import Image, ImageDraw 

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image) 
width  = image.size[0] 
height = image.size[1] 
hw = width / 2
hh = height / 2
pix = image.load()
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if x ** 2 + (y - hh) ** 2 <= hh ** 2:
                    draw.point((x,y), (255 - a, 255 - b, 255 - c))
                    
image.show()
del draw