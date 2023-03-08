#!/usr/bin/python3
import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """
    Parent class for AIRBNB clone
    """

    def __init__(self, *args, **kwargs):
        """Initialization of attributes"""
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns class name, id, dictionary"""
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Saves the object
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary"""
        dicts = self.__dict__.copy()
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        dicts["__class__"] = self.__class__.__name__
        return dicts