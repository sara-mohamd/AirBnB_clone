#!/usr/bin/python3
"""Test base_model file"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """test class of base_model"""

    @classmethod
    def setUpClass(cls) -> None:
        print('class starts'.center(20, '.'))

    """
    test datatype of different objs
    """

    my_model = BaseModel()
    my_model.name = 'base_model'
    my_model.my_number = 89

    def test_instance_creation_without_kwargs(self):
        """check obj created without kwargs"""

        # created, update, my_model, id, my_number, name
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertEqual(self.my_model.name, 'base_model')
        self.assertEqual(self.my_model.my_number, 89)

    my_model_dict = my_model.to_dict()
    my_new_model = BaseModel(**my_model_dict)

    def test_instance_creation_using_kwargs(self):
        """check obj created using kwargs"""
        self.assertIsInstance(self.my_new_model, BaseModel)
        self.assertIsInstance(self.my_new_model.id, str)
        self.assertIsInstance(self.my_new_model.created_at, datetime)
        self.assertIsInstance(self.my_new_model.updated_at, datetime)
        self.assertEqual(self.my_new_model.name, 'base_model')
        self.assertEqual(self.my_model.my_number, 89)

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.my_model.to_dict()
        expected_dic = self.my_model.__dict__.copy()
        expected_dic["__class__"] = self.my_model.__class__.__name__
        expected_dic["updated_at"] = self.my_model.updated_at.isoformat()
        expected_dic["created_at"] = self.my_model.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """
            test save class method
        """
        before_update = self.my_model.updated_at
        self.my_model.my_number = 90
        self.my_model.save()
        after_update = self.my_model.updated_at
        self.assertNotEqual(before_update, after_update)
