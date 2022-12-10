#!/usr/bin/python3
'''
Define City class to map
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''
    city class that inherits from Base
    linkes to the MySQL table cities
    class attr id that repr a col of an auto-generated,
    unique int, and can't be null
    '''

    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, Foreignkey('states.id'))
