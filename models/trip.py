#!/usr/bin/python3
'''
    Defines the trip class
'''
from models.base_model import BaseModel


class Trip(BaseModel):
    '''
        Defines the trip class which inherits from BaseModel
    '''
    country_id = ""
    city_id = ""
    name = ""
    description = ""
    users = []
    host_id = ""
    date_range = ""
    collection = "trips"
