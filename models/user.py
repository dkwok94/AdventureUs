#!/usr/bin/python3
'''
    Define the user class
'''
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, BaseModel):
    '''
        Defines the user class which inherits from BaseModel
    '''
    collection = "users"
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.city = ""
            self.country = ""
            self.username = ""
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            self.profile_pic = ""
            self.bio = ""
            self.destinations = []
            self.interests = ""
            self.languages = []
            self.friends = []
            self.images = []
            self.contact_info = {}
            self.hosted_trips = []
            self.active_trips = []
            self.notifications = {"sent": [], "received": [], "rejected": [], "approved": []}

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)
