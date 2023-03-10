#!/usr/bin/python3

"""City class"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Subclass of BaseModel class
    Public class attribute:
        state_id: (str)
        name: (str)
    """
    state_id = ""
    name = ""