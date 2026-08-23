# Day 009: EAN-13 & UPC-A Check Digit Calculator

- **Date:** 2026-08-23
- **Category:** GS1 / Barcode Utilities
- **Difficulty:** Beginner

---

# EAN-13 & UPC-A Check Digit Calculator

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
