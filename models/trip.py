#!/usr/bin/python3
'''
    Defines the trip class
'''
from models.base_model import BaseModel


class Trip(BaseModel):
    '''
        Defines the trip class which inherits from BaseModel
    '''
    collection = "trips"
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.country_id = ""
            self.city_id = ""
            self.country = ""
            self.city = ""
            self.name = ""
            self.description = ""
            self.users = []
            self.host = ""
            self.host_firstname = ""
            self.host_lastname = ""
            self.host_pic = ""
            self.date_range = ""
