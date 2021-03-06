#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:35:47 2021

@author: ace-of-diamonds
# """
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

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

today_date = str(today.strftime("%m/%d/%Y"))
yesterday_date = str(yesterday.strftime("%m/%d/%Y"))

print(yesterday_date)

print(today_date)

googlenews=GoogleNews(start= yesterday_date,end= today_date)
googlenews.search('"Federal Reserve"')
result=googlenews.result()
df=pd.DataFrame(result)
print(df.head())


today_date = str(today.strftime("%m-%d-%Y"))
yesterday_date = str(yesterday.strftime("%m-%d-%Y"))


df.to_csv(today_date+'.csv')

df1 = df[['title', 'media', 'datetime', 'desc', 'link']]

df1.to_csv(today_date+'parsed.csv')

df1.to_html(today_date+'parsed.html')
