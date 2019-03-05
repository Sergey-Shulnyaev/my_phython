# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:55:58 2019

"""
import random

def word_chose(l):
    a = random.randint(0,len(l)-1)
    return l[a]

def sym_chose(word):
    b = random.randint(0,len(word)-1)
    sym = word[b]
    new_word=word[:b]+'?'+word[b+1:]
    return new_word, sym



words = ['картина', 'дом', 'город', 'страна', 'метрополия', 'река', 'комната', 'квартира', 'пол', 'стена', 'стол', 'ноутбук']
word = word_chose(words)
question = sym_chose(word)
print(question[0])
sym=input('Введите букву:\t')
if question[1] == sym:
    print('Победа!\nСлово:',word)
else:
    print('Увы, вы проиграли.\nСлово:',word)
    