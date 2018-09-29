#!/usr/bin/python3
'''
    Main routes for Flask application
'''
import models
from models import storage
from app import application
from flask import render_template, flash, redirect, url_for, request, session
from flask import jsonify, abort
from app.forms import LoginForm, CreateTrip
from flask_login import current_user, login_user, logout_user, login_required
from models.user import User


@application.route('/', methods=['GET', 'POST'])
@application.route('/login', methods=['GET', 'POST'])
def login():
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
    logout_user()
    return redirect(url_for('login'))


@application.route('/profile', methods=["GET", "POST"])
@login_required
def display_profile():
    hosted_trips = []
    active_trips = []
    for trip in current_user.hosted_trips:
        hosted_trips.append(storage.get("Trip", trip))
    for trip in current_user.active_trips:
        active_trips.append(storage.get("Trip", trip))
    session['url'] = url_for('display_profile')
    tripform = CreateTrip(request.form)
    return render_template('profile.html', tripform=tripform,
                            hosted_trips=hosted_trips,
                            active_trips=active_trips)


@application.route('/adventures', methods=["GET", "POST"])
@login_required
def display_adventures():
    if request.method == "POST":
        content = request.get_json()
        print(content)
        trip = storage.get("Trip", content['id'])
        if trip:
            return jsonify(trip.to_dict())
        else:
            abort(404)
    all_trips = storage.all(models.Trip)
    session['url'] = url_for('display_adventures')
    tripform = CreateTrip(request.form)
    return render_template('adventures.html', tripform=tripform,
                            all_trips=all_trips)


@application.route('/createtrip', methods=["GET", "POST"])
@login_required
def create_trip():
    tripform = CreateTrip(request.form)
    if request.method == "POST" and tripform.validate_on_submit():
        trip_dict = {"city": tripform.city.data,
                     "country": tripform.country.data,
                     "date_range": tripform.dates.data,
                     "description": tripform.description.data,
                     "users": [current_user.username],
                     "host": current_user.username,
                     "host_pic": current_user.profile_pic,
                     "host_firstname": current_user.first_name,
                     "host_lastname": current_user.last_name}
        new_trip = models.Trip(**trip_dict)
        if current_user.hosted_trips:
            current_user.hosted_trips.append(new_trip.id)
        else:
            setattr(current_user, "hosted_trips", [new_trip.id])
        storage.save(current_user)
        storage.save(new_trip)
        return redirect(session['url'])
    else:
        return "", 204
