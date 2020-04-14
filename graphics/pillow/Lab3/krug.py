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
start = hw * 2 / 3
finish = hw
color = (192, 255, 255)
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if (x - hw) ** 2 + (y - hh) ** 2 <= start ** 2:
                    draw.point((x,y), (a, b, c))
                elif (x - hw) ** 2 + (y - hh) ** 2 <= finish ** 2:
                    r = math.sqrt((x - hw) ** 2 + (y - hh) ** 2)
                    k = (r - start)/(finish - start)
                    draw.point((x,y), (math.floor((1 - k) * a + k * color[0]), 
                                math.floor((1 - k) * b + k * color[1]), 
                                math.floor((1 - k) * c + k * color[2])))
                else: 
                    draw.point((x,y), color)
                     
#image.show()
image.save('serjkrug.jpg')
del draw
