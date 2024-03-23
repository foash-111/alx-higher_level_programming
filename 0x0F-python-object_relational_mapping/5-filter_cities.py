#!/usr/bin/python3
"""A module that link MySQLdb with python3"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="{}".format(args[1]),
        password="{}".format(args[2]),
        database="{}".format(args[3]),
        charset="utf8"
    )
    cursor = connection.cursor()

    if ';' in args[4]:
        raise MySQLdb.Error

    my_select_query = """
            SELECT cities.name FROM cities
            JOIN states ON states.id = cities.state_id
            WHERE states.name = '{}';
        """.format(args[4])

    cursor.execute(my_select_query)

    my_rows = cursor.fetchall()

    string = ''
    for i in range(0, len(my_rows)):
        string += my_rows[i]
        if i == len(my_rows) - 1:
            break
        string += ', '

    cursor.close()
    connection.close()
