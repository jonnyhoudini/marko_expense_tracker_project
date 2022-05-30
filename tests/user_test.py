import unittest

from models.user import *

class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User("Theodore Templeton")

    def test_user_has_name(self):
        self.assertEqual("Theodore Templeton", self.user.name)

    def test_user_limit_can_be_changed(self):
        self.user.change_limit(1500)
        self.assertEqual(1500, self.user.limit)

