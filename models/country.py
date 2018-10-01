#!/usr/bin/python3
'''
    Defines the country class
'''
from models.base_model import BaseModel


class Country(BaseModel):
    '''
        Defines the country class which inherits from BaseModel
    '''
    collection = "countries"
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.name = ""
            self.code = ""
            self.cities = []
            self.states = []
