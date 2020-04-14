# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:21:37 2020

@author: Lord
"""

import math
from PIL import Image, ImageDraw 

image = Image.open("serj.jpg")
image2 = Image.open("grad.jpg")
draw = ImageDraw.Draw(image) 
width  = image.size[0] 
height = image.size[1] 
hw = width / 2
hh = height / 2
pix = image.load()
pix2 = image2.load()
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                a2 = pix2[x, y][0]
                b2 = pix2[x, y][1] 
                c2 = pix2[x, y][2] 
                start = hw - hw / 5 
                finish = hw + hw / 5
                if x <= start:
                    draw.point((x,y), (a2, b2, c2))
                elif start <= x <= finish:      
                    k = (x - start) / (finish - start)
                    draw.point((x,y), (math.floor(a * k  + a2 * (1 - k)), 
                                       math.floor(b * k + b2 * (1 - k)),
                                                  math.floor(c * k + c2 * (1 - k))))
                elif finish <= x:
                    draw.point((x,y), (a, b, c))
                    
#image.show()
image.save('serjskley.jpg')
del draw
