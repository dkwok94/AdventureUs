#!/usr/bin/python3
'''
    Define the city class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Define the class City which inherits from BaseModel
    '''
    collection = "cities"
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.name = ""
            self.country_id = ""
            self.state_id = ""
            self.country = ""
            self.state = ""
