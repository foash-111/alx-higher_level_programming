#!/usr/bin/python3

""" my module that link MySQLdb with python"""


import MySQLdb
import sys

args = sys.argv
conn = MySQLdb.connect(host="localhost", port=3306, user="{}".format(args[1]), passwd="{}".format(args[2]), db="{}".format(args[3]), charset="utf8")

cur = conn.cursor()

create_table = """
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
"""

insert_into_table = """
INSERT INTO states (name)
VALUES
("California"),
("Arizona"),
("Texas"),
("New York"),
("Nevada");
"""

retrive = """
SELECT * FROM states
ORDER BY id ASC;
"""
cur.execute(create_table)
cur.execute(insert_into_table)
cur.execute(retrive)

states = cur.fetchall()

for state in states:
  print(state)

cur.close()
conn.close()
