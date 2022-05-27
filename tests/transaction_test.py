import unittest

from models.transaction import *
from models.category import *
from models.payee import *

class TransactionTest(unittest.TestCase):

    def setUp(self):
        self.payee1 = Payee("La Vita")
        self.category1 = Category("Food")
        self.transaction = Transaction("Lunch with client", 45.90, self.payee1, "27 May 2022", self.category1)

    def test_transaction_has_name(self):
        self.assertEqual("Lunch with client", self.transaction.description)

    def test_transaction_has_amount(self):
        self.assertEqual(45.90, self.transaction.amount)

    def test_transaction_be_marked_as_submitted(self):
        self.transaction.mark_submitted()
        self.assertEqual(True, self.transaction.submitted)

    def test_transaction_has_category_object(self):
        self.assertEqual("Food", self.transaction.category.name)

    def test_transaction_has_payee_object(self):
        self.assertEqual("La Vita", self.transaction.payee.name)