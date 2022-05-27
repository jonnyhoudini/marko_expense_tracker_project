import unittest

from models.payee import *

class PayeeTest(unittest.TestCase):

    def setUp(self):
        self.payee1 = Payee("La Vita")
    
    def test_payee_has_name(self):
        self.assertEqual("La Vita", self.payee1.name)

    def test_payee_has_no_ID(self):
        self.assertEqual(None, self.payee1.id)