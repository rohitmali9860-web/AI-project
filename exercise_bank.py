"""
exercise_bank.py
Curated repository of Python exercises across:
- Java/Python OOP practice
- GS1 / Barcode utilities
- Flask mini-features
- File & Data handling
- Algorithms & Data structures

Each exercise provides:
1. Problem specification & requirements (README.md)
2. Starter scaffold with type hints & TODO markers (solution.py)
3. Ready-to-run unit test suite (test_solution.py)
"""

EXERCISES = [
    # =========================================================================
    # 1. GS1 / Barcode Utilities: EAN-13 & UPC-A Check Digit
    # =========================================================================
    {
        "id": "gs1-ean13-check-digit",
        "title": "EAN-13 & UPC-A Check Digit Calculator",
        "category": "GS1 / Barcode Utilities",
        "difficulty": "Beginner",
        "readme": """# EAN-13 & UPC-A Check Digit Calculator

## Background
The GS1 standard specifies a Modulo-10 check digit algorithm for GTIN barcodes (EAN-13, UPC-A, ITF-14, SSCC).
The check digit is the final digit in the barcode, calculated using alternating weightings of 1 and 3.

## Requirements
Implement the functions in `solution.py`:
1. `calculate_check_digit(digits: str) -> int`:
   - Takes a string of digits (e.g. 12 digits for EAN-13 or 11 digits for UPC-A).
   - From right to left (excluding check digit position), weights alternate between 3 and 1 (i.e. position 1 from right * 3, position 2 * 1, position 3 * 3, etc.).
   - Sum the products, find the remainder modulo 10.
   - Check digit is `(10 - remainder) % 10`.
   - Raises `ValueError` if `digits` contains non-numeric characters or is empty.

2. `validate_barcode(barcode: str, expected_length: int = 13) -> bool`:
   - Validates that `barcode` is exactly `expected_length` numeric digits.
   - Verifies that the last digit matches the calculated check digit of the preceding digits.
   - Returns `True` if valid, `False` otherwise.

## Examples
- `calculate_check_digit("400638133393")` -> `1` (Full EAN-13: `4006381333931`)
- `calculate_check_digit("01234567890")` -> `5` (Full UPC-A: `012345678905`)
- `validate_barcode("4006381333931", 13)` -> `True`
- `validate_barcode("4006381333932", 13)` -> `False`

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: EAN-13 & UPC-A Check Digit Calculator
"""
import re


def calculate_check_digit(digits: str) -> int:
    """
    Calculate GS1 Modulo-10 check digit for a given sequence of numeric digits.
    
    Weights from right to left alternate 3, 1, 3, 1...
    Check digit = (10 - (sum % 10)) % 10
    
    Args:
        digits: String containing only numeric digits (e.g. 12 digits for EAN-13).
        
    Returns:
        int: Single calculated check digit (0-9).
        
    Raises:
        ValueError: If digits is empty or contains non-numeric characters.
    """
    # TODO: Validate input string (must be non-empty digits)
    # TODO: Calculate weighted sum from right to left with weights 3, 1, 3, 1...
    # TODO: Compute and return (10 - (total_sum % 10)) % 10
    raise NotImplementedError("TODO: Implement calculate_check_digit")


def validate_barcode(barcode: str, expected_length: int = 13) -> bool:
    """
    Validate whether a full barcode has valid length and check digit.
    
    Args:
        barcode: Full barcode string including the check digit.
        expected_length: Expected character length (e.g. 13 for EAN-13, 12 for UPC-A).
        
    Returns:
        bool: True if valid, False otherwise.
    """
    # TODO: Check length and numeric validity
    # TODO: Compare barcode[-1] with calculate_check_digit(barcode[:-1])
    raise NotImplementedError("TODO: Implement validate_barcode")
''',
        "test_code": '''import unittest
from solution import calculate_check_digit, validate_barcode


class TestGS1CheckDigit(unittest.TestCase):
    def test_ean13_check_digit(self):
        # Known EAN-13: 4006381333931 (STABILO Point 88 pen)
        self.assertEqual(calculate_check_digit("400638133393"), 1)
        self.assertTrue(validate_barcode("4006381333931", 13))
        self.assertFalse(validate_barcode("4006381333932", 13))

    def test_upca_check_digit(self):
        # Known UPC-A: 012345678905
        self.assertEqual(calculate_check_digit("01234567890"), 5)
        self.assertTrue(validate_barcode("012345678905", 12))
        self.assertFalse(validate_barcode("012345678908", 12))

    def test_zero_remainder(self):
        # If remainder is 0, check digit should be 0 (not 10)
        # e.g., 978020137962 -> check digit 4 -> 9780201379624
        self.assertEqual(calculate_check_digit("978020137962"), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_check_digit("")
        with self.assertRaises(ValueError):
            calculate_check_digit("1234A567")
        self.assertFalse(validate_barcode("12345", 13))
        self.assertFalse(validate_barcode("123456789012A", 13))


if __name__ == "__main__":
    unittest.main()
'''
    },

    # =========================================================================
    # 2. OOP Practice: Bank Account & Immutable Transactions
    # =========================================================================
    {
        "id": "oop-bank-transaction-system",
        "title": "Bank Account & Transaction Engine (OOP)",
        "category": "OOP Practice",
        "difficulty": "Intermediate",
        "readme": """# Bank Account & Transaction Engine (OOP)

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
""",
        "solution_scaffold": '''"""
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
''',
        "test_code": '''import unittest
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
'''
    },

    # =========================================================================
    # 3. GS1 / Barcode: GS1 Application Identifier (AI) Parser
    # =========================================================================
    {
        "id": "gs1-ai-parser",
        "title": "GS1 Application Identifier (AI) Barcode Parser",
        "category": "GS1 / Barcode Utilities",
        "difficulty": "Intermediate",
        "readme": """# GS1 Application Identifier (AI) Barcode Parser

## Background
In supply chain and logistics, GS1-128 and GS1 DataMatrix barcodes encode multiple data elements prefixed by 2-4 digit Application Identifiers (AIs).
Common AIs include:
- `01`: Global Trade Item Number (GTIN-14) - Fixed 14 numeric digits.
- `10`: Batch / Lot Number - Variable up to 20 alphanumeric characters (ended by `<GS>` / `\\x1d` if not at end).
- `17`: Expiration Date (YYMMDD) - Fixed 6 numeric digits.
- `21`: Serial Number - Variable up to 20 alphanumeric characters.
- `310x`: Net weight in kg (where x is decimal point).

## Requirements
Implement `parse_gs1_string(raw_data: str) -> dict[str, str]` in `solution.py`:
1. Parse bracketed format: `(01)00012345678905(17)261231(10)LOT42(21)SER999`
2. Parse raw FNC1 / `<GS>` delimited format: `01000123456789051726123110LOT42\\x1d21SER999`
3. Return a clean dictionary mapping AI code to parsed value:
   ```python
   {
       "01": "00012345678905",
       "17": "261231",
       "10": "LOT42",
       "21": "SER999"
   }
   ```

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: GS1 Application Identifier (AI) Barcode Parser
"""
import re
from typing import Dict

# Common GS1 AI specifications: AI -> (length_type, fixed_length_or_max)
AI_SPECS = {
    "01": ("FIXED", 14),   # GTIN
    "10": ("VAR", 20),     # Batch / Lot
    "17": ("FIXED", 6),    # Expiration (YYMMDD)
    "21": ("VAR", 20),     # Serial
    "00": ("FIXED", 18),   # SSCC
    "30": ("VAR", 8),      # Count
}


def parse_gs1_string(raw_data: str) -> Dict[str, str]:
    """
    Parse a GS1 barcode data string into a dictionary of AI -> value.
    
    Supports:
    1. Human readable bracketed format: '(01)00012345678905(17)261231(10)BATCH1'
    2. Raw scanner format with FNC1 / group separators (\\x1d or <GS>):
       '01000123456789051726123110BATCH1\\x1d21SER123'
       
    Args:
        raw_data: Raw barcode string.
        
    Returns:
        Dict[str, str]: Dictionary mapping AI code strings to their values.
    """
    # TODO: Check if raw_data is bracketed format e.g. '(01)...(17)...'
    # TODO: If bracketed, extract AI and values using regex
    # TODO: If raw stream, iterate through AI prefixes, consume fixed length for fixed AIs,
    #       and consume up to group separator (\\x1d, <GS>) or max length for variable AIs
    # TODO: Return parsed key-value dictionary
    raise NotImplementedError("TODO: Implement parse_gs1_string")
''',
        "test_code": '''import unittest
from solution import parse_gs1_string


class TestGS1AIParser(unittest.TestCase):
    def test_bracketed_format(self):
        raw = "(01)00012345678905(17)261231(10)LOT42(21)SER999"
        result = parse_gs1_string(raw)
        self.assertEqual(result.get("01"), "00012345678905")
        self.assertEqual(result.get("17"), "261231")
        self.assertEqual(result.get("10"), "LOT42")
        self.assertEqual(result.get("21"), "SER999")

    def test_raw_stream_with_gs_separator(self):
        # AI 01 (fixed 14) + AI 17 (fixed 6) + AI 10 (var, ended with \\x1d) + AI 21 (var)
        raw = "01000123456789051726123110LOT42\\x1d21SER999"
        result = parse_gs1_string(raw)
        self.assertEqual(result.get("01"), "00012345678905")
        self.assertEqual(result.get("17"), "261231")
        self.assertEqual(result.get("10"), "LOT42")
        self.assertEqual(result.get("21"), "SER999")

    def test_empty_and_single_ai(self):
        self.assertEqual(parse_gs1_string(""), {})
        result = parse_gs1_string("(01)00012345678905")
        self.assertEqual(result, {"01": "00012345678905"})


if __name__ == "__main__":
    unittest.main()
'''
    },

    # =========================================================================
    # 4. Flask Mini-Features: Request Token Auth & Rate Limiter Decorators
    # =========================================================================
    {
        "id": "flask-auth-rate-limit-decorators",
        "title": "Flask Auth & Sliding-Window Rate Limiter Decorators",
        "category": "Flask Mini-Features",
        "difficulty": "Intermediate",
        "readme": """# Flask Auth & Sliding-Window Rate Limiter Decorators

## Background
In microservices and API development, route decorators are used to enforce authentication and rate limiting without bloating route logic.

## Requirements
Implement the decorators in `solution.py`:
1. `require_api_key(valid_keys: set[str])`:
   - Checks `request.headers.get("X-API-Key")` or `Authorization: Bearer <key>`.
   - If missing or invalid, returns `{"error": "Unauthorized", "message": "Invalid or missing API key"}`, status code `401`.
   - If valid, proceeds to execute the decorated route.

2. `RateLimiter(max_requests: int, window_seconds: int)`:
   - Thread-safe in-memory sliding window rate limiter tracking client IP (`request.remote_addr`).
   - If client exceeds `max_requests` within the last `window_seconds`, returns `{"error": "Too Many Requests", "retry_after": <seconds>}`, status code `429`.
   - Otherwise, records request timestamp and allows execution.

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: Flask Auth & Sliding-Window Rate Limiter Decorators
"""
from collections import defaultdict, deque
from functools import wraps
import time
from typing import Callable, Set
from flask import Flask, jsonify, request


def require_api_key(valid_keys: Set[str]) -> Callable:
    """
    Decorator that checks request headers for a valid API Key.
    
    Accepts:
    - Header: 'X-API-Key': '<key>'
    - Header: 'Authorization': 'Bearer <key>'
    
    Returns 401 JSON response if key is missing or invalid.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Extract key from X-API-Key header or Authorization: Bearer <key>
            # TODO: Check if key in valid_keys
            # TODO: If not valid, return jsonify({"error": "Unauthorized", "message": "Invalid or missing API key"}), 401
            # TODO: Otherwise call and return func(*args, **kwargs)
            raise NotImplementedError("TODO: Implement require_api_key wrapper")
        return wrapper
    return decorator


class RateLimiter:
    """Sliding-window rate limiter decorator tracking client IP."""

    def __init__(self, max_requests: int = 5, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.client_records = defaultdict(deque)

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Get client IP from request.remote_addr or fallback "127.0.0.1"
            # TODO: Clean up timestamps older than (current_time - window_seconds)
            # TODO: If len(records) >= max_requests, return jsonify({"error": "Too Many Requests"}), 429
            # TODO: Append current_time and call func(*args, **kwargs)
            raise NotImplementedError("TODO: Implement RateLimiter wrapper")
        return wrapper
''',
        "test_code": '''import unittest
from flask import Flask, jsonify
from solution import require_api_key, RateLimiter


class TestFlaskDecorators(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["TESTING"] = True
        self.valid_keys = {"secret-token-123", "prod-key-xyz"}

        @self.app.route("/secure-data")
        @require_api_key(self.valid_keys)
        def secure_data():
            return jsonify({"status": "success", "data": [1, 2, 3]}), 200

        limiter = RateLimiter(max_requests=2, window_seconds=10)

        @self.app.route("/limited-ping")
        @limiter
        def limited_ping():
            return jsonify({"pong": True}), 200

        self.client = self.app.test_client()

    def test_api_key_header_success(self):
        resp = self.client.get("/secure-data", headers={"X-API-Key": "secret-token-123"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json["status"], "success")

    def test_bearer_token_success(self):
        resp = self.client.get("/secure-data", headers={"Authorization": "Bearer prod-key-xyz"})
        self.assertEqual(resp.status_code, 200)

    def test_unauthorized_missing_and_wrong_key(self):
        resp1 = self.client.get("/secure-data")
        self.assertEqual(resp1.status_code, 401)
        resp2 = self.client.get("/secure-data", headers={"X-API-Key": "invalid-token"})
        self.assertEqual(resp2.status_code, 401)

    def test_rate_limiter_throttles(self):
        # 1st request -> OK
        r1 = self.client.get("/limited-ping")
        self.assertEqual(r1.status_code, 200)
        # 2nd request -> OK
        r2 = self.client.get("/limited-ping")
        self.assertEqual(r2.status_code, 200)
        # 3rd request -> 429 Too Many Requests
        r3 = self.client.get("/limited-ping")
        self.assertEqual(r3.status_code, 429)


if __name__ == "__main__":
    unittest.main()
'''
    },

    # =========================================================================
    # 5. File & Data Handling: Atomic Safe File Writer
    # =========================================================================
    {
        "id": "file-atomic-writer",
        "title": "Atomic Safe File Writer & Backup Manager",
        "category": "File & Data Handling",
        "difficulty": "Intermediate",
        "readme": """# Atomic Safe File Writer & Backup Manager

## Background
Directly writing to production files can cause corruption if power is lost or the process crashes mid-write.
Atomic writing creates a temporary sibling file and performs an OS-level atomic rename (`os.replace`) upon successful write.

## Requirements
Implement `atomic_write_file` and `AtomicFileWriter` context manager in `solution.py`:
1. `atomic_write_file(filepath: str, content: str, make_backup: bool = False, encoding: str = 'utf-8') -> None`:
   - Writes content to a temporary file in the same directory as `filepath`.
   - Flushes and syncs (`os.fsync`) to disk.
   - If `make_backup` is True and `filepath` already exists, creates a `.bak` backup copy.
   - Replaces the target file atomically using `os.replace`.
   - Ensures temporary files are cleaned up if an exception occurs.

2. `class AtomicFileWriter`:
   - Context manager syntax:
     ```python
     with AtomicFileWriter("data.json") as f:
         f.write('{"status": "ok"}')
     ```
   - Only commits file upon clean context exit; discards partial writes on error.

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: Atomic Safe File Writer & Backup Manager
"""
import os
import shutil
import tempfile
from typing import Optional


def atomic_write_file(
    filepath: str,
    content: str,
    make_backup: bool = False,
    encoding: str = "utf-8"
) -> None:
    """
    Safely write content to a file atomically via temp file replacement.
    
    Args:
        filepath: Destination file path.
        content: String content to write.
        make_backup: If True and file exists, saves a copy to '<filepath>.bak'.
        encoding: File encoding (default 'utf-8').
    """
    # TODO: Resolve directory and ensure parent directories exist
    # TODO: Create temp file in same directory (to ensure same filesystem mount)
    # TODO: Write content, flush, and os.fsync
    # TODO: If make_backup and target exists, copy to .bak
    # TODO: Use os.replace(temp_path, filepath)
    # TODO: Clean up temp file in finally block if still present
    raise NotImplementedError("TODO: Implement atomic_write_file")


class AtomicFileWriter:
    """Context manager for atomic file writing."""

    def __init__(self, filepath: str, make_backup: bool = False, encoding: str = "utf-8"):
        self.filepath = filepath
        self.make_backup = make_backup
        self.encoding = encoding
        self._temp_file = None
        self._temp_path = None

    def __enter__(self):
        # TODO: Open temporary file and return file object
        raise NotImplementedError("TODO: Implement __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: If exc_type is None, flush, fsync, close, and os.replace to self.filepath
        # TODO: If exception occurred, close and delete temp file without touching target
        raise NotImplementedError("TODO: Implement __exit__")
''',
        "test_code": '''import os
import shutil
import tempfile
import unittest
from solution import atomic_write_file, AtomicFileWriter


class TestAtomicFileWriter(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.target_file = os.path.join(self.test_dir, "config.json")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_atomic_write_creates_file(self):
        atomic_write_file(self.target_file, '{"version": 1}')
        self.assertTrue(os.path.exists(self.target_file))
        with open(self.target_file, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), '{"version": 1}')

    def test_atomic_write_with_backup(self):
        atomic_write_file(self.target_file, "original content")
        atomic_write_file(self.target_file, "updated content", make_backup=True)

        backup_file = self.target_file + ".bak"
        self.assertTrue(os.path.exists(backup_file))
        with open(backup_file, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "original content")
        with open(self.target_file, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "updated content")

    def test_context_manager_aborts_on_error(self):
        atomic_write_file(self.target_file, "safe content")
        try:
            with AtomicFileWriter(self.target_file) as f:
                f.write("corrupted partial write")
                raise RuntimeError("Simulated crash")
        except RuntimeError:
            pass

        # Original content must remain intact
        with open(self.target_file, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "safe content")


if __name__ == "__main__":
    unittest.main()
'''
    },

    # =========================================================================
    # 6. Algorithms & Data Structures: LRU Cache
    # =========================================================================
    {
        "id": "algo-lru-cache",
        "title": "LRU (Least Recently Used) Cache Implementation",
        "category": "Algorithms & Data Structures",
        "difficulty": "Intermediate",
        "readme": """# LRU (Least Recently Used) Cache

## Background
An LRU Cache organizes items in order of use. When the capacity is reached, the least recently accessed item is evicted.
Both `get` and `put` operations must execute in O(1) average time complexity.

## Requirements
Implement `LRUCache` in `solution.py`:
1. `__init__(capacity: int)`: Initializes cache with given maximum capacity (`capacity > 0`).
2. `get(key: Any) -> Any`:
   - Returns the value associated with `key` if present.
   - Marks `key` as most recently used.
   - Returns `-1` (or `None` / default) if key not found.
3. `put(key: Any, value: Any) -> None`:
   - Inserts or updates key-value pair.
   - Marks key as most recently used.
   - If capacity is exceeded, evicts the least recently used key.
4. `__len__()`: Returns current number of items.
5. `keys() -> list`: Returns keys from least to most recently used.

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: LRU (Least Recently Used) Cache
"""
from collections import OrderedDict
from typing import Any, List, Optional


class LRUCache:
    """
    O(1) time complexity Least Recently Used (LRU) Cache.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive integer.")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: Any, default: Any = -1) -> Any:
        """
        Get value for key and mark as most recently used.
        """
        # TODO: Check if key exists in self.cache
        # TODO: Move key to end (most recently used)
        # TODO: Return value or default
        raise NotImplementedError("TODO: Implement LRUCache.get")

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update key-value pair. Evict LRU item if capacity exceeded.
        """
        # TODO: If key exists, update and move to end
        # TODO: If key is new and len == capacity, popitem(last=False) (evict LRU)
        # TODO: Store new key-value pair at end
        raise NotImplementedError("TODO: Implement LRUCache.put")

    def __len__(self) -> int:
        return len(self.cache)

    def keys(self) -> List[Any]:
        return list(self.cache.keys())
''',
        "test_code": '''import unittest
from solution import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_basic_put_get(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        self.assertEqual(cache.get("c"), -1)

    def test_eviction_order(self):
        cache = LRUCache(2)
        cache.put(1, "one")
        cache.put(2, "two")
        # Access 1 -> makes 2 the LRU item
        cache.get(1)
        # Insert 3 -> evicts 2
        cache.put(3, "three")
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), "one")
        self.assertEqual(cache.get(3), "three")

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put("x", 10)
        cache.put("y", 20)
        cache.put("x", 99)  # Update x
        cache.put("z", 30)  # Evicts y (because x was updated and is now recent)
        self.assertEqual(cache.get("y"), -1)
        self.assertEqual(cache.get("x"), 99)
        self.assertEqual(cache.get("z"), 30)


if __name__ == "__main__":
    unittest.main()
'''
    },

    # =========================================================================
    # 7. GS1 / Barcode: Code 128 Checksum & Encoded Barcode Validator
    # =========================================================================
    {
        "id": "gs1-code128-checksum",
        "title": "Code 128 Modulo-103 Checksum Calculator",
        "category": "GS1 / Barcode Utilities",
        "difficulty": "Intermediate",
        "readme": """# Code 128 Modulo-103 Checksum Calculator

## Background
Code 128 is a high-density alphanumeric barcode standard used worldwide.
It uses a weighted Modulo-103 check character algorithm:
- `Sum = StartCodeValue + (Position_1 * CharValue_1) + (Position_2 * CharValue_2) + ...`
- `CheckValue = Sum % 103`

## Requirements
Implement in `solution.py`:
1. `calculate_code128_checksum(start_code: int, char_values: list[int]) -> int`:
   - `start_code`: 103 (Code A), 104 (Code B), or 105 (Code C).
   - Weights for each character value are `1, 2, 3, 4, ...` (1-indexed position).
   - Returns `(start_code + sum(i * val for i, val in enumerate(char_values, 1))) % 103`.
2. `encode_code128_b_values(text: str) -> tuple[int, list[int], int]`:
   - Starts with Start B (104).
   - Converts standard ASCII characters (ASCII 32 to 126) to Code 128 values (`ASCII - 32`).
   - Calculates check value.
   - Returns `(104, char_values, check_value)`.

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: Code 128 Modulo-103 Checksum Calculator
"""
from typing import List, Tuple

START_CODE_A = 103
START_CODE_B = 104
START_CODE_C = 105
STOP_CODE = 106


def calculate_code128_checksum(start_code: int, char_values: List[int]) -> int:
    """
    Calculate Code 128 Modulo-103 checksum value.
    
    Formula: (start_code + sum(position * value for position, value in 1..N)) % 103
    """
    # TODO: Calculate weighted sum: start_code + sum((idx + 1) * val for idx, val in enumerate(char_values))
    # TODO: Return weighted_sum % 103
    raise NotImplementedError("TODO: Implement calculate_code128_checksum")


def encode_code128_b_values(text: str) -> Tuple[int, List[int], int]:
    """
    Convert ASCII text (32-126) to Code 128 Set B values and compute checksum.
    
    Returns:
        Tuple of (start_code_104, list_of_char_values, checksum_value)
    """
    # TODO: Validate text contains ASCII 32 to 126
    # TODO: Map each char to (ord(c) - 32)
    # TODO: Compute checksum with START_CODE_B (104)
    # TODO: Return (104, char_values, checksum)
    raise NotImplementedError("TODO: Implement encode_code128_b_values")
''',
        "test_code": '''import unittest
from solution import calculate_code128_checksum, encode_code128_b_values, START_CODE_B


class TestCode128(unittest.TestCase):
    def test_known_checksum(self):
        # Text: 'Code 128' in Set B
        # Start B = 104
        # 'C'(35), 'o'(79), 'd'(68), 'e'(69), ' '(0), '1'(17), '2'(18), '8'(24)
        start, values, check = encode_code128_b_values("Code 128")
        self.assertEqual(start, 104)
        self.assertEqual(values, [35, 79, 68, 69, 0, 17, 18, 24])
        # Weighted sum: 104 + (1*35) + (2*79) + (3*68) + (4*69) + (5*0) + (6*17) + (7*18) + (8*24) = 1198
        # 1198 % 103 = 65
        self.assertEqual(check, 65)

    def test_single_char(self):
        start, values, check = encode_code128_b_values("A")
        # 'A' = 33 -> 104 + (1 * 33) = 137 % 103 = 34
        self.assertEqual(check, 34)


if __name__ == "__main__":
    unittest.main()
'''
    },

    # =========================================================================
    # 8. Algorithms & Data Structures: Prefix Tree (Trie) Autocomplete
    # =========================================================================
    {
        "id": "algo-trie-autocomplete",
        "title": "Trie (Prefix Tree) for Fast Autocomplete",
        "category": "Algorithms & Data Structures",
        "difficulty": "Intermediate",
        "readme": """# Trie (Prefix Tree) for Fast Autocomplete

## Background
A Trie is an efficient search tree used for prefix matching, spell-checkers, and search engine autocomplete suggestions.

## Requirements
Implement `TrieNode` and `Trie` in `solution.py`:
1. `insert(word: str) -> None`: Inserts a word into the trie (case-insensitive).
2. `search(word: str) -> bool`: Returns `True` if the exact word exists in the trie.
3. `starts_with(prefix: str) -> bool`: Returns `True` if any word starts with `prefix`.
4. `autocomplete(prefix: str, limit: int = 5) -> list[str]`: Returns up to `limit` words starting with `prefix` in alphabetical order.

## Run Tests
```bash
python test_solution.py
```
""",
        "solution_scaffold": '''"""
Day Challenge: Trie (Prefix Tree) for Fast Autocomplete
"""
from typing import Dict, List, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert lowercase word into the Trie."""
        # TODO: Iterate chars, add child nodes as needed, mark last node is_end_of_word = True
        raise NotImplementedError("TODO: Implement insert")

    def search(self, word: str) -> bool:
        """Return True if word exists in Trie."""
        # TODO: Traverse nodes, return True if final node is_end_of_word is True
        raise NotImplementedError("TODO: Implement search")

    def starts_with(self, prefix: str) -> bool:
        """Return True if there is any word with the given prefix."""
        # TODO: Traverse prefix nodes, return True if prefix exists
        raise NotImplementedError("TODO: Implement starts_with")

    def autocomplete(self, prefix: str, limit: int = 5) -> List[str]:
        """Return list of up to `limit` words that start with `prefix`."""
        # TODO: Find prefix node
        # TODO: DFS/recursion to collect all words starting from prefix node
        # TODO: Return top `limit` results sorted alphabetically
        raise NotImplementedError("TODO: Implement autocomplete")
''',
        "test_code": '''import unittest
from solution import Trie


class TestTrieAutocomplete(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        words = ["python", "pytorch", "pyspark", "pyramid", "algorithm", "algo", "apple", "app"]
        for w in words:
            self.trie.insert(w)

    def test_search(self):
        self.assertTrue(self.trie.search("python"))
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("py"))
        self.assertFalse(self.trie.search("banana"))

    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("py"))
        self.assertTrue(self.trie.starts_with("alg"))
        self.assertFalse(self.trie.starts_with("cat"))

    def test_autocomplete(self):
        results = self.trie.autocomplete("py", limit=3)
        self.assertEqual(len(results), 3)
        self.assertEqual(results, ["pyramid", "pyspark", "python"])


if __name__ == "__main__":
    unittest.main()
'''
    }
]


def get_exercise_by_day(day_number: int) -> dict:
    """
    Returns exercise definition for a given day number (1-indexed).
    Cycles through the exercise bank via round-robin.
    """
    index = (day_number - 1) % len(EXERCISES)
    return EXERCISES[index]
