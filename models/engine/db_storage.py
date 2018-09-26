#!/usr/bin/python3
'''
DBStorage schema using SQLAlchemy and MySQL
'''
import pymongo
from pymongo import MongoClient
from models.base_model import BaseModel
import models


class DBStorage:
    '''
    Main database storage class
    '''

    __collection = None
    __client = None

    def __init__(self):
        '''
            Instantiation of a database storage class
        '''
        self.__client = MongoClient('localhost', 27017)

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
            # Set the database collection to query
            self.new(cls)

            # Queries the database collection for __class__ equivalency.
            # If there are matches, it loops and appends to results array.
            for dic in self.__collection.find({"__class__": cls.__name__}):
                results.append(models.classes[cls.__name__](**dic))
            for row in results:
                key = row.__class__.__name__ + '.' + row.id
                new_dict[key] = row
        else:
            for key, value in models.classes.items():
                try:
                    # Sets the database collection to query
                    self.new(value)

                    # If the query returns something, the class is
                    # appended to an array
                    if self.__collection.find_one({"__class__": key}):
                        to_query.append(models.classes[key])
                except BaseException:
                    continue

            for classes in to_query:
                # Set the database collection to query
                self.new(classes)

                # For every object with the classname associated with the
                # collection, append to the results array
                for dic in self.__collection.find(
                        {"__class__": classes.__name__}):
                    results.append(models.classes[classes.__name__](**dic))
                for row in results:
                    key = row.__class__.__name__ + '.' + row.id
                    new_dict[key] = row
        return new_dict

    def new(self, obj):
        '''
            Sets the MongoDB collection

            Parameters:
                obj (object): the object to refer to for database
                table/collection
        '''
        self.__collection = eval("self._DBStorage__client.AdventureUs.{}"
                                 .format(obj.collection), {"__builtins__": {}},
                                 {'self': self})

    def save(self, obj):
        '''
            Saves an object to MongoDB or updates it if it exists
        '''
        self.new(obj)

        # Checks if the MongoDB _id is present:
        # if not, the object is not in the database
        if hasattr(obj, "_id"):
            self.__collection.update_one({"id": obj.id},
                                         {"$set": obj.to_dict()})

        else:
            self.__collection.insert_one(obj.to_dict())

    def delete(self, obj=None):
        '''
            Deletes a specified object from the database

            Parameters:
                obj (object): the object to delete
        '''
        self.new(obj)
        self.__collection.delete_one({"id": obj.id})

    def reload(self):
        '''
            Restarts the database engine session
        '''

    def get(self, cls, id):
        '''
            Gets a single instance of a particular object based on id and class

            Parameters:
                cls (string): the class of the object to get
                id (string): the id of the object to get
        '''
        if cls not in models.classes.keys():
            return None
        self.new(models.classes[cls])
        obj = self.__collection.find_one({"id": id})
        if obj is None:
            return None
        return models.classes[cls](**obj)

    def get_user(self, username):
        '''
            Gets a single instance of a user based on username

            Parameters:
                username (string): the username to pull from the database
        '''
        self.new(models.User)
        obj = self.__collection.find_one({"username": username})
        if obj is None:
            return None
        return models.User(**obj)

    def count(self, cls=None):
        '''
            Counts the number of a specific class in storage or all objects
            if cls variable is None

            Parameters:
                cls (string): the class of the objects to count
        '''
        count_dict = {}
        if cls is None:
            count_dict = self.all()
        else:
            if cls in models.classes.keys():
                count_dict = self.all(models.classes[cls])
        return len(count_dict)
