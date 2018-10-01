#!/usr/bin/python3
'''
    Error handler routes
''' 
import models
from models import storage
from app import application
from flask import jsonify

@application.errorhandler(404)
def not_found(message):
    '''
        Handles 404 status codes

        Parameters:
            message [str]: a custom message to display
        Returns:
            The HTTP response for the request
    '''
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response
