"""
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
