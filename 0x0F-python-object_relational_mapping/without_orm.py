#!/usr/bin/python3

import MySQLdb
import sys

args = sys.argv

connection = MySQLdb.connect(
    host="localhost",
    port=8080,
    user="root",
    passwd="password",
    db="foash",
    charset="utf8"
)

cursor = connection.cursor()

query = "SELECT * FROM states WHERE name = '{}'".format(args[1])

cursor.execute(query)

rows = cursor.fetchall()

for i in rows:
    print(i)

cursor.close()
connection.close()
