# Day 006: LRU (Least Recently Used) Cache Implementation

- **Date:** 2026-08-20
- **Category:** Algorithms & Data Structures
- **Difficulty:** Intermediate

---

# LRU (Least Recently Used) Cache

## Background
An LRU Cache organizes items in order of use. When the capacity is reached, the least recently accessed item is evicted.
Both `get` and `put` operations must execute in O(1) average time complexity.

## Requirements
Implement `LRUCache` in `solution.py`:
1. `__init__(capacity: int)`: Initializes cache with given maximum capacity (`capacity > 0`).
2. `get(key: Any) -> Any`:
   - Returns the value associated with `key` if present.
   - Marks `key` as most recently used.
   - Returns `-1` (or `None` / default) if key not found.
3. `put(key: Any, value: Any) -> None`:
   - Inserts or updates key-value pair.
   - Marks key as most recently used.
   - If capacity is exceeded, evicts the least recently used key.
4. `__len__()`: Returns current number of items.
5. `keys() -> list`: Returns keys from least to most recently used.

## Run Tests
```bash
python test_solution.py
```
