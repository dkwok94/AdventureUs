#!/usr/bin/python3
'''
DBStorage schema using SQLAlchemy and MySQL
'''
import pymongo
from pymongo import MongoClient
from models.base_model import BaseModel
import models
from models.city import City
from models.country import Country
from models.trip import Trip
from models.user import User
from models.notification import Notification


class DBStorage:
    '''
    Main database storage class
    '''

    __collection = None

    def __init__(self):
        '''
            Instantiation of a database storage class
        '''
        self.client = MongoClient('localhost', 27017)

    def all(self, cls=None):
        '''
            Queries database for specified classes

            Parameters:
                cls (object): the class to query

            Return:
                a dictionary of objects of the corresponding cls
        '''
        to_query = []
        new_dict = {}
        results = []
        if cls is not None:
            '''Set the database collection to query'''
            self.new(cls)

            '''Queries the database collection for __class__ equivalency
               If there are matches, it loops and appends to results array'''
            for dic in self.__collection.find({"__class__": cls.__name__}):
                results.append(models.classes[cls.__name__](**dic))
            for row in results:
                key = row.__class__.__name__ + '.' + row.id
                new_dict[key] = row
        else:
            for key, value in models.classes.items():
                try:
                    '''Sets the database collection to query'''
                    self.new(value)

                    '''If the query returns something, the class is appended
                       to an array'''
                    if self.__collection.find_one({"__class__": key}):
                        to_query.append(models.classes[key])
                except BaseException:
                    continue
            for classes in to_query:
                '''Set the database collection to query'''
                self.new(classes)

                '''For every object with the classname associated with the collection
                   append to the results array'''
                for dic in self.__collection.find({"__class__": classes.__name__}):
                    results.append(models.classes[classes.__name__](**dic))
                for row in results:
                    key = row.__class__.__name__ + '.' + row.id
                    new_dict[key] = row
        return new_dict

    def new(self, obj):
        '''
            Sets the MongoDB collection to the corresponding object

            Parameters:
                obj (object): the object to refer to for database table/collection
        '''
        self.__collection = eval("self.client.AdventureUs.{}".format(obj.collection))

    def save(self, obj):
        '''
            Saves an object to the JSON database
        '''
        self.__collection.insert_one(obj.to_dict())

    def delete(self, obj=None):
        '''
            Deletes a specified object from the database

            Parameters:
                obj (object): the object to delete
        '''

    def reload(self):
        '''
            Restarts the database engine session
        '''

    def close(self):
        '''
            Closes the current session and destroys it
        '''
