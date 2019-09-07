# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import random
import math

class hero():
    def __init__(self, name, coord = [0,0], health = 10, speed = 1, damage = 1, inventory = []):
        self.name = name
        self.health = health 
        self.speed = speed
        self.damage = damage
        self.inventory = inventory
        self.coord = coord
    def pick_item(self, item): # item = (1,2,3) 1-название, 2 - повышение скорости, 3 - повышение урона
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
        hero_dict[enemy].take_damage(self.damage)
        
    def take_damage(self, damage):
        self.health -= damage

        
class field():
    def __init__(self, size=(40,40)):
        self.artifacts = {(-5,-5):('MagicBullet',10,10),(5,5):('CannonOfWisdom',20,20)}
        self.size = size
    def picking_item(self, coord):
        self.artifacts.pop(coord)
        
h1 = hero('Gendalf',[5,5])
h2 = hero('Smaug',[-5,-5])
hero_dict= {'Gendalf' : h1, 'Smaug' : h2}
game_field = field()


gameend = 0
while 1:
    if gameend == 0 or hero_dict == {}:
        for her in list(hero_dict.keys()):        
            print("Ты {0} и находишься в {1}.".format(her,hero_dict[her].coord))
            if game_field.artifacts.get(tuple(hero_dict[her].coord)):
                print("Рядом лежит {0}".format(game_field.artifacts[tuple(hero_dict[her].coord)]))
            print("Что ты хочешь сделать?(shoot, move, pick)")
            action = input()
            if action == 'move':
                print("Куда ты хочешь двигаться?(up, down, right, left)")
                hero_dict[her].move(input())
                if abs(hero_dict[her].coord[0]) > game_field.size[0] / 2 or abs(hero_dict[her].coord[1]) > game_field.size[1] / 2:
                    hero_dict[her].health = 0
                    print('Герой {0} упал'.format(hero_dict[her].name))
                    hero_dict.pop(her)
            elif action == "shoot":
                print("В кого ты хочешь выстрелить{0}".format(list(hero_dict.keys())))
                enemy = input()
                hero_dict[her].shoot(enemy)
                if hero_dict[enemy].health <= 0:
                    gameend = 1
                    print('Герой {0}  умер'.format(enemy))
                    hero_dict.pop(enemy)
                else:
                    print('Ты нанёс {0} урона игроку {1}, у него осталось {2} здоровья'.format(hero_dict[her].damage, enemy, hero_dict[enemy].health)) 
            elif action == 'pick':
                item = game_field.artifacts.get(tuple(hero_dict[her].coord))
                if item != None:
                    game_field.picking_item(tuple(hero_dict[her].coord))
                    hero_dict[her].pick_item(item)
                    print("Вы подобрали {0}".format(item[0]))
            elif action == 'exit':
                gameend = 1
                break
    else:
        break

    
 
        
    
