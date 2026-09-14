"""
Day Challenge: LRU (Least Recently Used) Cache
"""
from collections import OrderedDict
from typing import Any, List, Optional


class LRUCache:
    """
    O(1) time complexity Least Recently Used (LRU) Cache.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive integer.")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: Any, default: Any = -1) -> Any:
        """
        Get value for key and mark as most recently used.
        """
        # TODO: Check if key exists in self.cache
        # TODO: Move key to end (most recently used)
        # TODO: Return value or default
        raise NotImplementedError("TODO: Implement LRUCache.get")

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update key-value pair. Evict LRU item if capacity exceeded.
        """
        # TODO: If key exists, update and move to end
        # TODO: If key is new and len == capacity, popitem(last=False) (evict LRU)
        # TODO: Store new key-value pair at end
        raise NotImplementedError("TODO: Implement LRUCache.put")

    def __len__(self) -> int:
        return len(self.cache)

    def keys(self) -> List[Any]:
        return list(self.cache.keys())
