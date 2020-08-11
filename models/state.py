#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    cities = relationship('City', backref='state', cascade="all, delete")
    # else:
    @property
    def cities(self):
        """Returns cities"""
        from models import storage
        
        all_cities = storage.all(City)
        list_cities = []
        for key, value in all_cities.items():
            if self.id == value.state_id:
                list_cities.append(value)
        return list_cities
