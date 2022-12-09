#!/usr/bin/python3

'''
Select row for which state_id is equals
to name is argument name
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    state_name = argv[4].strip("'\"")
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities\
            WHERE state_id = (SELECT id from states\
            WHERE {} = %s)".format("name"), (state_name,))
    result = cursor.fetchall()

    j = 0
    for i in result:
        print(i[2], end="")
        if j != (len(result) - 1):
            print(", ", end="")
        j = j + 1

    print()

    cursor.close()
    conn.close()
