#!/usr/bin/python3


import MYSQLdb
from sys import argv

'''
a script that list all the list of row
in a database
'''
if __name__ == "__main__":
    conn = MYSQLdb.connect(
         host="localhost", port=3306, user=argv[1],
         passwd=argv[2], db=argv[3], charset="utf-8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    table_rows = cur.fetchall()
    for row in table_rows:
        print(row)
    cur.close()
    table_rows.close()
