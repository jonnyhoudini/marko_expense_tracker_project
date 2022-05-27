import unittest

from models.category import *

class CategoryTest(unittest.TestCase):
    def setUp(self):
        self.category1 = Category("Food")

    def test_category_has_name(self):
        self.assertEqual("Food", self.category1.name)

    def test_category_has_no_id(self):
        self.assertEqual(None, self.category1.id)