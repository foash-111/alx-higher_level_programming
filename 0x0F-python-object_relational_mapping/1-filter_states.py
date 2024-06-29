#!/usr/bin/python3
"""A module that link MySQLdb with python3"""
import MySQLdb
import sys
args = sys.argv
if __name__ == "__main__":
    connection = MySQLdb.connect( #  1 connection with mysql on specific database 
        host="localhost",
        port=3306,
        user=args[1],
        password=args[2],
        database=args[3],
        charset="utf8"
    )
    cursor = connection.cursor() # from connection object with cursor method,
                                 # return an cursor instance that we can deal with tables in our database
    my_select_query = """
            SELECT id, name FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC;
        """

    cursor.execute(my_select_query) # cursor.execute("") to execute our queries.

    my_rows = cursor.fetchall()     # cursor.fetchall() to return the value that returned by execute("") method 
                                    # if we execute an select query

    for row in my_rows:
        print(row)

    cursor.close()      # by cursor.close() we close connection with tables gracefully
    connection.close()  # close connection with database
