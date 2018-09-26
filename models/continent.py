#!/usr/bin/python3
'''
    Defines the continent class
'''
from models.base_model import BaseModel


class Continent(BaseModel):
    '''
        Defines the continent class which inherits from BaseModel
    '''
    name = ""
    countries = []
    collection = "continents"
