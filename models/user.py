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
    username = ""
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

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)
