# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:37:36 2020

@author: Lord
"""

import math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
hw = width / 2
hh = height / 2
k = 256 / hw
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                s = (a + 6 * b + 3 * c) // 10
                if (x - hw)**2 + (y - hh)**2 <= hh**2 // 4:
                    draw.point((x, y), (0, 255, 255))
                elif x // 20 % 2 == 1 and height / 4 <= y <= height * 3 / 4 :
                    draw.point((x, y), (255, 0, 0))
    
image.show()
del draw