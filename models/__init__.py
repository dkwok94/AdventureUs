#!/usr/bin/python3
'''
    Package initializer
'''

from models.base_model import BaseModel
from models.country import Country
from models.city import City
from models.trip import Trip
from models.user import User
from models.notification import Notification
from models.continent import Continent
from os import getenv
from models.engine.db_storage_2 import DBStorage

classes = {"BaseModel": BaseModel, "Country": Country,
           "City": City, "Trip": Trip, "User": User,
           "Notification": Notification, "Continent": Continent}

storage = DBStorage()
storage.reload()
