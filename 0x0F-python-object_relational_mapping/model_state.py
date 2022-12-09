#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    State class:
    inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is primary key
    class atrribute name that represent a column of string with max
    char of 128 can;t be null also
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name =  Column(String(128), nullable=False)
