def showGraph(image, draw, mass, start, color):
    width  = image.size[0] #Определяем ширину 
    height = image.size[1]
    hw = width // 2
    hh = height // 2
    ky = hh / max(mass) 
    for i in range(hw):
        px = math.floor(i * 256 / hw) 
        for j in range(math.floor(mass[px] * ky)):
            draw.point((i + start[0], hh - j + start[1]), color)

import math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	

pix = image.load() #Выгружаем значения пикселей
green = [0 for i in range(256)]
blue = [0 for i in range(256)]
red = [0 for i in range(256)]
brightness = [0 for i in range(256)]
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                s = (a + 6 * b + 3 * c) // 10
                green[b] += 1
                blue[c] += 1
                red[a] += 1
                brightness[s] += 1

showGraph(image, draw, green, (0, 0), (0, 255, 0))
showGraph(image, draw, blue, (width // 2, 0), (0, 0, 255))       
showGraph(image, draw, red, (0, height // 2), (255, 0, 0))       
showGraph(image, draw, brightness, (width // 2, height // 2), (128, 128, 128))       
    
#image.show()
image.save('lines.jpg')
del draw
