#!/usr/bin/python3
"""A module that link MySQLdb with python3"""


if __name__ == "__main__":   
    import MySQLdb
    import sys
    args = sys.argv
    connection_with_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="{}".format(args[1]),
        passwd="{}".format(args[2]),
        db="{}".format(args[3]),
        charset="utf8"
    )
    data_base_delivery = connection_with_db.cursor()

    my_select_query = """
            SELECT * FROM states
            WHERE name LIKE 'n%'
            ORDER BY id ASC;
        """

    data_base_delivery.execute(my_select_query)
    my_rows = data_base_delivery.fetchall()

    for row in my_rows:
        print(row)
    
    data_base_delivery.close()
    connection_with_db.close()
