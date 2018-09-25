#!/usr/bin/python3
'''
    Defines the notification class
'''
from models.base_model import BaseModel

class Notification(BaseModel):
    '''
        Defines the notification class which inherits from BaseModel
    '''
    text = ""
    sender = ""
    recipient = ""
    trip_id = ""
    collection = "notifications"
