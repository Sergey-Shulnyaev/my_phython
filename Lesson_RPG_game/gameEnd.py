# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import random
import math

class Hero():
    def __init__(self, name, coord = [0,0], health = 10, speed = 1, damage = 1, inventory = []):
        self.name = name
        self.health = health 
        self.speed = speed
        self.damage = damage
        self.inventory = inventory
        self.coord = coord
    def pickItem(self, item): # item = (1,2,3) 1-название, 2 - повышение скорости, 3 - повышение урона
        self.inventory.append(item)
        
        self.speed += item[1]
        self.damage += item[2]
        return "Hero pick{0}".format(str(item))
    def move(self, direction):
        if direction == 'up':
            self.coord[1] -= self.speed 
        elif direction == 'down':
            self.coord[1] += self.speed 
        elif direction == 'left':
            self.coord[0] -= self.speed 
        elif direction == 'right':
            self.coord[0] -= self.speed 
    def shoot(self, enemy):
        heroDict[enemy].takeDamage(self.damage)
        
    def takeDamage(self, damage):
        self.health -= damage

        
class Field():
    def __init__(self, size=(40,40)):
        self.artifacts = {(-5,-5):('MagicBullet',10,10),(5,5):('CannonOfWisdom',20,20)}
        self.size = size
    def pickingItem(self, coord):
        self.artifacts.pop(coord)
        
h1 = Hero('Gendalf',[5,5])
h2 = Hero('Smaug',[-5,-5])
heroDict= {'Gendalf' : h1, 'Smaug' : h2}
gameField = Field()


gameend = 0
while True:
    if gameend == 0 and heroDict != {}:
        for her in list(heroDict.keys()):        
            print("Ты {0} и находишься в {1}.".format(her,heroDict[her].coord))
            if gameField.artifacts.get(tuple(heroDict[her].coord)):
                print("Рядом лежит {0}".format(gameField.artifacts[tuple(heroDict[her].coord)]))
            print("Что ты хочешь сделать?(shoot, move, pick)")
            action = input()
            if action == 'move':
                print("Куда ты хочешь двигаться?(up, down, right, left)")
                heroDict[her].move(input())
                if abs(heroDict[her].coord[0]) > gameField.size[0] / 2 or abs(heroDict[her].coord[1]) > gameField.size[1] / 2:
                    heroDict[her].health = 0
                    print('Герой {0} упал'.format(heroDict[her].name))
                    heroDict.pop(her)
            elif action == "shoot":
                print("В кого ты хочешь выстрелить{0}".format(list(heroDict.keys())))
                enemy = input()
                heroDict[her].shoot(enemy)
                if heroDict[enemy].health <= 0:
                    gameend = 1
                    print('Герой {0}  умер'.format(enemy))
                    heroDict.pop(enemy)
                else:
                    print('Ты нанёс {0} урона игроку {1}, у него осталось {2} здоровья'.format(heroDict[her].damage, enemy, heroDict[enemy].health)) 
            elif action == 'pick':
                item = gameField.artifacts.get(tuple(heroDict[her].coord))
                if item != None:
                    gameField.pickingItem(tuple(heroDict[her].coord))
                    heroDict[her].pickItem(item)
                    print("Вы подобрали {0}".format(item[0]))
            elif action == 'exit':
                gameend = 1
                break
    else:
        break

    
 
        
    
