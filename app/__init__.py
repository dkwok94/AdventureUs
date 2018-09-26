#!/usr/bin/python3
'''
    Package initialization file
'''
from flask import Flask
from app.config import Config
from flask_login import LoginManager
import models
from models import storage

application = Flask(__name__)
application.config.from_object(Config)
login = LoginManager(application)
login.login_view = 'login'

import app.views

@login.user_loader
def load_user(id):
    return storage.get("User", id)
