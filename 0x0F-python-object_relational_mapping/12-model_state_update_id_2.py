#!/usr/bin/python3
'''
update a row from the db
'''


from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)

    engine = create_engine(url, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).filter(State.id == 2).first()
    row.name = "New Mexico"
    session.commit()
