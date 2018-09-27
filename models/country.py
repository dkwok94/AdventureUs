#!/usr/bin/python3
'''
    Defines the country class
'''
from models.base_model import BaseModel


class Country(BaseModel):
    '''
        Defines the country class which inherits from BaseModel
    '''
    name = ""
    code = ""
    cities = []
    states = []
    collection = "countries"
