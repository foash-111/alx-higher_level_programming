#!/usr/bin/python3
"""A module that link MySQLdb with python3"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    connection_with_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8"
    )
    data_base_delivery = connection_with_db.cursor()

    my_select_query = """
            SELECT * FROM states
            WHERE name LIKE 'N%';
        """

    data_base_delivery.execute(my_select_query)
    my_rows = data_base_delivery.fetchall()

    for row in my_rows:
        print(row)
    
    data_base_delivery.close()
    connection_with_db.close()
