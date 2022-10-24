import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cbs_news"
 
)

cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE cbs_news")
cursor.execute("CREATE TABLE cbs_news (Title VARCHAR(255), Link VARCHAR(255),Image VARCHAR(255), Description VARCHAR(255))")


 
# Printing the connection object
#print(mydb)

