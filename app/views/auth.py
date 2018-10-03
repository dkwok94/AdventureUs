#!/usr/bin/python3
'''
    Authentication functions for flask application
'''
import models
from models import storage
from app import application
from flask import render_template, flash, redirect, url_for, request, session
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user


@application.route('/', methods=['GET', 'POST'])
@application.route('/login', methods=['GET', 'POST'])
def login():
    '''
        User login function for login form
    '''
    if current_user.is_authenticated:
        return redirect(url_for('display_profile'))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = storage.get_user(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('display_profile'))
    return render_template('login.html', form=form)


@application.route('/logout')
def logout():
    '''
        User logout function to sign the user out of their account
    '''
    logout_user()
    return redirect(url_for('login'))
