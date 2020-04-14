# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:21:37 2020

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
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                s = (a + b * 6 + c * 3) // 10
                draw.point((x,y), ((s // 64) * 64 - 1, (s // 64) * 64 - 1, (s // 64) * 64 - 1))
                    
#image.show()
image.save('seriy.jpg')
del draw
