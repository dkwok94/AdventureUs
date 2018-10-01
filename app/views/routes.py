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

# Login-Logout view functions
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

# Display view functions
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
    return render_template('profile.html', tripform=tripform,
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


@application.route('/trip_roster', methods=["GET", "POST"])
@login_required
def trip_roster():
    '''
        Populates the modal footer with all users on a specific trip
    '''
    users = []
    if request.method == "POST":
        content = request.get_json()
        print(content)
        for user in content['users']:
            user_obj = storage.get_user(user)
            if user_obj:
                users.append(user_obj.to_dict_mongoid())
            else:
                abort(404)
        if users:
            return jsonify(users)
        else:
            abort(404)

@application.route('/get_trip/<trip_id>', methods=["GET"])
@login_required
def get_trip(trip_id):
    '''
        Grabs a specific trip from the database based on the trip ID to be
        used for dynamic AJAX updates on modals
    '''
    trip = storage.get("Trip", trip_id)
    if trip:
        return jsonify(trip.to_dict_mongoid())
    else:
        abort(404)

@application.route('/get_sender/<notification_id>', methods=["GET"])
@login_required
def get_sender(notification_id):
    '''
        Grabs the notification sender user from the database in order
        to dynamically update the message modal
    '''
    note = storage.get("Notification", notification_id)
    if note:
        user = storage.get_user(note.sender)
        if user:
            return jsonify(user.to_dict_mongoid())
        else:
            abort(404)

@application.route('/createtrip', methods=["GET", "POST"])
@login_required
def create_trip():
    '''
        Creates a new trip object in the database
    '''
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

# Send Notifications
@application.route('/send_notification/<trip_id>', methods=["POST"])
@login_required
def send_notification(trip_id):
    '''
        Sends a notification to a trip host and saves the notification
        to the user's sent notifications and the host's received notifications
    '''
    note = models.Notification()
    trip = storage.get("Trip", trip_id)
    if trip:
        trip_host = storage.get_user(trip.host)
        if trip_host:

            # Check if user is trying to join his/her own trip
            if trip_host.username == current_user.username:
                return jsonify({"response": "Can't request own trip..."})

            # Check if user has already a sent a request for this trip
            for notification in current_user.notifications['sent']:
                sent = storage.get("Notification", notification)
                if sent.trip_id == trip_id:
                    print("Already sent")
                    return jsonify({"response": "Request already sent..."})

            # Send a request to the host that current user wants to join
            note.sender = current_user.username
            note.recipient = trip.host
            note.trip_id = trip_id
            note.trip_info = {"country": trip.country, "city": trip.city, "date_range": trip.date_range}
            current_user.notifications['sent'].append(note.id)
            trip_host.notifications['received'].append(note.id)
            storage.save(note)
            storage.save(current_user)
            storage.save(trip_host)
            print("Success")
            return jsonify({"response": "Successfully Sent!"})
        else:
            abort(404)
    else:
        abort(404)

@application.route('/notification/<noteid>/accepted_request/<tripid>')
@login_required
def accept_request(noteid, tripid):
    '''
        The sequence of events that occur after the host of a trip
        accepts another user's request to join their trip
    '''
    trip = storage.get("Trip", tripid)
    if trip:
        note = storage.get("Notification", noteid)
        if note:
            user = storage.get_user(note.sender)
            host = storage.get_user(note.recipient)
            if user and host:
                trip.users.append(user.username)
                user.active_trips.append(trip.id)
                user.notifications['approved'].append(note.id)
                user.notifications['sent'].remove(note.id)
                host.notifications['received'].remove(note.id)
                storage.save(trip)
                storage.save(user)
                storage.save(host)
                return jsonify(dict(redirect=url_for('display_notifications')))
            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)

@application.route('/notification/<noteid>/rejected_request')
@login_required
def reject_request(noteid):
    '''
        The sequence of events that occur after the host of a trip
        rejects another user's request to join their trip
    '''
    note = storage.get("Notification", noteid)
    if note:
        user = storage.get_user(note.sender)
        host = storage.get_user(note.recipient)
        if user and host:
            print(user.notifications)
            print(host.notifications)
            user.notifications['rejected'].append(note.id)
            user.notifications['sent'].remove(note.id)
            host.notifications['received'].remove(note.id)
            print(user.notifications)
            print(host.notifications)
            storage.save(user)
            storage.save(host)
            return jsonify(dict(redirect=url_for('display_notifications')))
        else:
            abort(404)
    else:
        abort(404)
