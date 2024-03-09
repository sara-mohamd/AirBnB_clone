#!/usr/bin/python3
"""
- Save created objs in a file
-  convert the dictionary representation to a JSON string
"""
import json


class FileStorage:
    """"""
    __file_path = '' 
    __objects = {}

    @property
    def all(self):

        return self.__objects

    def new(self, obj):

        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        ...

    def reload(self):
        ...