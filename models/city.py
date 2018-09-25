#!/usr/bin/python3
'''
    Define the city class
'''
from models.base_model import BaseModel

class City(BaseModel):
    '''
        Define the class City which inherits from BaseModel
    '''
    name = ""
    country_id = ""
    state_id = ""
    collection = "cities"
