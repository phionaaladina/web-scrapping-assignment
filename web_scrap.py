'''
Scrape CBS news https://www.cbsnews.com/latest/rss/main and get the following data

Title
Link
Image
description
Using SqlAlchemy create a table called cbs_news and insert the data into the table.

Implement one route called /cbs_news that returns the data in json format.

NOTE: Use lxml to parse the xml data.

'''


import requests
import csv
from bs4 import BeautifulSoup




import urllib.request

response = urllib.request.urlopen('https://www.cbsnews.com/latest/rss/main').read()

soup = BeautifulSoup(response,'lxml')



titles = soup.find_all('title')
for title in titles:
     print(title.string)
   


descriptions = soup.find_all('description')
for description in descriptions:
   print(description.string)
   


images = soup.find_all('image')
for image in images:
    print(image.string)



import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cbs_news"
 
)

cursor = mydb.cursor()





print('done')


 


