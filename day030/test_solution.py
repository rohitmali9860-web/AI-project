import unittest
from solution import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_basic_put_get(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        self.assertEqual(cache.get("c"), -1)

    def test_eviction_order(self):
        cache = LRUCache(2)
        cache.put(1, "one")
        cache.put(2, "two")
        # Access 1 -> makes 2 the LRU item
        cache.get(1)
        # Insert 3 -> evicts 2
        cache.put(3, "three")
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), "one")
        self.assertEqual(cache.get(3), "three")

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put("x", 10)
        cache.put("y", 20)
        cache.put("x", 99)  # Update x
        cache.put("z", 30)  # Evicts y (because x was updated and is now recent)
        self.assertEqual(cache.get("y"), -1)
        self.assertEqual(cache.get("x"), 99)
        self.assertEqual(cache.get("z"), 30)


if __name__ == "__main__":
    unittest.main()
