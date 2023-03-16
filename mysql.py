#Created by Desislava Pavlova AKA DeepPpz

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    database = 'sims_database'
)

mycursor = mydb.cursor()
#traits.idb is the file, sims_database is the directory/database
mycursor.execute("SELECT * FROM traits")

myresult = mycursor.fetchall()

print(myresult)
