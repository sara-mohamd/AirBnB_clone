#!/usr/bin/python3
"""
    this module provides us with all comman
    attrs and methods
"""
import cmd
from uuid import uuid4
import datetime as dt


class BaseModel(cmd.Cmd):
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self):
        """ Base Constructor """
        self.id = str(uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """return object info"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
