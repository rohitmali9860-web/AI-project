# Day 016: Trie (Prefix Tree) for Fast Autocomplete

- **Date:** 2026-08-30
- **Category:** Algorithms & Data Structures
- **Difficulty:** Intermediate

---

# Trie (Prefix Tree) for Fast Autocomplete

## Background
A Trie is an efficient search tree used for prefix matching, spell-checkers, and search engine autocomplete suggestions.

## Requirements
Implement `TrieNode` and `Trie` in `solution.py`:
1. `insert(word: str) -> None`: Inserts a word into the trie (case-insensitive).
2. `search(word: str) -> bool`: Returns `True` if the exact word exists in the trie.
3. `starts_with(prefix: str) -> bool`: Returns `True` if any word starts with `prefix`.
4. `autocomplete(prefix: str, limit: int = 5) -> list[str]`: Returns up to `limit` words starting with `prefix` in alphabetical order.

## Run Tests
```bash
python test_solution.py
```
