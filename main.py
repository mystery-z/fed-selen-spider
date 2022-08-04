#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created on Mon Dec 27 22:35:47 2021

@author: ace-of-diamonds
# """

#https://news.google.com/search?q=%22Federal%20Reserve%22%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen 
def collect_data():
	from GoogleNews import GoogleNews
	from newspaper import Article
	import pandas as pd
	from datetime import date
	from datetime import timedelta

	import ssl
	ssl._create_default_https_context = ssl._create_unverified_context

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

def send_mail():
	import smtplib, ssl
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from datetime import timedelta
	from datetime import date

	today = date.today()

	yesterday = today - timedelta(days = 1)

	today_date = today.strftime("%m-%d-%Y")
	yesterday_date = yesterday.strftime("%m-%d-%Y")

	today_date = str(today_date)
	yesterday_date = str(yesterday_date)

	sender_email = "anothername@gmail.com"
	receiver_email = "name@gmail.com"
	password = "*******"

	message = MIMEMultipart("alternative")
	message["Subject"] = "Federal Reserve News-" + today_date
	message["From"] = sender_email
	message["To"] = receiver_email

	# Create the plain-text and HTML version of your message
	html=open(today_date+"parsed.html")
	# Turn these into plain/html MIMEText objects
	part2 = MIMEText(html.read(), "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part2)

	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(
			sender_email, receiver_email, message.as_string()
		)
		
	print("mail sent successfully")
		
import schedule
import time

def job():
	collect_data()
	time.sleep(60)
	send_email()

schedule.every().day.at("08:00").do(job)

while True:
	print(".")
	schedule.run_pending()
	time.sleep(1)
