import mysql.connector

conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')

cursor = conn.cursor()

cursor.execute("DROP database IF EXISTS EMPLOYEE1")

sql ='''CREATE TABLE EMPLOYEE1(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)'''

cursor.execute(sql)
print("Table created Successfully")
conn.close()