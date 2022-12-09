#!/usr/bin/python3
'''
Select object that contains the letter a
from the database
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

    engine = create_engine(url, echo=False)
    q = engine.execute("SELECT * FROM states ORDER BY id ASC")
    db = q.fetchall()

    for i in db:
        if i[1].find('a') != -1:
            print("{}: {}".format(i[0], i[1]))
