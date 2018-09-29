#!/usr/bin/python3
'''
    JSON Encoder definition
'''

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    '''
        Helps to encode non-serializable attributes
    '''
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, o)
