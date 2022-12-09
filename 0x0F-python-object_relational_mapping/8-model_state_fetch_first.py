#!/usr/bin/python3

'''
prints the first state object from the database
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
    qry = engine.execute("SELECT * from states WHERE id=1")
    db = qry.fetchall()
    db = db[0]
    print("{}: {}".format(db[0], db[1]))
