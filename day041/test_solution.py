import unittest
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
