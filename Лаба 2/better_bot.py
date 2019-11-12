# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:18:13 2019

@author: Lord
"""



import feedparser
from bs4 import BeautifulSoup
import json
import nltk
from nltk.stem.snowball import SnowballStemmer
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
            
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Добрый день список команд\n
/sub [название] [сайт] - подписаться на RSS ленту\n
/unsub [название] [название] ...  - отписаться от RSS ленты\n
/addwords [название] [слово] [слово] ... - добавить ключевые слова к RSS ленте\n
/deletewords [название] [слово] [слово] ... - удалить ключевые слова \n
/checkwords [название] [название] [название] ... - посмотреть ключевые слова для данных RSS лент\n
/checksubs - посмотреть все ленты, на которые вы подписаны\n
/update - прислать новые новости из RSS лент""")
def sentence(summary, par = 5):
    s = [nltk.word_tokenize(i) for i in nltk.sent_tokenize(summary)]
    s = s[:par]
    result = ''
    for sentence in s:
        for word in sentence:
            if set(word) & set(list('.,?!:;({<'))  == set():
                result = result + ' ' + word
            else:
                result += word
    return result + '..'

def sub(update, context):
    try:
        message = context.args
        name = message[0]
        url = message[1]
        date = None
        keywords = []
        dic = {'name': name, 'url' : url, 'date' : date, 'keywords' : keywords}
        try:
            with open('sites.json', 'r') as file:
                site_list = json.load(file)
            with open('sites.json', 'w') as file:
                site_list.append(dic)
                json.dump(site_list, file) 
        except Exception:
            with open('sites.json', 'w') as file:
                json.dump([dic], file)            
        
            
    except Exception as exxx:
        context.bot.send_message(chat_id=update.effective_chat.id, text= ('Возникла следующая ошибка '+ str(exxx)))
        
        
def unsub(update, context):
    try:
        message = context.args
        new_site_list = []
        with open('sites.json', 'r') as file:
                site_list = json.load(file)
        for i in site_list:
            flag = 0
            for j in message:
                if j == i['name']:
                    flag = 1
                    break
            if flag == 0:
                new_site_list.append(i)
                
        with open('sites.json', 'w') as file:                
            json.dump(new_site_list, file) 

        context.bot.send_message(chat_id=update.effective_chat.id, text=sublist())
                                 
    except FileNotFoundError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Нет списка сайтов, задайте его командой /sub')   
        
    except Exception as exxx:
        context.bot.send_message(chat_id=update.effective_chat.id, text= ('Возникла следующая ошибка '+ str(exxx)) )
        
def sublist():
    try:
        with open('sites.json', 'r') as file:
            site_list = json.load(file)
        if site_list != []:
            mes = 'Ваш список подписок:\n'
            for i in site_list:
                mes = mes + i['name'] + ' ' 
            return mes 
        else: 
            return 'Ваш список подписок пуст'
    except FileNotFoundError:
        return 'Нет списка сайтов, задайте его командой /sub'
    except Exception as exxx:
        return 'Возникла следующая ошибка ' + exxx

def showsublist(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = sublist())

def sitekeywords(message = []):
    try: 
        with open('sites.json' , 'r') as file:
            site_list = json.load(file)
        
        mes = 'Ваши следующие подписки с ключевыми словами:\n'
        if message != []:
            for site in site_list:
                for word in message:
                    if site['name'] == word:
                        mes = mes + word + ' ' 
                        for i in site['keywords']:
                            mes = mes + i + ' ' 
                        mes += '\n'
       
        else:
            for site in site_list:
                mes = mes + site['name'] + ' ' 
                for i in site['keywords']:
                    mes = mes + i + ' ' 
                mes += '\n'
                
        return mes    
        with open('sites.json', 'w') as file:                
                json.dump(site_list, file) 
        
    except FileNotFoundError:
        return 'Нет списка сайтов, задайте его командой /sub'   
        
    except Exception as exxx:
        return ('Возникла следующая ошибка '+ str(exxx)) 

def showkeywords(update, context):
    message = context.args
    context.bot.send_message(chat_id=update.effective_chat.id, text=sitekeywords(message))

        

def addkeywords(update, context):
    try: 
        with open('sites.json' , 'r') as file:
            site_list = json.load(file)
        
        message = context.args
        site = message[0]
        keywords = message[1:]
        for i in range(len(site_list)):
            if site_list[i]['name'] == site:
                keywords.extend(site_list[i]['keywords'])
                site_list[i]['keywords'] = keywords
                break
        
        
        with open('sites.json', 'w') as file:                
                json.dump(site_list, file) 
        
    except FileNotFoundError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Нет списка сайтов, задайте его командой /sub')   
        
    except Exception as exxx:
        context.bot.send_message(chat_id=update.effective_chat.id, text= ('Возникла следующая ошибка '+ str(exxx)) )
        
       

