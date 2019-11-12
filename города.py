# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:52:20 2019

@author: Lord

"""
import speech_recognition as sr
import sys
import webbrowser
import os
import gtts
from gtts import gTTS
import random
from bs4 import BeautifulSoup
import requests

link = 'https://on55.ru/articles/2'
page = requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')
cities = [city.text for city in soup.find_all(class_='xl63') if city.text.isalpha()] # список российских городов

city = 'москва'              
last_letter = city.lower()[-1]
print(last_letter)
new_city_list = [i for i in cities if i.lower()[0] == last_letter]
print(new_city_list)