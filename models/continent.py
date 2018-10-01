#!/usr/bin/python3
'''
    Defines the continent class
'''
from models.base_model import BaseModel


class Continent(BaseModel):
    '''
        Defines the continent class which inherits from BaseModel
    '''
    collection = "continents"
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.name = ""
            self.countries = []
