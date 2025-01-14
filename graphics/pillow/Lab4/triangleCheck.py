# Для выполнения практической работы номер 2 используйте ЭТОТ файл
import random
import math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("bear.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def lineP(p1, p2, color):  # рисуем линию из точки p1(x1,y1) в точку p2(x2,y2)
        x1 = p1[0]  # Перекладываем координаты точек в более понятные переменные
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        dX = abs(x2 - x1) # Вычисляем "смещение по X"
        dY = abs(y2 - y1) # Вычисляем "смещение по Y"
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY # "Изменение ошибки"
            y = y1    # текущий Y (начальное значение)
            dirY = sign(y2 - y1) # направление изменения Y
            for x in range(x1, x2 + 1): # перебираем все X от x1 до x2
                    draw.point((x,y),color) # закрашиваем пиксель (x,y)
                    err += dErr             # добавляем "смежение" к "ошибке"
                    if err + err >= dX: # если "ошибка" накопилась
                            y += dirY   # изменяем Y на 1
                            err -= dX   # вычитаем из "ошибки" dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),color)
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY
def triangle (p1, p2, p3, color): # Рисуем треугольник по трем точкам - p1, p2, p3
	# Сейчас здесь вместо заливки треугольника просто рисуются его границы
	# Нужно именно здесь расположить код своей программы, которая будет
	# Закрашивать треугольник
        lineP(p1, p2, color)
        lineP(p2, p3, color)
        lineP(p1, p3, color)
        if p2[0] > p3[0]:
            p2, p3 = p3, p2
        if p1[0] > p2[0]:
            p1, p2 = p2, p1
        if p2[0] > p3[0]:
            p2, p3 = p3, p2
        #y - y1 = k1(x - x1)
        k1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
        k2 = (p3[1] - p1[1]) / (p3[0] - p1[0])
        k3 = (p3[1] - p2[1]) / (p3[0] - p2[0])
        ycenter = k2 * (p2[0] - p1[0]) + p1[1]
               
        if ycenter > p2[1]:
            for x in range(p1[0], p2[0] + 1):
                y1 = math.floor(k1 * (x - p1[0]) + p1[1]) 
                y2 = math.floor(k2 * (x - p1[0]) + p1[1])
                for y in range(y1, y2 + 1):
                    draw.point((x,y), color)
                           
            for x in range(p2[0], p3[0] + 1):
                y1 = math.floor(k3 * (x - p2[0]) + p2[1]) 
                y2 = math.floor(k2 * (x - p1[0]) + p1[1])
                for y in range(math.floor(y1), math.floor(y2) + 1):
                    draw.point((x,y), color)
        else:
            for x in range(p1[0], p2[0] + 1):
                y1 = math.floor(k1 * (x - p1[0]) + p1[1]) 
                y2 = math.floor(k2 * (x - p1[0]) + p1[1])
                for y in range(y2, y1 + 1):
                    draw.point((x,y), color)
                           
            for x in range(p2[0], p3[0] + 1):
                y1 = math.floor(k3 * (x - p2[0]) + p2[1]) 
                y2 = math.floor(k2 * (x - p1[0]) + p1[1])
                for y in range(y2, y1 + 1):
                    draw.point((x,y), color)
            
        
# В следующих строках задаются цвета треугольников и точки, по которым они строятся
black = (0,0,0)
green = (0,200,0)
red = (200,0,0)
blue = (0,0,200)
t1 = (0,height//4)
t2 = (width//2, 0)
t3 = (width//4, height//2)
t4 = (width-1,height//2)
t5 = (width//2,height//4)
t6 = (width*3//4,0)
t7 = (0,height//2)
t8 = (width//4,height-1)
t9 = (width//2,height*3//4)
t10 = (width-1,height*3//4)
t11 = (width*3//4,height//2)
t12 = (width//2,height-1)
# Ниже вызываем заливку 4-х треугольников для проверки работы программы
triangle(t1, t2, t3, green)
triangle(t4, t5, t6, red)
triangle(t7, t8, t9, blue)
triangle(t10, t11, t12, black)

image.show()
#image.save("result.jpg")
del draw
