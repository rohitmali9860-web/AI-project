import os
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
