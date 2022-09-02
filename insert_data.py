import mysql.connector

conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')

cursor = conn.cursor()

sql = """INSERT INTO EMPLOYEE1(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('MAC', 'MOHAN', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    conn.commit()
    print("Data Inserted")
except:
    conn.rollback()
conn.close()