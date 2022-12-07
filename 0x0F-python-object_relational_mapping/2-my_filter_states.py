#!/usr/bin/python3


import MySQLdb
from sys import argv
'''
list row for which name matches argument
'''

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = conn.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE '{:s}'"
            " ORDER BY id ASC".format(name))

    db = cursor.fetchall()

    L = list(db)
    if L[0][1] == L[1][1]:
        print(L[0])
    cursor.close()
    conn.close()
