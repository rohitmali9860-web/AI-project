# Day 002: Bank Account & Transaction Engine (OOP)

- **Date:** 2026-08-16
- **Category:** OOP Practice
- **Difficulty:** Intermediate

---

# Bank Account & Transaction Engine (OOP)

## Background
Build a robust, object-oriented financial ledger that encapsulates account state, records immutable transactions, supports deposits/withdrawals/transfers, and implements Python dunder methods (`__len__`, `__getitem__`, `__repr__`).

## Requirements
Implement the classes in `solution.py`:
1. `class InsufficientFundsError(Exception)`: Custom exception for failed debits.
2. `class InvalidAmountError(Exception)`: Custom exception for zero/negative amounts.
3. `class Transaction(NamedTuple or Dataclass)`:
   - Fields: `transaction_id: str`, `amount: float`, `transaction_type: str` ('DEPOSIT' or 'WITHDRAWAL'), `timestamp: datetime`, `description: str`.
4. `class BankAccount`:
   - `__init__(account_number: str, owner_name: str, initial_balance: float = 0.0)`
   - Properties: `account_number`, `owner_name`, `balance` (read-only property).
   - Methods:
     - `deposit(amount: float, description: str = "") -> Transaction`: Adds funds, records transaction. Raises `InvalidAmountError` if `amount <= 0`.
     - `withdraw(amount: float, description: str = "") -> Transaction`: Deducts funds, records transaction. Raises `InvalidAmountError` if `amount <= 0`, or `InsufficientFundsError` if `amount > balance`.
     - `transfer(target_account: BankAccount, amount: float, description: str = "") -> tuple[Transaction, Transaction]`: Atomic transfer between accounts.
     - `get_statement() -> list[Transaction]`: Returns a copy of transaction history.
   - Dunder methods:
     - `__len__`: Returns the number of transactions.
     - `__getitem__(index)`: Returns the transaction at the given index.
     - `__repr__`: e.g. `BankAccount(account_number='ACC123', owner='Rohit', balance=500.00)`

## Run Tests
```bash
python test_solution.py
```
