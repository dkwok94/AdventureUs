#!/usr/bin/python3
'''
    Defines the notification class
'''
from models.base_model import BaseModel


class Notification(BaseModel):
    '''
        Defines the notification class which inherits from BaseModel
    '''
    collection = "notifications"
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.text = ""
            self.sender = ""
            self.recipient = ""
            self.trip_id = ""
            self.trip_info = {"city": "", "country": "", "date_range": ""}
