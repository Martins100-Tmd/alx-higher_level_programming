#!/usr/bin/python3


'''
list city and state
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            )

    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON states.id=cities.states_id ORDER BY id ASC")

    result = cursor.fetchall()
    for i in result:
        print(i)
