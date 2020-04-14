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
                s = (a + 6 * b + 3 * c) // 10
                w = width / 20
                h = height / 20
                for k in range(20):
                    if x + (5 - k * 2) * w <= y / 2 <= x + (6 - k * 2) * w:
                        draw.point((x, y), (127, 128, 0))
                    
image.show()
del draw