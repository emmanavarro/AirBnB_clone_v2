#!/usr/bin/python3
""" Module for testing DB storage"""
import os
import sys
import pep8
import models
import MySQLdb
import unittest
from io import StringIO
from unittest.mock import patch
from models.__init__ import storage
from models.engine import db_storage
from models.engine.db_storage import DBStorage


class Test_DB_Storage(unittest.TestCase):
    """ Class to test the DB storage method """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     'environment = db')
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

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     'environment = db')
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(db_storage.__doc__) > 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     'environment = db')
    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(DBStorage.__doc__) > 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     'environment = db')
    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(DBStorage):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
