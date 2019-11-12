# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:57:03 2019

@author: Lord
"""

import telebot
import random
import feedparser
from bs4 import BeautifulSoup

import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class News():
    def __init__(self):
        self.news = list()
        self.tags = set()
        
        
        
    def get_News(self, url):
        
        feed = feedparser.parse(url)
        raw_News = feed['entries'] #  новости в формате списка словарей             
        for i in raw_News:
            try:
                self.news.append({'url' : i['id'],'tags' : (i['tags'][0]['term']),
                                  'data' : i['published'],'title' : i['title'],'summary' : BeautifulSoup(i['summary'], 'html.parser').get_text()})#запись словаря
            except:
                self.news.append({'url' : i['id'],'tags' : [0],
                                  'data' : i['published'],'title' : i['title'],'summary' : BeautifulSoup(i['summary'], 'html.parser').get_text()})#запись словаря
    
    
    def consider_Tags(self):
        try:
             #создание множества для того, чтобы не было повторных элементов
            for i in self.news:
                if i['tags'][0] != 0:
                    self.tags.add(i['tags'])                
            
            return 1
        except:
            return 0
    
    def get_All_News(self):
        mes = ""
        for i in self.news:            
            mes = mes + i['url'] + '\n' + i['data'] + '\n' + i['title'] + '\n' + i['summary'] + '\n\n\n\n'
        
        return mes
    
    def get_Tagged_News(self, tag):
        mes = ""
        for i in self.news:
            if i['tags'].count(tag) > 0:
                mes = mes + i['url'] + '\n' + i['data'] + '\n' + i['title'] + '\n' + i['summary'] + '\n\n\n\n'
        
        return mes
    
    def get_KWorded_News(self, keywords):
        stemmer = SnowballStemmer("russian")
        kwords = [stemmer.stem(i) for i in keywords]
        mes = ""
        for i in self.news:
            word_list = [j for j in nltk.word_tokenize(i["summary"]) if j not in string.punctuation and j not in stopwords.words('russian')]
            word_list = set([stemmer.stem(i) for i in word_list])
            flag = 0
            for k in kwords:
                if flag == 0:
                    for j in word_list:
                        if k == j:
                            flag = 1
                            break
                else:
                    break
            if flag == 1:
                mes = mes + i['url'] + '\n' + i['data'] + '\n' + i['title'] + '\n' + i['summary'] + '\n\n\n\n'
        return mes


bot = telebot.TeleBot('1059401034:AAEuVg-2Abu1thyWwi9aN-iypAX6Ozdnz14')
rss = News()
#Задаю множество фраз приветствия
greeting_tuple_human = set(['привет', 'здравствуйте', 'добрый день',
                  'доброго времени суток', 'приветствую', 'моё почтение', 'мое почтение', 'здорово'])
greeting_tuple_bot = ('Здравствуйте', 'Здравия желаю, командир. Готовность к информированию максимальная')

parting_tuple_human = set(['до свидания', 'пока', 'до скорой встречи', 'до завтра'])
parting_tuple_bot = ('Поздравляем вас с использованием лучшего бота для Telegram!!!')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    text = message.text.lower()
    words = text.split(" ")
    if set(words) & greeting_tuple_human != set():
        bot.send_message(message.chat.id, greeting_tuple_bot[random.randint(0,len(greeting_tuple_bot))])
    elif set(words) & parting_tuple_human != set():
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif text[:4] == 'http':
        rss.get_News(text)
        bot.send_message(message.chat.id, 'Я готов к работе с лентой')
    elif words[0] == 'слова':
        bot.send_message(message.chat.id, rss.get_KWorded_News(words[1:]))
    elif words[0] == 'лента':
        bot.send_message(message.chat.id, rss.get_All_News())
#@bot.message_handler(content_types=['sticker'])
#def sticker_id(message):
#    print(message)

bot.polling()
