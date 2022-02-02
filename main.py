#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:35:47 2021

@author: ACE-OF-DIAMONDS
# """
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path="/home/juwoncha/문서/fed_selen/geckodriver")
# driver.get('https://www.linuxhint.com')
# print('Title: %s' % driver.title)
# driver.quit()


#https://news.google.com/search?q=%22Federal%20Reserve%22%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen 

from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
from datetime import date
from datetime import timedelta

today = date.today()

yesterday = today - timedelta(days = 1)

today_date = today.strftime("%m/%d/%Y")
yesterday_date = yesterday.strftime("%m/%d/%Y")

today_date = str(today_date)
yesterday_date = str(yesterday_date)

print(yesterday_date)

print(today_date)

googlenews=GoogleNews(start= yesterday_date,end= today_date)
googlenews.search('"Federal Reserve"')
result=googlenews.result()
df=pd.DataFrame(result)
print(df.head())


df.to_csv('file_name.csv')

df1 = df[['title', 'media', 'datetime', 'desc', 'link']]

df1.to_csv('parsed.csv')

df1.to_html('parsed.html')
