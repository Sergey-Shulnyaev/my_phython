# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:56:34 2020

@author: Lord
"""
from random import randint

def main():
    """
    Игра предлагает случайную загадку, необходимо отгадать одно слово.
    """
    riddles=[["Глубоко был спрятан он,\nРаз-два-три - и вышел вон,\nИ стоит он на виду.\nБелый, я тебя найду.","боровик"],
                 ["Коренастый, в шляпе новой\nГриб в бору растет сосновом.\nРады бабушка и дед:\n– Будет праздничный обед!\nОй, схватили белки вмиг\nЭтот белый…","боровик"],
                 ["Растут на опушке\nрыжие подружки,\nИх зовут …", "волнушки"],
                 ["Весь Антошка -\nШляпка да ножка.\nДождь пойдёт -\nОн подрастёт.", "гриб"],
                 ["Зашёл мужик в сосняк,\nНашёл слизняк,\nБросить - жалко,\nСъесть - сыро.", "груздь"],
                 ["Мы ребята удалые лезут в щели половые.", "веник"],
                 ["Сверху черно, внутри красно, а засунешь, так прекрасно.", "галоши"],
                 ["Чтобы спереди погладить нужно сзади полизать.", "марка"]]
    a = randint(0,len(riddles) - 1)
    riddle = riddles[a][0]
    rAnswer = riddles[a][1]
    print("Попробуйте отгадать следующую загадку:\n", riddle, sep='')
    answer = input("Ваш ответ: ")
    while answer.lower() != rAnswer:
        print("Вы не отгадали, желаете попробовать ещё раз?")
        if input().lower() == "нет":
                break    
        answer = input("Ваш ответ: ")
    print("Поздравляю вы отгадали!")
            
            
            
if __name__=='__main__':
    main()