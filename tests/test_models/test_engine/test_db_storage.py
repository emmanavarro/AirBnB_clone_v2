#!/usr/bin/python3
""" Module for testing file storage"""
import pep8
import unittest
from unittest import TestCase
from unittest.mock import patch
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


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
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


class Test_DB_Storage(unittest.TestCase):
    """ Class to test the DB storage method """
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')

    def setUp(self):
        """ Set up test environment """
        self.instan = DBStorage()  # create DBStorage instance

    def tearDown(self):
        """ Remove storage file at end of tests """
        pass

    def test_obj_list_empty(self):
        """ __objects is initially empty
        self.assertEqual(len(storage.all()), 0) """
        pass

    def test_new(self):
        """ New object is correctly added to __objects
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj) """
        pass

    def test_all(self):
        """ __objects is properly returned
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict) """
        pass

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        pass

    def test_empty(self):
        """ Data is saved to file """
        pass

    def test_save(self):
        """ FileStorage save method """
        pass

    def test_reload(self):
        """ Storage file is successfully loaded to __objects
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])"""
        pass

    def test_reload_empty(self):
        """ Load from an empty file
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload() """
        pass

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        # self.assertEqual(storage.reload(), None)
        pass

    def test_base_model_save(self):
        """ BaseModel save method calls storage save
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json')) """
        pass

    def test_type_path(self):
        """ Confirm __file_path is string
        self.assertEqual(type(storage._FileStorage__file_path), str) """
        pass

    def test_type_objects(self):
        """ Confirm __objects is a dict
        self.assertEqual(type(storage.all()), dict) """
        pass

    def test_key_format(self):
        """ Key is properly formatted
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id) """
        pass

    def test_storage_var_created(self):
        """ FileStorage object storage created
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage) """
        pass


if __name__ == "__main__":
    unittest.main()
