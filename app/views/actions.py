#!/usr/bin/python3
'''
    Creation, Updating, Deleting functions from Flask application
'''
import models
from models import storage
from app import application
from flask import render_template, flash, redirect, url_for, request, session
from flask import jsonify, abort
from app.forms import CreateTrip
from flask_login import current_user, login_required


# Getter Functions for Dynamic Loading

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

@application.route('/users/<username>', methods=["GET"])
@login_required
def get_user_profile(username):
    if username == current_user.username:
        return redirect(url_for('display_profile'))
    hosted_trips = []
    active_trips = []
    user = storage.get_user(username)
    if user:
        for trip in user.hosted_trips:
            hosted_trips.append(storage.get("Trip", trip))
        for trip in user.active_trips:
            active_trips.append(storage.get("Trip", trip))
        session['url'] = url_for('get_user_profile', username=username)
        tripform = CreateTrip(request.form)
        return render_template('user_profile.html', user=user,
                                hosted_trips=hosted_trips,
                                active_trips=active_trips,
                                tripform=tripform)
    else:
        abort(404)

#######################################################################

# Object Creation Functions

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

            # Check if user has already joined the selected trip
            if current_user.username in trip.users:
                return jsonify({"response": "Already part of this trip"})

            # Send a request to the host that current user wants to join
            note.sender = current_user.username
            note.recipient = trip.host
            note.trip_id = trip_id
            note.purpose = "Join"
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

@application.route('/friend_request/<username>', methods=["GET"])
@login_required
def send_friend_request(username):
    note = models.Notification()
    note.sender = current_user.username
    note.recipient = username
    note.purpose = "Friend"
    recipient = storage.get_user(username)
    if recipient:
        for note in current_user.notifications['sent']:
            if note.purpose == "Friend" and note.sender == current_user.username \
                    and note.recipient == recipient.username:
                        return jsonify({"response": "Friend request pending.."})
            if recipient.username in current_user.friends:
                return jsonify({"response": "Already friends"})
        current_user.notifications['sent'].append(note.id)
        recipient.notifications['received'].append(note.id)
        storage.save(note)
        storage.save(recipient)
        storage.save(current_user)
    else:
        abort(404)

#######################################################################

# Object Deletion Functions

@application.route('/delete_trip/<tripid>', methods=["DELETE"])
@login_required
def delete_trip(tripid):
    trip = storage.get("Trip", tripid)
    if trip:
        for user in trip.users:
            person = storage.get_user(user)
            if person.username == trip.host:
                person.hosted_trips.remove(tripid)
            else:
                person.active_trips.remove(tripid)
            storage.save(person)
        storage.delete(trip)
        return jsonify(dict(redirect=url_for('display_profile')))
    else:
        abort(404)

#######################################################################

# Notification Accept/Reject Functions

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
