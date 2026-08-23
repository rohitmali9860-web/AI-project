import unittest
from solution import BankAccount, InsufficientFundsError, InvalidAmountError, Transaction


class TestBankAccountSystem(unittest.TestCase):
    def setUp(self):
        self.acc1 = BankAccount("ACC-001", "Rohit", 1000.0)
        self.acc2 = BankAccount("ACC-002", "Alex", 200.0)

    def test_deposit(self):
        tx = self.acc1.deposit(500.0, "Salary")
        self.assertEqual(self.acc1.balance, 1500.0)
        self.assertEqual(tx.amount, 500.0)
        self.assertEqual(tx.transaction_type, "DEPOSIT")

    def test_withdraw_success(self):
        tx = self.acc1.withdraw(300.0, "ATM")
        self.assertEqual(self.acc1.balance, 700.0)
        self.assertEqual(tx.amount, 300.0)
        self.assertEqual(tx.transaction_type, "WITHDRAWAL")

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.acc1.withdraw(2000.0)

    def test_invalid_amount_errors(self):
        with self.assertRaises(InvalidAmountError):
            self.acc1.deposit(-50.0)
        with self.assertRaises(InvalidAmountError):
            self.acc1.withdraw(0.0)

    def test_transfer(self):
        tx_out, tx_in = self.acc1.transfer(self.acc2, 400.0, "Rent share")
        self.assertEqual(self.acc1.balance, 600.0)
        self.assertEqual(self.acc2.balance, 600.0)
        self.assertEqual(tx_out.transaction_type, "WITHDRAWAL")
        self.assertEqual(tx_in.transaction_type, "DEPOSIT")

    def test_dunder_methods(self):
        self.acc1.deposit(100.0)
        self.acc1.withdraw(50.0)
        # 1 initial deposit + 2 transactions = 3
        self.assertEqual(len(self.acc1), 3)
        self.assertIsInstance(self.acc1[0], Transaction)
        self.assertIn("ACC-001", repr(self.acc1))


if __name__ == "__main__":
    unittest.main()
