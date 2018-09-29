#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            try:
                # Converts a datetime string in template format to datetime
                # object
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            except KeyError:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save(self)

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__

        # Converts a datetime object into a string of a specific template
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cp_dct)

    def to_dict_mongoid(self):
        '''
            Returns dictionary representation of BaseModel class
            taking into account the MongoDB _id attribute is not
            allowed to change.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__

        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        
        # Excludes the _id attribute that MongoDB appends to the object
        # to avoid update errors when saving to the database
        del cp_dct['_id']
        return (cp_dct)
