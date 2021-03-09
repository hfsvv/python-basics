from mysql.connector import *
db=connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='pythondec'
)
cursor=db.cursor()
sql='create table movie(id int,name varchar(50),year varchar(50),rating int)'
cursor.execute(sql)
print("table created")
db.close()
