#!/usr/bin/python3

"""my module that link MySQLdb with python without ORM"""


import MySQLdb


elsta_atef = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="foash",
    passwd="password",
    db="foash",
    charset="utf8")

abdo = elsta_atef.cursor()

retrive = "SELECT * FROM tv_genres;"
abdo.execute(retrive)

states = abdo.fetchall()

for state in states:
    print(state)

abdo.close()
elsta_atef.close()
