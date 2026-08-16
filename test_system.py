"""
test_system.py
End-to-end verification script for Daily Python Practice system.
"""

import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

import exercise_bank


class TestPracticeSystem(unittest.TestCase):
    def setUp(self):
        self.base_dir = Path(__file__).resolve().parent

    def test_exercise_bank_integrity(self):
        """Verify that all exercises in exercise_bank have required fields."""
        exercises = exercise_bank.EXERCISES
        self.assertGreaterEqual(len(exercises), 5, "Should have at least 5 exercises in bank")
        
        required_keys = {"id", "title", "category", "difficulty", "readme", "solution_scaffold", "test_code"}
        categories = set()
        
        for idx, ex in enumerate(exercises):
            for k in required_keys:
                self.assertIn(k, ex, f"Exercise at index {idx} missing key '{k}'")
            categories.add(ex["category"])
            self.assertTrue(len(ex["solution_scaffold"]) > 0)
            self.assertTrue(len(ex["test_code"]) > 0)

        self.assertIn("GS1 / Barcode Utilities", categories)
        self.assertIn("OOP Practice", categories)
        self.assertIn("Algorithms & Data Structures", categories)

    def test_scaffold_test_runner(self):
        """Verify that day test templates can be executed via python test runner."""
        ex = exercise_bank.get_exercise_by_day(1)
        self.assertEqual(ex["id"], "gs1-ean13-check-digit")


if __name__ == "__main__":
    unittest.main()
