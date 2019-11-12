# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:04:36 2019

@author: Lord
"""

import requests
from bs4 import BeautifulSoup
import feedparser



feed = feedparser.parse("https://lenta.ru/rss/news")
raw_News = feed['entries'][0]
text = BeautifulSoup(raw_News['summary'], 'html.parser').get_text()
print(text)
