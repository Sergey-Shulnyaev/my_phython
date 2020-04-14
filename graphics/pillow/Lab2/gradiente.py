# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:46:42 2020

@author: Lord
"""

import math
from PIL import Image, ImageDraw 

image = Image.open("serj.jpg")
draw = ImageDraw.Draw(image) 
width  = image.size[0] 
height = image.size[1] 
hw = width / 2
hh = height / 2
pix = image.load()
for x in range(width-1):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                s1 = math.floor((a + b * 6 + c * 3)/10)
                a = pix[x + 1, y][0]
                b = pix[x + 1, y][1]
                c = pix[x + 1, y][2]
                s2 = math.floor((a + b * 6 + c * 3)/10)
                
                s =128 + (s2 - s1) * 2
                draw.point((x,y), (s, s, s))
                    
image.show()
#image.save('grad.jpg')
del draw
