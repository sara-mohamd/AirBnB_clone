#!/usr/bin/python3
"""
this module provides us with all comman
atts and methods in project classes
"""
import cmd
from uuid import uuid4
import datetime as dt
import models


class BaseModel(cmd.Cmd):
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Class Constructor"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            models.storage.new(self)
        else:

            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, dt.datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Return string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = dt.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        - method that generate a dictionary representation of an instance
        - use it to Create an instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
