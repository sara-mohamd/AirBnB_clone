#!/usr/bin/python3
"""
- Save created objs in a file
-  convert the dictionary representation to a JSON string
"""
import json


class FileStorage:
    """"""
    __file_path = 'file.json'
    __objects = {}

    @property
    def all(self):

        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except Exception as e:
            pass
