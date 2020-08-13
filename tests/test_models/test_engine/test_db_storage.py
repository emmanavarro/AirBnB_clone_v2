#!/usr/bin/python3
""" Module for testing DB storage"""
import pep8
import unittest
from unittest import TestCase
from unittest.mock import patch
import models
from models.engine import db_storage
from models.__init__ import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
import os
import sys
import MySQLdb
from io import StringIO


class Test_DB_Storage(unittest.TestCase):
    """ Class to test the DB storage method """
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8(self):
        """
        * Test pep8 style validation
        * Test base and test_base for pep8 conformance
        """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(db_storage.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(DBStorage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(DBStorage):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
