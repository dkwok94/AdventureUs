#!/usr/bin/python3
'''
    Define the user class
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
        Defines the user class which inherits from BaseModel
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    profile_pic = ""
    bio = ""
    destinations = []
    interests = ""
    languages = []
    friends = []
    images = []
    contact_info = {}
    hosted_trips = []
    active_trips = []
    notifications = {}
    collection = "users"
