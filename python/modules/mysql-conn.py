# При виборі записів з таблиці можна відфільтрувати вибірку за допомогою оператора WHERE.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Також можна вибрати записи, які починаються, включають або закінчуються цією літерою чи фразою. Для цього слід використати %.
