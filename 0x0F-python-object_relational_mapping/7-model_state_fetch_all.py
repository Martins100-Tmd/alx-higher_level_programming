#!/usr/bin/python3
'''
Select all items in the states table
'''

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    conn = create_engine(url, echo=False)
    query = conn.execute("select * from states ORDER BY id ASC")
    al = query.fetchall()
    for i in al:
        print("{}: {}".format(i[0], i[1]))
