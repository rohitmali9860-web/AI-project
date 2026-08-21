# Day 007: Code 128 Modulo-103 Checksum Calculator

- **Date:** 2026-08-21
- **Category:** GS1 / Barcode Utilities
- **Difficulty:** Intermediate

---

# Code 128 Modulo-103 Checksum Calculator

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
