#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from models.review import Review
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(60),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # DBStorage
        reviews = relationship("Review",
                               backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        # FileStorage
        @property
        def reviews(self):
            """   returns the list of Review instances """
            all_revi = models.storage.all(Review)
            list_revi = []
            for key, value in all_revi.items():
                if self.id == value.place_id:
                    list_revi.append(value)
            return list_revi

        @property
        def amenities(self):
            """ Returns the list of Amenity instances
            all_amen = models.storage.all(Amenity)
            list_amen = []
            for key, value in all_amen.items():
                if self.amenity_ids == value.id:
                    list_amen.append(value)
            return list_amen """
        return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ Adds the ids of Amenity """
            if 'Amenity' == type(obj).__name__:
                self.amenity_ids.append(obj.id)
