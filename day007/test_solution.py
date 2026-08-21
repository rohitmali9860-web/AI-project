import unittest
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
