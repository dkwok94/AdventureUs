#!/usr/bin/python3
'''
    View functions for the various flask web pages
'''
import models
from models import storage
from app import application
from flask import render_template, flash, redirect, url_for, request, session
from flask import jsonify, abort
from app.forms import CreateTrip
from flask_login import current_user, login_required


@application.route('/profile', methods=["GET", "POST"])
@login_required
def display_profile():
    '''
        Loads the current user profile from the database
    '''
    hosted_trips = []
    active_trips = []
    for trip in current_user.hosted_trips:
        hosted_trips.append(storage.get("Trip", trip))
    for trip in current_user.active_trips:
        active_trips.append(storage.get("Trip", trip))
    session['url'] = url_for('display_profile')
    tripform = CreateTrip(request.form)
    return render_template('my_profile.html', tripform=tripform,
                            hosted_trips=hosted_trips,
                            active_trips=active_trips)


@application.route('/adventures', methods=["GET", "POST"])
@login_required
def display_adventures():
    '''
        Loads the current trips with active status from the database
    '''
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

@application.route('/notifications', methods=["GET"])
@login_required
def display_notifications():
    '''
        Displays the user's received and sent requests/notifications
    '''
    sent = []
    received = []
    session['url'] = url_for('display_notifications')
    tripform = CreateTrip(request.form)
    for note in current_user.notifications['sent']:
        sent.append(storage.get("Notification", note))
    for note in current_user.notifications['received']:
        received.append(storage.get("Notification", note))
    return render_template('notifications.html', tripform=tripform, 
                            sent=sent, received=received)
