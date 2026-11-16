import unittest
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
