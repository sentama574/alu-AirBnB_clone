#!/usr/bin/python3
"""The base model class which is going to act as a parent"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Start of the Base model class"""

    def __init__(self, *args, **kwargs):
        """Base model constructor taking args and kwargs"""
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """updates the UPDATED_AT instance"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Returns the string representation"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
