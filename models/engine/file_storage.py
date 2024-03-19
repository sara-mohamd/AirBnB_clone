#!/usr/bin/python3
"""
- Save created objs.
- Convert these objs to a JSON string.
"""
import json


class FileStorage:
    """"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        - sets in __objects the obj with key <obj class name>.id
        - {<obj class name>.id : id}
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to file.json"""
        objs = {}
        for key, value in self.__objects.items():
            objs[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objs, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except Exception as e:
            pass
