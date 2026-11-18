"""
Day Challenge: Bank Account & Transaction Engine (OOP)
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Tuple
import uuid


class InsufficientFundsError(Exception):
    """Raised when an account does not have enough balance for a withdrawal."""
    pass


class InvalidAmountError(Exception):
    """Raised when a deposit or withdrawal amount is <= 0."""
    pass


@dataclass(frozen=True)
class Transaction:
    """Immutable record of an account transaction."""
    transaction_id: str
    amount: float
    transaction_type: str  # "DEPOSIT" | "WITHDRAWAL"
    timestamp: datetime
    description: str


class BankAccount:
    """Encapsulated bank account supporting deposits, withdrawals, and transfers."""

    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = float(initial_balance)
        self._transactions: List[Transaction] = []

        if initial_balance > 0:
            self._transactions.append(
                Transaction(
                    transaction_id=str(uuid.uuid4())[:8],
                    amount=initial_balance,
                    transaction_type="DEPOSIT",
                    timestamp=datetime.now(),
                    description="Initial Deposit"
                )
            )

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def owner_name(self) -> str:
        return self._owner_name

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float, description: str = "Deposit") -> Transaction:
        # TODO: Validate amount > 0 (raise InvalidAmountError)
        # TODO: Increase balance, create Transaction, append to history, and return it
        raise NotImplementedError("TODO: Implement deposit")

    def withdraw(self, amount: float, description: str = "Withdrawal") -> Transaction:
        # TODO: Validate amount > 0 (raise InvalidAmountError)
        # TODO: Validate balance >= amount (raise InsufficientFundsError)
        # TODO: Decrease balance, create Transaction, append to history, and return it
        raise NotImplementedError("TODO: Implement withdraw")

    def transfer(self, target_account: "BankAccount", amount: float, description: str = "Transfer") -> Tuple[Transaction, Transaction]:
        # TODO: Perform atomic transfer: withdraw from self and deposit into target_account
        # TODO: Return tuple of (withdrawal_tx, deposit_tx)
        raise NotImplementedError("TODO: Implement transfer")

    def get_statement(self) -> List[Transaction]:
        return list(self._transactions)

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index: int) -> Transaction:
        return self._transactions[index]

    def __repr__(self) -> str:
        return f"BankAccount(account_number={self._account_number!r}, owner={self._owner_name!r}, balance={self._balance:.2f})"
