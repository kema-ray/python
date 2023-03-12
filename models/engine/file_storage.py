#!/usr/bin/python3
"""File storage for airBnB clone project"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """Storage Engine for AirBnB clone project"""
    __file_path = 'file.json'
    __objects = {}
    class_dicts = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity, 
                   "City":City, "Place": Place, "Review": Review, "State": State}

    def all(self):
        """Return dictionary of <class>.<id> :object instance"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__,obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        object_dict = {}
        for key, obj in self.__objects.items():
            object_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_object_dict = json.load(f)
            for key, value in new_object_dict.items():
                objs = self.class_dicts[value['__class__']](**value)
                self.__objects[key] = objs
        except FileNotFoundError:
            pass
