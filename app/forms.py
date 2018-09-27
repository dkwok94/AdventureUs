#!/usr/bin/python3
'''
    Form classes
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from models import storage
import models

def get_countries():
    choices = []
    countries = storage.all(models.Country)
    for country in countries.values():
        choices.append((country.name, country.name))
    return choices

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Log In')

class CreateTrip(FlaskForm):
    city = StringField(validators=[DataRequired()])
    country = SelectField(choices=get_countries(), validators=[DataRequired()]) 
    dates = StringField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    create = SubmitField('CREATE TRIP')
