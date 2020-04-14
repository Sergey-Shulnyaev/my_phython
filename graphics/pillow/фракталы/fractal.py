# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:53:31 2020

@author: Lord
"""
import math
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def line(x1, y1, x2, y2):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1)
            for x in range(x1, x2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dX:
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY

class Turtle():
    def __init__(self, x, y):
        self.position = x, y
        self.direction = 0
    
    def forward(self, a):
        nx = self.position[0] + a * math.cos(self.direction * math.pi / 180)
        ny = self.position[1] + a * math.sin(self.direction * math.pi / 180)
        x, y = self.position
        line(math.floor(x), math.floor(y), math.floor(nx), math.floor(ny))
        self.position = (nx, ny)
    
    def left(self, angle):
        self.direction -= angle
    
    def right(self, angle):
        self.direction += angle
    


image = Image.open("white.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load()

turt = Turtle(400, 500)
turt.left(90)

def rec(a, k):
    if k == 1:
        turt.forward(a)
    else:
        turt.left(30)
        rec(a/2, k-1)
        turt.right(90)
        rec(a/2, k-1)
        turt.left(90)
        rec(a/2, k-1)
        turt.right(30)
for i in range(3):
    rec(200, 7)
    turt.right(120)
image.show()