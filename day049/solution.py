"""
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