def deletekeywords(update, context):
    try:
        with open('sites.json' , 'r') as file:
            site_list = json.load(file)
            
        message = context.args
        site = message[0]
        keywords = message[1:]
        context.bot.send_message(chat_id=update.effective_chat.id, text =str(site_list))
        for i in range(len(site_list)):
            if site_list[i]['name'] == site:
                context.bot.send_message(chat_id=update.effective_chat.id, text =str(keywords))
                newkwords = set(site_list[i]['keywords']) - set(keywords)
                context.bot.send_message(chat_id=update.effective_chat.id, text =str(newkwords))
                site_list[i]['keywords'] = list(newkwords)
                context.bot.send_message(chat_id=update.effective_chat.id, text =str(site_list))
                context.bot.send_message(chat_id=update.effective_chat.id, text = "У сайта " + site + " удалены следующие слова: " + ', '.join(keywords))
                break
            
        with open('sites.json', 'w') as file:                
                json.dump(site_list, file) 
        
        
        
    except FileNotFoundError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Нет списка сайтов, задайте его командой /sub')   
        
    except Exception as exxx:
        context.bot.send_message(chat_id=update.effective_chat.id, text= ('Возникла следующая ошибка '+ str(exxx)) )
        


        
def update(update, context):
    """
    Обновляет ленту, отправляя новые посты с rss ленты
    """
    try:
        with open('sites.json', 'r') as file:
            site_list = json.load(file)
            
        new_site_list = []
        for site in site_list:
            raw_news = feedparser.parse(site['url'])['entries'][::-1] #запись новостей в raw файл 
            
            date = site['date']
            keywords = site['keywords']
            new_date = raw_news[-1]['published']
            if keywords == [] and date == None:
                for new in raw_news:
                    time.sleep(0.01)
                    summary = BeautifulSoup(new['summary'], 'html.parser').get_text()   
                    summary = sentence(summary)
                    mes = new['title'] + "\n\n" + summary + "\n" + new['link'] #создание сообщения для отправки
                    
                    context.bot.send_message(chat_id=update.effective_chat.id, text=mes)
                    
            elif keywords == [] and date != None:
                for new in raw_news:
                    time.sleep(0.01)
                    summary = BeautifulSoup(new['summary'], 'html.parser').get_text()
                    summary = sentence(summary)
                    if new['published'] != date:
                        mes = new['title'] + "\n\n" + summary + "\n" + new['link'] #создание сообщения для отправки
                        context.bot.send_message(chat_id=update.effective_chat.id, text=mes)
                    else:
                        break
                    
            elif keywords != [] and date == None:
                time.sleep(0.01)
                stemmer = SnowballStemmer("russian")
                kwords = set([stemmer.stem(i) for i in keywords])              
                        
                for new in raw_news:
                    summary = BeautifulSoup(new['summary'], 'html.parser').get_text()
                    summary = sentence(summary)
                    word_set = set([stemmer.stem(i) for i in summary.split(' ')])
                    if word_set & kwords != set():
                        mes = new['title'] + "\n\n" + summary + "\n" + new['link'] #создание сообщения для отправки
                        context.bot.send_message(chat_id=update.effective_chat.id, text=mes)
                        
                        
            elif keywords != [] and date != None:
                time.sleep(0.01)
                stemmer = SnowballStemmer("russian")
                kwords = set([stemmer.stem(i) for i in keywords])              
                        
                for new in raw_news:
                    
                    summary = BeautifulSoup(new['summary'], 'html.parser').get_text() 
                    summary = sentence(summary)
                    word_set = set([stemmer.stem(i) for i in summary.split(' ')])
                    if word_set & kwords != set() and new['published'] != date:
                        mes = new['title'] + "\n\n" + summary + "\n" + new['link'] #создание сообщения для отправки
                        context.bot.send_message(chat_id=update.effective_chat.id, text=mes)
                    else: 
                        break
                    
            new_site_list.append({'name': site['name'], 'url' : site['url'], 'date' : new_date, 'keywords' : site['keywords']})
        
        
        with open('sites.json', 'w') as file:                
            json.dump(new_site_list, file)         
            
    except FileNotFoundError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Нет списка сайтов, задайте его командой /sub')   

    
    except Exception as exxx:
        context.bot.send_message(chat_id=update.effective_chat.id, text= ('Возникла следующая ошибка '+ str(exxx)) )
   

def helpme(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= """Добрый день список команд\n
/sub [название] [сайт] - подписаться на RSS ленту\n
/unsub [название] [название] ...  - отписаться от RSS ленты\n
/addwords [название] [слово] [слово] ... - добавить ключевые слова к RSS ленте\n
/deletewords [название] [слово] [слово] ... - удалить ключевые слова \n
/checkwords [название] [название] [название] ... - посмотреть ключевые слова для данных RSS лент\n
/checksubs - посмотреть все ленты, на которые вы подписаны\n
/update - прислать новые новости из RSS лент""")

updater = Updater(token='TOKEN', use_context=True)
worker = updater.job_queue
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
sub_handler = CommandHandler('sub', sub)
unsub_handler = CommandHandler('unsub', unsub)
addkeywords_handler = CommandHandler('addwords', addkeywords)
deletekeyword_handler = CommandHandler('deletewords', deletekeywords)
showsubs_handler = CommandHandler('checksubs', showsublist)
showkeywords_handler = CommandHandler('checkwords', showkeywords)
check_handler = CommandHandler('update', update)
unknown_handler = MessageHandler(Filters.text, helpme)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(unsub_handler)
dispatcher.add_handler(addkeywords_handler)
dispatcher.add_handler(deletekeyword_handler)
dispatcher.add_handler(showsubs_handler)
dispatcher.add_handler(showkeywords_handler)
dispatcher.add_handler(check_handler)
dispatcher.add_handler(unknown_handler) 
            
            


updater.start_polling()
updater.idle()
            
            
            
            
            