import unittest
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
        # AI 01 (fixed 14) + AI 17 (fixed 6) + AI 10 (var, ended with \x1d) + AI 21 (var)
        raw = "01000123456789051726123110LOT42\x1d21SER999"
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
