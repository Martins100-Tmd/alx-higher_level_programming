#!/usr/bin/python3
''' a class Student that defines a student
'''


class Student:
    '''module class student
    '''

    def __init__(self, first_name, last_name, age):
        '''method __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method to_json
        '''
        return self.__dict__

    def reload_from_json(self, json):
        '''
        method to setattr to replace all attr of student instance

        Args:
            json(dict): student instance dictionary
        '''
        for k, v in json.items():
            setattr(self, k, v)
