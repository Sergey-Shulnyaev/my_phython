# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:54:04 2019

@author: mag
"""

import feedparser

python_wiki_rss_url = "https://lenta.ru/rss/news"

feed = feedparser.parse( python_wiki_rss_url )
ke = feed.keys()
news = feed['entries'][0]
#for i in  ke:
#    print(feed[i])
#print(ke)#'feed', 'entries', 'bozo', 'headers', 'etag', 'href', 'status', 'encoding', 'version', 'namespaces'

#print(feed['entries'][0].keys())#'id', 'guidislink', 'link', 'title', 'title_detail', 'links', 'summary', 'summary_detail', 'published', 'published_parsed', 'tags'
print(news['id'], '\n', news['title'], '\n', news['summary'], '\n', news['tags'][0]['term'])