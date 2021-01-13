import unittest
from utils.bank import Bank


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank(2)

    def test_create_account(self):
        self.bank.create_account()
        self.assertEqual(1, self.bank.ACCOUNTS[0].get('id'))
        self.assertEqual(2, self.bank.ACCOUNTS[1].get('id'))
        self.assertNotEqual(1, self.bank.ACCOUNTS[1].get('id'))

    def test_deposit_amount(self):
        self.bank.deposit_amount(2000)
        self.assertEqual(2000, self.bank.ACCOUNTS[1].get('amount'))
        self.bank.deposit_amount(1000)
        self.assertEqual(3000, self.bank.ACCOUNTS[1].get('amount'))
        self.assertNotEqual(2000, self.bank.ACCOUNTS[1].get('amount'))

    def test_withdraw_amount(self):
        self.bank.withdraw_amount(1000)
        self.assertEqual(2000, self.bank.ACCOUNTS[1].get('amount'))
        self.bank.withdraw_amount(500)
        self.assertEqual(1500, self.bank.ACCOUNTS[1].get('amount'))
        self.assertNotEqual(2000, self.bank.ACCOUNTS[1].get('amount'))


if __name__ == '__main__':
    unittest.main()
