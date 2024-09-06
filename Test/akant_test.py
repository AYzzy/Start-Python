from unittest import TestCase

from understanding_class import Akant

class AkantTest(TestCase):
    def test_that_account_can_deposit(self):
        a1 = Akant("Stanley", "0000")
        a1.deposit(5000)
        self.assertEqual(a1.balance, 5000)

    def test_that_account_cannot_deposit_negative_number(self):
        a1 = Akant("Stanley", "0000")
        self.assertRaises(ValueError, a1.deposit(-5000))

