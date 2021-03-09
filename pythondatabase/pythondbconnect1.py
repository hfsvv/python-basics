#step1 import mysql.connector

import mysql.connector
#step 2 establish a connection with mysql
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123'
)
#step 3 create a cursor object

cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()