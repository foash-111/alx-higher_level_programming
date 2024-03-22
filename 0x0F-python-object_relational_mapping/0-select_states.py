#!/usr/bin/python3

"""my module that link MySQLdb with python"""

import MySQLdb
import sys

class Linker:
  """link MySQLdb with python"""

  def __init__():
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user="{}".format(args[1]), passwd="{}".format(args[2]), db="{}".format(args[3]), charset="utf8")

    cur = conn.cursor()
    retrive = """
    SELECT * FROM states
    ORDER BY id ASC;
    """
    cur.execute(retrive)

    states = cur.fetchall()

    for state in states:
      print(state)

    cur.close()
    conn.close()
if __name__ == "__main__":
  obj = Linker()
